#!/usr/bin/env python3
"""A whole standard game for the rules simulator: bonfire, four encounters, the mini-boss, four more encounters,
the main boss, under any ruleset of rules.py. Returns what happened, for the tables in 41_rules_workshop.md."""
import random
from engine import Fight, Policy, ENCOUNTERS, BOSSES, ENEMIES
from characters import Char, Economy, CORE4

MINIS = [b for b, v in BOSSES.items() if v['kind'] == 'mini']
MAINS = [b for b, v in BOSSES.items() if v['kind'] == 'main']


class Table(Policy):
    """How the simulated players run the campaign side of the game."""
    reserve = 1          # sparks kept back for another try at a boss before any voluntary rest
    ready2 = -9.0        # party strength (mean `power`) wanted before a Level 2 encounter or the mini-boss; below it,
    ready3 = -9.0        # the same before a Level 3 encounter or the main boss: rest to grind or to spend souls
    worn_at = 5          # damage on any one character that justifies a rest between encounters


def danger(names): return sum(ENEMIES[n]['hp'] * max(s.get('dmg', 0) for s in ENEMIES[n]['steps']) for n in names)


def play(n, rules, seed, table=None, classes=None):
    rng = random.Random(seed); r = rules; t = table or Table()
    # players pick their classes: a lone character is a Knight or a Warrior; a pair includes one of them
    cls = classes or ([rng.choice(CORE4[:2])] if n == 1 else rng.sample(CORE4, n))
    if n == 2 and not classes and not set(cls) & set(CORE4[:2]): cls[0] = rng.choice(CORE4[:2])
    party = [Char(c, r) for c in cls]; eco = Economy(party, r, rng)
    if n == 1:
        if r.pool: eco.pool = r.solo_souls
        else: party[0].souls = r.solo_souls
    for c in party: c.dropped = None
    sparks = r.sparks(n)
    eco.spend()                                            # the party starts at the bonfire
    out = dict(win=False, rests=0, fights=0, char_turns=0, enemy_acts=0, rounds=0, lost_at=None, deaths=0,
               by_level={}, sparks_left=0, souls=0)
    decks = {lv: rng.sample(ENCOUNTERS[str(lv)], len(ENCOUNTERS[str(lv)])) for lv in (1, 2, 3)}
    dropped_pool = None                                   # official: the cache lies on the tile where the party fell

    def spend():
        eco.spend()

    def rest(free=False):
        nonlocal sparks
        if not free:
            if sparks <= 0: return False
            sparks -= 1; out['rests'] += 1
        for c in party: c.full_rest()
        spend(); return True

    for stage, boss in enumerate((rng.choice(MINIS), rng.choice(MAINS))):
        levels = BOSSES[boss]['levels']; cards = []
        for lv in levels:
            a = decks[lv].pop()
            if getattr(r, 'choose_of_two', False) and decks[lv]:
                b = decks[lv].pop(); a, b = sorted((a, b), key=lambda e: danger(e['enemies'])); decks[lv].append(b)
            cards.append(a)
        ever = [False] * 4; done = [False] * 4; boss_seen = False; pos = 0; walk = 0; fresh = True
        while True:
            at_boss = pos >= 4
            # ---- a voluntary rest before the next fight
            want = False
            if sparks > t.reserve and not fresh:
                worn = any(c.hollow for c in party) or max(c.dmg for c in party) >= t.worn_at \
                    or sum(not c.estus for c in party) * 2 > n
                lvl = ('mini' if stage == 0 else 'main') if at_boss else levels[pos]
                goal = t.ready3 if lvl in (3, 'main') else t.ready2 if lvl in (2, 'mini') else -99
                weak = sum(c._power for c in party) / n < goal
                # a rest helps a weak party only if it can then earn or spend souls
                can_grow = (r.skip_cost is None and pos > 0) or (eco.pool if r.pool else sum(c.souls for c in party)) >= 2 * n
                if worn and (r.death == 'hollow' or at_boss) and (at_boss or sparks > t.reserve + 1): want = True
                if weak and can_grow: want = True
            if want and not fresh:
                rest(); done = [False] * 4; fresh = True
                if r.skip_cost is None or not r.fog_gate: pos = 0
                else: pos = 4 if boss_seen else 0
                walk = 0
                continue
            if getattr(r, 'free_visit', False): spend()     # 2017: Andre and the Firekeeper can be visited between encounters
            # ---- walk to the next fight
            if not at_boss and r.skip_cost is not None and ever[pos] and not done[pos]:
                walk += r.skip_cost; done[pos] = True; pos += 1; continue        # skip a cleared encounter
            if not at_boss and done[pos]: pos += 1; continue
            for c in party:
                c.sta = min(walk, c.cap - c.dmg - 1) if walk else c.sta
            walk = 0
            if at_boss:
                boss_seen = True; f = Fight(party, r, rng, boss=boss, policy=t); lv = 'mini' if stage == 0 else 'main'
            else:
                f = Fight(party, r, rng, enemies=cards[pos]['enemies'], policy=t); lv = levels[pos]
            ok = f.run(); fresh = False
            out['fights'] += 1; out['char_turns'] += f.char_turns; out['enemy_acts'] += f.enemy_acts; out['rounds'] += f.rounds
            out['deaths'] += f.deaths
            d = out['by_level'].setdefault(lv, dict(n=0, rounds=0, death=0, fail=0, turns=0))
            d['n'] += 1; d['rounds'] += f.rounds; d['death'] += f.deaths > 0; d['fail'] += not ok; d['turns'] += f.char_turns + f.enemy_acts
            if ok:
                first = at_boss or not ever[pos]
                # ---- souls
                if r.pool:
                    if dropped_pool and dropped_pool[0] == (stage, pos): eco.pool += dropped_pool[1]; dropped_pool = None
                    eco.pool += r.boss_souls(n, sparks) if at_boss else r.souls(lv, n, first)
                    out['souls'] += r.boss_souls(n, sparks) if at_boss else r.souls(lv, n, first)
                else:
                    for c in party:
                        if not c.alive:
                            c.dropped = ((stage, pos), c.souls); c.souls = 0
                        elif c.dropped and c.dropped[0] == (stage, pos):
                            c.souls += c.dropped[1]; c.dropped = None
                        gain = r.boss_souls(n, sparks) if at_boss else r.souls(lv, n, first)
                        c.souls += gain; c.earned += gain; out['souls'] += gain
                # ---- treasure
                if not at_boss and first:
                    k = r.free_treasure(lv, n); k = int(k) + (rng.random() < k - int(k))
                    cardsT = [eco.draw(1 if stage == 0 else 2) for _ in range(k * (n if r.treasure == 'author' else 1))]
                    eco.give(cardsT)
                # ---- recovery
                for c in party:
                    if not c.alive: c.alive = True; c.hollow = True; c.dmg = 0; c.sta = 0
                    elif r.recover == 'all': c.dmg = 0; c.sta = 0
                    else: c.dmg = max(0, c.dmg - getattr(r, 'heal_after', 1)); c.sta = 0
                    c.stagger = c.frost = c.bleed = False; c.poison = 0
                if at_boss: break
                ever[pos] = True; done[pos] = True; pos += 1
            else:
                # ---- a failed encounter: souls are dropped and the party must rest
                if r.pool:
                    dropped_pool = ((stage, pos), eco.pool); eco.pool = 0
                else:
                    for c in party:
                        c.dropped = ((stage, pos), c.souls); c.souls = 0
                if not rest():
                    out['lost_at'] = lv; out['sparks_left'] = 0; return out
                done = [False] * 4; fresh = True
                if not at_boss: ever[pos] = False                                  # a failed encounter cannot be skipped
                pos = 4 if (at_boss and r.fog_gate) else 0
        # ---- the boss is dead
        if stage == 0:
            sparks = r.sparks(n) if r.boss_spark == 'reset' else sparks + 1
            eco.after_mini_boss(); rest(free=True)
    out['win'] = True; out['sparks_left'] = sparks
    out['power'] = sum(c._power for c in party) / n
    return out
