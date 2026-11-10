# Audit F — Cross-Reference & Voice

**Manuscript:** `/home/user/DSTBG2E/work/docx/manuscript.md` (body from L361; lines cited as Lnnn).
**Companion file:** `/home/user/DSTBG2E/work/audit/F_rows.csv` (134 rows, F-001…F-134).
**Official texts consulted for the copied-prose check:** `work/text/DS-Core-Rules-lores.txt` (2017 Core), `work/text/DS-TG-Rulebook-Compressed_compressed.txt` (2022 V2), plus the expansion booklets in the same folder. Page numbers are PDF page indices split on form-feed, verified equal to the printed folios (Core p.10 → "10", V2 p.9 → "9").

## 1. Method

1. Read the whole body (L361–L3366) once end to end; classified every paragraph by register.
2. Targeted sweeps with `grep` over the body for: first person (`I`, `my`, `me`, `we`, `our`); second person (`you`, `your`); reader imperatives (`Remember`, `Note that`, `Please`, `See`, `Refer`); advisory/hedge vocabulary (`should`, `simply`, `typically`, `usually`, `often`, `essentially`, `largely`, `just`, `Of course`, `Thus`, `Therefore`); future tense (`will`, `would`, `could`, `might`); prose cross-references (`later`, `previously`, `earlier`, `above`, `below`, `aforementioned`, `as described`, `as usual`, `section title`, `see`, `refer`); external sources (`SFG`, `Steam Forged`, `Kickstarter`, `google`, `rule book`, `booklet`, `first edition`, `original`, `official`, `errata`, `video game`, `source material`, `basic game/rules`, `expansion set`).
3. Copied-prose detection: a Python script (`copycheck.py`, scratchpad) normalised ligatures/quotes, built 6-word shingles for every page of every official text, and reported each manuscript line whose longest matching run was ≥ 8 words or whose shingle-overlap fraction was ≥ 30 %. Hits were then read against the official page to classify them as verbatim / near-verbatim / paraphrase.
4. Flavour phrases ("safe haven", "polearms", "heart of", "Remember that", "Players should", "prepare to die"…) were located in the official texts to separate inherited official voice from the author's own.
5. Every finding was written to `F_rows.csv` (Python `csv`, `QUOTE_ALL`). Severity: **Blocker** = would break Class B (external rulebook citation, design commentary in a rules chapter, first person); **Major** = tone/advice/modal slip in rules text; **Minor** = cross-reference format and register inconsistencies; **Note** = copied-prose observations and items needing no change.

### Counts

| Category | Count | IDs |
|---|---|---|
| Meta-commentary passages (design/process/advice/editorial, incl. first person) | 15 passages in F-002…F-006, F-009…F-011, F-023, F-025, F-033, F-035…F-038, F-040, F-041, F-046…F-048 (rows: meta-commentary 12 + first-person 3) | see §2 |
| External-reference items (rulebook/product/source citations) | 10 rows (F-001, F-010, F-011, F-047, F-049…F-054) + 6 in the Second Edition Notes covered by F-002…F-005 | see §3 |
| Second-person / reader imperatives | 5 rows (F-007, F-026, F-032, F-055, F-056); `you` occurs only at L377 (×2) | see §4 |
| Prose cross-references | 28 rows (F-057…F-083 + F-066), 4 dangling/imprecise | see §6 |
| Copied-prose passages | 42 rows (F-093…F-134); 11 verbatim or ≥ 85 % | see §7 |
| Tone / register / modal / tense rows | 34 rows (F-008, F-012…F-022, F-024, F-027…F-031, F-034, F-039, F-042…F-045, F-084…F-092) | see §4 |
| **Total rows** | **134** (Blocker 9, Major 33, Minor 47, Note 45; Decision needed Y = 10, all OQ-01-dependent) | |

### Chapter map and provisional section numbering (used in all "(see §)" targets below)

The TOC (L7–L359) lists 24 chapters after itself. The body contains 23 of them (GLOSSARY is in the TOC at L355 but absent from the body). Numbering below assumes OQ-01 option A (Second Edition Notes replaced by an unnumbered Foreword) and the F.A.Q. cut.

| Body lines | Manuscript chapter | Provisional § | Sections |
|---|---|---|---|
| L361–369 | INTRODUCTION | §1 | — |
| L371–381 | SECOND EDITION NOTES | Foreword (unnumbered) | — |
| L383–723 | GAME COMPONENTS | §2 | 2.1 Characters … 2.8 Tokens & Terrain |
| L725–805 | CHARACTERS | §3 | 3.1 Dashboards, 3.2 Equipment Slots, 3.3 Stat Progression, 3.4 Endurance Bar, 3.5 Character Tokens |
| L807–891 | EQUIPMENT | §4 | 4.1 Equipment Cards, 4.2 Upgrades, 4.3 Spells, 4.4 Embers |
| L895–981 | TILES & NODES | §5 | 5.1 Basics, 5.2 Movement, 5.3 Node Limits, 5.4 Range, 5.5 Terrain |
| L985–1195 | SETUP | §6 | 6.1 Character, 6.2 Treasure Decks, 6.3 Shop, 6.4 Bonfire, 6.5 Encounter, 6.6 After the Mini-boss, 6.7 After the Main-boss |
| L1197–1479 | GAMEPLAY | §7 | 7.1 Objective, 7.2 Death & Hollowing, 7.3 Embering, 7.4 Sparks, 7.5 Encounters, 7.6 Souls, 7.7 Treasure Rewards |
| L1481–1658 | COMBAT BASICS | §8 | 8.1 Target vs Hit, 8.2 Enemy Data Cards, 8.3 Enemy Scaling, 8.4 Pushing, 8.5 Conditions |
| L1660–1796 | ENEMY TURN | §9 | 9.1 Overview, 9.2 Enemy Movement, 9.3 Enemy Attacks |
| L1798–1880 | CHARACTER TURN | §10 | 10.1 Turn Order, 10.2 Movement, 10.3 Attacks, 10.4 Two-Handed, 10.5 Stat Scaling |
| L1884–1963 | RETURNING TO THE BONFIRE | §11 | 11.1 The Bonfire, 11.2 Resting, 11.3 Firekeeper, 11.4 Blacksmith Andre, 11.5 Resuming Exploration |
| L1967–2037 | SUMMONS | §12 | 12.1 Phantoms, 12.2 Invaders |
| L2039–2047 | MIMICS | §13 | — |
| L2051–2057 | CRYSTAL LIZARDS | §14 | — |
| L2061–2151 | BOSS ENCOUNTERS | §15 | 15.1 Fog Gate, 15.2 Overview, 15.3 Tiles, 15.4 Data Cards, 15.5 Behaviour Cards, 15.6 Arcs & Defence |
| L2153–2197 | BOSS TURNS | §16 | 16.1 Overview, 16.2 Movement & Symbols, 16.3 Attacks, 16.4 Aggro, 16.5 Death |
| L2199–2213 | BOSS SPECIAL RULES | §17 | 17.1 Asylum Demon & Stray Demon (only) |
| L2217–2348 | CAMPAIGN PLAY | §18 | 18.1 Setup … 18.8 Transposition |
| L2350–3034 | CAMPAIGNS | §19 | one sub-section per campaign |
| L3038–3094 | PLAYER VS PLAYER | §20 | — |
| (absent; TOC L355) | GLOSSARY | §21 | to be written |
| L3098 | F.A.Q. | cut | empty |
| L3102–3366 | COMMUNITY UPDATE PACK | Appendix A (stat table), Appendix B (card amendments) | working notes cut |

## 2. Meta-commentary inventory

Category key: **PUB** publisher criticism · **DES** design rationale / "this edition aims to…" · **1P** first person · **COM** appeal to the community · **ED** editorial note · **WIP** work-in-progress statement · **ADV** advice to players (difficulty, strategy, session logistics) · **SELF** self-reference to "this rule-set" / "these rules".

| ID | Lines | Opening words (verbatim) | Category | Disposition | Rewritten text (for REWRITE / MOVE) |
|---|---|---|---|---|---|
| F-002 | L373 | "Dark Souls the Board Game was developed and published by Steam Forged Games (SFG) in 2017. The original Kickstarter…" | PUB, DES | CUT | — |
| F-003 | L375 | "This rule set is designed to be an answer to the community's request… Ultimately, I would love to produce…" | DES, 1P, COM | MOVE-TO-FOREWORD | "This book is the complete rulebook for Dark Souls: The Board Game, Second Edition. It gathers the rules of the core game and of every expansion into one text and resolves the conflicts between them. Nothing beyond this book and the game components is required to play." (full Foreword in §9) |
| F-004 | L377 | "This project started by cutting out any more radical additions that were present in my own playtested ruleset…" | WIP, 1P (×5), COM, ED, 2P | CUT | — |
| F-005 | L379 | "For editors reading through this, please note that this rule-book will have many diagrams…" | ED, 1P (×3) | CUT | — |
| F-006 | L381 | "Please note game terms that are written in *italics* will have quick reference definitions in a glossary…" | ED | REWRITE-IN-VOICE → Foreword | "Terms set in *italics* are defined in the Glossary (see §21)." |
| F-009 | L845 | "Players should include all equipment cards from expansions available in their games to increase variety." | ADV, DES | REWRITE-IN-VOICE (or CUT as duplicate of L1057) | "Equipment cards from every expansion in the party's collection are included in the treasure decks (see §6.2)." |
| F-010 | L1057 | "DStBG has many expansion sets available of which many include new treasure cards. Players should include…" | ADV, product ref | REWRITE-IN-VOICE | "Treasure cards from every expansion in the party's collection are sorted into the tier one and tier two decks by the rules in §6.2." |
| F-011 | L1141 | "DStBG has many expansion sets available which include new encounter cards. By default, players should include only…" | ADV, product ref | REWRITE-IN-VOICE | "Each encounter deck contains only the encounter cards from the set of the next boss. The party may instead agree during setup to build each deck from all encounter cards in its collection." + *Example.* (Gargoyle / Sif) |
| F-013 | L1109 | "For added challenge the players may forgo choice and instead randomly determine…" | ADV | REWRITE-IN-VOICE | "The party may instead select each boss at random: shuffle the data cards of the eligible bosses of that type and reveal one." |
| F-023 | L2041 | "Players with the Encounters expansion set available may choose… Groups with new players should default to leaving mimics out…" | ADV, SELF ("The following rules assume…") | REWRITE-IN-VOICE | "Mimics are an optional rule. They require the Explorers expansion. The party decides during setup whether mimics are in play." |
| F-025 | L2053 | "…Players should include crystal lizards as an optional game component if they own the Iron Keep expansion set. The following rules are assuming…" | ADV, SELF | REWRITE-IN-VOICE (first sentence KEEP-AS-INTRO, trimmed) | "Crystal lizards are glimmering reptiles that yield rare materials if slain before they escape. Crystal lizards are an optional rule. They require the Iron Keep expansion. The party decides during setup whether crystal lizards are in play." |
| F-027 / F-050 | L2069 | "…The core game does not come with mega-bosses as they are optional objectives which players can attempt… should they want a more epic final battle." | product ref, ADV | CUT (sentence); rest of paragraph KEEP-AS-INTRO trimmed | see §5 |
| F-033 | L2159 | "Players can gain an advantage over a boss by memorising the order in which the boss behaviour cards will appear…" | ADV (strategy) | CUT | — |
| F-034 | L2191 | "Because the boss takes a turn after each individual character takes their turn, one can assume…" | DES (reasoning in place of rule) | REWRITE-IN-VOICE | "After each character's turn, if that character dealt damage to the boss, move the *aggro* token to that character. Otherwise it does not move." |
| F-035 | L2197 | "This is often a reasonable time to end a game session if time is limited. Either today or another day…" | ADV (session logistics) | CUT | — |
| F-036 | L2221 | "Campaigns provide a more challenging and longer play experience suitable for players who have played the basic game at least a few times.." | ADV | CUT (or chapter-intro sentence: "A campaign is a longer adventure of several sections, each ending in a boss.") | — |
| F-037 | L2223 | "Players might expect to meet over multiple play sessions to complete a campaign…" | ADV (and factually wrong: campaigns run 3–6 sections) | CUT | — |
| F-038 | L2225 | "This rule-set includes three campaigns which require only the components available in the core set. Many of the game's expansions also add additional campaigns…" | SELF, external | REWRITE-IN-VOICE | "The party chooses a campaign from §19. Each campaign lists the components it requires." |
| F-040 | L2297 | "The rules for returning to the *bonfire* are essentially unchanged from the basic rules… increased in Campaign play to slow the characters' progression to scale better across a longer journey." | DES | REWRITE-IN-VOICE | "The *bonfire* rules of §11 apply in a campaign with the following changes. Stat tier costs are those in the table below. Characters may also transpose boss treasure (§18.8) and burn a bonfire ascetic (§18.7)." |
| F-041 | L2312 | "Andre's Shop functions similarly to the basic rules with some changes to how the shop is stocked to better suit the progression of the campaign." | DES | REWRITE-IN-VOICE | "The shop rules of §11.4 apply in a campaign with the following changes." |
| F-042 | L2304 | "They must decide at what point their need for better equipment outweighs the cost of increased difficulty." | ADV | CUT | — |
| F-046 | L3098 | "# F.A.Q." (empty) | ED (format) | CUT | — |
| F-047 | L3102–3206 | "**Treasure - Official** … **Treasure - Errata/Updated** … (will keep old one-handed version) … (will need custom card…)" | WIP, ED, external ("Official", "Errata") | CUT from rulebook; rules content → Appendix B "Card Text Amendments" | e.g. "Titanite Chunk: +2 attack. May be attached only in place of a Titanite Shard." / "Chloranthy Ring: each character on the wearer's node recovers one additional stamina at the start of their turn." |
| F-048 | L3208 | "The first edition of DStBG has many nonsensical weapon stat requirements which this edition aims to remedy…" | DES ("changes from prior edition"), external (video game, source material) | CUT paragraph; table → Appendix A | "The weapons listed below use the stat requirements given here in place of the values printed on their cards." |

Lesser advisory/rationale fragments inside otherwise sound rules (handled as tone rows): F-012 L1107 "if they wish… epic battle… if they like"; F-014 L1201 "Players should agree"; F-015 L1596 "Players should take note… Of course"; F-020 L1890 "the players must carefully weigh the timing of each spark spent"; F-022 L2027 "Thus, the invader will take many more turns…"; F-028 L2077 "information about boss behaviour cards will follow"; F-044 L1017/1021 "to suggest which class might benefit most".

## 3. External-reference inventory

Legitimate component identification (e.g. "(Darkroot Basin)" in §2 lists, "requires the Core set and Iron Keep expansion" in §19 headers, "Explorers expansion" as the home of mimics) is **not** listed; it stays. Listed below are references to other rulebooks, products or sources **as rules sources or as framing**.

| ID | Line | Text | Disposition | Replacement |
|---|---|---|---|---|
| F-001 | L1–3 | "Based on related works by Steam Forged Games (SFG), Konami, Santuric, … and the rest of the DStBG Community." | MOVE to colophon as acknowledgements | "Rules compiled and revised by PittedPanda. With thanks to Santuric, Wilhelm, Astray, Manuel, Chud, Winston, Jyace, Absolute Disgrace, Zed and Gorus." (publisher trademark line, if required, as a single legal line) |
| F-002 | L373 | "Steam Forged Games (SFG) in 2017", "The original Kickstarter", "two new core sets" | CUT | — |
| F-004 | L377 | "my own playtested ruleset", "community and SFG rulesets", "google docs" | CUT | — |
| F-005 | L379 | "rip the old ones from the original rule book" | CUT | — |
| F-006 | L381 | "at the end of the rule book" (self-reference, future tense) | REWRITE | "(see §21)" |
| F-010 | L1057 | "DStBG has many expansion sets available…" | REWRITE | see §2 |
| F-011 | L1141 | "DStBG has many expansion sets available…" | REWRITE | see §2 |
| F-049 | L1195 | "employing any special rules described in the mega-boss rule booklet" | REWRITE (Blocker) | "The mega-boss's special rules (see §17) apply." — **§17 must be completed for the eight other mega-bosses or this resolves to nothing** |
| F-050 | L2069 | "The core game does not come with mega-bosses…" | CUT | — |
| F-051 | L2041 | "Encounters expansion set" (wrong component name; "Explorers" elsewhere) | REWRITE | "the Explorers expansion" |
| F-038 | L2225 | "This rule-set includes three campaigns… Many of the game's expansions also add additional campaigns for selection." | REWRITE | "The party chooses a campaign from §19. Each campaign lists the components it requires." |
| F-053 | L2221, 2229, 2233, 2235, 2243, 2245, 2289, 2297, 2312, 3060 | "the basic game" / "the basic rules" (×10, reads as a separate book) | REWRITE | define "the standard game" once in §18 intro; thereafter "(see §x.y)" |
| F-052 | L2352 ff. (13 campaign headings) | "Dark Souls 3 (Core)", "Dark Souls 2 (Explorers)", "Dark Souls (Phantoms)" — video-game titles as source tags | OPTIONAL rewrite | keep the component tag only: "The Coiled Sword (Core)"; setting, if wanted, as an in-voice subtitle |
| F-047 | L3104, L3176 | "Treasure - Official", "Treasure - Errata/Updated" | CUT | Appendix B heading "Card Text Amendments" |
| F-048 | L3208 | "The first edition of DStBG…", "from the video game series", "in the source material", "roughly equal to the first edition" | CUT | Appendix A lead sentence (see §2) |
| F-054 | L387–723 | Set codes "PWA", "ToG" undefined | KEEP with key | one-line key at head of §2 |

No reference to a page number of any external book was found. No URL was found other than the "google docs" mention at L377.

