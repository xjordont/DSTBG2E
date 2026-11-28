#!/usr/bin/env python3
"""The measurements behind section 38 of 41_rules_workshop.md, kept so that they can be run again.

  python3 tools/sim/measure_settled.py game [--games 500] [--probe 300] [--world 'core box'] [--chars 3 4]
                                                                           whole games, every 2017 set and the core box
  python3 tools/sim/measure_settled.py boss [--games 600]                  the bosses with a rule of their own in the simulator

`game` runs each cell twice: with players who know that the next death fails the encounter (Policy.count_dead) and
with players who do not. `boss` fights Gravelord Nito with and without his escort and Crossbreed Priscilla with and
without her invisibility, each party equipped as for a main boss (fights.BUDGET)."""
import argparse, os, random, sys
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rules as RU
from compare import SPECS, PROPOSED_20_CORE
from run import batch, summary, GRID
from engine import Fight, Policy
from characters import Char, Economy, CORE4
from fights import BUDGET

SETTLED = SPECS['settled'][1]
RULE = {k: SETTLED[k] for k in ('boss_add', 'boss_atk', 'hp_add', 'atk', 'fail_dead')}
WORLDS = {'every 2017 set': SETTLED, 'core box': dict(PROPOSED_20_CORE, **RULE)}
# how the players run the campaign at each party size (sections 28 to 38): fight reset encounters again or not, and
# the unspent souls at which they rest to spend
POL = {1: dict(regrind=0, bank=10), 2: dict(regrind=0, bank=6), 3: dict(regrind=0, bank=6), 4: dict(regrind=2, bank=6)}


def game(games, probe, worlds=None, chars=(1, 2, 3, 4)):
    print('world           chars  players    won     turns   dodge share   lost at: encounter / mini-boss / main boss   boss fights lost: mini / main')
    for wname, spec in WORLDS.items():
        if worlds and wname not in worlds: continue
        for n in chars:
            for aware in (False, True):
                top = None
                for g in GRID:
                    tk = dict(g, skill=1, count_dead=aware, **POL[n])
                    w = sum(x['win'] for x in batch(spec, n, probe, tk, seed0=10 ** 6)) / probe
                    if top is None or w > top[0]: top = (w, tk)
                res = batch(spec, n, games, top[1]); s = summary(res)
                lost = s['lost']; enc = sum(v for k, v in lost.items() if k in ('1', '2', '3'))
                d = s['dec']; dodge = d.get('dodge', 0) / max(1e-9, d.get('dodge', 0) + d.get('block', 0))
                bf = lambda k: s.get(('fail', k), 0)
                print('%-15s   %d    %-8s  %3.0f%% +/-%1.0f  %4.0f     %3.0f%%            %3.0f%% / %3.0f%% / %3.0f%%                     %3.0f%% / %3.0f%%' % (
                    wname, n, 'aware' if aware else 'unaware', 100 * s['win'], 100 * s['ci'], s['time'], 100 * dodge,
                    100 * enc, 100 * lost.get('mini', 0), 100 * lost.get('main', 0), 100 * bf('mini'), 100 * bf('main')), flush=True)


def _boss(job):
    boss, n, extra, seeds = job
    r = RU.make(dict(SETTLED, **extra)); out = []
    for s in seeds:
        rng = random.Random(s)
        cls = [rng.choice(CORE4[:2])] if n == 1 else rng.sample(CORE4, n)
        party = [Char(c, r) for c in cls]
        shop = RU.OFFICIAL_2017.but(block=r.block, dodge_fail=r.dodge_fail, parry=r.parry, tier4=None, hollow_bar=r.hollow_bar, bar=r.bar)
        eco = Economy(party, shop, rng); eco.after_mini_boss(); eco.pool = BUDGET['main'] * n; eco.spend()
        for c in party: c.r = r; c.refresh(); c.full_rest()
        f = Fight(party, r, rng, boss=boss, policy=Policy(skill=1)); ok = f.run(150)
        out.append((ok, f.deaths, f.char_turns + f.enemy_acts))
    return out


def boss(games):
    cells = [('Gravelord Nito', 'alone', dict(escort=False)), ('Gravelord Nito', 'with his escort', {}),
             ('Crossbreed Priscilla', 'always visible', dict(veil=False)), ('Crossbreed Priscilla', 'invisible as written', {})]
    jobs = [(b, n, extra, list(range(games))) for b, _, extra in cells for n in (1, 2, 3, 4)]
    with Pool(4) as pool: res = pool.map(_boss, jobs, chunksize=1)
    print('boss                    as                      fights lost, 1/2/3/4 characters   deaths a fight          turns')
    for i, (b, how, _) in enumerate(cells):
        row = res[4 * i:4 * i + 4]
        print('%-22s  %-22s  %s        %s     %s' % (b, how, ' / '.join('%3.0f%%' % (100 * (1 - sum(o[0] for o in x) / len(x))) for x in row),
              ' / '.join('%3.1f' % (sum(o[1] for o in x) / len(x)) for x in row), ' / '.join('%3.0f' % (sum(o[2] for o in x) / len(x)) for x in row)))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('what', choices=('game', 'boss'))
    ap.add_argument('--games', type=int, default=None); ap.add_argument('--probe', type=int, default=300)
    ap.add_argument('--world', choices=tuple(WORLDS), nargs='*'); ap.add_argument('--chars', type=int, nargs='*', default=[1, 2, 3, 4]); a = ap.parse_args()
    if a.what == 'game': game(a.games or 500, a.probe, a.world, a.chars)
    else: boss(a.games or 600)
