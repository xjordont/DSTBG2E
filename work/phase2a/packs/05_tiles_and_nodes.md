# Drafting pack — chapter 05 (tiles_and_nodes) — manuscript chapter "TILES & NODES"

Source text: `work/phase2a/source/05_tiles_and_nodes.md` (manuscript.md lines 895–984).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 895.
- **The Basics** · present — to audit · line 897.
- **Movement** · present — to audit · line 913.
- **Node Model Limits** · present — to audit · line 917.
- **Range** · present — to audit · line 923.
- **Terrain** · present — to audit · line 927.
- **Gravestones** · present — to audit · line 929.
- **Barrels** · present — to audit · line 947.
- **Chests** · present — to audit · line 957.
- **Traps** · present — to audit · line 967.
- **(empty heading)** · ORPHAN — delete · line 983: empty H1 used as page break

## Audit findings mapped to this chapter (50)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### A-090 · omission · Blocker · REQUIRED
- Location: GAME COMPONENTS › Event cards (manuscript.md lines 659–667); SETUP steps (lines 1133, 1161, 1181); Encounter Start step 5 (line 1269); Gravestones (line 939)
- Evidence: manuscript.md:659–667, 939, 1133, 1147, 1161, 1181, 1269; no official 1E source; DS-TG-Rulebook p.19 (V2 event cards are a different, unlevelled mechanic drawn after encounters)
- Current text: Deal one face-down event card of the encounter card's level to each tile. ... Reveal the tile's event card, if not already revealed.
- Proposed fix: Either delete every reference to event cards and the Special Trap cards (components, setup steps, Encounter Start step 5, Event scrying), or add a chapter 'Event Cards': When an encounter's event card is revealed, resolve its text immediately; its effect lasts for that encounter only. When the encounter is reset, the event card is returned face-down to its tile and is resolved again the next time the encounter is fought. Event cards are not used in boss, mimic or Level 4 encounters.
- Rationale: Thirty-five cards are listed, dealt and scried, but nothing says what an event card is, what it does, or where it comes from; no supplied official or community source defines levelled event cards. The rulebook cannot stand alone until the component is defined or removed.
- Gameplay impact: A dealt component with no rules blocks every encounter setup.
- Decision needed: Y

### D-001 · hybrid · Blocker · REQUIRED
- Location: manuscript.md 661–667 (components), 1133, 1161 (setup), 1269 (encounter start), 939 (scrying)
- Evidence: No 1E event cards exist (Core p.6–7 lists none). V2 p.6/p.19 has 30 un-levelled event cards of three kinds (Immediate, Consumable, Rendezvous) drawn after completing an encounter. The manuscript lists levelled event cards plus 'Special Trap cards', deals one per tile, reveals it at encounter start and allows scrying it, but contains no rule stating what an event card does.
- Current text: 10x Level 1 event cards / 10x Level 2 event cards / 10x Level 3 event cards / 5x Special Trap cards … Deal one face-down event card of the encounter card's level to each tile … Reveal the tile's event card, if not already revealed.
- Proposed fix: Either (a) add a section 'Event Cards' defining the card anatomy, when the card's text applies, and how it is discarded or reset when the characters rest; or (b) delete every reference to event cards (components, setup steps 3 and 7, encounter start step 5, event scrying).
- Rationale: A V2-style component has been grafted onto 1E tiles with no mechanic attached; the halves are not reconciled because the V2 event mechanic (drawn after an encounter, tied to the encounter track) cannot operate in the manuscript's tile dungeon.
- Gameplay impact: Players cannot resolve setup or encounter start as written.
- Decision needed: Y

### A-033 · undefined-state · Major · REQUIRED
- Location: PLAYER VS PLAYER (manuscript.md lines 3062–3066)
- Evidence: manuscript.md:713, 967–981, 3062–3066; DS-Core-Rules-lores.txt p.18 (trap tokens show a dodge value and damage, or are blank)
- Current text: Players place a trap token on an outermost available node after each turn. Characters that move onto a trap token may attempt to dodge. Characters that fail to dodge a trap immediately die.
- Proposed fix: After each character turn, the player who took that turn draws a random trap token from the supply and places it face-up on an unoccupied outermost node (a node touching the tile edge) that holds no terrain or trap token; if no such node exists, the token is placed on any unoccupied node. A character who moves onto or is pushed onto a trap token rolls dodge dice against the trap's dodge difficulty; a blank token has no effect and is removed. On a failed dodge the character dies.
- Rationale: Which player places the token, which token, whether it is face-up, what 'available' and 'outermost' mean, and how a trap's dodge difficulty is read are all unstated. The arena-shrinking effect is the only mechanism that ends a ranged stalemate, so it must work.
- Gameplay impact: Without this the PvP end condition can never be reached between two cautious players.
- Decision needed: N

### A-039 · undefined-state · Major · PROPOSED
- Location: GAME COMPONENTS › Main-Bosses (manuscript.md lines 509–511) vs CAMPAIGNS (lines 2398, 2500, 2660, 2934); Node Model Limits (line 921)
- Evidence: manuscript.md:509, 511, 921, 2157, 2191, 2398; DS-Core-Rules-lores.txt p.5 ('Dragon Slayer Ornstein & Executioner Smough' is one main boss), p.21
- Current text: Dragon Slayer Ornstein (Core) / Executioner Smough (Core) ... Ornstein & Smough (main-boss)
- Proposed fix: Multiple-boss encounters: When a boss encounter contains two bosses, each boss has its own behaviour deck, health dial and heat-up point. During each boss turn both bosses act, in descending threat order; if tied, the players choose. The aggro token is assessed once for both bosses. The special rules on the bosses' data cards state what happens when one of them is slain. The encounter is cleared when both bosses are slain, and a single boss treasure is awarded.
- Rationale: The component list splits the pair while every campaign lists them as one boss. The only multi-boss rule in the manuscript is the node push (921). Alternative: list the pair as one main boss and play both bosses on a single alternating sequence (boss A, character, boss B, character).
- Gameplay impact: The core set's main boss cannot be played from the text.
- Decision needed: Y

### A-043 · procedural · Major · REQUIRED
- Location: TILES & NODES › Terrain › Gravestones (manuscript.md line 943) vs BOSS ENCOUNTERS › Boss Behaviour Cards (line 2125)
- Evidence: manuscript.md:933–943, 1117, 2125; DS-Core-Rules-lores.txt p.28 step 3 (reveal one random behaviour card per gravestone at boss start)
- Current text: Boss Behaviour scrying allows the players to reveal the top card of the upcoming boss's Behaviour Deck.
- Proposed fix: The boss behaviour deck is constructed as described in Boss Behaviour Cards during Encounter Setup, when the boss's cards are placed on the boss tile, and is kept face-down there. Boss Behaviour scrying reveals the top card of that deck and returns it to the top or the bottom.
- Rationale: Scrying happens when an encounter is cleared, but the manuscript builds the boss deck only at the start of the boss encounter (2125), so there is no deck to scry. Alternative: replace Boss Behaviour scrying with the official reveal of one random behaviour card per gravestone when the boss encounter starts.
- Gameplay impact: One of the four gravestone options is unusable as written.
- Decision needed: Y

### A-082 · undefined-state · Major · REQUIRED
- Location: TILES & NODES › Terrain › Gravestones, Barrels, Chests (manuscript.md lines 931, 949, 959); Character Movement (line 1840)
- Evidence: manuscript.md:931, 949, 951, 959, 1670–1678, 1840, 2175; DS-Core-Rules-lores.txt p.17 ('Gravestones block movement')
- Current text: Models cannot walk, run, dodge, or be pushed into nodes containing a gravestone. / Models cannot walk or run into nodes containing barrels. / Models cannot move, dodge, or be pushed into nodes containing a chest.
- Proposed fix: No model, including enemies and bosses, may move, leap, dodge or be pushed into a node containing a gravestone or a chest. No model may walk, run, shift or move into a node containing an intact barrel; a model that dodges or is pushed into such a node destroys the barrel and the token is removed.
- Rationale: Enemy movement is 'move', which is not in the gravestone or barrel lists; whether enemies and leaping bosses are blocked by terrain is unstated.
- Gameplay impact: Enemy pathing around terrain is decided every encounter.
- Decision needed: N

### A-083 · omission · Major · REQUIRED
- Location: TILES & NODES › Terrain › Traps (manuscript.md lines 967–981)
- Evidence: manuscript.md:713, 967–981, 3064; DS-Core-Rules-lores.txt p.18 (trap tokens: blank or damage; dodge or suffer; cannot be blocked; no effect on enemies)
- Current text: When a character is pushed onto or moves into a node containing a face-down trap token, flip the token face-up and resolve its effect on all models on that node.
- Proposed fix: A trap token shows either nothing (blank) or a dodge difficulty and a damage value. When a trap token is revealed, each character on that node must either suffer the damage or attempt to dodge it as an attack with that dodge difficulty; trap damage is not reduced by block or resist. A blank token has no effect. Enemy models on the node suffer the trap's damage without rolling. A revealed trap does not trigger again until the encounter is reset.
- Rationale: What a trap token shows and how it is resolved is never described; 'resolve its effect on all models' extends traps to enemies, which the official rule forbids, so the intent must be stated. Alternative: traps have no effect on enemies.
- Gameplay impact: Traps appear on roughly a third of encounter cards.
- Decision needed: Y

### A-122 · omission · Major · REQUIRED
- Location: BOSS ENCOUNTERS (manuscript.md lines 2061–2151) — boss encounter start
- Evidence: manuscript.md:909–911, 1265, 2131, 2165; DS-Core-Rules-lores.txt p.28 ('Then place the Aggro token on one of the characters, and place the boss model on the Mini Boss Spawn node'); DS-BDK-Rules-web.txt p.12 ('front arc facing the centre')
- Current text: Bosses always directly face an adjacent node.
- Proposed fix: At the start of a boss encounter, place the characters on the entry nodes beside the fog gate doorway and the boss on its spawn node with the centre of its front arc facing the adjacent node closest to the entry nodes.
- Rationale: The boss's initial facing determines which arcs are weak and which characters are in range; no rule sets it, and the chapter never states the placement step at all.
- Gameplay impact: First boss turn of every boss fight.
- Decision needed: N

### C-019 · hedge · Major · REQUIRED
- Location: L765; L793; L979; L1131; L1159; L1201; L1880; L1963; L2065; L2169
- Evidence: 10 'should' in procedural rules, e.g. L1131 'Encounter levels should increase from the tile adjacent to The Bonfire tile'; L2065 'the fog gate tile should be removed... and placed on the bonfire tile'; L1880 'the character should mark the equipped item with a red damage cube'; L765 'players should not interact with their character's inventory cards'
- Current text: should
- Proposed fix: must / imperative: 'Encounter levels must increase from the tile adjacent to the bonfire tile towards the mini-boss tile.' / 'Move the fog gate token from the boss tile's entrance to the bonfire tile.' / 'Mark the equipped card with a red damage cube.' / 'During an encounter a character may not access their inventory.' Full list in C_report.md Task 2.
- Rationale: These are mandatory steps; 'should' makes them optional.
- Gameplay impact: Setup order, fog-gate shortcut, inventory access and scaling marker become mandatory as intended
- Decision needed: N

### C-048 · terminology · Major · REQUIRED
- Location: L1393; L805; L891; L919; L2239; L989; L1095
- Evidence: 'Successfully defeated invaders provide additional *souls* per player' (1393) vs Soul Reward Table 'per character' (1411); 'when that player discards an ember card' (805); 'stored in a player's inventory' (891); 'characters must choose a friendly model to push' (919 - a decision); 'If a player character leaves the characters' (2239). Note L989 'character dashboard(s)' and L1095 'character model(s)' allow one player to control several characters.
- Current text: per player / that player / player's inventory / characters must choose
- Proposed fix: Rule of use: PLAYERS decide, agree, choose and roll; CHARACTERS act, hold tokens, own cards and inventories, gain souls and die; MODELS occupy nodes, move and are pushed. L1393 -> 'per character'; L805 -> 'when that character discards'; L891 -> 'a character's inventory'; L919 -> 'the players must choose a friendly model to push'; L2239 -> 'If a player leaves, remove their character...'
- Rationale: When one player controls two characters, 'per player' and 'per character' pay different soul rewards.
- Gameplay impact: Soul rewards for invaders in 1-2 player games
- Decision needed: N

### C-086 · cross-ref · Major · REQUIRED
- Location: L931; L949; L959; L1840
- Evidence: Terrain rules differ between §Terrain and §Character Movement: Gravestones 'cannot *walk*, *run*, *dodge*, or be pushed' (931); Barrels 'cannot *walk* or *run*' (949) and 'may be pushed or *dodge*' (951); Chests 'cannot move, dodge, or be pushed' (959); Character Movement: 'not permitted to *walk, run,* or *shift* to a node containing a barrel' and 'pushed or *dodge* into a node with a barrel' (1840). *Shift* is never mentioned in §Terrain.
- Current text: (four different verb sets)
- Proposed fix: Define 'move' once as 'walk, run or shift' and use it in every terrain rule: Gravestone/Chest: 'Models may not move, dodge or be pushed into this node.' Barrel: 'Models may not move into this node; a model that dodges or is pushed into it destroys the barrel.' Then L1840 cites §Terrain.
- Rationale: Same rule stated twice with different verb lists.
- Gameplay impact: Whether a character may *shift* onto a gravestone or chest
- Decision needed: N

### C-087 · cross-ref · Major · REQUIRED
- Location: L963; L1461; L1479; L2043
- Evidence: Chest treasure tie-break: 'If they cannot decide, the treasure should be awarded to a randomly selected character' (963) vs 'If the players cannot decide, the treasure will be awarded to the character who ended the encounter with the *aggro* token' (1461, 1479); mimic chest decision deadlock 'the character with the *aggro* token makes the final decision' (2043)
- Current text: randomly selected character (963)
- Proposed fix: State the tie-break once (recommended: aggro-token holder) in §Treasure Rewards and have §Chests cite it.
- Rationale: Two sections give different resolutions for the same deadlock.
- Gameplay impact: Who receives contested treasure
- Decision needed: Y

### C-119 · voice · Major · REQUIRED
- Location: L1205-1253; L1299-1399; L1445-1479; L1935-1949; L859-887; L931-981; L1604-1658; L2243-2293; L2314-2322; L3040-3094
- Evidence: Rules stated as bullet fragments: Death & Hollowing, Embering, Sparks (1205-1253); Encounter Resolution/Recovery, Souls (1299-1399); Treasure Rewards (1445-1479); Shop Rules (1935-1949); Spells (859-887); Terrain (931-981); Conditions (1604-1658); campaign Soul/Treasure Rewards and Shop (2243-2322); the whole PLAYER VS PLAYER chapter (3040-3094) is 27 bullets with no sentence structure
- Current text: - Encounters are *failed* if either all characters die.
- Proposed fix: Policy: PROCEDURES (setup, turn sequence, defence rolls, encounter start, resting, transposition) = numbered steps; DEFINITIONS and component anatomies (dashboard parts, data-card fields, condition effects, terrain) = bulleted lists of complete sentences; RULES (everything else) = short declarative paragraphs in 'When [trigger], [subject] must/may [action].' form. Rewrite PvP as prose plus a dodge table.
- Rationale: Fragments omit the trigger and subject that lawbook syntax requires ('Encounters are failed if either all characters die' has a dangling 'either').
- Gameplay impact: None
- Decision needed: Y

### D-009 · dropped-rule · Major · REQUIRED
- Location: manuscript.md 975 (Traps)
- Evidence: Core p.18: on revealing a trap the character 'must suffer the damage or attempt to dodge'; trap damage cannot be blocked; traps have no effect on enemies and cannot be triggered by them; a trap triggers once per encounter. V2 p.12: defence roll with dodge dice only. The manuscript says only 'resolve its effect on all models on that node', which both omits the resolution procedure and implies enemies are affected.
- Current text: When a character is pushed onto or moves into a node containing a face-down trap token, flip the token face-up and resolve its effect on all models on that node.
- Proposed fix: When a character moves or is pushed onto a node containing a face-down trap token, flip the token. A blank token has no effect. Otherwise each character on that node either suffers the damage shown or attempts to dodge against the dodge difficulty shown; trap damage cannot be blocked or resisted. Enemies are not affected by traps and do not trigger them. A face-up trap token has no further effect during that encounter.
- Rationale: Restores the official resolution; the manuscript's 'all models' wording is the only part that needs a decision (whether enemies suffer traps).
- Gameplay impact: Trapped encounters are unplayable without a resolution rule.
- Decision needed: Y

### F-086 · register-shift · Major · CLEAN-UP
- Location: L919, L1461, L1479, L2043, L1245 vs L2233, L1201, L1107
- Evidence: Actor shifts between 'players' and 'characters' for the same kind of decision: 'the players must push one of the three models… characters must choose a friendly model' (L919); 'Players decide which character should receive' (L1461) vs 'Characters must collectively decide' (L2043); 'Players begin sparks equal to' (L1245) vs 'The characters start a campaign with the same number of sparks' (L2233).
- Current text: Multiple models can share the same node… the players must push one of the three models already on the node. characters must choose a friendly model to push…
- Proposed fix: Apply the actor policy (Voice Guide §3): characters act in the game world (move, attack, spend, die); players make rules decisions where the game asks for a human choice; 'the party' for a collective decision. E.g. L919: 'If a fourth model enters a node, the party chooses a friendly model to push; an enemy pushes another enemy if able.'
- Rationale: Clarity of who acts; also removes the lower-case sentence starts ('characters must…' L919, L1931, L2069, L2155, L2185, L2207).
- Gameplay impact: none
- Decision needed: N

### F-089 · tone · Major · CLEAN-UP
- Location: L765, L979, L1131, L1159, L1201, L1461, L1479, L1666, L1880, L2065, L2169, L2596 ff.
- Evidence: 'should' used as a rule modal: 'players should not interact with their character's inventory cards' (L765); 'Players should fill the basic nodes furthest from the tiles entry' (L979); 'Encounter levels should increase' (L1131); 'the character should mark the equipped item' (L1880); 'the fog gate tile should be removed' (L2065); 'The target character model should remain static' (L2169); 'players should add the Explorers and Characters expansions if available' (campaign headers ×9).
- Current text: Once the encounter has started players should not interact with their character's inventory cards.
- Proposed fix: Modal policy (Voice Guide §2): 'must' for obligations, 'may' for permissions, 'cannot' for prohibitions, 'is/are' for states. E.g. 'During an encounter the inventory cannot be accessed.'; 'Trap tokens are placed first on the basic nodes furthest from the entry.'; 'Encounter levels increase from the tile adjacent to the *bonfire* tile towards the boss tile.'; 'Mark the item with a red cube.'; campaign headers: 'Recommended additions: Explorers, Characters.'
- Rationale: 'should' is advisory and leaves the rule optional.
- Gameplay impact: none
- Decision needed: N

### F-090 · tone · Major · CLEAN-UP
- Location: L859, L979, L1674, L1676, L1852, L2073, L2103, L2121, L2123, L2191, L2221, L2245, L2297, L2312, L2456, L2504
- Evidence: Hedge and filler words in rules text: 'usually' (L859, L2073), 'simply' (L979, L1674, L1676, L1852, L2191), 'typically' (L2073, L2123), 'generally' (L2121), 'often' (L2103), 'largely' (L2221), 'just' (L2245, L2456, L2504), 'essentially' (L2297), 'similarly' (L2312).
- Current text: If an enemy movement icon instructs an enemy to move towards a character it already shares a node with, then it simply does not move. / Mega-boss encounters usually have a unique mega-boss encounter tile…
- Proposed fix: Delete the adverb or state the exception: 'An enemy instructed to move towards a character on its own node does not move.'; 'A mega-boss encounter uses the tile supplied with that mega-boss.'
- Rationale: No hedge words in rules.
- Gameplay impact: none
- Decision needed: N

### A-056 · terminology · Minor · CLEAN-UP
- Location: RETURNING TO THE BONFIRE › Resuming Exploration (manuscript.md line 1963); Terrain › Traps (line 977)
- Evidence: manuscript.md:977, 1317, 1337, 1963
- Current text: flip all cleared and failed encounter tiles face-down to reset them.
- Proposed fix: Reset: an encounter is reset by turning its encounter card face-down and setting aside any enemy models; terrain, trap and chest tokens remain in place. Replace 'encounter tiles' with 'encounter cards' at line 1963.
- Rationale: Tiles are double-sided boards; flipping them would change the map. 'Reset' is used four times without a definition.
- Gameplay impact: Cosmetic but a literal reading flips the map.
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

### A-084 · terminology · Minor · CLEAN-UP
- Location: TILES & NODES › Terrain › Traps (manuscript.md line 971)
- Evidence: manuscript.md:901–903, 971
- Current text: dealt out to all basic (yellow) nodes on the encounter tile
- Proposed fix: The Basics: Basic nodes are printed in yellow. Traps: ...dealt out to every basic node...
- Rationale: Colour is used as an identifier once, without being introduced where nodes are defined.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-085 · undefined-state · Minor · REQUIRED
- Location: COMBAT BASICS › Pushing (manuscript.md line 1592)
- Evidence: manuscript.md:931, 959, 1592; DS-Core-Rules-lores.txt p.21; FAQ (push: any node farther from the attacker)
- Current text: The pushed model(s) must move to the adjacent node most directly opposite of the attacking model. ... A model being pushed directly into a corner remains on the corner node.
- Proposed fix: If the node most directly opposite the attacker is not a valid node, the pushed model moves to the valid adjacent node that is farthest from the attacker, chosen by the players if several are tied. If no valid adjacent node exists, the model is not pushed.
- Rationale: Gravestones and chests forbid entry; the push rule gives no fallback except for corners.
- Gameplay impact: Occurs on most tiles with terrain.
- Decision needed: N

### A-086 · undefined-state · Minor · OPTIONAL
- Location: TILES & NODES › Node Model Limits (manuscript.md line 919); Character Movement (line 1840)
- Evidence: manuscript.md:919, 1840
- Current text: the players must push one of the three models already on the node.
- Proposed fix: A model pushed to make room moves to any valid adjacent node chosen by the players.
- Rationale: Direction and validity of the overcrowding push are unstated.
- Gameplay impact: Cosmetic.
- Decision needed: N

### C-015 · spelling · Minor · REQUIRED
- Location: L793; L849; L887; L979; L1517; L1664; L1880; L2017; L2021; L2043; L2045; L2053; L2456; L2504; L3082; L377
- Evidence: Typos: L793 'a read and a used side'; L849 'play mail', 'used up grade armour'; L887 'a characters' catalyst'; L979 'the tiles entry'; L1517 'the enemies block'; L1664 'wound token's'; L1880 'who's stats', 'its' attack options'; L2017 'starting decks deck size'; L2021 'blocked by train'; L2043 'The then are faced'; L2045 'reveal one an ambush card', 'min-boss'; L2053 'offer character's powerful rewards'; L2456/L2504 'Do no place'; L3082 'based on an the attacker attack option's'; L377 'desist in google docs'
- Current text: (see Evidence)
- Proposed fix: ready side; plate mail; used to upgrade armour; a character's catalyst; the tile's entry nodes; the enemy's block; wound tokens; whose stats; its attack options; starting deck size; blocked by terrain; They then are faced; reveal the ambush card; mini-boss; offer characters powerful rewards; Do not place; based on the attacker's attack option's; reside in Google Docs
- Rationale: Plain typographical errors; 'Do no place' and 'blocked by train' change sense.
- Gameplay impact: L2456/L2504 'Do no place' reads as a permission, not a prohibition
- Decision needed: N

### C-020 · hedge · Minor · REQUIRED
- Location: L963; L1461; L1479; L1664
- Evidence: 'the treasure should be awarded to a randomly selected character' (L963); 'Players decide which character should receive this treasure' (L1461, L1479); 'the players decide which model should go first' (L1664)
- Current text: should be awarded / should receive / should go first
- Proposed fix: is awarded / receives / takes its turn first (present indicative)
- Rationale: Decision outcomes are stated as facts, not advice.
- Gameplay impact: None (but see tie-break conflict row C-089)
- Decision needed: N

### C-030 · italics · Minor · REQUIRED
- Location: Whole body
- Evidence: Inconsistent keyword italicisation (italic/plain in rules text L361-3100): bonfire 39/79; soul 35/33; dodge 27/17; cleared 27/5; spark 25/16; ember 23/10; hollow 19/8; block 17/8; resist 15/6; aggro 14/10; luck 12/4; heroic action 11/5; attack option 10/5; threat 10/14; stamina 8/34; run 12/1; walk 8/0; shift 8/1; parry 7/0; push 2/49; heat-up 2/15; endurance bar 1/16
- Current text: *bonfire* ... the bonfire
- Proposed fix: Adopt one policy (recommended: italicise a glossary keyword at its first use in each H2 section and in headings/tables; plain thereafter) and apply it mechanically from the glossary headword list.
- Rationale: Readers cannot tell which words are defined terms; the Introduction (L381) promises every italicised term is in the glossary.
- Gameplay impact: None
- Decision needed: Y

### C-049 · terminology · Minor · CLEAN-UP
- Location: L387; L411; L729; L915ff
- Evidence: 'unique miniature' (387), 'a number of miniatures' (411) vs 'model' x140 (729 'represented by a unique model')
- Current text: miniature
- Proposed fix: model
- Rationale: One word for the physical piece; 'model' is used for all movement and node rules.
- Gameplay impact: None
- Decision needed: N

### C-051 · terminology · Minor · CLEAN-UP
- Location: L793; L797; L801; L995; L1099; L1900; L961ff
- Evidence: Tokens defined with a 'ready side' and 'used side' (793-801) but then 'flipped face-down' (793), 'face-up on each character's dashboard' (995), 'Flip ... tokens face-up' (1900); cards 'face-down' x37, 'face down' x1 (1181), 'face up' (1099)
- Current text: flip face-down (tokens); face up / face-down (mixed hyphenation)
- Proposed fix: Tokens: 'flip to the used side' / 'flip to the ready side'. Cards and tiles: 'face up' / 'face down' as predicates ('place the card face down'), hyphenated only as an attributive adjective ('a face-down card').
- Rationale: Two-sided tokens have named sides; cards do not. Hyphenation follows grammatical role.
- Gameplay impact: None
- Decision needed: N

### C-057 · terminology · Minor · CLEAN-UP
- Location: L1193; L2047; L2085; L2101; L2117; L2017; L2123; L2125; L943
- Evidence: 'heat-up' (1193, 2047, 2085, 2101, 2117); 'Heat Up' x11 (2017, 2123, 2125); 'heats-up' (2047); 'Heat-up' (2085, 2117); also 'Behaviour Deck' capitalised (943)
- Current text: Heat Up / heats-up / Heat-up / Behaviour Deck
- Proposed fix: 'heat-up' as noun/adjective ('heat-up point', 'heat-up card'); verb 'heats up'; 'behaviour deck' lower-case
- Rationale: Common nouns are lower-case; one hyphenation.
- Gameplay impact: None
- Decision needed: N

### C-059 · terminology · Minor · CLEAN-UP
- Location: L969; L1017; L1021; L1025; L1029; L1201; L2055; L2748; L1473
- Evidence: 'set-up' x8 (noun), 'setup' x21 (noun), 'set up' (1473, verb)
- Current text: set-up
- Proposed fix: Noun 'setup' (and 'Setup' in headings); verb 'set up'
- Rationale: Standard British usage distinguishes noun and phrasal verb.
- Gameplay impact: None
- Decision needed: N

### C-062 · terminology · Minor · CLEAN-UP
- Location: L1985; L2065; L1179; L903; L1265
- Evidence: 'the boss tile's entrance node' (1985); 'the boss-tile entryway' (2065); 'placed at the entrance' (1179) vs 'entry node' (903, 1265)
- Current text: entrance node / entryway / entrance
- Proposed fix: entry node
- Rationale: Defined term at L903.
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

### C-109 · punctuation · Minor · REQUIRED
- Location: L1033; L1035; L1043; L1045; L1563-1577; L3084-3094; L3182; L3184; L925
- Evidence: '=\>' used for 'greater than or equal to' (1033-1045: 'without a required statistic =\> 25'); '1 -&gt; 2' in the scaling table (1563-1577); '-\>' in the PvP list; escaped '\[25/25/0/0 Common\]' (3182, 3184); 'Range ∞ (inﬁnity)' (925)
- Current text: =\> 25; 1 -&gt; 2; -\>
- Proposed fix: '25 or more' in prose (or '≥ 25' in tables only); '1 → 2' or 'becomes 2'; tables for the PvP list; '[25/25/0/0, common]'; 'Range ∞ (infinity)' with the ligature removed
- Rationale: '=>' is not the symbol for 'greater than or equal'; ASCII arrows and escaped brackets are pandoc artefacts.
- Gameplay impact: L1033-1045 as written literally means 'equals-implies 25'
- Decision needed: N

### C-110 · punctuation · Minor · REQUIRED
- Location: L921; L925
- Evidence: Typographic ligature glyphs pasted from a PDF: 'ﬁrst' (921), 'eﬀects', 'inﬁnity', 'aﬀect' (925) (U+FB01, U+FB00)
- Current text: ﬁrst / eﬀects / inﬁnity / aﬀect
- Proposed fix: first / effects / infinity / affect (plain letters)
- Rationale: Ligature code points break search, spell-check and many fonts.
- Gameplay impact: None
- Decision needed: N

### C-112 · punctuation · Minor · CLEAN-UP
- Location: L679; L895; L1199; L1203; L1710; L1766; L2161; L2201; L2237; L449; L2398
- Evidence: '&' in nine headings and in list items 'Mushroom Child & Parent' (449), 'Ornstein & Smough' (2398, 2500, 2660, 2934)
- Current text: &
- Proposed fix: 'and' in headings and prose; '&' only inside an official product or card name
- Rationale: Ampersand is a logo/label device, not prose.
- Gameplay impact: None
- Decision needed: N

### C-113 · punctuation · Minor · REQUIRED
- Location: L925; L377
- Evidence: 'Range 2 means the models can be up to two nodes apart, etc.' (925); '(layout, font, diagrams, art, etc)' (377)
- Current text: etc.
- Proposed fix: L925: 'Range N means the models may be up to N nodes apart.' L377: front matter, delete.
- Rationale: 'etc.' leaves a rule open-ended.
- Gameplay impact: None
- Decision needed: N

### C-114 · punctuation · Minor · REQUIRED
- Location: L919; L1931; L2069; L2157; L2185; L2207
- Evidence: Sentences beginning with lower-case 'characters': 'characters must choose a friendly model' (919); 'characters cannot equip weapons' (1931); 'characters can expect to die often' (2069); 'characters must take an equal number of turns' (2157); 'characters targeted by an *area* attack' (2185); 'characters within one node range' (2207)
- Current text: characters ...
- Proposed fix: Characters ...
- Rationale: Capitalise sentence starts (likely a global find-and-replace artefact).
- Gameplay impact: None
- Decision needed: N

### C-116 · punctuation · Minor · CLEAN-UP
- Location: L925; L1069; L1079; L1085; L1093; L1263; L1860; L1880; L1914; L2177; L2179; L2293; L2316; L2340; L1261
- Evidence: Numerals vs words mixed in prose: 'Range 0 / Range 1 / Range 2' (925); '3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells' (1069, 1079, 1085) vs 'two stamina cubes' (1261) and '6 stamina' (1263); 'six minus the number of characters' (1093); 'costs 0 Stamina' (1860); '5 greater' (1914); '90 degrees', '180 degrees' (2177-2179); '16 *souls*' (2293, 2316) vs 'sixteen souls' (2340). Number words in body: one x155, two x79, four x30, three x27, six x6, five x5, ten x3.
- Current text: 3 weapons ... 6 stamina ... sixteen souls ... 5 greater
- Proposed fix: Policy: words for zero to nine in running prose ('two stamina', 'three weapons'); numerals for 10 and above ('16 souls'), for every value in a table, for values with a sign or symbol ('+1', '≥ 25', '90°'), for dice counts beside icons, and for printed labels ('Level 1', 'Range 0'). Violations under this policy: 1069/1079/1085 (3, 3, 2, 2, 2 -> words), 1263 (6 -> six), 1860 (0 -> no), 1914 (5 -> five), 2340 (sixteen -> 16).
- Rationale: One policy; approximately 8 prose lines currently violate it.
- Gameplay impact: None
- Decision needed: Y

### C-123 · voice · Minor · CLEAN-UP
- Location: L979; L1596; L1674; L1676; L2157; L2191; L2207; L1963
- Evidence: Conversational filler: 'simply stop adding trap tokens' (979); 'Of course,' (1596); 'it simply does not move' (1674, 1676); 'and so-on' (2157); 'one can assume... simply move' (2191); 'it is possible for a demon to smash through multiple pillars' (2207); 'nearly ready to resume' (1963)
- Current text: simply / Of course / and so-on / one can assume / it is possible
- Proposed fix: Delete the filler; state the rule: 'the enemy does not move'; 'A demon may destroy several pillars with one attack.'
- Rationale: Terse voice.
- Gameplay impact: None
- Decision needed: N

### D-003 · hybrid · Minor · REQUIRED
- Location: manuscript.md 945 (Gravestones)
- Evidence: 1E gravestone tokens are single-sided (Core p.7, p.17). V2 p.12 gravestones have illuminated and diminished sides and are flipped after use. The manuscript adopts V2 scrying but never flips a gravestone; the sentence about not flipping is a vestige of V2.
- Current text: When the characters rest at the bonfire, gravestone tokens are not flipped from their current side or moved.
- Proposed fix: When the characters rest at the bonfire, gravestone tokens are not moved.
- Rationale: Removes a reference to a state the manuscript's gravestones never enter.
- Gameplay impact: None; clarity only.
- Decision needed: N

### D-037 · underspecified-deviation · Minor · REQUIRED
- Location: manuscript.md 964 (Chests) vs 1461 (Treasure Rewards)
- Evidence: Two tie-break rules for an undecided chest treasure: random character (964) and the aggro holder (1461).
- Current text: If they cannot decide, the treasure should be awarded to a randomly selected character. … the treasure will be awarded to the character who ended the encounter with the aggro token.
- Proposed fix: If the players cannot agree, the treasure is awarded to the character holding the aggro token.
- Rationale: One rule; the aggro version is used twice (1461, 1479).
- Gameplay impact: None.
- Decision needed: Y

### C-094 · example · Note · CLEAN-UP
- Location: L921
- Evidence: 'a node may contain one boss and three characters, for example' - consistent with 'only three models can share a node' (919) plus 'the boss does not count to the standard three model node limit' (921).
- Current text: (verified)
- Proposed fix: No change.
- Rationale: Verified.
- Gameplay impact: None
- Decision needed: N

### F-101 · copied-prose · Note · OPTIONAL
- Location: L899–901 §Tiles & Nodes › The Basics
- Evidence: Matches official text — near-verbatim (19-word run, 59%)
- Current text: All tiles have one or more doorways. Doorways allow characters to travel between tiles. / Every tile except for the bonfire tile has a number of circular symbols on it. These symbols, called nodes, are used for setup and movement…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.10. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-102 · copied-prose · Note · OPTIONAL
- Location: L903–911 §Tiles & Nodes › The Basics
- Evidence: Matches official text — verbatim (L909 100%, L911 74%)
- Current text: Basic nodes are the most common type of node… Spawn nodes are where enemy models are placed… Terrain nodes are where terrain features are placed… The mini-boss spawn node is where the mini-boss is placed at the start of the mini-boss encounter… The main-boss spawn node…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.10. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-103 · copied-prose · Note · OPTIONAL
- Location: L915 §Tiles & Nodes › Movement
- Evidence: Matches official text — close paraphrase (13-word run)
- Current text: During encounters, each model must always occupy a single node. When a character moves, they place their model on an adjacent node. An adjacent node is any node located directly next to another node…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.10. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-104 · copied-prose · Note · OPTIONAL
- Location: L919 §Tiles & Nodes › Node Model Limits
- Evidence: Matches official text — near-verbatim (35-word run)
- Current text: Multiple models can share the same node. However, only three models can share a node at the same time, regardless of how many are friendly or enemy models…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.10 (also V2 p.11). Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-105 · copied-prose · Note · OPTIONAL
- Location: L921 §Tiles & Nodes › Node Model Limits
- Evidence: Matches official text — near-verbatim (27-word run)
- Current text: The exception to this rule is that nodes also have a boss limit. Only one boss model can ever be on a node… Therefore, a node may contain one boss and three characters, for example.
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.10. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-106 · copied-prose · Note · OPTIONAL
- Location: L925 §Tiles & Nodes › Range
- Evidence: Matches official text — near-verbatim (53%)
- Current text: Attacks and effects have a maximum range that is counted from one model to another model, whether friendly or enemy. Range 0 means the models must be on the same node… Range ∞ (infinity) indicates unlimited range…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.10. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-107 · copied-prose · Note · OPTIONAL
- Location: L961 §Tiles & Nodes › Chests
- Evidence: Matches official text — paraphrase (10-word run)
- Current text: Chests always begin encounters with the closed side face-up and with one face-down treasure Card of the appropriate Tier beneath it.
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: V2 p.12. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

## Completion entries that apply (2) — approved at Gate 1

### [CMP-0012] Game Components and owning chapters — Undefined components (event cards, ambush cards, mega-boss items, Level 4 tiles, pillar tokens, strafe and track cards) — Proposed Completion [PROPOSED-SYSTEMIC for event cards]
- Read `04_completion_backlog.md` lines 929–983 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

### [CMP-0014] MIMICS / Gameplay › Treasure Rewards / Tiles & Nodes › Chests — Mimic and chest procedure reconciliation — Proposed Completion
- Read `04_completion_backlog.md` lines 1028–1060 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

