# Drafting pack — chapter 16 (boss_turns) — manuscript chapter "BOSS TURNS"

Source text: `work/phase2a/source/16_boss_turns.md` (manuscript.md lines 2153–2198).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 2153.
- **Boss Turn Overview** · present — to audit · line 2155.
- **Boss Movement & Symbols** · present — to audit · line 2161.
- **Boss Attacks** · present — to audit · line 2181.
- **Boss Aggro** · present — TOC mismatch · line 2189. Not listed in TOC.
- **Boss Death** · present — to audit · line 2193.

## Audit findings mapped to this chapter (48)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### A-019 · undefined-state · Major · REQUIRED
- Location: BOSS TURNS › Boss Turn Overview (manuscript.md line 2157)
- Evidence: manuscript.md:2157, 1205, 1211
- Current text: characters must take an equal number of turns and cannot take a turn until every other character has taken an equal number of turns.
- Proposed fix: Dead characters are ignored when counting turns. Within each round the living characters choose the order in which they take their turns, and no living character takes a second turn in a round until every other living character has taken one.
- Rationale: A dead character can take no turns, so the literal equal-turns rule blocks every living character once anyone dies in a boss fight.
- Gameplay impact: Boss fights after a death become unplayable as written.
- Decision needed: N

### A-020 · contradiction · Major · REQUIRED
- Location: SUMMONS › Phantoms step 6 (manuscript.md line 1987) vs BOSS TURNS › Boss Turn Overview (line 2157)
- Evidence: manuscript.md:1971, 1987, 2157; DS-Phantoms-Rules-lores.txt p.8 (summon activates after each character activation)
- Current text: Phantoms take their turn after all character turns are resolved and before the first enemy turn begins.
- Proposed fix: In a boss encounter the phantom takes its turn after each character turn and before the following boss turn.
- Rationale: Phantoms are only ever summoned into boss encounters (1971), where boss and character turns alternate one at a time; 'after all character turns' has no meaning in that structure. The official rule is one phantom turn per character turn. Alternative: one phantom turn per full round of character turns.
- Gameplay impact: Phantom activation frequency changes its value by a factor of up to four.
- Decision needed: Y

### A-024 · undefined-state · Major · REQUIRED
- Location: COMBAT BASICS › Enemy Scaling (manuscript.md line 1529); Character Attacks › Repeat (line 1872); Boss Attacks (line 2187)
- Evidence: manuscript.md:1529, 1579, 1872, 2187; DS-Core-Rules-lores.txt p.40 ('Repeat behaviour or attack' icon exists on official cards)
- Current text: If playing with four characters, add repeat to each non-boss enemy's attack behaviour.
- Proposed fix: When Repeat 2 is added by scaling, each attack icon on the enemy's data card is resolved twice in succession against the same target before the next icon is resolved. The damage value of a push-movement is not an attack icon and is not repeated. If an attack icon already bears a Repeat icon, increase its value by one.
- Rationale: Repeat is defined for weapons (entire option) and bosses (entire card) but not for non-boss enemies, and official data cards already carry Repeat icons. Alternative: Repeat added by scaling does not stack with a printed Repeat icon.
- Gameplay impact: Four-player games double or quadruple some enemy damage output depending on the reading.
- Decision needed: Y

### A-038 · omission · Major · REQUIRED
- Location: BOSS TURNS › Boss Movement & Symbols (manuscript.md line 2175)
- Evidence: manuscript.md:2173–2179; DS-Core-Rules-lores.txt p.29 (Leap icon definition)
- Current text: If a boss leaps into a node occupied by a character, the boss maintains its original facing and the character(s) are pushed into any adjacent node of their choosing unrestricted by the boss arc.
- Proposed fix: Leap: Remove the boss from the tile and place it on the node of its target, the character with the aggro token or the nearest character as shown on the icon. A leap has no distance limit. The boss keeps its facing. Every character on that node is pushed to an adjacent node of that character's choice and is not placed in any arc.
- Rationale: The Turn and Rotate icons are defined but the Leap icon that the sentence depends on is not, and nothing says the leap targets a character.
- Gameplay impact: Leap appears on core mini-boss and main-boss cards; unresolvable without a definition.
- Decision needed: N

### A-039 · undefined-state · Major · PROPOSED
- Location: GAME COMPONENTS › Main-Bosses (manuscript.md lines 509–511) vs CAMPAIGNS (lines 2398, 2500, 2660, 2934); Node Model Limits (line 921)
- Evidence: manuscript.md:509, 511, 921, 2157, 2191, 2398; DS-Core-Rules-lores.txt p.5 ('Dragon Slayer Ornstein & Executioner Smough' is one main boss), p.21
- Current text: Dragon Slayer Ornstein (Core) / Executioner Smough (Core) ... Ornstein & Smough (main-boss)
- Proposed fix: Multiple-boss encounters: When a boss encounter contains two bosses, each boss has its own behaviour deck, health dial and heat-up point. During each boss turn both bosses act, in descending threat order; if tied, the players choose. The aggro token is assessed once for both bosses. The special rules on the bosses' data cards state what happens when one of them is slain. The encounter is cleared when both bosses are slain, and a single boss treasure is awarded.
- Rationale: The component list splits the pair while every campaign lists them as one boss. The only multi-boss rule in the manuscript is the node push (921). Alternative: list the pair as one main boss and play both bosses on a single alternating sequence (boss A, character, boss B, character).
- Gameplay impact: The core set's main boss cannot be played from the text.
- Decision needed: Y

### A-045 · undefined-state · Major · REQUIRED
- Location: SUMMONS › Invaders › Invader Tokens step 1 (manuscript.md line 1999); Boss Death (line 2195)
- Evidence: manuscript.md:1999–2011, 1147, 2195; DS-Phantoms-Rules-lores.txt p.11 ('if there are no invader tokens already in play and there is at least one unexplored tile')
- Current text: Embered characters provoke an invader if no invasion has occurred yet.
- Proposed fix: An invasion is provoked the first time a character becomes embered while at least one face-down encounter card is on the tiles. If characters become embered when no face-down encounter card exists (for example when a boss is slain), the invasion is provoked when encounter cards are next dealt. At most one invasion occurs before the mini-boss and at most one after it.
- Rationale: Boss Death embers everyone at a moment when the old encounter cards have been cleared and the new ones not yet dealt, so the token-placing procedure (2007) has nothing to place on. 'If no invasion has occurred yet' also leaves it open whether the limit is one per game or one per leg. Alternative: one invasion per game.
- Gameplay impact: Determines whether advanced invaders ever appear in a standard game.
- Decision needed: Y

### A-082 · undefined-state · Major · REQUIRED
- Location: TILES & NODES › Terrain › Gravestones, Barrels, Chests (manuscript.md lines 931, 949, 959); Character Movement (line 1840)
- Evidence: manuscript.md:931, 949, 951, 959, 1670–1678, 1840, 2175; DS-Core-Rules-lores.txt p.17 ('Gravestones block movement')
- Current text: Models cannot walk, run, dodge, or be pushed into nodes containing a gravestone. / Models cannot walk or run into nodes containing barrels. / Models cannot move, dodge, or be pushed into nodes containing a chest.
- Proposed fix: No model, including enemies and bosses, may move, leap, dodge or be pushed into a node containing a gravestone or a chest. No model may walk, run, shift or move into a node containing an intact barrel; a model that dodges or is pushed into such a node destroys the barrel and the token is removed.
- Rationale: Enemy movement is 'move', which is not in the gravestone or barrel lists; whether enemies and leaping bosses are blocked by terrain is unstated.
- Gameplay impact: Enemy pathing around terrain is decided every encounter.
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

### C-033 · italics · Major · REQUIRED
- Location: L1399; L1890; L1906; L2235; L1397; L1277; L3056; L2175; L2017; L1985
- Evidence: Undefined keywords: '*lost*' used at 1890/1906/2235 ('lost to the hollow', 'revives lost characters who have been removed from play due to dying while hollow') but never defined and conflicts with L1223 (hollow death forces a rest, no removal) and L1195 (mega-boss death = permanent removal); 'mastering the encounter' (1397) undefined; '*first player* token' (1277) placed but never used and not a component; 'First turn token' (3056) different name for same thing; boss '*leaps*' (2175) icon undefined; 'Heat Up value' for invaders (2017) undefined on invader cards; 'entrance node' (1985)
- Current text: lost / mastering / first player token / leaps
- Proposed fix: Define *lost* once (proposed: 'A character who dies while *hollow* is *lost*: remove the model from play until the party next rests at the *bonfire*'), then make L1223, L1906 and L1195 agree; delete 'mastering'; either define the first player token's effect or delete L1277 and use 'first player' in PvP only; define *leap*; use 'entry node'.
- Rationale: A term used as a keyword must be defined once.
- Gameplay impact: Whether a hollow character's death removes it from play or ends the encounter
- Decision needed: Y

### D-002 · hybrid · Major · REQUIRED
- Location: manuscript.md 1987 (Summons step 6) vs 2158 (Boss Turn Overview)
- Evidence: PH p.8: 'there will be a summon activation after each character activation' (boss, character, summon, boss, character, summon). The manuscript's phantom acts 'after all character turns are resolved and before the first enemy turn begins', a phase that exists only in the manuscript's round-based standard encounters (1281–1295); boss encounters keep the 1E alternation (2158), where no such phase occurs.
- Current text: Phantoms take their turn after all character turns are resolved and before the first enemy turn begins.
- Proposed fix: The phantom takes a turn immediately after each character's turn, before the boss's next turn. The phantom does not take a turn after the boss's turn.
- Rationale: The summon cadence was written for the manuscript's round structure, but summons appear only in boss encounters, which use 1E alternation. The official cadence (PH p.8) fits boss alternation without further change.
- Gameplay impact: As written the phantom never has a defined moment to act in a boss fight.
- Decision needed: Y

### F-033 · meta-commentary · Major · CLEAN-UP
- Location: L2159 §Boss Turns › Boss Turn Overview ¶2
- Evidence: Strategy advice: 'Players can gain an advantage over a boss by memorising the order in which the boss behaviour cards will appear each time the deck is renewed.'
- Current text: Players can gain an advantage over a boss by memorising the order in which the boss behaviour cards will appear each time the deck is renewed.
- Proposed fix: CUT
- Rationale: Tactical advice is not a rule. The preceding sentence already states that the discard pile is flipped without shuffling.
- Gameplay impact: none
- Decision needed: N

### F-034 · tone · Major · CLEAN-UP
- Location: L2191 §Boss Turns › Boss Aggro
- Evidence: Rationale and person shift to 'one': 'Because the boss takes a turn after each individual character takes their turn, one can assume any damage dealt… Therefore, simply move…'
- Current text: Because the boss takes a turn after each individual character takes their turn, one can assume any damage dealt by a character will be the most damage prior to the boss's activation. Therefore, simply move the *aggro* token to a character's dashboard if they deal any damage to the boss during their turn. If no damage is dealt, the *aggro* token remains stationary for that turn.
- Proposed fix: REWRITE-IN-VOICE: 'At the start of a boss encounter, the *aggro* token is placed on the character with the highest *threat*. After each character's turn, if that character dealt damage to the boss, move the *aggro* token to that character. Otherwise it does not move.'
- Rationale: State the rule, not the reasoning that derives it.
- Gameplay impact: none
- Decision needed: N

### F-035 · meta-commentary · Major · CLEAN-UP
- Location: L2197 §Boss Turns › Boss Death ¶2
- Evidence: Session advice: 'This is often a reasonable time to end a game session if time is limited. Either today or another day the players may continue on…'
- Current text: This is often a reasonable time to end a game session if time is limited. Either today or another day the players may continue on with post-boss setup rules as described earlier in these rules.
- Proposed fix: CUT. (If a pause rule is wanted, state it in-voice: 'The game may be paused after a boss is defeated. Record each character's dashboard, inventory and *souls* and the *spark* dial.')
- Rationale: Advice about table logistics, with a hedge ('often … reasonable').
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

### A-005 · contradiction · Minor · REQUIRED
- Location: GAMEPLAY › Death & Hollowing (manuscript.md line 1221) vs Resting at The Bonfire (line 1898), Boss Death (line 2195), PvP (line 3046)
- Evidence: manuscript.md:1221, 1898, 1908, 2195, 3046
- Current text: Hollow status is only removed by using a spark or an ember token.
- Proposed fix: Hollow status is removed only by resting at the bonfire or by becoming embered.
- Rationale: Resting after a boss (2195) and before PvP (3046) costs no spark yet removes hollow cubes (1898). The restriction must name the rest, not the spark.
- Gameplay impact: Literal reading leaves characters hollow after the free post-boss rest.
- Decision needed: N

### A-007 · undefined-state · Minor · PROPOSED
- Location: GAMEPLAY › Embering (manuscript.md line 1243); Shop Rules (line 1949); Boss Death (line 2195)
- Evidence: manuscript.md:1243, 1949, 2195
- Current text: Characters cannot carry an ember card while embered.
- Proposed fix: When a character becomes embered while holding an ember card, that character must immediately give the ember card to another character who is neither embered nor holding an ember card. If no such character exists, the ember card is returned to the tier one shop.
- Rationale: Boss Death embers every character at once (2195), so a character holding an ember card is placed in an illegal state with no resolution. Alternative: return the card to the game box.
- Gameplay impact: Rare but guaranteed to arise after the first boss when a character has bought an ember.
- Decision needed: Y

### A-018 · undefined-state · Minor · OPTIONAL
- Location: BOSS TURNS › Boss Aggro (manuscript.md line 2191); Parry & Riposte (line 1790)
- Evidence: manuscript.md:1790, 2191
- Current text: ...simply move the aggro token to a character's dashboard if they deal any damage to the boss during their turn.
- Proposed fix: Damage inflicted on a boss by a riposte during the boss's turn moves the aggro token to the riposting character at the end of that boss turn.
- Rationale: A riposte is an out-of-turn attack; the boss aggro rule only covers damage dealt 'during their turn'.
- Gameplay impact: Edge case created by the manuscript's own parry rule.
- Decision needed: N

### A-022 · undefined-state · Minor · OPTIONAL
- Location: BOSS TURNS › Boss Turn Overview (manuscript.md line 2157) vs Encounter Turn Order step 2 (line 1289)
- Evidence: manuscript.md:1289, 2157
- Current text: After each boss turn, one character may take their turn, then the boss takes another turn, a second character, and so-on.
- Proposed fix: In boss encounters the players choose which living character takes each character turn, subject to the equal-turns rule. The descending threat order of ordinary encounters does not apply.
- Rationale: Ordinary encounters fix character order by threat (1289); boss encounters say 'one character may take their turn', which implies free choice without saying so. Alternative: apply threat order in boss encounters as well.
- Gameplay impact: Determines whether players can sequence the healer after the tank in boss fights.
- Decision needed: Y

### A-042 · undefined-state · Minor · OPTIONAL
- Location: BOSS ENCOUNTERS › Boss Behaviour Cards (manuscript.md line 2125); Parry & Riposte (line 1790)
- Evidence: manuscript.md:1790, 2125, 2159
- Current text: When the boss's health is reduced to (or below) its Heat Up point, take a random Heat Up behaviour card and shuffle it into the boss behaviour deck.
- Proposed fix: If the boss heats up during its own turn (for example from a riposte), finish resolving the current behaviour card, then shuffle the Heat Up card into the remaining behaviour deck. If the behaviour deck is empty at that moment, the Heat Up card becomes the behaviour deck and the discard pile is not yet renewed.
- Rationale: A riposte can damage the boss mid-card; and the deck may be empty (all cards in the discard) when heat-up occurs.
- Gameplay impact: Edge case that arises once in most boss fights with a parrying character.
- Decision needed: N

### A-047 · undefined-state · Minor · OPTIONAL
- Location: GAMEPLAY › Sparks (manuscript.md lines 1247–1253); Boss Death (line 2195)
- Evidence: manuscript.md:715, 1093, 1249, 2195, 2233; DS-Core-Rules-lores.txt p.33 (campaign maximum = starting sparks)
- Current text: Defeating a mini-boss or main-boss provides one additional spark.
- Proposed fix: The spark dial never shows more sparks than the characters' starting number; a spark gained beyond that maximum is lost.
- Rationale: The campaign chapter sets this maximum (2233) but the basic game does not; a solo character would reach six or seven, beyond the physical dial. Alternative: no maximum, track overflow with a token.
- Gameplay impact: Solo and two-character basic games only.
- Decision needed: Y

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

### C-039 · terminology · Minor · REQUIRED
- Location: L1606; L1618; L1860; L2191
- Evidence: 'not removed at the end of activations' (1606); 'at the end of its activation' (1618); 'during their activation' (1860); 'prior to the boss's activation' (2191) vs 'turn' x65 incl. L1600 'When a model ends its turn'
- Current text: activation
- Proposed fix: turn
- Rationale: One word for one concept; 'turn' is the manuscript's dominant and defined term (L1279-1295, L1800).
- Gameplay impact: None
- Decision needed: N

### C-042 · terminology · Minor · CLEAN-UP
- Location: L771; L849; L1131; L1171; L1179; L1886; L1892; L2195; L2295; L2358ff
- Evidence: 'The Bonfire' capitalised mid-sentence x10 (e.g. 771 'resting at The Bonfire'); '*bonfire*' x35; plain 'the bonfire' x27; 'Bonfire Tile' x48 in campaign lists; 'The Bonfire tile' (1131, 1171, 1179)
- Current text: The Bonfire / Bonfire Tile
- Proposed fix: the *bonfire* (lower-case keyword); 'bonfire tile' for the component; headings may read 'The Bonfire'
- Rationale: Game locations are common nouns (cf. fog gate, shop); capital 'The' mid-sentence is inconsistent with the keyword form.
- Gameplay impact: None
- Decision needed: N

### C-043 · terminology · Minor · CLEAN-UP
- Location: L841; L1025; L1099; L1169; L1888; L1904; L1927; L1929; L2195; L2297; L2310; L2312; L2314; L2340
- Evidence: 'Blacksmith Andre' x7; bare 'Andre' x11 (e.g. 1099 'next to Andre'); 'Andre's Shop' x9; 'the shop' x3; heading 'Blacksmith Andre's Shop' (2310)
- Current text: Andre's Shop / the shop / Andre
- Proposed fix: 'Blacksmith Andre' at first mention in a section, 'Andre' thereafter; 'Andre's shop' (lower-case s) for the shop, 'the shop' acceptable after first mention
- Rationale: One NPC, one shop; choose capitalisation once. Recommend lower-case 'shop' to match other lower-cased game locations (bonfire, fog gate).
- Gameplay impact: None
- Decision needed: Y

### C-052 · terminology · Minor · CLEAN-UP
- Location: L1093
- Evidence: 'Set the *sparks* dial' vs 'spark dial' (715, 1167, 1185, 2195)
- Current text: sparks dial
- Proposed fix: spark dial
- Rationale: Component name is singular-attributive.
- Gameplay impact: None
- Decision needed: N

### C-061 · terminology · Minor · REQUIRED
- Location: L1517; L1850; L1295; L1301; L2053; L2195; L1223; L1305
- Evidence: Enemy death verbs vary: 'considered killed and removed from the tile' (1517); 'that enemy dies and is removed from play' (1850); 'all enemy models are defeated' (1295, 1301); 'the lizard is slain' (2053); 'the boss is slain' (2195). Characters 'die' (1223, 1305).
- Current text: killed / dies / defeated / slain
- Proposed fix: Characters 'die'; non-boss enemy models are 'killed' (and removed); bosses and encounters are 'defeated'/'cleared'. Replace 'slain' and enemy 'dies'.
- Rationale: Distinct verbs let rules refer unambiguously to character death (which has consequences) versus enemy removal.
- Gameplay impact: None
- Decision needed: Y

### C-084 · cross-ref · Minor · CLEAN-UP
- Location: L837; L839; L841; L891; L1057; L1165; L1475; L1485; L1760; L1852; L2045; L2069; L2077; L2099; L2105; L2163; L2195; L2197; L2289; L2297; L2312
- Evidence: 21 prose cross-references resolved correctly but informally: 'explained in detail later on in the section title "Character Attacks"' (837, 'title' for 'titled'); 'section titled "Enemy Attacks"' (839); 'described later in more detail' (841); 'aforementioned effects' (891); 'as above' (1057, 1760); 'as previously described' (1165, 2195); 'later in these rules' (1475); 'detailed later' (1485); 'explained above/previously' (1852); 'per normal treasure chest rules' (2045); 'as described previously' (2069); 'will follow' (2077); 'previously described' (2099, 2163); 'as detailed during the setup chapter' (2105); 'as described earlier' (2197); 'as in the basic rules' (2289, 2297, 2312)
- Current text: (see Evidence)
- Proposed fix: Convert every one to the form '(see §N.N Heading)' once section numbers exist; drop 'later/earlier/previously/aforementioned'. Resolution table in C_report.md Task 6.
- Rationale: Positional words break when sections move; numbered references do not.
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

### C-112 · punctuation · Minor · CLEAN-UP
- Location: L679; L895; L1199; L1203; L1710; L1766; L2161; L2201; L2237; L449; L2398
- Evidence: '&' in nine headings and in list items 'Mushroom Child & Parent' (449), 'Ornstein & Smough' (2398, 2500, 2660, 2934)
- Current text: &
- Proposed fix: 'and' in headings and prose; '&' only inside an official product or card name
- Rationale: Ampersand is a logo/label device, not prose.
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

### C-121 · voice · Minor · OPTIONAL
- Location: L1888; L1890; L2069; L2159; L2197; L2041; L2053; L1876; L1872; L1107; L1109
- Evidence: Flavour and advice inside rules paragraphs: Firekeeper/Andre description (1888); 'Sparks are the most precious resource in this game and the players must carefully weigh the timing' (1890); 'targets of their bloodlust... characters can expect to die often' (2069); 'Players can gain an advantage over a boss by memorising the order' (2159); session-break advice (2197); 'quite punishing' (2041); 'strange and glimmering reptiles' (2053); 'decidedly on the offensive' (1876); 'rapid flurry of attacks' (1872); 'if they like' (1107); 'For added challenge' (1109)
- Current text: (flavour)
- Proposed fix: Move to clearly styled sidebars/flavour boxes or cut; rules paragraphs carry rules only.
- Rationale: Mixing flavour and rules obscures what is binding.
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

### F-078 · prose-crossref · Minor · CLEAN-UP
- Location: L2163 §Boss Turns › Boss Movement & Symbols
- Evidence: Prose cross-reference: 'previously described with the following exceptions'
- Current text: previously described with the following exceptions
- Proposed fix: '(see §9.2 and §9.3)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §9.2 Enemy Movement; §9.3 Enemy Attacks. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-079 · prose-crossref · Minor · CLEAN-UP
- Location: L2195 §Boss Turns › Boss Death
- Evidence: Prose cross-reference: 'as previously described'
- Current text: as previously described
- Proposed fix: '(see §7.6 and §7.7)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §7.6 Souls; §7.7 Treasure Rewards. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-080 · prose-crossref · Minor · CLEAN-UP
- Location: L2197 §Boss Turns › Boss Death
- Evidence: Prose cross-reference: 'post-boss setup rules as described earlier in these rules'
- Current text: post-boss setup rules as described earlier in these rules
- Proposed fix: '(see §6.6 and §6.7)' — sentence otherwise CUT (F-row for L2197) — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §6.6 Setup After the Mini-boss; §6.7 Setup After the Main-boss. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-087 · register-shift · Minor · CLEAN-UP
- Location: L769, L2191
- Evidence: Indefinite pronoun 'one': 'one must pay the cost in souls for the tier one upgrade' (L769); 'one can assume any damage dealt' (L2191)
- Current text: (i.e., to upgrade strength from base tier to tier two, one must pay the cost in *souls* for the tier one upgrade, and then the tier two upgrade).
- Proposed fix: Third person with a named actor: 'the character pays the tier one cost and then the tier two cost'. Set L769 as an *Example.*
- Rationale: 'one' is a third voice alongside players/characters.
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

### A-041 · inherits-official-silently · Note · CLEAN-UP
- Location: BOSS TURNS › Boss Turn Overview (manuscript.md line 2159)
- Evidence: manuscript.md:2159; DS-Core-Rules-lores.txt p.29; DS-TG-Rulebook p.30
- Current text: flip the discard pile face-down without shuffling the cards to renew the boss behaviour deck.
- Proposed fix: No change.
- Rationale: Identical to the official rule and explicitly justified in the text (memorisation). Recorded so that no editor 'fixes' it by adding a shuffle.
- Gameplay impact: None.
- Decision needed: N

### B-036 · scaling · Note · OPTIONAL
- Location: L1531 (Enemy Scaling: bosses do not scale) with L2184 (Boss Turn Overview)
- Evidence: Boss health is fixed (consistent with Core p.26 and V2 p.28). Because the boss acts after every character turn, the number of boss activations needed to kill it is independent of player count (example boss 24 health / block 2: about 11 character turns with Shortsword [2], 6 with tier-two weapons), so each character absorbs 1/N of the boss's attacks. Combined with the ordinary-encounter scaling of L1519-1560, the route is harder than the boss at 4 players and easier than the boss at 1 player.
- Current text: Boss enemies (mini, main, and mega) do NOT modify their base health or receive scaling benefits otherwise.
- Proposed fix: No change to the boss rule; adopt B-003/B-004 so that encounter difficulty does not invert relative to bosses. Optionally: "At four characters, increase a mini-boss's or main-boss's starting health by four."
- Rationale: Both official editions leave bosses unscaled; the inversion is caused by the encounter table, not by the boss rule.
- Gameplay impact: None unless the optional sentence is adopted (adds about two boss activations at 4 players).
- Decision needed: N

### C-044 · terminology · Note · CLEAN-UP
- Location: L1169; L1187; L1888; L1902; L1912; L2195; L2297
- Evidence: 'Firekeeper' x8, no variants; matches Core/TG rulebooks ('Firekeeper' x16)
- Current text: Firekeeper
- Proposed fix: No change
- Rationale: Consistent; record in style sheet.
- Gameplay impact: None
- Decision needed: N

### F-132 · copied-prose · Note · OPTIONAL
- Location: L2159 §Boss Turns › Boss Turn Overview
- Evidence: Matches official text — close paraphrase (13-word run)
- Current text: If there are no cards remaining in the behaviour deck at the start of a boss's turn, flip the discard pile face-down without shuffling the cards to renew the boss behaviour deck.
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: V2 p.30. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-133 · copied-prose · Note · OPTIONAL
- Location: L2177–2179 §Boss Turns › Boss Movement & Symbols
- Evidence: Matches official text — paraphrase (8-word runs)
- Current text: The turn symbol indicates the boss turns 90 degrees to the left or right… The rotate symbol indicates the boss turns 180 degrees to face their rear.
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: V2 p.30. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

## Completion entries that apply (0) — approved at Gate 1

