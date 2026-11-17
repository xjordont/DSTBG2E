#!/usr/bin/env python3
"""A whole standard game for the rules simulator: bonfire, four encounters, the mini-boss, four more encounters,
the main boss, under any ruleset of rules.py. Returns what happened, for the tables in 41_rules_workshop.md."""
import random
from engine import Fight, Policy, ENCOUNTERS, BOSSES, ENEMIES
from characters import Char, Economy, CORE4, ALL10

MINIS = [b for b, v in BOSSES.items() if v['kind'] == 'mini']
MAINS = [b for b, v in BOSSES.items() if v['kind'] == 'main']


def in_play(rules, what, card):
    """Whether a boss or an encounter card of this set is in the game: the core set's always, the others' where the
    ruleset says bosses='all' or encounters='all'."""
    return card.get('set', 'Core') == 'Core' or getattr(rules, what, 'core') == 'all'


class Table(Policy):
    """How the simulated players run the campaign side of the game."""
    reserve = 1          # sparks kept back for another try at a boss before any voluntary rest
    ready2 = -9.0        # party strength (mean `power`) wanted before a Level 2 encounter or the mini-boss; below it,
    ready3 = -9.0        # the same before a Level 3 encounter or the main boss: rest to grind or to spend souls
    worn_at = 5          # damage on any one character that justifies a rest between encounters
    grind = False        # fight a cleared encounter again where the rules let it be rushed past instead
    regrind = 0          # the highest level of reset encounter fought again while a repeat still pays (0 = always rush)
    bank = None          # rest to spend once the characters hold this many unspent souls each (where spending needs a rest)


def danger(names): return sum(ENEMIES[n]['hp'] * max(s.get('dmg', 0) for s in ENEMIES[n]['steps']) for n in names)


def play(n, rules, seed, table=None, classes=None):
    rng = random.Random(seed); r = rules; t = table or Table()
    # players pick their classes: a lone character is a Knight or a Warrior; a pair includes one of them
    # (with roster='all' any of the ten classes is as likely as any other, at every party size)
    if classes: cls = classes
    elif getattr(r, 'roster', 'core') == 'all': cls = rng.sample(ALL10, n)
    else:
        cls = [rng.choice(CORE4[:2])] if n == 1 else rng.sample(CORE4, n)
        if n == 2 and not set(cls) & set(CORE4[:2]): cls[0] = rng.choice(CORE4[:2])
    party = [Char(c, r) for c in cls]; eco = Economy(party, r, rng)
    if n == 1:
        if r.pool: eco.pool = r.solo_souls
        else: party[0].souls = r.solo_souls
    for c in party: c.dropped = None; c.lost = False
    sparks = r.sparks(n)
    # the party starts at the bonfire; souls held at setup may be spent there only where the ruleset allows a visit
    # without a rest (the manuscript as written does not: a lone character's six souls wait for the first rest)
    fv0 = getattr(r, 'free_visit', False)
    if fv0: eco.spend(levels=fv0 != 'shop')
    out = dict(win=False, rests=0, fights=0, char_turns=0, enemy_acts=0, rounds=0, lost_at=None, deaths=0,
               by_level={}, sparks_left=0, souls=0, repeats=0, dec={}, carried=0.0, souls_lost=0.0, classes=list(cls))
    decks = {}
    for lv in (1, 2, 3):
        pool = [e for e in ENCOUNTERS[str(lv)] if in_play(r, 'encounters', e)]; decks[lv] = rng.sample(pool, len(pool))
    dropped_pool = None                                   # official: the cache lies on the tile where the party fell

    def spend():
        eco.spend()

    def rest(free=False):
        nonlocal sparks
        if not free:
            if sparks <= 0: return False
            sparks -= 1; out['rests'] += 1
        for c in party: c.full_rest(); c.lost = False
        eco.renew_row(); spend(); return True

    for stage, boss in enumerate((rng.choice([b for b in MINIS if in_play(r, 'bosses', BOSSES[b])]),
                                  rng.choice([b for b in MAINS if in_play(r, 'bosses', BOSSES[b])]))):
        levels = BOSSES[boss]['levels']; cards = []; eco.boss_named(boss, stage)
        out['mini' if stage == 0 else 'main'] = boss
        for lv in levels:
            a = decks[lv].pop()
            if getattr(r, 'choose_of_two', False) and decks[lv]:
                b = decks[lv].pop(); a, b = sorted((a, b), key=lambda e: danger(e['enemies'])); decks[lv].append(b)
            cards.append(a)
        clears = [0] * 4; must = [False] * 4; done = [False] * 4; boss_seen = False; pos = 0; walk = 0; fresh = True
        tab = getattr(r, 'soul_tab', None)        # souls a character by which clear this is: first, second, third and later

        def pay(lv, k):                           # k: how often the encounter has been cleared already
            if tab is None: return r.souls(lv, n, k == 0)
            return tab[min(k, len(tab) - 1)][lv - 1] * (n if r.pool else 1)

        def rush_cost(k):                         # damage to each character for rushing past an encounter cleared k times
            sd = getattr(r, 'skip_dmg', 0)
            return sd[min(k, len(sd)) - 1] if isinstance(sd, (list, tuple)) else sd

        def refight(i):                           # would the players fight reset encounter i again, not rush past it?
            return t.grind or (tab is not None and levels[i] <= t.regrind and pay(levels[i], clears[i]) > 0)
        while True:
            at_boss = pos >= 4
            # ---- a voluntary rest before the next fight
            want = False
            if sparks > t.reserve and not fresh:
                worn = any(c.hollow or c.lost for c in party) or max(c.dmg for c in party) >= t.worn_at \
                    or sum(not c.estus for c in party) * 2 > n
                lvl = ('mini' if stage == 0 else 'main') if at_boss else levels[pos]
                goal = t.ready3 if lvl in (3, 'main') else t.ready2 if lvl in (2, 'mini') else -99
                weak = sum(c._power for c in party) / n < goal
                # a rest helps a weak party only if it can then earn or spend souls
                can_grow = (r.skip_cost is None and pos > 0) or (eco.pool if r.pool else sum(c.souls for c in party)) >= 2 * n \
                    or any(clears[i] and refight(i) for i in range(4))
                # where skipped encounters cost damage, a rest is worth it only if it heals more than the walk back costs
                toll = 0 if (at_boss or (r.fog_gate and boss_seen)) else sum(rush_cost(clears[i]) for i in range(pos) if not refight(i))
                if toll and not any(c.hollow or c.lost for c in party) and max(c.dmg for c in party) - toll < 3: worn = False
                if worn and (r.death != 'party' or at_boss) and (at_boss or sparks > t.reserve + 1): want = True
                if weak and can_grow: want = True
                # where souls can only be spent at a rest, a party that holds enough of them goes back to bank them
                if t.bank is not None and getattr(r, 'free_visit', False) is not True and not r.pool \
                        and sum(c.souls for c in party) >= t.bank * n: want = True
            if want and not fresh:
                rest(); done = [False] * 4; fresh = True
                if r.skip_cost is None or not r.fog_gate: pos = 0
                else: pos = 4 if (boss_seen and not any(clears[i] and refight(i) for i in range(4))) else 0
                walk = 0
                continue
            fv = getattr(r, 'free_visit', False)             # visiting the bonfire between encounters without resting:
            if fv: eco.spend(levels=fv != 'shop')            # True = Andre and the Firekeeper; 'shop' = Andre only
            # ---- walk to the next fight
            if not at_boss and r.skip_cost is not None and clears[pos] and not must[pos] and not done[pos] and not refight(pos):
                gate = r.fog_gate and boss_seen                                  # the shortcut: nothing to pass, nothing to pay
                if not gate:
                    walk += r.skip_cost                                          # skip a cleared encounter
                    for c in party:                                              # a toll in damage for rushing past it
                        if not c.lost: c.dmg = min(c.cap - 1, c.dmg + rush_cost(clears[pos]))
                done[pos] = True; pos += 1
                continue
            if not at_boss and done[pos]: pos += 1; continue
            for c in party:
                c.sta = min(walk, c.cap - c.dmg - 1) if walk else c.sta
            walk = 0
            here = [c for c in party if not c.lost]
            out['carried'] += (eco.pool if r.pool else sum(c.souls for c in party)) / n          # unspent souls taken into the fight
            if at_boss:
                boss_seen = True; f = Fight(here, r, rng, boss=boss, policy=t, n=n); lv = 'mini' if stage == 0 else 'main'
            else:
                f = Fight(here, r, rng, enemies=cards[pos]['enemies'], policy=t, n=n); lv = levels[pos]
            if not at_boss and clears[pos]: out['repeats'] += 1      # an encounter fought again after it was cleared: the grind
            ok = f.run(); fresh = False
            for k, v in f.dec.items(): out['dec'][k] = out['dec'].get(k, 0) + v
            out['fights'] += 1; out['char_turns'] += f.char_turns; out['enemy_acts'] += f.enemy_acts; out['rounds'] += f.rounds
            out['deaths'] += f.deaths
            d = out['by_level'].setdefault(lv, dict(n=0, rounds=0, death=0, fail=0, turns=0))
            d['n'] += 1; d['rounds'] += f.rounds; d['death'] += f.deaths > 0; d['fail'] += not ok; d['turns'] += f.char_turns + f.enemy_acts
            if ok:
                first = at_boss or not clears[pos]
                k = 0 if at_boss else clears[pos]
                # ---- souls
                if r.pool:
                    if dropped_pool and dropped_pool[0] == (stage, pos): eco.pool += dropped_pool[1]; dropped_pool = None
                    eco.pool += r.boss_souls(n, sparks) if at_boss else pay(lv, k)
                    out['souls'] += r.boss_souls(n, sparks) if at_boss else pay(lv, k)
                else:
                    for c in party:
                        simple = getattr(r, 'drop', 'manuscript') == 'simple'
                        if simple and c.dropped and c.dropped[0] == (stage, pos):
                            c.souls += c.dropped[1]; c.dropped = None      # the encounter is cleared: everyone takes their souls back
                        elif not c.alive and not simple:
                            c.dropped = ((stage, pos), c.souls); c.souls = 0
                        elif c.dropped and c.dropped[0] == (stage, pos):
                            c.souls += c.dropped[1]; c.dropped = None
                        gain = r.boss_souls(n, sparks) if at_boss else pay(lv, k)
                        c.souls += gain; c.earned += gain; out['souls'] += gain
                if not at_boss:                                           # a ring that adds a soul to an encounter's reward
                    for c in party:
                        if 'serpent' in c.traits and c.alive:
                            if r.pool: eco.pool += 1
                            else: c.souls += 1
                            out['souls'] += 1; break
                # ---- treasure
                if not at_boss and first:
                    each = r.free_treasure in (None, 'each')             # one card for each character on a first clear
                    k = 1.0 if each else (r.free_treasure(lv, n) if callable(r.free_treasure) else r.free_treasure); k = int(k) + (rng.random() < k - int(k))
                    cardsT = [eco.draw(1 if stage == 0 else 2) for _ in range(k * (n if each else 1))]
                    if any('serpent2' in c.traits and c.alive for c in party): cardsT.append(eco.draw(1 if stage == 0 else 2))   # one more card
                    eco.give(cardsT)
                # ---- recovery
                for c in party:
                    if c.lost: continue
                    if not c.alive and c.hollow and r.death == 'lost': c.lost = True; continue
                    if not c.alive: c.alive = True; c.hollow = True; c.dmg = 0; c.sta = 0
                    elif r.recover == 'all': c.dmg = 0; c.sta = 0
                    else: c.dmg = max(0, c.dmg - getattr(r, 'heal_after', 1)); c.sta = 0
                    c.stagger = c.frost = c.bleed = False; c.poison = 0
                if at_boss: break
                clears[pos] += 1; must[pos] = False; done[pos] = True; pos += 1
            else:
                # ---- a failed encounter: souls are dropped and the party must rest
                if r.pool:
                    dropped_pool = ((stage, pos), eco.pool); eco.pool = 0
                else:
                    for c in party:
                        if c.dropped: out['souls_lost'] += c.dropped[1] / n                # a second defeat: the souls left behind are gone
                        c.dropped = ((stage, pos), c.souls); c.souls = 0
                if not rest():
                    out['lost_at'] = lv; out['sparks_left'] = 0; return out
                done = [False] * 4; fresh = True
                if not at_boss: must[pos] = True                                   # a failed encounter cannot be skipped
                pos = 4 if (at_boss and r.fog_gate and not any(clears[i] and refight(i) for i in range(4))) else 0
        # ---- the boss is dead
        if stage == 0:
            sparks = r.sparks(n) if r.boss_spark == 'reset' else sparks + 1
            if getattr(r, 'ember', False):
                for c in party: c.ember = True               # the manuscript: each character is embered when a boss falls
            eco.after_mini_boss(); rest(free=True)
    out['win'] = True; out['sparks_left'] = sparks
    out['power'] = sum(c._power for c in party) / n
    return out
