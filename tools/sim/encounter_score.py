#!/usr/bin/env python3
"""Score encounters (lists of enemy names) by single fights at equal party strength, as fights.py equips its parties,
under the settled ruleset. Used to balance the print-and-play encounter decks against the printed 2017 encounters.

For each encounter and party size: fights won, fights in which a character died, damage carried out by a surviving
character, rounds. The score is one number per encounter: the mean over party sizes of
damage carried + 5 x (share of fights with a death) + 10 x (share of fights lost).

Usage: python3 tools/sim/encounter_score.py FILE.json [--games 200] [--sizes 1 2 3 4]
FILE.json: {"1": [{"name": ..., "enemies": [...]}, ...], "2": [...], "3": [...]}; "core" scores the printed core set."""
import argparse, json, os, random, sys
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rules as RU
from engine import Fight, Policy, ENCOUNTERS
from characters import Char, Economy, CORE4
from compare import SPECS
from fights import BUDGET


def one(job):
    level, enemies, n, seeds = job
    r = RU.make(dict(SPECS['settled'][1])); out = []
    for s in seeds:
        rng = random.Random(s)
        cls = [rng.choice(CORE4[:2])] if n == 1 else rng.sample(CORE4, n)
        party = [Char(c, r) for c in cls]
        shop = RU.OFFICIAL_2017.but(block=r.block, dodge_fail=r.dodge_fail, parry=r.parry, tier4=None, hollow_bar=r.hollow_bar, bar=r.bar)
        eco = Economy(party, shop, rng)
        if level == 3: eco.after_mini_boss()
        eco.pool = BUDGET[level] * n; eco.spend()
        for c in party: c.r = r; c.refresh(); c.full_rest()
        f = Fight(party, r, rng, enemies=list(enemies), policy=Policy(skill=1.0))
        ok = f.run()
        out.append((ok, f.deaths > 0, sum(c.dmg for c in party if c.alive) / n, f.rounds))
    N = len(out)
    return dict(win=sum(o[0] for o in out) / N, death=sum(o[1] for o in out) / N, hurt=sum(o[2] for o in out) / N, rounds=sum(o[3] for o in out) / N)


def score(decks, games=200, sizes=(1, 2, 3, 4), procs=4):
    jobs = []; keys = []
    for lv in ('1', '2', '3'):
        for e in decks.get(lv, []):
            for n in sizes:
                keys.append((lv, e['name'], n)); jobs.append((int(lv), e['enemies'], n, list(range(games))))
    with Pool(procs) as pool: res = dict(zip(keys, pool.map(one, jobs, chunksize=2)))
    out = {}
    for lv in ('1', '2', '3'):
        for e in decks.get(lv, []):
            cells = [res[(lv, e['name'], n)] for n in sizes]
            sc = sum(c['hurt'] + 5 * c['death'] + 10 * (1 - c['win']) for c in cells) / len(cells)
            out[(lv, e['name'])] = dict(score=sc, cells=cells, enemies=e['enemies'])
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('file'); ap.add_argument('--games', type=int, default=200)
    ap.add_argument('--sizes', type=int, nargs='+', default=[1, 2, 3, 4]); a = ap.parse_args()
    if a.file == 'core': decks = {lv: [e for e in ENCOUNTERS[lv] if e['set'] == 'Core'] for lv in ('1', '2', '3')}
    else: decks = json.load(open(a.file))
    out = score(decks, a.games, tuple(a.sizes))
    for lv in ('1', '2', '3'):
        rows = sorted(((v['score'], k[1], v) for k, v in out.items() if k[0] == lv))
        if not rows: continue
        sc = [r[0] for r in rows]
        print('Level %s: %d encounters, score min %.1f  median %.1f  max %.1f' % (lv, len(rows), sc[0], sc[len(sc) // 2], sc[-1]))
        for s, name, v in rows:
            print('  %5.1f  %-24s win %s  death %s  | %s' % (s, name[:24], '/'.join('%3.0f' % (100 * c['win']) for c in v['cells']),
                  '/'.join('%3.0f' % (100 * c['death']) for c in v['cells']), ', '.join(v['enemies'])))
