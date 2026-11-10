# Drafting pack — chapter 13 (mimics) — manuscript chapter "MIMICS"

Source text: `work/phase2a/source/13_mimics.md` (manuscript.md lines 2039–2050).

## Tracker rows (section · status · notes)

- **(chapter)** · present — defect · line 2039. Calls the expansion "Encounters" then "Explorers"; "min-boss"; "one an ambush card"; double full stop.
- **(empty heading)** · ORPHAN — delete · line 2049: empty H1 used as page break

## Audit findings mapped to this chapter (37)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### A-060 · undefined-state · Major · REQUIRED
- Location: GAMEPLAY › Treasure Rewards (manuscript.md lines 1463–1475); MIMICS (lines 2043–2047)
- Evidence: manuscript.md:1313, 1357, 1467–1475, 2043–2047; DS-Explorers-Rules-Web.txt p.12–13 (official: recover and gain souls first, then flip the ambush card)
- Current text: The characters do not recover stamina, remove damage, draw treasure, or collect souls until a decision is made.
- Proposed fix: Until the ambush card is revealed, dead characters remain dead and no character recovers stamina or damage. If the mimic is slain, resolve the cleared encounter's soul and treasure rewards and Encounter Recovery (reviving dead characters), then award the mimic's treasure. If the mimic encounter is failed, the cleared encounter's soul and treasure rewards are forfeited, the encounter card is reset and the cleared marker remains.
- Rationale: The deferred-reward rule leaves open whether the dead fight the mimic, whether the original rewards survive a mimic wipe, and when recovery happens after a mimic kill. Alternative: adopt the official order (recover and collect rewards before the ambush card).
- Gameplay impact: A mimic wipe can cost or not cost an entire encounter's rewards depending on reading.
- Decision needed: Y

### A-061 · contradiction · Major · REQUIRED
- Location: GAMEPLAY › Encounter Recovery (manuscript.md line 1347) vs MIMICS (line 2043)
- Evidence: manuscript.md:1347, 2043
- Current text: Remove one damage cube from each character. / they proceed to recover all stamina and two damage normally.
- Proposed fix: Encounter Recovery: Remove two damage cubes from each surviving character. (Align line 2043 to the same number.)
- Rationale: The two passages give different healing amounts for the same event. Alternative: one damage cube, with the mimic chapter corrected.
- Gameplay impact: Changes attrition across every encounter chain.
- Decision needed: Y

### C-018 · hedge · Major · REQUIRED
- Location: L845; L1057; L1141; L2041; L2053; L2596; L2664; L2720; L2766; L2812; L2884; L2948; L2994
- Evidence: 14 'should' in optional-content advice, e.g. L845 'Players should include all equipment cards from expansions'; L1141 'players should include only the encounter cards from the same set'; L2041 'Groups with new players should default to leaving mimics out... Experienced players should include mimics'; L2596ff 'players should add the Explorers and Characters expansions if available' (x8)
- Current text: Players should include / should add / should default to
- Proposed fix: Rewrite as permissions or labelled recommendations: 'Players may include equipment cards from every expansion they own.' / 'By default, build each encounter deck only from cards of the next boss's set.' / 'Mimics are an optional rule; the players decide during setup whether to use them.' / campaign lines: 'Recommended: Explorers and Characters expansions.' Full per-line rewrites in C_report.md Task 2.
- Rationale: 'Should' leaves it unclear whether expansions are required, optional or recommended. Lawbook voice uses must/may or a labelled 'Recommended' line.
- Gameplay impact: Which components a group must own to play a campaign
- Decision needed: Y

### C-087 · cross-ref · Major · REQUIRED
- Location: L963; L1461; L1479; L2043
- Evidence: Chest treasure tie-break: 'If they cannot decide, the treasure should be awarded to a randomly selected character' (963) vs 'If the players cannot decide, the treasure will be awarded to the character who ended the encounter with the *aggro* token' (1461, 1479); mimic chest decision deadlock 'the character with the *aggro* token makes the final decision' (2043)
- Current text: randomly selected character (963)
- Proposed fix: State the tie-break once (recommended: aggro-token holder) in §Treasure Rewards and have §Chests cite it.
- Rationale: Two sections give different resolutions for the same deadlock.
- Gameplay impact: Who receives contested treasure
- Decision needed: Y

### D-035 · underspecified-deviation · Major · REQUIRED
- Location: manuscript.md 1347 (Encounter Recovery) vs 2043 (Mimics)
- Evidence: Core p.19 and HE p.6 both restore all health after a victory; the manuscript's partial heal is original and is stated as one damage cube at 1347 but 'two damage' at 2043.
- Current text: Remove one damage cube from each character. … they proceed to recover all stamina and two damage normally.
- Proposed fix: Characters who survive to clear an encounter remove one damage cube and all stamina cubes.
- Rationale: One value must be chosen; the author decides which was playtested.
- Gameplay impact: Attrition pacing across a dungeon.
- Decision needed: Y

### F-023 · meta-commentary · Major · CLEAN-UP
- Location: L2041 §Mimics ¶1
- Evidence: Advice to groups and a scope disclaimer: 'Groups with new players should default to leaving mimics out as they can be quite punishing. Experienced players should include mimics… The following rules assume the play with the Explorers expansion set including mimics.' Also 'Encounters expansion set' vs 'Explorers expansion set'.
- Current text: Players with the Encounters expansion set available may choose whether they wish to include mimics in their game during setup. Groups with new players should default to leaving mimics out as they can be quite punishing. Experienced players should include mimics to ensure they are challenged. The following rules assume the play with the Explorers expansion set including mimics.
- Proposed fix: REWRITE-IN-VOICE: 'Mimics are an optional rule. They require the Explorers expansion. The party decides during setup whether mimics are in play.'
- Rationale: Difficulty advice is excluded; the component name must be consistent ('Explorers').
- Gameplay impact: none
- Decision needed: N

### F-086 · register-shift · Major · CLEAN-UP
- Location: L919, L1461, L1479, L2043, L1245 vs L2233, L1201, L1107
- Evidence: Actor shifts between 'players' and 'characters' for the same kind of decision: 'the players must push one of the three models… characters must choose a friendly model' (L919); 'Players decide which character should receive' (L1461) vs 'Characters must collectively decide' (L2043); 'Players begin sparks equal to' (L1245) vs 'The characters start a campaign with the same number of sparks' (L2233).
- Current text: Multiple models can share the same node… the players must push one of the three models already on the node. characters must choose a friendly model to push…
- Proposed fix: Apply the actor policy (Voice Guide §3): characters act in the game world (move, attack, spend, die); players make rules decisions where the game asks for a human choice; 'the party' for a collective decision. E.g. L919: 'If a fourth model enters a node, the party chooses a friendly model to push; an enemy pushes another enemy if able.'
- Rationale: Clarity of who acts; also removes the lower-case sentence starts ('characters must…' L919, L1931, L2069, L2155, L2185, L2207).
- Gameplay impact: none
- Decision needed: N

### A-044 · omission · Minor · OPTIONAL
- Location: MIMICS (manuscript.md line 2047); SUMMONS › Invaders (line 2017)
- Evidence: manuscript.md:2017, 2047, 2127–2151; DS-Explorers-Rules-Web.txt p.11; DS-Phantoms-Rules-lores.txt p.13 (no arc markings)
- Current text: Refer to 'Boss Encounter' rules for more details on how to manage the mimic's behaviour cards.
- Proposed fix: Mimics, invaders and phantoms have no arcs. The boss arc movement rules and the weak-arc black die do not apply to them.
- Rationale: The mimic chapter defers to boss rules wholesale; their models have no arc bases.
- Gameplay impact: Avoids players inventing arcs for the mimic.
- Decision needed: N

### A-058 · contradiction · Minor · REQUIRED
- Location: GAMEPLAY › Treasure Rewards (manuscript.md line 1471) vs Terrain › Chests (line 961) and Encounter Start step 7 (line 1273)
- Evidence: manuscript.md:961, 1273, 1459, 1471, 2045
- Current text: If the ambush card shows treasure, they collect one treasure card from the appropriate tier treasure deck.
- Proposed fix: If the ambush card shows treasure, reveal the treasure card placed beneath the chest token and award it as for an ordinary chest.
- Rationale: Chests carry a pre-placed card (961, 1273, 1459); the mimic branch draws a fresh one instead, leaving the pre-placed card unresolved.
- Gameplay impact: Small duplication of treasure when mimics are used.
- Decision needed: N

### A-059 · contradiction · Minor · REQUIRED
- Location: Terrain › Chests (manuscript.md line 963) vs Treasure Rewards (lines 1465–1469) and MIMICS (line 2043)
- Evidence: manuscript.md:963, 1465, 1469, 2043
- Current text: the players must flip the chest permanently to its open side / If any surviving character wishes to open a chest after an encounter ends, they must reveal the ambush card / If the characters cannot agree, the character with the aggro token makes the final decision.
- Proposed fix: Without mimics, a chest is opened automatically when the encounter is cleared. With mimics, the surviving characters decide collectively whether to open the chest; if they cannot agree, the character holding the aggro token decides.
- Rationale: Three passages give three decision rules (automatic; any single character; collective with aggro tie-break).
- Gameplay impact: Table disputes about who may force a mimic check.
- Decision needed: N

### A-063 · omission · Minor · REQUIRED
- Location: GAMEPLAY › Encounters (manuscript.md lines 1255–1341); MIMICS (line 2043)
- Evidence: manuscript.md:1255–1341, 1890, 2043
- Current text: The then are faced with the typical option of continuing onto the next encounter or returning to rest at the bonfire for the cost of one spark.
- Proposed fix: After an encounter is cleared, the characters choose either to continue to an adjacent tile or to return to the bonfire tile and rest, spending one spark.
- Rationale: The 'typical option' is referred to only inside the Mimics chapter; the Encounters chapter never states that a voluntary return is possible between encounters.
- Gameplay impact: The core exploration decision is undocumented in the chapter that owns it.
- Decision needed: N

### A-092 · omission · Minor · CLEAN-UP
- Location: GAME COMPONENTS › Cards (manuscript.md lines 631–667)
- Evidence: manuscript.md:631–667, 1137, 2045; DS-Explorers-Rules-Web.txt p.4 (5x Mimic Ambush Cards); DS-Phantoms-Rules-lores.txt p.5 (invader tokens)
- Current text: (no entry)
- Proposed fix: Add to Cards: 5x Ambush cards (Explorers). Add to Tokens: 6x Standard invader tokens, 6x Advanced invader tokens, 3x Blank invader tokens (Phantoms).
- Rationale: Ambush cards and invader tokens are used by the rules but absent from the component list.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-101 · terminology · Minor · CLEAN-UP
- Location: MIMICS (manuscript.md line 2041)
- Evidence: manuscript.md:2041, 443
- Current text: Players with the Encounters expansion set available may choose whether they wish to include mimics
- Proposed fix: Players with the Explorers expansion may choose whether to include mimics.
- Rationale: Wrong expansion name in the first sentence; the second sentence names it correctly.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-102 · contradiction · Minor · REQUIRED
- Location: CAMPAIGNS › A Hollow Pursuit Section Two (manuscript.md line 2748)
- Evidence: manuscript.md:2748, 2043–2047; DS-Explorers-Rules-Web.txt p.15 ('Do not place an Ambush card beside this tile; the chest is automatically a mimic. The party proceeds to Section 3 when the mimic is defeated')
- Current text: Add Voracious Mimic during encounter set-up..
- Proposed fix: Gallery of the Hidden Warrior: do not place an ambush card beside this tile; the chest is a Voracious Mimic. The section is completed when the mimic is slain.
- Rationale: 'During encounter set-up' places the mimic as an ordinary enemy, which contradicts the manuscript's own post-clear mimic procedure.
- Gameplay impact: Section progression depends on it.
- Decision needed: N

### B-035 · balance · Minor · PROPOSED
- Location: L2047-2049 (Mimics) with L1455-1463 (Treasure Rewards, mimic ambush)
- Evidence: Characters 'do not recover stamina, remove damage ... until a decision is made' and then fight the mimic (Hungry Mimic health 18, heat-up 8, deck 4; Explorers text) from their end-of-encounter nodes with the stamina and damage they carry. After a 4-character scaled encounter this is typically 4-6 stamina and 2-4 damage already on an 8-box bar; the mimic acts first and needs about six activations to kill with starting weapons.
- Current text: Characters remain on the nodes they occupied at the end of the encounter containing the chest. The mimic will take its turn first.
- Proposed fix: "Characters remain on the nodes they occupied at the end of the encounter containing the chest and remove all stamina cubes, but no damage cubes, before the mimic takes its first turn."
- Rationale: Keeps the ambush dangerous (damage carries over) without starting the fight with characters unable to act.
- Gameplay impact: Mimic fights begin with full stamina; expected character deaths in the first mimic activation fall sharply at 3-4 players.
- Decision needed: N

### C-015 · spelling · Minor · REQUIRED
- Location: L793; L849; L887; L979; L1517; L1664; L1880; L2017; L2021; L2043; L2045; L2053; L2456; L2504; L3082; L377
- Evidence: Typos: L793 'a read and a used side'; L849 'play mail', 'used up grade armour'; L887 'a characters' catalyst'; L979 'the tiles entry'; L1517 'the enemies block'; L1664 'wound token's'; L1880 'who's stats', 'its' attack options'; L2017 'starting decks deck size'; L2021 'blocked by train'; L2043 'The then are faced'; L2045 'reveal one an ambush card', 'min-boss'; L2053 'offer character's powerful rewards'; L2456/L2504 'Do no place'; L3082 'based on an the attacker attack option's'; L377 'desist in google docs'
- Current text: (see Evidence)
- Proposed fix: ready side; plate mail; used to upgrade armour; a character's catalyst; the tile's entry nodes; the enemy's block; wound tokens; whose stats; its attack options; starting deck size; blocked by terrain; They then are faced; reveal the ambush card; mini-boss; offer characters powerful rewards; Do not place; based on the attacker's attack option's; reside in Google Docs
- Rationale: Plain typographical errors; 'Do no place' and 'blocked by train' change sense.
- Gameplay impact: L2456/L2504 'Do no place' reads as a permission, not a prohibition
- Decision needed: N

### C-027 · italics · Minor · REQUIRED
- Location: L793; L1369; L1445; L1776; L1840; L1890; L1906; L1963; L2043; L2047; L2099; L2185; L2195
- Evidence: Punctuation inside italics: '*heroic actions, luck, and estus flask.*' (793); '*failed:*' (1369); '*cleared.*' (1445); '*Push, area-of-effect,*' (1776); '*dodge,*' and '*walk, run,*' (1840); '*hollow.*' (1890, 1906); '*failed),*' (1963); '*spark.*' (2043); '*cleared.*.' (2047); '*threat, block,*' (2099); '*, resist,*' (2185); '*embered.*' (2195)
- Current text: *cleared.* etc.
- Proposed fix: Italicise the term only; punctuation outside: '*cleared*.' - and italicise each term separately in lists: '*walk*, *run*,'
- Rationale: Keyword italics must not include punctuation or spaces; it breaks glossary linking and search.
- Gameplay impact: None
- Decision needed: N

### C-030 · italics · Minor · REQUIRED
- Location: Whole body
- Evidence: Inconsistent keyword italicisation (italic/plain in rules text L361-3100): bonfire 39/79; soul 35/33; dodge 27/17; cleared 27/5; spark 25/16; ember 23/10; hollow 19/8; block 17/8; resist 15/6; aggro 14/10; luck 12/4; heroic action 11/5; attack option 10/5; threat 10/14; stamina 8/34; run 12/1; walk 8/0; shift 8/1; parry 7/0; push 2/49; heat-up 2/15; endurance bar 1/16
- Current text: *bonfire* ... the bonfire
- Proposed fix: Adopt one policy (recommended: italicise a glossary keyword at its first use in each H2 section and in headings/tables; plain thereafter) and apply it mechanically from the glossary headword list.
- Rationale: Readers cannot tell which words are defined terms; the Introduction (L381) promises every italicised term is in the glossary.
- Gameplay impact: None
- Decision needed: Y

### C-040 · terminology · Minor · REQUIRED
- Location: L2041
- Evidence: 'Players with the Encounters expansion set available... The following rules assume the play with the Explorers expansion set'
- Current text: Encounters expansion
- Proposed fix: Explorers expansion
- Rationale: Wrong expansion name in consecutive sentences; mimics ship in Explorers (L443).
- Gameplay impact: Players look for a non-existent product
- Decision needed: N

### C-057 · terminology · Minor · CLEAN-UP
- Location: L1193; L2047; L2085; L2101; L2117; L2017; L2123; L2125; L943
- Evidence: 'heat-up' (1193, 2047, 2085, 2101, 2117); 'Heat Up' x11 (2017, 2123, 2125); 'heats-up' (2047); 'Heat-up' (2085, 2117); also 'Behaviour Deck' capitalised (943)
- Current text: Heat Up / heats-up / Heat-up / Behaviour Deck
- Proposed fix: 'heat-up' as noun/adjective ('heat-up point', 'heat-up card'); verb 'heats up'; 'behaviour deck' lower-case
- Rationale: Common nouns are lower-case; one hyphenation.
- Gameplay impact: None
- Decision needed: N

### C-082 · cross-ref · Minor · REQUIRED
- Location: L2047
- Evidence: 'Refer to "**Boss Encounter**" rules for more details on how to manage the mimic's behaviour cards' - no heading has that exact title; the relevant sections are 'Boss Behaviour Cards' (2107) and 'Boss Turn Overview' (2155)
- Current text: Refer to "Boss Encounter" rules
- Proposed fix: '(see §Boss Behaviour Cards and §Boss Turn Overview)'
- Rationale: Cross-reference must name an existing heading.
- Gameplay impact: None
- Decision needed: N

### C-084 · cross-ref · Minor · CLEAN-UP
- Location: L837; L839; L841; L891; L1057; L1165; L1475; L1485; L1760; L1852; L2045; L2069; L2077; L2099; L2105; L2163; L2195; L2197; L2289; L2297; L2312
- Evidence: 21 prose cross-references resolved correctly but informally: 'explained in detail later on in the section title "Character Attacks"' (837, 'title' for 'titled'); 'section titled "Enemy Attacks"' (839); 'described later in more detail' (841); 'aforementioned effects' (891); 'as above' (1057, 1760); 'as previously described' (1165, 2195); 'later in these rules' (1475); 'detailed later' (1485); 'explained above/previously' (1852); 'per normal treasure chest rules' (2045); 'as described previously' (2069); 'will follow' (2077); 'previously described' (2099, 2163); 'as detailed during the setup chapter' (2105); 'as described earlier' (2197); 'as in the basic rules' (2289, 2297, 2312)
- Current text: (see Evidence)
- Proposed fix: Convert every one to the form '(see §N.N Heading)' once section numbers exist; drop 'later/earlier/previously/aforementioned'. Resolution table in C_report.md Task 6.
- Rationale: Positional words break when sections move; numbered references do not.
- Gameplay impact: None
- Decision needed: N

### C-097 · example · Minor · CLEAN-UP
- Location: L2017; L2047; L2125
- Evidence: Heat-up mechanic worded three ways: invader 'add an unused invader behaviour card to the behaviour deck and shuffle' (2017); mimic 'just shuffles in one unused normal behaviour card when it heats-up' (2047); boss 'take a random Heat Up behaviour card and shuffle it into the boss behaviour deck' (2125)
- Current text: (three wordings)
- Proposed fix: State the boss rule once in §Boss Behaviour Cards; invader and mimic sections: 'When the invader/mimic heats up, shuffle one unused normal behaviour card into its behaviour deck (it has no heat-up cards).'
- Rationale: Parallel mechanics should use parallel wording.
- Gameplay impact: None
- Decision needed: N

### C-098 · heading · Minor · REQUIRED
- Location: L893; L983; L1059; L1441; L1842; L1882; L1910; L1925; L1959; L1965; L2049; L2059; L2215; L2308; L2324; L2336; L2400; L3036; L3096; L3100
- Evidence: 20 empty headings ('# ', '## ', '### ') used as page breaks
- Current text: #  (empty)
- Proposed fix: Delete all 20; page breaks belong to layout, not structure.
- Rationale: Empty headings produce blank TOC entries and broken numbering.
- Gameplay impact: None
- Decision needed: N

### C-104 · heading · Minor · CLEAN-UP
- Location: L2350; L1662; L679-2237 (9 headings); L3038; L3098; L1967
- Evidence: '# CAMPAIGNS' (2350) jumps to H3 with no H2; '## Overview' (1662) is generic; '&' in nine headings (679, 895, 1199, 1203, 1710, 1766, 2161, 2201, 2237); '# PLAYER VS PLAYER' (3038) vs 'Target versus Hit' (1483); '# F.A.Q.' (3098); '# SUMMONS' (1967) contains Invaders
- Current text: CAMPAIGNS > ### ; Overview; Tokens & Terrain Elements; PLAYER VS PLAYER; F.A.Q.; SUMMONS
- Proposed fix: Promote campaign headings to H2; 'Enemy Turn Overview'; 'and' for '&' in headings; 'PLAYER VERSUS PLAYER (PvP)'; 'FAQ'; 'PHANTOMS'
- Rationale: Consistent hierarchy and wording.
- Gameplay impact: None
- Decision needed: N

### C-106 · punctuation · Minor · REQUIRED
- Location: L793; L2221; L2748; L2047
- Evidence: Double full stops: 'at the start of the game..' (793); 'at least a few times..' (2221); 'during encounter set-up..' (2748); '*cleared.*.' (2047)
- Current text: ..
- Proposed fix: Single full stop.
- Rationale: Typo.
- Gameplay impact: None
- Decision needed: N

### C-111 · punctuation · Minor · CLEAN-UP
- Location: L375; L529; L805; L835; L853; L1025; L1529; L1726; L1826; L1904; L1929; L1985; L2310; L2312; L2314; L837; L839; L2047
- Evidence: Mixed quotation marks: curly apostrophe ’ x146 in the body vs straight ' in ~20 lines (e.g. L529 'Executioner's Chariot (Executioner’s Chariot)' has both forms in one line); curly double quotes “ ” at 837, 839, 2047
- Current text: ' / ’ mixed
- Proposed fix: Policy: straight quotes in the Markdown source; the typesetter converts to curly. Until then, make every line consistent (curly).
- Rationale: Mixed glyphs show in print.
- Gameplay impact: None
- Decision needed: N

### C-120 · voice · Minor · REQUIRED
- Location: L1963; L2043-2047; L2055-2057; L2065; L2125; L2340; L2348; L1592-1594
- Evidence: Procedures written as long prose paragraphs: Resuming Exploration (1963); mimic chest procedure (2043-2047); crystal lizard spawn/escape (2055-2057); fog gate (2065); behaviour deck construction (2125); bonfire ascetic (2340); transposition 'First, ... Second, ... Third, ... Fourth, ...' (2348); push resolution (1592-1594)
- Current text: First, players gather all available legendary treasure cards... Second, ... Third, ... Fourth, ...
- Proposed fix: Numbered steps, one action per step.
- Rationale: Multi-step procedures are read at the table mid-game; numbered steps are scannable.
- Gameplay impact: None
- Decision needed: N

### C-121 · voice · Minor · OPTIONAL
- Location: L1888; L1890; L2069; L2159; L2197; L2041; L2053; L1876; L1872; L1107; L1109
- Evidence: Flavour and advice inside rules paragraphs: Firekeeper/Andre description (1888); 'Sparks are the most precious resource in this game and the players must carefully weigh the timing' (1890); 'targets of their bloodlust... characters can expect to die often' (2069); 'Players can gain an advantage over a boss by memorising the order' (2159); session-break advice (2197); 'quite punishing' (2041); 'strange and glimmering reptiles' (2053); 'decidedly on the offensive' (1876); 'rapid flurry of attacks' (1872); 'if they like' (1107); 'For added challenge' (1109)
- Current text: (flavour)
- Proposed fix: Move to clearly styled sidebars/flavour boxes or cut; rules paragraphs carry rules only.
- Rationale: Mixing flavour and rules obscures what is binding.
- Gameplay impact: None
- Decision needed: Y

### C-122 · voice · Minor · CLEAN-UP
- Location: L1115; L1141; L1241; L1461; L1479; L2027; L2047; L2055; L2057; L1171; L2996
- Evidence: Future tense for rules: 'This will create a linear route' (1115); 'they would use only the encounters' (1141); 'Invaders will attempt to kill the characters' (1241); 'the treasure will be awarded' (1461, 1479); 'the invader will take many more turns' (2027); 'The mimic will take its turn first' (2047); 'the crystal lizards will respawn' (2055); 'no further crystal lizards will spawn' (2057); 'When all three section two options are complete, the players win' (2996, ok)
- Current text: will be awarded / will take / will respawn
- Proposed fix: Present indicative: 'is awarded', 'takes its turn first', 'respawn'.
- Rationale: Rules are timeless statements.
- Gameplay impact: None
- Decision needed: N

### C-124 · voice · Minor · REQUIRED
- Location: L1107; L1109; L1137; L1141; L2041; L2053; L1201; L3040
- Evidence: Optional rules are introduced inconsistently: 'if they wish... if they like' (1107); 'For added challenge the players may forgo choice' (1109); 'If playing with optional mimics for increased challenge' (1137); 'if they prefer more variety' (1141); 'may choose whether they wish to include mimics' (2041); 'as an optional game component' (2053); 'Players should agree on whether they will include a mega-boss and/or PvP' (1201); 'Decide during setup if PvP rules will be used' (3040)
- Current text: (eight phrasings)
- Proposed fix: One pattern: a boxed 'Optional rule: <name>' heading, then 'If the players choose this option during setup, ...'. List all options (random bosses, all-expansion decks, mimics, crystal lizards, mega-boss, PvP) once in §Setup.
- Rationale: Options are rules too; they need a fixed form.
- Gameplay impact: None
- Decision needed: N

### F-024 · tone · Minor · CLEAN-UP
- Location: L2043–2045 §Mimics ¶2–3
- Evidence: Flavour phrases in rules: 'leave it be out of fear of encountering a mimic'; 'to determine if the chest is a lurking mimic'; 'The then are faced with the typical option'
- Current text: Characters must collectively decide whether they wish to open the chest or leave it be out of fear of encountering a mimic… they must reveal one an *ambush* card to determine if the chest is a lurking mimic.
- Proposed fix: REWRITE-IN-VOICE: 'The party decides whether to open the chest. If the party cannot agree, the character with the *aggro* token decides. … To open the chest, reveal the *ambush* card dealt to that tile.'
- Rationale: Flavour inside a rule; 'the party' is the collective actor.
- Gameplay impact: none
- Decision needed: N

### F-051 · external-reference · Minor · CLEAN-UP
- Location: L2041 §Mimics ¶1
- Evidence: Inconsistent component name: 'Encounters expansion set' (L2041, first sentence) vs 'Explorers expansion set' (same paragraph) and '(Explorers)' in §2.
- Current text: Players with the Encounters expansion set available…
- Proposed fix: Use 'the Explorers expansion' throughout.
- Rationale: Component identification is legitimate but must use the component's name.
- Gameplay impact: none
- Decision needed: N

### F-056 · second-person · Minor · CLEAN-UP
- Location: L1475 §Gameplay › Treasure Rewards; L2047 §Mimics
- Evidence: Imperatives addressed to the reader: 'See the detailed rules on mimics later in these rules for details.'; 'Refer to "Boss Encounter" rules for more details…'
- Current text: See the detailed rules on mimics later in these rules for details. / Refer to “**Boss Encounter**” rules for more details on how to manage the mimic's behaviour cards.
- Proposed fix: Replace with parenthetical references: '(see §13)' and '(see §15.5 and §16)'.
- Rationale: 'See'/'Refer to' are reader imperatives; the convention is a parenthetical § reference.
- Gameplay impact: none
- Decision needed: N

### F-074 · prose-crossref · Minor · CLEAN-UP
- Location: L2047 §Mimics
- Evidence: Prose cross-reference: 'Refer to “Boss Encounter” rules'
- Current text: Refer to “Boss Encounter” rules
- Proposed fix: '(see §15.5 and §16)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §15.5 Boss Behaviour Cards; §16 Boss Turns (heading is 'BOSS ENCOUNTERS', not 'Boss Encounter'). Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-088 · register-shift · Minor · CLEAN-UP
- Location: L1241, L1461, L1479, L1670, L1848, L2047, L2057, L2151, L3040, L3042, L1115, L1109
- Evidence: Future tense in rules: 'Invaders will attempt to kill the characters'; 'the treasure will be awarded'; 'how an enemy model will move'; 'will instead do magical damage'; 'The mimic will take its turn first'; 'no further crystal lizards will spawn'; 'a PvP encounter will occur'; 'This will create a linear route'.
- Current text: - Invaders will attempt to kill the characters. … After each boss (mini, main, and mega) a PvP encounter will occur.
- Proposed fix: Present tense throughout: 'Invaders attack the characters.'; 'the treasure is awarded to…'; 'The mimic takes the first turn.'; 'a PvP encounter follows each boss'.
- Rationale: Tense policy: present.
- Gameplay impact: none
- Decision needed: N

### C-089 · cross-ref · Note · CLEAN-UP
- Location: L1471; L1473-1475; L2045; L2047
- Evidence: Mimic rules split between §Treasure Rewards (1463-1475) and §MIMICS (2041-2047); the two are consistent (one treasure on a treasure ambush; two treasures for killing the mimic) but §Treasure Rewards repeats five sentences of §MIMICS
- Current text: (duplicate)
- Proposed fix: Keep the full procedure in §MIMICS; reduce §Treasure Rewards to one sentence with '(see §Mimics)'.
- Rationale: Duplicated rules drift apart in later edits.
- Gameplay impact: None
- Decision needed: N

## Completion entries that apply (2) — approved at Gate 1

### [CMP-0007] Truncated and defective sentences (several chapters) — Proposed Completion
- Current state: Six sentences are cut short or carry a wrong word.
  1. Summons › Phantoms, line 1993: "Phantoms are removed from play if their health dial is reduced to or the encounter ends."
  2. Setup › Setup After the mini-boss step 11, line 1169: "Place all character models on the *bonfire* tile where they may now without spending a spark."
  3. Setup › Shop Setup › After Boss is Defeated step 2.3, line 1089: "Shuffle five random legendary treasure cards."
  4. Summons › Invader Encounter Setup step 2, line 2017: "deal a number equal to their starting decks deck size".
  5. Summons › Invader Encounter Setup step 4, line 2021: "If the central node is blocked by train".
  6. Mimics, line 2045: "they must reveal one an *ambush* card".
  Also: Summons › Phantoms step 7, line 1989, stray "i" after "behaviour deck."; steps 8 (line 1991) and Invader Combat step 4 (line 2031) say "each icon on the encounter card" where the behaviour card is meant; Soul Reward Table header, line 1412, "per characteri"; Mimics line 2047 "*cleared.*."; Game Components line 443 "1x HungryVoracious Mimic".
- Proposed completion (completed sentences, to be substituted in place):

  > 1. Phantoms are removed from play when their health dial is reduced to zero or when the encounter ends.
  >
  > 2. Place all character models on the *bonfire* tile, where they may now rest without spending a *spark*. They may visit the Firekeeper and Andre's Shop as usual after resting at the *bonfire*.
  >
  > 3. Shuffle five random legendary treasure cards into the tier two treasure deck. Return the remaining legendary treasure cards to the game box.
  >
  > 4. Shuffle the invader's behaviour cards and deal a number of them equal to the behaviour deck size on the invader's data card, face down, to create the invader behaviour deck. When the invader's health is reduced to or below its heat-up point, shuffle one unused invader behaviour card into the behaviour deck.
  >
  > 5. After the encounter card setup is complete, place the invader model on the encounter tile's central node. If the central node is blocked by terrain, place the invader model on a node adjacent to the central node, chosen by the players.
  >
  > 6. If the characters wish to open the chest, they must reveal the *ambush* card beside that encounter tile to determine whether the chest is a lurking mimic.
  >
  > Step 7 (line 1989): Each phantom turn, draw and resolve the top card of the phantom behaviour deck.
  >
  > Step 8 (line 1991) and Invader Combat step 4 (line 2031): After each icon on the behaviour card is resolved in left-to-right order, the phantom's [invader's] turn ends.
  >
  > Soul Reward Table header: "*Soul* reward per character".
  >
  > Mimics line 2047: "…and may mark the encounter *cleared*."
  >
  > Game Components line 443: "1x Hungry Mimic and 1x Voracious Mimic (Explorers)" — two data cards sharing two miniatures and one health dial.
- Design rationale: Each completion supplies the word the sentence's structure demands and that the surrounding rules confirm (zero health; rest; the tier two deck, as Legendary Treasure line 1025 already states; deck size; terrain; one ambush card). "Encounter card" in the phantom and invader turn steps is corrected to "behaviour card" because the phantom and invader rules draw from behaviour decks, not encounter cards.
- Mechanical impact: None; restores intended text.
- Follow-on changes required: None beyond substitution. Glossary (CMP-0002) and CMP-0018 reference the corrected phantom steps.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

### [CMP-0014] MIMICS / Gameplay › Treasure Rewards / Tiles & Nodes › Chests — Mimic and chest procedure reconciliation — Proposed Completion
- Current state: Three passages state the chest-and-mimic procedure with differences. Chests (line 963): undecided treasure goes to "a randomly selected character". Treasure Rewards (lines 1453–1475): undecided treasure goes to the character who ended the encounter with the aggro token; no recovery "until a decision is made"; one treasure if the ambush card shows treasure; mimic encounter set up immediately. Mimics (lines 2041–2047): the expansion is called "Encounters" then "Explorers"; the aggro holder makes the open/leave decision; after leaving the chest the characters "recover all stamina and two damage" (Encounter Recovery, line 1347, removes one damage cube); "min-boss"; killing the mimic gives two treasures and marks the encounter *cleared*; a mimic that defeats the characters is fought again "next time they complete the normal encounter"; "once the mimic has been fought once, it must be fought again at the end of the encounter until it is killed".
- Proposed completion: The Mimics chapter owns the procedure. Treasure Rewards and Chests keep one pointer each.

  Replacement for Tiles & Nodes › Chests bullet at line 963: "Upon *clearing* an encounter containing a chest, the players flip the chest to its open side and decide which character takes the revealed treasure. If they cannot decide, the character who ended the encounter with the *aggro* token takes it. When playing with mimics, see Mimics before opening a chest."

  Replacement for Treasure Rewards lines 1463–1475 (the five mimic bullets): "- If playing with mimics, a chest is opened only as the Mimics chapter describes; the encounter is not resolved until the characters have decided whether to open it."

  Replacement for the MIMICS chapter (lines 2039–2047):

  > # MIMICS
  >
  > Mimics are an optional challenge from the Explorers expansion. The players decide during setup whether to include them. Groups with new players are advised to leave mimics out; experienced groups are advised to include them. When mimics are in play, one face-down *ambush* card is dealt beside each encounter tile at setup.
  >
  > When an encounter containing an unopened chest is *cleared*, the characters do not recover at once. They remain on their nodes and decide collectively whether to open the chest. If they cannot agree, the character holding the *aggro* token decides.
  >
  > If the characters leave the chest closed, they recover as Encounter Recovery describes and collect their *soul* and treasure rewards. The chest stays closed and may be opened after a later clearing of the same encounter.
  >
  > If the characters open the chest, reveal the *ambush* card beside the tile. If it shows Treasure, the characters receive the treasure card beneath the chest and assign it as the Chests rules describe; then they recover and collect their rewards. If it shows Mimic, a mimic encounter begins at once, before any recovery or reward.
  >
  > The mimic encounter is a mini-boss encounter fought on the same tile. Use the Hungry Mimic's data and behaviour cards if the mini-boss has not yet been defeated, and the Voracious Mimic's if it has. Replace the chest token with the mimic model on the chest's node. The characters keep their damage cubes, stamina cubes and condition tokens and remain on the nodes they occupied. Build the mimic's behaviour deck from random behaviour cards equal to its deck size. The mimic takes the first turn, then the characters and the mimic alternate as in any boss encounter. Mimics have no arcs and no heat-up cards; see Boss Special Rules › Explorers Expansion.
  >
  > If the mimic is slain, the characters receive two treasure cards of the current tier in place of the chest's one, assign them as the Chests rules describe, recover as Encounter Recovery describes, and collect the rewards of the encounter that contained the chest. Mark that encounter *cleared*. The mimic does not return; the chest's node is a basic node for the rest of the game.
  >
  > If every character dies, the mimic encounter is *failed*: the characters drop their *souls*, the encounter card is turned face down and the characters must rest at the *bonfire*. The mimic returns to its chest. Each later time the characters *clear* that encounter, they may again choose to open the chest, and the mimic must be fought again until it is slain.

- Design rationale: One procedure, in one chapter, with the other two passages reduced to pointers so no second version can drift. The aggro holder is chosen as tie-breaker in every case because Treasure Rewards and Mimics both already use it and a random draw adds a step. Recovery after leaving the chest follows Encounter Recovery (one damage cube) rather than the Mimics chapter's "two damage". The mimic replacing the chest token on its node follows the Explorers booklet ("the mimic returns to its terrain node") and gives the mimic a defined starting node, which the manuscript never states. "Each later time… they may again choose" resolves the manuscript's two incompatible sentences (fought "next time they complete the encounter" versus "must be fought again until it is killed") in favour of choice, since the characters can always decline to open the chest.
- Mechanical impact: Recovery after declining a chest is one damage cube, not two. The mimic starts on the chest node (previously undefined). Everything else is unchanged.
- Follow-on changes required: Delete the empty heading at line 2049. Glossary entries Chest, Mimic, Ambush card (CMP-0002) align. CMP-0005 holds the mimic's special rules.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

