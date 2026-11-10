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

## 2. Enemy Scaling table (L1519–1560)

Manuscript rule: health +1 per character beyond one; move 1 → 2 at 2+ characters; attack +1 at 3+; **Repeat 2** on the attack behaviour at 4; bosses unscaled. Campaign Bonfire Ascetic (L2342): +1 attack to all non-boss enemies, "cumulative with stat scaling for character count".

Official comparison: **1E has no player-count scaling at all** — Core p.20 "An enemy's starting Health is how much damage the enemy can suffer"; nothing in Core pp.17–25 varies by player count. Difficulty in 1E is instead carried by the activation structure (all enemies act between every single character turn, Core p.19) and by sparks (p.8). **V2** scales by *enemy count*: encounter cards carry a "number of players" symbol (V2 p.16). Neither official edition adds attack value or Repeat. Hollowed Edition has no scaling rule. The manuscript's table is therefore new design and is the most aggressive scaling of the four rule-sets.

### 2.1 Scaled stats for real cards (and one labelled archetype)
| Enemy | Characters | Health | Move | Attack | Repeats | Attack after Ascetic (campaign) |
|---|---|---|---|---|---|---|
| Hollow Soldier (Core p.20: H1, move 1, attack 4) | 1 | 1 | 1 | 4 | 1 | 5 |
| | 2 | 2 | 2 | 4 | 1 | 5 |
| | 3 | 3 | 2 | 5 | 1 | 6 |
| | 4 | 4 | 2 | 5 | **2** | 6 |
| Skeleton Soldier (V2 p.24: H1, push-move 1 with 2-damage push attack) | 1 | 1 | 1 | 2 | 1 | 3 |
| | 2 | 2 | 2 | 2 | 1 | 3 |
| | 3 | 3 | 2 | 3 | 1 | 4 |
| | 4 | 4 | 2 | 3 | 2 | 4 |
| Icon-key node attack (Core p.25: 5 physical, push) | 3 | – | – | 6 | 1 | 7 |
| | 4 | – | – | 6 | 2 | 7 |
| Heavy archetype (ASSUMPTION: H3, attack 5, block 2) | 1 | 3 | 1 | 5 | 1 | 6 |
| | 4 | 6 | 2 | 6 | 2 | 7 |

Note on the Skeleton Soldier: its only attack is a push-attack inside a move. The text (L1529) says Repeat is added to "each non-boss enemy's attack behaviour"; whether a move-with-push counts is undefined (B-005). Note also that the move 1 → 2 rule doubles the number of push-attack hits this enemy can deliver, so for push-movers the 2-player row is already an attack doubling.

### 2.2 Expected damage per activation (physical attack vs block pools; ASSUMED pools)
E[damage] = Σ P(block = b) × max(0, A − b). Pools are "best two dice" per L1722.

| Attack value A | Repeats | E[dmg] 2 black | E[dmg] 3 black (best 2) | E[dmg] 2 black + 1 blue (best 2) | P(0 dmg), 2 black | P(dmg ≥ 3), 2 black |
|---|---|---|---|---|---|---|
| 2 | 1 | 0.22 | 0.05 | 0.01 | 0.806 | 0 |
| 3 | 1 | 0.78 | 0.38 | 0.17 | 0.444 | 0.028 |
| 4 (Hollow Soldier, 1–2p) | 1 | **1.67** | 1.12 | 0.69 | 0.111 | 0.194 |
| 5 (Hollow Soldier, 3p) | 1 | **2.67** | 2.12 | 1.60 | 0 | 0.556 |
| 5 ×2 (Hollow Soldier, 4p) | 2 | **5.33** | 4.23 | 3.20 | 0 | 0.556 per hit |
| 6 ×2 (4p + Ascetic) | 2 | **7.33** | 6.23 | 5.20 | 0 | 0.889 per hit |
| 7 ×2 (icon-key 5-attack enemy, 4p + Ascetic) | 2 | 9.33 | 8.23 | 7.20 | 0 | 1.000 per hit |

Worked line (A = 5, 2 black): 0.028×5 + 0.167×4 + 0.361×3 + 0.333×2 + 0.111×1 = 0.14+0.67+1.08+0.67+0.11 = **2.67**. Repeat 2 doubles it to 5.33.

### 2.3 Survivability against one scaled Hollow Soldier activation (2 black block dice)
P(death) = P(total damage ≥ K free boxes).

| Bar state (K free boxes) | A4 ×1 (1–2p) | A5 ×1 (3p) | A5 ×2 (4p) | A6 ×2 (4p + Ascetic) |
|---|---|---|---|---|
| 8 free — full bar, 8-box manuscript bar | 0 | 0 | 0.058 | **0.444** |
| 6 free — hollow, nothing spent | 0 | 0 | **0.444** | **0.914** |
| 4 free — two skips, or hollow after 2 stamina | 0.028 | 0.194 | 0.914 | 1.000 |
| 2 free — three skipped encounters (L1263) | 0.556 | 0.889 | 1.000 | 1.000 |
| 10 free — official 1E ten-box board (Core p.20) | 0 | 0 | 0.001 | 0.058 |

Expected activations to empty a full 8-box bar: A4 → 4.8; A5 → 3.0; A5×2 → 1.5; A6×2 → **1.1**. A hollow (6-box) character facing the 4-player campaign Hollow Soldier dies in 0.8 expected activations — i.e. usually on the first hit pair.

### 2.4 Assessment
- 1–2 players: the table is benign (health +1, move 2). A lone Hollow Soldier is a 1.67-damage threat; a full encounter of three (Core p.18 example has two Hollow Soldiers + a Greatbowman) costs about 3–5 damage per enemy phase before the party acts. **OK.**
- 3 players: +1 attack is a 60 % increase in expected damage for a 4-attack enemy (1.67 → 2.67) and removes any chance of a zero-damage block (P(0) falls from 0.111 to 0). Because the enemy count on the card does not change, three characters absorb 3× the activations of one character but each enemy hits 60 % harder. **Tune** — this step is steeper than the health step.
- 4 players: Repeat 2 **doubles** expected damage on top of the +1 (1.67 → 5.33 per activation, +220 %). With the two-highest-dice cap the best black-dice blocker (4 dice, mean 3.19) still takes 1.8 × 2 = 3.6 per activation. One Hollow Soldier activation has a 5.8 % chance of killing a full-health starting character outright and a 44 % chance of killing a hollow one. **Broken** at 4 players.
- Campaign, 4 players after Ascetic: attack 6, Repeat 2 → 7.33 expected, 44 % kill chance on a full bar, 91 % on a hollow bar. **Broken**; see §14.
- Compared with 1E: the 1E endurance bar has **ten** boxes (Core p.20; Herald board image p.11 shows ten) and 1E enemies never scale, so a 1E Hollow Soldier threatens 1.67 of 10 boxes (17 %); the 4-player 2E Hollow Soldier threatens 5.33 of 8 (67 %).

Recommended numbers (B-003, B-004): drop Repeat from the 4-player row; use attack +1 at **four** characters only (3-player row "–"); or, if Repeat is kept, apply it only to enemies whose printed attack value is 3 or less. Alternative that preserves the author's intent: 4 players → "+1 attack and +1 health" instead of Repeat. Resulting 4-player Hollow Soldier: attack 5, health 5, E[dmg] 2.67 (vs 5.33).

## 3. Stat Tier Costs (basic L1918–1923; campaign L2301–2306)

| Table | Per-tier cost | Cumulative for one stat (T1/T2/T3/T4) | Cumulative for all four stats |
|---|---|---|---|
| Basic as written | 2 / 4 / 8 / **8** | 2 / 6 / 14 / 22 | 8 / 24 / 56 / 88 |
| Basic, proposal A (campaign ratio 1:2:4:5) | 2 / 4 / 8 / **10** | 2 / 6 / 14 / 24 | 8 / 24 / 56 / 96 |
| Basic, proposal B (doubling) | 2 / 4 / 8 / **16** | 2 / 6 / 14 / 30 | 8 / 24 / 56 / 120 |
| Campaign as written | 4 / 8 / 16 / 20 | 4 / 12 / 28 / 48 | 16 / 48 / 112 / 192 |
| Official 1E (Core p.15) + campaign Tier 4 (Core p.33) | 2 / 4 / 8 / 20 | 2 / 6 / 14 / 34 | 8 / 24 / 56 / 136 |
| Hollowed Edition p.3 | 2 / 4 / 6 / 8 | 2 / 6 / 12 / 20 | 8 / 24 / 48 / 80 |

Worked example (Core p.15 reproduces the same arithmetic for 1E): a character raising STR and DEX to Tier 1 and FTH to Tier 3 pays 2 + 2 + (2 + 4 + 8) = 18 souls. Under the campaign table the same purchases cost 4 + 4 + 28 = 36.

**Tier Four = 8 is almost certainly a typo.** Every other progression in the manuscript and its sources is strictly increasing (campaign 4/8/16/20 is exactly 2× the basic row, which would make basic Tier Four = 10). The author's own campaign curve has ratios 1 : 2 : 4 : 5, so the consistent basic value is **10** (proposal A). Proposal B (16) matches the doubling of the first three steps but, at a cumulative 30 for one stat, Tier Four would consume 68 % of a character's whole-game income (§4) and would never be bought. Recommendation: **10** (B-007).

Tier Four value: the manuscript (L1914) sets Tier Four = Tier Three + 5; official 1E campaign (Core p.33) and Hollowed Edition p.3 both set Tier Four = **40 for every stat**. See §7 for why this matters.

## 4. Souls economy

### 4.1 Rules as written
Basic Soul Reward Table (L1401–1434): L1 & standard invaders 3; L2 & advanced invaders 4; L3 5; L4 & bosses 6, per character, individual (L1383 "cannot be transferred"). Campaign table (L2247–2280): 2 / 3 / 4 / 5. "Reduced soul reward" for re-cleared encounters (L1391) is **never defined** anywhere in the manuscript (B-008). Solo start 6 souls (L1003; Hollowed p.2 — official 1E gives 16 to the cache, Core p.13). Invaders: "additional souls per player" (L1393) — the amount is only given through the reward table's row labels (3 standard / 4 advanced); official 1E gives 3 to the cache (Phantoms p.15).

Prices: tier one card 2, tier two 4, sell 1, boss treasure sells 6 (L1955–1957); phantom draw 2 (L1973); campaign: boss treasure sells 4, legendary = 4 souls + a boss treasure, Bonfire Ascetic 16 shared (L2330–2334).

### 4.2 Model of a standard basic game (per character)
Encounter levels are **ASSUMED** (not printed in any supplied text; extrapolated from Core p.35): mini-boss route L1, L1, L2, L2; main-boss route L2, L2, L3, L3.

| Phase | Encounters | Souls | Boss | Phase total | Running total |
|---|---|---|---|---|---|
| Route to mini-boss | L1 + L1 + L2 + L2 | 3 + 3 + 4 + 4 = 14 | 6 | 20 | 20 |
| Route to main-boss | L2 + L2 + L3 + L3 | 4 + 4 + 5 + 5 = 18 | 6 | 24 | **44** |

(a) **No repeats, no losses: 44 souls per character for the whole basic game.**

(b) **Typical repeats** — one rest per half forces one full re-clear of the four tiles at the undefined reduced reward. Candidate definitions and what they add:

| Reduced reward rule | L1 / L2 / L3 / L4 | Re-clear of half 1 | Re-clear of half 2 | Game total |
|---|---|---|---|---|
| Half, rounded down | 1 / 2 / 2 / 3 | 6 | 8 | 58 |
| Half, rounded up | 2 / 2 / 3 / 3 | 8 | 10 | 62 |
| Reward − 2 | 1 / 2 / 3 / 4 | 6 | 10 | 60 |
| Flat 1 | 1 / 1 / 1 / 1 | 4 | 4 | 52 |

Recommendation: **half, rounded down** (1/2/2/3 basic; campaign 2/3/4/5 → 1/1/2/2). It is the strongest anti-grind option that still pays something, it needs no second table (one sentence), and it keeps a full re-clear (6–8 souls) worth less than one Tier Three step (8). "Reward − 2" produces 0 at campaign Level 1 and is rejected.

(c) **Typical deaths.** A death only costs souls if the dropper dies again before reclaiming (L1393–1397). Model: two deaths with recovery (0 loss) and one unrecovered loss of the ~8 souls carried → **44 − 8 = 36** (no repeats) or 58 − 8 = 50 (with repeats).

### 4.3 What that buys
| Purchase | Cost | Share of 44 |
|---|---|---|
| One stat to Tier Three | 14 | 32 % |
| One stat to Tier Four (as written 8 / proposed 10) | 22 / 24 | 50 % / 55 % |
| All four stats to Tier Two | 24 | 55 % |
| All four stats to Tier Three | 56 | 127 % — unreachable without ≥ 2 full re-clears |
| Tier two shop card | 4 | 9 % |
| Phantom draw | 2 | 5 % |

By the mini-boss a character holds 20 souls (if nothing was spent at an interim rest): enough for one stat to Tier Three (14) **and** one tier-two card (4) when the tier-two shop opens after the mini-boss (L1083). So the tier-two shop at 4 souls is **reachable before the main boss** for every character, with ~2 souls to spare. Over the whole game a character can reach Tier Three in one stat plus Tier Two in a second (14 + 6 = 20) and buy three or four cards; that is meaningful but shallow — a Tier Four stat costs half of all income. Verdict: **OK for a one-session game; tune Tier Four to 10 and define the reduced reward.**

Comparison with 1E (shared cache, Core p.19/13/14): 8 encounters × 2 souls × N characters + boss souls (1 per character per spark remaining) ≈ 43 (1p incl. the 16-soul solo bonus), 50 (2p), 69 (3p), 84 (4p) in the cache, i.e. 21–25 per character at 2–4 players, with cards at 1 soul and levels 2/4/8. The manuscript roughly doubles per-character income and doubles card prices, so purchasing power is similar to 1E while levelling is about twice as affordable. Extended Rules p.2 ("double the typical number of souls, except L4 and bosses") lands in the same place.

Campaign (First Journey, Core p.35 structure, campaign table): section 1 (L1, L1, L2 + two Gargoyles at 5 each) = 17; section 2 (L1, L1, L2, L2 + 5) = 15; section 3 (L2, L2, L3, L3, L3 + 5) = 23; **55 per character** across three sessions, against 48 for one Tier Four stat, 112 for four stats to Tier Three and 16 (shared) for the Ascetic. With 3 characters the Ascetic costs 5.3 each (10 % of income) — affordable in section 1 if the party chooses. Campaign stat progression is deliberately slow (one stat to Tier Three = 28 = half of all income); that matches the stated intent (L2297) but means most characters end a three-section campaign at Tier Two–Three in one stat. **Tune:** either lower campaign Tier Three to 12 or raise campaign soul rewards back to the basic table and keep the slower levelling through prices.

Solo: 6 starting souls (L1003) buys three tier-one cards or Tier One in three stats; official 1E gave a solo party 16 (Core p.13) because the single character carries every activation. With the manuscript's unscaled 1-player enemies the lower figure is defensible; flagged as a Note (B-010).

## 5. Spark economy

Rules: sparks = 6 − N (L1093, L1247); +1 per mini-/main-boss (L1249; also L1167, L1185); rest costs 1 (L1253); a failed encounter forces a rest (L1341, L1371); post-boss rest free (L1908); loss when all characters are dead with no sparks (L1197). Campaign: maximum = starting value (L2233); no free post-boss rest except the section's final boss (L2235); adding a player costs 1 spark and resets the maximum (L2239).

### 5.1 Basic game
| Characters | Start (6 − N) | After mini-boss | After main-boss (only matters if a mega-boss follows) | Paid rests available before the main-boss kill | Free rests | Forced rests the party can absorb |
|---|---|---|---|---|---|---|
| 1 | 5 | 6 | 7 | 6 | 2 | 6 — the seventh wipe loses |
| 2 | 4 | 5 | 6 | 5 | 2 | 5 |
| 3 | 3 | 4 | 5 | 4 | 2 | 4 |
| 4 | 2 | 3 | 4 | 3 | 2 | 3 |

Reading: a 4-player party has **three** paid bonfire visits in the whole basic game (two before the mini-boss, one more after it) plus the two free post-boss rests. Every failed encounter (a wipe **or any single death of a hollow character**, L1223) consumes one of them. Because §2 shows a hollow character at 4 players has a 44 % chance of dying to a single Hollow Soldier activation, and the party cannot remove hollow status without spending a spark (L1219), the 4-player game is a tight spiral: first death → hollow → high chance of a second death → forced rest (−1 spark). Expected sparks lost per boss route at 4 players is plausibly 1–2, leaving no voluntary rests for shopping. The table itself matches official 1E (Core p.8) exactly; the problem is the interaction with §2, not the numbers. Verdict: **1–3 players OK; 4 players tune via §2.**

Edge: the text never says what happens when a rest is forced at 0 sparks. L1197 loses the game only when "all characters are dead and there are no remaining sparks"; a single hollow death with 0 sparks and survivors standing is undefined (B-012).

### 5.2 Campaign
| Characters | Start = maximum | Boss +1 | Add a player | Drop a player |
|---|---|---|---|---|
| 1 | 5 | only if below 5 | pay 1 → 4 sparks, max 4 | – |
| 2 | 4 | only if below 4 | pay 1 → 3, max 3 | +1 → 5, max 5 |
| 3 | 3 | only if below 3 | pay 1 → 2, max 2 | +1 → 4, max 4 |
| 4 | 2 | only if below 2 | – | +1 → 3, max 3 |

Degenerate states:
- 4-player campaign with a maximum of 2: any boss defeated while the dial shows 2 yields nothing; two forced rests in one section leave 0 and the next hollow death ends the campaign. Official 1E campaign (Core p.33) allowed buying sparks back at 2 souls per character up to the maximum; the manuscript removes that valve (L2235 "Sparks cannot be purchased") without replacing it (B-013).
- Dropping from 4 to 3 players at 2 sparks gives 3 with a new maximum of 3 — fine; adding a 4th player to a 3-player party at 1 spark leaves **0** sparks with a maximum of 2 — the rule should forbid joining when the dial is at 1 or lower, or set the dial to at least 1 (B-013).
- The free post-boss rest of the basic game is withdrawn in campaign except for section finals (L2235), yet the "Setup After the mini-boss" step 11 (L1169) that grants it is the only place the free rest is written as procedure; the campaign chapter should state the replacement procedure explicitly (editorial, not numeric).

## 6. Hollow penalty (L781, L1215–1219, L1367) and encounter skipping (L1261–1263)

Rules: hollow = two right-hand spaces blocked, bar "from a total of eight stamina/damage cubes to only six" (L781); skipping a cleared encounter costs **2 stamina per skipped encounter per character**, so three skips = 6 stamina placed (L1263, the manuscript's own example); recovery is 1 stamina per turn (L1802) or a Rest major action; "If a character is ever forced to place a stamina cube … but there is no space … the character is instead marked staggered. A character may never elect to spend excess stamina" (L791–793); a damage cube with no space = death (L795).

### 6.1 Survivable hits
Free boxes K after setup, and P(death) from one Hollow Soldier activation (2 black block dice; from §2.3):

| State | K | A4 (1–2p) | A5 (3p) | A5 ×2 (4p) | Expected hits (A4) to die |
|---|---|---|---|---|---|
| Healthy, no skips | 8 | 0 | 0 | 0.058 | 4.8 |
| Hollow, no skips | 6 | 0 | 0 | 0.444 | 3.6 |
| Healthy, 2 skips (4 stamina) | 4 | 0.028 | 0.194 | 0.914 | 2.4 |
| Hollow, 1 skip (2 stamina) | 4 | 0.028 | 0.194 | 0.914 | 2.4 |
| Healthy, 3 skips (6 stamina) | 2 | **0.556** | **0.889** | 1.000 | 1.2 |
| Hollow, 2 skips (4 stamina) | 2 | **0.556** | **0.889** | 1.000 | 1.2 |
| **Hollow, 3 skips (6 stamina)** | **0** | **1.000** | **1.000** | **1.000** | 0 — any damage kills |

Worked line (healthy, 3 skips, A4): P(block ≤ 2) = 0.028 + 0.167 + 0.361 = 0.556 → the character dies from the first hit 56 % of the time.

### 6.2 Findings
- **Blocker (B-014):** a hollow character who skips three cleared encounters starts the fourth encounter with 6 stamina on a 6-space bar: zero free space. Any damage kills; any stamina-costing action is impossible (the stamina rule converts it to Stagger and forbids electing to overspend), so the character cannot run, dodge, or use most attack options, and the Rest action (restore all stamina) is the only legal major action. The manuscript's own example (L1263) therefore describes a state that is lethal to every hollow character in the party — and any hollow death fails the encounter and costs a spark (L1223). Even a healthy character with three skips has 2 free boxes and a 56 % chance of dying to one Hollow Soldier hit at 1–2 players (89 % at 3 players).
- The skip is meant to replace the ten minutes of re-fighting a cleared tile with a stamina tax; the tax is too high relative to an 8-box bar. Recommended value: **1 stamina per skipped encounter**, maximum 3 (hollow 3 skips → 3 free boxes, healthy → 5); or 2 per skip with a cap of 4 in total. Alternatively, hollow characters may not skip (clumsy).
- The hollow penalty alone (−2 of 8 = −25 % capacity) is sharper than Hollowed Edition's, which applies the same −2 cubes to a **ten**-box bar (Hollowed p.5 with the official board) = −20 %. If the 2E intends to use official dashboards (ten boxes, Core p.20) the manuscript's "eight" is simply wrong and every figure in this report shifts two boxes in the player's favour (B-015).
- Interaction with the Ember reduction (L1237: damage > 2 reduced by 1): against A4 with 2 black dice, P(dmg ≥ 3) = 0.194, so the ember saves 0.19 expected damage per hit (12 % of 1.67). Minor.

Verdict: hollow −2 **OK**; skip cost **broken** as written (fix to 1 per skip).

## 7. Stat scaling threshold (L1880) and Tier Four value (L1914)

Rule: +1 attack on every option of a weapon when the character's stat **exceeds the weapon's highest requirement by ten or more**; Tier Four = Tier Three + 5.

### 7.1 Dashboard tiers available
Herald (Core p.11 image): STR 12/19/28/37, DEX 11/17/26/34, INT 8/12/20/29, FTH 13/22/31/40. Cleric (V2 p.26): STR 12/18/27/37, DEX 8/15/24/33, INT 7/14/22/30, FTH 16/23/32/40. Tier Four under the manuscript rule: Herald STR 42, DEX 39, INT 34, FTH 45; under Core p.33 / Hollowed p.3: 40 for all.

### 7.2 Worked examples (weapons from the manuscript table L3212–3330)
| Weapon | Req. (STR/DEX) | Highest | Stat needed for +1 (≥ highest + 10) | Herald reaches it at | Cleric reaches it at |
|---|---|---|---|---|---|
| Sunlight Straight Sword | 15/15 | 15 | 25 (STR or DEX) | STR Tier Two (28) | STR Tier Two (27) |
| Mace | 16/0 | 16 | STR 26 | STR Tier Two (28) | STR Tier Two (27) |
| Rapier | 14/21 | 21 | DEX 31 | DEX Tier Three (34) | DEX Tier Three (33) |
| Uchigatana | 14/32 | 32 | DEX 42 | never (DEX T4 = 39 by L1914; 40 by Core p.33) | never (38 / 40) |
| Falchion (as printed) | 37/30 | 37 | STR 47 | never (STR T4 = 42 / 40) | never |
| Dragon Tooth | 40/25 | 40 | STR 50 | never | never |

Arithmetic: Mace highest requirement 16; 16 + 10 = 26; Herald STR Tier Two = 28 ≥ 26 → scaled. Rapier 21 + 10 = 31; Herald DEX Tier Two 26 < 31, Tier Three 34 ≥ 31 → scaled at Tier Three.

### 7.3 Findings
- Scaling is only ever reachable for tier-one weapons (highest requirement ≤ 24 → threshold ≤ 34, within Tier Three for STR/DEX/FTH on these boards). **No tier-two weapon (requirement ≥ 25) can ever scale**, because the threshold would be ≥ 35 and the highest Tier Four value is 40–45. The rule therefore rewards keeping a starting or tier-one weapon into the end-game — the opposite of the "seek out powerful weapons" goal (L365). Tune: lower the margin to **five** (tier-two weapons with requirement ≤ 35 then scale at Tier Four; the Mace still scales at Tier Two) or make scaling +1 per full ten points over the *lowest non-zero* requirement (B-016).
- Tier Four "+5 over Tier Three" (L1914) produces class-dependent Tier Four values (Herald FTH 45, INT 34) and contradicts both the official campaign rule and Hollowed Edition (both: Tier Four = 40). With "+5", a Herald's FTH Tier Four (45) exceeds the highest printed requirement in the manuscript (40); with "= 40" the Herald's FTH Tier Four is identical to Tier Three (40) and worth nothing. Recommend: **"Tier Four is treated as 40, or Tier Three + 5 if that is higher"** — i.e. max(40, T3 + 5) — which is a strict improvement for every stat and keeps the official number (B-017).

## 8. Tier split at ≥ 25 applied to "Weapons — Updated Stat Requirements" (L3208–3330)

Rule (L1013, L1045–1057): any card with a requirement ≥ 25 in any stat is tier two; everything below is tier one. Applied to the 60 revised rows: **22 tier one, 38 tier two** (63 % of the revised weapons are pushed into the post-mini-boss deck). Original official requirements are **not in any supplied source** (the Extended Rules PDF has no stat tables; the Core rulebook shows only Battle Axe STR 14, Fume Ultra Greatsword STR 37 and Faraam Armour STR 20 as card images), so "flips tier" cannot be verified here; rows that sit within ±1 of the split are marked because a one-point revision moves them between decks.

### 8.1 Clean table
| Weapon | STR | DEX | INT | FTH | Highest req. | Tier (>=25) | Notes |
|---|---|---|---|---|---|---|---|
| Avelyn | 23 | 30 | 0 | 0 | 30 | Two | Crossbow; STR 23 raised to balance (DS1: 16 STR/8 DEX). |
| Bewitched Alonne Sword | 18 | 24 | 0 | 0 | 24 | One | 18/24 tier one; DEX 24 one under the split. |
| Black Knight Greataxe | 32 | 20 | 0 | 0 | 32 | Two | Tier two; consistent with Black Knight Halberd 32. |
| Black Knight Halberd | 32 | 18 | 0 | 0 | 32 | Two | Boss treasure in the Community Update list (L3156) yet also in the common revision table. |
| Brigand Axe | 19 | 16 | 0 | 0 | 19 | One |  |
| Butcher Knife | 25 | 0 | 0 | 0 | 25 | Two | STR 25 exactly: falls into tier two by one point with no secondary requirement. Suspicious: a basic DS1 weapon. |
| Caestus | 0 | 15 | 0 | 0 | 15 | One | STR 0 for a fist weapon contradicts the stated method (add STR or DEX if previously zero). |
| Carthus Curved Greatsword | 19 | 30 | 0 | 0 | 30 | Two | 19/30: the greatsword requires LESS STR than the Carthus Curved Sword (25/35). Inverted pair. |
| Carthus Curved Sword | 25 | 35 | 0 | 0 | 35 | Two | 25/35: heavier than its greatsword; STR 25 puts a one-handed curved sword in tier two. |
| Chariot Lance | 22 | 33 | 0 | 0 | 33 | Two | 22/33 tier two on DEX. |
| Claws | 0 | 20 | 0 | 0 | 20 | One | 0/20 vs Manikin Claws 24/24: same weapon class, 24 STR difference. Suspicious. |
| Crystal Straight Sword | 21 | 30 | 0 | 0 | 30 | Two | Tier two on DEX 30. |
| Dark Silver Tracer | 0 | 25 | 0 | 0 | 25 | Two | DEX 25 exactly: tier two by one point; STR 0. |
| Dragon Tooth | 40 | 25 | 0 | 0 | 40 | Two | STR 40 is reachable only at Tier Four (Herald STR T3 37, T4 42 under L1914 or 40 under Core p.33). |
| Drake Sword | 27 | 17 | 0 | 0 | 27 | Two | Tier two on STR 27. |
| Drakewing Ultra Greatsword | 33 | 23 | 0 | 0 | 33 | Two | Tier two. |
| East-West Shield | 28 | 0 | 0 | 0 | 28 | Two | A shield inside the weapons table; STR 28 puts a basic shield in tier two. |
| Falchion | 37 | 30 | 0 | 0 | 37 | Two | 37/30: a basic DS1 curved sword with a higher STR requirement than the Black Knight Greataxe (32). Almost certainly a transposition (e.g. 17/30 or 13/37). |
| Four-Pronged Plough | 23 | 18 | 0 | 0 | 23 | One |  |
| Giant's Halberd | 27 | 16 | 0 | 0 | 27 | Two |  |
| Gold Tracer | 25 | 35 | 0 | 0 | 35 | Two | 25/35: both stats high for a DEX dagger-class weapon; STR 25 is one point over the split. |
| Gravelord Sword | 32 | 18 | 0 | 0 | 32 | Two | 32/18 tier two; boss treasure listed at L3176 as well. |
| Great Mace | 28 | 0 | 0 | 0 | 28 | Two | 28/0 vs Mace 16/0: +12 STR is plausible; tier two. |
| Halberd | 31 | 18 | 0 | 0 | 31 | Two | Tier two on STR 31. |
| Irithyll Rapier | 24 | 24 | 0 | 0 | 24 | One | 24/24: one point under the split on both stats; tier one. |
| Irithyll Straight Sword | 23 | 23 | 0 | 0 | 23 | One | 23/23: tier one. |
| Lifehunt Scythe | 32 | 23 | 0 | 0 | 32 | Two | 32/23 tier two; boss treasure listed at L3168 as well. |
| Lucerne | 22 | 31 | 0 | 0 | 31 | Two | 22/31: tier two on DEX for a polearm; check against Halberd 31/18 (STR-weighted). |
| Mace | 16 | 0 | 0 | 0 | 16 | One | 16/0 tier one; compare Morning Star 16/0 identical. |
| Manikin Claws | 24 | 24 | 0 | 0 | 24 | One | 24/24 vs Claws 0/20; one point under tier two on both stats. |
| Morning Star | 16 | 0 | 0 | 0 | 16 | One | Identical to Mace (16/0). |
| Murakumo | 27 | 17 | 0 | 0 | 27 | Two |  |
| Onikiri And Ubadachi | 26 | 36 | 0 | 0 | 36 | Two | 26/36 tier two. |
| Painting Guardian Curved Sword | 18 | 26 | 0 | 0 | 26 | Two |  |
| Parrying Dagger | 14 | 21 | 0 | 0 | 21 | One | 14/21 identical to Rapier 14/21. |
| Partizan | 28 | 17 | 0 | 0 | 28 | Two |  |
| Pike | 23 | 16 | 0 | 0 | 23 | One |  |
| Poison Throwing Knives | 0 | 14 | 0 | 0 | 14 | One | Identical to Throwing Knives (0/14). |
| Priscilla's Dagger | 0 | 31 | 0 | 0 | 31 | Two | 0/31 tier two; boss treasure listed at L3166 as well. |
| Rapier | 14 | 21 | 0 | 0 | 21 | One | 14/21 identical to Parrying Dagger; both tier one. |
| Reinforced Club | 23 | 0 | 0 | 0 | 23 | One |  |
| Rotten Ghru Dagger | 17 | 17 | 0 | 0 | 17 | One |  |
| Rotten Ghru Spear | 12 | 21 | 0 | 0 | 21 | One | 12/21: lowest STR of any polearm; tier one. |
| Royal Dirk | 18 | 31 | 0 | 0 | 31 | Two | 18/31 tier two on DEX for a dagger. |
| Scimitar | 18 | 20 | 0 | 0 | 20 | One |  |
| Shield Crossbow | 33 | 20 | 0 | 0 | 33 | Two | 33/20: STR 33 for a crossbow; tier two. |
| Shotel | 26 | 29 | 0 | 0 | 29 | Two |  |
| Silver Knight Spear | 22 | 26 | 0 | 0 | 26 | Two |  |
| Silver Knight Straight Sword | 16 | 22 | 0 | 0 | 22 | One |  |
| Spiked Mace | 32 | 22 | 0 | 0 | 32 | Two |  |
| Spotted Whip | 23 | 30 | 0 | 0 | 30 | Two | 23/30 tier two on DEX. |
| Sunlight Straight Sword | 15 | 15 | 0 | 0 | 15 | One | 15/15 tier one. |
| Throwing Knives | 0 | 14 | 0 | 0 | 14 | One | 0/14: items in a weapons table; identical to Poison Throwing Knives. |
| Uchigatana | 14 | 32 | 0 | 0 | 32 | Two | 14/32: an early DS1 weapon placed in tier two by DEX 32. |
| Umbral Dagger | 18 | 35 | 0 | 0 | 35 | Two | 18/35 tier two on DEX. |
| Vordt's Great Hammer | 33 | 0 | 0 | 0 | 33 | Two | 33/0 tier two; boss weapon in the common table. |
| Warden Twinblades | 17 | 25 | 0 | 0 | 25 | Two |  |
| Washing Pole | 37 | 21 | 0 | 0 | 37 | Two | 37/21: STR 37 for a katana (DEX weapon in source); tier two on STR. |
| Winged Knight Halberd | 32 | 16 | 0 | 0 | 32 | Two | 32/16 tier two. |
| Winged Spear | 20 | 22 | 0 | 0 | 22 | One |  |

Rows within ±1–2 of the split (a one-point edit changes deck): Bewitched Alonne Sword 18/24, Butcher Knife 25/0, Dark Silver Tracer 0/25, Four-Pronged Plough 23/18, Irithyll Rapier 24/24, Irithyll Straight Sword 23/23, Manikin Claws 24/24, Painting Guardian Curved Sword 18/26, Pike 23/16, Reinforced Club 23/0, Silver Knight Spear 22/26, Warden Twinblades 17/25.

Identical stat lines (nine pairs): Avelyn = Spotted Whip (23/30); Black Knight Halberd = Gravelord Sword (32/18); Carthus Curved Sword = Gold Tracer (25/35); Drake Sword = Murakumo (27/17); East-West Shield = Great Mace (28/0); Irithyll Rapier = Manikin Claws (24/24); Mace = Morning Star (16/0); Parrying Dagger = Rapier (14/21); Poison Throwing Knives = Throwing Knives (0/14). Duplicates are not errors in themselves, but Parrying Dagger = Rapier and Claws (0/20) ≠ Manikin Claws (24/24) suggest rows were filled by analogy rather than from the source material the rationale (L3210) cites.

### 8.2 Suspicious rows (B-018 … B-021)
| Row | Why suspicious | Suggested check |
|---|---|---|
| Falchion 37/30 | A basic curved sword with the highest STR requirement in the table bar Dragon Tooth; higher than Black Knight Greataxe (32) and Vordt's Great Hammer (33). | Probable digit transposition: 17/30 (tier two on DEX) or 13/27. |
| Carthus Curved Sword 25/35 vs Carthus Curved Greatsword 19/30 | The greatsword is lighter in both stats than the one-handed sword. | Swap the two lines, or set the sword to 19/30 and the greatsword to 25/35. |
| Butcher Knife 25/0 | Exactly on the split with no second stat; a basic DS1 weapon lands in the post-mini-boss deck. | 24/0 (tier one) or 28/0 if intended as a heavy weapon. |
| Rapier 14/21 = Parrying Dagger 14/21 | Identical lines for a main-hand thrusting sword and an off-hand parry tool. | Parrying Dagger 10/18 or similar. |
| Great Mace 28/0 vs Mace 16/0 | Plausible (+12), but Great Mace = East-West Shield (28/0) exactly. | None required. |
| Claws 0/20 vs Manikin Claws 24/24 | Same weapon class; 24 STR added to one and 0 left on the other contradicts the stated method ("adding a strength or dexterity requirement if previously zero"). | Claws 12/20; Manikin Claws 14/24. |
| Caestus 0/15; Throwing Knives 0/14; Dark Silver Tracer 0/25; Priscilla's Dagger 0/31 | STR 0 remains after a revision whose stated purpose was to remove zero requirements. | Give each a STR value or state that 0 is intentional. |
| Washing Pole 37/21; Shield Crossbow 33/20; Avelyn 23/30 | STR-heavy requirements on DEX weapons/crossbows. | Confirm against the author's balance notes. |
| East-West Shield 28/0 | A shield inside a weapons table; see §9 on whether "shield" is a card type. | Move to an armour/shield table. |
| Black Knight Halberd, Gravelord Sword, Lifehunt Scythe, Priscilla's Dagger, Vordt's Great Hammer | Also appear in the boss-treasure lists (L3156–3176) yet are revised as if common; boss treasure is excluded from both tier decks (L1059). | Mark as boss treasure in the table or remove. |

