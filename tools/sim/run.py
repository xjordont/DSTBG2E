#!/usr/bin/env python3
"""Runs batches of simulated games in parallel and summarises them."""
import math, os, sys
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rules as RU
from game import play, Table


def _work(job):
    spec, n, seeds, tkw = job
    r = RU.make(spec); t = Table(**tkw)
    return [play(n, r, s, table=t) for s in seeds]


_pool = None


def batch(spec, n, games=2000, table=None, seed0=0, procs=4):
    """Play `games` games; returns the list of result dicts."""
    global _pool
    if _pool is None: _pool = Pool(procs)
    chunk = max(1, games // (procs * 4)); seeds = list(range(seed0, seed0 + games))
    jobs = [(spec, n, seeds[i:i + chunk], table or {}) for i in range(0, games, chunk)]
    out = []
    for part in _pool.map(_work, jobs): out += part
    return out


def ci(p, n): return 1.96 * math.sqrt(max(p * (1 - p), 1e-9) / n)


def summary(res):
    N = len(res); s = {}
    s['win'] = sum(x['win'] for x in res) / N; s['ci'] = ci(s['win'], N)
    for k in ('rests', 'fights', 'rounds', 'char_turns', 'enemy_acts', 'deaths'): s[k] = sum(x[k] for x in res) / N
    s['time'] = s['char_turns'] + s['enemy_acts']
    lv = {}
    for x in res:
        for k, d in x['by_level'].items():
            a = lv.setdefault(k, dict(n=0, rounds=0, death=0, fail=0, turns=0))
            for kk in a: a[kk] += d[kk]
    for k, a in lv.items():
        s[('rounds', k)] = a['rounds'] / a['n']; s[('death', k)] = a['death'] / a['n']; s[('fail', k)] = a['fail'] / a['n']
        s[('fights', k)] = a['n'] / N
    lost = [str(x['lost_at']) for x in res if not x['win']]
    s['lost'] = {k: lost.count(k) / N for k in sorted(set(lost))}
    return s


GRID = [dict(ready2=a, ready3=b, reserve=c) for a, b in ((-9, -9), (-2.0, -0.5), (-1.0, 0.5)) for c in (0, 1)]


def best(spec, n, skill=1, games=1500, probe=300, extra=None):
    """Lets the simulated players pick the campaign policy that suits the ruleset (on one set of seeds), then
    measures it on another. Returns (summary, policy)."""
    top = None
    for g in GRID:
        tk = dict(g, skill=skill, **(extra or {}))
        w = sum(x['win'] for x in batch(spec, n, probe, tk, seed0=10 ** 6)) / probe
        if top is None or w > top[0]: top = (w, tk)
    return summary(batch(spec, n, games, top[1])), top[1]
