# Audit A — Rules Integrity Report

Project: Dark Souls: The Board Game — Second Edition (homebrew). Manuscript audited: `work/docx/manuscript.md` (pandoc conversion of `DarkSoulsTBG2E.docx`; body lines 361–3366). Companion data: `work/audit/A_rows.csv` (125 rows, IDs A-001–A-125). Date: 2026-11-10.

## 1. Method

1. The whole manuscript body (lines 361–3366) was read in sequence, chapter by chapter, and every rule that references another rule (death, hollowing, sparks, aggro, turn order, scaling, conditions, terrain, setup, shop, campaign, PvP, phantoms, invaders, mimics, crystal lizards, boss encounters) was traced to every other passage that touches the same object. Line numbers in the CSV refer to this file.
2. Each rule was tested for the five failure classes in the brief: (a) internal contradiction, (b) undefined state or unresolved edge case, (c) arithmetic or procedural breakage, (d) silent inheritance of an official rule that the manuscript never states, (e) loop or exploit. The seventeen specific checks in the brief were worked through in order, and the campaign listings were checked one by one.
3. Official texts were used as evidence of what a complete rule looks like, never as an authority over the manuscript: the 2017 core rulebook (all 40 pages), the 2022 V2 rulebook (all 32 pages), the official FAQ, and the Characters, Phantoms, Darkroot, Iron Keep, Explorers, Black Dragon Kalameet and Executioner's Chariot booklets were read in full from `work/text/`. The Hollowed Edition and Extended Rules homebrews were consulted only for precedent (solo souls, hollowing, stagger, two-highest-dice defence, condition stacking).
4. Where the manuscript is clear and complete its mechanical choice is treated as final even when it differs from official play; such choices are recorded in the Preserve list (section 5) so that later editorial passes do not "correct" them. A proposed fix is written only where the text is contradictory, silent, broken or exploitable.
5. Every claim in the CSV was verified against the quoted line before it was written; named campaign encounters were checked against the supplied expansion booklets (nine confirmed; the Gaping Dragon, Vordt, Four Kings, Manus and Last Giant booklets were not supplied and are marked unverified in A-111).
6. CSV discipline: eleven fields per row, `csv.QUOTE_ALL`, British English, lawbook voice in every Proposed fix, no hedge words (should / might / could / probably / perhaps / reasonably) and no "you" — verified by script.

## 2. Summary counts

| Severity | Rows |
|---|---|
| Blocker | 5 |
| Major | 41 |
| Minor | 74 |
| Note | 5 |
| **Total** | **125** |

Issue types: undefined-state 54, contradiction 23, omission 17, terminology 14, inherits-official-silently 8, arithmetic 4, procedural 3, loop/exploit 2.

Tags: REQUIRED 58, OPTIONAL 32, PROPOSED 8, CLEAN-UP 27. Rows needing a user decision (Decision needed = Y): 41.

Blockers: A-002, A-023, A-032, A-053, A-090.

## 3. The ten highest-risk findings

1. **A-053 — The "reduced" soul reward is never quantified (Blocker).** The Souls section distinguishes a full reward (first clear) from a reduced reward (repeat clear) and the campaign chapter repeats the distinction, but both Soul Reward Tables have a single column. Repeating cleared encounters is an explicit mechanic of this edition, so every repeat is currently unresolvable. Recommended: half the full reward rounded up, added as a second table column; alternative "full minus two, minimum one".

2. **A-023 — Enemy attack targeting is never defined (Blocker).** Enemy Attacks promises that the symbols beside the attack icon are "detailed later"; nothing follows. The aggro/nearest target icons, the node (area) attack, the out-of-range miss and the fact that a push-movement's number is an attack are all absent (the core rulebook p.25 supplies all four). Every enemy data card depends on them.

3. **A-090 — Event cards are a dealt component with no rules (Blocker).** Thirty-five event cards are listed, dealt to every tile, revealed at Encounter Start and scried via gravestones, yet no passage says what an event card is or does, and no supplied official or community source defines levelled event cards. The component must be defined in a new chapter or removed everywhere (decision required).

4. **A-032 — PvP attack resolution is undefined (Blocker).** The PvP chapter supplies a dodge-difficulty table but never says how a character's rolled attack value meets another character's block/resist/dodge/parry, nor how push, area-of-effect, condition or riposte icons apply to characters. Companion rows A-031 (PvP after every boss vs only the final boss), A-033 (trap placement) and A-034/A-035 complete the set.

5. **A-002 — Forced rest at zero sparks has no outcome (Blocker).** A hollow character's death fails the encounter while others live; the forced rest then costs a spark that may not exist, and the stated loss condition (all characters dead) never fires. The game's commonest defeat sequence lacks an end-state. Related: A-001 ("lost" undefined), A-003 (dropped souls of a hollow character), A-050 (mega-boss permadeath vs the hollow rule).

6. **A-057 — Treasure is both pre-dealt to tiles and drawn on clearing (Major).** Setup deals one treasure per character to every tile; Treasure Rewards says to draw from the deck when the encounter is cleared. Applied literally the party collects both. The pre-deal is the only reading that makes "even if they died" and the campaign tier rules mechanical; a decision is required.

7. **A-078 — The parry's stagger is void under the condition-removal rule (Major).** Stagger is removed at the end of the affected model's turn; a parry staggers an enemy during that enemy's own turn, so the token vanishes before any character can exploit it. A-079 adds that "subtract one from dodge" has no defined meaning for an enemy's fixed dodge difficulty.

8. **A-039 / A-040 — Two-boss encounters are undefined (Major).** Ornstein & Smough are listed as two main bosses in the components and as one boss in four campaigns; the only multi-boss rule is the node push. The doubled "Gargoyle (Mini-Boss)" entry in three campaigns likewise carries no rule (the official footnote about back-to-back fights is omitted). The core set's main boss and its first campaign section cannot be played from the text.

9. **A-048 / A-049 / A-104 — Campaign progression keyed to "boss" breaks for boss-less and mega-boss sections (Major).** Sparks, free rests, restocks and section setup all trigger on a boss kill, but four sections end in a named encounter and the Gauntlet has no bosses; the mega-boss "permanent death / players win" text (line 1195) fires mid-campaign in Demon Hunting and Big Game Hunting; and Demon Hunting Section One has no bonfire to be forced back to.

10. **A-073 / A-019 / A-020 — Turn-sequencing gaps (Major).** The character turn lists actions with no ordering rule (move after attack?), the boss-fight equal-turns rule locks every living character once anyone dies, and the phantom's "after all character turns" cannot be placed inside the boss/character alternation. Each is a one-sentence fix but each is hit in every session.

Also high-risk but cheap: A-088 (the "two by six" tile grid), A-068 (left/right slots never defined but the parry rule depends on them), A-045 (invasion timing when embers arrive from a boss kill), A-096 (Titanite Chunk vs Scale), A-013 (aggro when the holder dies), A-082/A-083 (enemies vs terrain and traps).

## 4. Decision register (rows with Decision needed = Y)

A-006, A-007, A-008, A-020, A-022, A-024, A-025, A-028, A-031, A-035, A-036, A-039, A-040, A-043, A-045, A-046, A-047, A-049, A-050, A-053, A-055, A-057, A-060, A-061, A-062, A-066, A-067, A-069, A-072, A-073, A-078, A-083, A-090, A-091, A-093, A-094, A-096, A-104, A-110, A-121, A-123.

The recommended text is in each row's Proposed fix; the alternative is named in Rationale. The largest design forks are: reduced-reward value (A-053); event cards keep-or-cut (A-090); pre-dealt vs drawn treasure (A-057); whether embering heals (A-006); mega-boss permadeath (A-049/A-050); stagger duration (A-078); invader/lizard exemption from attack scaling (A-028); PvP frequency (A-031); heal one or two damage on clearing (A-061); tier-four cost (A-067).

## 5. Preserve list — intentional, complete and coherent departures from official play (KEEP)

These rules differ from the 2017 and/or 2022 rulebooks but are stated clearly and work as written. They must not be "corrected" in later passes.

- **Round structure: all enemies act first, then every character in descending threat order, then aggro is reassigned** (lines 1281–1295, 1664). Replaces the official enemy-activation-between-each-character model. (A-124)
- **Invader acts after each individual character turn** (2025–2027) and **phantom acts once per character turn in boss fights** (as clarified by A-020). The manuscript states the invader's extra tempo is intended.
- **Aggro by damage dealt, ties keep the token** (1291–1293); **boss aggro moves on any damage** (2191).
- **Character turn: recover one stamina; minor actions Walk / Run / Equip / Heroic; one major action Attack / Rest / Estus / Ember** (1800–1834). Rest blocked after Run. Armour may be swapped mid-encounter via Equip.
- **Stamina overflow becomes a stagger token; excess stamina may never be spent electively** (787).
- **Hollowing: death with a surviving party revives the character hollow (−2 endurance); a hollow death fails the encounter and forces a spark rest; hollow is removed by rest or ember** (1213–1223, 1367).
- **Dropped souls are personal, stay on the tile and return only to the dropper on a surviving clear** (1395–1399); souls are personal and non-transferable (1387).
- **Skipping cleared encounters costs two stamina per skipped encounter per character** (1261); **cleared encounters may be repeated for souls but not treasure** (1321–1327).
- **Encounter recovery heals only a little between fights (one or two damage — see A-061) and does not refresh Estus, Luck or Heroic tokens** (1345–1353).
- **Spark gained per boss instead of a reset; free rest after a boss; campaign spark maximum = starting value** (1249, 1908, 2233).
- **Shops: two tiers stocked by category quotas; restock only after a boss (campaign: only after a section); embers only from the tier one shop at setup, limited supply; prices 2 / 4, sell 1, boss treasure sells for 6 (campaign 4)** (1061–1089, 1933–1957).
- **Treasure tiers split at a stat requirement of 25; transposed cards are tier two; five legendaries enter the tier two deck; a single random boss treasure per boss kill** (1013–1053, 1479).
- **Campaign economy: ascetic (16 souls) unlocks tier two and gives all non-boss enemies +1 attack; transposition of boss treasure into legendaries for 4 souls; soul rewards one lower; stat costs 4/8/16/20** (2287–2348).
- **Stat scaling (+1 attack when a stat exceeds the highest requirement by 10) and tier four = tier three + 5** (1880, 1914).
- **Two-handed reroll of one die, including a lone one-handed weapon** (1876).
- **Spells: one spell attack option per turn; three spells stored per catalyst; no scaling or two-handed bonus; upgrade spells cast as a major action for the encounter** (851–887).
- **Defence: block/resist uses the two highest dice; dodge costs one stamina, +2 stamina for an extra die (max four), success forces a move; failed dodge rolls armour dice only; parry (shield + weapon, same node) with stagger and riposte on success, full damage and self-stagger on failure** (1710–1797).
- **Conditions: bleed triggers three unblockable damage on the second token; poison one damage per token, remove one; frostbite blocks stamina recovery; stagger −1 to attack/block/resist/dodge; Calamity lasts the encounter; Corrosion −1 block until damaged** (1600–1658).
- **Enemy scaling table: +1 health per extra character, movement 1→2 at two, +1 attack at three, Repeat 2 at four; bosses never scale** (1519–1584).
- **Terrain: gravestones grant a scry on clearing (treasure, event, encounter or boss behaviour); barrels broken by dodge or push; chests hold one pre-placed card; traps are shuffled face-down onto basic nodes and persist through resets** (929–981).
- **Boss behaviour deck renewed by flipping the discard without shuffling** (2159); **weak-arc black die; same-arc rule for movement and pushes; dodge ignores arcs** (2137–2151).
- **Mimics: deferred recovery until the chest decision; mimic kill yields two treasures; fought-but-unkilled mimic must be fought again** (2043–2047).
- **Crystal lizards: immediate titanite on kill; no respawn once one has died; health unscaled** (2055–2057).
- **Mega-boss as optional final act after a single Level 4 encounter** (1173–1195) — the permadeath clause is flagged for decision (A-050) but the structure is kept.
- **Solo character starts with six souls** (1003). **Threat** is the manuscript's single term for the dashboard's "Taunt" and the enemy's threat value (A-125).
- **Campaign fog gate is aesthetic only** (2229).

## 6. Rules referenced but never described

| Term / object | Where referenced | Status | Row |
|---|---|---|---|
| Event cards (Level 1–3), Special Trap cards | 659–667, 939, 1133, 1161, 1181, 1269 | No definition anywhere; no official 1E source | A-090, A-091 |
| "lost" (character) | 1890, 1906, 2235 | Undefined | A-001 |
| "mastering" an encounter | 1397 | Undefined; only cleared/failed exist | A-112 |
| Reduced soul reward | 1327, 1391, 2245 | No value in either table | A-053 |
| First player token / First turn token | 1277, 3056 | Not a component; no function | A-017 |
| Left / right weapon slot | 1772, 1790, 1822 | Slots never named in Equipment Slots | A-068 |
| Shield, item (shop categories) | 811, 1069 | Never defined | A-069 |
| Enemy attack target icons, node attack, out-of-range miss | 1706 ("detailed later") | Never detailed | A-023 |
| Leap icon | 2175 | Used, not defined | A-038 |
| Multiple-boss encounter (Ornstein & Smough); Gargoyle ×2 | 509–511, 2366–2368, 2398 | No rule | A-039, A-040 |
| Mega-boss "Items" | 1183 | Undefined | A-093 |
| Mega-boss special rules ("mega-boss rule booklet") | 1195 | External reference; only Asylum/Stray covered | A-115 |
| Strafe attack (Kalameet), track deck / Death Race (Chariot) | implied by 1640 and the campaign lists | Not described | A-115 |
| Level 4 encounter tile / board in campaign sections | 2642, 2712–2714, 2932, 2940–2942 | No layout rule | A-094 |
| Pillar tokens and pillar nodes | 2205–2209 | Not in components or node types | A-114 |
| Trap token contents and resolution | 967–981, 3064 | Never stated | A-083, A-033 |
| "basic (yellow) nodes" | 971 | Colour never introduced | A-084 |
| Phantom data card values (threat, defence, special ability, Distract) | 1971–1993 | Omitted | A-016 |
| Ambush cards; invader tokens (as components) | 1137, 2007, 2045 | Not in component list | A-092 |
| Estus Flask rule | 751, 1830 (footer only) | Body text missing | A-012 |
| Health tracker dial / "heal dial" | 2019, 2099 | Named inconsistently; defined by use | A-098 (typo) |
| Wound tokens vs damage tokens vs damage cubes | 681, 1285, 1850 | Three names for two components | A-113 |
| Ready side / used side | 793 ("read and a used side") | Defined with a typo | — (style pass) |
| "Threat" of characters (dashboard prints "Taunt") | 745 | Needs glossary bridge | A-125 |
| The Last Giant (mega-boss) | 3018 | Not in components or requirements | A-108 |
| Glossary | 381 (promised) | Absent (intake finding) | — |

## 7. Files

- `/home/user/DSTBG2E/work/audit/A_rows.csv` — 125 rows, header exactly as specified, QUOTE_ALL.
- `/home/user/DSTBG2E/work/audit/A_report.md` — this report.
