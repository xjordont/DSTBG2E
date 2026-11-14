#!/usr/bin/env python3
"""Single fights at equal party strength, to compare how rulesets scale with the number of characters.

Every party is equipped the same way whatever the ruleset: each character brings a fixed budget of souls for the
stage of the game (BUDGET), pooled and spent on blind treasure draws and level-ups as in the official rules. The
party then fights one random encounter of the level (or one random boss) from a full rest. So differences between
rulesets in this table come from the combat and scaling rules alone, not from their economies.

Usage: python3 tools/sim/fights.py [--games 600] [--skill 0.5]
"""
import argparse, os, random, sys
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rules as RU
from engine import Fight, Policy, ENCOUNTERS, BOSSES
from characters import Char, Economy, CORE4

BUDGET = {1: 0, 2: 8, 'mini': 14, 3: 26, 'main': 36}          # souls a character has earned by that stage (a judgement)
STAGES = (1, 2, 'mini', 3, 'main')


def one(job):
    spec, n, stage, seeds, skill = job
    r = RU.make(spec); out = []
    for s in seeds:
        rng = random.Random(s)
        cls = [rng.choice(CORE4[:2])] if n == 1 else rng.sample(CORE4, n)
        party = [Char(c, r) for c in cls]
        shop = RU.OFFICIAL_2017.but(block=r.block, dodge_fail=r.dodge_fail, parry=r.parry, tier4=None, hollow_bar=r.hollow_bar, bar=r.bar)
        eco = Economy(party, shop, rng)
        if stage in (3, 'main'): eco.after_mini_boss()
        eco.pool = BUDGET[stage] * n; eco.spend()
        for c in party: c.r = r; c.refresh(); c.full_rest()
        pol = Policy(skill=skill)
        if stage in ('mini', 'main'):
            f = Fight(party, r, rng, boss=rng.choice([b for b, v in BOSSES.items() if v['kind'] == stage]), policy=pol)
        else:
            f = Fight(party, r, rng, enemies=rng.choice(ENCOUNTERS[str(stage)])['enemies'], policy=pol)
        ok = f.run()
        out.append((ok, f.rounds, f.deaths > 0, f.char_turns + f.enemy_acts, sum(c.dmg for c in party if c.alive) / n))
    return out


def table(specs, games=600, skill=0.5, procs=4):
    res = {}
    with Pool(procs) as pool:
        jobs = []; keys = []
        for name, spec in specs.items():
            for stage in STAGES:
                for n in (1, 2, 3, 4):
                    keys.append((name, stage, n)); jobs.append((spec, n, stage, list(range(games)), skill))
        for k, out in zip(keys, pool.map(one, jobs, chunksize=1)):
            N = len(out)
            res[k] = dict(win=sum(o[0] for o in out) / N, rounds=sum(o[1] for o in out) / N, death=sum(o[2] for o in out) / N,
                          time=sum(o[3] for o in out) / N, hurt=sum(o[4] for o in out) / N)
    return res


def show(res, specs):
    for name in specs:
        print('\n' + name)
        print('  stage   cleared, 1/2/3/4 characters   rounds                someone dies         table time (activations)')
        for stage in STAGES:
            row = [res[(name, stage, n)] for n in (1, 2, 3, 4)]
            print('  %-6s  %s     %s     %s     %s' % (
                stage, ' / '.join('%3.0f%%' % (100 * x['win']) for x in row), ' / '.join('%4.1f' % x['rounds'] for x in row),
                ' / '.join('%3.0f%%' % (100 * x['death']) for x in row), ' / '.join('%3.0f' % x['time'] for x in row)))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--games', type=int, default=600); ap.add_argument('--skill', type=float, default=1.0)
    ap.add_argument('--specs'); a = ap.parse_args()
    if a.specs:
        import json
        specs = json.load(open(a.specs)); show(table(specs, a.games, a.skill), specs); sys.exit(0)
    from compare import PROPOSED_A, PROPOSED_B
    specs = {'Official 2017': {'base': 'official2017'},
             "Author's manuscript, as written": {'base': 'manuscript'},
             'Proposal A (section 13.4)': PROPOSED_A,
             'Proposal B (section 13.4)': PROPOSED_B}
    show(table(specs, a.games, a.skill), specs)
