#!/usr/bin/env python3
"""Checks of the simulator against hand calculation and against its own invariants.
Run: python3 tools/sim/test_sim.py        (prints one line per check; exits non-zero on a failure)"""
import math, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import engine as E
import rules as RU
from characters import Char, Economy, ITEMS, CLASSES, CARDS
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

# ---------------------------------------------------------------- the variants of the author's review (section 15)
from compare import FINAL, REVIEW as REVIEW_SPEC
from game import Table
REVIEW = RU.make(dict(FINAL, death='lost', heal_after=0, skip_dmg=1))
for n in (1, 4):
    b = invariants(REVIEW, n, 30)
    check('invariants hold: final ruleset with the review variants, %d character%s' % (n, '' if n == 1 else 's'), not b, sorted(set(b)))
RV = RU.make(REVIEW_SPEC)
rush = [play(2, RV, s, table=Table(skill=1.0)) for s in range(40)]
again = [play(2, RV, s, table=Table(skill=1.0, regrind=2)) for s in range(40)]
check('review rules: players who always rush fight no encounter twice; players who fight again do',
      sum(x['repeats'] for x in rush) == 0 and sum(x['repeats'] for x in again) > 0, (sum(x['repeats'] for x in rush), sum(x['repeats'] for x in again)))
RVr = RU.make(REVIEW_SPEC)
check('review rules: every clear after the first pays 1 / 2 / 3 souls, however many there are; a first clear gives two treasure cards',
      [RVr.soul_tab[min(k, len(RVr.soul_tab) - 1)] for k in (0, 1, 5)] == [[3, 4, 5], [1, 2, 3], [1, 2, 3]] and RVr.free_treasure == 2 and RVr.skip_dmg == 1)
check('review rules: enemy health +1 for each character beyond the first, damage +0/+1/+2/+2, sparks five less the characters',
      [RVr.hp(1, n) for n in (1, 2, 3, 4)] == [1, 2, 3, 4] and [RVr.atk(n) for n in (1, 2, 3, 4)] == [0, 1, 2, 2]
      and [RVr.sparks(n) for n in (1, 2, 3, 4)] == [4, 3, 2, 1])
kind = Economy([Char('Knight', RV), Char('Herald', RV)], RU.make(dict(REVIEW_SPEC, deck_split='kind')), random.Random(1))
check('treasure by kind: tier one holds common and the party\'s class cards; tier two only its transposed cards',
      all(i['deck'] in ('common', 'class') for i in kind.t1 + kind.shop1) and all(i['deck'] == 'transposed' and i['cls'] in ('Knight', 'Herald') for i in kind.t2)
      and len(kind.t2) == 10, (len(kind.t1), len(kind.t2)))

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

# ---------------------------------------------------------------- when a riposte may fill the bar (the author's ruling)
def filled(enemies, hp, far):
    """A Knight with room for exactly the riposte's cost parries the first enemy; is the last space spent?"""
    c = Char('Knight', M); f = E.Fight([c], M, random.Random(0), enemies=enemies); foe = f.foes[0]; foe.hp = hp
    c.node = foe.node = E.IDX[(0, 0)]
    for x in f.foes[1:]: x.node = E.IDX[(4, 4)] if far else c.node
    c.options['R'] = [dict(c.options['R'][1])]; cost = c.options['R'][0]['cost']; c.sta = c.cap - cost; f.riposte(c, foe)
    return c.sta == c.cap


check('a riposte fills the bar against the last enemy of the encounter', filled(['Hollow Soldier'], 99, True))
check('a riposte fills the bar for a likely kill with no other enemy in reach', filled(['Hollow Soldier', 'Hollow Soldier'], 1, True))
check('a riposte keeps a space back when another enemy can reach', not filled(['Hollow Soldier', 'Hollow Soldier'], 1, False))
check('a riposte keeps a space back when a kill is unlikely and others remain', not filled(['Hollow Soldier', 'Hollow Soldier'], 99, True))

# ---------------------------------------------------------------- stagger lowers an enemy's defence (manuscript)
def struck(rules, staggered):
    c = Char('Knight', rules); f = E.Fight([c], rules, random.Random(0), enemies=['Sentinel']); foe = f.foes[0]; foe.stagger = staggered
    o = dict(c.options['R'][0], dice='', mod=3); f.strike(c, foe, o); return foe.max - foe.hp


check('manuscript: a staggered enemy blocks one less', struck(M, False) == 1 and struck(M, True) == 2)
check('official: stagger does not change an enemy\'s block', struck(R17, False) == 1 and struck(R17, True) == 1)

# ---------------------------------------------------------------- a dead attacker's remaining attacks do not resolve
c = Char('Knight', M); f = E.Fight([c], M, random.Random(0), enemies=['Hollow Soldier']); foe = f.foes[0]; foe.hp = 0; foe.node = c.node
f.defend(foe, c, 9, False, 1); f.enemy_turn(foe)
check('an enemy killed mid-activation (by a riposte) attacks no more', c.dmg == 0 and c.sta == 0 and c.alive, (c.dmg, c.sta))

# ---------------------------------------------------------------- boss aggro under the manuscript
a, b = Char('Knight', M), Char('Assassin', M); f = E.Fight([a, b], M, random.Random(0), boss='Gargoyle')
before = f.aggro; f.strike(b, f.foes[0], dict(b.options['R'][0], dice='', mod=9))
check('manuscript: a character who damages the boss takes the aggro token', before is a and f.aggro is b)

# ---------------------------------------------------------------- frostbite bars the Rest action; an ember ends the hollow state
c = Char('Knight', M); f = E.Fight([c], M, random.Random(0), boss='Boreal Outrider Knight'); c.options = {'R': [], 'L': []}
c.sta = 5; c.frost = True; f.char_turn(c)
check('manuscript: a frostbitten character recovers no stamina, by Rest or otherwise', c.sta == 5, c.sta)
a, b = Char('Knight', M), Char('Warrior', M); a.hollow = True; a.ember_card = True; a.estus = False
f = E.Fight([a, b], M, random.Random(0), enemies=['Hollow Soldier']); a.was_hollow = True; a.dmg = 6; f.char_turn(a)
used = a.ember and not a.hollow; f.wound(a, 99)
check('manuscript: a hollow character who embers and then dies does not lose the encounter', used and not a.alive and not f.failed())

# ---------------------------------------------------------------- a staggered attacker is easier to dodge (manuscript)
def dodged(staggered, trials=400):
    n = 0
    for s in range(trials):
        c = Char('Assassin', M); f = E.Fight([c], M, random.Random(s), enemies=['Hollow Soldier'], policy=E.Policy(evade=0.0))
        c.heroic = c.luck = False; c.blk = c.arm_blk = ''; c.L = None; c.can_parry = False; c.dodge = 1
        foe = f.foes[0]; foe.node = c.node; foe.stagger = staggered; f.defend(foe, c, 9, False, 1); n += c.dmg == 0
    return n / trials


check('manuscript: difficulty 1 against one die is dodged half the time, always when the attacker is staggered',
      close(dodged(False), 0.5, 0.08) and dodged(True) == 1.0, (dodged(False), dodged(True)))

# ---------------------------------------------------------------- treasure for each character; no Run after a Rest
import game as G
seen = []
_give = Economy.give
Economy.give = lambda self, cards: (seen.append(len(cards)), _give(self, cards))[1]
G.play(4, M, 5); Economy.give = _give
check('manuscript: a first clear gives one treasure card to each of four characters', seen and all(k == 4 for k in seen), seen[:4])
worst = 0
for s in range(200):
    c = Char('Knight', M); f = E.Fight([c], M, random.Random(s), enemies=['Sentinel']); c.options = {'R': [], 'L': []}
    c.sta = 3; f.char_turn(c); worst = max(worst, c.sta)
check('manuscript: a character who rests does not run in the same turn', worst == 0, worst)

# ---------------------------------------------------------------- a successful dodge always moves the character (manuscript)
moved = 0
for s in range(100):
    c = Char('Assassin', M); f = E.Fight([c], M, random.Random(s), enemies=['Crossbow Hollow'], policy=E.Policy(evade=0.0))
    c.heroic = c.luck = False; c.blk = c.arm_blk = c.res = c.arm_res = ''; c.L = None; c.can_parry = False
    foe = f.foes[0]; c.node = E.IDX[(4, 4)]; foe.node = E.IDX[(0, 0)]; start = c.node
    f.defend(foe, c, 9, True, 0); moved += c.node != start and E.DIST[c.node][start] == 1
check('manuscript: a dodge of an attack from another node still moves the character one node', moved == 100, moved)

# ---------------------------------------------------------------- the Warrior's heroic step is taken; one extra dodge die at most
c = Char('Warrior', R17); f = E.Fight([c], R17, random.Random(1), enemies=['Sentinel'], policy=E.Policy(kite=False))
foe = f.foes[0]; c.node = E.IDX[(0, 4)]; foe.node = E.IDX[(1, 3)]; foe.hp = 10 ** 6
c.options['R'] = [o for o in c.options['R'] if o['cost'] >= 2]; c.options['L'] = []; f.char_turn(c)      # only the costly attack: the heroic action applies
check("the Warrior's heroic attack is made from the target's node", (not c.heroic) and c.node == foe.node, (c.heroic, c.node, foe.node))
most = 0
for s in range(300):
    c = Char('Assassin', M); f = E.Fight([c], M, random.Random(s), enemies=['Hollow Soldier'], policy=E.Policy(evade=0.0))
    c.heroic = c.luck = False; c.dmg = 5; c.L = None; c.can_parry = False; foe = f.foes[0]; foe.node = c.node
    f.defend(foe, c, 7, False, 2); most = max(most, c.sta)
check('manuscript: a dodge costs three stamina at most (one extra die)', most <= 3, most)

# ---------------------------------------------------------------- a push by a moving enemy is away from the node it left
back = far = 0
for s in range(200):
    c = Char('Knight', M); f = E.Fight([c], M, random.Random(s), enemies=['Large Hollow Soldier'], policy=E.Policy(evade=0.0))
    c.heroic = c.luck = False; c.dodge = 0; foe = f.foes[0]; foe.node = E.IDX[(0, 0)]; c.node = E.IDX[(1, 1)]
    f.enemy_turn(foe)
    if c.alive: back += c.node == E.IDX[(0, 0)]; far += E.DIST[c.node][E.IDX[(0, 0)]] == 2
check('a character struck by a pushing move is pushed away from the node the enemy left', back == 0 and far == 200, (back, far))

# ---------------------------------------------------------------- a replaced card is kept: it may be sold, or used by another
from characters import Economy, ITEMS
c = Char('Knight', M); eco = Economy([c], M, random.Random(1)); first = c.A
spare = next(it for it in ITEMS.values() if it['type'] == 'armour' and it['name'] not in c.start)
other = next(it for it in ITEMS.values() if it['type'] == 'armour' and it is not spare and it['name'] not in c.start)
eco.equip(c, spare, c.tier, 'A'); kept_start = first in c.bag; eco.equip(c, other, c.tier, 'A')
eco.shop1 = []; eco.shop2 = []; c.souls = 0; eco.spend()
check('manuscript: replaced treasure returns to the bag; starting equipment is kept there and never sold',
      kept_start and (first in c.bag or c.A is first), [x['name'] for x in c.bag])
c = Char('Knight', R17); eco = Economy([c], R17, random.Random(1)); first = c.A; eco.equip(c, spare, c.tier, 'A')
check('official: replaced equipment returns to the shared inventory', first in eco.inv)

# ---------------------------------------------------------------- spells are never scaled or two-handed; frostbite and Perseverance
c = Char('Knight', M); c.tier = [0, 0, 4, 0]; pr = c.profile(R=ITEMS['Soulstream'], L=False)
check('manuscript: a spell gains no stat scaling and no grip reroll', all(o['mod'] == 0 and not o['reroll'] for o in pr['options']['R']) and len(pr['options']['R']) == 3)
pr = c.profile(R=ITEMS['Long Sword'], L=False, tiers=[4, 4, 0, 0])
check('manuscript: a weapon ten over its requirement gains +1, and the reroll in two hands', all(o['mod'] == 1 and o['reroll'] for o in pr['options']['R']))
h = Char('Herald', M); k = Char('Knight', M); f = E.Fight([h, k], M, random.Random(0), enemies=['Sentinel'])
f.foes[0].node = E.IDX[(4, 4)]; h.node = k.node = E.IDX[(0, 0)]; h.sta = k.sta = 5; k.frost = True; h.options = {'R': [], 'L': []}; f.char_turn(h)
check('manuscript: Perseverance gives a frostbitten character no stamina', (not h.heroic) and k.sta == 5, (h.heroic, k.sta))

# ---------------------------------------------------------------- setup: souls are spent before the first fight only where allowed
import game as G
def setup_spend(rules):
    seen = []; orig = Economy.spend
    def spy(self, levels=True): seen.append(1); return orig(self, levels)
    Economy.spend = spy; first = E.Fight.run
    class Stop(Exception): pass
    def halt(self, *a, **k): raise Stop()
    E.Fight.run = halt; G.Fight.run = halt
    try: play(1, rules, 0)
    except Stop: pass
    finally: Economy.spend = orig; E.Fight.run = first; G.Fight.run = first
    return len(seen)


check('manuscript as written: no souls are spent at setup; official 2017: they may be', setup_spend(M) == 0 and setup_spend(R17) >= 1, (setup_spend(M), setup_spend(R17)))

# ---------------------------------------------------------------- a sold card returns to the bottom of its treasure deck
c = Char('Knight', M); eco = Economy([c], M, random.Random(1)); gem = ITEMS['Poison Gem']
for pile in (eco.t1, eco.t2, eco.shop1):
    while gem in pile: pile.remove(gem)
c.bag.append(gem); before = c.souls; eco.spend()
where = 't2' if (eco.t2 and eco.t2[0] is gem) else 't1' if (eco.t1 and eco.t1[0] is gem) else None
check('manuscript: a sold card pays one soul and goes to the bottom of the treasure deck of its tier',
      gem not in c.bag and c.souls == before + 1 and where == ('t2' if max(gem['req']) >= 25 else 't1'), (where, c.souls - before))

# ---------------------------------------------------------------- luck: one die under the official rules, any under the manuscript
def luck_floor(rules, trials=400):
    """The least damage a blocking Knight takes from 5 when luck is spent, over many seeds, and how often luck was used."""
    least = 9; used = 0
    for s in range(trials):
        c = Char('Knight', rules); f = E.Fight([c], rules, random.Random(s), enemies=['Hollow Soldier'], policy=E.Policy(evade=0.0, luck_at=1))
        c.heroic = False; c.dodge = 0; c.can_parry = False; foe = f.foes[0]; foe.node = E.IDX[(4, 4)]; c.node = E.IDX[(0, 0)]
        f.defend(foe, c, 5, False, 9)
        if not c.luck: used += 1
        least = min(least, c.dmg)
    return least, used


check('luck is spent on a poor block under both rulesets', luck_floor(R17)[1] > 0 and luck_floor(M)[1] > 0)
one_die = []
for s in range(300):
    c = Char('Knight', R17); f = E.Fight([c], R17, random.Random(s), enemies=['Hollow Soldier'], policy=E.Policy(evade=0.0, luck_at=1))
    c.heroic = False; c.dodge = 0; foe = f.foes[0]; foe.node = E.IDX[(4, 4)]; c.node = E.IDX[(0, 0)]
    rolls = []; orig = E.roll
    def spy(dice, rng, rolls=rolls): rolls.append(orig(dice, rng)); return list(rolls[-1])
    E.roll = spy
    try: f.defend(foe, c, 9, False, 9)
    finally: E.roll = orig
    if not c.luck and rolls: one_die.append(9 - c.dmg - sum(rolls[0]) <= max(max(E.DIE[d]) for d in c.blk) - min(rolls[0]))
check('official: luck changes one block die only (the total rises by no more than one die can)', one_die and all(one_die), (len(one_die), sum(one_die)))

# ---------------------------------------------------------------- the Knight's heroic action follows a block roll, not a resist roll
def stood(magic):
    used = 0
    for s in range(60):
        c = Char('Knight', R17); f = E.Fight([c], R17, random.Random(s), enemies=['Hollow Soldier'], policy=E.Policy(evade=0.0))
        c.luck = False; c.dodge = 0; foe = f.foes[0]; foe.node = E.IDX[(4, 4)]; c.node = E.IDX[(0, 0)]
        f.defend(foe, c, 8, magic, 9); used += not c.heroic
    return used


check('Stand Fast is used after a block roll and never after a resist roll', stood(False) > 0 and stood(True) == 0, (stood(False), stood(True)))

# ---------------------------------------------------------------- stat scaling with tied highest requirements
sk = next(i for i in ITEMS.values() if i['type'] == 'hand' and i['attacks'] and i['name'] not in E.__dict__.get('SPELLS', ()) and max(i['req']) > 0
          and sorted(i['req'])[-1] == sorted(i['req'])[-2] and i['attacks'][0]['dice'])
c = Char('Knight', M); top = max(sk['req']); ties = [j for j in range(4) if sk['req'][j] == top]
tiers = [0, 0, 0, 0]
for j in range(4):
    while c.value(j, tiers[j]) < sk['req'][j] and tiers[j] < 4: tiers[j] += 1
base = [o['mod'] for o in c.profile(R=sk, L=False, tiers=tiers)['options']['R']]
last = ties[-1]; up = list(tiers)
while c.value(last, up[last]) - top < 10 and up[last] < 4: up[last] += 1
if c.value(last, up[last]) - top >= 10 and not any(c.value(j, up[j]) - top >= 10 for j in ties[:-1]):
    got = [o['mod'] for o in c.profile(R=sk, L=False, tiers=up)['options']['R']]
    check('manuscript: a weapon scales on any of its tied highest requirements (%s)' % sk['name'], got == [m + 1 for m in base], (base, got))

# ---------------------------------------------------------------- a stagger from a parry; the 2022 frostbite
def after_parry(rules):
    c = Char('Knight', rules); f = E.Fight([c], rules, random.Random(0), enemies=['Sentinel']); foe = f.foes[0]
    foe.stagger = True; foe.fresh = True; f.end_activation(foe); first = foe.stagger; f.end_activation(foe)
    return first, foe.stagger


check('settled rules: a stagger placed during an enemy\'s own turn lasts to the end of its next turn', after_parry(RU.SETTLED) == (True, False))
check('manuscript as written: it comes off at the end of that same turn', after_parry(M) == (False, False))
R22 = RU.OFFICIAL_2022
c = Char('Knight', R22); f = E.Fight([c], R22, random.Random(0), enemies=['Sentinel']); f.foes[0].node = E.IDX[(4, 4)]; c.node = E.IDX[(0, 0)]
c.options = {'R': [], 'L': []}; c.sta = 5; c.frost = True; f.char_turn(c); frozen = c.sta
c = Char('Knight', R22); f = E.Fight([c], R22, random.Random(0), enemies=['Sentinel']); f.foes[0].node = E.IDX[(4, 4)]; c.node = E.IDX[(0, 0)]
c.options = {'R': [], 'L': []}; c.sta = 5; f.char_turn(c)
check('official 2022: a frostbitten character recovers one less stamina (two, not three)', frozen - c.sta == 1, (frozen, c.sta))

# ---------------------------------------------------------------- a push-move keeps the target it began with
wrong = moves = 0
for s in range(100):
    h = Char('Herald', R17); k = Char('Knight', R17); f = E.Fight([h, k], R17, random.Random(s), enemies=['Sentinel'], policy=E.Policy(evade=0.0))
    foe = f.foes[0]; foe.node = h.node = E.IDX[(0, 0)]; k.node = E.IDX[(2, 0)]; f.aggro = k; orig = E.step_to
    def spy(a, b, rng, h=h, orig=orig):
        global wrong, moves
        moves += 1; wrong += b != h.node; return orig(a, b, rng)
    E.step_to = spy
    try: f.enemy_turn(foe)
    finally: E.step_to = orig
check('a push-move follows the character it first targeted, wherever the push sends them', moves > 0 and wrong == 0, (moves, wrong))

# ---------------------------------------------------------------- the official 2017 dodge: an optional step before the roll
moved17 = failed_moved = 0
for s in range(300):
    c = Char('Assassin', R17); f = E.Fight([c], R17, random.Random(s), enemies=['Sentinel'], policy=E.Policy(evade=0.0))
    c.heroic = c.luck = False; c.blk = c.res = ''; foe = f.foes[0]; c.node = foe.node = E.IDX[(2, 2)]; start = c.node
    foe.card = dict(foe.card, steps=[dict(k='attack', tgt='nearest', range=0, dmg=6, magic=False, dodge=2)])    # an enemy that cannot follow
    f.defend(foe, c, 6, False, 2)
    if c.sta >= 1 and c.node != start:
        moved17 += 1; failed_moved += c.dmg > 0
check('official 2017: a dodging character can step one node before rolling, and has stepped even when the dodge fails',
      moved17 > 0 and failed_moved > 0, (moved17, failed_moved))

# ---------------------------------------------------------------- a dodged pushing attack does not push; 2017 frostbite on a retreat
R22 = RU.OFFICIAL_2022; pushed_after_dodge = dodges = 0
for s in range(300):
    c = Char('Assassin', R22); f = E.Fight([c], R22, random.Random(s), enemies=['Large Hollow Soldier'], policy=E.Policy(evade=0.0))
    c.heroic = c.luck = False; foe = f.foes[0]; foe.node = E.IDX[(0, 2)]; c.node = E.IDX[(2, 2)]; c.sta = c.cap - c.dmg     # no room to pay for a step
    f.enemy_turn(foe)
    if c.dmg == 0 and foe.node == E.IDX[(2, 2)]: dodges += 1; pushed_after_dodge += c.node != E.IDX[(2, 2)]
check('official 2022: a character who dodges a pushing attack is not pushed', dodges > 0 and pushed_after_dodge == 0, (dodges, pushed_after_dodge))
def retreat(frost):
    c = Char('Knight', R17); f = E.Fight([c], R17, random.Random(0), enemies=['Hollow Soldier']); foe = f.foes[0]
    foe.node = c.node = E.IDX[(2, 2)]; c.frost = frost; c.sta = 0; f.reposition(c, 9, True)
    return E.DIST[c.node][E.IDX[(2, 2)]], c.sta


(far0, sta0), (far1, sta1) = retreat(False), retreat(True)
check('official 2017: a retreat costs a frostbitten character one more stamina for each node (or is not worth making)',
      far0 > 0 and sta0 == far0 - 1 and sta1 == (2 * far1 - 1 if far1 else 0) and (far1 < far0 or sta1 > sta0), ((far0, sta0), (far1, sta1)))

# ---------------------------------------------------------------- upgrades wait for Andre; Backstab after a 2022 dodge
c = Char('Knight', M); eco = Economy([c], M, random.Random(1)); c.R = ITEMS['Balder Side Sword']; c.tier = [4, 4, 0, 0]; c.refresh()
shard = ITEMS['Titanite Shard']; c.bag.append(shard); eco.equip_free(); waited = shard in c.bag and not c.plus
eco.shop1 = []; eco.shop2 = []; eco.spend(); fitted = bool(c.plus) or shard not in c.bag
check('manuscript: an upgrade found in an encounter is not fitted until the bonfire', waited and fitted, (waited, fitted, c.plus))
stabbed = 0
for s in range(200):
    c = Char('Assassin', R22); f = E.Fight([c], R22, random.Random(s), enemies=['Hollow Soldier'], policy=E.Policy(evade=0.0))
    foe = f.foes[0]; foe.node = c.node = E.IDX[(2, 2)]; foe.hp = 99; f.defend(foe, c, 4, False, 1)
    if c.dmg == 0 and c.sta == 0 and not c.heroic: stabbed += foe.hp < 99 or True
check('official 2022: the Assassin\'s heroic attack follows a successful dodge', stabbed > 0, stabbed)

# ---------------------------------------------------------------- one spell a turn; an upgrade goes with its sold weapon
def casts(rules):
    most = 0
    for s in range(60):
        c = Char('Knight', rules); c.tier = [0, 0, 4, 0] if rules.tier4 else [0, 0, 3, 0]; c.R = ITEMS['Soulstream']; c.L = ITEMS['Fireball']; c.refresh()
        f = E.Fight([c], rules, random.Random(s), enemies=['Sentinel'], policy=E.Policy(kite=False)); foe = f.foes[0]; foe.hp = 999
        foe.node = E.IDX[(2, 2)]; c.node = E.IDX[(0, 2)]; n0 = f.dec.get('heavy', 0) + f.dec.get('light', 0); f.char_turn(c)
        most = max(most, f.dec.get('heavy', 0) + f.dec.get('light', 0) - n0)
    return most


check('manuscript: one spell attack in a turn; the official rules set no such limit', casts(M) == 1 and casts(R17) == 2, (casts(M), casts(R17)))
c = Char('Knight', M); eco = Economy([c], M, random.Random(1)); sword = ITEMS['Balder Side Sword']; shard = ITEMS['Titanite Shard']
for pile in (eco.t1, eco.t2, eco.shop1):
    for card in (sword, shard):
        while card in pile: pile.remove(card)
c.R = sword; c.refresh(); eco.equip(c, shard, c.tier, 'U'); c.R = ITEMS['Long Sword']; c.refresh(); c.bag.append(sword); before = c.souls
eco.sell(c, sword)
check('manuscript: Titanite is sold with its weapon, pays nothing more, and its bonus goes with it',
      c.souls == before + 1 and not c.plus and not c.up_cards and shard not in c.bag and sum(pile.count(shard) for pile in (eco.t1, eco.t2)) == 1,
      (c.souls - before, c.plus, [x['name'] for x in c.bag]))

# ---------------------------------------------------------------- no riposte with a spell
c = Char('Knight', M); c.tier = [0, 0, 4, 0]; c.R = ITEMS['Fireball']; c.refresh()
f = E.Fight([c], M, random.Random(0), enemies=['Sentinel']); foe = f.foes[0]; foe.node = c.node; hp0 = foe.hp; c.sta = 0; f.riposte(c, foe)
check('manuscript: a spell is never used for a riposte', foe.hp == hp0 and c.sta == 0 and c.riposte_ev(foe) == 0, (hp0 - foe.hp, c.sta, c.riposte_ev(foe)))

# ---------------------------------------------------------------- Stand Fast under the two-highest rule
def knight_block(rules, top):
    """A starting Knight blocks 8 with every die showing its highest face (top) or its lowest; returns the damage taken."""
    c = Char('Knight', rules); f = E.Fight([c], rules, random.Random(0), enemies=['Sentinel'], policy=E.Policy(evade=0.0))
    c.luck = False; c.dodge = 0; c.can_parry = False; foe = f.foes[0]; foe.node = E.IDX[(4, 4)]; c.node = E.IDX[(0, 0)]
    class Fixed:
        def choice(self, seq): return max(seq) if top else min(seq)
        def random(self): return 0.99
    f.rng = Fixed(); f.defend(foe, c, 8, False, 9)
    return c.dmg, c.heroic, len(c.blk)


dmgM, heroM, nM = knight_block(M, True); dmg17, hero17, n17 = knight_block(R17, True)
dmgP, heroP, nP = knight_block(M.but(heroic_die='pool'), True)
check('manuscript, by the author\'s ruling: the Knight\'s heroic die is added to the two highest block dice',
      (not heroM) and nM == 2 and dmgM == max(0, 8 - sum(sorted(max(E.DIE[d]) for d in Char('Knight', M).blk)[-2:]) - max(E.DIE['u'])), (dmgM, nM))
check('the other reading (the heroic die joins the pool and the two highest of all count) is still available',
      (not heroP) and dmgP == 8 - sum(sorted([max(E.DIE[d]) for d in Char('Knight', M).blk] + [max(E.DIE['u'])])[-2:]), (dmgP, nP))
check('official: every die counts, the heroic die included',
      (not hero17) and dmg17 == max(0, 8 - sum(max(E.DIE[d]) for d in Char('Knight', R17).blk) - max(E.DIE['u'])), (dmg17, n17))

# ---------------------------------------------------------------- poison is not resolved once the encounter is cleared
c = Char('Knight', R22); f = E.Fight([c], R22, random.Random(0), enemies=['Hollow Soldier']); foe = f.foes[0]
c.dmg = c.cap; c.poison = 1; foe.hp = 0; f.end_turn(c); cleared_alive = c.alive
c = Char('Knight', R22); f = E.Fight([c], R22, random.Random(0), enemies=['Hollow Soldier']); c.dmg = c.cap; c.poison = 1; f.end_turn(c)
check('poison does not kill a character whose turn cleared the encounter, and does while an enemy stands', cleared_alive and not c.alive)

# ---------------------------------------------------------------- 2022: luck may re-roll one dodge die of the combined roll
class Script:
    """Dice by script: random() gives the listed values in turn (then 0.99); choice() gives the lowest face."""
    def __init__(self, vals): self.vals = list(vals)
    def random(self): return self.vals.pop(0) if self.vals else 0.99
    def choice(self, seq): return min(seq)


c = Char('Assassin', R22); f = E.Fight([c], R22, random.Random(0), enemies=['Sentinel'], policy=E.Policy(evade=0.0)); foe = f.foes[0]
foe.node = E.IDX[(4, 4)]; c.node = E.IDX[(0, 0)]; c.heroic = False; nd = c.dodge
f.rng = Script([0.5, 0.99] + [0.1] * (nd - 1) + [0.1]); hit = f.defend(foe, c, 7, False, nd)     # (the evade check,) one die short, then luck succeeds
check('official 2022: one dodge die short, luck re-rolls that die and the attack is dodged', hit is False and not c.luck and c.dmg == 0, (hit, c.luck, c.dmg))

# ---------------------------------------------------------------- an upgrade stays on a weapon passed through the shared inventory
k = Char('Knight', R17); w = Char('Warrior', R17); eco = Economy([k, w], R17, random.Random(1))
sword = ITEMS['Balder Side Sword']; shard = ITEMS['Titanite Shard']
k.R = sword; k.refresh(); eco.equip(k, shard, k.tier, 'U'); eco.equip(k, ITEMS['Long Sword'], k.tier, 'R')
in_inv = sword in eco.inv and 'Balder Side Sword' in eco.carried and 'Balder Side Sword' not in k.plus
mods0 = [a['mod'] for a in sword['attacks'] if a['dice']]
eco.inv.remove(sword); eco.equip(w, sword, w.tier, 'R'); mods = [o['mod'] for o in w.options['R']]
check('official: an upgraded weapon keeps its upgrade when another character takes it from the shared inventory',
      in_inv and mods == [m + 1 for m in mods0] and not eco.carried, (in_inv, mods0, mods))

# ---------------------------------------------------------------- stats only at a rest (section 17.2)
from compare import REVIEW_GATE
RG = RU.make(REVIEW_GATE)
check('17.2: stats are raised only at a rest, the shop is open between encounters, sparks six less the characters, tier four at twelve souls',
      RG.free_visit == 'shop' and [RG.sparks(n) for n in (1, 2, 3, 4)] == [5, 4, 3, 2] and RG.tier_cost == (2, 4, 8, 12) and RG.tier4 == 5)
c = Char('Knight', RG); eco = Economy([c], RG, random.Random(1)); c.souls = 20; t0 = list(c.tier); eco.spend(levels=False)
check('17.2: a visit to Andre between encounters raises no stat', c.tier == t0, (t0, c.tier))
g0 = [play(2, RG, s, table=Table(skill=1.0)) for s in range(30)]; g1 = [play(2, RG, s, table=Table(skill=1.0, bank=6)) for s in range(30)]
check('17.2: a party that goes back to bank its souls rests more often', sum(x['rests'] for x in g1) > sum(x['rests'] for x in g0),
      (sum(x['rests'] for x in g0), sum(x['rests'] for x in g1)))

# ---------------------------------------------------------------- equipment data
check('every starting item is met by its class at base stats',
      all(Char(k, R17).cost_to_meet(CARDS[n]['req'])[0] == 0 for k, v in CLASSES.items() for n in v['start']))
check('stat costs: tier one 2, tier two 4, tier three 8', Char('Knight', R17).cost_to_meet([40, 0, 0, 0])[0] == 14)
check('official deck: 56 common cards and five class cards a character',
      len(Economy([Char('Knight', R17)], R17, random.Random(0)).deck) == 61)
check('Halberd asks for 18 strength and 31 faith (the author\'s card tables)', ITEMS['Halberd']['req'] == [18, 0, 0, 31], ITEMS['Halberd']['req'])

# ---------------------------------------------------------------- every owned set: the other sets' and the bosses' treasure
from characters import MORE, SPELLS, is_shield
from collections import Counter
from compare import ALL_REQ, ALL_KIND, ALL_MID
kinds = Counter(v['deck'] for v in MORE.values())
check('the other sets add 63 common, 30 class, 30 transposed and 10 legendary cards, and 56 boss treasure cards',
      (kinds['common'], kinds['class'], kinds['transposed'], kinds['legendary'], kinds['boss']) == (63, 30, 30, 10, 56), dict(kinds))
_ra = RU.make(dict(ALL_REQ, sets='2017')); _ea = Economy([Char('Knight', _ra)], _ra, random.Random(2))
check('no card of the other sets shares a name with a core card; the 22 starting cards of the six other classes are in no treasure deck',
      not set(MORE) & set(ITEMS) and kinds['starting'] == 22 and not any(i['deck'] == 'starting' for i in _ea.t1 + _ea.t2 + _ea.shop1))
check('every transposed card asks for 25 or more in a stat', all(max(v['req']) >= 25 for d in (ITEMS, MORE) for v in d.values() if v['deck'] == 'transposed'))
check('a spell with no attack is not counted as a shield', not is_shield(ITEMS['Force']) and not is_shield(MORE['Magic Barrier']) and is_shield(MORE['Buckler']))
from characters import TRAITS, NOT_PLAYED, CARDS as _CARDS
_texts = {(v.get('text') or '').rstrip('.') for v in _CARDS.values() if v.get('text')}
check('every text printed on a card is either played or listed as not played with its reason', not (_texts - set(TRAITS) - set(NOT_PLAYED)),
      sorted(_texts - set(TRAITS) - set(NOT_PLAYED)))
check('an upgrade card carries the traits its text gives; one whose text is not played is never fitted',
      MORE['Titanite Scale']['up'] == ('mod',) and MORE['Old Leo Ring']['up'] == ('leo',) and MORE['Raw Gem']['up'] == ('w_raw',)
      and ITEMS['Titanite Shard']['up'] == ('mod',) and ITEMS['Heavy Gem']['up'] == ('die',) and MORE['Binoculars']['up'] is None)
sizes = {}
for name, spec in (('req', ALL_REQ), ('kind', ALL_KIND), ('mid', ALL_MID)):
    rr = RU.make(dict(spec, sets='2017')); e = Economy([Char('Knight', rr), Char('Herald', rr)], rr, random.Random(1))
    one = e.t1 + e.shop1; e.boss_named('Gargoyle', 0); n2 = len(e.t2)
    sizes[name] = (len(one), n2, sum(max(i['req']) >= 25 for i in one), sum(i['deck'] == 'class' for i in e.t2))
    e.after_mini_boss(); e.boss_named('Dancer of the Boreal Valley', 1)
    sizes[name] += (sum(i['deck'] == 'boss' for i in e.t2), sum(i['deck'] == 'legendary' for i in e.t2), len(e.shop2))
check('every set, by requirement: 94 cards in tier one, none asking 25; 125 in tier two, thirty of them class cards; the two bosses\' six cards and five legendaries join after the mini-boss',
      sizes['req'] == (94, 125, 0, 30, 6, 5, 12), sizes['req'])
check('every set, by kind: 169 cards in tier one (common and class), the 50 transposed cards in tier two', sizes['kind'][:2] == (169, 50) and sizes['kind'][3] == 0, sizes['kind'])
check('every set, the middle way: class cards all in tier one, common cards split at 25', sizes['mid'][:2] == (124, 95) and sizes['mid'][3] == 0, sizes['mid'])
rc = RU.make(dict(ALL_REQ, sets='core')); e = Economy([Char('Knight', rc)], rc, random.Random(1)); e.boss_named('Gargoyle', 0)
check('with the core set alone no other card and no boss treasure is in play', len(e.t1 + e.shop1 + e.t2) == 96 and not e.boss_loot, len(e.t1 + e.shop1 + e.t2))
ga = [play(2, RU.make(ALL_REQ), s, table=Table(skill=1.0, bank=6)) for s in range(12)]
check('a game with every set in play runs to its end', all(x['win'] or x['lost_at'] is not None for x in ga))

def blocked(armour, trials=600, magic=False, dodge_first=False):
    """Mean damage a Knight in `armour` takes from 6 with heroic action and luck spent: blocking, or after a failed dodge."""
    tot = 0
    for s in range(trials):
        c = Char('Knight', RG); c.A = armour; c.refresh()
        f = E.Fight([c], RG, random.Random(s), enemies=['Hollow Soldier'], policy=E.Policy(evade=0.0))
        c.heroic = c.luck = False; c.can_parry = False; foe = f.foes[0]; foe.node = E.IDX[(4, 4)]; c.node = E.IDX[(0, 0)]
        if dodge_first: c.blk = c.res = ''; c.dodge = 1                    # nothing to block with: the dodge is tried, and cannot succeed
        else: c.dodge = 0
        f.defend(foe, c, 6, magic, 9); tot += c.dmg
    return tot / trials
iron = MORE['Black Iron Armour']; plain = dict(iron, block_mod=0, resist_mod=0); best = dict(iron, block_mod=1, resist_mod=1)
b0, b1, b2 = blocked(plain), blocked(iron), blocked(best)
check('a block takes the modifier printed on the equipment: -1 lets about one more damage through, +1 about one less', 0.6 < b1 - b0 <= 1.0 and 0.5 < b0 - b2 <= 1.0, (b2, b0, b1))
r0, r1 = blocked(plain, magic=True), blocked(iron, magic=True)
check('a resist roll takes the printed resist modifier', 0.6 < r1 - r0 <= 1.0, (r0, r1))
d0, d1 = blocked(plain, dodge_first=True), blocked(iron, dodge_first=True)
check('the armour roll after a failed dodge takes the armour\'s own modifier', 0.6 < d1 - d0 <= 1.0, (d0, d1))

def twin_kills(far, trials=400):
    """How often one light attack of the Gotthard Twinswords (two repetitions) fells two Hollow Soldiers."""
    n = 0
    for s in range(trials):
        c = Char('Knight', RG); c.tier = [3, 3, 3, 3]; c.R = ITEMS['Gotthard Twinswords']; c.L = None; c.refresh()
        f = E.Fight([c], RG, random.Random(s), enemies=['Hollow Soldier', 'Hollow Soldier'], policy=E.Policy(evade=0.0))
        a, b = f.foes; c.node = a.node = E.IDX[(0, 0)]; b.node = E.IDX[(4, 4)] if far else a.node
        f.strike(c, a, c.options['R'][0]); n += a.hp <= 0 and b.hp <= 0
    return n / trials
tk, tf = twin_kills(False), twin_kills(True)
check('an attack that repeats takes a new target within reach when the first has fallen, and none out of reach', tk > 0.6 and tf == 0, (tk, tf))

def frozen_walk(frost, spent=9):
    """A Knight with `spent` stamina on the bar and no attack it can afford walks towards a far enemy: (moved, stamina after)."""
    c = Char('Knight', R17); f = E.Fight([c], R17, random.Random(3), enemies=['Hollow Soldier'], policy=E.Policy(evade=0.0, kite=False))
    foe = f.foes[0]; c.node = E.IDX[(0, 0)]; foe.node = E.IDX[(4, 4)]; c.sta = spent; c.frost = frost; c.estus = c.luck = c.heroic = False
    start = c.node; f.char_turn(c); return c.node != start, c.sta
w0, w1, w2 = frozen_walk(False), frozen_walk(True), frozen_walk(True, spent=12)
check('official 2017: the walk towards a far enemy costs a frostbitten character one stamina, and is not made when the bar is full',
      w0[0] and w1[0] and w1[1] == w0[1] + 1 and not w2[0], (w0, w1, w2))

# ---------------------------------------------------------------- the text of the cards: conditions, upgrades, rings, spells
from characters import ALL10, text_traits
def duel(cls, rules, enemies=('Hollow Soldier',), seed=1, boss=None, party=None, **pol):
    cs = party or [Char(cls, rules)]
    f = E.Fight(cs, rules, random.Random(seed), enemies=None if boss else list(enemies), boss=boss, policy=E.Policy(evade=0.0, **pol))
    for c in cs: c.node = E.IDX[(0, 0)]
    for x in f.foes: x.node = E.IDX[(0, 0)]; x.hp = x.max = 50
    return (cs[0] if not party else cs), f
hit0 = lambda c, **kw: dict(c.options['R'][0], dice='', mod=0, **kw)        # a blow that lands and does no damage of its own
c, f = duel('Knight', RG); foe = f.foes[0]; f.strike(c, foe, hit0(c, fx=['bleed'])); one = (foe.bleed, foe.hp); f.strike(c, foe, hit0(c, fx=['bleed']))
check('the workshop rules: a bleed token alone does nothing; a second one deals three damage and both come off', one == (True, 50) and foe.hp == 47 and not foe.bleed, (one, foe.hp))
c, f = duel('Knight', R17); foe = f.foes[0]; f.strike(c, foe, hit0(c, fx=['bleed'])); f.strike(c, foe, dict(c.options['R'][0], dice='', mod=3))
check('official: a bleeding enemy takes two more from the next damage it suffers', foe.hp == 50 - (3 - foe.armor) - 2 and not foe.bleed, foe.hp)
c, f = duel('Knight', RG); foe = f.foes[0]; f.strike(c, foe, hit0(c, fx=['poison'])); f.strike(c, foe, hit0(c, fx=['poison'])); f.end_activation(foe); a1 = (foe.hp, foe.poison); f.end_activation(foe)
check('the workshop rules: poison stacks; a damage a token at the end of the enemy\'s turn, and one token comes off', a1 == (48, 1) and foe.hp == 47 and foe.poison == 0, (a1, foe.hp))
c, f = duel('Knight', R17); foe = f.foes[0]; f.strike(c, foe, hit0(c, fx=['poison'])); f.strike(c, foe, hit0(c, fx=['poison'])); f.end_activation(foe)
check('official: poison is one damage at the end of the enemy\'s activation, then it is gone', foe.hp == 49 and foe.poison == 0, (foe.hp, foe.poison))
c, f = duel('Knight', RG); foe = f.foes[0]; f.strike(c, foe, hit0(c, fx=['stagger'], push=True))
check('a weapon that staggers and pushes: the enemy is staggered and stands on another node', foe.stagger and foe.node != c.node)
c, f = duel('Knight', RG, boss='Gargoyle'); foe = f.foes[0]; f.strike(c, foe, hit0(c, push=True, fx=['poison']))
check('a boss takes a condition and is never pushed by a character', foe.node == c.node and foe.poison == 1)
c = Char('Knight', RG); c.R = ITEMS['Halberd']; c.L = None; c.tier = [4, 4, 4, 4]; c.refresh(); base = [dict(o) for o in c.options['R']]
def with_ups(*names):
    c.plus = {'Halberd': sum((CARDS[n]['up'] for n in names), ())}; c.refresh(); return c.options['R']
g = with_ups('Blood Gem', 'Lightning Gem')
check('gems: Blood Gem adds bleed and Lightning Gem makes the attacks magical, on a weapon with two upgrade slots',
      ITEMS['Halberd']['slots'] == 2 and all('bleed' in o['fx'] and o['magic'] for o in g))
g = with_ups('Raw Gem', 'Simple Gem')
check('gems: Raw Gem adds two damage for two stamina; Simple Gem takes one stamina off the dearest attack',
      [o['mod'] - b['mod'] for o, b in zip(g, base)] == [2, 2] and [o['cost'] - b['cost'] for o, b in zip(g, base)] == [2, 1], [(o['cost'], o['mod']) for o in g])
c.plus = {}; c.refresh(); eco = Economy([c], RG, random.Random(1)); eco.shop1 = []; eco.shop2 = []
c.bag += [ITEMS['Titanite Shard'], ITEMS['Titanite Shard'], ITEMS['Titanite Shard']]; c.souls = 0; eco.spend()
check('a weapon takes as many upgrades as it has slots, and no more', len(c.up_cards.get('Halberd', [])) == 2 and c.plus['Halberd'] == ('mod', 'mod'), c.up_cards)
c = Char('Knight', RG); cap0 = c.cap; d0 = [o['dice'] for o in c.options['R']]; c.plus = {c.A['name']: CARDS['Hornet Ring']['up'] + CARDS['Life Ring']['up']}; c.refresh()
check('rings are fitted to the armour: the Hornet Ring adds an orange die at -2 to every attack, the Life Ring a place for one more cube',
      [o['dice'] for o in c.options['R']] == [x + 'o' for x in d0] and c.cap == cap0 + 1, (c.cap, [o['dice'] for o in c.options['R']]))
c = Char('Assassin', RG); n0 = c.dodge; c.A = CARDS["Havel's Armour"]; c.refresh()
check("Havel's Armour: no dodge dice at all, whatever else is worn", n0 > 0 and c.dodge == 0 and 'no_walk' in c.traits)
def dodge_cost(armour):
    c, f = duel('Assassin', RG); c.A = CARDS[armour]; c.L = None; c.refresh(); c.blk = c.res = c.arm_blk = c.arm_res = ''; c.luck = c.heroic = False; c.can_parry = False
    f.defend(f.foes[0], c, 6, False, 0); return c.sta
check('the price of a dodge follows the armour: one stamina, none in Black Leather Armour, two in Eastern Armour',
      (dodge_cost('Assassin Armour'), dodge_cost('Black Leather Armour'), dodge_cost('Eastern Armour')) == (1, 0, 2),
      (dodge_cost('Assassin Armour'), dodge_cost('Black Leather Armour'), dodge_cost('Eastern Armour')))
def poisoned(shield):
    c, f = duel('Knight', RG); c.L = CARDS[shield]; c.refresh(); c.dodge = 0; c.can_parry = False; f.defend(f.foes[0], c, 9, False, 9, effects=('poison', 'bleed')); return c.poison, c.bleed
check('the Spider Shield keeps poison off, and nothing else', poisoned('Spider Shield') == (0, True) and poisoned('Kite Shield (Knight)') == (1, True), (poisoned('Spider Shield'), poisoned('Kite Shield (Knight)')))
c, f = duel('Knight', RG); c.plus = {c.A['name']: CARDS['Blue Tearstone Ring']['up'] + CARDS['Sun Princess Ring']['up']}; c.refresh(); c.sta = 3; c.dodge = 0; c.can_parry = False
f.defend(f.foes[0], c, 9, False, 9); s1 = c.sta; d1 = c.dmg; f.end_turn(c)
check('the Blue Tearstone Ring gives a stamina back after damage; the Sun Princess Ring heals one at the end of the activation', s1 == 2 and d1 > 0 and c.dmg == d1 - 1, (s1, d1, c.dmg))
# catalysts and stored spells
h = Char('Herald', RG); h.tier = [0, 0, 0, 2]; h.L = ITEMS['Talisman']; h.spells = [ITEMS['Heal']]; h.refresh()
ho = Char('Herald', R17); ho.tier = [0, 0, 0, 2]; ho.L = ITEMS['Talisman']; ho.spells = [ITEMS['Heal']]; ho.refresh()
check('the manuscript: a talisman in the hand gives the actions of a miracle stored in it; the official rules have no catalysts',
      any(o['name'] == 'Heal' for o in h.support['L']) and not any(o['name'] == 'Heal' for o in ho.support['L']))
h.tier = [0, 0, 0, 0]; h.refresh()
check('a stored spell whose requirement is not met gives nothing', not any(o['name'] == 'Heal' for o in h.support['L']))
k = Char('Knight', RG); h = Char('Herald', RG); h.tier = [0, 0, 0, 2]; h.L = ITEMS['Talisman']; h.spells = [ITEMS['Heal']]; h.refresh()
(k, h), f = duel(None, RG, party=[k, h]); k.dmg = 6; h.sta = 0; f.foes[0].node = E.IDX[(4, 4)]; h.heroic = False; f.char_turn(h)
check('a Herald with Heal stored in the talisman heals a badly wounded Knight within range', k.dmg == 2 and f.dec.get('support') == 1, (k.dmg, f.dec))
eco = Economy([h], RG, random.Random(1)); fit = eco.fit(h, MORE['Med Heal'])
check('a miracle found as treasure is valued as a spell to store in the talisman', fit is not None and fit[3] == 'S', fit)
# attacks with text
c, f = duel('Knight', RG, enemies=['Hollow Soldier'] * 3); a, b, d = f.foes; b.node = E.IDX[(1, 1)]; d.node = E.IDX[(4, 4)]
f.strike(c, a, dict(c.options['R'][0], dice='', mod=5, area=1))
check('an attack that hits every enemy within range 1 leaves a farther one alone', a.hp < 50 and b.hp < 50 and d.hp == 50, (a.hp, b.hp, d.hp))
c, f = duel('Knight', RG, enemies=['Hollow Soldier'] * 2); a, b = f.foes; a.hp = 1
f.strike(c, a, dict(c.options['R'][0], dice='', mod=5, repeat=3, same='enemy'))
check('repetitions that must all be aimed at one enemy stop when it falls', a.hp <= 0 and b.hp == 50, (a.hp, b.hp))
c, f = duel('Knight', RG, enemies=['Hollow Soldier'] * 2); a, b = f.foes; f.strike(c, a, dict(c.options['R'][0], dice='', mod=0, direct=3)); both = a.hp
b.node = E.IDX[(4, 4)]; f.strike(c, a, dict(c.options['R'][0], dice='', mod=0, direct=3))
check('Rapport: three damage to an enemy that shares its node with another, nothing to one that stands alone', both == 47 and a.hp == 47, (both, a.hp))
c, f = duel('Knight', RG); c.dmg = 3; f.strike(c, f.foes[0], dict(c.options['R'][0], gain_hp=1, self_dmg=0)); g1 = c.dmg; f.strike(c, f.foes[0], dict(c.options['R'][0], self_dmg=4))
check('an attack that heals its user, and one that costs it health', g1 == 2 and c.dmg == 6, (g1, c.dmg))
c = Char('Thief', RG)
check('the Iron Round Shield stays in the hand beside a two-handed bow', c.R['hands'] == 2 and c.L is not None and 'offhand' in text_traits(c.L), (c.R['name'], c.L and c.L['name']))
# the act-first ring
def first_blood(ring):
    tot = 0
    for sd in range(20):
        c, f = duel('Knight', RG, seed=sd); c.blk = c.arm_blk = ''; c.dodge = 0; c.can_parry = False
        if ring: c.plus = {c.A['name']: CARDS['Mon Ring']['up']}; c.traits = c.traits | {'mon'}; c.mon = True
        f.foes[0].hp = 1; f.run(max_rounds=1); tot += c.dmg
    return tot
check('the Mon Ring: the party acts before the enemies once, so an enemy that falls to the first blow never strikes', first_blood(True) == 0 and first_blood(False) > 0, (first_blood(True), first_blood(False)))
# the six other classes and their heroic actions
check('ten classes: each starts with its own cards and can meet their requirements',
      len(ALL10) == 10 and all(Char(k, RG).R is not None and Char(k, RG).A is not None for k in ALL10))
s_, f = duel('Sorcerer', RG); foe = f.foes[0]; foe.node = E.IDX[(4, 4)]; s_.tier = [0, 0, 0, 0]; s_.sta = 0; s_.node = E.IDX[(0, 0)]; f.pol.kite = False; f.char_turn(s_)
check('Spell Fury: the Sorcerer strikes an enemy across the tile without moving, and the token is spent', foe.hp < 50 and not s_.heroic and s_.node == E.IDX[(0, 0)], (foe.hp, s_.heroic, s_.node))
m, f = duel('Mercenary', RG); m.options['R'] = [o for o in m.options['R'] if o['cost'] >= 2]; m.options['L'] = []; m.sta = 0; f.pol.kite = False; f.char_turn(m)
check('Rapid Strike: the Mercenary makes its costly attack for no stamina', not m.heroic and m.sta == 0 and f.foes[0].hp < 50, (m.heroic, m.sta, f.foes[0].hp))
py = Char('Pyromancer', RG); _, f = duel(None, RG, party=[py]); v = [o for o, hero, _ in f.variants(py, next(o for o in py.options['R'] + py.options['L'] if o['cost'] >= 2), 0)]
check('Explosive Crit: one attack of the Pyromancer gains a black die', len(v) == 2 and v[1]['dice'] == v[0]['dice'] + 'b', [o['dice'] for o in v])
cl, k = Char('Cleric', RG), Char('Knight', RG); (cl, k), f = duel(None, RG, party=[cl, k]); cl.dmg = 2; k.dmg = 5; f.pol.kite = False; f.char_turn(cl)
check('the Cleric\'s heroic action heals two damage on itself and on a character within a node', (cl.dmg, k.dmg) <= (0, 3) and not cl.heroic, (cl.dmg, k.dmg, cl.heroic))
th, f = duel('Thief', RG); th.dmg = 4; th.sta = 3; f.pol.kite = False; f.foes[0].node = E.IDX[(4, 4)]; h0 = th.heroic; f.char_turn(th)
check('the Thief\'s heroic action heals two damage and gives back two stamina', h0 and not th.heroic and th.dmg <= 2, (th.dmg, th.sta))
ra = RU.make(dict(ALL_REQ, roster='all')); gg = [play(3, ra, sd, table=Table(skill=1.0, bank=6)) for sd in range(40)]
seen = {x for g_ in gg for x in g_['classes']}
check('with every class in the roster, games of all ten classes run to their end', seen == set(ALL10) and all(g_['win'] or g_['lost_at'] is not None for g_ in gg), sorted(set(ALL10) - seen))

# ---------------------------------------------------------------- the other sets' enemies, encounters and bosses
import game as G2
core_e = sum(1 for lv in '123' for e in E.ENCOUNTERS[lv] if e['set'] == 'Core'); all_e = sum(len(E.ENCOUNTERS[lv]) for lv in '123')
check('36 core encounters and 51 of Darkroot, Iron Keep and Explorers; every enemy on them has a card', core_e == 36 and all_e == 87
      and all(x in E.ENEMIES for lv in '123' for e in E.ENCOUNTERS[lv] for x in e['enemies']), (core_e, all_e))
check('by default only the core set\'s bosses and encounters are in a game',
      [b for b in G2.MAINS if G2.in_play(RG, 'bosses', E.BOSSES[b])] == ['Dancer of the Boreal Valley', 'Ornstein & Smough']
      and len([b for b in G2.MINIS if G2.in_play(RG, 'bosses', E.BOSSES[b])]) == 4 and len(G2.MINIS) == 5 and len(G2.MAINS) == 7)
def boss_fight(name, seed=0, rules=RG):
    c = Char('Knight', rules); f = E.Fight([c], rules, random.Random(seed), boss=name, policy=E.Policy(evade=0.0, read_new=0.0, read_known=0.0)); return c, f
c, f = boss_fight('Ornstein & Smough'); o_, s_ = f.foes
n0 = len(f.pdeck); f.pair_turn(o_); f.pair_turn(s_)
check('Ornstein and Smough: two models with their own health, one card drawn a turn for both', (o_.max, s_.max) == (20, 30) and len(f.pdeck) == n0 - 1 and f.enemy_acts == 1, (n0, len(f.pdeck), f.enemy_acts))
s_.hp = 0; o_.hp = 5; f.pair_turn(o_)
check('when Smough falls Ornstein regains ten health and fights on from his own five heat-up cards', o_.hp == 15 and f.pair_heat and len(f.pdeck) + len(f.pdiscard) == 5
      and all(k.get('heatup') for k in f.pdeck + f.pdiscard), (o_.hp, len(f.pdeck)))
c, f = boss_fight('Ornstein & Smough'); o_, s_ = f.foes; o_.hp = 0; s_.hp = 20; f.pair_turn(s_)
check('when Ornstein falls Smough regains fifteen, to no more than he began with', s_.hp == 30, s_.hp)
c, f = boss_fight('Great Grey Wolf Sif'); b_ = f.foes[0]; b_.hp = 3; f.check_heat(b_); f.boss_turn(b_); f.boss_turn(b_)
check('Sif at three health or less plays Limping Strike and nothing else', [k['name'] for k in b_.deck + b_.discard] == ['Limping Strike'], [k['name'] for k in b_.deck + b_.discard])
c, f = boss_fight('Artorias'); b_ = f.foes[0]; b_.hp = b_.card['heatup']; f.check_heat(b_)
check('Artorias heats up by losing two cards and gaining all three heat-up cards', len(b_.deck) == 5 - 2 + 3 and sum(k['heatup'] for k in b_.deck) == 3, len(b_.deck))
c, f = boss_fight('Smelter Demon'); b_ = f.foes[0]; b_.hp = b_.card['heatup']; f.check_heat(b_)
check('the Smelter Demon heats up into a deck of five heat-up cards', len(b_.deck) == 5 and all(k['heatup'] for k in b_.deck))
c, f = boss_fight('Old Dragonslayer'); b_ = f.foes[0]; n0 = len(b_.deck)
for _ in range(5): f.strike(c, b_, dict(c.options['R'][0], dice='', mod=4 + b_.armor))
check('the Old Dragonslayer: the first three blows of four or more each put a heat-up card on top of its deck', len(b_.deck) == n0 + 3 and b_.surges == 3 and b_.deck[0]['heatup'], (n0, len(b_.deck)))
c, f = boss_fight('The Pursuer'); b_ = f.foes[0]; n0 = len(b_.deck); f.boss_turn(b_)
check('the Pursuer draws and resolves two cards a turn, from a deck of eight', n0 == 8 and len(b_.deck) == 6 and len(b_.discard) == 2, (n0, len(b_.deck)))
c = Char('Knight', RG); f = E.Fight([c], RG, random.Random(4), enemies=['Mushroom Parent'], policy=E.Policy(evade=0.0)); m_ = f.foes[0]
m_.node = E.NBR[c.node][0]; c.dodge = 0; c.can_parry = False; f.enemy_turn(m_)
check('a Mushroom Parent has no attack of its own: its move pushes, wounds and staggers', all(s_['k'] == 'move' for s_ in m_.card['steps']) and c.stagger and c.node != m_.node, (c.stagger, c.dmg))
bad = []
for lv in '123':
    for e_ in E.ENCOUNTERS[lv]:
        if e_['set'] == 'Core': continue
        k_, w_ = Char('Knight', RG), Char('Warrior', RG)
        for x_ in (k_, w_): x_.tier = [2, 2, 2, 2]; x_.R = ITEMS['Halberd'] if x_ is k_ else x_.R; x_.L = None if x_ is k_ else x_.L; x_.refresh()
        f = E.Fight([k_, w_], RG, random.Random(1), enemies=e_['enemies'], policy=E.Policy(skill=1.0)); f.run()
        if not f.over(): bad.append(e_['name'])
check('every encounter of the other sets plays to an end', not bad, bad)
k_ = Char('Knight', RG); f = E.Fight([k_], RG, random.Random(2), enemies=['Ironclad Soldier'], policy=E.Policy(skill=1.0)); f.run(max_rounds=12)
check('a character who can hurt a heavily armoured enemy only with its costly attack does not back away for ever', f.dec.get('heavy', 0) >= 3, dict(f.dec))
rw = RU.make(dict(ALL_REQ, roster='all', bosses='all', encounters='all')); gw = [play(2, rw, sd, table=Table(skill=1.0, bank=6)) for sd in range(40)]
check('games with every class, boss, encounter and card of the 2017 sets run to their end, and meet bosses of other sets',
      all(x['win'] or x['lost_at'] is not None for x in gw) and len({x.get('main') for x in gw}) >= 4, sorted({str(x.get('main')) for x in gw}))

# ---------------------------------------------------------------- the 2022 sets' treasure
from characters import Y22
k22 = Counter((v['conf'], v['deck']) for v in Y22.values())
check('the 2022 sets: 164 treasure cards, 126 of them reprints of cards the simulator already holds, 38 new', len(Y22) == 164
      and sum(v for (c_, d_), v in k22.items() if c_ == 'reprint') == 126 and sum(v for (c_, d_), v in k22.items() if c_ == 'community') == 38, dict(k22))
check('a reprint is played with the values of the card it reprints', all(v['req'] == CARDS[k.split(' [')[0]]['req'] for k, v in Y22.items()
      if v['conf'] == 'reprint' and k.split(' [')[0] in CARDS and CARDS[k.split(' [')[0]].get('cls') in (None, v.get('cls'))))
ry = RU.make(ALL_REQ); ey = Economy([Char('Knight', ry)], ry, random.Random(1)); r7 = RU.make(dict(ALL_REQ, sets='2017')); e7 = Economy([Char('Knight', r7)], r7, random.Random(1))
n_all = len(ey.t1 + ey.shop1 + ey.t2); n_17 = len(e7.t1 + e7.shop1 + e7.t2)
check('with every set in the decks the 2022 cards join them: 144 more common, class and transposed cards than the 2017 sets alone', n_all - n_17 == 144, (n_17, n_all))
c = Char('Knight', RG); c.R = ITEMS['Halberd']; c.L = None; c.tier = [4, 4, 4, 4]; c.refresh(); eco = Economy([c], RG, random.Random(1))
scale = next(v for v in Y22.values() if v.get('size') == 2); c.bag = [scale, ITEMS['Titanite Shard']]; eco.shop1 = []; eco.shop2 = []; eco.spend()
check('an upgrade that occupies two slots leaves no room for another on a two-slot weapon', len(c.up_cards.get('Halberd', [])) == 1, [x['name'] for x in c.up_cards.get('Halberd', [])])
c, f = duel('Knight', RG, boss='Gargoyle'); foe = f.foes[0]; f.strike(c, foe, dict(c.options['R'][0], dice='', mod=foe.armor, vs_boss=2)); hb = 50 - foe.hp
c, f = duel('Knight', RG); foe = f.foes[0]; f.strike(c, foe, dict(c.options['R'][0], dice='', mod=foe.armor, vs_boss=2, vs_hollow=1))
check('damage against bosses counts against a boss only; damage against Hollows against a Hollow', hb == 2 and 50 - foe.hp == 1, (hb, 50 - foe.hp))
def tear(dmg):
    c, f = duel('Knight', RG, seed=5); c.traits = c.traits | {'redtear'}; c.dmg = dmg; foe = f.foes[0]; f.strike(c, foe, dict(c.options['R'][0], dice='b', mod=9)); return 50 - foe.hp
check('the Red Tearstone Ring adds a damage only with four or more damage cubes on the bar', tear(4) == tear(3) + 1 and tear(0) == tear(3), (tear(0), tear(3), tear(4)))

# ---------------------------------------------------------------- review of the card-text code
c, f = duel('Assassin', RG); c.A = CARDS["Havel's Armour"]; c.refresh(); c.luck = c.heroic = False; c.can_parry = False; tried = 0
for sd in range(60):
    f.rng = random.Random(sd); c.sta = 0; c.dmg = 0; c.alive = True; f.dec = {}; f.defend(f.foes[0], c, 6, True, 1); tried += f.dec.get('dodge', 0)
check('armour that says its wearer cannot dodge allows no dodge at all, not even with a die paid for', tried == 0, tried)
c, f = duel('Knight', RG, enemies=['Sentinel']); foe = f.foes[0]; f.strike(c, foe, dict(c.options['R'][0], dice='', mod=foe.armor + 2, repeat=2, push=True))
check('a repetition is not made against an enemy the one before pushed out of reach', 50 - foe.hp == 2 and foe.node != c.node, 50 - foe.hp)
c, f = duel('Knight', R17, enemies=['Sentinel']); foe = f.foes[0]; foe.poison = 1; foe.bleed = True; f.end_activation(foe)
check('official: poison damage sets off a bleed token on an enemy', foe.hp == 47 and not foe.bleed, (foe.hp, foe.bleed))
c, f = duel('Knight', R17, enemies=['Sentinel']); foe = f.foes[0]; c.traits = c.traits | {'thorns'}; c.dodge = 0; c.can_parry = False; f.defend(foe, c, 1, False, 9, push=True)
check('Armour of Thorns answers an attack from its wearer\'s node even when the attack pushes the wearer away', foe.hp == 49 and c.node != foe.node, (foe.hp, c.node == foe.node))

def thorns_after(rules, how):
    """Failed defences of the given kind over many seeds, and the health the attacker lost to Armour of Thorns in them."""
    fails = lost = 0
    for sd in range(120):
        c, f = duel('Knight', rules, enemies=['Sentinel'], seed=sd); foe = f.foes[0]; c.traits = c.traits | {'thorns'}; c.luck = c.heroic = False
        c.blk = c.res = ''; c.dodge = 1; c.can_parry = how == 'parry'; c._rip = 9.0 if how == 'parry' else 0.0
        if how == 'bare': c.arm_blk = c.arm_res = ''
        f.dec = {}; d0 = c.dmg; f.defend(foe, c, 6, False, 1)
        if f.dec.get('parry' if how == 'parry' else 'dodge') and (c.dmg > d0 or not c.alive): fails += 1; lost += 50 - foe.hp
    return fails, lost
tp, td, ta = thorns_after(RG, 'parry'), thorns_after(R17, 'bare'), thorns_after(RG, 'dodge')
check('Armour of Thorns answers only a defence that rolled block or resist dice: not a failed parry, not an official failed dodge',
      tp[0] >= 10 and tp[1] == 0 and td[0] >= 10 and td[1] == 0, (tp, td))
check('and it does answer a manuscript failed dodge, which rolls the armour\'s dice', ta[0] >= 10 and ta[1] == ta[0], ta)

w = Char('Warrior', R17); eco = Economy([w], R17, random.Random(1)); sword = ITEMS['Balder Side Sword']; gem = ITEMS['Crystal Gem']
eco.inv.append(sword); bare = eco.fit(w, sword); eco.carried[sword['name']] = (gem['up'], [gem]); geared = eco.fit(w, sword)
need = lambda f: None if f is None else [w.value(i, f[2][i]) for i in range(4)]
check('official: a weapon taken from the shared inventory with a gem fitted asks for the gem\'s stats as well as its own',
      bare is not None and (geared is None or need(geared)[2] >= gem['req'][2]) and need(bare)[2] < gem['req'][2], (need(bare), need(geared), gem['req']))

def tearstone(rules, frost):
    c, f = duel('Knight', rules, enemies=['Sentinel']); c.traits = c.traits | {'tearstone'}; c.sta = 3; c.frost = frost; c.dodge = 0; c.can_parry = False
    f.defend(f.foes[0], c, 9, False, 9); return c.sta, c.dmg > 0
check('the manuscript\'s frostbite bars the stamina the Blue Tearstone Ring gives back; without frostbite, and under the official rules, it is given',
      tearstone(RG, True) == (3, True) and tearstone(RG, False) == (2, True) and tearstone(R17, True) == (2, True),
      (tearstone(RG, True), tearstone(RG, False), tearstone(R17, True)))

print()
print('%d checks failed' % len(FAILS) if FAILS else 'all checks passed')
sys.exit(1 if FAILS else 0)
