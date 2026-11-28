# Enemy data cards (2017 expansions) and 2022 treasure cards: web research

Compiled by web research only. Raw downloads are in `/tmp/claude-0/-home-user-DSTBG2E/ff710c3a-8948-5673-b38b-8c94b4dc4aee/scratchpad/web2022/`. Companion JSON for Part A: `/home/user/DSTBG2E/work/phase7/enemy_cards_web.json` (extra keys beyond your shape: `push_dmg` and `effects` on move steps, `expansion`, `notes`).

## Sources and how far to trust them

| Tag | Source | Type |
|---|---|---|
| S1 | Steamforged official Core rulebook, `https://gamers-hq.de/media/pdf/97/3a/29/DS-Core-Rules-lores.pdf`, pp.24-25 (enemy movement and attack icons) and p.40 (icon key) | official document |
| S2 | Official Darkroot rulebook `https://desktopgames.com.ua/games/5951/DS_Darkroot_Rules_web.pdf` and Iron Keep rulebook `https://gamers-hq.de/media/pdf/g0/e8/c6/DS-IronKeep-Rules-Web.pdf` | official document |
| S3 | DSBG-Shuffle repository (`github.com/DanDuhon/DSBG-Shuffle`, files under `lib/`): `dsbg_shuffle_images/enemies/<Enemy> - data.jpg`, `dsbg_shuffle_enemies.py`, `dsbg_shuffle_behaviors.py`, `dsbg_shuffle_encounters/<Encounter><1-4>.json`; fetched via raw.githubusercontent.com | community re-creation of the printed cards (read from card image) plus community data |
| S4 | Community Google Sheet "DSBG - Enemy & Equipment" (`https://docs.google.com/spreadsheets/d/1q76mS5wAMcfct8izvUsggbTJbezmfTuf_uPG5CPLsSc/`, found via the "DSBG - Unofficial Guide & Rules FAQ" Google Doc), sheets Enemies, Encounters, Equipment | community database |

Not reachable from this session: the GitHub API and codeload (blocked), the Fextralife wiki (host not allowed). The Steamforged expansion rulebooks contain no per-enemy behaviour ("The information for these miniatures can be found on their corresponding enemy data cards"), so the data-card images in S3 are the only per-enemy source found. The Explorers rulebook was not located.

## How I read the data-card images (legend, from S1 pp.24-25, 40)

- Top-left number = threat. Left-bottom roundel = attack range (0, 1, 2 or infinity; a dash = no attack).
- Four-way arrow with a number: number on the top arrow = move towards, number on the bottom arrow = move away.
- Ring icon = targets the nearest character; skull icon = targets the character with the aggro token. The ring or skull beside the arrow belongs to the move, the one on the right belongs to the attack.
- Shield-with-crown icon at the top-left corner of the arrow = the move pushes. Shield-with-crown in the middle, left of the attack's target icon = the attack pushes.
- Small ring-with-dot icon below = node attack (hits everyone on the node).
- Behaviour icons resolve left to right. For Silver Knight Spearman and Greatbowman the attack is at the left and the arrow to its right, so they attack first and move second.
- The community images leave damage, damage type, push damage and dodge blank (DSBG-Shuffle overlays them), so those come from S3 `behaviors.py`, cross-checked against S4.
- The card shows the node, push and range icons directly. A repeat icon is not drawn on any image; Shears Scarecrow's repeat comes from S3/S4 only.

## Part A: enemy data-card behaviour

Targets: "nearest" = ring, "aggro" = skull. Damage, type and dodge are your cross-check values.

| Enemy | Expansion | Threat | Steps in activation order | Source | Confidence |
|---|---|---|---|---|---|
| Stone Guardian | Darkroot | 6 | Move 1 towards aggro holder, push (4 dmg); Attack aggro holder, range 1, 5 physical, dodge 1, node, push | S3 image + S1 legend; S4 agrees | high |
| Stone Knight | Darkroot | 7 | Move 1 towards nearest; Attack nearest, range 0, 5 magic, dodge 1, push | S3 image + S1 legend; S4 agrees | high |
| Demonic Foliage | Darkroot | 3 | Move 1 towards nearest, push; Attack nearest, range 1, 5 physical, dodge 1 | S3 image + S1 legend; S4 agrees | high |
| Mushroom Parent | Darkroot | 1 | Move 1 towards nearest, push (6 dmg), stagger. Note: No attack step (range shown as a dash). Damage 6 is the push damage on the movement. | S3 image + S1 legend; S4 agrees | high |
| Mushroom Child | Darkroot | 2 | Move 1 towards nearest; Attack nearest, range 0, 5 physical, dodge 1 | S3 image + S1 legend; S4 agrees | high |
| Plow Scarecrow | Darkroot | 4 | Move 2 towards aggro holder; Attack aggro holder, range 1, 4 physical, dodge 2 | S3 image + S1 legend; S4 agrees | high |
| Shears Scarecrow | Darkroot | 8 | Move 1 towards nearest; Attack nearest, range 0, 3 physical, dodge 2, node, repeat 2. Note: Repeat 2 comes from DSBG-Shuffle behaviors.py and the spreadsheet (Repeat Actions=2); the card image shows no repeat icon, so which steps repeat (attack only, or move+attack) is unverified. | S3 image (move, range, node) + S3/S4 (repeat) | medium |
| Alonne Bow Knight | Iron Keep | 2 | Move 2 away from aggro holder; Attack aggro holder, range unlimited, 4 physical, dodge 2, push | S3 image + S1 legend; S4 agrees | high |
| Alonne Sword Knight | Iron Keep | 5 | Move 2 towards nearest; Attack nearest, range 0, 5 physical, dodge 1 | S3 image + S1 legend; S4 agrees | high |
| Alonne Knight Captain | Iron Keep | 8 | Move 2 towards nearest; Attack nearest, range 0, 5 magic, dodge 1 | S3 image + S1 legend; S4 agrees | high |
| Ironclad Soldier | Iron Keep | 6 | Move 1 towards nearest, push (5 dmg), stagger. Note: No attack step (range dash). 5 is push damage on the movement; dodge 2. | S3 image + S1 legend; S4 agrees | high |
| Firebomb Hollow | Explorers | 2 | Move 1 towards aggro holder; Attack aggro holder, range 2, 3 magic, dodge 1, node, push. Note: Printed range is 2, outside your 0/1/9 set. | S3 image + S1 legend; S4 agrees | high |
| Silver Knight Spearman | Explorers | 8 | Attack nearest, range 1, 6 physical, dodge 2; Move 1 towards aggro holder, push. Note: Attack comes first (left), then the move with push (no damage number). | S3 image + S1 legend; S4 agrees | high |
| Mimic | Sunless City / Explorers (see notes) | 4 | Move 2 towards aggro holder; Attack aggro holder, range 1, 6 physical, dodge 2, push. Note: Image + DSBG-Shuffle damage only: the spreadsheet has no stat row for plain Mimic, and DSBG-Shuffle lists it under The Sunless City. | S3 image + S1 legend | medium |
| Hungry Mimic | Explorers | 10 | (no printed steps; behaviour deck). Note: Mini-boss style: data card has threat 10, behaviour deck size 4, a heat-up icon and the 'Loot the Body' text, but no movement or attack icons; behaviour lives on boss behaviour cards (not obtained). | S3 image | medium |
| Voracious Mimic | Explorers | 10 | (no printed steps; behaviour deck). Note: As Hungry Mimic; same card layout, threat 10, deck size 4. | S3 image | medium |
| Crystal Lizard | Iron Keep | 1 | Move 1 away from nearest. Note: Not an Explorers enemy; it is in Iron Keep. Move away 1 from nearest is from the spreadsheet only; no card image to confirm. | S4 + S2 | low |
| Hollow Soldier | Core | 5 | Move 1 towards nearest; Attack nearest, range 0, 4 physical, dodge 1. Note: Matches the printed sample card on official Core rulebook p.24. | S3 image + S1 legend; S4 agrees; S1 p.24 sample card | high |
| Crossbow Hollow | Core | 2 | Move 1 away from aggro holder; Attack aggro holder, range unlimited, 3 magic, dodge 1. Note: Magic damage type comes from DSBG-Shuffle and the spreadsheet; the card image cannot show it. | S3 image + S1 legend; S4 agrees | high |
| Large Hollow Soldier | Core | 6 | Move 1 towards nearest, push (5 dmg). Note: No attack step (range dash). | S3 image + S1 legend; S4 agrees | high |
| Sentinel | Core | 9 | Move 1 towards nearest, push; Attack nearest, range 1, 6 physical, dodge 1, node | S3 image + S1 legend; S4 agrees | high |
| Silver Knight Swordsman | Core | 7 | Move 2 towards nearest; Attack nearest, range 0, 5 physical, dodge 2, node, push | S3 image + S1 legend; S4 agrees | high |
| Silver Knight Greatbowman | Core | 3 | Attack aggro holder, range unlimited, 4 physical, dodge 1, node; Move 1 away from aggro holder. Note: Attack first (left), then the move. | S3 image + S1 legend; S4 agrees | high |

### Agreement and disagreement between sources

- Threat on every card image equals the `threat` value in S3 `dsbg_shuffle_enemies.py` and the Threat Level in S4, for all 20 enemies that have an image. No disagreement.
- Move distance and direction, move push, attack push and node flags from the images match S4 (Move, Move Push, Move DMG, Attack Push, Node Attack columns) for every enemy that has an S4 row. Range matches if S4's integer 1 is read as range 0 (S4 stores melee as integer 1 and real range 1 as 1.0). Exceptions in range: Firebomb Hollow prints 2 (S4 2.0), ranged enemies print infinity (S4 3.0).
- Stone Knight prints range 0 on its card although it is a magic attack; S4 shows integer 1, consistent with 0.
- Your damage values (S3 `behaviors.py`) equal S4 DMG Phy/Mag for all rows checked. S3 and S4 are both community data, not independent of the printed cards. Crossbow Hollow magic damage and Large Hollow Soldier's lack of an attack are in both S3 and S4 but cannot be seen on the images; for the Core enemies the official sample on S1 p.25 only confirms the icon grammar.
- S3 `behaviors.py` stores `left/middle/right` slots: `left` push = movement push damage (this is what the Stone Guardian, Mushroom Parent, Ironclad Soldier, Large Hollow Soldier entries mean), `middle` = attack damage and type, `right` = repeat. This is my inference from matching them against the images; no documentation found.
- Unverified (from memory): none used for the table.

### Not established or weakly established

- Hungry Mimic and Voracious Mimic: threat 10 and deck size 4 are read from the images, but their behaviour cards were not found, so no steps are given. Cards exist in S3 only as `data.jpg`; behaviour names (Aggressive Grab, Charging Chomp, and so on) are listed in S3 `behaviors.py` without values.
- Crystal Lizard: no data-card image in S3 (the file does not exist). Threat 1 and "move away 1" are from S4 only (low confidence). Official Iron Keep rulebook confirms only that it does not actively attack and need not be killed. It is an Iron Keep enemy, not Explorers.
- Mimic (plain): S3 lists it as The Sunless City; S4 gives no stat row. Image-derived behaviour (move 2 to aggro, attack aggro range 1 with push, 6 physical, dodge 2) is medium confidence.
- Shears Scarecrow repeat scope, as above.
- Whether the printed Silver Knight Spearman has any push damage number: the image shows a bare crown (no number) and S4 Move DMG is 0.

## Encounter cards of Darkroot, Iron Keep, Explorers

A public machine-readable list exists in two independent places that agree on all 51 encounters. Sources: S3 `dsbg_shuffle_encounters.json` (name, expansion, level) plus the per-encounter files `lib/dsbg_shuffle_encounters/<name><players>.json` (field `original`, enemy ids; identical for 1 to 4 players in all 51 files), and S4 sheet "Encounters" (enemies by node, terrain, Crystal Lizard counts). Both are community-transcribed from the cards. S3 names Iron Keep encounter 'Flaming Passageway' where S4 has 'Flaming Passage'. Neither gives the per-player-count enemy numbers printed on the real cards; S3's `original` is one list for all player counts, and Crystal Lizards are not in it. S4 gives Crystal Lizards through terrain nodes; for the six Iron Keep encounters that have them, counts are shown in the table. Saved raw files: `.../web2022/dsbg/enc/original_named.json` (S3, names resolved), `.../web2022/out/encounters_sheet_subset.json` (S4, 51 rows), `.../web2022/dsbg/dsbg_shuffle_encounters.json`.

| Expansion | Level | Encounter | Enemies (S3 order) | Crystal Lizards (S4) | Terrain (S4) |
|---|---|---|---|---|---|
| Darkroot | 1 | Blackroot Well | Demonic Foliage, Plow Scarecrow, Plow Scarecrow |  | Gravestone |
| Darkroot | 1 | Fearful Woods | Plow Scarecrow, Shears Scarecrow, Mushroom Child |  | Chest |
| Darkroot | 1 | Leafy Grotto | Shears Scarecrow, Plow Scarecrow, Demonic Foliage |  | Barrel |
| Darkroot | 1 | Misty Woods | Shears Scarecrow, Shears Scarecrow, Plow Scarecrow |  | Gravestone |
| Darkroot | 1 | Overgrown Caves | Mushroom Child, Demonic Foliage |  | Barrel |
| Darkroot | 1 | Wild Glades | Plow Scarecrow, Shears Scarecrow, Plow Scarecrow |  | Barrel, Chest |
| Darkroot | 2 | Black Bog | Demonic Foliage, Shears Scarecrow, Demonic Foliage, Plow Scarecrow |  | Barrel |
| Darkroot | 2 | Boggy Hollow | Stone Guardian, Mushroom Child |  | Gravestone |
| Darkroot | 2 | Haunted Ruins | Stone Knight, Demonic Foliage |  | Gravestone |
| Darkroot | 2 | Murky Roots | Mushroom Parent, Mushroom Child |  | Barrel |
| Darkroot | 2 | Stone Hollow | Plow Scarecrow, Shears Scarecrow, Stone Guardian |  | Chest |
| Darkroot | 2 | Withered Thicket | Mushroom Parent, Mushroom Child, Plow Scarecrow |  | Chest |
| Darkroot | 3 | Abandoned Tower | Demonic Foliage, Plow Scarecrow, Plow Scarecrow, Stone Knight, Plow Scarecrow |  | Gravestone |
| Darkroot | 3 | Corpselight Fens | Stone Knight, Demonic Foliage, Stone Guardian, Demonic Foliage |  | Gravestone |
| Darkroot | 3 | Dark Woods | Stone Guardian, Stone Guardian, Stone Knight |  | Chest |
| Darkroot | 3 | Desolate Hinterland | Stone Knight, Mushroom Parent, Mushroom Child |  | Barrel |
| Darkroot | 3 | Hydra Lake | Mushroom Parent, Demonic Foliage, Mushroom Child, Stone Knight |  | Barrel, Chest |
| Darkroot | 3 | Sodden Mire | Demonic Foliage, Plow Scarecrow, Demonic Foliage, Plow Scarecrow, Stone Knight |  | Barrel |
| Iron Keep | 1 | Blazing Plaza | Alonne Sword Knight, Crossbow Hollow, Crossbow Hollow |  | Barrel |
| Iron Keep | 1 | Burning Hold | Alonne Bow Knight, Hollow Soldier, Crossbow Hollow |  | Gravestone |
| Iron Keep | 1 | Charred Keep | Hollow Soldier, Crossbow Hollow, Hollow Soldier, Alonne Bow Knight |  | Barrel, Chest |
| Iron Keep | 1 | Flaming Passageway | Alonne Bow Knight, Alonne Sword Knight | 1 | Barrel |
| Iron Keep | 1 | Furnace Room | Alonne Sword Knight, Crossbow Hollow, Alonne Bow Knight |  | Chest |
| Iron Keep | 1 | Threshold Bridge | Alonne Bow Knight, Hollow Soldier, Crossbow Hollow | 1 | Gravestone |
| Iron Keep | 2 | Brass Sanctum | Alonne Knight Captain, Alonne Bow Knight, Alonne Bow Knight |  | Barrel, Gravestone |
| Iron Keep | 2 | Bronze Spire | Alonne Bow Knight, Ironclad Soldier |  | Gravestone |
| Iron Keep | 2 | Iron Depths | Alonne Bow Knight, Alonne Bow Knight, Alonne Knight Captain | 2 |  |
| Iron Keep | 2 | Pyre of Souls | Ironclad Soldier, Crossbow Hollow | 2 |  |
| Iron Keep | 2 | Searing Hallway | Ironclad Soldier, Alonne Sword Knight |  | Chest |
| Iron Keep | 2 | Smouldering Labyrinth | Alonne Knight Captain, Alonne Bow Knight, Alonne Sword Knight |  | Barrel, Chest |
| Iron Keep | 3 | Castle Aflame | Alonne Sword Knight, Ironclad Soldier, Alonne Bow Knight, Alonne Knight Captain |  | Chest |
| Iron Keep | 3 | Hollowed Threshold | Alonne Bow Knight, Alonne Knight Captain, Alonne Bow Knight, Alonne Bow Knight, Alonne Knight Captain |  | Gravestone |
| Iron Keep | 3 | Melting Gallery | Alonne Knight Captain, Alonne Knight Captain, Alonne Knight Captain | 2 |  |
| Iron Keep | 3 | Shrine of the Torch | Alonne Sword Knight, Alonne Sword Knight, Alonne Knight Captain, Alonne Bow Knight, Alonne Bow Knight |  | Barrel, Gravestone |
| Iron Keep | 3 | Smoking Gallery | Alonne Sword Knight, Alonne Sword Knight, Alonne Sword Knight, Alonne Bow Knight, Alonne Knight Captain | 2 |  |
| Iron Keep | 3 | Sweltering Sanctum | Ironclad Soldier, Ironclad Soldier, Alonne Bow Knight |  | Barrel, Chest |
| Explorers | 1 | Burning Swamp | Hollow Soldier, Crossbow Hollow, Firebomb Hollow |  | Barrel |
| Explorers | 1 | Halls of the Forsworn | Large Hollow Soldier, Firebomb Hollow, Hollow Soldier |  | Chest |
| Explorers | 1 | Lothric Castle | Hollow Soldier, Firebomb Hollow, Firebomb Hollow |  | Barrel |
| Explorers | 1 | Unholy Tunnels | Silver Knight Spearman, Hollow Soldier, Firebomb Hollow |  | Barrel, Chest |
| Explorers | 1 | Wicked Vault | Silver Knight Spearman, Firebomb Hollow |  | Barrel |
| Explorers | 2 | Lost Grotto | Silver Knight Spearman, Silver Knight Greatbowman, Silver Knight Spearman |  | Barrel, Chest |
| Explorers | 2 | Spirit Tomb | Silver Knight Swordsman, Silver Knight Spearman, Silver Knight Greatbowman |  | Gravestone |
| Explorers | 2 | Sunken Stairwell | Silver Knight Greatbowman, Silver Knight Swordsman, Silver Knight Spearman |  | Barrel |
| Explorers | 2 | The Void Pit | Firebomb Hollow, Firebomb Hollow, Large Hollow Soldier, Firebomb Hollow |  | Barrel, Gravestone |
| Explorers | 2 | Unhallowed Caves | Silver Knight Spearman, Silver Knight Spearman, Firebomb Hollow |  | Barrel, Gravestone |
| Explorers | 3 | Gallery of the Hidden Warrior | Silver Knight Spearman, Silver Knight Spearman, Silver Knight Greatbowman, Silver Knight Spearman, Silver Knight Greatbowman, Silver Knight Greatbowman |  | Chest, Gravestone |
| Explorers | 3 | Giant's Keep | Silver Knight Spearman, Silver Knight Swordsman, Silver Knight Greatbowman, Silver Knight Spearman, Silver Knight Swordsman |  | Barrel |
| Explorers | 3 | Hidden Chamber | Sentinel, Firebomb Hollow, Firebomb Hollow, Crossbow Hollow, Large Hollow Soldier |  | Barrel |
| Explorers | 3 | Refuge of Silence | Large Hollow Soldier, Silver Knight Spearman, Firebomb Hollow, Large Hollow Soldier, Silver Knight Spearman, Firebomb Hollow |  | Barrel |
| Explorers | 3 | Scarlet Battlement | Large Hollow Soldier, Firebomb Hollow, Hollow Soldier, Large Hollow Soldier, Silver Knight Spearman, Firebomb Hollow |  | Gravestone |

## Part B: 2022 treasure cards (Tomb of Giants, Painted World of Ariamis, The Sunless City)

### Is there a machine-readable source?

Yes, one: the community Google Sheet "DSBG - Enemy & Equipment" (S4, `https://docs.google.com/spreadsheets/d/1q76mS5wAMcfct8izvUsggbTJbezmfTuf_uPG5CPLsSc/`), sheet **Equipment**. It has one row per item (378 rows; 95 flagged Painted World, 97 Tomb of Giants, 95 Sunless City, with overlap, plus Characters-expansion, Darkroot, Iron Keep, Explorers, Phantoms and boss items). The DSBG-Shuffle repository itself does not have it: its `dsbg_shuffle_treasure.py` holds only name, type, class, encounter levels, expansions and the four stat requirements, no dice (I read the whole file; the image folder `lib/dsbg_shuffle_images` has only custom_encounters, encounters, enemies, events and icons subfolders, so no treasure card images). A search for other repositories, Tabletop Simulator saves, campaign managers and BoardGameGeek files found no JSON/CSV elsewhere. The Fextralife wiki host is blocked in this session, so its card pages could not be checked. The Tabletop Simulator mods only carry card images, and I did not download any.

Saved files (all in `/tmp/claude-0/-home-user-DSTBG2E/ff710c3a-8948-5673-b38b-8c94b4dc4aee/scratchpad/web2022/`):

- `sheet/dsbg_enemy_equipment.xlsx`: the whole workbook exported as xlsx (untrusted, never executed; read with openpyxl in isolated mode, cached values only).
- `out/equipment_dice.csv` and `out/equipment_dice.json`: my extraction of the Equipment sheet (header row 21, items rows 22 to 416) with the columns below renamed from the sheet's duplicate headers. Extraction script: `scripts/extract_eq.py` in the scratchpad.

### Schema (one record per card)

- Identity: `Name`, `Tier`, `Unique` (boss or mini-boss items), `Expansion`, `2nd Expansion`, `3rd Expansion` with `Type_9/12/15` and `Source_10/13/16` (Common, Transposed, Mini Boss, Main Boss, Mega Boss and the boss name), and four booleans `Core`, `Painted World`, `Tomb of Giants`, `Sunless City` (plus `Any Core Set`) showing which of the sets the card appears in. A card can be in several sets (for example Claymore is flagged Core, Painted World and Sunless City).
- `Type` (Weapon, Armor, Shield, Ring, Spell, Upgrade, Ember), `2H` (two-handed), stat requirements `Str`, `Dex`, `Int`, `Fth` (with `SUM` and `MAX`). Class and threat columns for class-specific items.
- Defence: `block1`, `block2` (die colours BLK/BLU/ORA of the block dice), `block_mod`, `resist1`, `resist2`, `resist_mod`, `dodge` (a count only), `slots_icons` and `slots_num` (upgrade slots), `buff`, `debuff`.
- Attack options: `a1_*`, `a2_*`, `a3_*` each with `range`, `cost` (stamina), `die1` to `die4` (BLK, BLU, ORA), `mod`, `mag` (magical), `node`, `bleed`, `poison`, `frost`, `stagger`, `push`, `move`, `buff`, `shaft`, `repeat`. Then `use_w_2h`, `description` (special text) and `has_duplicate` (the same name appears twice, for example a boss version and a Characters-expansion "transposed" version).

Example (Claymore): block die BLK; one upgrade slot; attack 1 range 1, stamina 1, two BLU dice, modifier +1; attack 2 range 1, stamina 4, two ORA dice, modifier +1; Str 30, Dex 26.

### Quality check

I compared the Str/Dex/Int/Fth requirements in the sheet against your source's `dsbg_shuffle_treasure.py` after normalising spelling (Armor/Armour): 191 cards matched on name, 187 matched exactly, 4 differ (Gold-Hemmed Black Robes, Crimson Robes, Halberd, Black Knight Shield; the sheet and the repository disagree, or a Legendary or transposed variant shares the name). So the sheet is largely consistent with the repository on identity, but that checks only requirements, not dice.

### Caveats

- It is a community database (S4), not an official document, and no card image was read to confirm dice. Treat dice values as unverified until sampled against physical cards or an official scan.
- Blank cells are ambiguous. For dice colour cells, blank means "no die". For `range`, `cost` and `mod` I believe blank means 0, but cannot confirm (for example Abyss Greatsword's first attack has a stamina cost of 1 and no range cell).
- The sheet gives a dodge count only, with no dice colour; block and resist carry colours. You asked for black/blue/orange dodge counts, and the sheet does not provide that.
- `mod` is a signed number (+1, -1, +2, -2); it is unclear whether it is the printed attack modifier or the sheet author's derived value.
- Boolean flags are stored as True or blank. A few attack options mark buffs as numbers (`buff` = 1, 2, 4, 10, 15), which looks like the author's own scoring weights, not printed values; the `description` text is the printed special rule.
- Card names use US spelling (Armor); your repository uses UK spelling (Armour). Join on a normalised key.
