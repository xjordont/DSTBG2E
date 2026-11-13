#!/usr/bin/env python3
"""Search the scaling rules with tools/sim_game.py: which rule gives two, three and four characters the same
win rate as a lone character, with Level 3 encounters of four to seven rounds?

  python3 tools/sim_search.py solo              # solo win rate by difficulty setting and starting souls
  python3 tools/sim_search.py grid REACH [games]   # every candidate rule for 2, 3 and 4 characters at that setting
"""
import sys, random, statistics as st, math, itertools
from multiprocessing import Pool
sys.path.insert(0, __file__.rsplit('/', 1)[0]); import sim_game as G

HEALTH = {'+1': G.PLUS(1), '+2': G.PLUS(2), '+3': G.PLUS(3), 'half': G.HALF, 'x n': lambda h, n: h * n}

def run(args):
    n, reach, hname, atk, reps, souls, sparks, games, seed = args
    random.seed(seed); G.REACH = reach
    rule = dict(hp=HEALTH[hname], atk=lambda _n: atk, reps=reps)
    if souls is not None: rule['souls'] = lambda _n: souls
    if sparks is not None: rule['sparks'] = lambda _n: sparks
    s = {}
    for _ in range(games): G.game(n, rule, s)
    res = s['result']
    return (n, hname, atk, reps, souls, sparks, 100 * st.mean(r[0] for r in res), st.mean(s.get(('rounds', 3), [0])),
            100 * st.mean(s.get(('death', 3), [0])), s['turns'] / games, st.mean(r[1] for r in res), s['rounds_total'] / games)

if __name__ == '__main__':
    mode = sys.argv[1]
    with Pool(4) as pool:
        if mode == 'solo':
            jobs = [(1, r, '+1', 0, 1, so, None, 3000, 1) for r in (0.20, 0.24, 0.28, 0.32, 0.36, 0.42) for so in (6, 16)]
            for (n, h, a, rp, so, sp, win, l3, d3, t, rests, rounds), j in zip(pool.map(run, jobs), jobs):
                print(f'reach {j[1]:.2f} souls {so:2d}: win {win:3.0f}%  L3 {l3:4.1f} rounds, someone dies {d3:3.0f}%  rests {rests:3.1f}  table time {t:4.0f}')
        else:
            reach = float(sys.argv[2]); games = int(sys.argv[3]) if len(sys.argv) > 3 else 1500
            jobs = [(n, reach, h, a, rp, None, None, games, 7) for n in (2, 3, 4) for h in HEALTH for a in (0, 1, 2) for rp in (1, 2)]
            out = pool.map(run, jobs)
            print('chars health atk phases   win   L3 rounds  L3 death  table time  rests')
            for n, h, a, rp, so, sp, win, l3, d3, t, rests, rounds in out:
                print(f'  {n}   {h:>5s}  +{a}    {rp}     {win:4.0f}%    {l3:5.1f}     {d3:4.0f}%      {t:5.0f}     {rests:3.1f}')
