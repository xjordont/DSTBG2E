#!/usr/bin/env python3
"""Whole-game comparison of rulesets, one to four characters. Reproduces the tables of 41_rules_workshop.md, section 12.

For each ruleset and party size the simulated players first pick the resting policy that suits it (on one set of
seeds), then that policy is measured on another set. Figures are means over `--games` games; the win rate carries a
95% interval.

Usage:
  python3 tools/sim/compare.py                      # the named rulesets at the middle skill setting
  python3 tools/sim/compare.py --skill 0.25         # weaker play (0.75: stronger)
  python3 tools/sim/compare.py --only proposed --games 3000
"""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run import best

# the proposal: enemy health +2 for each character beyond the second; enemy attacks -1 against a lone character;
# boss health one third of the printed value with one character, two thirds with two, as printed with three or four;
# souls may be spent at the bonfire between encounters without resting
PROPOSED = dict(base='settled', free_visit=True, hp_add=[0, 0, 0, 2, 4], atk=[0, -1, 0, 0, 0], boss_mul=[0, 0.33, 0.67, 1, 1])
SPECS = {
    'official2017': ('Official 2017', {'base': 'official2017'}),
    'official2022': ('Official 2022 (same enemy cards; its own rewards and shop)', {'base': 'official2022'}),
    'manuscript': ("Author's manuscript, as written", {'base': 'manuscript'}),
    'settled': ('Settled rules of section 9.6 with the scaling of section 11', {'base': 'settled'}),
    'proposed': ('Proposed (section 12.5)', PROPOSED),
    'proposed_rest': ('Proposed, but souls can only be spent at a rest (the manuscript rule)', dict(PROPOSED, free_visit=False)),
}


def show(key, skill, games, probe):
    name, spec = SPECS[key]
    print('\n' + name)
    print('  chars  sparks  games won        rests  fights  table time   L3 rounds  L3 someone dies   lost at: encounter / mini-boss / main boss')
    for n in (1, 2, 3, 4):
        s, pol = best(spec, n, skill, games=games, probe=probe)
        lost = s['lost']; enc = sum(v for k, v in lost.items() if k in ('1', '2', '3'))
        print('    %d      %d     %3.0f%% (+/-%2.0f)     %4.1f   %5.1f    %6.0f       %4.1f         %3.0f%%            %3.0f%% / %3.0f%% / %3.0f%%' % (
            n, 6 - n, 100 * s['win'], 100 * s['ci'], s['rests'], s['fights'], s['time'], s.get(('rounds', 3), 0),
            100 * s.get(('death', 3), 0), 100 * enc, 100 * lost.get('mini', 0), 100 * lost.get('main', 0)))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--games', type=int, default=1500); ap.add_argument('--probe', type=int, default=300)
    ap.add_argument('--skill', type=float, default=0.5); ap.add_argument('--only', nargs='*')
    a = ap.parse_args()
    for key in (a.only or SPECS): show(key, a.skill, a.games, a.probe)
