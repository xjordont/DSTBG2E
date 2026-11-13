#!/usr/bin/env python3
"""Rough Monte Carlo comparison of round structures and enemy scaling for one to four characters.

A deliberately crude model: it is for comparing rules with each other, not for predicting a real table.
  - characters: ten-space bar (damage only), block = two highest of three black dice, attack = two black dice
    for one target a turn, always the weakest enemy standing;
  - enemies: (health, block, attack value) from a typical Level 2 mix; each attacks once per enemy phase, and
    half of those attacks come to nothing (out of reach, or dodged): the model is tuned so that a lone
    character dies in roughly a third of encounters under the published rules;
    half target the aggro holder and half a random living character ("nearest");
  - aggro: the last character to deal damage (the character who has just acted, in the alternating structure);
  - an encounter ends when every enemy or every character is dead.
Reports, per number of characters: rounds, damage taken per character, the worst-hit character's damage,
the chance that at least one character dies, and the chance of a wipe.
Usage: python3 tools/sim_scaling.py [trials]
"""
import random, sys, statistics as st
BLACK = [0, 1, 1, 1, 2, 2]
ENEMIES = [(1, 1, 4), (1, 1, 4), (1, 0, 3), (5, 1, 5), (5, 2, 5)]   # two soldiers, crossbow, large hollow, knight

def block():  return sum(sorted(random.choice(BLACK) for _ in range(3))[-2:])
REACH = 0.3      # share of enemy attacks that land on a target at all (movement, range, dodges)
BONUS = 3        # flat bonus on a character's attack
def attack(): return random.choice(BLACK) + random.choice(BLACK) + BONUS

def run(n, rule):
    hp_bonus = {'x': 0}.get(rule['hp'], None)
    en = []
    for h, b, a in ENEMIES:
        if rule['hp'] == 'plus':  h += n - 1
        elif rule['hp'] == 'times': h *= n
        elif rule['hp'] == 'plus2': h += 2 * (n - 1)
        a += rule['atk'](n)
        en.append([h, b, a])
    dmg = [0] * n; alive = [True] * n; aggro = 0; rounds = 0
    def enemy_phase(reps=1):
        nonlocal aggro
        for e in en:
            if e[0] <= 0: continue
            for _ in range(reps):
                live = [i for i in range(n) if alive[i]]
                if not live: return
                if not alive[aggro]: aggro = random.choice(live)
                if random.random() > REACH: continue
                t = aggro if random.random() < 0.5 else random.choice(live)
                d = max(0, e[2] - block()); dmg[t] += d
                if dmg[t] >= 10: alive[t] = False
    def char_turn(i):
        nonlocal aggro
        tg = [e for e in en if e[0] > 0]
        if not tg or not alive[i]: return
        e = min(tg, key=lambda e: e[0]); d = max(0, attack() - e[1])
        if d: e[0] -= d; aggro = i
    while any(e[0] > 0 for e in en) and any(alive) and rounds < 60:
        rounds += 1
        order = [i for i in range(n) if alive[i]]; random.shuffle(order)
        if rule['shape'] == 'alternate':            # the published game: enemies act after each character
            for i in order:
                if not alive[i]: continue           # killed earlier this round: no turn, and no enemy phase for it
                enemy_phase(); aggro = i if alive[i] else aggro; char_turn(i)
        elif rule['shape'] == 'pairs':              # enemies again after every second character
            k = 0
            for i in order:
                if not alive[i]: continue
                if k % 2 == 0: enemy_phase()
                char_turn(i); k += 1
        else:                                       # all enemies, then all characters
            enemy_phase(rule.get('reps', lambda n: 1)(n))
            for i in order: char_turn(i)
    return rounds, sum(dmg) / n, max(dmg), not all(alive), not any(alive)

RULES = {
 'published game (enemies after each character)': dict(shape='alternate', hp='none', atk=lambda n: 0),
 'all-then-all, no scaling':                      dict(shape='all', hp='none', atk=lambda n: 0),
 'manuscript (+1 hp each, +1 atk at 3, repeat at 4)': dict(shape='all', hp='plus', atk=lambda n: 1 if n >= 3 else 0, reps=lambda n: 2 if n >= 4 else 1),
 'numbers only (+1 hp each, +1 atk at 3+)':       dict(shape='all', hp='plus', atk=lambda n: 1 if n >= 3 else 0),
 'second phase after two characters (+1 hp each)': dict(shape='pairs', hp='plus', atk=lambda n: 0),
 'health x characters only':                      dict(shape='all', hp='times', atk=lambda n: 0),
 '+1 hp each, +1 atk per character beyond two':   dict(shape='all', hp='plus', atk=lambda n: max(0, n - 2)),
 '+1 hp each, +1 atk at 2+, +2 at 4':             dict(shape='all', hp='plus', atk=lambda n: 0 if n == 1 else 2 if n == 4 else 1),
 '+2 hp each, +1 atk at 3+':                      dict(shape='all', hp='plus2', atk=lambda n: 1 if n >= 3 else 0),
 '+1 hp each, nothing else':                      dict(shape='all', hp='plus', atk=lambda n: 0),
}
if __name__ == '__main__':
    T = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    random.seed(7)
    for name, rule in RULES.items():
        print(f'\n{name}')
        print('  chars rounds  dmg/char  worst-hit  P(any death)  P(wipe)')
        for n in (1, 2, 3, 4):
            R = [run(n, rule) for _ in range(T)]
            print(f'    {n}    {st.mean(r[0] for r in R):5.1f}   {st.mean(r[1] for r in R):6.2f}    {st.mean(r[2] for r in R):6.2f}      {100*st.mean(r[3] for r in R):5.1f}%     {100*st.mean(r[4] for r in R):5.1f}%')
