#!/usr/bin/env python3
"""Whole-game comparison of rulesets, one to four characters. Reproduces the tables of 41_rules_workshop.md, section 13.

For each ruleset and party size the simulated players first pick the resting policy that suits it (on one set of
seeds), then that policy is measured on another set. Figures are means over `--games` games; the win rate carries a
95% interval.

Usage:
  python3 tools/sim/compare.py                      # the named rulesets at the calibrated skill setting (1.0)
  python3 tools/sim/compare.py --skill 0.8          # weaker play
  python3 tools/sim/compare.py --only A B --games 3000
"""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run import best

# Section 13. Common to both proposals: enemy health +2 for each character beyond the second; bosses as printed for a
# lone character; enemies and bosses hit harder as characters are added; a lone character starts with extra souls.
HEALTH = dict(base='settled', hp_add=[0, 0, 0, 2, 4])
A_DMG = [0, 0, 2, 3, 3]            # proposal A: +2 damage with two characters, +3 with three or four
B_DMG = [0, 0, 1, 1, 1]            # proposal B: +1 damage with two or more characters
PROPOSED_A = dict(HEALTH, atk=A_DMG, boss_atk=A_DMG, free_visit=True, solo_souls=6)       # Andre and the Firekeeper without a rest
PROPOSED_B = dict(HEALTH, atk=B_DMG, boss_atk=B_DMG, free_visit='shop', solo_souls=10)    # Andre only without a rest
PROPOSED = PROPOSED_A
SPECS = {
    'official2017': ('Official 2017 (the calibration anchor)', {'base': 'official2017'}),
    'official2022': ('Official 2022 rules on the 2017 enemy cards (not a valid test of the 2022 sets; see 13.2)', {'base': 'official2022'}),
    'manuscript': ("Author's manuscript, as written", {'base': 'manuscript'}),
    'health': ('Health rule only: bosses as printed, souls spent at a rest', dict(HEALTH, atk=[0] * 5)),
    'A': ('Proposal A (Andre and the Firekeeper without a rest)', PROPOSED_A),
    'B': ('Proposal B (Andre only without a rest)', PROPOSED_B),
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
    ap.add_argument('--skill', type=float, default=1.0); ap.add_argument('--only', nargs='*')
    a = ap.parse_args()
    for key in (a.only or SPECS): show(key, a.skill, a.games, a.probe)
