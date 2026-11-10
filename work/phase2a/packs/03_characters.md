# Drafting pack — chapter 03 (characters) — manuscript chapter "CHARACTERS"

Source text: `work/phase2a/source/03_characters.md` (manuscript.md lines 725–806).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 725.
- **Character Dashboards** · present — to audit · line 727.
- **Equipment Slots** · present — to audit · line 755.
- **Stat Progression Track** · present — to audit · line 767.
- **Endurance Bar** · present — to audit · line 773.
- **Character Tokens** · present — defect · line 791. Says "three types" then "four following tokens"; Estus Flask subsection MISSING (text survives only in DOCX footer).
- **Heroic Action** · present — to audit · line 795.
- **Luck** · present — to audit · line 799.
- **Ember** · present — to audit · line 803.
- **Estus Flask** · MISSING — in TOC only · Rule text only in DOCX footer: "flip estus flask token as a major action to remove all damage cubes; stamina cubes are not removed."

## Audit findings mapped to this chapter (45)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### B-014 · balance · Blocker · REQUIRED
- Location: L1261-1263 (Encounter Start step 2) with L781 and L791-795
- Evidence: Three skipped encounters = 6 stamina (the manuscript's own example). Hollow bar = 6 spaces, so a hollow character starts with zero free boxes: any damage kills (L795) and any stamina cost is forbidden (L791-793), leaving Rest as the only legal major action. A healthy character with three skips has 2 free boxes: P(death) from one Hollow Soldier hit (attack 4, 2 black block dice) = 0.556; at 3 players (attack 5) 0.889. Any hollow death fails the encounter and costs a spark (L1223).
- Current text: Characters may skip previously *cleared* encounters at the cost of two stamina cubes placed in the endurance bar of each character. For example, if the first three encounters are marked *cleared* then the characters could skip to the fourth encounter but would all start with 6 stamina expended.
- Proposed fix: "Characters may skip previously cleared encounters. Each character places one stamina cube in their endurance bar for each encounter skipped, to a maximum of three. For example, if the first three encounters are marked cleared, the characters may skip to the fourth encounter and each starts it with three stamina spent."
- Rationale: The skip is a time-saving device; the tax must leave a hollow character at least three free boxes (6 - 3 = 3) so that the first enemy phase is survivable.
- Gameplay impact: Hollow three-skip death chance per Hollow Soldier hit falls from 100% to 19% (3 free boxes, attack 4); healthy from 56% to 3%.
- Decision needed: Y

### A-006 · contradiction · Major · REQUIRED
- Location: GAMEPLAY › Embering (manuscript.md line 1229) vs CHARACTERS › Ember (line 805) and CHARACTER TURN › Major Action › Ember (line 1834)
- Evidence: manuscript.md:805, 891, 1227–1233, 1834
- Current text: Ember: Place ember token on dashboard; discard equipped ember card.
- Proposed fix: Ember (major action, or at any time outside an encounter): Discard an ember card from the back-up slot. Remove all damage cubes and all hollow markers from the endurance bar and place an ember token on the dashboard. The character is now embered.
- Rationale: Three passages define embering; only Embering (1229) says it removes all damage cubes. A full heal as a major action is a major tactical resource and must be stated identically everywhere. Alternative: delete 'Remove all damage cubes' at 1229 so that embering only removes hollow markers (Hollowed Edition precedent, p.5).
- Gameplay impact: Groups will disagree on whether embering heals; the difference is up to eight health in combat.
- Decision needed: Y

### A-008 · contradiction · Major · REQUIRED
- Location: GAMEPLAY › Encounters › Encounter Start step 2 (manuscript.md lines 1261–1263) vs CHARACTERS › Endurance Bar (line 787)
- Evidence: manuscript.md:781, 787, 1261–1263
- Current text: A character may never elect to spend excess stamina at the cost of receiving a staggered condition marker.
- Proposed fix: The characters may skip cleared encounters only if every character can place all of the required stamina cubes without exceeding their endurance bar. A hollow character has six spaces. The stamina cubes for skipped encounters are placed at the start of the next encounter the characters fight.
- Rationale: Skipping is elective, costs two stamina per skipped encounter per character, and a hollow character has six spaces; skipping four encounters (eight stamina) is therefore impossible under line 787, yet campaign sections list up to five encounters. Alternative: allow the skip and place a single stagger token for the overflow.
- Gameplay impact: Determines whether hollow characters can use the skip mechanic at all in long sections.
- Decision needed: Y

### A-012 · omission · Major · REQUIRED
- Location: CHARACTERS › Character Tokens (manuscript.md line 793) — Estus Flask absent from body; DOCX footer only
- Evidence: manuscript.md:793, 1830; DOCX footer ('The character may flip their estus flask token to the used side as a major action to remove all damage cubes from their endurance bar. Stamina cubes are not removed.'); DS-Core-Rules-lores.txt p.11
- Current text: There are three different types of character tokens: heroic actions, luck, and estus flask. ... Each character has one of each of the four following tokens
- Proposed fix: Estus Flask: A character may flip their estus flask token to the used side as a major action to remove all damage cubes from their endurance bar. Stamina cubes and hollow markers are not removed. There are four character tokens: heroic action, luck, estus flask and ember.
- Rationale: The only Estus rule lives in the page footer. The body also says 'three types' then 'four following tokens'. The hollow interaction (markers stay) must be explicit because hollow markers occupy endurance spaces.
- Gameplay impact: Without the body text, the Drink Estus major action (1830) has no definition of what 'health' it restores.
- Decision needed: N

### A-068 · inherits-official-silently · Major · REQUIRED
- Location: ENEMY TURN › Parry & Riposte (manuscript.md lines 1772, 1790); CHARACTER TURN › Major Action › Attack (line 1822); CHARACTERS › Equipment Slots (line 761)
- Evidence: manuscript.md:757–763, 1772, 1790, 1822; DS-Core-Rules-lores.txt p.12 (left-hand and right-hand slots); DS-TG-Rulebook p.8 (hand slots)
- Current text: Characters must be equipped with a shield as their left weapon. ... using any attack option on the weapon equipped to the right weapon slot.
- Proposed fix: Equipment Slots: The two weapon slots are the left-hand slot and the right-hand slot; a one-handed card may be placed in either. Parry: Characters must have a shield equipped in one weapon slot and a weapon with at least one attack option in the other; the riposte uses that weapon.
- Rationale: Left and right slots exist on the official dashboards but the manuscript's Equipment Slots section never names them; the parry rule then depends on which physical slot holds the shield, which is a player choice with no rule attached.
- Gameplay impact: Players cannot tell whether a shield in the right slot permits a parry.
- Decision needed: N

### B-015 · table-text-mismatch · Major · REQUIRED
- Location: L781 (Endurance Bar) and L1215-1219 (Death & Hollowing)
- Evidence: Manuscript: endurance bar 'total of eight stamina/damage cubes', hollow reduces to six. Official 1E boards have ten boxes (Core p.20: 'If all ten of a character's endurance bar boxes have cubes'; Herald board image p.11). Hollowed Edition p.5 applies the same two cubes to the official ten-box bar. Every survivability figure in B_report assumes eight.
- Current text: The effect of these *hollow* markers is to reduce the functional capacity of the endurance bar from a total of eight stamina/damage cubes to only six.
- Proposed fix: Either (a) "from a total of ten stamina and damage cubes to eight" if official dashboards are used, or (b) state in Game Components that Second Edition dashboards have an eight-space endurance bar.
- Rationale: The number must match the physical component the players own; nothing in the manuscript announces new dashboards.
- Gameplay impact: Two boxes = 25% of capacity; with ten boxes the 4-player Repeat Hollow Soldier one-activation kill chance drops from 5.8% to 0.1%.
- Decision needed: Y

### B-022 · undefined-value · Major · REQUIRED
- Location: L1069/L1079/L1085 (Shop Setup) with L823-829 (Equipment Cards), L747-753 (Equipment Slots), L1769 (Parry)
- Evidence: The stock list requires '2 shields' per shop and the parry rule requires 'a shield as their left weapon', but the card-typing rules define only one-handed weapon, two-handed weapon, armour (by icon) and spell (by scroll art). No rule says how a shield is recognised; shields are weapon-typed cards in 1E (East-West Shield appears in the manuscript's own weapons table, L3244).
- Current text: Equipment cards include weapons, spells, shields, armour, and items which the character equips to improve their combat capabilities. ... 3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells.
- Proposed fix: Add to Equipment Cards: "A shield is a one-handed weapon card that shows a block or resist value and has no attack option. Shields count as weapons for equipment slots and as shields for shop stocking and parrying."
- Rationale: The shop and parry procedures cannot be executed without a test for 'shield'.
- Gameplay impact: Makes the 12-card stock list and the parry prerequisite determinable.
- Decision needed: Y

### C-019 · hedge · Major · REQUIRED
- Location: L765; L793; L979; L1131; L1159; L1201; L1880; L1963; L2065; L2169
- Evidence: 10 'should' in procedural rules, e.g. L1131 'Encounter levels should increase from the tile adjacent to The Bonfire tile'; L2065 'the fog gate tile should be removed... and placed on the bonfire tile'; L1880 'the character should mark the equipped item with a red damage cube'; L765 'players should not interact with their character's inventory cards'
- Current text: should
- Proposed fix: must / imperative: 'Encounter levels must increase from the tile adjacent to the bonfire tile towards the mini-boss tile.' / 'Move the fog gate token from the boss tile's entrance to the bonfire tile.' / 'Mark the equipped card with a red damage cube.' / 'During an encounter a character may not access their inventory.' Full list in C_report.md Task 2.
- Rationale: These are mandatory steps; 'should' makes them optional.
- Gameplay impact: Setup order, fog-gate shortcut, inventory access and scaling marker become mandatory as intended
- Decision needed: N

### C-035 · terminology · Major · REQUIRED
- Location: L775; L1215; L1205
- Evidence: 'A character's stamina bar tracks their stamina and damage' (775); 'Place two white cubes on the right side of the stamina bar' (1215); 'cannot add a damage cube to their endurance tracker' (1205); 'endurance bar' x14 elsewhere incl. heading L773
- Current text: stamina bar / endurance tracker
- Proposed fix: endurance bar
- Rationale: The bar tracks both stamina and damage; 'stamina bar' misdescribes it. Official term is 'endurance bar' (Core/TG x21).
- Gameplay impact: None once standardised
- Decision needed: N

### C-048 · terminology · Major · REQUIRED
- Location: L1393; L805; L891; L919; L2239; L989; L1095
- Evidence: 'Successfully defeated invaders provide additional *souls* per player' (1393) vs Soul Reward Table 'per character' (1411); 'when that player discards an ember card' (805); 'stored in a player's inventory' (891); 'characters must choose a friendly model to push' (919 - a decision); 'If a player character leaves the characters' (2239). Note L989 'character dashboard(s)' and L1095 'character model(s)' allow one player to control several characters.
- Current text: per player / that player / player's inventory / characters must choose
- Proposed fix: Rule of use: PLAYERS decide, agree, choose and roll; CHARACTERS act, hold tokens, own cards and inventories, gain souls and die; MODELS occupy nodes, move and are pushed. L1393 -> 'per character'; L805 -> 'when that character discards'; L891 -> 'a character's inventory'; L919 -> 'the players must choose a friendly model to push'; L2239 -> 'If a player leaves, remove their character...'
- Rationale: When one player controls two characters, 'per player' and 'per character' pay different soul rewards.
- Gameplay impact: Soul rewards for invaders in 1-2 player games
- Decision needed: N

### C-050 · terminology · Major · REQUIRED
- Location: L781; L805; L1215; L1231; L1367; L1379; L1898; L3074; L771; L993; L1914; L689
- Evidence: 'block off the two furthest right spaces... with a marker such as white cubes. The effect of these *hollow* markers' (781); 'discard any *hollow* tokens' (805, 1379); 'Place two white cubes' (1215, 1367); 'Remove all *hollow* cubes' (1231, 1898, 3074). 'White cubes' are also the stat cubes (771, 993, 1914) and the component list has exactly 16 stat tier cubes (689) = 4 characters x 4 stats, none spare.
- Current text: hollow markers / hollow tokens / hollow cubes / white cubes
- Proposed fix: 'hollow cube' throughout; add a component line '8x Hollow cubes (white)' or specify the colour and source of the marker once in §Death & Hollowing
- Rationale: One component, four names; and the marker is not in the component list.
- Gameplay impact: Players may be short of markers; 'white cube' is ambiguous with stat cubes
- Decision needed: Y

### C-064 · terminology · Major · REQUIRED
- Location: L543; L1967; L1969; L1971; L3052; L805; L1239
- Evidence: 'Phantoms' heading (543) covers Invaders and Summons; chapter 'SUMMONS' (1967) contains both 'Phantoms' (= summons only, 1969-1993) and 'Invaders' (1995); 'summon a random friendly phantom' (1971); 'Phantoms (Summons and Invaders)' (3052); 'enable the character to summon phantoms, but also attract malicious invaders' (805)
- Current text: Phantoms (two senses); chapter SUMMONS
- Proposed fix: *phantom* = umbrella (summons and invaders); *summon* = friendly phantom; *invader* = hostile phantom. Rename chapter 'PHANTOMS' with sections 'Summons' and 'Invaders'; L1969 heading -> 'Summons'.
- Rationale: The same word names the superset and one subset within two pages.
- Gameplay impact: Reader confusion over which rules apply to invaders
- Decision needed: N

### D-021 · component-count · Major · REQUIRED
- Location: manuscript.md 781 (Endurance Bar)
- Evidence: Core p.20: 'If all ten of a character's endurance bar boxes have cubes, that character has been killed.' The official dashboard has ten boxes; the manuscript says eight.
- Current text: The effect of these hollow markers is to reduce the functional capacity of the endurance bar from a total of eight stamina/damage cubes to only six.
- Proposed fix: The hollow markers reduce the capacity of the endurance bar from ten spaces to eight.
- Rationale: Factual error against the official component unless the manuscript intends custom dashboards.
- Gameplay impact: Health and stamina totals for every character.
- Decision needed: N

### D-030 · underspecified-deviation · Major · REQUIRED
- Location: manuscript.md 1772, 1790, 1822 (Parry; Major Action) vs 757–763 (Equipment Slots)
- Evidence: Core p.12 names left-hand and right-hand slots; the manuscript's Equipment Slots section names only 'the weapon slots' but the parry rule requires a shield in the 'left weapon slot' and the riposte uses the 'right weapon slot'.
- Current text: Characters must be equipped with a shield as their left weapon … using any attack option on the weapon equipped to the right weapon slot
- Proposed fix: The two weapon slots are the left-hand slot and the right-hand slot. A card equipped in either slot is in hand.
- Rationale: Parry and riposte cannot be applied without named slots.
- Gameplay impact: Defensive option availability.
- Decision needed: N

### F-057 · prose-crossref · Major · CLEAN-UP
- Location: L757 §Characters › Equipment Slots
- Evidence: Prose cross-reference: 'as described'
- Current text: as described
- Proposed fix: Delete 'as described'; the following paragraphs state the rule. — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: DANGLING — no antecedent (the slot rules follow in the same section). Numbering per F_report.md §6 provisional map.
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

### A-009 · undefined-state · Minor · OPTIONAL
- Location: CHARACTERS › Endurance Bar (manuscript.md line 787); Conditions › Stagger (line 1634)
- Evidence: manuscript.md:787, 1634
- Current text: Stagger tokens are limited to one per model.
- Proposed fix: If a character who is already staggered is forced to place a stamina cube when no space remains, the cube is not placed and no further effect occurs.
- Rationale: Stamina overflow converts to a stagger token, and stagger is capped at one; the second overflow has no stated outcome.
- Gameplay impact: Edge case only; prevents table arguments about repeated overflow.
- Decision needed: N

### A-052 · contradiction · Minor · CLEAN-UP
- Location: SETUP › Character Setup step 5 (manuscript.md line 997) vs CHARACTERS › Character Tokens (line 793)
- Evidence: manuscript.md:793, 997
- Current text: Place an ember token beside the character's board. / The ember tokens ... should be placed in the condition token supply at the start of the game.
- Proposed fix: Place the ember tokens in the token supply.
- Rationale: Two setup locations for the same token.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-072 · undefined-state · Minor · OPTIONAL
- Location: CHARACTER TURN › Minor Actions › Equip (manuscript.md line 1814)
- Evidence: manuscript.md:763, 1806–1818; DS-Core-Rules-lores.txt p.22 (swap only between backup and hand slots)
- Current text: Equip: Swap equipment cards between the back-up slot, weapon slots, and armour slots on the character dashboard. Inventory is unavailable.
- Proposed fix: Equip may be taken once per turn and exchanges any number of cards among the back-up, weapon and armour slots.
- Rationale: Each minor action is listed with 'AND' but no frequency; Run is explicitly repeatable, the others are not addressed. Armour swapping mid-encounter is a deliberate extension of the official rule and is kept. Alternative: Equip may be taken any number of times.
- Gameplay impact: Stops repeated swap-attack-swap sequences within one turn.
- Decision needed: Y

### A-105 · undefined-state · Minor · OPTIONAL
- Location: CAMPAIGN PLAY › Adding & Dropping Players (manuscript.md line 2239)
- Evidence: manuscript.md:765, 1385–1387, 2239; DS-Core-Rules-lores.txt p.33
- Current text: New players can join a campaign that is in progress at the cost of one spark each. ... the character's equipment is added to the inventory
- Proposed fix: A new player may join only while the spark dial shows at least one spark. When a character leaves, their equipment cards are distributed among the remaining characters' inventories as the players choose, and their souls are returned to the supply.
- Rationale: The manuscript has personal inventories and personal souls (765, 1387), so the official communal-inventory sentence no longer resolves; joining at zero sparks is unaddressed.
- Gameplay impact: Rare.
- Decision needed: N

### A-125 · terminology · Minor · CLEAN-UP
- Location: CHARACTERS › Character Dashboards item 7 (manuscript.md line 745)
- Evidence: manuscript.md:745, 1289, 1515; DS-Core-Rules-lores.txt p.11 ('Taunt Level'); DS-Phantoms-Rules-lores.txt p.6
- Current text: Threat Level
- Proposed fix: Glossary: Threat – the value printed as 'Taunt' on official character dashboards and summon cards; the manuscript uses 'threat' for characters, phantoms and enemies alike.
- Rationale: Physical dashboards say Taunt; without the glossary note readers cannot find the character's threat value.
- Gameplay impact: Cosmetic.
- Decision needed: N

### B-029 · table-text-mismatch · Minor · REQUIRED
- Location: L689 (Stat tier cubes) with L781, L1215, L1367 (hollow markers 'white cubes')
- Evidence: 16 white cubes = 4 characters x 4 stats, all placed on dashboards at setup (L771). Hollow status is marked with two white cubes per hollow character; in a four-character game none are spare.
- Current text: When a character dies and is revived *hollow*, they block off the two furthest right spaces of the endurance bar with a marker such as white cubes.
- Proposed fix: "...block off the two furthest right spaces of the endurance bar with two hollow markers (use the Tier Four red cube from a stat track that has not reached tier four, or any two counters)." and add "8x Hollow markers" to the component list.
- Rationale: A marker must exist in the component list; white cubes are fully committed at four players.
- Gameplay impact: None.
- Decision needed: N

### C-015 · spelling · Minor · REQUIRED
- Location: L793; L849; L887; L979; L1517; L1664; L1880; L2017; L2021; L2043; L2045; L2053; L2456; L2504; L3082; L377
- Evidence: Typos: L793 'a read and a used side'; L849 'play mail', 'used up grade armour'; L887 'a characters' catalyst'; L979 'the tiles entry'; L1517 'the enemies block'; L1664 'wound token's'; L1880 'who's stats', 'its' attack options'; L2017 'starting decks deck size'; L2021 'blocked by train'; L2043 'The then are faced'; L2045 'reveal one an ambush card', 'min-boss'; L2053 'offer character's powerful rewards'; L2456/L2504 'Do no place'; L3082 'based on an the attacker attack option's'; L377 'desist in google docs'
- Current text: (see Evidence)
- Proposed fix: ready side; plate mail; used to upgrade armour; a character's catalyst; the tile's entry nodes; the enemy's block; wound tokens; whose stats; its attack options; starting deck size; blocked by terrain; They then are faced; reveal the ambush card; mini-boss; offer characters powerful rewards; Do not place; based on the attacker's attack option's; reside in Google Docs
- Rationale: Plain typographical errors; 'Do no place' and 'blocked by train' change sense.
- Gameplay impact: L2456/L2504 'Do no place' reads as a permission, not a prohibition
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

### C-042 · terminology · Minor · CLEAN-UP
- Location: L771; L849; L1131; L1171; L1179; L1886; L1892; L2195; L2295; L2358ff
- Evidence: 'The Bonfire' capitalised mid-sentence x10 (e.g. 771 'resting at The Bonfire'); '*bonfire*' x35; plain 'the bonfire' x27; 'Bonfire Tile' x48 in campaign lists; 'The Bonfire tile' (1131, 1171, 1179)
- Current text: The Bonfire / Bonfire Tile
- Proposed fix: the *bonfire* (lower-case keyword); 'bonfire tile' for the component; headings may read 'The Bonfire'
- Rationale: Game locations are common nouns (cf. fog gate, shop); capital 'The' mid-sentence is inconsistent with the keyword form.
- Gameplay impact: None
- Decision needed: N

### C-045 · terminology · Minor · REQUIRED
- Location: L771; L1451; L2314; L2316; L1920-1923; L1955-1956; L2303-2306; L2330-2331; L689; L1914; L2299
- Evidence: 'tier one/two' lower-case x60 in prose; 'Tier One/Two' x10 in table and heading labels; 'Tier one/two' mid-sentence (1451, 2314, 2316). Separately, 'tier' has two senses: stat tier (771 'from base tier to tier two', 1914) and treasure tier (1013 'tier two treasure deck').
- Current text: Tier one treasure deck (mid-sentence); 'tier two' (stat sense) unqualified
- Proposed fix: Lower-case 'tier one/two' in prose; Title Case only in headings and table row labels. Always qualify the stat sense as 'stat tier' ('stat tier two') and the treasure sense as 'tier two' ('tier two treasure', 'tier two shop').
- Rationale: Ambiguity: L771 'tier two' means a stat tier while L1013 'tier two' means a treasure deck.
- Gameplay impact: Misreading stat tiers as treasure tiers
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

### C-060 · terminology · Minor · CLEAN-UP
- Location: L801; L1720; L1744; L1780; L1876; L1846; L3194; L763; L805; L1814; L891; L1201; L1908; L373-379; L2225
- Evidence: 'reroll' x8 vs 're-roll' x2 (1846, 3194); 'back-up slot' x2 vs 'backup slot' (891); 'PvP' x10 vs 'player versus player (PvP)' (1201) vs 'player-versus-player (PvP)' (1908); 'rule set'/'ruleset'/'rule-set'; 'rule book'/'rulebook'/'rule-book'
- Current text: (variants)
- Proposed fix: reroll; back-up slot; define 'player versus player (PvP)' once (L1201) then 'PvP'; ruleset; rulebook
- Rationale: One spelling per compound.
- Gameplay impact: None
- Decision needed: N

### C-063 · terminology · Minor · CLEAN-UP
- Location: L787; L701; L793; L1351; L1600
- Evidence: 'the appropriate condition marker' / 'a staggered condition marker' (787) vs 'condition token' x10
- Current text: condition marker
- Proposed fix: condition token
- Rationale: Component name.
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

### D-039 · underspecified-deviation · Minor · OPTIONAL
- Location: manuscript.md 745, 1690, 1282 (Threat Level)
- Evidence: Core p.11 and V2 p.8 call the character value 'taunt level' and the enemy value 'threat level'. The manuscript uses 'threat' for both, so 'higher threat level' at 1690 (copied from Core p.24 'higher Taunt level') now reads as an enemy statistic.
- Current text: 7. Threat Level … the enemy moves towards the character with the higher threat level.
- Proposed fix: Characters have a taunt level; enemies have a threat level. (Restore 'taunt' at 745, 1003, 1275, 1277, 1289, 1690, 1694, 2192, 3056, 3058.)
- Rationale: Avoids one word meaning two different statistics; optional if the author prefers a single term and defines it.
- Gameplay impact: Clarity of targeting rules.
- Decision needed: Y

### F-087 · register-shift · Minor · CLEAN-UP
- Location: L769, L2191
- Evidence: Indefinite pronoun 'one': 'one must pay the cost in souls for the tier one upgrade' (L769); 'one can assume any damage dealt' (L2191)
- Current text: (i.e., to upgrade strength from base tier to tier two, one must pay the cost in *souls* for the tier one upgrade, and then the tier two upgrade).
- Proposed fix: Third person with a named actor: 'the character pays the tier one cost and then the tier two cost'. Set L769 as an *Example.*
- Rationale: 'one' is a third voice alongside players/characters.
- Gameplay impact: none
- Decision needed: N

### C-092 · example · Note · OPTIONAL
- Location: L849; L771; L1914; L1918-1923
- Evidence: Upgrade-limit example (849: limit two -> up to two upgrade cards) correct. Stat-tier examples (771 'pay... tier one upgrade, and then the tier two upgrade'; 1914 'two souls to reach tier one before paying four additional souls to reach tier two') match the basic Stat Tier Costs table (2, 4). The campaign table (4, 8) differs; the 1914 example sits in the basic chapter.
- Current text: (verified)
- Proposed fix: Add to §The Bonfire Tile (campaign): 'In campaign play the same example costs four then eight souls.'
- Rationale: Examples verified; one clarifying sentence recommended.
- Gameplay impact: None
- Decision needed: N

### F-094 · copied-prose · Note · OPTIONAL
- Location: L777–779 §Characters › Endurance Bar
- Evidence: Matches official text — close paraphrase (10-word runs)
- Current text: When a character spends one or more stamina, they add that number of stamina cubes… / When a character suffers one or more damage, they add that number of damage cubes…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: V2 p.9. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-095 · copied-prose · Note · OPTIONAL
- Location: L797 §Characters › Heroic Action
- Evidence: Matches official text — paraphrase (9-word run)
- Current text: A character may flip their heroic action token to the used side as a minor action…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: V2 p.9. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-096 · copied-prose · Note · OPTIONAL
- Location: L801 §Characters › Luck
- Evidence: Matches official text — close paraphrase (12-word run)
- Current text: A character may flip their luck token to the used side to reroll any attack or defence roll…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.11, p.15. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-097 · copied-prose · Note · OPTIONAL
- Location: L805 §Characters › Ember
- Evidence: Matches official text — paraphrase (11-word run)
- Current text: Ember tokens are placed face-up onto a character's dashboard when that player discards an ember card…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: V2 p.9. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

## Completion entries that apply (1) — approved at Gate 1

### [CMP-0001] Characters › Character Tokens › Estus Flask — Proposed Completion
- Current state: The TOC (line 65) lists an "Estus Flask" sub-heading under Character Tokens; no such sub-section exists in the body. The rule survives only in the DOCX page footer ("The character may flip their estus flask token to the used side as a major action to remove all damage cubes from their endurance bar. Stamina cubes are not removed."). The Character Tokens paragraph (line 793) says "There are three different types of character tokens: heroic actions, luck, and estus flask", then "Each character has one of each of the four following tokens", then lists Heroic Action, Luck and Ember; it also says ember tokens "should be placed in the condition token supply", while Character Setup step 5 (line 997) says "Place an ember token beside the character's board". The Character Turn (line 1830) calls the action "Drink Estus: Restore all of the character's health".
- Proposed completion:

  Replacement for the Character Tokens paragraph (line 793):

  > ## Character Tokens
  >
  > There are four types of character token: *heroic action*, *luck*, *estus flask* and *ember*. Each token has a ready side and a used side. The ready side is printed in brighter colours than the used side. A token's effect is available only while its ready side is face up. When a character uses a token's effect, the token must be flipped to its used side.
  >
  > Each character has one token of each type. The *heroic action*, *luck* and *estus flask* tokens begin the game ready, in their slots on the character dashboard. The *ember* token begins the game beside the dashboard and is placed in its slot only when the character becomes *embered* (see Embering).

  New sub-section, inserted after *Luck* and before *Ember* (after line 801):

  > ### *Estus Flask*
  >
  > A character may flip their *estus flask* token to the used side as a major action (*Drink Estus*) to remove all damage cubes from their endurance bar. Stamina cubes are not removed. *Hollow* markers are not removed. Condition tokens are not removed.
  >
  > The *estus flask* token is not restored when an encounter is *cleared*. It is flipped to the ready side only when the characters rest at the *bonfire*.

  Consequential edit to Character Turn › Major Action (line 1830): "*Drink Estus*: Remove all damage cubes from the endurance bar; flip *estus flask* face-down."
- Design rationale: The footer text is the only surviving source and already matches the manuscript's terminology (damage cubes, endurance bar, major action). Making the Ember token the fourth type resolves the "three types / four tokens" contradiction without changing play. "Health" in the Major Action list is replaced by the manuscript's own unit (damage cubes) so the action text and the token text agree.
- Mechanical impact: None on play. Clarifies that Estus does not clear hollow markers or conditions (both already stated indirectly in Death & Hollowing and Conditions).
- Follow-on changes required: Delete the DOCX footer paragraph. Character Setup step 5 (line 997) stands. Add "Estus flask" to the Glossary (CMP-0002). Regenerate TOC.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

