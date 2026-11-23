#!/usr/bin/env python3
"""Whole-game comparison of rulesets, one to four characters. Reproduces the tables of 41_rules_workshop.md, sections 13 and 14.

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
import rules as RU
from run import best

# Section 13. Common to both proposals: enemy health +2 for each character beyond the second; bosses as printed for a
# lone character; enemies and bosses hit harder as characters are added; a lone character starts with extra souls.
HEALTH = dict(base='settled', hp_add=[0, 0, 0, 2, 4])
A_DMG = [0, 0, 2, 3, 3]            # proposal A: +2 damage with two characters, +3 with three or four
B_DMG = [0, 0, 1, 1, 1]            # proposal B: +1 damage with two or more characters
PROPOSED_A = dict(HEALTH, atk=A_DMG, boss_atk=A_DMG, free_visit=True, solo_souls=6)       # Andre and the Firekeeper without a rest
PROPOSED_B = dict(HEALTH, atk=B_DMG, boss_atk=B_DMG, free_visit='shop', solo_souls=10)    # Andre only without a rest
PROPOSED = PROPOSED_A
# Section 14: the final ruleset, built up from the official 2017 rules one module at a time (rules.py lists the modules)
FINAL = dict(base='official2017', mods=['HOLLOW', 'ROUND_ALL', 'TURN_MS', 'ATTRITION', 'ECON_MS', 'NO_REFIGHT'],
             choose_of_two=True, hp_add=[0, 0, 0, 2, 4], atk=A_DMG, boss_atk=A_DMG, solo_souls=6)
# Section 15: the rules as the author's review has them. Encounters reset at every rest. A first clear pays 3 / 4 / 5 souls
# a character and two treasure cards to the party; every later clear pays 1 / 2 / 3 and no treasure. A cleared encounter
# may always be rushed past for one damage to each character. One encounter card a tile. Scaling: see section 15.6.
R_DMG = [0, 0, 2, 3, 4]            # the damage steps first proposed in 15.4, which the author rejected
LOOP = dict(FINAL, death='lost', heal_after=0, choose_of_two=False, soul_tab=[[3, 4, 5], [1, 2, 3]], skip_dmg=1,
            free_treasure=2, hp_add=[0] * 5, atk=[0] * 5, boss_atk=[0] * 5)            # the loop, with no scaling at all
# Section 15.7, on the author's shape: +1 health an enemy for each character beyond the first, small damage steps, short
# fights, and sparks of five less the number of characters.
SPARKS = [0, 4, 3, 2, 1]
AUTHOR = dict(LOOP, hp_add=[0, 0, 1, 2, 3], atk=[0, 0, 0, 1, 2], boss_atk=[0, 0, 0, 1, 2], sparks=SPARKS)   # the author's table as proposed
REVIEW = dict(LOOP, hp_add=[0, 0, 1, 2, 3], atk=[0, 0, 1, 2, 2], boss_atk=[0, 0, 1, 2, 2], boss_mul=[1, 1, 1.5, 2, 2.5], sparks=SPARKS,
              tier4=None, solo_souls=6)        # the standard game has three stat tiers; the fourth is for campaigns
# Section 17.2: souls are spent on stats only at a rest; the shop stays open between encounters. Sparks go back to six less
# the characters, bosses keep their printed health, and the fourth stat tier costs twelve souls in every kind of game.
REVIEW_GATE = dict(LOOP, hp_add=[0, 0, 1, 2, 3], atk=[0, 0, 1, 2, 2], boss_atk=[0, 0, 1, 2, 2], sparks=[0, 5, 4, 3, 2], solo_souls=6,
                   free_visit='shop', tier4=5, tier_cost=(2, 4, 8, 12))
# Every owned set in the treasure decks, whoever is playing (sections 18 and 19), under the three ways of sorting them.
# sets='2017' keeps to the 2017 sets; sets='all' adds the 2022 sets' cards. WORLD adds every class, boss and encounter.
WORLD = dict(roster='all', bosses='all', encounters='all')
ALL_REQ = dict(REVIEW_GATE, sets='all', deck_split='req')          # by requirement: 25 or more is tier two, with the transposed cards
ALL_KIND = dict(REVIEW_GATE, sets='all', deck_split='type_all')    # by kind: common and class tier one, transposed tier two
ALL_MID = dict(REVIEW_GATE, sets='all', deck_split='mid')          # common cards split at 25, class cards tier one, transposed tier two
# Section 19: everything owned (every set's cards, class, boss and encounter), sorted by requirement; and the same with the
# tuning proposed for three and four characters (one spark fewer each, boss health x1.25 and x1.5)
OWNED = dict(ALL_REQ, **WORLD)
# Section 20: the author's choice of treasure split (between), on every 2017 set; WORLD_22 adds the 2022 sets' enemies,
# encounters and bosses as printed for the 2022 rules, which the workshop keeps apart
WORLD_22 = dict(roster='all', bosses='all22', encounters='all22')
OWNED_20 = dict(ALL_MID, **WORLD)
OWNED_20_22 = dict(ALL_MID, **WORLD_22)
TUNING_20 = dict(sparks=[0, 4, 3, 2, 1], boss_add=[0, 0, 4, 8, 12])      # five less the characters; a boss gains 4 health a character beyond the first
PROPOSED_20 = dict(OWNED_20, **TUNING_20)
PROPOSED_20_CORE = dict(REVIEW_GATE, **TUNING_20)
PROPOSED_20_22 = dict(OWNED_20_22, **TUNING_20)
PROPOSED_19 = dict(OWNED, sparks=[0, 5, 4, 2, 1], boss_mul=[1, 1, 1, 1.25, 1.5])
# Section 19.8, with the manuscript's card amendments played: sparks five less the number of characters, the same boss health
TUNING_198 = dict(sparks=[0, 4, 3, 2, 1], boss_mul=[1, 1, 1, 1.25, 1.5])
PROPOSED_198 = dict(OWNED, **TUNING_198)
PROPOSED_198_CORE = dict(REVIEW_GATE, **TUNING_198)
REVIEW_TWICE = dict(LOOP, hp_add=[0, 0, 1, 2, 3], atk=[0, 0, 1, 1, 1], boss_atk=[0, 0, 1, 1, 1], reps=[1, 1, 1, 2, 2], sparks=SPARKS)
REVIEW_HEALTH = dict(LOOP, hp_add=[0, 0, 3, 6, 9], boss_mul=[1, 1, 2, 3, 4])            # 15.6: health only (set aside: it lengthens the game)
REVIEW_D1 = dict(LOOP, atk=[0, 0, 1, 1, 1], boss_atk=[0, 0, 1, 1, 1], hp_add=[0, 0, 1, 4, 6], boss_mul=[1, 1, 1.5, 2, 2.5])   # 15.6: the shorter alternative
SPECS = {
    'official2017': ('Official 2017 (the calibration anchor)', {'base': 'official2017'}),
    'official2022': ('Official 2022 rules on the 2017 enemy cards (not a valid test of the 2022 sets; see 13.2)', {'base': 'official2022'}),
    'manuscript': ("Author's manuscript, as written", {'base': 'manuscript'}),
    'health': ('Health rule only: bosses as printed, souls spent at a rest', dict(HEALTH, atk=[0] * 5)),
    'final': ('The final ruleset (section 14)', FINAL),
    'review': ("The author's review so far (section 15); add --regrind 2 for players who fight reset encounters again", REVIEW),
    'review_gate': ('17.2: stats are raised only at a rest; the shop is open between encounters (use --bank 6 or 10)', REVIEW_GATE),
    'all_req': ('Section 18: every 2017 set in the decks, sorted by requirement (25 or more is tier two)', ALL_REQ),
    'all_kind': ('Section 18: every 2017 set, sorted by kind (common and class / transposed)', ALL_KIND),
    'all_mid': ('Section 18: every 2017 set, common cards split at 25, class cards tier one', ALL_MID),
    'owned': ('Section 19: the accepted rules with everything owned (every set, class, boss and encounter)', OWNED),
    'proposed19': ('Section 19: the same with sparks 5/4/2/1 and boss health x1.25 / x1.5 for three and four characters', PROPOSED_19),
    'proposed198': ('Section 19.8: everything owned, sparks 4/3/2/1 and boss health x1.25 / x1.5 for three and four characters', PROPOSED_198),
    'proposed198_core': ('Section 19.8: the same tuning on the core set alone', PROPOSED_198_CORE),
    'owned20': ('Section 20: accepted rules, every 2017 set, all treasure, the between split', OWNED_20),
    'proposed20': ('Section 20: the same with sparks 4/3/2/1 and boss health +4 a character beyond the first', PROPOSED_20),
    'settled21': ('Section 21: the rules as settled then (the between split, sparks 4/3/2/1, boss health +4 a character beyond the first; the party chooses its order), every 2017 set', PROPOSED_20),
    'settled23': ('Section 23: section 21 with characters acting in ascending threat; a boss before each character', dict(PROPOSED_20, order='asc')),
    'settled24': ('Section 24, withdrawn (one round for every encounter: enemies in ascending threat, the boss once, characters in ascending threat; boss damage +2/+3/+4), every 2017 set',
                dict(PROPOSED_20, order='asc', enemy_order='asc', boss_round='once', boss_atk=[0, 0, 2, 3, 4])),
    'settled25': ('Section 25 (enemies in descending threat, then the characters in any order; a boss before each character; bosses, invaders and summons not scaled), every 2017 set',
                dict(PROPOSED_20, boss_add=[0] * 5, boss_atk=[0] * 5)),
    'settled26': ('Section 26, withdrawn (section 25, with a black die for a one-handed weapon gripped in both hands and two more stamina for a two-handed weapon swung in one), every 2017 set',
                dict(PROPOSED_20, boss_add=[0] * 5, boss_atk=[0] * 5, grip_die='only', one_hand='sta2')),
    'settled27': ('Section 27, superseded (section 25, with enemy health +2 for each character beyond the first; one reroll for a two-handed weapon and for a one-handed weapon with the other weapon slot empty), every 2017 set',
                dict(PROPOSED_20, boss_add=[0] * 5, boss_atk=[0] * 5, hp_add=[0, 0, 2, 4, 6])),
    'settled29': ('Section 29, superseded (section 25, with enemy health +2 / +3 / +4 and enemy damage +1 / +2 / +3 for two, three and four characters; bosses not scaled), every 2017 set',
                dict(PROPOSED_20, boss_add=[0] * 5, boss_atk=[0] * 5, hp_add=[0, 0, 2, 3, 4], atk=[0, 0, 1, 2, 3])),
    'settled34': ('Section 34, superseded (section 25, with enemy health +2 / +3 / +4, enemy damage +1 / +2 / +2 and every enemy movement one node further with four characters; bosses not scaled), every 2017 set',
                dict(PROPOSED_20, boss_add=[0] * 5, boss_atk=[0] * 5, hp_add=[0, 0, 2, 3, 4], atk=[0, 0, 1, 2, 2], move_up=[0, 0, 0, 0, 1])),
    'settled': ('Section 35: the rules as settled (section 25, with enemy health +2 for each character beyond the first and enemy damage +1 for any party of two or more; bosses not scaled), every 2017 set',
                dict(PROPOSED_20, boss_add=[0] * 5, boss_atk=[0] * 5, hp_add=[0, 0, 2, 4, 6], atk=[0, 0, 1, 1, 1])),
    'ladder': ('Section 23, not adopted: enemies and characters on one ladder of ascending threat', dict(PROPOSED_20, round='ladder', order='threat')),
    'proposed20_core': ('Section 20: that tuning on the core set alone', PROPOSED_20_CORE),
    'proposed20_22': ('Section 20: that tuning with the 2022 sets\' enemies, encounters and bosses in, as printed', PROPOSED_20_22),
    'author': ("The author's own table (15.7): health +1 a character, damage +0/+0/+1/+2, sparks 4/3/2/1", AUTHOR),
    'review_twice': ('15.7, the other candidate: +1 damage, enemies attack twice against three or more', REVIEW_TWICE),
    'review_health': ('15.6, set aside: health only, +3 an enemy for each extra character', REVIEW_HEALTH),
    'review_d1': ('15.6, set aside: +1 damage, enemy health +1/+4/+6', REVIEW_D1),
    'review_kind': ('The review rules with treasure sorted by kind of card (15.5)', dict(REVIEW, deck_split='kind')),
    'A': ('Proposal A of section 13 (Andre and the Firekeeper without a rest)', PROPOSED_A),
    'B': ('Proposal B (Andre only without a rest)', PROPOSED_B),
}


def show(key, skill, games, probe, regrind=0, bank=None):
    name, spec = SPECS[key]
    print('\n' + name)
    print('  chars  sparks  games won        rests  fights  table time   L3 rounds  L3 someone dies   lost at: encounter / mini-boss / main boss')
    for n in (1, 2, 3, 4):
        s, pol = best(spec, n, skill, games=games, probe=probe, extra=dict(regrind=regrind, bank=bank))
        lost = s['lost']; enc = sum(v for k, v in lost.items() if k in ('1', '2', '3'))
        print('    %d      %d     %3.0f%% (+/-%2.0f)     %4.1f   %5.1f    %6.0f       %4.1f         %3.0f%%            %3.0f%% / %3.0f%% / %3.0f%%' % (
            n, RU.make(spec).sparks(n), 100 * s['win'], 100 * s['ci'], s['rests'], s['fights'], s['time'], s.get(('rounds', 3), 0),
            100 * s.get(('death', 3), 0), 100 * enc, 100 * lost.get('mini', 0), 100 * lost.get('main', 0)))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--games', type=int, default=1500); ap.add_argument('--probe', type=int, default=300)
    ap.add_argument('--skill', type=float, default=1.0); ap.add_argument('--only', nargs='*')
    ap.add_argument('--regrind', type=int, default=0, help='highest level of reset encounter the players fight again (0: always rush)')
    ap.add_argument('--bank', type=int, default=None, help='unspent souls a character at which the party rests to spend them')
    a = ap.parse_args()
    for key in (a.only or SPECS): show(key, a.skill, a.games, a.probe, a.regrind, a.bank)
