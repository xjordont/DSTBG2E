# 2022 core-set enemies, original encounter line-ups, and three treasure cards: web research

Raw downloads (untrusted, never executed): `/tmp/claude-0/-home-user-DSTBG2E/ff710c3a-8948-5673-b38b-8c94b4dc4aee/scratchpad/web2022b/` (`img/` enemy data cards, `enc/` encounter JSON, `encimg/` encounter card images, `pdf/` rulebook and FAQ text, `misc/` DSBG-Shuffle source). Method as in `enemy_cards_web.md`; deliverables `enemies_2022_web.json`, `encounters_2022_web.json`.

## Sources
- S3 DSBG-Shuffle, `https://raw.githubusercontent.com/DanDuhon/DSBG-Shuffle/master/lib/`: `dsbg_shuffle_images/enemies/<Enemy> - data.jpg`, `dsbg_shuffle_encounters/<Name><1-4>.json`, `dsbg_shuffle_images/encounters/<Name>.jpg`, `dsbg_shuffle_variants.py`, plus the earlier local `dsbg_shuffle_behaviors.py`, `dsbg_shuffle_enemies.py`, `dsbg_shuffle_treasure.py`.
- S4 community sheet "DSBG - Enemy & Equipment" (local xlsx, sheets Enemies, Equipment, Unique Equipment).
- S5 official Tomb of Giants rulebook `https://cdn.shopify.com/s/files/1/0602/0156/6449/files/DS-TG-Rulebook-Compressed_compressed.pdf` (icon key, Resurrect, push-damage rule).
- S6 community "DSBG - Unofficial Guide & Rules FAQ" `https://docs.google.com/document/d/1DmbTaM68OoosZcSCFW0bTNgBWCaHSP2UE9Um-X4XF54/export?format=txt` (Skeleton Soldier errata and behaviour, leap, set contents).
- Not found: Painted World of Ariamis rulebook, Executioner's Chariot rulebook text, any official card scan, Fextralife wiki (host blocked earlier).

## Part 1: 14 enemy cards (`enemies_2022_web.json`, same shape as enemy_cards_web.json plus `hp`, `armor`, `resist`)
Extra step keys: `push_dmg` on attacks; `dir:"leap"` with `n:null` for leap moves; `effects:["resurrect"]`; `repeat` on a move. Range 9 = infinity, melee = 0, as before.
hp/armor/resist come from behaviors.py (`health`, `armor`, `resist`) and agree with the sheet (Health, Block, Resist) for all 14. The card images print them as blank icons, so they are not image-verified; hp is 1 or 5 only, which looks like a category value, so treat it with care.

| Enemy | Set | Threat | Steps | HP/Arm/Res | Confidence |
|---|---|---|---|---|---|
| Skeleton Soldier | ToG | 5 | move 1 to nearest, pushing for 2 physical + bleed; no attack | 1/2/1 | high |
| Skeleton Archer | ToG | 3 | attack aggro, inf, 4 phys, dodge 1; move 2 away from aggro | 1/1/1 | high |
| Skeleton Beast | ToG | 6 | move 1 to nearest, push 4, repeat 2 | 5/2/2 | medium (repeat scope) |
| Giant Skeleton Soldier | ToG | 2 | move 1 to nearest; attack nearest r1, 5 phys, push 2, dodge 1 | 5/1/1 | high |
| Giant Skeleton Archer | ToG | 1 | move 1 away nearest; attack aggro inf, 5 phys, push 2, dodge 2 | 5/1/1 | high |
| Necromancer | ToG | 7 | attack aggro inf, 3 magic, node, resurrect, dodge 1 | 5/1/2 | high |
| Bonewheel Skeleton | PW | 7 | move 1 to nearest, push 4, repeat 2 | 1/1/1 | medium |
| Crow Demon | PW | 9 | leap to aggro, push 6 | 5/1/2 | medium |
| Engorged Zombie | PW | 8 | move 1 to nearest; attack nearest r0, 4 magic, dodge 1 | 1/2/2 | high |
| Phalanx | PW | 4 | attack nearest r1 node 5 phys; move 1 to aggro | 5/1/1 | medium |
| Phalanx Hollow | PW | 4 | attack nearest r1 4 phys; move 1 to aggro | 1/1/1 | high |
| Snow Rat | PW | 1 | leap to aggro; attack aggro r0, 3 phys + poison | 1/0/1 | medium |
| Black Hollow Mage | Chariot | 8 | attack aggro inf, 4 magic, dodge 2, resurrect | 5/2/3 | medium |
| Falchion Skeleton | Chariot | 4 | move 2 to nearest; attack nearest r0, 3 phys + bleed, push | 1/1/1 | high |

Special card text:
- Necromancer and Black Hollow Mage: the card shows only the skeletal-hand Resurrect icon, no text. Official wording (S5, p.25): "If the resurrect symbol appears on an enemy card, at the end of the enemy's turn, place a skeleton soldier on the closest enemy spawn node to the enemy. If each skeleton soldier model is already on the playing area, ignore this rule." For the Mage the Chariot rulebook was not checked, so a Falchion Skeleton (not Skeleton Soldier) may be the spawned model; this is unverified.
- Phalanx: no text on the image; the sheet flags a special "Phalanx" rule. The Painted World rulebook was NOT found, so no verbatim rule. Only known: the Phalanx is shown as three Phalanx Hollow miniatures pushed together (S6).
- Skeleton Soldier (S6, rulings): pushes characters off its node at activation, then moves pushing and making a 2 physical attack against each node entered; push cannot be dodged; bleed token on failed dodge.
- Leap (Crow Demon, Snow Rat), S6: the enemy immediately reaches the movement target and proceeds with the attack if possible; push damage applies on the node where the leap ended.

Disagreements between sources:
1. Skeleton Soldier: the card prints range 0, the sheet has Range 1 (its melee encoding) and DMG Phy 0 with Move DMG 2. No icon shows a push crown; the push-damage reading rests on the sheet, behaviors.py, S5 legend and S6.
2. Engorged Zombie: card range 0, sheet Range blank.
3. Skeleton Beast, Bonewheel Skeleton: repeat 2 exists only in behaviors.py and the sheet, not drawn on the image.
4. Leap enemies: the sheet gives Move blank plus Leap=True; the image shows no distance number. Consistent, but the leap range limits are not stated by any source.
5. The Giant Skeleton Archer's move direction is read from the arrow (number on the bottom arrow = away); the sheet (Move -1) agrees.
No disagreement was found on threat (image = enemies.py = sheet for all 14), dodge (behaviors.py = sheet) or damage values.

## Part 2: original printed line-ups (`encounters_2022_web.json`)
Row shape as `original_named.json`: `[set, level, name, {"1":[enemies],"2":[...],"3":[...],"4":[...]}, same_for_all_player_counts, extra]`. The 5th element is `true` when the file is identical for 1 to 4 players (my inference of the earlier flag; it was true in all 51 earlier rows). Extra 6th element (new): `enemySlots_by_players`, tentative `slot_groups_1_player_tentative`, `card_text`, `card_text_source`.
The field that identifies the original line-up is `original` in `lib/dsbg_shuffle_encounters/<Name><players>.json` (a list of enemy ids, resolved with the ids of dsbg_shuffle_enemies.py; the `alternatives` field holds the shuffle variants). The list order follows `enemySlots`: slots 0-3 tile 1, 4 spawn, 5-6 tile 2, 7 spawn, 8-9 tile 3, 10 spawn (per a code comment in encounters.py); enemies are consumed from `original` slot by slot. The mapping of the slots to physical nodes is not documented, so the grouping is tentative.
Counts: Tomb of Giants 27 (9+9+9), Painted World 27 (9+9+9), Chariot 6 (2+2+2). Extras in the repository but not delivered: Tomb of Giants "Gravelord Nito Setup" (the boss encounter, listed as level 3; delivered as a 10th level-3 row, not one of the 27); five Chariot level-4 encounters (Brume Tower, Gate of Peril, Huntsman's Copse, Mega Boss Setup, Undead Purgatory; mega boss related) omitted.
Card text: transcribed by eye from the DSBG-Shuffle card images for all 54 (27+27) 2022 cards and Nito. In the images enemy names and several icons are blank, written `[icon]`; the objective text "Kill the [icon]" hides the enemy name. Spawn lines such as "Spawn a [icon] on [spawn 1]" can be completed from `enemySlots` but I did not guess them. The Chariot images show only the enemy-placement face (spawn rows, two terrain nodes, level); no rules text exists there, terrain listed in `terrain_from_image`. These are community re-creations, not scans of the printed cards: typos such as "thoes" (Nito flavour) and "Trecherous Tower" are as in the images. Confidence: line-ups medium-high (one community source, consistent with the card text where checkable: Pitch Black and Skeleton Ball name two Necromancers or two targets, Overlord and In Deep Water spawn counts match slot 4); card text medium (blanks).
Caveats:
- Lakeview Refuge is the only file that differs by player count: 1 player lists 10 enemies; 2, 3, 4 players append one extra Skeleton Soldier each and make slot 7 hold 2/3/4. Flattened by slot the 2-4 player lists are misaligned with slots, so treat that variation as low confidence (probably N Skeleton Soldiers on the tile-2 spawn).
- Abandoned Storeroom (objective "Break all barrels") lists one Giant Skeleton Soldier in the data; unverified against a real card.
- Crystal-lizard-like extras or terrain are not in these files; terrain beyond the Chariot images was not extracted.

## Part 3: treasure cards
Local data checked: `equipment_dice.json` (from the S4 sheet) and `dsbg_shuffle_treasure.py`. Dice colours BLK/BLU/ORA; blank range/cost/mod = 0 (assumed, as before).

| Card | Result |
|---|---|
| Manikin Claws | Found under the spelling "Mannikin Claws" (sheet and treasure.py). Darkroot expansion. Weapon, two-handed, sheet marks it Unique (expansion item); treasure.py: type weapon, no class, encounter levels 1-4, expansions Darkroot. Requirements DEX 24, INT 24 (both sources agree; sheet tier 2). 1 upgrade slot. Attack 1: stamina 2, two BLK dice, move 1, repeat 2. Attack 2: stamina 4, two BLU dice, move 1, repeat 2. Range blank (melee). No rules text in the sheet. Deck (common vs boss) not established. Related card "Claws" (Explorers): DEX 20, INT 20, same dice without the move. |
| Titanite Slab | Only the sheet row "Titanite (slab)": Upgrade, expansion Asylum Demon, Source Mega Boss, Stray Demon (so a boss/mega-boss treasure), tier 1, no stat requirements, one modifier +1, text "This weapon's attacks gain +1 damage". Not in treasure.py. The name "Titanite Slab" is my reading of the lower-case "(slab)" label; no official card text or image found. Confidence medium-low. |
| Titanite Chunk | NOT FOUND in the sheet, treasure.py, the Core, ToG, Iron Keep, Darkroot rulebooks or the web search. Searches found no card. The project manuscript (not edited) mentions it only through a "Community Update Pack" (a 25/25, tier two card, per `02_audit_table.csv` A-074), so it may exist in no official set. |
| Crescent Axe | Sheet row: Tomb of Giants, flagged Unique and Any Core Set; weapon, one-handed (2H blank); requirements STR 22, DEX 17, FTH 15; 2 upgrade slots; attack 1: range 1, no stamina cost shown, one BLU die, shaft; attack 2: range 1, stamina 4, two BLU dice, +1 modifier, shaft. No text. The FAQ lists it under Tomb of Giants "Common Items". NOT in treasure.py (so absent from the shuffle data). |
| Four-Pronged Plow | Darkroot; weapon, two-handed; STR 23, FTH 23 (sheet and treasure.py agree; treasure.py levels 1-4); block die BLK, resist die BLK; 1 upgrade slot; attack 1: range 1, stamina 1, one BLU die, shaft; attack 2: range 1, stamina 3, two BLU dice, shaft. No text. Unique Equipment sheet lists it. |

Caveat for all five: the dice come from a community sheet, not a card scan. Crescent Axe attack 1 shows no stamina cost (blank = 0 or missing).

## Not found
Painted World and Chariot rulebooks (Phalanx text, Chariot Resurrect wording); verbatim printed encounter text (only community re-creations with blanks); real per-player-count enemy numbers; Titanite Chunk; official text and deck for Manikin Claws and Titanite Slab; enemy hit-point values confirmed on a card.
