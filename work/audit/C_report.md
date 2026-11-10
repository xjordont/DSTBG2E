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
