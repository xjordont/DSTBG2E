# Drafting pack — chapter 15 (boss_encounters) — manuscript chapter "BOSS ENCOUNTERS"

Source text: `work/phase2a/source/15_boss_encounters.md` (manuscript.md lines 2061–2152).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 2061.
- **The Fog Gate** · present — to audit · line 2063.
- **Boss Encounter Overview** · present — to audit · line 2067.
- **Boss Encounter Tiles** · present — to audit · line 2071.
- **Boss Data Cards** · present — to audit · line 2075.
- **Boss Behaviour Cards** · present — to audit · line 2107.
- **Boss Arcs and Defence** · present — to audit · line 2127.
- **Character Arc Movement** · present — to audit · line 2133.
- **Attacking Bosses and Weak Arcs** · present — to audit · line 2147.

## Audit findings mapped to this chapter (54)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### A-043 · procedural · Major · REQUIRED
- Location: TILES & NODES › Terrain › Gravestones (manuscript.md line 943) vs BOSS ENCOUNTERS › Boss Behaviour Cards (line 2125)
- Evidence: manuscript.md:933–943, 1117, 2125; DS-Core-Rules-lores.txt p.28 step 3 (reveal one random behaviour card per gravestone at boss start)
- Current text: Boss Behaviour scrying allows the players to reveal the top card of the upcoming boss's Behaviour Deck.
- Proposed fix: The boss behaviour deck is constructed as described in Boss Behaviour Cards during Encounter Setup, when the boss's cards are placed on the boss tile, and is kept face-down there. Boss Behaviour scrying reveals the top card of that deck and returns it to the top or the bottom.
- Rationale: Scrying happens when an encounter is cleared, but the manuscript builds the boss deck only at the start of the boss encounter (2125), so there is no deck to scry. Alternative: replace Boss Behaviour scrying with the official reveal of one random behaviour card per gravestone when the boss encounter starts.
- Gameplay impact: One of the four gravestone options is unusable as written.
- Decision needed: Y

### A-054 · contradiction · Major · REQUIRED
- Location: RETURNING TO THE BONFIRE › Resuming Exploration (manuscript.md line 1963) vs Encounter Start step 2 (line 1261), Encounter Resolution (line 1319) and The Fog Gate (line 2065)
- Evidence: manuscript.md:1261, 1317–1319, 1339, 1963, 2065
- Current text: If the encounter card on the tile is face-down (cleared or failed), they must flip the card face-up and proceed with fighting the enemies of that encounter.
- Proposed fix: After the characters rest, every encounter card is face-down. When the characters enter a tile whose card is face-down, they reveal it. If the encounter is marked cleared, the characters may skip it for the stamina cost; otherwise they must fight it. The fog gate shortcut is unaffected.
- Rationale: 'Must ... proceed with fighting' contradicts the skip rule for cleared encounters (1261, 1319) and the fog gate shortcut (2065), both of which assume the party can bypass reset tiles.
- Gameplay impact: Decides whether the skip mechanic exists after the first rest.
- Decision needed: N

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

### C-036 · terminology · Major · REQUIRED
- Location: L1285; L1291; L1293; L1850
- Evidence: 'the model with the most damage tokens' (1285); 'the character who placed the most damage tokens on enemy models' (1291, 1293); 'place a number of damage tokens onto the target enemy model's base' (1850) vs 'wound token' (681, 1517, 1664, 2099) and 'damage cubes' for characters (x16)
- Current text: damage tokens
- Proposed fix: wound tokens (enemies); damage cubes (characters)
- Rationale: Two components, two names: enemies take wound tokens (L1517), characters take red damage cubes (L779). 'Damage token' is neither.
- Gameplay impact: Avoids confusion between the two damage-tracking components
- Decision needed: N

### F-027 · tone · Major · CLEAN-UP
- Location: L2069 §Boss Encounters › Boss Encounter Overview
- Evidence: Chapter intro with tone slips and a product reference: 'the bosses are the targets of their bloodlust'; 'characters can expect to die often'; 'Only with adequate preparation, astute tactics, and the favour of luck should the characters hope to fell a boss'; 'The core game does not come with mega-bosses…'
- Current text: Boss encounters are the heart of the character's adventure and the bosses are the targets of their bloodlust. Bosses are single models that are not only large in stature, but formidable opponents… characters can expect to die often at the hands of these powerful enemies. Only with adequate preparation, astute tactics, and the favour of luck should the characters hope to fell a boss… The core game does not come with mega-bosses as they are optional objectives… Boss encounters follow many of the same rules as other enemies as described previously, but there are key differences outlined as follows.
- Proposed fix: KEEP-AS-INTRO, trimmed to ≤60 words: 'Boss encounters are the heart of the adventure. A boss is a single model of great health and power, with a behaviour deck in place of fixed behaviours. There are three types: mini-boss, main-boss and mega-boss.' Then the rule: 'Bosses follow the enemy rules of §8 and §9 except as stated in this chapter and §16.'
- Rationale: 'bloodlust', 'can expect to die often' and the strategy sentence are tone slips; 'The core game does not come with mega-bosses' describes the product.
- Gameplay impact: none
- Decision needed: N

### F-032 · second-person · Major · CLEAN-UP
- Location: L2151 §Boss Encounters › Attacking Bosses and Weak Arcs
- Evidence: Reader address and strategy aside (copied Core p.28): 'Remember that a character can be in more than one arc… This makes it easier to gain the weak arc bonus, but it also means… Note that even if…'
- Current text: Remember that a character can be in more than one arc if it is on a node along the arc line. This makes it easier to gain the weak arc bonus, but it also means the character will be targeted by attacks against either arc. Note that even if a character is attacking multiple weak arcs, they gain just one black die for attacking the boss in a weak arc.
- Proposed fix: REWRITE-IN-VOICE: 'A character on a node that lies on an arc line is in both arcs: they may claim the weak-arc bonus from either, and they are targeted by attacks against either. The weak-arc bonus is one black die regardless of how many weak arcs the character is in.'
- Rationale: 'Remember that' and 'Note that' address the reader; the middle sentence is tactical commentary.
- Gameplay impact: none
- Decision needed: N

### F-050 · external-reference · Major · CLEAN-UP
- Location: L2069 §Boss Encounters › Boss Encounter Overview
- Evidence: Product-contents statement: 'The core game does not come with mega-bosses as they are optional objectives which players can attempt after defeating a main-boss should they want a more epic final battle.'
- Current text: The core game does not come with mega-bosses as they are optional objectives which players can attempt after defeating a main-boss should they want a more epic final battle.
- Proposed fix: CUT (the mega-boss option is already a rule at §6.5 Boss Selection and §7.1).
- Rationale: Describes the product line, not the game.
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

### A-036 · undefined-state · Minor · OPTIONAL
- Location: BOSS ENCOUNTERS › Character Arc Movement (manuscript.md line 2143)
- Evidence: manuscript.md:2143; DS-Core-Rules-lores.txt p.28; Dark_Souls_The_Board_Game_FAQ.txt (push by boss attack: any node farther from attacker)
- Current text: If the character is pushed off of the boss's node, they must move to the centre-most node in the boss's arc they originate from, if possible.
- Proposed fix: If a character is pushed off a boss's node, the character moves to a node adjacent to the boss's node within the same arc, chosen by the players. If no such node exists because of a wall or terrain, the character moves to any adjacent node touching that wall.
- Rationale: 'Centre-most node' is undefined (arcs are wedges with no centre node on most tiles). The manuscript deliberately keeps the same-arc rule for pushes, which the FAQ relaxed; the simpler wording keeps that choice. Alternative: adopt the FAQ ruling (any adjacent node farther from the boss).
- Gameplay impact: Frequent event in every boss fight.
- Decision needed: Y

### A-037 · undefined-state · Minor · OPTIONAL
- Location: BOSS ENCOUNTERS › Attacking Bosses and Weak Arcs (manuscript.md line 2149)
- Evidence: manuscript.md:1864, 1872, 2149–2151
- Current text: If the character is attacking a weak arc, the attack gains an additional black die.
- Proposed fix: The additional black die is rolled for each attack roll made against a weak arc, including each repetition of a Repeat attack and each riposte.
- Rationale: A Repeat option is 'that entire weapon option' used several times; whether each roll gains the die is unstated.
- Gameplay impact: Small but constant in boss fights with Repeat weapons.
- Decision needed: N

### A-042 · undefined-state · Minor · OPTIONAL
- Location: BOSS ENCOUNTERS › Boss Behaviour Cards (manuscript.md line 2125); Parry & Riposte (line 1790)
- Evidence: manuscript.md:1790, 2125, 2159
- Current text: When the boss's health is reduced to (or below) its Heat Up point, take a random Heat Up behaviour card and shuffle it into the boss behaviour deck.
- Proposed fix: If the boss heats up during its own turn (for example from a riposte), finish resolving the current behaviour card, then shuffle the Heat Up card into the remaining behaviour deck. If the behaviour deck is empty at that moment, the Heat Up card becomes the behaviour deck and the discard pile is not yet renewed.
- Rationale: A riposte can damage the boss mid-card; and the deck may be empty (all cards in the discard) when heat-up occurs.
- Gameplay impact: Edge case that arises once in most boss fights with a parrying character.
- Decision needed: N

### A-044 · omission · Minor · OPTIONAL
- Location: MIMICS (manuscript.md line 2047); SUMMONS › Invaders (line 2017)
- Evidence: manuscript.md:2017, 2047, 2127–2151; DS-Explorers-Rules-Web.txt p.11; DS-Phantoms-Rules-lores.txt p.13 (no arc markings)
- Current text: Refer to 'Boss Encounter' rules for more details on how to manage the mimic's behaviour cards.
- Proposed fix: Mimics, invaders and phantoms have no arcs. The boss arc movement rules and the weak-arc black die do not apply to them.
- Rationale: The mimic chapter defers to boss rules wholesale; their models have no arc bases.
- Gameplay impact: Avoids players inventing arcs for the mimic.
- Decision needed: N

### A-087 · undefined-state · Minor · OPTIONAL
- Location: ENEMY TURN › Dodge step 4.4 (manuscript.md line 1754)
- Evidence: manuscript.md:1754, 1840, 2145; Dark_Souls_The_Board_Game_FAQ.txt (official dodge: 'can move one node')
- Current text: The character must move to an adjacent node.
- Proposed fix: If no valid adjacent node exists, the dodging character remains on their node.
- Rationale: The mandatory dodge move (a deliberate change from the official optional move) has no fallback when terrain and node limits block every adjacent node.
- Gameplay impact: Rare.
- Decision needed: N

### A-089 · omission · Minor · REQUIRED
- Location: SETUP › Encounter tiles (manuscript.md lines 1111–1117); Setup After the mini-boss step 4 (line 1151); BOSS ENCOUNTERS › The Fog Gate (line 2065)
- Evidence: manuscript.md:719, 1111–1117, 1151, 2065; DS-Core-Rules-lores.txt p.8
- Current text: Place the fog-gate as before.
- Proposed fix: Encounter tiles step 3: Place the fog gate token on the doorway of the boss tile.
- Rationale: The fog gate is a component, is moved by The Fog Gate rule and is placed 'as before' after the mini-boss, but the initial setup never places it.
- Gameplay impact: Setup omission.
- Decision needed: N

### A-095 · inherits-official-silently · Minor · OPTIONAL
- Location: SETUP › Setup After the main-boss step 3 (manuscript.md line 1179)
- Evidence: manuscript.md:1179, 1193, 2065; DS-EC-Rules-Web.txt p.9 (fog gate placed on the mega-boss board doorway after the Level 4 encounter)
- Current text: Place the Level 4 encounter tile associated with the chosen mega-boss adjacent to The Bonfire tile with the fog-gate placed at the entrance.
- Proposed fix: Place the mega-boss board, encounter side up, adjacent to the bonfire tile. After the Level 4 encounter is cleared, flip the board to its boss side and place the fog gate token on its doorway.
- Rationale: The fog gate marks the boss entrance; at the Level 4 entrance it is meaningless and its shortcut rule (2065) would trigger on the encounter, not the boss.
- Gameplay impact: Cosmetic ordering.
- Decision needed: N

### A-119 · undefined-state · Minor · OPTIONAL
- Location: ENEMY TURN › Parry & Riposte step 5.4 (manuscript.md line 1790)
- Evidence: manuscript.md:1790, 1846, 1876, 2149
- Current text: The character may make one riposte attack out of turn against the attacker using any attack option on the weapon equipped to the right weapon slot after paying the associated stamina cost.
- Proposed fix: A riposte is an attack for all purposes (two-handed reroll, luck, weak-arc die, conditions) except that it does not count towards the limit of one attack per weapon per turn.
- Rationale: Nothing says whether the riposte consumes the weapon's attack for the character's next turn or benefits from attack modifiers.
- Gameplay impact: Arises on every successful parry.
- Decision needed: N

### C-021 · hedge · Minor · REQUIRED
- Location: L805; L1596; L2069; L2197
- Evidence: L805 'players should be aware that ember tokens enable...'; L1596 'Players should take note that only enemy behaviours that deal damage can be dodged'; L2069 'should the characters hope to fell a boss', 'should they want a more epic final battle'; L2197 'This is often a reasonable time to end a game session'
- Current text: should be aware / should take note / should the characters hope / should they want / reasonable time
- Proposed fix: Delete the advisory frame and state the rule: 'An embered character may summon a phantom and provokes invaders (see §Phantoms).' / 'Only enemy behaviours with an attack value may be dodged.' / delete flavour sentences; L2197 to a sidebar or delete.
- Rationale: Advisory and flavour sentences are not rules.
- Gameplay impact: None
- Decision needed: N

### C-027 · italics · Minor · REQUIRED
- Location: L793; L1369; L1445; L1776; L1840; L1890; L1906; L1963; L2043; L2047; L2099; L2185; L2195
- Evidence: Punctuation inside italics: '*heroic actions, luck, and estus flask.*' (793); '*failed:*' (1369); '*cleared.*' (1445); '*Push, area-of-effect,*' (1776); '*dodge,*' and '*walk, run,*' (1840); '*hollow.*' (1890, 1906); '*failed),*' (1963); '*spark.*' (2043); '*cleared.*.' (2047); '*threat, block,*' (2099); '*, resist,*' (2185); '*embered.*' (2195)
- Current text: *cleared.* etc.
- Proposed fix: Italicise the term only; punctuation outside: '*cleared*.' - and italicise each term separately in lists: '*walk*, *run*,'
- Rationale: Keyword italics must not include punctuation or spaces; it breaks glossary linking and search.
- Gameplay impact: None
- Decision needed: N

### C-028 · italics · Minor · REQUIRED
- Location: L787; L1341; L1794; L1880; L2145; L3082
- Evidence: Split or partial italics: 'stagger*ed*' x2 (787); '*C*haracters' (1341); 'block*/*resist' (1794); 'attack option*s*' (1880); 'dodge*s*' (2145); 'attack option*'s*' (3082)
- Current text: stagger*ed*
- Proposed fix: *staggered*; Characters; *block*/*resist*; *attack options*; *dodges*; *attack option*'s
- Rationale: Italicise the whole inflected word or none.
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

### C-037 · terminology · Minor · REQUIRED
- Location: L2019; L2099
- Evidence: 'Set the invader heal dial' (2019); 'health tracker dial' (2099) vs 'health dial' (1105, 1993, 2035, 2195)
- Current text: heal dial / health tracker dial
- Proposed fix: health dial
- Rationale: One component, one name (official: 'health dial').
- Gameplay impact: None
- Decision needed: N

### C-041 · terminology · Minor · CLEAN-UP
- Location: L483; L501; L523; L2073; L2366ff; L2692ff; L2716ff; L2826ff; L2996
- Evidence: mini-boss x47 / Mini-Boss x15 / Mini Boss x5 / mini boss x1 / 'mini bosses'; main-boss x31 / Main-Boss x1 / Main Boss x11; mega-boss x28 / Mega-boss x2 / Mega Boss x7 / 'mega boss' x1 (L2996)
- Current text: Mini Boss / Main Boss / Mega Boss / mini boss
- Proposed fix: mini-boss, main-boss, mega-boss (lower-case, hyphenated) in prose and campaign lists; Title Case 'Mini-Boss' only as a heading word
- Rationale: Six spellings of three terms; the campaign lists (L2692-3034) use the unhyphenated Title Case form throughout.
- Gameplay impact: None
- Decision needed: N

### C-047 · terminology · Minor · CLEAN-UP
- Location: L2115; L3082; L831; L1501; L1734
- Evidence: 'Dodge difficulty' plain capital (2115, 3082); '*Dodge*' italic capital in lists/headings (831, 1501, 1734); '*dodge*' x22 and plain 'dodge' x16 elsewhere
- Current text: Dodge
- Proposed fix: *dodge* (lower-case keyword; capital only at sentence start or in a heading)
- Rationale: Keyword case must be uniform.
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

### C-058 · terminology · Minor · CLEAN-UP
- Location: L719; L1151; L1179; L2063; L2065; L2227; L2229
- Evidence: 'Fog Gate token' (719), 'fog-gate' (1151, 1179), 'fog gate' x11, 'the fog gate tile should be removed' (2065) vs 'fog gate token' (719, 2229)
- Current text: fog-gate / Fog Gate / fog gate tile
- Proposed fix: fog gate (lower-case, no hyphen); the component is the 'fog gate token'
- Rationale: One component, one name; it is a token not a tile.
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

### C-084 · cross-ref · Minor · CLEAN-UP
- Location: L837; L839; L841; L891; L1057; L1165; L1475; L1485; L1760; L1852; L2045; L2069; L2077; L2099; L2105; L2163; L2195; L2197; L2289; L2297; L2312
- Evidence: 21 prose cross-references resolved correctly but informally: 'explained in detail later on in the section title "Character Attacks"' (837, 'title' for 'titled'); 'section titled "Enemy Attacks"' (839); 'described later in more detail' (841); 'aforementioned effects' (891); 'as above' (1057, 1760); 'as previously described' (1165, 2195); 'later in these rules' (1475); 'detailed later' (1485); 'explained above/previously' (1852); 'per normal treasure chest rules' (2045); 'as described previously' (2069); 'will follow' (2077); 'previously described' (2099, 2163); 'as detailed during the setup chapter' (2105); 'as described earlier' (2197); 'as in the basic rules' (2289, 2297, 2312)
- Current text: (see Evidence)
- Proposed fix: Convert every one to the form '(see §N.N Heading)' once section numbers exist; drop 'later/earlier/previously/aforementioned'. Resolution table in C_report.md Task 6.
- Rationale: Positional words break when sections move; numbered references do not.
- Gameplay impact: None
- Decision needed: N

### C-096 · example · Minor · CLEAN-UP
- Location: L1943; L1945; L2141; L771; L853
- Evidence: '(i.e.: Titanite Shards)' (1943), '(i.e.: gems)' (1945), '(i.e.: *Run*)' (2141) each introduce an example, not a restatement, so 'e.g.' is meant; 771 and 853 use 'i.e.,' correctly; punctuation varies ('i.e.:' vs 'i.e.,').
- Current text: i.e.:
- Proposed fix: Write out: 'for example, Titanite Shards' / 'such as gems' / 'for example by running'; and 'that is,' for the two true restatements. Avoid Latin abbreviations in rules text.
- Rationale: Misused abbreviation changes meaning (Titanite Shards are one kind of Titanite upgrade, not the definition).
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

### C-103 · heading · Minor · CLEAN-UP
- Location: L1916/L2299; L1951/L2326; L2063/L2227; L1245/L2231; L633/L1119; L543/L1969; L385/L725; L985/L2219
- Evidence: Identical heading titles in different chapters: 'Stat Tier Costs' x2, 'Shop Price Table' x2, 'The Fog Gate' x2, 'Sparks' x2, 'Encounter cards' x2, 'Phantoms' x2, 'Characters' x2, 'Setup' x2
- Current text: Stat Tier Costs (x2)
- Proposed fix: Qualify the campaign versions: 'Stat Tier Costs (Campaign)', 'Shop Price Table (Campaign)', 'The Fog Gate in Campaigns', 'Sparks in Campaigns'; rename L633 'Encounter and Event Cards', L1969 'Summons', L385 'Character Classes'
- Rationale: Duplicate titles defeat '(see §Heading)' cross-references and index entries.
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

### C-114 · punctuation · Minor · REQUIRED
- Location: L919; L1931; L2069; L2157; L2185; L2207
- Evidence: Sentences beginning with lower-case 'characters': 'characters must choose a friendly model' (919); 'characters cannot equip weapons' (1931); 'characters can expect to die often' (2069); 'characters must take an equal number of turns' (2157); 'characters targeted by an *area* attack' (2185); 'characters within one node range' (2207)
- Current text: characters ...
- Proposed fix: Characters ...
- Rationale: Capitalise sentence starts (likely a global find-and-replace artefact).
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

### D-004 · hybrid · Minor · OPTIONAL
- Location: manuscript.md 2144 (Character Arc Movement)
- Evidence: Core p.28 says a character pushed off a boss's node must remain in the same arc. FAQ p.1 overrides this: 'Any time a character is pushed by an attack, it simply needs to be moved farther from the attacking model (p. 21).' The manuscript keeps the pre-FAQ text and adds an original 'centre-most node' clause.
- Current text: If the character is pushed off of the boss's base arc, they must move to the centre-most node in the boss's arc they originate from, if possible. Otherwise, the character is pushed to any valid node in that arc.
- Proposed fix: If a character is pushed off a boss's node by an attack, the character moves to an adjacent node farther from the boss; the arc restriction does not apply. If a character is pushed off a boss's node by the boss's movement, the character moves to a node within the arc the character occupied.
- Rationale: The official FAQ ruling distinguishes attack pushes from movement pushes; the manuscript's version follows the superseded rulebook text.
- Gameplay impact: Push geometry in boss fights.
- Decision needed: Y

### F-028 · tone · Minor · CLEAN-UP
- Location: L2077 §Boss Encounters › Boss Data Cards
- Evidence: Editorial adverb: 'are noticeably lacking behaviours to dictate how they act on their turns… information about boss behaviour cards will follow.'
- Current text: Boss data cards include similar information to enemy data cards but are noticeably lacking behaviours to dictate how they act on their turns. Instead, bosses have variable behaviours determined by a special deck of behaviour cards. The specifics of boss data cards is detailed here and information about boss behaviour cards will follow.
- Proposed fix: REWRITE-IN-VOICE: 'A boss data card lists no behaviours. A boss acts according to its behaviour deck (see §15.5).' CUT the final sentence.
- Rationale: Signposting sentence ('will follow') is unnecessary once headings and § references exist.
- Gameplay impact: none
- Decision needed: N

### F-029 · tone · Minor · CLEAN-UP
- Location: L2099 §Boss Encounters › Boss Data Cards ¶
- Evidence: Aside: 'instead of using dozens of wound tokens, players track the boss's remaining health on a health tracker dial'
- Current text: Boss starting health is treated the same as well but instead of using dozens of wound tokens, players track the boss's remaining health on a health tracker dial specific to each boss.
- Proposed fix: REWRITE-IN-VOICE: 'Boss health is tracked on that boss's health dial, not with wound tokens.'
- Rationale: Terse statement; no contrast commentary.
- Gameplay impact: none
- Decision needed: N

### F-030 · tone · Minor · CLEAN-UP
- Location: L2103 §Boss Encounters › Boss Data Cards ¶
- Evidence: Hedge words: 'provides an overarching theme to the boss which often gives the boss unique powers'
- Current text: Boss special ability provides an overarching theme to the boss which often gives the boss unique powers.
- Proposed fix: REWRITE-IN-VOICE: 'The special ability is a rule unique to that boss. It applies for the whole encounter.'
- Rationale: 'often' is a hedge; 'theme' is not a rules concept.
- Gameplay impact: none
- Decision needed: N

### F-031 · tone · Minor · OPTIONAL
- Location: L2129 §Boss Encounters › Boss Arcs and Defence
- Evidence: Official-voice commentary sentence (Core p.27): 'These arcs are a key part of what makes boss encounters unique, and they add an extra layer of tactics to fighting against bosses.'
- Current text: These arcs are a key part of what makes boss encounters unique, and they add an extra layer of tactics to fighting against bosses.
- Proposed fix: CUT
- Rationale: Commentary; no rule.
- Gameplay impact: none
- Decision needed: N

### F-075 · prose-crossref · Minor · CLEAN-UP
- Location: L2069 §Boss Encounters › Overview
- Evidence: Prose cross-reference: 'as described previously'
- Current text: as described previously
- Proposed fix: '(see §8 and §9)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §8 Combat Basics; §9 Enemy Turn. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-076 · prose-crossref · Minor · CLEAN-UP
- Location: L2099 §Boss Encounters › Boss Data Cards
- Evidence: Prose cross-reference: 'from previously described enemy data cards'
- Current text: from previously described enemy data cards
- Proposed fix: '(see §8.2)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §8.2 Enemy Data Cards. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-077 · prose-crossref · Minor · CLEAN-UP
- Location: L2105 §Boss Encounters › Boss Data Cards
- Evidence: Prose cross-reference: 'as detailed during the setup chapter of these rules'
- Current text: as detailed during the setup chapter of these rules
- Proposed fix: '(see §6.5)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §6.5 Encounter Setup › Encounter cards. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-083 · prose-crossref · Minor · CLEAN-UP
- Location: L1263, L1141, L849, L1914, L2141 (inline 'For example…')
- Evidence: Prose cross-reference: 'For example, if the first three encounters are marked cleared…'
- Current text: For example, if the first three encounters are marked cleared…
- Proposed fix: Set each as a separate *Example.* paragraph per the Voice Guide §7; examples are not rules. — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: n/a — worked examples embedded in rule sentences. Numbering per F_report.md §6 provisional map.
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

### F-091 · tone · Minor · OPTIONAL
- Location: L1487, L1596, L2027, L2143, L2191
- Evidence: Logical connectives in rules prose: 'Therefore' (L1487, L1596, L2191), 'Thus' (L2027, L2143), 'In other words' (L1594).
- Current text: Therefore, targets who successfully *dodge* an attack are not considered hit and therefore are not pushed or afflicted with conditions…
- Proposed fix: Delete the connective and state the consequence as its own rule: 'A model that dodges an attack is not hit: it is not pushed and receives no condition.'
- Rationale: Lawbook sentences do not argue; each states one outcome.
- Gameplay impact: none
- Decision needed: N

### F-125 · copied-prose · Note · OPTIONAL
- Location: L2069 §Boss Encounters › Overview
- Evidence: Matches official text — structural paraphrase; 'heart of' lifted from Core p.20
- Current text: Boss encounters are the heart of the character's adventure… There are three types of bosses… Boss encounters follow many of the same rules as other enemies… but there are key differences outlined as follows.
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.26 ('Boss encounters are the culmination of the party's exploration… There are two types of bosses… They follow many of the same rules as other enemies, but there are also some key differences.'). Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-126 · copied-prose · Note · OPTIONAL
- Location: L2101 §Boss Encounters › Boss Data Cards
- Evidence: Matches official text — paraphrase (9-word run)
- Current text: Boss behaviour deck size and heat-up point are used to determine the composition of the boss behaviour deck.
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.26. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-127 · copied-prose · Note · OPTIONAL
- Location: L2123–2125 §Boss Encounters › Boss Behaviour Cards
- Evidence: Matches official text — paraphrase (10-word runs)
- Current text: Some boss behaviour cards have a Heat Up symbol signifying those cards as Heat Up cards… To construct the initial boss behaviour deck, first set aside all of the Heat Up behaviours. Then, shuffle the normal boss behaviour cards and deal a number equal to the boss's behaviour deck size…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.28 (also BDK p.12). Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-128 · copied-prose · Note · OPTIONAL
- Location: L2129 §Boss Encounters › Boss Arcs and Defence
- Evidence: Matches official text — near-verbatim (64%, 24-word run; first sentence is V2's wording, second is Core's)
- Current text: The base of a boss model is separated into four distinct arcs: front, left, right, and back. These arcs are a key part of what makes boss encounters unique, and they add an extra layer of tactics…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.27 / V2 p.29. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-129 · copied-prose · Note · OPTIONAL
- Location: L2131 §Boss Encounters › Boss Arcs and Defence
- Evidence: Matches official text — near-verbatim (59%, 27-word run)
- Current text: Bosses always directly face an adjacent node. For a model to directly face a node, the centre of the model's front arc must line up with the centre of that node… Nodes along the lines between arcs are considered to be in both arcs.
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.27 (also V2 p.29). Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-130 · copied-prose · Note · OPTIONAL
- Location: L2137–2143 §Boss Encounters › Character Arc Movement
- Evidence: Matches official text — paraphrase (9-word run)
- Current text: A character moving onto the same node as a boss must remain in the same arc as the node from which they are moving… If a character moves out of a node shared with a boss, they must remain in the same arc…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.28 / V2 p.29. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-131 · copied-prose · Note · OPTIONAL
- Location: L2149–2151 §Boss Encounters › Attacking Bosses and Weak Arcs
- Evidence: Matches official text — verbatim (L2151 85%, 40-word run) — the 'Remember/Note' tone slips are inherited from Core
- Current text: When a character attacks a boss, the most recently resolved boss behaviour card determines which arcs are considered weak… Remember that a character can be in more than one arc if it is on a node along the arc line. This makes it easier to gain the weak arc bonus, but it also means… Note that even if…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.28. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

## Completion entries that apply (0) — approved at Gate 1

