# Audit B — Numerical Balance

Project: Dark Souls: The Board Game — Second Edition (homebrew) editorial pipeline.
Manuscript audited: `/home/user/DSTBG2E/work/docx/manuscript.md` (body from line 361; all "L" references below are line numbers in that file).
Companion data file: `/home/user/DSTBG2E/work/audit/B_rows.csv` (IDs B-001 …).
Conventions: British English. "Official" = Steamforged texts in `/home/user/DSTBG2E/work/text/`, cited as *file p.N* (PDF page). Anything not found in a supplied source is labelled **ASSUMPTION**.

## 0. Sources and assumptions used for the base numbers

| Datum | Value used | Source |
|---|---|---|
| Spark table | 1p 5, 2p 4, 3p 3, 4p 2 | DS-Core-Rules-lores p.8 (table) |
| 1E level-up costs | Base→T1 2, T1→T2 4, T2→T3 8 | Core p.15; V2 (DS-TG-Rulebook) p.26 identical |
| 1E campaign level-up costs | 4 / 8 / 16; Tier 4 = 20 souls, "value of any stat at Tier 4 is considered to be 40" | Core p.33 |
| 1E soul income | non-boss encounter: 2 souls per character to a shared cache; boss: 1 soul per character per spark remaining | Core p.19 |
| 1E solo bonus | soul cache starts with 16 souls in a one-player game | Core p.13 |
| 1E shop | random draw, 1 soul per card; campaign 2 souls, sell-back 1 | Core p.14, p.33 |
| 1E endurance bar | **ten** boxes ("If all ten of a character's endurance bar boxes have cubes, that character has been killed") | Core p.20 text and Herald board image p.11 |
| 1E stamina recovery | +2 stamina at start of activation | Core p.22 (V2 p.20: +3) |
| 1E block/resist | roll all block dice and **add them together** | Core p.25 |
| 1E dodge | 1 stamina, move 1 node, roll dodge dice; successes ≥ difficulty | Core p.25; FAQ (0 dodge dice may still dodge, auto-hit if difficulty ≥ 1) |
| 1E conditions | Bleed: +2 damage when next damaged, then remove; Poison: 1 damage end of activation; Stagger: character +1 stamina to attack, enemy −1 damage; Frostbite: character +1 stamina to move/dodge, enemy −1 move | Core p.21; V2 p.21 (Poison also discards token) |
| Calamity (official) | −1 success on block/resist/dodge rolls; removed when the character suffers damage from the attack | DS-BDK-Rules-web p.? (text lines 452–458) |
| Hollow Soldier data card (1E) | Threat 5, range 0, dodge difficulty 2, block 1, resist 1, health 1; behaviour: move 1 towards nearest, then attack 4 (physical) vs nearest | Core p.20 (card image, read from the rendered page) |
| Skeleton Soldier data card (V2) | Threat 5, range 1, dodge 1, block 2, resist 1, health 1; behaviour: push-move 1 towards nearest with a 2-damage push attack | V2 p.24 (card image) |
| Printed enemy attack values in the icon key | 5 physical (node, push), 4 physical (node), 3 magical | Core p.25; V2 p.25 |
| Silver Knight Swordsman kill threshold | block + health = 4 (inferred: Extended Rules p.27 says cards II+V on three blue dice, or orange VI = 4, "guarantee" a kill); Hollow Soldier threshold 2 (orange II = 2 kills it) | DS-Extended-Rules-V45 p.27 |
| Example boss data (unnamed) | Threat 6, deck size 4, block 2, resist 1, health 24, heat-up 12 | Core p.40 / V2 p.32 icon key |
| Hungry Mimic | Threat 10, health 18, deck 4, block 1, resist 1, heat-up 8; Voracious Mimic health 22 | DS-Explorers-Rules-Web p.? (text lines 105–130, 408–420) |
| Fencer Sharron (advanced invader) | Threat 10, health 20, deck 5, block 1, resist 1, heat-up 12 (digits read from the text dump; order partly inferred) | DS-Phantoms-Rules-lores p.12 |
| Invader reward (1E) | 3 souls to the cache | Phantoms p.15 |
| Kalameet (mega) | Threat 10, health 38, heat-up 22, deck 6 | DS-BDK-Rules-web p.? (text lines 325–345) |
| Mega-boss stage bonus (1E) | +8 souls per character before the mega-boss | BDK text 252–253; EC text 287–288 |
| Herald dashboard tiers (1E) | STR 12/19/28/37, DEX 11/17/26/34, INT 8/12/20/29, FTH 13/22/31/40 | Core p.11 (image) |
| Cleric dashboard tiers (V2) | STR 12/18/27/37, DEX 8/15/24/33, INT 7/14/22/30, FTH 16/23/32/40 | V2 p.26 (image) |
| Core components | 5 black, 4 blue, 2 orange, 4 green dice; 5× each of Bleed/Poison/Frostbite/Stagger tokens; souls 10×1, 5×3, 3×5, 1×8; wounds 6×1, 3×3, 1×5; 16 level-up cubes; 32 red, 32 black cubes | Core p.7 |
| Hollowed Edition (community) | level 2/4/6/8; Bleed 3 damage at 2 stacks; block = best two dice; solo 6 souls; sparks cap 5 | Hollowed_Edition_v1.3 pp.1,3,5,7,8 |
| Extended Rules (community) | "double souls except L4/boss"; summon 2 souls per player; two treasure decks split at 25; Deck 1 stocked "3 weapons, 2 armours, 1 shield, 2 items" per player | DS-Extended-Rules-V45 pp.2–3 |

**Not in any supplied source (ASSUMPTIONS, flagged where used):**
- Full dice face distributions (see §1 — three of six faces per die are evidenced).
- Starting equipment of the Knight/Warrior. Block pool assumed **2 black dice** (brief's default); sensitivity shown for 3 black.
- Data cards for Silver Knight Swordsman, Sentinel, Crossbow Hollow, Large Hollow Soldier (not printed as text in any supplied file). A labelled "heavy" archetype (attack 5, health 3, block 2) is used as a stress case.
- Encounter levels on mini-boss/main-boss data cards (Core p.9 says they are printed on the card; cards are not reproduced). The four-tile basic game is modelled as L1/L1/L2/L2 before the mini-boss and L2/L2/L3/L3 before the main boss, extrapolated from the Core p.35 campaign lists (Gargoyle section L1/L1/L2; Ornstein & Smough section L2/L2/L3/L3/L3).
- Original (pre-revision) weapon stat requirements for the 60-row table. The Extended Rules PDF does **not** contain stat tables (checked page by page); only four cards appear as images in the Core rulebook (Battle Axe STR 14; Fume Ultra Greatsword STR 37; Faraam Armour STR 20/INT 19 — partly legible).
- Composition of the common treasure deck by card type (weapons/armour/shields/upgrades/spells). Estimated in §9.

---

## 1. Dice

### 1.1 Face evidence
No supplied text prints the die faces. Evidence assembled:
- *DS-Extended-Rules-V45 p.27* reproduces combat cards II, V and VI, each showing one face of every die colour: **II** = black 1 / blue 1 / orange 2 / green blank; **V** = black 2 / blue 2 / orange 3 / green success; **VI** = black 2 / blue 3 / orange 4 / green success. The cards are numbered I–VI in ascending value, so these are the 2nd, 5th and 6th faces of each die in sorted order.
- *Core p.12* (Estoc example): three black dice can roll "a 2, a 1, and a blank" → the black die has faces 0, 1 and 2.
- *V2 p.25* (Thief example): two black dice show 2 and 1; two green dice show blank faces.

The only sorted six-face sets consistent with all of the above and with a 0/1/2 black die are the community-documented distributions below. The unseen faces (I, III, IV) are an **ASSUMPTION**; every later calculation states which die it uses so it can be re-run if the author's dice differ.

| Die | Faces (ASSUMED full set; bold = evidenced) | Mean | P(≥1) | P(≥2) | P(≥3) | P(≥4) |
|---|---|---|---|---|---|---|
| Black | 0, **1**, 1, 1, **2**, **2** | 1.17 | 0.833 | 0.333 | 0 | 0 |
| Blue | 1, **1**, 2, 2, **2**, **3** | 1.83 | 1.000 | 0.667 | 0.167 | 0 |
| Orange | 1, **2**, 2, 3, **3**, **4** | 2.50 | 1.000 | 0.833 | 0.500 | 0.167 |
| Green (dodge) | 0, **0**, 0, 1, **1**, **1** | 0.50 success | 0.500 | 0 | 0 | 0 |

Arithmetic: black mean = (0+1+1+1+2+2)/6 = 7/6 = 1.17; blue = 11/6 = 1.83; orange = 15/6 = 2.50. The three attack dice step up by exactly 0.67 each, which supports the reconstruction.
Note on the green die: the sorted faces II = blank, V and VI = single success rule out a two-success face (card VI would show it); 0,0,0,1,1,1 is the only symmetric candidate. If the real die is 0,0,1,1,1,1 every dodge probability in §10 rises (p = 2/3 instead of 1/2).

### 1.2 Two dice
| Two dice | Mean | P(≥2) | P(≥3) | P(≥4) | P(≥5) | P(≥6) |
|---|---|---|---|---|---|---|
| 2 × Black | 2.33 | 0.806 | 0.444 | 0.111 | 0 | 0 |
| 2 × Blue | 3.67 | 1.000 | 0.889 | 0.556 | 0.194 | 0.028 |
| 2 × Orange | 5.00 | 1.000 | 0.972 | 0.861 | 0.639 | 0.361 |
| 2 × Green | 1.00 | P(≥1 success) = 0.750; P(2) = 0.250 | | | | |

Distribution of 2 black dice (the assumed starting block pool): 0: 0.028, 1: 0.167, 2: 0.361, 3: 0.333, 4: 0.111.

### 1.3 The manuscript's "two highest dice" block rule (L1722)
Manuscript: defence total = sum of the **two highest** block dice. Official 1E (Core p.25) sums **all** dice; the manuscript follows Hollowed Edition p.7.
- 3 black dice, best two: 0: 0.005, 1: 0.042, 2: 0.278, 3: 0.417, 4: 0.259 → mean **2.88** (official sum-of-three mean 3.50).
- 4 black dice, best two: mean **3.19**, ceiling 4.
- 2 black + 1 blue, best two: mean **3.40**, P(≥4) = 0.477.
Consequence: a block total can never exceed 4 with black dice (6 with blue, 8 with orange). Any enemy attack value of 5+ therefore always does damage to a black-dice blocker. This cap is the key constraint for §2.

