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

## 4. Voice audit per chapter

Register key: **PROC** numbered procedure · **BUL** bullet fragments · **DECL** declarative prose · **CONV** conversational / explanatory prose · **ADV** advisory ("players should…") · **LIST** component/campaign lists · **FLAV** flavour.

| # | Chapter (lines) | Dominant register | Example lines | Tense / person shifts | Tone slips (line: phrase) |
|---|---|---|---|---|---|
| 1 | INTRODUCTION (L361–369) | DECL + FLAV intro | L363 "Dark Souls the Board Game Second Edition (DStBG 2E) is a cooperative dungeon crawl…"; L369 "Nameless accursed undead, seek strength, and prepare to die." | future "Each player will control" (L363); imperative to reader in flavour (L369, permitted) | none beyond the intro flavour |
| 2 | SECOND EDITION NOTES (L371–381) | CONV, 1P, ED | L375 "Ultimately, I would love to produce…"; L379 "For editors reading through this, please note…" | first person throughout; "you" ×2 (L377); future "will desist", "will have" | whole chapter is meta (F-002…F-006) |
| 3 | GAME COMPONENTS (L383–723) | LIST | L387 "Each character has a unique miniature, character dashboard…"; L409 "Each enemy has a number of miniatures and a data card." | none | none; set codes undefined (F-054); "HungryVoracious Mimic" (L441) and "2X" (L451, L673) are typographic, not voice |
| 4 | CHARACTERS (L725–805) | DECL | L775 "When a character spends one or more stamina, they add that number of stamina cubes…"; L789 "If a character is ever forced to place a damage cube… the character dies." | "one must pay" (L769); "players should not interact" (L765) vs characters acting elsewhere; "Finally, players should be aware that…" (L805) | L765 "Finally,"; L805 "Finally, players should be aware"; L793 "The ready side is coloured in brighter colours" (descriptive, fine) |
| 5 | EQUIPMENT (L807–891) | DECL (numbered card anatomy) + BUL (Spells) | L811 "Equipment cards include weapons, spells, shields, armour, and items…"; L861 "- A character is always limited to one spell *attack option* per turn." | register switches from prose (4.1–4.2) to bullets (4.3) and back (4.4) | L845 "Players should include… to increase variety" (ADV); L859 "usually with a coloured magic effect"; L849 "For example, a character could attach…" (inline example) |
| 6 | TILES & NODES (L895–981) | DECL (5.1–5.4, official Core voice) + BUL (5.5 Terrain) | L919 "Multiple models can share the same node. However, only three models…"; L933 "- Models cannot *walk*, *run*, *dodge*, or be pushed into nodes containing a gravestone." | "the players must push" vs "characters must choose" (L919); lower-case sentence start "characters must choose" | L921 "Therefore, a node may contain one boss and three characters, for example."; L979 "simply stop adding trap tokens… Players should fill" |
| 7 | SETUP (L985–1195) | PROC | L989 "2. Equip each character with the starting equipment with a matching icon."; L1145 "1. Return any dropped souls to the characters." | imperatives (implied actor: the party) — acceptable in procedures; prose asides in ADV (L1057, L1141); conditional mood L1109 "This would be repeated" | L1107 "epic battle… if they like"; L1109 "For added challenge"; L1131/L1159 "should increase"; L1195 "mega-boss rule booklet" |
| 8 | GAMEPLAY (L1197–1479) | BUL (nested fragments) with one PROC (Encounter Start) | L1207 "- Drop all *souls* from the dashboard onto the current encounter tile."; L1385 "- *Souls* cannot be transferred between characters." | "Players begin *sparks*" (L1245) vs "Characters track their personal supply" (L1385); future "will be awarded" (L1461, L1479), "Invaders will attempt" (L1241) | L1201 "a single intimate victor", "Players should agree"; L1263 inline example in conditional mood; L1475 "See the detailed rules on mimics later" |
| 9 | COMBAT BASICS (L1481–1658) | DECL (8.1–8.4) + BUL (8.5 Conditions) | L1485 "When a character or an enemy attacks, the model defending the attack is considered the attack's target."; L1606 "- *Bleed* tokens are limited to one per model." | "the players choose the node" (L1592) — players as deciders, acceptable; "Therefore… therefore" (L1487) | L1596 "Players should take note that… Of course,"; L1594 "In other words," |
| 10 | ENEMY TURN (L1660–1796) | DECL (9.1–9.2, verbatim Core) + PROC (9.3 defence sequences) | L1678 "When two different nodes would take an enemy closer to where it is trying to go, the players can choose…"; L1741 "1. Pay one stamina to attempt to *dodge* an attack." | future "how an enemy model will move" (L1670), "that enemy will make" (L1706); "the players decide which model should go first" (L1666) | L1674/1676 "it simply does not move"; L1708 "More on each defensive option listed below." (fragment); L1706 "special rules detailed later" |
| 11 | CHARACTER TURN (L1798–1880) | hybrid: blockquote AND/OR fragments (10.1), DECL (10.2–10.5, Core voice for icons) | L1806 "> *Walk*: Move character model to an adjacent node. > **AND**"; L1846 "During the character's turn they may make up to one attack with each weapon…" | "the player may elect to issue any re-rolls" (L1846) vs "the character" elsewhere; future "will instead do magical damage" (L1848) | L1876 "decidedly on the offensive"; L1868 "Bows, polearms, and other unwieldy weapons…"; L1872 "rapid flurry of attacks… agile sword"; L1852 "Though many weapons simply deal damage" |
| 12 | RETURNING TO THE BONFIRE (L1884–1963) | FLAV intro + BUL (11.2) + DECL (11.3–11.4) + CONV (11.5) | L1896 "- Remove all damage and stamina from the character dashboards."; L1963 "Once the characters are restored to strength and no longer wish to spend souls they are nearly ready…" | "the characters must collectively spend" (L1890) vs "players must carefully weigh" (L1890); lower-case "characters cannot equip" (L1931); "should move their models" (L1963) | L1888 "mysterious blindfolded woman", "massive smith toiling endlessly"; L1890 "paramount", "hard-earned", "most precious resource… carefully weigh the timing"; L1963 "nearly ready", "At this point" |
| 13 | SUMMONS (L1967–2037) | PROC | L1973 "1. *Embered* characters may elect to pay two *souls* to draw a phantom card."; L2003 "3. Shuffle enough blank invader tokens…" | "Players must agree" (L1977) vs "*Embered* characters may elect" (L1973); future "the invader will take many more turns" (L2027) | L2027 "Thus, the invader will take many more turns than any other model" (aside); L2037 "Invaders do not reset or return once encountered regardless of outcome" (fine) |
| 14 | MIMICS (L2039–2047) | CONV / ADV | L2041 "Groups with new players should default to leaving mimics out as they can be quite punishing."; L2045 "However, if the characters wish to open the chest, they must reveal one an *ambush* card…" | "Players with…" → "characters must collectively decide" → "the party" (L2045); future "The mimic will take its turn first" (L2047); "The then are faced" (typo) | L2041 "quite punishing", "Experienced players should"; L2043 "out of fear of encountering a mimic"; L2045 "lurking mimic"; L2047 "Refer to…" |
| 15 | CRYSTAL LIZARDS (L2051–2057) | FLAV intro + CONV | L2053 "Crystal lizards are strange and glimmering reptiles…"; L2055 "However, their behaviours dictate that they simply run from the characters which makes killing them challenging." | future "no further crystal lizards will spawn" (L2057); "Players should include" (L2053) | L2055 "which makes killing them challenging"; L2057 "Note that an encounter is still considered *cleared*" |
| 16 | BOSS ENCOUNTERS (L2061–2151) | FLAV intro + DECL (Core/V2 voice) | L2131 "Bosses always directly face an adjacent node."; L2139 "A character sharing a node with a boss may elect to move to an adjacent boss arc…" | "the player may select" (L2137) vs "the character" (L2139); lower-case "characters can expect" (L2069); "should be removed" (L2065) | L2069 "targets of their bloodlust", "can expect to die often", "astute tactics, and the favour of luck"; L2077 "noticeably lacking"; L2099 "dozens of wound tokens"; L2103 "often"; L2129 "key part of what makes boss encounters unique"; L2151 "Remember that… Note that" |
| 17 | BOSS TURNS (L2153–2197) | DECL | L2165 "When a boss moves towards a target, it first rotates to align the centre of its front arc…"; L2195 "When the boss's health dial is reduced to zero, the boss is slain and the encounter ends." | "one can assume" (L2191); "should remain static" (L2169); lower-case "characters must take an equal number" (L2155), "characters targeted" (L2185) | L2159 "Players can gain an advantage… by memorising"; L2191 "Therefore, simply move"; L2197 "This is often a reasonable time to end a game session" |
| 18 | BOSS SPECIAL RULES (L2199–2213) | DECL | L2205 "When the Asylum Demon or Stray Demon makes a physical attack with an *area* icon, check to see if there are any pillar tokens within the affected area."; L2213 "When the Wind Up behaviour icon is resolved, the characters may each spend one stamina…" | "the party rests" (L2209) — first use of "the party" as actor (good) | L2207 "it is possible for a demon to smash through multiple pillars at once or even…" (explanatory, acceptable if shortened) |
| 19 | CAMPAIGN PLAY (L2217–2348) | CONV + DECL + BUL | L2221 "The setup for a campaign is largely the same as the basic game."; L2243 "- Encounter *soul* rewards are reduced by one compared to the basic game." | "Players might expect" (L2223) vs "the characters gain one *spark*" (L2235); conditional "would like to join" (L2239) | L2221 "more challenging and longer play experience… at least a few times.."; L2297 "essentially unchanged… to slow the characters' progression"; L2312 "to better suit the progression"; L2304 "must decide at what point their need… outweighs"; L2306 "invites stronger enemies" |
| 20 | CAMPAIGNS (L2350–3034) | LIST with one-line preambles | L2354 "Use only encounters from the core set when setting up each section."; L2456 "Do no place invader tokens during the campaign. Instead, just add the invaders below." | imperative preambles (acceptable as setup instructions); "players should add… if available" (×9) | L2456/2504 "just add"; campaign subtitles cite video games (F-052); "Facing the Abyss" appears twice (L2548, L2764) — content duplicate for Audit C/E |
| 21 | PLAYER VS PLAYER (L3038–3094) | BUL (whole chapter) | L3040 "- Decide during setup if PvP rules will be used or not."; L3058 "- Characters take turns in descending threat order." | imperative + future ("will be used", "will occur"); passive "is awarded victory" | L3082 "Victory on the final boss determines the ultimate champion." (fine); no flavour |
| 22 | GLOSSARY (absent) | — | TOC L355 only | — | referenced at L381; must be written (F-082) |
| 23 | F.A.Q. (L3098) | empty | — | — | format is reader dialogue (F-046) |
| 24 | COMMUNITY UPDATE PACK (L3102–3366) | LIST + working notes + CONV preamble | L3190 "- Sellsword Twinblade (will keep old one-handed version)"; L3208 "The first edition of DStBG has many nonsensical weapon stat requirements which this edition aims to remedy." | future "will keep / will use / will need" (×5); passive past "where assessed", "were revised" (L3208) | whole preamble is design commentary (F-048); labels "Official", "Errata" (F-047) |

### Second person and reader imperatives (Task 4)

| Line | Text | Type | Disposition |
|---|---|---|---|
| L377 | "Please comment on any errors you find or issues with proposed rules." | "you" | CUT (F-004/F-055) |
| L377 | "Thank you for reading this far." | "you" | CUT |
| L369 | "Nameless accursed undead, seek strength, and prepare to die." | imperative, chapter-intro flavour | KEEP-AS-INTRO (F-007) |
| L379 | "For editors reading through this, please note…" | reader imperative | CUT (F-005) |
| L381 | "Please note game terms that are written in *italics*…" | reader imperative | REWRITE (F-006) |
| L1475 | "See the detailed rules on mimics later in these rules for details." | reader imperative | "(see §13)" (F-056, F-067) |
| L1596 | "Players should take note that only enemy behaviours that deal damage can be dodged." | reader address via "players" | REWRITE (F-015) |
| L2047 | "Refer to “**Boss Encounter**” rules for more details…" | reader imperative | "(see §15.5 and §16)" (F-056, F-074) |
| L2057 | "Note that an encounter is still considered *cleared*…" | reader imperative | REWRITE (F-026) |
| L2151 | "Remember that a character can be in more than one arc…" / "Note that even if a character is attacking multiple weak arcs…" | reader imperatives (inherited from Core p.28) | REWRITE (F-032) |

Procedural imperatives in numbered steps ("Shuffle…", "Place…", "Draw…", L987–1195, L1255–1281, L1969–2037, L3040–3094) are **not** second person: they are the procedure register with the party as implied actor and are retained under Voice Guide §6.

## 5. Flavour sentences

Flavour is permitted only in chapter intros (≤ 60 words). Everything else is CUT or folded into a rule.

| Line | Chapter | Sentence | Verdict |
|---|---|---|---|
| L365 | Introduction | "To succeed in their quest the characters must: learn their enemies behaviours, train their skills, seek out powerful weapons, and work together…" | KEEP-AS-INTRO (tightened in §9) |
| L367 | Introduction | "When characters die, they lose part of their humanity. After death they arise weaker and *hollow*…" | KEEP-AS-INTRO (tightened in §9) |
| L369 | Introduction | "Nameless accursed undead, seek strength, and prepare to die." | KEEP-AS-INTRO |
| L1025 | Setup › Legendary Treasure | "These represent exceedingly rare relics that do not appear in every game and cannot be purchased." | CUT flavour; keep the two rules (F-045) |
| L1107 | Setup › Boss Selection | "…ending in an epic battle with a mega-boss…" | CUT (F-012) |
| L1868 | Character Turn › Shaft | "Bows, polearms, and other unwieldy weapons are difficult to use effectively at short range." | CUT (F-016) — Core p.23 voice |
| L1872 | Character Turn › Repeat | "This represents a rapid flurry of attacks such as from an agile sword or a repeating crossbow." | CUT (F-017) |
| L1876 | Character Turn › Two-Handed | "Characters equipped with a two-handed weapon are decidedly on the offensive." | CUT (F-018) |
| L1888 | Returning to the Bonfire (intro) | "The *bonfire* serves as a safe haven in an otherwise treacherous world… a mysterious blindfolded woman… a massive smith toiling endlessly at his forge." | KEEP-AS-INTRO, trim to ≤ 60 words (F-019); remove the rule hidden in "if they bring him suitable materials" |
| L1890 | Returning to the Bonfire | "Resting at the *bonfire* is paramount…"; "hard-earned *souls*"; "*Sparks* are the most precious resource in this game…" | CUT (F-020) |
| L2043 | Mimics | "…or leave it be out of fear of encountering a mimic." | CUT (F-024) |
| L2045 | Mimics | "…to determine if the chest is a lurking mimic." | CUT (F-024) |
| L2053 | Crystal Lizards (intro) | "Crystal lizards are strange and glimmering reptiles that offer character's powerful rewards if the lizard is slain before it can escape." | KEEP-AS-INTRO, trimmed (F-025) |
| L2055 | Crystal Lizards | "…they simply run from the characters which makes killing them challenging." | CUT clause |
| L2069 | Boss Encounters (intro) | "Boss encounters are the heart of the character's adventure and the bosses are the targets of their bloodlust. Bosses are single models that are not only large in stature, but formidable opponents…" | KEEP-AS-INTRO, trimmed: drop "targets of their bloodlust" |
| L2069 | Boss Encounters | "characters can expect to die often at the hands of these powerful enemies. Only with adequate preparation, astute tactics, and the favour of luck should the characters hope to fell a boss." | CUT (F-027) |
| L2129 | Boss Encounters › Arcs | "These arcs are a key part of what makes boss encounters unique, and they add an extra layer of tactics…" | CUT (F-031) — Core p.27 voice |
| L2221 | Campaign Play | "Campaigns provide a more challenging and longer play experience…" | CUT or one intro sentence (F-036) |
| L2306 | Campaign Play › Bonfire Ascetic | "However, burning the bonfire ascetic invites stronger enemies." | CUT (F-043) |

Chapters with **no** intro flavour at all (acceptable; an intro may be added at ≤ 60 words if layout wants one): Game Components, Characters, Equipment, Tiles & Nodes, Setup, Gameplay, Combat Basics, Enemy Turn, Character Turn, Summons, Boss Turns, Boss Special Rules, Campaigns, Player vs Player.

## 6. Prose cross-reference resolution

Phase 2A convention: a parenthetical **(see §N.M)** placed after the clause, using the provisional numbering in §1; **never** 'later', 'previously', 'earlier', 'aforementioned', 'as described', 'as usual', 'as before'. 'Below' and 'above' are permitted only for material inside the same numbered section. Reader imperatives ('See…', 'Refer to…') are replaced by the parenthetical. Dangling or imprecise references are marked **DANGLING** / **IMPRECISE**.

| ID | Line / section | Current wording | Resolves to | Phase 2A replacement |
|---|---|---|---|---|
| F-053 | L2221, L2229, L2233, L2235, L2243, L2245, L2289, L2297, L2312, L3060 | 'the basic game' / 'the basic rules' (×10) | §6–§17 (the standard game) — internal, but reads as another book | Define 'the standard game' once in the §18 intro; thereafter '(see §x.y)' or delete |
| F-057 | L757 §Characters › Equipment Slots | as described | no antecedent (the slot rules follow in the same section) **DANGLING** | Delete 'as described'; the following paragraphs state the rule. |
| F-058 | L837 §Equipment › Equipment Cards | explained in detail later on in the section title “Character Attacks” | §10.3 Character Attacks | '(see §10.3)' |
| F-059 | L839 §Equipment › Equipment Cards | explained in detail later on in the section titled “Enemy Attacks” | §9.3 Enemy Attacks | '(see §9.3)' |
| F-060 | L841 §Equipment › Equipment Cards | at Blacksmith Andre which is described later in more detail | §11.4 Blacksmith Andre | '(see §11.4)' |
| F-061 | L891 §Equipment › Embers | with the aforementioned effects | §3.5 Character Tokens › Ember; §7.3 Embering | '(see §7.3)' |
| F-062 | L1057 §Setup › Using Expansion Treasure | as above | §6.2 Treasure Deck Setup | '(see §6.2)' |
| F-063 | L1165 §Setup › Setup After the mini-boss step 9 | as previously described | §6.3 Shop Setup › After Boss is Defeated | '(see §6.3)' |
| F-064 | L1169, L1187 §Setup › After mini-boss step 11 / After main-boss step 7 | as usual | §11 Returning to the Bonfire | '(see §11)' |
| F-065 | L1171 §Setup › Setup After the mini-boss step 12 | in the same way as before | §7.5 Encounters | '(see §7.5)' |
| F-066 | L1195 §Setup › Setup After the main-boss step 11 | described in the mega-boss rule booklet | external; nearest in-book target §17 Boss Special Rules (incomplete) **DANGLING** | '(see §17)' once §17 is complete |
| F-067 | L1475 §Gameplay › Treasure Rewards | See the detailed rules on mimics later in these rules for details. | §13 Mimics | '(see §13)' |
| F-068 | L1485 §Combat Basics › Target versus Hit | per the optional rules detailed later | §20 Player vs Player | '(see §20)' |
| F-069 | L1600 §Combat Basics › Conditions | listed below | same section (§8.5 sub-headings) | Permitted: 'below' may be used only for material within the same numbered section. |
| F-070 | L1706 §Enemy Turn › Enemy Attacks | with special rules detailed later | targets are §8.4 Pushing and §8.5 Conditions (earlier), and §16.3 Boss Attacks (later) **IMPRECISE** | '(see §8.4, §8.5 and §16.3)' |
| F-071 | L1708 §Enemy Turn › Enemy Attacks | More on each defensive option listed below. | same section | CUT the fragment; the sub-headings follow. |
| F-072 | L1760 §Enemy Turn › Dodge step 5.2 | Determine damage to the defending character as above. | §9.3 Block & Resist step 5 | 'as in Block & Resist step 5' (same section) or '(see §9.3, step 5)' |
| F-073 | L1852 §Character Turn › Character Attacks | the magical damage icon explained above, the conditions explained previously, and the following weapon icons | §10.3 (same section); §8.5 Conditions | 'the magical damage icon (above), conditions (see §8.5), and the following icons' |
| F-074 | L2047 §Mimics | Refer to “Boss Encounter” rules | §15.5 Boss Behaviour Cards; §16 Boss Turns (heading is 'BOSS ENCOUNTERS', not 'Boss Encounter') | '(see §15.5 and §16)' |
| F-075 | L2069 §Boss Encounters › Overview | as described previously | §8 Combat Basics; §9 Enemy Turn | '(see §8 and §9)' |
| F-076 | L2099 §Boss Encounters › Boss Data Cards | from previously described enemy data cards | §8.2 Enemy Data Cards | '(see §8.2)' |
| F-077 | L2105 §Boss Encounters › Boss Data Cards | as detailed during the setup chapter of these rules | §6.5 Encounter Setup › Encounter cards | '(see §6.5)' |
| F-078 | L2163 §Boss Turns › Boss Movement & Symbols | previously described with the following exceptions | §9.2 Enemy Movement; §9.3 Enemy Attacks | '(see §9.2 and §9.3)' |
| F-079 | L2195 §Boss Turns › Boss Death | as previously described | §7.6 Souls; §7.7 Treasure Rewards | '(see §7.6 and §7.7)' |
| F-080 | L2197 §Boss Turns › Boss Death | post-boss setup rules as described earlier in these rules | §6.6 Setup After the Mini-boss; §6.7 Setup After the Main-boss | '(see §6.6 and §6.7)' — sentence otherwise CUT (F-row for L2197) |
| F-081 | L2456, L2504 §Campaigns | just add the invaders below | same section list | Permitted ('listed below', same section). Fix typo 'Do no place' → 'Do not place'. |
| F-082 | L381 §Second Edition Notes | in a glossary at the end of the rule book | Glossary appears in TOC (L355) but not in the body **DANGLING** | '(see §21)' once the Glossary exists |
| F-083 | L1263, L1141, L849, L1914, L2141 (inline 'For example…') | For example, if the first three encounters are marked cleared… | n/a — worked examples embedded in rule sentences | Set each as a separate *Example.* paragraph per the Voice Guide §7; examples are not rules. |

Dangling / imprecise: F-057 (L757 'as described' — no antecedent), F-066 (L1195 'mega-boss rule booklet' — external; in-book target §17 is incomplete), F-070 (L1706 'detailed later' — targets are mostly earlier), F-082 (L381 'glossary at the end of the rule book' — no Glossary in the body). Heading-name mismatch: L2047 cites “Boss Encounter” but the chapter is 'BOSS ENCOUNTERS' (F-074).

## 7. Copied-prose check

Detected by 6-word shingle overlap against every official text in `work/text/`; 'run' = longest consecutive matching word run; '%' = share of the manuscript line's shingles found on the cited page. Page = printed folio. These are **voice** observations only (rights are held): verbatim passages carry the official explanatory register — reader address ('Remember that', 'Note that'), examples in parentheses, 'for example' tails — and will need the same treatment as the author's own prose in Phase 2A.

| ID | Line / section | Manuscript text (opening) | Official source | Degree |
|---|---|---|---|---|
| F-093 | L387 §Game Components › Characters | Each character has a unique miniature, character dashboard, three to four starting equipment cards… | Core p.4 | close paraphrase (10-word run) |
| F-094 | L777–779 §Characters › Endurance Bar | When a character spends one or more stamina, they add that number of stamina cubes… / When a character suffers one or more damage, they add that numbe… | V2 p.9 | close paraphrase (10-word runs) |
| F-095 | L797 §Characters › Heroic Action | A character may flip their heroic action token to the used side as a minor action… | V2 p.9 | paraphrase (9-word run) |
| F-096 | L801 §Characters › Luck | A character may flip their luck token to the used side to reroll any attack or defence roll… | Core p.11, p.15 | close paraphrase (12-word run) |
| F-097 | L805 §Characters › Ember | Ember tokens are placed face-up onto a character's dashboard when that player discards an ember card… | V2 p.9 | paraphrase (11-word run) |
| F-098 | L837 §Equipment › Equipment Cards | An equipment card's actions represent an attack or special effect used during an encounter. Each line on the card represents a separate attack option… | Core p.12 | close paraphrase (14-word run) |
| F-099 | L843 §Equipment › Equipment Cards | Some equipment cards have dice modifiers that add a fixed value to the die roll or subtract a fixed value from the die roll. | Core p.12 | near-verbatim (74% shingle overlap) |
| F-100 | L849 §Equipment › Upgrades | Upgrade cards are used to enhance equipment. There are two types of upgrade cards… | V2 p.10 | paraphrase (10-word run) |
| F-101 | L899–901 §Tiles & Nodes › The Basics | All tiles have one or more doorways. Doorways allow characters to travel between tiles. / Every tile except for the bonfire tile has a number of circu… | Core p.10 | near-verbatim (19-word run, 59%) |
| F-102 | L903–911 §Tiles & Nodes › The Basics | Basic nodes are the most common type of node… Spawn nodes are where enemy models are placed… Terrain nodes are where terrain features are placed… The … | Core p.10 | verbatim (L909 100%, L911 74%) |
| F-103 | L915 §Tiles & Nodes › Movement | During encounters, each model must always occupy a single node. When a character moves, they place their model on an adjacent node. An adjacent node i… | Core p.10 | close paraphrase (13-word run) |
| F-104 | L919 §Tiles & Nodes › Node Model Limits | Multiple models can share the same node. However, only three models can share a node at the same time, regardless of how many are friendly or enemy mo… | Core p.10 (also V2 p.11) | near-verbatim (35-word run) |
| F-105 | L921 §Tiles & Nodes › Node Model Limits | The exception to this rule is that nodes also have a boss limit. Only one boss model can ever be on a node… Therefore, a node may contain one boss and… | Core p.10 | near-verbatim (27-word run) |
| F-106 | L925 §Tiles & Nodes › Range | Attacks and effects have a maximum range that is counted from one model to another model, whether friendly or enemy. Range 0 means the models must be … | Core p.10 | near-verbatim (53%) |
| F-107 | L961 §Tiles & Nodes › Chests | Chests always begin encounters with the closed side face-up and with one face-down treasure Card of the appropriate Tier beneath it. | V2 p.12 | paraphrase (10-word run) |
| F-108 | L1485–1487 §Combat Basics › Target versus Hit | When a character or an enemy attacks, the model defending the attack is considered the attack's target… A model is considered hit by an attack even if… | Core p.20 | paraphrase (section structure and phrasing) |
| F-109 | L1491–1493 §Combat Basics › Enemy Data Cards | Each enemy type in the game has a data card breaking down how it works in the game. Enemy data cards give the information necessary… Each enemy data c… | Core p.20 | verbatim (33-word run, 88%) |
| F-110 | L1513–1517 §Combat Basics › Enemy Data Cards | The behaviour icons are the core element of any enemy… An enemy's threat level determines the order in which it takes a turn in combat with higher val… | Core p.20 | near-verbatim (24-word run; 'heart of any enemy' → 'core element') |
| F-111 | L1588–1594 §Combat Basics › Pushing | Certain movements and attacks are labelled as push-movements and push-attacks… Push movement does not cost stamina. / Boss models cannot be pushed by … | Core p.21 (L1590 also V2 p.21) | near-verbatim (L1590 58%; L1594 16-word run) |
| F-112 | L1600 §Combat Basics › Conditions | Some attacks inflict conditions on their target. When an attack has a condition icon, place the corresponding condition token on the model(s) hit by t… | Core p.21 | near-verbatim (10-word run) |
| F-113 | L1664–1666 §Enemy Turn › Overview | …beginning with the highest threat and ending with the model with the lowest threat. For enemies with equal threat levels… / Non-boss enemies follow t… | Core p.24 (also p.27, p.29) | close paraphrase (20-word run) |
| F-114 | L1670–1672 §Enemy Turn › Enemy Movement | The enemy movement icon shows how an enemy model will move. Various smaller icons can appear around the movement icon, modifying how the enemy moves. … | Core p.24 | verbatim (47%; first three sentences identical) |
| F-115 | L1678 §Enemy Turn › Enemy Movement | When two different nodes would take an enemy closer to where it is trying to go, the players can choose which node the enemy enters. | Core p.24 | verbatim (100%) |
| F-116 | L1682–1694 §Enemy Turn › Towards/Away from aggro/nearest | The enemy moves the indicated number of nodes closer to the character with the aggro token. / …farther from the character with the aggro token. / The … | Core p.24–25 (repeated p.29–30, p.40) | verbatim (L1682/L1686 100%; L1690 92%, 56-word run; L1694 68%) |
| F-117 | L1698–1702 §Enemy Turn › Push-move / Push-attack | If the Movement icon includes the push icon, the enemy's movement pushes characters out of its way. / If the push icon includes a number, characters p… | Core p.24 | near-verbatim (50%) |
| F-118 | L1838, L1846 §Character Turn › Movement / Attacks | Characters have four methods of moving from node to node… / During the character's turn they may make up to one attack with each weapon or spell equip… | Core p.22 | loose paraphrase (8–10-word runs only) |
| F-119 | L1852–1856 §Character Turn › Character Attacks / Range | Though many weapons simply deal damage, some have special abilities explained in text on their cards or with icons. This includes the magical damage i… | Core p.23 | verbatim (L1852 74%, 28-word run) |
| F-120 | L1860 §Character Turn › Shift | When a character makes an attack with the shift icon, they may move up to the number of nodes shown. Shift icons that appear before the dice icons all… | Core p.23 (also Phantoms p.9, V2 p.22) | verbatim (93%, 63-word run) |
| F-121 | L1864 §Character Turn › Area-of-Effect | Attacks with the AoE icon can target all enemies on a single node within range instead of targeting just one enemy. Make the attack roll once, and com… | Core p.23 | near-verbatim (49%, 16-word run) |
| F-122 | L1868–1872 §Character Turn › Shaft / Repeat | Bows, polearms, and other unwieldy weapons are difficult to use effectively at short range… / The repeat icon allows the character to use that entire … | Core p.23 | close paraphrase (12-word run; 'polearms' flavour is Core's) |
| F-123 | L1888 §Returning to the Bonfire › The Bonfire | The bonfire serves as a safe haven in an otherwise treacherous world… | V2 p.26 ('The bonfire is a safe haven where characters can rest for a short time') | phrase borrowing only; remainder is the author's flavour (blindfolded woman, toiling smith) |
| F-124 | L1931 §Returning to the Bonfire › Blacksmith Andre | Characters may attach any weapon upgrade cards from their inventory to equipped weapon cards and armour upgrade cards to equipped armour… | V2 p.27 | loose paraphrase (8-word run) |
| F-125 | L2069 §Boss Encounters › Overview | Boss encounters are the heart of the character's adventure… There are three types of bosses… Boss encounters follow many of the same rules as other en… | Core p.26 ('Boss encounters are the culmination of the party's exploration… There are two types of bosses… They follow many of the same rules as other enemies, but there are also some key differences.') | structural paraphrase; 'heart of' lifted from Core p.20 |
| F-126 | L2101 §Boss Encounters › Boss Data Cards | Boss behaviour deck size and heat-up point are used to determine the composition of the boss behaviour deck. | Core p.26 | paraphrase (9-word run) |
| F-127 | L2123–2125 §Boss Encounters › Boss Behaviour Cards | Some boss behaviour cards have a Heat Up symbol signifying those cards as Heat Up cards… To construct the initial boss behaviour deck, first set aside… | Core p.28 (also BDK p.12) | paraphrase (10-word runs) |
| F-128 | L2129 §Boss Encounters › Boss Arcs and Defence | The base of a boss model is separated into four distinct arcs: front, left, right, and back. These arcs are a key part of what makes boss encounters u… | Core p.27 / V2 p.29 | near-verbatim (64%, 24-word run; first sentence is V2's wording, second is Core's) |
| F-129 | L2131 §Boss Encounters › Boss Arcs and Defence | Bosses always directly face an adjacent node. For a model to directly face a node, the centre of the model's front arc must line up with the centre of… | Core p.27 (also V2 p.29) | near-verbatim (59%, 27-word run) |
| F-130 | L2137–2143 §Boss Encounters › Character Arc Movement | A character moving onto the same node as a boss must remain in the same arc as the node from which they are moving… If a character moves out of a node… | Core p.28 / V2 p.29 | paraphrase (9-word run) |
| F-131 | L2149–2151 §Boss Encounters › Attacking Bosses and Weak Arcs | When a character attacks a boss, the most recently resolved boss behaviour card determines which arcs are considered weak… Remember that a character c… | Core p.28 | verbatim (L2151 85%, 40-word run) — the 'Remember/Note' tone slips are inherited from Core |
| F-132 | L2159 §Boss Turns › Boss Turn Overview | If there are no cards remaining in the behaviour deck at the start of a boss's turn, flip the discard pile face-down without shuffling the cards to re… | V2 p.30 | close paraphrase (13-word run) |
| F-133 | L2177–2179 §Boss Turns › Boss Movement & Symbols | The turn symbol indicates the boss turns 90 degrees to the left or right… The rotate symbol indicates the boss turns 180 degrees to face their rear. | V2 p.30 | paraphrase (8-word runs) |
| F-134 | L2219–2221, L2233–2239 §Campaign Play › Setup / Sparks / Adding & Dropping Players | The setup for a campaign is largely the same as the basic game. However, each section of a scenario has varying numbers of exploration tiles… / Each t… | Core p.33 | near-verbatim (L2239 68%, 34-word run; L2221 opening sentence) |

**Summary.** Author's own voice: Introduction, Second Edition Notes, Setup (§6), Gameplay (§7), Enemy Attacks defence sequences (§9.3), Character Turn Order (§10.1), Returning to the Bonfire (§11, bar one phrase), Summons (§12), Mimics (§13), Crystal Lizards (§14), Boss Special Rules (§17), most of Campaign Play (§18), Campaigns (§19), PvP (§20), Community Update Pack. Official voice (Core 2017 unless noted): Tiles & Nodes §5.1–5.4 (Core p.10, near-verbatim), Enemy Data Cards §8.2 (Core p.20), Pushing/Conditions §8.4–8.5 openers (Core p.21), Enemy Turn §9.1–9.2 (Core p.24–25, verbatim movement rules), Character Attack icons §10.3 (Core p.23, verbatim Shift/AoE/Repeat), Boss Arcs §15.6 (Core p.27–28 / V2 p.29, near-verbatim incl. the 'Remember/Note' sentences), Boss deck renewal and turn/rotate symbols §16 (V2 p.30), Campaign Setup/Sparks/Adding Players §18.1–18.3 (Core p.33), Endurance Bar and token sentences §3.4–3.5 (V2 p.9). Official voice is **not** lawbook voice: it explains and reassures; Phase 2A should rewrite these passages to the same pattern as the rest rather than preserve them.

## 8. Voice & Register Guide (for Phase 2A)

**1. Sentence pattern.** Trigger → actor → modal → action. "When [trigger], [actor] must/may [action]." One rule per sentence; one outcome per clause. Conditions before consequences. No rhetorical connectives ("Therefore", "Thus", "Of course", "In other words", "However" as a sentence opener); state the exception as its own sentence beginning "If…" or "A … does not…".
*Before:* "Players should take note that only enemy behaviours that deal damage can be dodged. Therefore, only enemy behaviours with an associated attack value can be dodged…" *After:* "A character may dodge a push effect only if the behaviour has an attack value."

**2. Modal policy.** **must** = obligation; **may** = permission or option; **cannot** = prohibition; **never / always** only where the rule has no exception in the whole book; **is / are** for states and definitions. No **should** (advice), no **can** for permission (use *may*; *can* only for capability: "a node can hold three models" → prefer "A node holds at most three models"), no **will / would / could**. No hedge words: *usually, typically, often, generally, essentially, largely, simply, just, roughly, quite, noticeably*.

**3. Actor policy.** *Characters* act in the game world: move, attack, spend stamina and souls, equip, die, rest. *Players* appear only where the game needs a human decision that is not the character's act (tie-breaks, choosing which enemy acts first, choosing a push node). *The party* is the actor for collective decisions and collective resources (sparks, boss choice, chest decisions, campaign options). *The enemy / the boss / the model* for enemy actions. Never "one" ("one must pay"), never "you" outside the Introduction flavour. Capitalise sentence-initial "Characters".

**4. Tense and person.** Present tense, third person, active voice where the actor is known ("The boss rotates", not "facing is resolved"). Passive is permitted for setup placements with no meaningful actor ("Trap tokens are dealt face-down…").

**5. Numerals and terms.** Spell out one to nine in prose; digits for 10+ and for all values in tables, dice, costs and stats (2 souls, +1 attack, Tier 2, Level 3, 25 STR). Game terms defined in the Glossary are set in *italics* on first use in each section and are lower-case (*bonfire*, *spark*, *hollow*, *aggro* token). Named places and persons keep capitals (the Firekeeper, Blacksmith Andre, Andre's Shop). Keyword actions in small caps or italics as layout decides (*Walk*, *Run*, *Attack*), consistently.

**6. Procedures.** A numbered list, one action per step, imperative mood with the party as implied actor ("Shuffle the tier one treasure deck."), sub-steps numbered 1.1, 1.2. A procedure never contains advice, options with motives, or examples; options are their own step ("The party may instead…"). Standing rules that are not sequential are written as declarative sentences, not bullets. Bullets are reserved for unordered lists of components, conditions or eligible items.

**7. Worked examples.** Set apart from the rule as a separate paragraph (box or indented), opening with the italic label *Example.* Present tense, named characters ("the Knight", "the Herald"), concrete numbers, no conditionals ("could", "would"). An example states what happens; it never introduces a rule. *Example.* The Knight attacks a Hollow Soldier with a scaled Longsword: four sword icons rolled, +1 for scaling, five attack. The Hollow Soldier's block is 1. The Knight places four wound tokens on its base.

**8. Definitions.** Bold headword, one sentence, present tense: "**Entry node.** A basic node adjacent to the doorway through which the characters entered the tile." Definitions live in the Glossary (§21) and, where first needed, in the rules text in the same form.

**9. Chapter intros.** ≤ 60 words, in-voice flavour permitted (declarative, third person, no second person except the Introduction's closing line). An intro contains no rule; any rule found in flavour is moved below the intro.

**10. Cross-references.** "(see §N.M)" after the clause; "below"/"above" only within the same numbered section; never a chapter's name in quotation marks, never "later/earlier/previously/aforementioned", never "See"/"Refer to". No reference to any text outside this book.

**11. Headings.** Chapter titles in title case (not capitals in running text); section headings are nouns ("Enemy Movement"), not instructions ("Recover one stamina."). Optional rules open with the same three-sentence formula: "X are an optional rule. They require the Y expansion. The party decides during setup whether X are in play."

**12. Second Edition Notes (OQ-01).** *Option A — Foreword:* replace the chapter with the ≤ 180-word in-voice Foreword in §9 (scope, supersession of card text, conventions, a one-line acknowledgement) and move personal credits to the colophon. *Option B — Cut:* delete the chapter outright; move the italics/Glossary convention into the Introduction and the credits to the colophon; no Foreword. **Recommendation: Option A.** A Foreword is permitted by the brief, it gives the new reader the one fact the Notes contain that matters (this book is self-contained and governs over card text), and it is the only legitimate home for the acknowledgements at L3. All publisher history, process description and community appeals are cut under either option; if the owner wants them preserved, they belong in a separate Class C "Designer's Notes" document, not in the book.

## 9. Drafts

### 9.1 Foreword (OQ-01 option A) — 165 words

This book is the complete rulebook for Dark Souls: The Board Game, Second Edition. It gathers the rules of the core game and of every expansion into one text, resolves the conflicts between them, and incorporates the revisions that extended play has shown to be necessary. Nothing beyond this book and the game components is required to play.

The Second Edition alters the shape of play in a few deliberate ways. Encounters are shorter, and downtime between turns is reduced. Each defensive choice — *block*, *resist*, *dodge* and *parry* — is viable. Andre's Shop offers a chosen selection rather than a random one, and progression is paced across the whole adventure. Where the printed text of a card conflicts with this book, this book governs.

Terms set in *italics* are defined in the Glossary (see §21). Worked examples are labelled *Example* and are not themselves rules. Numbered procedures are followed in order.

Rules compiled and revised by PittedPanda, with thanks to the players whose work informed them.

*Colophon line (replaces L1–3):* Rules compiled and revised by PittedPanda. With thanks to Santuric, Wilhelm, Astray, Manuel, Chud, Winston, Jyace, Absolute Disgrace, Zed and Gorus.

### 9.2 Introduction (tightened, replaces L363–369) — 59 words

Dark Souls: The Board Game, Second Edition is a cooperative dungeon crawl for one to four players; each controls one character. The party must defeat a mini-boss and then a main-boss, chosen during setup. Characters who die rise *hollow*, regaining their humanity only at the *bonfire* or from an *ember*. Nameless accursed undead, seek strength, and prepare to die.

### 9.3 Trimmed chapter intros referenced above

*Returning to the Bonfire* (38 words): The *bonfire* is a safe haven in a treacherous world. Two strangers wait beside it. The Firekeeper, blindfolded and silent, strengthens the characters in exchange for *souls*. Blacksmith Andre, toiling at his forge, sells equipment and fits upgrades.

*Boss Encounters* (36 words): Boss encounters are the heart of the adventure. A boss is a single model of great health and power, with a behaviour deck in place of fixed behaviours. There are three types: mini-boss, main-boss and mega-boss. — followed by the rule: "Bosses follow the enemy rules of §8 and §9 except as stated in this chapter and §16."

## 10. OQ-01 recommendation

**Option A — replace the Second Edition Notes with the in-voice Foreword above; cut all publisher history, process notes and community appeals; move credits to the colophon.** Option B (cut with no Foreword) is Class-B compliant but loses the supersession statement ("this book governs over card text") and leaves the acknowledgements homeless.

Decision-needed rows (all OQ-01): F-001, F-002, F-003, F-004, F-005, F-006, F-046, F-047, F-048, F-055.
