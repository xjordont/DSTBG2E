# Audit C — Style & Consistency Report

Project: Dark Souls: The Board Game — Second Edition (homebrew). Manuscript: `work/docx/manuscript.md` (pandoc GFM conversion of `DarkSoulsTBG2E.docx`). Lines 1–360 are a stale TOC; the body runs from line 361 to 3366. All line references below cite the body. Companion files: `C_rows.csv` (124 rows, C-001…C-124) and `C_glossary_candidates.md` (118 headwords).

Target voice: lawbook clarity — strict conditional syntax ("When [trigger], [subject] must/may [action]."), terse, British English, no hedge words, no second person outside worked examples, every keyword italicised consistently and defined once in a glossary.

## 1. Method

1. Read the whole body (lines 361–3366) once in sequence.
2. Mechanical sweeps with `grep -n -i -E` over the body for: Americanisms and -ize forms; the known misspelling list; every hedge word (should / might / could / reasonably / probably / perhaps / maybe / likely, plus "reasonable"); every italic span (`\*[^*]+\*`); every heading (`^#`); cross-reference phrases (later / previously / earlier / aforementioned / as above / section titled / refer to / see the / rule booklet / as usual / as before); example markers (example / e.g. / i.e. / such as); punctuation defects (double stops, `2X`, `=\>`, `-\>`, `\[`, `&amp;`, stray `i`, `&` in headings, `etc.`, ligature code points U+FB00–FB06, straight vs curly quotes, lower-case sentence starts); numerals vs number words; serial-comma patterns.
3. Two Python counters (run with `-I`): (a) 190 variant patterns for the terminology pairs in Task 4, each returning total count and line list; (b) italic-vs-plain counts for 150 candidate glossary terms over the rules text (lines 361–3100, excluding the Community Update Pack skeleton).
4. Official spellings verified against the pdftotext extracts in `work/text/` (Core 2017, Tomb of Giants V2, Phantoms, Explorers, Darkroot, Iron Keep booklets).
5. Every table in the manuscript was re-added by hand and compared with its governing prose; every worked example was recomputed against the rule it illustrates.
6. Severity: Blocker = a rule cannot be applied; Major = a terminology or structure defect that changes meaning or sends the reader to the wrong rule; Minor = cosmetic or mechanical; Note = verified clean, recorded for the style sheet.

## 2. Counts

| Sweep | Result |
|---|---|
| Americanisms (armor, behavior, center, color, favor, defense, gray, catalog, plow, jewelry, fulfill, traveled, canceled, labeled, modeled, maneuver, -ize/-ization) | **0** hits. The body already uses armour, behaviour, centre, colour, defence, grey, plough, finalised, summarised, randomised, memorising. |
| Known misspellings | publically ×1, Titanate ×1, Andor Londo ×3, Earthern ×1, Jeramiah ×1 (Jeremiah ×2 elsewhere), HungryVoracious ×1 |
| Name variants against official booklets | Skeletal/Skeleton Beast, Sunless Realm/Realms, Old Dragon Slayer/Dragonslayer, Grey Wolf Sif/Great Grey Wolf Sif, Sword Master Sabre (official: "Sword Master"), Armourer Dennis / Marvellous Chester / Plough Scarecrow (cards print US spellings) |
| Hedge words | should ×34, might ×4, could ×4, reasonably ×1, likely ×1 = **44**; plus "reasonable" ×1 (L2197) = 45 rewrites below |
| Second person "you" | 1 (L377, front matter); 0 in rules text |
| Italic spans (raw, body) | 601 spans, ~45 distinct terms; 13 spans with punctuation inside, 6 split-word spans, 8 non-term fragments |
| Keywords never italicised | ≈ 40 (endurance bar, node, tier, heat-up, weak arc, scry, push, wound token, damage cube, behaviour deck, data card, fog gate, bonfire ascetic, transposition, legendary, catalyst, two-handed, AoE, range, riposte, lost, model, PvP …) |
| Glossary headwords proposed | 118 (6 where the manuscript is silent or self-contradictory) |
| Terminology variant groups | 33 (Task 4 table) |
| Table-vs-text mismatches | 9 real mismatches, 3 verified consistent |
| Cross-references | 33 resolved; 2 broken (fog gate "as before"; external mega-boss booklet); 2 inexact targets; 3 forward references phrased as "as usual/as before" |
| Worked examples | 12 checked; 1 arithmetic error (L1113 "two by six" grid), 11 verified |
| Empty headings | 20; duplicate "Spells" H2/H3; 4 headings with trailing punctuation; 2 duplicate campaigns; 8 duplicate heading titles across chapters |
| CSV rows | 124: Blocker 1, Major 30, Minor 81, Note 12; REQUIRED 74, CLEAN-UP 47, OPTIONAL 3; Decision needed 26 |

## 3. Task 1 — British-English and spelling sweep

The manuscript is already British-spelled; no Americanism needs changing. Fixes required (all in `C_rows.csv` C-001…C-017):

| Line | Current | Fix | Authority |
|---|---|---|---|
| 377 | publically | publicly | dictionary |
| 853 | Titanate | Titanite | card family; L497, L1943, L2055 |
| 2384, 2486, 2646 | Andor Londo | Anor Londo | Core/TG rulebooks ("Anor Londo" ×5) |
| 2736 | Lower Earthern Peak | Lower Earthen Peak | Explorers booklet body text; game canon |
| 557 | Xanthous King Jeramiah | Xanthous King Jeremiah | Phantoms booklet ×3; manuscript L2492, L2528 |
| 443 | 1x HungryVoracious Mimic | 1x Mimic (Hungry Mimic and Voracious Mimic data cards) | Explorers booklet |
| 469 | Skeletal Beast | Skeleton Beast | ToG rulebook ×3; manuscript L3354 |
| 593 | Sirris of the Sunless Realm | Sirris of the Sunless Realms | Phantoms booklet |
| 2734 | Old Dragon Slayer | Old Dragonslayer | Explorers booklet ×11; manuscript L495, L2838 |
| 1141 | Grey Wolf Sif | Great Grey Wolf Sif | component list L515; Darkroot booklet |
| 583 | Sword Master Sabre | Sword Master | Phantoms booklet names him "Sword Master" only — **decision** |
| 561, 569, 457 | Armourer Dennis, Marvellous Chester, Plough Scarecrow | Armorer Dennis, Marvelous Chester, Plow Scarecrow (as printed) — or keep British forms with a style-sheet note | cards print US spellings — **decision** |
| 445 | 3x Ironclad Soldiers | 3x Ironclad Soldier | list convention |
| 1201 | intimate victor | ultimate victor | wrong word |
| 793, 849, 887, 979, 1517, 1664, 1880, 2017, 2021, 2043, 2045, 2053, 2456, 2504, 3082 | read/used side; play mail; up grade; characters' catalyst; tiles entry; enemies block; wound token's; who's; its'; decks deck size; blocked by train; The then; one an; min-boss; character's powerful; Do no place; an the attacker | ready side; plate mail; upgrade; character's; tile's entry nodes; enemy's; wound tokens; whose; its; starting deck size; terrain; They then; the; mini-boss; characters; Do not place; the attacker's | typos (C-015) |

Credits (L3: Jyace, Santuric, etc.) stay as written.

## 4. Task 2 — Hedge-word rewrite list (all 45 occurrences)

Decision key: **must** = mandatory rule; **may** = permission/optional rule; **state** = rewrite as present-indicative fact; **cut** = delete (advice, flavour or front matter). Front-matter items (L373–L379) are recommended for a Foreword outside the rules; rewrites are given in case the text is retained.

| # | Line | Word | Current sentence | Rewrite (lawbook voice) | Decision |
|---|---|---|---|---|---|
| 1 | 373 | likely | Unfortunately, likely due to the Kickstarter sales model, the game shipped in many small expansions leaving the overall rules fragmented. | The game shipped in many small expansions, leaving the rules fragmented. | cut (front matter) |
| 2 | 375 | could | …a professional quality rulebook that new players could use to learn the second edition of the game without requiring referencing other texts. | …a rulebook from which new players can learn the game without reference to other texts. | cut (front matter) |
| 3 | 377 | should | As such, it should be considered a work in progress. | These rules are a work in progress. | cut (front matter) |
| 4 | 377 | could | …review these rules for any sort of improvement that could be made. | …review these rules and propose improvements. | cut (front matter) |
| 5 | 379 | should | But I have yet to decide if I should just rip the old ones from the original rule book or generate my own. | (editorial note — delete) | cut |
| 6 | 765 | should | Once the encounter has started players should not interact with their character's inventory cards. | During an encounter, a character may not access their inventory. | must (prohibition) |
| 7 | 793 | should | The *ember* tokens are treated differently, and should be placed in the condition token supply at the start of the game.. | At the start of the game, place the *ember* tokens in the token supply, not on the dashboard. | must |
| 8 | 805 | should | Finally, players should be aware that *ember* tokens enable the character to summon phantoms, but also attract malicious invaders. | An *embered* character may summon a phantom and provokes an invader (see §Phantoms). | state |
| 9 | 845 | should | Players should include all equipment cards from expansions available in their games to increase variety. | Players may include equipment cards from every expansion they own. (Duplicate of L1057 — keep one.) | may |
| 10 | 849 | could | For example, a character could attach up to two weapon upgrade cards to a weapon card with an upgrade limit of two. | Example: a character may attach up to two weapon upgrade cards to a weapon with an upgrade limit of two. | may |
| 11 | 963 | should | If they cannot decide, the treasure should be awarded to a randomly selected character. | If the players cannot agree, the treasure is awarded to the character holding the *aggro* token (see §Treasure Rewards). | state — align with L1461 (decision C-089) |
| 12 | 979 | should | Players should fill the basic nodes furthest from the tiles entry with trap tokens first. | Place trap tokens on the basic nodes furthest from the tile's entry nodes first. | must |
| 13 | 1017 | might | …a tiny white emblem in the top right icon to suggest which class might benefit most from its use. | The emblem indicates the class for which the card is designed; it has no rules effect. | state |
| 14 | 1021 | might | They also feature a tiny white class emblem to suggest which class of character might benefit most from its use. | The class emblem has no rules effect. | state |
| 15 | 1057 | should | Players should include all treasure cards from expansion sets in their appropriate type of treasure deck as above. | Add treasure cards from every available expansion to the treasure deck of their type (see §Treasure Deck Setup). | must (if expansions are in play) — decision C-018 |
| 16 | 1131 | should | Encounter levels should increase from the tile adjacent to The Bonfire tile towards the mini-boss tile. | Encounter levels must increase from the tile adjacent to the *bonfire* tile towards the mini-boss tile. | must |
| 17 | 1141 | should | By default, players should include only the encounter cards from the same set as the boss they will face next. | By default, build each encounter deck only from encounter cards of the same set as the next boss. | must (default) |
| 18 | 1159 | should | Encounter levels should increase from the tile adjacent to the *bonfire* tile towards the main-boss tile. | Encounter levels must increase from the tile adjacent to the *bonfire* tile towards the main-boss tile. | must |
| 19 | 1201 | should | Players should agree on whether they will include a mega-boss and/or PvP encounter during set-up. | During setup, the players must decide whether the game includes a mega-boss and whether it includes a PvP encounter. | must |
| 20 | 1263 | could | For example, if the first three encounters are marked *cleared* then the characters could skip to the fourth encounter but would all start with 6 stamina expended. | Example: the first three encounters are *cleared*. The characters may skip to the fourth encounter; each character begins it with six stamina cubes on their endurance bar. | may |
| 21 | 1461 | should | Players decide which character should receive this treasure. | The players decide which character receives the treasure. | state |
| 22 | 1479 | should | Players decide which character should receive the treasure. | The players decide which character receives the treasure. | state |
| 23 | 1596 | should | Players should take note that only enemy behaviours that deal damage can be dodged. | Only enemy behaviours with an attack value may be dodged. | state |
| 24 | 1664 | should | …then the players decide which model should go first. | …the players decide which model takes its turn first. | state |
| 25 | 1666 | reasonably | If there is no valid target or the enemy behaviour otherwise cannot be reasonably executed, that enemy behaviour is skipped… | If an enemy behaviour has no valid target or cannot be executed, skip that icon and resolve the next icon to the right. | cut word |
| 26 | 1880 | should | …the character should mark the equipped item with a red damage cube to indicate that it is scaled. | …mark the equipped card with a red damage cube to show that it is *scaled*. | must |
| 27 | 1963 | should | At this point characters should move their models to the closest encounter tile to the bonfire tile. | The characters then move their models to the encounter tile adjacent to the *bonfire* tile. | must |
| 28 | 2041 | should | Groups with new players should default to leaving mimics out as they can be quite punishing. | (delete) Mimics are an optional rule. | cut |
| 29 | 2041 | should | Experienced players should include mimics to ensure they are challenged. | (delete) The players decide during setup whether to use mimics. | cut |
| 30 | 2053 | should | Players should include crystal lizards as an optional game component if they own the Iron Keep expansion set. | Crystal lizards are an optional component of the Iron Keep expansion; the players decide during setup whether to use them. | may |
| 31 | 2065 | should | The first time a character passes through the fog gate the fog gate tile should be removed from the boss-tile entryway and placed on the *bonfire* tile to serve as a shortcut. | When a character first passes through the fog gate, move the fog gate token from the boss tile's entry node to the *bonfire* tile. | must |
| 32 | 2069 | should | Only with adequate preparation, astute tactics, and the favour of luck should the characters hope to fell a boss. | (delete — flavour) | cut |
| 33 | 2069 | should | …optional objectives which players can attempt after defeating a main-boss should they want a more epic final battle. | Mega-bosses are optional final bosses fought after the main-boss (see §Setup After the Main-Boss). | state |
| 34 | 2169 | should | The target character model should remain static while the boss model rotates underneath to change facing towards the target. | The target character model does not move while the boss rotates beneath it. | state |
| 35 | 2197 | reasonable | This is often a reasonable time to end a game session if time is limited. | (delete, or sidebar: "A boss's defeat is a natural session break.") | cut |
| 36 | 2223 | might | Players might expect to meet over multiple play sessions to complete a campaign. | A campaign is designed to be played over several sessions. | state (or cut) |
| 37 | 2223 | might | A single section of a campaign might serve as a convenient amount of content to cover in a session. | One section is a convenient session. | state (or cut) |
| 38 | 2596 | should | This campaign requires the core set and Asylum Demon expansion but players should add the Explorers and characters expansions if available. | Requires: Core set, Asylum Demon. Recommended: Explorers, Characters. | may (labelled) |
| 39 | 2664 | should | …but players should add the Explorers and Characters expansions if available. | Requires: Core set, Darkroot Basin, The Four Kings. Recommended: Explorers, Characters. | may |
| 40 | 2720 | should | …but players should add the Explorers and characters expansions if available. | Requires: Core set, Explorers. Recommended: Characters. (requirement line is wrong — C-079) | may |
| 41 | 2766 | should | …but players should add the Explorers and Characters expansions if available. | Requires: Core set, Darkroot Basin. Recommended: Explorers, Characters. | may |
| 42 | 2812 | should | Players should add the Explorers and Characters expansions if available. | Requires: Core set, Darkroot Basin, Vordt of the Boreal Valley, Executioner's Chariot, Explorers. Recommended: Characters. | may |
| 43 | 2884 | should | Players should add the Darkroot, Explorers, and Characters expansions if available. | Requires: Core set, Gaping Dragon, Darkroot Basin. Recommended: Explorers, Characters. | may |
| 44 | 2948 | should | Players should add the Explorers and Characters expansions if available. | Requires: Core set, Iron Keep. Recommended: Explorers, Characters. | may |
| 45 | 2994 | should | Players should add the Explorers and Characters expansions if available. | Requires: Core set, Manus, Asylum Demon, The Last Giant. Recommended: Explorers, Characters. | may |

Tally: 34 should (10 → must, 8 → may/labelled, 9 → state, 7 → cut), 4 could, 4 might, 1 reasonably, 1 likely, 1 reasonable. No "probably", "perhaps" or "maybe" in the manuscript.

## 5. Task 3 — Keyword / italics audit (summary; full table in `C_glossary_candidates.md`)

Raw extraction: 601 italic spans in the body, ~45 distinct terms. The most-used keywords are italicised inconsistently (italic / plain counts in rules text L361–3100):

| Term | Italic | Plain | Term | Italic | Plain |
|---|---|---|---|---|---|
| bonfire | 39 | 79 | threat | 10 | 14 |
| soul | 35 | 33 | stamina | 8 | 34 |
| dodge | 27 | 17 | walk | 8 | 0 |
| cleared | 27 | 5 | shift | 8 | 1 |
| spark | 25 | 16 | parry | 7 | 0 |
| ember | 23 | 10 | push | 2 | 49 |
| hollow | 19 | 8 | heat-up | 2 | 15 |
| block | 17 | 8 | endurance bar | 1 | 16 |
| resist | 15 | 6 | aggro token | 3 | 18 |
| aggro | 14 | 10 | behaviour card | 2 | 28 |
| luck | 12 | 4 | node | 8 | 151 |
| heroic action | 11 | 5 | model | 5 | 140 |
| attack option | 10 | 5 | mini-boss | 0 | 53 |

Malformed italics (C-027…C-029):
- Punctuation inside the span: L793 `*heroic actions, luck, and estus flask.*`; L1369 `*failed:*`; L1445 `*cleared.*`; L1776 `*Push, area-of-effect,*`; L1840 `*dodge,*`, `*walk, run,*`; L1890, L1906 `*hollow.*`; L1963 `*failed),*`; L2043 `*spark.*`; L2047 `*cleared.*.`; L2099 `*threat, block,*`; L2185 `*, resist,*`; L2195 `*embered.*`.
- Split words: L787 `stagger*ed*` ×2; L1341 `*C*haracters`; L1794 `block*/*resist`; L1880 `attack option*s*`; L2145 `dodge*s*`; L3082 `attack option*'s*`.
- Fragments / non-terms: L705 `*4x Corrosion*`; L1529 `*repeat to*`; L1890 `*spark to*`; L1345 `*clear an*`; L3056 `*First* *turn*`; headings L1640 `*Calamity (*Kalameet Expansion*)*` and L1650 `*Corrosion (*Gaping Dragon Expansion*)*`; bold `**AND**`/`**OR**` connectors L1808–1832. (The regex also returns `*8*`, `*4*`, `*|*` etc.; these are bold table cells, not defects.)

Definitions missing or contradictory (C-033, C-034): *lost* (L1399, 1890, 1906, 2235 — partial definition at 1906 conflicts with L1223 and L1195); "mastering" (L1397); *first player* token (L1277, never used; "First turn token" at L3056); boss *leaps* (L2175); invader "Heat Up value" (L2017); "health" used for characters (L1830). The glossary promised at L381 does not exist.

Recommended italics policy (see Style Sheet §14): italicise a glossary keyword at its first use in each H2 section, in its own definition, and in headings and table labels; plain thereafter. Never italicise inflections separately, punctuation, quantities or connectors. 118 headwords are proposed in `C_glossary_candidates.md`.

## 6. Task 4 — Canonical terminology table

| # | Variants found (count; evidence lines) | Canonical | Rule / note | Row |
|---|---|---|---|---|
| 1 | stamina bar (2; 775, 1215) · endurance tracker (1; 1205) · endurance bar (14; 741–789, 1261, 1367) | **endurance bar** | Tracks both stamina and damage; official term. | C-035 |
| 2 | damage tokens (4; 1285, 1291, 1293, 1850) · wound tokens (5; 681, 1517, 1664, 2099) · damage cubes (16; 685, 775–789, 999, 1205, 1229, 1347, 1726, 1880) | **wound token** (enemies) / **damage cube** (characters) | Confirmed: enemies take wound tokens on the base (L1517); characters add red damage cubes (L779). "Damage token" is neither — change all four. | C-036 |
| 3 | heal dial (1; 2019) · health tracker dial (1; 2099) · health dial (4; 1105, 1993, 2035, 2195) | **health dial** | | C-037 |
| 4 | main action (2; 837, 851) · major action (2; 1820, 1838) | **major action** | "Main action" never defined; turn structure defines minor/major. | C-038 |
| 5 | minor action (4; 797, 1804, 1838) | **minor action** | consistent | — |
| 6 | activation (4; 1606, 1618, 1860, 2191) · turn (65) | **turn** | | C-039 |
| 7 | Encounters expansion (1; 2041) · Explorers (15) | **Explorers** | | C-040 |
| 8 | mini-boss 47 · Mini-Boss 15 · Mini Boss 5 · mini boss 1 · mini bosses 1; main-boss 31 · Main-Boss 1 · Main Boss 11; mega-boss 28 · Mega-boss 2 · Mega Boss 7 · mega boss 1 (campaign lists 2366–3034; 2996) | **mini-boss / main-boss / mega-boss** (lower-case, hyphenated); Title Case only in headings | | C-041 |
| 9 | The Bonfire (10; 771, 849, 1131, 1171, 1179, 1886, 1892, 2195, 2295) · *bonfire* (35) · the bonfire (27) · Bonfire Tile (48, campaign lists) | **the *bonfire*** ; component = **bonfire tile** | Headings may read "The Bonfire". | C-042 |
| 10 | Andre's Shop (9) · the shop (3; 2312, 2314, 2340) · Blacksmith Andre (7) · Andre (11) | **Blacksmith Andre** (first mention per section) → **Andre**; **Andre's shop** / **the shop** | Lower-case "shop" recommended (decision). | C-043 |
| 11 | Firekeeper (8) | **Firekeeper** | consistent; matches official. | C-044 |
| 12 | tier one/two (60, prose) · Tier One/Two (10, tables/headings) · Tier one/two mid-sentence (3; 1451, 2314, 2316) · stat sense unqualified (771 "tier two", 1914) | **tier one / tier two** (treasure); **stat tier one…four** (stats); Title Case only in headings/table labels | Two senses of "tier" must always be distinguishable. | C-045 |
| 13 | Level 1–4 (194) · level one, two, and three (1; 1121) | **Level 1 / 2 / 3 / 4** | Printed card label. | C-046 |
| 14 | *dodge* 22 · dodge 16 · Dodge 2 (2115, 3082) · *Dodge* 3 (831, 1501, 1734) | ***dodge*** | | C-047 |
| 15 | players (102) · characters (484) · models (140); misuse at 1393 "per player", 805, 891, 919, 2239 | **players** decide/agree/roll; **characters** act, own tokens and cards, gain souls, die; **models** occupy nodes, move, are pushed | One player may run two characters (L989, L1095), so "per player" ≠ "per character". | C-048 |
| 16 | miniature (2; 387, 411) · model (140) | **model** | | C-049 |
| 17 | hollow markers (1; 781) · hollow tokens (2; 805, 1379) · hollow cubes (3; 1231, 1898, 3074) · white cubes (781, 1215, 1367) — also stat cubes (771, 993, 1914) | **hollow cube** | Component not in the list; "white cube" ambiguous with stat cubes. | C-050 |
| 18 | ready side / used side (793–801) · face-up (10) · face up (3) · face-down (37) · face down (1) | tokens: **ready side / used side**; cards & tiles: **face up / face down** (predicate), **face-up / face-down** (attributive only) | | C-051 |
| 19 | sparks dial (1; 1093) · spark dial (4) | **spark dial** | | C-052 |
| 20 | exploration tiles (1; 2221) · encounter tile (47) | **encounter tile** | | C-053 |
| 21 | treasure card (40) · equipment card (24) · item(s) (1183, 1880, 1941) · bare "treasure" (68) · bare "equipment" (32) | **treasure card** (any card from a treasure deck) ⊃ **equipment card** (can be equipped); no bare "item" | Define the relation once. | C-054 |
| 22 | attack option (15) · weapon option (1; 1872) · attack action (2; 1856, 1876) · attack major action (1838) | **attack option** (card line); **attack** (the major action) | | C-055 |
| 23 | Titanite Chunk (1477) · Titanite Scale (2055) for the crystal-lizard reward | **Titanite Scale** | Iron Keep booklet; Chunk is a different (common) card in the Update Pack. | C-056 |
| 24 | heat-up 5 · Heat Up 11 · Heat-up 2 · heats-up 1 · Behaviour Deck (943) | **heat-up** (n./adj.), **heats up** (v.); **behaviour deck** | | C-057 |
| 25 | fog gate 11 · fog-gate 2 (1151, 1179) · Fog Gate 3 · "fog gate tile" (2065) vs "token" (719, 2229) | **fog gate**; component **fog gate token** | | C-058 |
| 26 | set-up 8 · setup 21 · set up 1 | noun **setup**, verb **set up** | | C-059 |
| 27 | reroll 8 · re-roll 2; back-up slot 2 · backup slot 1; PvP 10 · player versus player 1 · player-versus-player 1; rule set/ruleset/rule-set; rule book/rulebook/rule-book | **reroll**; **back-up slot**; "player versus player (PvP)" once, then **PvP**; **ruleset**; **rulebook** | | C-060 |
| 28 | killed (1517) · dies (1850) · defeated (1295, 1301) · slain (2053, 2195) for enemies; characters die (1223, 1305) | characters **die**; enemy models are **killed**; bosses and encounters are **defeated** / **cleared** | decision | C-061 |
| 29 | entrance node (1985) · entryway (2065) · entrance (1179) · entry node (903, 1265) | **entry node** | | C-063 |
| 30 | condition marker (787) · condition token (10) | **condition token** | | C-064 |
| 31 | phantom = umbrella (543, 3052, 805) and = summon only (1969–1993, 1971); chapter "SUMMONS" contains Invaders | ***phantom*** (umbrella) ⊃ ***summon*** (friendly) + ***invader*** (hostile); chapter **PHANTOMS** | | C-065 |
| 32 | "encounter card" for the card whose icons the phantom/invader resolves (1991, 2031) | **behaviour card** | wrong card named | C-066 |
| 33 | health (characters, 1830) vs damage cubes | characters have **damage** (cubes) and **stamina**; **health** is for enemies/bosses only | | C-034 |

Also confirmed consistent (no change): *souls* spelt the same throughout; Firekeeper; "Blacksmith Andre"; "dashboard"; "data card"; "behaviour card".

## 7. Task 5 — Table-vs-text consistency

| # | Table | Governing prose | Finding | Severity / row |
|---|---|---|---|---|
| 1 | Enemy Scaling table (L1533–1584): 2→Base+1, 3→Base+2, 4→Base+3 | L1523 "beyond one" (agrees); **L1517 "adding one health for each character (including dead characters) in play"** (two characters → Base+2) | Prose at L1517 contradicts bullet and table. | Major, C-068 |
| 2 | Enemy Scaling table: 4 characters "*Repeat* 2"; column "Enemy Damage +1" | L1529 "add *repeat to* each non-boss enemy's attack behaviour" (no value); L1527 "increase all non-boss attack values by one" | Bullet omits the repeat value; column header uses "Damage" where bullets say "attack value". | Major, C-069 |
| 3 | Soul Reward Table (L1401–1439): single column 3 / 4 / 5 / 6 | L1389 "full *soul* reward"; **L1391 "reduced *soul* reward"** for repeat clears | No reduced value exists anywhere; rule cannot be applied. | **Blocker**, C-070 |
| 4 | Campaign Soul Reward Table (L2247–2285): 2 / 3 / 4 / 5 | L2243 "reduced by one compared to the basic game" | Consistent (3/4/5/6 − 1). Header "per characteri" (L1412) vs "per character" (L2258): stray i. | Note, C-071 |
| 5 | Shop Price Table basic (L1951–1957): Tier One 2/1, Tier Two 4/1, Boss Treasure N/A/**6** | — | — | — |
| 6 | Shop Price Table campaign (L2326–2334): Boss Treasure −/**4**; Legendary Shop "4 + Boss Treasure"/4; Bonfire Ascetic 16/− | L2348 transposition = boss treasure + four souls (agrees); L2293/2316/2340 bonfire ascetic 16 (agrees); L2322 legendary "only available through transposition" (row is called a "Shop"); legendary sell value 4 never in prose; boss-treasure sell 6→4 unexplained | Boss-treasure sell value differs between modes with no stated rule; null marker N/A vs −; legendary row name and sell value unsupported. | Major, C-072 |
| 7 | Stat Tier Costs basic (L1918–1923): 2 / 4 / 8 / **8** | L1914 example "two souls … then four additional souls" (agrees for tiers one–two) | Tier Four repeats Tier Three; campaign table is 4/8/16/20 (doubling then +4). Probable error (expected 16). | Major, C-073 |
| 8 | Stat Tier Costs campaign (L2301–2306): 4 / 8 / 16 / 20 | L2297 "cost to level up stats … is increased in Campaign play" (agrees) | Consistent. | — |
| 9 | Weapon stat table (L3210–3330): 60 rows as plain text, header "**Weapon Name STR DEX INT FTH**" | L3208 explains INT/FTH removal; all 60 rows show INT 0, FTH 0 (agrees) | Needs a real 5-column table. | Minor, C-074 |
| 10 | Tokens list (L701–705): "35x Condition tokens" | itemised 7×4 + 4×2 = 36 | Sum mismatch. | Minor, C-075 |
| 11 | Treasure Cards (L597–629): total 534 | 13+45+40+120+60+145+10+20+18+63 = 534 | Verified. L621 "20 (Expansions)" lacks "x". | Note, C-080 |
| 12 | Encounter cards (L633–657): total 169 | 12+31+12+31+12+31+40 = 169 | Verified. | Note, C-080 |
| 13 | Campaign Play prose (L2223, L2225): "all three sections long"; "three campaigns which require only … the core set" | CAMPAIGNS chapter: 13 campaigns, 3–6 sections; 2 core-only | Prose contradicts chapter. | Major, C-076 |
| 14 | Mega-bosses component list (L523–541) | L3018 "The Last Giant (Mega Boss)"; L2994 requirements omit it | Boss used but not listed. | Major, C-077 |
| 15 | Campaign requirement lines vs section lists | A Hollow Pursuit (L2720) copies Demon Hunting's line; Undead Colosseum (L2812) omits Explorers; Into the Depths (L2884) lists Darkroot as optional though Artorias is a section boss | Requirements wrong or incomplete. | Major, C-078 |
| 16 | PvP dodge list (L3084–3094) as escaped brackets and ASCII arrows | L3082 | Should be a two-column table. | Minor, C-081 |

## 8. Task 6 — Cross-reference resolution

| Line | Reference text | Resolves to | Status |
|---|---|---|---|
| 757 | "of the appropriate equipment type as described" | the three paragraphs that follow (759–763) | OK — change to "as described below" |
| 837 | "explained in detail later on in the section title 'Character Attacks'" | ## Character Attacks (L1844) | OK — typo "title" → "titled"; convert to §-ref |
| 839 | "explained in detail later on in the section titled 'Enemy Attacks'" | ## Enemy Attacks (L1704) | OK |
| 841 | "upgrade cards at Blacksmith Andre which is described later in more detail" | ## Upgrades (L847) and ## Blacksmith Andre (L1927) | OK — two targets; cite both |
| 891 | "with the aforementioned effects" | ### *Ember* (L803) | OK (backward) |
| 1057 | "as above" | ## Treasure Deck Setup (L1005–1053) | OK |
| 1151 | "Place the fog-gate as before." | **no earlier step places the fog gate** (Encounter tiles L1111–1117 silent); only L1179 and L2063–2065 | **BROKEN** — add a placement step to Encounter tiles (C-082) |
| 1165 | "stocked as previously described" | ### After Boss is Defeated (L1075–1089) | OK |
| 1169, 1187 | "visit the Firekeeper and Andre's Shop as usual after resting" | ## Resting at The Bonfire (L1892) — **forward** | Inexact — "as usual" precedes the rule; use §-ref (C-087) |
| 1171 | "Resume encounters in the same way as before" | ### Encounter Start (L1257) — **forward** | Inexact (C-087) |
| 1195 | "special rules described in the mega-boss rule booklet" | **external document**; # BOSS SPECIAL RULES (L2199) covers Asylum/Stray Demon only | **BROKEN / external** (C-083) |
| 1261 | "previously *cleared* encounters" | ### Encounter Resolution (L1301) | OK |
| 1273 | "Draw from the tier one treasure deck before the mini-boss is defeated and tier two thereafter" | duplicates L1451 | OK — keep one |
| 1475 | "See the detailed rules on mimics later in these rules" | # MIMICS (L2039) | OK |
| 1485 | "per the optional rules detailed later" | # PLAYER VS PLAYER (L3038) | OK |
| 1600 | "listed below" | ### Bleed … Corrosion (L1602–1658) | OK |
| 1706 | "special rules detailed later" | ## Pushing (L1586, **earlier**), ## Conditions (L1598, **earlier**), ## Boss Attacks (L2181) | Wrong direction for two of three (C-085) |
| 1708 | "listed below" | ### Block & Resist / Dodge / Parry (L1710–1796) | OK |
| 1760 | "as above" | ### Block & Resist step 5 (L1724–1728) | OK |
| 1852 | "explained above … explained previously … the following weapon icons" | L1848; ## Conditions (L1598); L1854–1872 | OK |
| 1963 | "(*cleared* or *failed*)" | ### Encounter Resolution (L1297) | OK |
| 2045 | "per normal treasure chest rules" | ## Treasure Rewards (L1453–1461) / ### Chests (L963) | OK (two statements — see C-089) |
| 2047 | "Refer to 'Boss Encounter' rules for more details on how to manage the mimic's behaviour cards" | ## Boss Behaviour Cards (L2107) and ## Boss Turn Overview (L2155); no heading "Boss Encounter" | Inexact title (C-084) |
| 2069 | "as described previously" | # COMBAT BASICS / # ENEMY TURN | OK |
| 2077 | "information about boss behaviour cards will follow" | ## Boss Behaviour Cards (L2107) | OK |
| 2099 | "previously described enemy data cards" | ## Enemy Data Cards (L1489) | OK |
| 2105 | "as detailed during the setup chapter" | ### Encounter cards (L1119–1131) | OK |
| 2135 | "the following rules" | L2137–2145 | OK |
| 2163 | "previously described" | ## Enemy Movement / ## Enemy Attacks (L1668–1796) | OK |
| 2195 | "as previously described" | ## Treasure Rewards (L1479); ## Souls (L1383) | OK |
| 2197 | "post-boss setup rules as described earlier" | ## Setup After the mini-boss / main-boss (L1143, L1173) | OK |
| 2289, 2297, 2312 | "as in the basic rules" / "unchanged from the basic rules" / "Use the basic rules for Andre's Shop" | ## Treasure Rewards, # RETURNING TO THE BONFIRE, ### Shop Rules | OK |
| 2235 | "as in the rules for the basic game" | ## Sparks (L1245) | OK |

Rule statements that exist in two places with different content (treated as cross-reference defects): terrain movement verbs (§Terrain L931–959 vs §Character Movement L1840 — C-088); contested-treasure tie-break (L963 random vs L1461/1479 aggro — C-089); hollow death consequences (L1223 forced rest vs L1906 "lost … removed from play" vs L1195 permanent — C-090); mimic procedure duplicated in §Treasure Rewards and §Mimics (consistent — C-091).

## 9. Task 7 — Example verification

| Line | Example | Rule it illustrates | Check | Result |
|---|---|---|---|---|
| 1113 | "arrange them so they are connected in a two by six tile grid" (4 encounter tiles + bonfire + mini-boss) | L1115 "linear route along four sequential encounter tiles between *bonfire* and *boss* tiles" | 4 + 1 + 1 = 6 tiles = 2 × 3 | **ERROR** — "two by three" (C-092) |
| 1263 | skip 3 cleared encounters → "6 stamina expended" | L1261 two stamina cubes per skipped encounter per character | 3 × 2 = 6 | OK (voice/numeral fix only) |
| 849 | upgrade limit two → "up to two weapon upgrade cards" | L849 upgrade slots limit | OK | OK |
| 771 | base → tier two: pay tier one then tier two | L771 sequential payment | OK | OK |
| 1914 | STR base → tier two: 2 souls then 4 | Stat Tier Costs basic 2 / 4 | OK (campaign would be 4 / 8 — add note) | OK |
| 1141 | Gargoyle (core) then Darkroot Basin encounters for Sif | component sets L491, L515 | OK; name "Grey Wolf Sif" | OK (C-012) |
| 921 | "one boss and three characters" on a node | L919 three-model limit; L921 boss does not count | OK | OK |
| 1742 | two extra stamina (total three) for one extra dodge die, max four dice | L1736 one stamina to dodge | 1 + 2 = 3 | OK |
| 853 / 1943 | "(i.e., Titanite Shard)" / "(i.e.: Titanite Shards)" | Titanite upgrades fused to weapon | Shard is an example, not the whole class (Chunk, Slab exist at L3182–3184) | "e.g." / "for example" (C-098) |
| 1945 | "(i.e.: gems)" | non-Titanite upgrades returned on sale | gems are an example ("gems and relics", L853) | "e.g." (C-098) |
| 2141 | "(i.e.: *Run*) … (for example) to move to a side-arc" | moving between boss arcs | Run is one of several multi-node moves (also *shift*) | "e.g." (C-098) |
| 1872 | "such as from an agile sword or a repeating crossbow" | *repeat* icon | flavour, no arithmetic | OK (move to flavour) |
| 1840 | "terrain that would block movement such as a gravestone or chest" | §Terrain | consistent with L931/L959, but barrels and *shift* differ between sections | see C-088 |

## 10. Task 8 — Heading hygiene

**Empty headings (20) — delete:** L893, 983, 1059, 1441, 1842, 1882, 1910, 1925, 1959, 1965, 2049, 2059, 2215, 2308, 2324, 2336, 2400, 3036, 3096, 3100 (matches `00_intake_validation.md` §3.3).

**Duplicate / structural:**
- L855 `## Spells` followed by L857 `### Spells` → one H2.
- L2548 "Facing the Abyss - Dark Souls (Darkroot Basin)" and L2764 "Facing the Abyss - Dark Souls (Darkroot)": identical section lists, different preambles → delete one (decision on preamble).
- L2350 `# CAMPAIGNS` jumps to H3 campaign headings with no H2 → promote campaigns to H2.
- L1967 `# SUMMONS` contains `## Invaders` → rename chapter PHANTOMS.
- L1662 `## Overview` (Enemy Turn) → "Enemy Turn Overview".
- L3098 `# F.A.Q.` is an empty stub; L3102 `# COMMUNITY UPDATE PACK` uses bold paragraphs as sub-headings (L3104, 3176, 3206, 3332, 3358) → real H2s.

**Trailing punctuation / sentences as headings:** L1075 "After Boss is Defeated:"; L1802 "Recover one stamina."; L1804 "Minor Actions:"; L1820 "Major Action:" (the last three are turn-sequence steps followed by blockquoted actions joined by bold AND/OR, L1806–1834) → rewrite as a numbered procedure under "Character Turn Sequence".

**Case:** H1 = ALL CAPS throughout (consistent). H2 = Title Case except none. H3 = mixed: sentence case at L1111 "Encounter tiles", L1119 "Encounter cards", L1680 "Towards aggro", L1684 "Away from aggro", L1688 "Towards nearest", L1692 "Away from nearest", L1696 "Push-move", L1700 "Push-attack"; mixed at L1143/1173 "Setup After the mini-boss/main-boss"; L523 "Mega-bosses" vs L483 "Mini-Bosses", L501 "Main-Bosses"; L1015 "Class-specific Treasure". Policy: Title Case for H2/H3; keyword italics allowed in headings; hyphenated compounds capitalise both parts ("Mini-Boss", "Push-Move").

**Whitespace:** trailing spaces at L1041, 1091, 2454, 2502, 2548, 2594, 2662, 2718, 2764, 2810, 2882, 2946, 2992; double space after `#` at L361, L2217.

**Duplicate titles across chapters (need qualification for §-references):** Stat Tier Costs (1916, 2299); Shop Price Table (1951, 2326); The Fog Gate (2063, 2227); Sparks (1245, 2231); Encounter cards (633, 1119); Phantoms (543, 1969); Characters (385 H2, 725 H1); Setup (985 H1, 2219 H2).

**"&" in headings (9):** L679, 895, 1199, 1203, 1710, 1766, 2161, 2201, 2237 → "and".

**Campaign list formatting (C-108):** "Section Four- Haunting Warrior" (2854); "Section Five Dark Champion" (2864); "Gaping Dragon(Mega Boss)" (2944); trailing stops at 2692, 2794; "Bonfire Tiles" (2830); "set-up.." (2748); inconsistent terminal stops on invader lines (2478–2546 vs 2526–2532); Section Three of The Coiled Sword repeats "High Wall of Lothric" (2438); "Gargoyle (Mini-Boss)" listed twice in three campaigns (2366–2368, 2468–2470, 2616–2618) — confirm intentional (two Bell Gargoyles) and label "×2, fought together".

## 11. Task 9 — Punctuation and typography

| Class | Count (body) | Lines / examples | Policy |
|---|---|---|---|
| Double full stop | 4 | 793, 2221, 2748, 2047 (`*cleared.*.`) | single stop |
| Stray "i" | 2 | 1412 "per characteri", 1989 "deck.i" | delete |
| Quantity format | 4 | 447, 675 "2X"; 621 "20 (Expansions)"; 681 "6x1 , 3x3" | "Nx Name", lower-case x, no space before comma |
| `=\>` for ≥ | 4 | 1033, 1035, 1043, 1045 | prose: "25 or more"; tables: "≥ 25" |
| ASCII arrows | 3 + 6 | 1563–1577 `-&gt;`; 3084–3094 `-\>` | "→" in tables, or "becomes" in prose |
| Escaped brackets | 8 | 3084–3094, 3182, 3184 | tables / plain brackets |
| Ligature glyphs (U+FB00/01) | 4 | 921 "ﬁrst"; 925 "eﬀects", "inﬁnity", "aﬀect" | plain letters |
| Straight vs curly quotes | ’ ×146 vs ' in ~20 lines; “ ” ×3 pairs (837, 839, 2047); L529 mixes both in one line | 375, 529, 805, 835, 853, 1025, 1529, 1726, 1826, 1904, 1929, 1985, 2310, 2312, 2314 | straight in source, typesetter converts (or curly throughout — pick one) |
| "&" outside names | 9 headings + 449, 2398, 2500, 2660, 2934 | | "and"; "&" only inside an official product/card name |
| "etc." | 2 | 925 (rules), 377 (front matter) | never in rules; complete the statement |
| i.e. / e.g. | i.e. ×5 ("i.e.," ×2 correct at 771, 853; "i.e.:" ×3 misused at 1943, 1945, 2141); e.g. ×0 | | avoid both; write "for example" / "that is" |
| Lower-case sentence start "characters" | 6 | 919, 1931, 2069, 2157, 2185, 2207 | capitalise |
| Serial (Oxford) comma | 20 with / 0 without | — | always use it (already consistent) |
| Pandoc artefacts | 2 + 14 | `<!-- -->` at 875, 3154; blockquote `>` lines 1806–1834 | remove |
| Hyphenation | set-up/setup/set up; re-roll/reroll; back-up/backup; fog-gate/fog gate; face-up/face up; tile-by-tile; one-by-one | | see Style Sheet §8 |

**Numerals policy (recommended, decision C-120).** Words for zero to nine in running prose; numerals for 10 and above; numerals always in tables, with signs or symbols (+1, ≥ 25, 90°), beside dice icons, and in printed labels ("Level 1", "Range 0", "Tier 2 shop" if the card says so — the manuscript's "tier one/two" is retained because it is not a printed label). Counts in the body: one ×155, two ×79, four ×30, three ×27, six ×6, five ×5, ten ×3, sixteen ×1, eight ×1; digits in prose lines ≈ 15. Violations under the policy (by line, not exhaustive per instance): 1069/1079/1085 ("3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells" → words), 1263 ("6 stamina" → six), 1860 ("0 Stamina" → no stamina), 1914 ("5 greater" → five), 2340 ("sixteen souls" → 16 souls, to match 2293/2316); 925 "Range 0/1/2" and 2177/2179 "90/180 degrees" are compliant.

## 12. Task 10 — Voice and tense

Current form by chapter:

| Chapter | Current form | Target form |
|---|---|---|
| INTRODUCTION / SECOND EDITION NOTES (361–381) | first-person essay, reader address, "you" ×1 | Foreword outside the rules; "How to read this book" note |
| GAME COMPONENTS (383–723) | component bullet lists | bullets (lists) — keep; fix quantity format |
| CHARACTERS (725–805) | prose + numbered dashboard anatomy | short declarative paragraphs; anatomy stays numbered |
| EQUIPMENT (807–891) | prose; Spells (859–887) bullet fragments | prose; Spells → definition bullets of full sentences |
| TILES & NODES (895–981) | prose; Terrain (929–981) bullets | prose; terrain entries → definition bullets with one verb set |
| SETUP (985–1195) | numbered procedures (good); Treasure Deck Setup prose; Tier deck criteria numbered | numbered steps throughout; add the missing fog-gate step |
| GAMEPLAY (1197–1479) | Objective prose; Death/Embering/Sparks/Resolution/Recovery/Souls/Treasure Rewards as bullet fragments; Encounter Start/Turn Order numbered | rules → declarative paragraphs; Encounter Start/Recovery → numbered; Soul table |
| COMBAT BASICS (1481–1658) | prose; Scaling bullets + table; Conditions bullets | prose; scaling table only (one source); condition entries as definition bullets |
| ENEMY TURN (1660–1796) | prose; Block/Dodge/Parry numbered (good) | keep; cut filler |
| CHARACTER TURN (1798–1880) | headings-as-steps + blockquote AND/OR; prose | numbered turn sequence; prose for Movement/Attacks/icons |
| RETURNING TO THE BONFIRE (1884–1963) | flavour prose + bullets + tables; Resuming Exploration prose procedure | flavour to sidebar; Resting → numbered; Shop Rules → paragraphs; Resuming → numbered |
| SUMMONS (1967–2037) | numbered (good) with wrong card names | keep; fix L1991/2031 |
| MIMICS, CRYSTAL LIZARDS (2039–2057) | long prose paragraphs mixing option, flavour and procedure | optional-rule box; numbered procedure; one paragraph of rules |
| BOSS ENCOUNTERS / BOSS TURNS (2061–2197) | prose; anatomies numbered | prose; deck construction (2125) → numbered |
| BOSS SPECIAL RULES (2199–2213) | prose | prose; extend to all mega-bosses or cite expansion rules |
| CAMPAIGN PLAY (2217–2348) | prose + bullets + tables; Transposition "First … Fourth" prose | paragraphs; transposition → numbered; tables qualified "(Campaign)" |
| CAMPAIGNS (2350–3034) | nested bullets | keep as structured lists; "Requires / Recommended / Encounters" header per campaign |
| PLAYER VS PLAYER (3038–3094) | 27 bullet fragments | declarative paragraphs + dodge table |
| COMMUNITY UPDATE PACK (3102–3366) | lists; plain-text table | real tables; prose only at 3208 |

**Recommended form per content type (Style Sheet §10):** procedures = numbered steps, one action per step, imperative mood; definitions and component anatomies = bulleted full sentences; rules = short declarative paragraphs, each sentence of the form "When [trigger], [subject] must/may [action]."; options = boxed "Optional rule" with a fixed opening sentence; flavour = sidebars only.

**"Players should…" and other advisory sentences that must become rules or be cut** (all rewritten in §4 above): 765, 805, 845, 979, 1057, 1141, 1201, 1596, 2041 (×2), 2053, 2596, 2664, 2720, 2766, 2812, 2884, 2948, 2994. Related advisory/flavour that is not a rule: 1107 "if they wish … if they like"; 1109 "For added challenge"; 1141 "if they prefer more variety"; 1888 (Firekeeper/Andre description); 1890 "players must carefully weigh the timing"; 2069 "bloodlust … can expect to die often"; 2159 "Players can gain an advantage … by memorising"; 2197 session break; 1872, 1876, 2053 flavour adjectives.

**Tense:** present indicative for all rules. Future "will" at 1115, 1141, 1241, 1461, 1479, 2027, 2047, 2055, 2057 → present. Filler to delete: "simply" (979, 1674, 1676, 2191), "Of course" (1596), "and so-on" (2157), "one can assume" (2191), "it is possible" (2207), "nearly ready" (1963).
