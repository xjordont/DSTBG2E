#!/usr/bin/env python3
"""Checks of the simulator against hand calculation and against its own invariants.
Run: python3 tools/sim/test_sim.py        (prints one line per check; exits non-zero on a failure)"""
import math, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import engine as E
import rules as RU
from characters import Char, Economy, ITEMS, CLASSES
from game import play

FAILS = []


def check(name, ok, detail=''):
    print(('ok   ' if ok else 'FAIL ') + name + (('   ' + str(detail)) if detail else ''))
    if not ok: FAILS.append(name)


def close(a, b, tol): return abs(a - b) <= tol


# ---------------------------------------------------------------- dice and the tile
check('black die mean 7/6', close(sum(v * p for v, p in E.pmf_sum('b')), 7 / 6, 1e-9))
check('blue die mean 11/6', close(sum(v * p for v, p in E.pmf_sum('u')), 11 / 6, 1e-9))
check('orange die mean 15/6', close(sum(v * p for v, p in E.pmf_sum('o')), 15 / 6, 1e-9))
check('every distribution sums to one', all(close(sum(p for _, p in f(d)), 1, 1e-9) for d in ('', 'b', 'bu', 'buo', 'bbbb') for f in (E.pmf_sum, E.pmf_best2)))
check('two highest of two dice is their sum', all(close(a[1], b[1], 1e-9) and a[0] == b[0] for a, b in zip(E.pmf_best2('bu'), E.pmf_sum('bu'))))
check('two highest of three is never above the sum', sum(v * p for v, p in E.pmf_best2('bbu')) < sum(v * p for v, p in E.pmf_sum('bbu')))
check('dodge: one die, difficulty one, is one half', close(E.p_dodge(1, 1), 0.5, 1e-9))
check('dodge: two dice, difficulty one, is three quarters', close(E.p_dodge(2, 1), 0.75, 1e-9))
check('dodge: two dice, difficulty two, is one quarter', close(E.p_dodge(2, 2), 0.25, 1e-9))
check('dodge: difficulty zero always succeeds', E.p_dodge(0, 0) == 1.0)
check('the tile has 13 nodes', len(E.NODES) == 13)
check('corner to opposite corner is four steps', E.DIST[E.IDX[(0, 0)]][E.IDX[(4, 4)]] == 4)
check('along an edge, corner to corner is two steps', E.DIST[E.IDX[(0, 0)]][E.IDX[(4, 0)]] == 2)
check('the centre touches eight nodes', len(E.NBR[E.IDX[(2, 2)]]) == 8)
check('a corner touches three nodes', len(E.NBR[E.IDX[(0, 0)]]) == 3)

# ---------------------------------------------------------------- attack arithmetic
# Long Sword light attack (one blue die) against block 1: damage 0,0,1,1,1,2 -> mean 5/6; kills a 1-health enemy 4 times in 6
pm = dict(E.attack_pmf('u', 0, 1, 1))
check('Long Sword against block 1: mean 5/6', close(sum(d * p for d, p in pm.items()), 5 / 6, 1e-9))
check('Long Sword kills a Hollow Soldier 4 times in 6', close(1 - pm[0], 4 / 6, 1e-9))
# an attack of 4 against a Knight's starting block (blue + black, summed): mean damage by enumeration
exp = sum(max(0, 4 - a - b) for a in E.DIE['u'] for b in E.DIE['b']) / 36
check('attack 4 against blue+black block, enumerated', close(sum(d * p for d, p in E.hit_stats('ub', 'sum', 4, 0)), exp, 1e-9), round(exp, 3))

# ---------------------------------------------------------------- one enemy, one character: simulation against enumeration
R17 = RU.OFFICIAL_2017


def lone(seeds=4000):
    """A Knight with no tokens and only his light attack, a Hollow Soldier already on his node, official rules."""
    wins = dmg = 0
    for s in range(seeds):
        c = Char('Knight', R17); f = E.Fight([c], R17, random.Random(s), enemies=['Hollow Soldier'],
                                             policy=E.Policy(estus_risk=9, luck_at=99, evade=0.0, kite=False))
        c.heroic = c.luck = c.estus = False; c.options['R'] = c.options['R'][:1]; f.foes[0].node = c.node
        ok = f.run(); wins += ok; dmg += c.dmg
    return wins / seeds, dmg / seeds


# The soldier attacks in every enemy phase it is alive; the Knight kills it with probability 2/3 on each of his turns.
# Expected attacks: 1 + 1/3 + 1/9 + ... = 1.5, each for the enumerated mean above.
w, d = lone()
check('Knight against one Hollow Soldier: always wins', w > 0.999, w)
check('Knight against one Hollow Soldier: mean damage is 1.5 attacks, as enumerated', close(d, 1.5 * exp, 0.07), '%.3f against %.3f' % (d, 1.5 * exp))

# ---------------------------------------------------------------- scaling is applied as written


def foes(rules, n, names):
    party = [Char(c, rules) for c in ('Knight', 'Warrior', 'Herald', 'Assassin')[:n]]
    return E.Fight(party, rules, random.Random(0), enemies=names).foes


M = RU.MANUSCRIPT
check('manuscript: +1 health per extra character', [foes(M, n, ['Hollow Soldier'])[0].hp for n in (1, 2, 3, 4)] == [1, 2, 3, 4])
check('manuscript: +1 attack at three and four', [foes(M, n, ['Hollow Soldier'])[0].atk_bonus for n in (1, 2, 3, 4)] == [0, 0, 1, 1])
check('manuscript: repeat only at four', [M.reps(n) for n in (1, 2, 3, 4)] == [1, 1, 1, 2])
check('manuscript: one-node moves become two at two or more', [M.move2(n) for n in (1, 2, 3, 4)] == [False, True, True, True])
check('official: no scaling', all(foes(R17, n, ['Sentinel'])[0].hp == 10 and foes(R17, n, ['Sentinel'])[0].atk_bonus == 0 for n in (1, 2, 3, 4)))
check('sparks are five, four, three, two', [R17.sparks(n) for n in (1, 2, 3, 4)] == [5, 4, 3, 2] == [M.sparks(n) for n in (1, 2, 3, 4)])

# ---------------------------------------------------------------- activations per round


def acts(rules, n, seeds=200):
    """Mean enemy activations per character turn while every enemy is alive (one unkillable enemy)."""
    card = dict(E.ENEMIES['Hollow Soldier']); card = dict(card, hp=10 ** 6, steps=[dict(k='move', n=1, dir='to', tgt='nearest')])
    E.ENEMIES['_Dummy'] = card; tot = 0
    for s in range(seeds):
        party = [Char(c, rules) for c in ('Knight', 'Warrior', 'Herald', 'Assassin')[:n]]
        f = E.Fight(party, rules, random.Random(s), enemies=['_Dummy']); f.run(max_rounds=5)
        tot += f.enemy_acts / f.char_turns
    del E.ENEMIES['_Dummy']; return tot / seeds


check('official: one enemy activation for each character turn', all(close(acts(R17, n), 1.0, 1e-9) for n in (1, 2, 3, 4)))
check('manuscript: one enemy activation for each round of n character turns', all(close(acts(M, n), 1.0 / n, 1e-9) for n in (1, 2, 3, 4)))

# ---------------------------------------------------------------- invariants over whole games


def invariants(rules, n, seeds):
    bad = []
    orig_wound = E.Fight.wound; orig_turn = E.Fight.char_turn; orig_enemy = E.Fight.enemy_turn; orig_boss = E.Fight.boss_turn

    def wound(self, c, d):
        orig_wound(self, c, d)
        if c.alive and c.dmg + c.sta > c.cap: bad.append('bar overfull')

    def turn(self, c):
        if not c.alive: bad.append('dead character acted')
        orig_turn(self, c)
        if c.sta < 0 or c.dmg < 0: bad.append('negative cubes')
        if c.alive and c.dmg + c.sta > c.cap: bad.append('bar overfull after turn')

    def enemy(self, f):
        if f.hp <= 0: bad.append('dead enemy acted')
        orig_enemy(self, f)

    def boss(self, f):
        if f.hp <= 0: bad.append('dead boss acted')
        orig_boss(self, f)
    E.Fight.wound, E.Fight.char_turn, E.Fight.enemy_turn, E.Fight.boss_turn = wound, turn, enemy, boss
    try:
        for s in range(seeds):
            o = play(n, rules, s)
            if o['rests'] > rules.sparks(n) + 1 + (rules.sparks(n) if rules.boss_spark == 'reset' else 0): bad.append('more rests than sparks')
            if o['win'] and o['lost_at'] is not None: bad.append('won and lost')
    finally:
        E.Fight.wound, E.Fight.char_turn, E.Fight.enemy_turn, E.Fight.boss_turn = orig_wound, orig_turn, orig_enemy, orig_boss
    return bad


for name, rules in (('official 2017', R17), ('official 2022', RU.OFFICIAL_2022), ('manuscript', M), ('settled', RU.SETTLED)):
    for n in (1, 2, 3, 4):
        b = invariants(rules, n, 40)
        check('invariants hold: %s, %d character%s' % (name, n, '' if n == 1 else 's'), not b, sorted(set(b)))

# ---------------------------------------------------------------- determinism and the death rules
a = play(3, M, 11); b = play(3, M, 11)
check('the same seed gives the same game', a == b)
c = Char('Knight', R17); f = E.Fight([c], R17, random.Random(0), enemies=['Hollow Soldier']); c.dmg = 7; c.sta = 0
check('official: damage that fills the bar kills', f.lethal(c, 3) and not f.lethal(c, 2))
c = Char('Knight', M); f = E.Fight([c], M, random.Random(0), enemies=['Hollow Soldier']); c.dmg = 7; c.sta = 0
check('manuscript: damage that fills the bar exactly does not kill; one more does', (not f.lethal(c, 3)) and f.lethal(c, 4))
c.hollow = True
check('manuscript: a hollow character has an eight-space bar', c.cap == 8)

# ---------------------------------------------------------------- a riposte is paid for
c = Char('Knight', M); f = E.Fight([c], M, random.Random(0), enemies=['Hollow Soldier'])
c.options['R'] = [dict(c.options['R'][1])]; cost = c.options['R'][0]['cost']; c.sta = 0; f.riposte(c, f.foes[0])
check('a riposte costs its attack option\'s stamina', cost > 0 and c.sta == cost, (cost, c.sta))

# ---------------------------------------------------------------- equipment data
check('every starting item is met by its class at base stats',
      all(Char(k, R17).cost_to_meet(ITEMS[n]['req'])[0] == 0 for k, v in CLASSES.items() for n in v['start']))
check('stat costs: tier one 2, tier two 4, tier three 8', Char('Knight', R17).cost_to_meet([40, 0, 0, 0])[0] == 14)
check('official deck: 56 common cards and five class cards a character',
      len(Economy([Char('Knight', R17)], R17, random.Random(0)).deck) == 61)

print()
print('%d checks failed' % len(FAILS) if FAILS else 'all checks passed')
sys.exit(1 if FAILS else 0)
