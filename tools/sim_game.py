#!/usr/bin/env python3
"""Whole-game Monte Carlo model of the standard game, for tuning enemy scaling against sparks.

It plays the settled ruleset (41_rules_workshop.md, section 9.6) from the first bonfire to the main boss:
four encounters (Levels 1, 1, 2, 2), the mini-boss, four more (Levels 2, 2, 3, 3), the main boss.

What is modelled
  - Round: all enemies act, then every character acts. Bosses act after each character's turn.
  - Endurance bar of ten spaces shared by stamina and damage (eight when hollow); a character dies when damage
    has no space. One stamina back each turn. Light and heavy attacks, the Rest action, the estus flask.
  - Aggro: the last character to deal damage. Half of enemy attacks go to the aggro holder, half to a random
    living character. A boss attacks the aggro holder.
  - Death and hollowing: a dead character is revived hollow if the encounter is cleared; an encounter fails if
    every character dies or a hollow character dies; a failure forces a rest.
  - Sparks: six minus the number of characters; +1 for each boss; a rest costs one, restores everything and
    resets the encounters; the rest after a boss is free. The game is lost when a rest is forced at zero sparks.
  - Recovery after a clear: all stamina, one damage cube.
  - Skipping cleared encounters after a rest: two stamina each (at most three skipped, the rest is the walk in).
    A boss already reached is entered through the fog gate.
  - Progression: souls per character (3/4/5 for Levels 1/2/3, 6 for a boss), spent at a rest; a character's
    dice improve at 6, 16 and 30 souls earned. A lone character starts with six souls.
  - Enemy scaling: the rule under test (health and attack bonus by number of characters).

What is not modelled: movement and range (a fixed share of enemy attacks comes to nothing), dodging, parrying,
conditions, luck and heroic actions, individual classes and cards, treasure choice, invaders, mimics. The
players follow one fixed, sensible policy. The model is for comparing scaling rules with each other across
player counts. It is not a forecast of a real table.

Usage:
  python3 tools/sim_game.py                 # the candidate rules, 1 to 4 characters
  python3 tools/sim_game.py --reach 0.34    # an easier table (0.42: a harder one)
  python3 tools/sim_game.py --games 5000
"""
import argparse, random, statistics as st

B = [0, 1, 1, 1, 2, 2]; U = [1, 1, 2, 2, 2, 3]; O = [1, 2, 2, 3, 3, 4]
LIGHT = [(B, B), (B, U), (U, U), (U, O)]                 # attack dice by progression tier, cost 1 stamina
HEAVY = [(B, B, B), (B, U, U), (U, U, O), (U, O, O)]     # cost 3 stamina
BLOCK = [(B, B, B), (B, B, U), (B, U, U), (U, U, O)]     # two highest count
UPGRADE = (0, 0, 1, 2)                                   # flat bonus on each attack by tier (weapon upgrades)
TIER_AT = (6, 16, 30)                                    # souls earned per character for tiers 1, 2, 3
# (health, block, attack value) of a typical encounter of each level
MIX = {1: [(1, 1, 4), (1, 1, 4), (1, 0, 3)],
       2: [(1, 1, 4), (1, 1, 4), (1, 0, 3), (5, 1, 5), (5, 2, 5)],
       3: [(5, 2, 5), (5, 2, 5), (5, 1, 5), (5, 1, 5), (10, 2, 6)]}
SOULS = {1: 3, 2: 4, 3: 5, 'boss': 6}
BOSS = {'mini': dict(hp=24, block=1, atk=5, heat=12), 'main': dict(hp=36, block=2, atk=6, heat=18)}
REACH, REACH_BOSS = 0.39, 0.62                           # share of enemy and boss attacks that connect
ROUTE = [1, 1, 2, 2, 'mini', 2, 2, 3, 3, 'main']


def roll(dice): return sum(random.choice(d) for d in dice)
def block(t):   return sum(sorted(random.choice(d) for d in BLOCK[t])[-2:])


class Char:
    def __init__(self, souls=0):
        self.souls = souls; self.tier = 0; self.full_rest()
    def cap(self): return 8 if self.hollow else 10
    def full_rest(self):
        self.dmg = 0; self.sta = 0; self.hollow = False; self.alive = True; self.estus = True
        self.tier = sum(self.souls >= x for x in TIER_AT)
    def hurt(self, d):
        if d <= 0 or not self.alive: return
        if self.dmg + self.sta + d > self.cap():
            # damage needs space: stamina cubes do not make room
            self.alive = self.dmg + d <= self.cap() - self.sta
        if self.alive: self.dmg += d
    def act(self, target_block):
        """One character turn: up to one attack with each hand. Returns the damage dealt (0 if the turn went
        on resting or drinking)."""
        self.sta = max(0, self.sta - 1)
        free = self.cap() - self.dmg - self.sta
        if self.estus and self.dmg >= 5:
            self.estus = False; self.dmg = 0; return 0
        if self.sta >= 5 or free <= 2:
            self.sta = 0; return 0                        # the Rest action
        hit = lambda dice: max(0, roll(dice) + UPGRADE[self.tier] - target_block)
        if free >= 7:
            self.sta += 4; return hit(HEAVY[self.tier]) + hit(LIGHT[self.tier])
        if free >= 5:
            self.sta += 2; return hit(LIGHT[self.tier]) + hit(LIGHT[self.tier])
        self.sta += 1; return hit(LIGHT[self.tier])


def fight(party, level, rule, stats=None, start_sta=0):
    """Play one encounter or boss fight. Returns True if cleared."""
    n = len(party)
    for c in party:
        c.alive = True; c.sta = min(start_sta, c.cap() - c.dmg - 1) if start_sta else c.sta
    live = lambda: [c for c in party if c.alive]
    failed = lambda: not live() or any(c.hollow and not c.alive for c in party)
    aggro = random.choice(party); rounds = 0; turns = 0
    if level in BOSS:
        b = BOSS[level]; hp = b['hp']
        while hp > 0 and not failed() and rounds < 80:
            rounds += 1
            for c in list(party):
                # the boss acts, then one character; a dead character takes no turn and earns the boss none
                if not c.alive: continue
                if not aggro.alive and live(): aggro = random.choice(live())
                if random.random() < REACH_BOSS and live():
                    aggro.hurt(max(0, b['atk'] + (1 if hp <= b['heat'] else 0) - block(aggro.tier)))
                turns += 1
                if failed() or hp <= 0: break
                if c.alive:                               # the boss may have just killed this character
                    d = c.act(b['block']); turns += 1
                    if d: hp -= d; aggro = c
        ok = hp <= 0 and not failed()
    else:
        en = [[rule['hp'](h, n), bl, a + rule['atk'](n)] for h, bl, a in MIX[level]]
        while any(e[0] > 0 for e in en) and not failed() and rounds < 80:
            rounds += 1
            for e in en:
                for _ in range(rule['reps_by'](n) if 'reps_by' in rule else rule.get('reps', 1)):
                    if e[0] <= 0 or not live(): continue
                    turns += 1
                    if random.random() > REACH: continue
                    if not aggro.alive: aggro = random.choice(live())
                    t = aggro if random.random() < 0.5 else random.choice(live())
                    t.hurt(max(0, e[2] - block(t.tier)))
            if failed(): break
            order = live(); random.shuffle(order)
            for c in order:
                tg = [e for e in en if e[0] > 0]
                if not tg: break
                e = min(tg, key=lambda e: e[0]); d = c.act(e[1]); turns += 1
                if d: e[0] -= d; aggro = c
        ok = not any(e[0] > 0 for e in en) and not failed()
    if stats is not None:
        stats.setdefault(('rounds', level), []).append(rounds)
        stats.setdefault(('death', level), []).append(any(not c.alive for c in party))
        stats['turns'] = stats.get('turns', 0) + turns; stats['rounds_total'] = stats.get('rounds_total', 0) + rounds
        stats['fights'] = stats.get('fights', 0) + 1
    return ok


def game(n, rule, stats):
    party = [Char(rule.get('souls', lambda n: 6 if n == 1 else 0)(n)) for _ in range(n)]
    for c in party: c.full_rest()
    sparks = rule.get('sparks', lambda n: 6 - n)(n); pos = 0; cleared = set(); rests = 0; walk = 0
    def rest(free=False):
        nonlocal sparks, rests
        if not free:
            if sparks == 0: return False
            sparks -= 1; rests += 1
        for c in party: c.full_rest()
        return True
    def walk_back():
        """After a rest the party walks out again: two stamina for each cleared encounter skipped (at most
        three). A boss already reached is entered through the fog gate at no cost."""
        if ROUTE[pos] in BOSS: return 0
        leg = 0 if pos <= 4 else 5
        return 2 * min(3, sum(1 for i in range(leg, pos) if i in cleared))
    while pos < len(ROUTE):
        lv = ROUTE[pos]
        # a voluntary rest before the next fight: someone is hollow or badly hurt, and a spark can be spared
        worn = any(c.hollow for c in party) or max(c.dmg for c in party) >= 5
        if worn and (sparks >= 2 or (sparks == 1 and lv in BOSS)):
            rest(); walk = walk_back()
        ok = fight(party, lv, rule, stats, start_sta=walk); walk = 0
        if ok:
            for c in party:
                if pos not in cleared: c.souls += SOULS['boss' if lv in BOSS else lv]
                if not c.alive: c.alive = True; c.hollow = True; c.dmg = 0
                else: c.dmg = max(0, c.dmg - 1)
                c.sta = 0
            cleared.add(pos); pos += 1
            if lv in BOSS:
                sparks += 1; rest(free=True)
        else:
            if not rest():
                stats.setdefault('result', []).append((False, rests, pos)); return
            walk = walk_back()
    stats.setdefault('result', []).append((True, rests, pos - 1))


import math
PLUS = lambda k: (lambda h, n: h + k * (n - 1))                     # +k health for each character beyond the first
HALF = lambda h, n: math.ceil(h * (1 + 0.5 * (n - 1)))               # half again for each character beyond the first
RULES = {
    'calibrated: +1 attack per character beyond the first, +2 health per character beyond the second':
        dict(hp=lambda h, n: h + 2 * max(0, n - 2), atk=lambda n: n - 1),
    'one-line alternative: +1 health and +1 attack per character beyond the first': dict(hp=PLUS(1), atk=lambda n: n - 1),
    'round four: +1 health each, +1 attack at three or more': dict(hp=PLUS(1), atk=lambda n: 1 if n >= 3 else 0),
    'manuscript: +1 health each, +1 attack at three, attacks repeated at four':
        dict(hp=PLUS(1), atk=lambda n: 1 if n >= 3 else 0, reps_by=lambda n: 2 if n >= 4 else 1),
    'health multiplied by the number of characters (Faded Embers)': dict(hp=lambda h, n: h * n, atk=lambda n: 0),
    'no scaling': dict(hp=PLUS(0), atk=lambda n: 0),
}


def report(name, rule, games):
    print(f'\n{name}')
    print('  chars sparks  win    L3 rounds  L3 death  rests  fights  rounds  table time   lost at (enc / mini / main)')
    out = {}
    for n in (1, 2, 3, 4):
        s = {}
        for _ in range(games): game(n, rule, s)
        res = s['result']; win = st.mean(r[0] for r in res)
        lost = [ROUTE[r[2]] for r in res if not r[0]]
        where = (sum(1 for x in lost if x not in BOSS), lost.count('mini'), lost.count('main'))
        l3 = s.get(('rounds', 3), [0]); d3 = s.get(('death', 3), [0])
        print(f"    {n}     {6 - n}    {100 * win:4.0f}%    {st.mean(l3):5.1f}     {100 * st.mean(d3):4.0f}%    {st.mean(r[1] for r in res):4.1f}   {s['fights'] / games:5.1f}   {s['rounds_total'] / games:5.0f}   {s['turns'] / games:6.0f}        "
              f"{100 * where[0] / games:3.0f}% / {100 * where[1] / games:3.0f}% / {100 * where[2] / games:3.0f}%")
        out[n] = (win, st.mean(l3), s['turns'] / games)
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--games', type=int, default=3000); ap.add_argument('--reach', type=float)
    a = ap.parse_args(); random.seed(1)
    if a.reach: REACH = a.reach; globals()['REACH'] = a.reach
    for name, rule in RULES.items(): report(name, rule, a.games)
