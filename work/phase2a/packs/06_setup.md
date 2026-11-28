# Drafting pack — chapter 06 (setup) — manuscript chapter "SETUP"

Source text: `work/phase2a/source/06_setup.md` (manuscript.md lines 985–1196).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 985.
- **Character Setup** · present — to audit · line 987.
- **Treasure Deck Setup** · present — to audit · line 1005.
- **Starting Treasure** · present — to audit · line 1007.
- **Common Treasure** · present — to audit · line 1011.
- **Class-specific Treasure** · present — to audit · line 1015.
- **Transposed Treasure** · present — to audit · line 1019.
- **Legendary Treasure** · present — to audit · line 1023.
- **Boss Treasure** · present — to audit · line 1027.
- **Tier One Treasure Deck** · present — to audit · line 1031.
- **Tier Two Treasure Deck** · present — to audit · line 1041.
- **Using Expansion Treasure** · present — to audit · line 1055.
- **(empty heading)** · ORPHAN — delete · line 1059: empty H2 used as page break
- **Shop Setup** · present — to audit · line 1061.
- **Start of Game Setup** · present — to audit · line 1063.
- **After Boss is Defeated:** · present — to audit · line 1075.
- **Bonfire Setup** · present — to audit · line 1091.
- **Encounter Setup** · present — to audit · line 1101.
- **Boss Selection** · present — to audit · line 1103.
- **Encounter tiles** · present — to audit · line 1111.
- **Encounter cards** · present — to audit · line 1119.
- **Using Expansion Encounters** · present — to audit · line 1139.
- **Setup After the mini-boss** · present — to audit · line 1143.
- **Setup After the main-boss** · present — to audit · line 1173.

## Audit findings mapped to this chapter (94)

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

### F-049 · external-reference · Blocker · CLEAN-UP
- Location: L1195 §Setup › Setup After the main-boss step 11
- Evidence: Cross-reference to an external booklet as a rules source: 'employing any special rules described in the mega-boss rule booklet'
- Current text: The characters now begin combat with the mega-boss employing any special rules described in the mega-boss rule booklet. If a character dies they are permanently removed from play…
- Proposed fix: REWRITE-IN-VOICE: 'The mega-boss encounter begins. The mega-boss's special rules (see §17) apply. A character who dies in this encounter is removed from the game. If every character dies, the party loses. If any character survives and the mega-boss is defeated, the party wins.'
- Rationale: The book must stand alone. §17 currently covers only Asylum Demon/Stray Demon — the remaining mega-boss special rules must be written into §17 or the reference resolves to nothing.
- Gameplay impact: none (voice). Content gap: §17 lacks special rules for Four Kings, Kalameet, Executioner's Chariot, Gaping Dragon, Guardian Dragon, Manus, Old Iron King, Vordt — flagged for the content audit.
- Decision needed: N

### F-066 · prose-crossref · Blocker · CLEAN-UP
- Location: L1195 §Setup › Setup After the main-boss step 11
- Evidence: Prose cross-reference: 'described in the mega-boss rule booklet'
- Current text: described in the mega-boss rule booklet
- Proposed fix: '(see §17)' once §17 is complete — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: DANGLING — external; nearest in-book target §17 Boss Special Rules (incomplete). Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### A-003 · undefined-state · Major · REQUIRED
- Location: GAMEPLAY › Souls (manuscript.md lines 1395–1399); Encounter Resolution (line 1331)
- Evidence: manuscript.md:1207, 1309, 1323, 1331, 1395–1399, 1145
- Current text: Dropped souls are lost forever if the character who dropped them dies before reclaiming the souls.
- Proposed fix: Souls dropped by a character remain on the encounter tile where they were dropped. Souls dropped at the moment of death are not forfeited by that death; they are returned to the supply only if the same character dies again before reclaiming them. When an encounter is failed, every living character drops their souls on that tile in addition to any souls already there. A character reclaims their own dropped souls only by surviving to clear the encounter on the tile where the souls lie.
- Rationale: A hollow character's death simultaneously drops souls (1207) and fails the encounter (1305), so the literal text ('dies before reclaiming') forfeits the souls dropped by that very death. Line 1331 also makes all characters drop souls, including characters whose souls already lie on the tile. Hollowed Edition keeps dropped souls until a second death.
- Gameplay impact: Whether a hollow character's death wipes their souls is the single largest soul swing in the game and is currently ambiguous.
- Decision needed: N

### A-043 · procedural · Major · REQUIRED
- Location: TILES & NODES › Terrain › Gravestones (manuscript.md line 943) vs BOSS ENCOUNTERS › Boss Behaviour Cards (line 2125)
- Evidence: manuscript.md:933–943, 1117, 2125; DS-Core-Rules-lores.txt p.28 step 3 (reveal one random behaviour card per gravestone at boss start)
- Current text: Boss Behaviour scrying allows the players to reveal the top card of the upcoming boss's Behaviour Deck.
- Proposed fix: The boss behaviour deck is constructed as described in Boss Behaviour Cards during Encounter Setup, when the boss's cards are placed on the boss tile, and is kept face-down there. Boss Behaviour scrying reveals the top card of that deck and returns it to the top or the bottom.
- Rationale: Scrying happens when an encounter is cleared, but the manuscript builds the boss deck only at the start of the boss encounter (2125), so there is no deck to scry. Alternative: replace Boss Behaviour scrying with the official reveal of one random behaviour card per gravestone when the boss encounter starts.
- Gameplay impact: One of the four gravestone options is unusable as written.
- Decision needed: Y

### A-045 · undefined-state · Major · REQUIRED
- Location: SUMMONS › Invaders › Invader Tokens step 1 (manuscript.md line 1999); Boss Death (line 2195)
- Evidence: manuscript.md:1999–2011, 1147, 2195; DS-Phantoms-Rules-lores.txt p.11 ('if there are no invader tokens already in play and there is at least one unexplored tile')
- Current text: Embered characters provoke an invader if no invasion has occurred yet.
- Proposed fix: An invasion is provoked the first time a character becomes embered while at least one face-down encounter card is on the tiles. If characters become embered when no face-down encounter card exists (for example when a boss is slain), the invasion is provoked when encounter cards are next dealt. At most one invasion occurs before the mini-boss and at most one after it.
- Rationale: Boss Death embers everyone at a moment when the old encounter cards have been cleared and the new ones not yet dealt, so the token-placing procedure (2007) has nothing to place on. 'If no invasion has occurred yet' also leaves it open whether the limit is one per game or one per leg. Alternative: one invasion per game.
- Gameplay impact: Determines whether advanced invaders ever appear in a standard game.
- Decision needed: Y

### A-046 · undefined-state · Major · REQUIRED
- Location: SETUP › Shop Setup › After Boss is Defeated (manuscript.md lines 1077–1089); EQUIPMENT › Embers (line 891)
- Evidence: manuscript.md:891, 1039, 1049, 1067–1089, 1935
- Current text: Draw tier one treasure cards one at a time to restock tier one shop: 3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells.
- Proposed fix: When a shop is restocked, every card remaining in that shop is placed on the bottom of its treasure deck before new cards are drawn. Ember cards remaining in the tier one shop stay in the shop and are never replaced; no ember card is ever added to a shop after setup.
- Rationale: Nothing says what happens to unsold shop cards on restock, and the ember restriction ('limited supply', 891) only works if the restock neither adds nor removes embers. Alternative: unsold cards remain and the restock only tops up to the quotas.
- Gameplay impact: Shop contents after the first boss are undefined.
- Decision needed: Y

### A-048 · undefined-state · Major · REQUIRED
- Location: CAMPAIGN PLAY › Sparks (manuscript.md line 2235); SETUP › Setup After the mini-boss steps 10–11 (lines 1167–1169); CAMPAIGNS (Gauntlet 2502–2546, Facing the Abyss S1 2564, Playing with Fire S1 2962)
- Evidence: manuscript.md:1167–1169, 2235, 2314, 2564, 2962, 2502–2546; DS-Darkroot-Rules-web.txt p.11 ('The party proceeds to Section 2 when the encounter is defeated'); DS-Phantoms-Rules-lores.txt p.19
- Current text: characters no longer rest at the bonfire for free after defeating a boss except for the final boss of each section.
- Proposed fix: When a section ends with an encounter rather than a boss, clearing that encounter counts as defeating the section's final boss: the characters gain one spark, rest at the bonfire without spending a spark, restock the shops and set up the next section. When a section contains more than one boss, the characters gain one spark for each boss slain but rest without spending a spark only after the section's final boss.
- Rationale: Four campaign sections end in a named encounter and the Gauntlet has no bosses at all; sparks, free rests, restocks and section setup are all keyed to 'boss' in the manuscript.
- Gameplay impact: Three supplied campaigns cannot progress between sections as written.
- Decision needed: N

### A-049 · contradiction · Major · REQUIRED
- Location: SETUP › Setup After the main-boss step 11 (manuscript.md line 1195) vs CAMPAIGNS › Demon Hunting Section Four (line 2644), Big Game Hunting (lines 3012–3034)
- Evidence: manuscript.md:1195, 2235, 2644, 2996, 3018–3034
- Current text: If a character dies they are permanently removed from play. If all characters die, the players lose the game. If any character survives to defeat the mega-boss, the players win the game.
- Proposed fix: The permanent-death and victory rules of the mega-boss encounter apply only when the mega-boss is the final boss of the game. In campaign play a mega-boss that is not the campaign's final boss is fought under the normal boss rules; when slain it awards a spark, ember tokens and boss treasure like any other boss, and the campaign continues.
- Rationale: Demon Hunting places the Stray Demon in Section Four of five, and Big Game Hunting has three mega-bosses; under the literal text the game ends at the first of them.
- Gameplay impact: Two campaigns end early or lose characters permanently mid-campaign.
- Decision needed: Y

### A-050 · contradiction · Major · REQUIRED
- Location: SETUP › Setup After the main-boss step 11 (manuscript.md line 1195) vs Death & Hollowing (line 1223) and Objective & Loss Conditions (line 1201)
- Evidence: manuscript.md:1191, 1195, 1201, 1223, 1305; DS-EC-Rules-Web.txt p.9 and DS-BDK-Rules-web.txt p.9 (official: no free rest after the level 4 encounter; retries cost a spark)
- Current text: If a character dies they are permanently removed from play. If all characters die, the players lose the game.
- Proposed fix: During the final mega-boss encounter the Death & Hollowing rules are replaced: a character who dies is removed from play for the rest of the game, the encounter is not failed, and the players lose only when every character is dead. Sparks cannot be spent during or after the final mega-boss encounter.
- Rationale: A hollow character's death normally fails the encounter and forces a rest (1223); the mega-boss text instead removes the character permanently without saying that the failure rule is suspended. Alternative: delete the permanent-death sentence and let the mega-boss follow normal boss rules with spark-costed retries, as the official mega-boss booklets do.
- Gameplay impact: The climactic fight has two incompatible death rules.
- Decision needed: Y

### A-057 · contradiction · Major · REQUIRED
- Location: SETUP › Encounter cards step 4 (manuscript.md line 1135) and Setup After the mini-boss step 8 (line 1163) vs Treasure Rewards (line 1451)
- Evidence: manuscript.md:1135, 1163, 1313, 1445–1451, 2291–2293, 2340
- Current text: Deal one tier one treasure per character face-down to each encounter tile. / Draw cards from the Tier one treasure deck before defeating the mini-boss, and Tier two treasure deck thereafter.
- Proposed fix: The treasure cards dealt face-down to an encounter tile during setup are that encounter's treasure reward. When the encounter is cleared for the first time, each character takes one of those cards; the cards are not drawn from the deck at that time. In campaign play, treasure cards already dealt to tiles are not replaced when the bonfire ascetic is burnt.
- Rationale: Setup pre-deals one card per character to every tile, yet Treasure Rewards says to draw from the deck on clearing; a party would collect both. The pre-deal is the only reading under which 'Characters receive their treasure card reward even if they died' and the campaign tier rules (2291) are mechanical. Alternative: delete the pre-deal steps and draw on clearing.
- Gameplay impact: Doubles treasure income if both are applied.
- Decision needed: Y

### A-069 · undefined-state · Major · REQUIRED
- Location: SETUP › Shop Setup (manuscript.md line 1069); EQUIPMENT › Equipment Cards (line 811)
- Evidence: manuscript.md:811, 1069, 1079, 1085, 1876
- Current text: 3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells.
- Proposed fix: For stocking the shop: a shield is a weapon-slot card bearing the shield icon; a spell is a card whose art shows a scroll; an upgrade is a card with the weapon-upgrade or armour-upgrade icon, including rings and titanite; every other weapon-slot card, including catalysts and throwable items, is a weapon; an armour card is a card with the armour icon. A shield counts as equipment in the other hand for the two-handed rule.
- Rationale: Five shop categories are used but only armour, weapon and spell are defined; 'shield' and 'item' never are, and catalysts and consumables fall between categories.
- Gameplay impact: Shop stocking is the only treasure source before the first boss.
- Decision needed: Y

### A-075 · contradiction · Major · REQUIRED
- Location: SETUP › Legendary Treasure (manuscript.md line 1025) vs Tier Two Treasure Deck step 6 (line 1053) and After Boss is Defeated step 2.3 (line 1089)
- Evidence: manuscript.md:1025, 1053, 1089; DS-Core-Rules-lores.txt p.9; DS-Characters-Rules-lores.txt p.7 (legendary armour added at the same time as legendary weapons, after the mini boss)
- Current text: All legendary treasure cards are shuffled during set-up, after Andre's Shop is stocked, and five unrevealed legendary treasures are then shuffled into the tier two treasure deck.
- Proposed fix: After the tier two shop is first stocked, shuffle five random legendary treasure cards into the tier two treasure deck and return the rest to the game box. Legendary cards are not added at game setup.
- Rationale: Three passages give two different moments (game setup vs after the mini-boss); step 2.3 is also truncated and names no destination.
- Gameplay impact: Determines whether legendaries can be found before the first boss.
- Decision needed: N

### A-088 · arithmetic · Major · REQUIRED
- Location: SETUP › Encounter tiles step 1 (manuscript.md line 1113)
- Evidence: manuscript.md:721–723, 1113–1115; DS-Core-Rules-lores.txt p.8
- Current text: arrange them so they are connected in a two by six tile grid with the bonfire tile and mini-boss tile on opposite corners.
- Proposed fix: Arrange the six tiles (the bonfire tile, four encounter tiles and the mini-boss tile) in a grid of two rows of three, with the bonfire tile and the mini-boss tile in opposite corners.
- Rationale: Six tiles cannot form a 2×6 grid; the intended layout is 2×3.
- Gameplay impact: Setup instruction is impossible as printed.
- Decision needed: N

### A-093 · undefined-state · Major · REQUIRED
- Location: SETUP › Setup After the main-boss step 5 (manuscript.md line 1183)
- Evidence: manuscript.md:1029, 1183, 1189–1195; DS-EC-Rules-Web.txt p.8 (official Level 4 reward: 8 souls per character); DS-BDK-Rules-web.txt p.4 (2x Kalameet Treasure Cards)
- Current text: Shuffle mega-boss Items and deal one face-down to the encounter tile.
- Proposed fix: Deal one of the mega-boss's boss treasure cards face-down to the Level 4 encounter tile as that encounter's treasure reward; the remaining mega-boss treasure cards are the reward for slaying the mega-boss.
- Rationale: 'Items' is used nowhere else; the only mega-boss cards are its boss treasure cards. Alternative: deal one tier two treasure card per character as for other tiles and keep all boss treasure for the kill.
- Gameplay impact: Level 4 encounter reward is undefined.
- Decision needed: Y

### A-094 · undefined-state · Major · PROPOSED
- Location: CAMPAIGNS › Call of the Abyss Section Four (manuscript.md lines 2712–2714); Into the Depths Sections Four–Five (lines 2932, 2940–2942); Demon Hunting Section Four (line 2642); Big Game Hunting (lines 3016–3032)
- Evidence: manuscript.md:1179, 1193, 2642, 2712–2714, 2932, 2940–2942, 3016–3032; DS-EC-Rules-Web.txt p.7–8 and DS-BDK-Rules-web.txt p.7–8, p.15 (Level 4 encounters are played on the encounter side of the mega-boss game board)
- Current text: Level 4 Encounter / Level 4 Encounter / The Four Kings (Mega Boss)
- Proposed fix: In campaign play a Level 4 encounter is always played on the encounter side of a mega-boss game board placed in the section's tile sequence. When a section lists two Level 4 encounters, the second is played on a second mega-boss board if one is available; otherwise the same board is cleared and reused after the first encounter is cleared. The board is flipped to its boss side only when the section's mega-boss is reached.
- Rationale: The basic game puts the single Level 4 encounter on the mega-boss tile (1179); campaigns list Level 4 encounters mid-section and twice in a row with no board rule.
- Gameplay impact: Four campaign sections cannot be laid out as written.
- Decision needed: Y

### A-115 · omission · Major · PROPOSED
- Location: BOSS SPECIAL RULES (manuscript.md lines 2199–2213); Setup After the main-boss step 11 (line 1195)
- Evidence: manuscript.md:1195, 1640, 2199–2213; DS-BDK-Rules-web.txt p.12–13 (Strafe cards, Signature cards, Calamity); DS-EC-Rules-Web.txt p.12–15 (track deck, No Starting Health, Death Race, Central Wall, Chariot Crash)
- Current text: The characters now begin combat with the mega-boss employing any special rules described in the mega-boss rule booklet.
- Proposed fix: Replace the external reference with sections under Boss Special Rules for each supported mega-boss. For the supplied booklets: Black Dragon Kalameet (Signature cards always in the deck; Strafe deck; Strafe attack targets the nodes shown and lands the boss on the landing node, pushing characters there to any adjacent node; Calamity condition). Executioner's Chariot (track behaviour deck resolved in numbered order; the boss has no health until every other enemy is slain; track attacks target the nodes shown and push hit characters to untargeted adjacent nodes; the board centre is treated as a gravestone node; on heat-up remove the chariot, flip the data card and switch to the heat-up deck).
- Rationale: The manuscript's own goal (line 375) is a rulebook that needs no other text, yet nine mega-bosses are listed and only the Asylum/Stray Demon is covered. The Calamity condition (1640) is defined but the Strafe mechanic that delivers it is not.
- Gameplay impact: Mega-boss games are unplayable from the manuscript alone.
- Decision needed: N

### B-022 · undefined-value · Major · REQUIRED
- Location: L1069/L1079/L1085 (Shop Setup) with L823-829 (Equipment Cards), L747-753 (Equipment Slots), L1769 (Parry)
- Evidence: The stock list requires '2 shields' per shop and the parry rule requires 'a shield as their left weapon', but the card-typing rules define only one-handed weapon, two-handed weapon, armour (by icon) and spell (by scroll art). No rule says how a shield is recognised; shields are weapon-typed cards in 1E (East-West Shield appears in the manuscript's own weapons table, L3244).
- Current text: Equipment cards include weapons, spells, shields, armour, and items which the character equips to improve their combat capabilities. ... 3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells.
- Proposed fix: Add to Equipment Cards: "A shield is a one-handed weapon card that shows a block or resist value and has no attack option. Shields count as weapons for equipment slots and as shields for shop stocking and parrying."
- Rationale: The shop and parry procedures cannot be executed without a test for 'shield'.
- Gameplay impact: Makes the 12-card stock list and the parry prerequisite determinable.
- Decision needed: Y

### C-018 · hedge · Major · REQUIRED
- Location: L845; L1057; L1141; L2041; L2053; L2596; L2664; L2720; L2766; L2812; L2884; L2948; L2994
- Evidence: 14 'should' in optional-content advice, e.g. L845 'Players should include all equipment cards from expansions'; L1141 'players should include only the encounter cards from the same set'; L2041 'Groups with new players should default to leaving mimics out... Experienced players should include mimics'; L2596ff 'players should add the Explorers and Characters expansions if available' (x8)
- Current text: Players should include / should add / should default to
- Proposed fix: Rewrite as permissions or labelled recommendations: 'Players may include equipment cards from every expansion they own.' / 'By default, build each encounter deck only from cards of the next boss's set.' / 'Mimics are an optional rule; the players decide during setup whether to use them.' / campaign lines: 'Recommended: Explorers and Characters expansions.' Full per-line rewrites in C_report.md Task 2.
- Rationale: 'Should' leaves it unclear whether expansions are required, optional or recommended. Lawbook voice uses must/may or a labelled 'Recommended' line.
- Gameplay impact: Which components a group must own to play a campaign
- Decision needed: Y

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

### C-070 · table-text · Major · REQUIRED
- Location: L1951-1957; L2326-2334; L2348; L1025; L2322
- Evidence: Basic Shop Price Table: Boss Treasure purchase 'N/A', sell 6. Campaign table: Boss Treasure purchase '-', sell 4; extra rows 'Legendary Shop: 4 + Boss Treasure / sell 4' and 'Bonfire Ascetic 16 / -'. Prose: transposition costs a boss treasure + four souls (2348, matches); bonfire ascetic 16 souls (2293/2316/2340, matches); L2322 'Legendary Treasures are now only available through transposition' but the table calls it a 'Shop'; legendary sell value 4 appears nowhere in prose.
- Current text: Boss Treasure sell 6 (basic) vs 4 (campaign); 'N/A' vs '-'; 'Legendary Shop'
- Proposed fix: Confirm whether the campaign boss-treasure sell value (4) is a deliberate change; if so state it in §Blacksmith Andre's Shop (campaign); use one null marker ('-') in both tables; rename row 'Legendary (transposition)'; add a prose line for selling legendary treasure or delete the sell value.
- Rationale: Tables must agree with prose and with each other except where a change is stated.
- Gameplay impact: Boss treasure sale income differs by 2 souls between modes
- Decision needed: Y

### C-080 · cross-ref · Major · REQUIRED
- Location: L1151; L1111-1117
- Evidence: Setup After the mini-boss step 4: 'Place the fog-gate as before.' The initial Encounter tiles procedure (1111-1117) never places the fog gate; the only placement instructions are L1179 (mega-boss) and §The Fog Gate (2063).
- Current text: Place the fog-gate as before.
- Proposed fix: Add to Encounter tiles (after L1117): '4. Place the fog gate token on the doorway of the mini-boss tile.' Then L1151: 'Place the fog gate token on the doorway of the main-boss tile.'
- Rationale: Reference to a step that does not exist.
- Gameplay impact: Fog gate never placed in the first half of the game
- Decision needed: N

### C-081 · cross-ref · Major · REQUIRED
- Location: L1195; L2199-2213
- Evidence: 'employing any special rules described in the mega-boss rule booklet' - external reference; §BOSS SPECIAL RULES covers only Asylum Demon and Stray Demon
- Current text: described in the mega-boss rule booklet
- Proposed fix: 'employing that boss's special rules (see §Boss Special Rules)' - and complete §Boss Special Rules for every listed mega-boss, or state explicitly that each mega-boss's expansion rules apply
- Rationale: A self-contained rulebook (L375 goal) cannot point to an external booklet.
- Gameplay impact: None
- Decision needed: Y

### C-088 · cross-ref · Major · REQUIRED
- Location: L1223; L1906; L1195; L1341
- Evidence: Hollow death: 'any character with *hollow* status dies, then the characters are forced to immediately spend one *spark* and rest' (1223, 1341) vs 'revives *lost* characters who have been removed from play due to dying while *hollow*' (1906) vs mega-boss 'If a character dies they are permanently removed from play' (1195)
- Current text: (three statements)
- Proposed fix: Make §Death & Hollowing the single source: define *lost*, state the forced rest, and have §Resting at the Bonfire and §Setup After the main-boss cite it (with the mega-boss exception stated as an exception).
- Rationale: Three sections describe the same event with different consequences.
- Gameplay impact: Whether the encounter ends immediately when a hollow character dies
- Decision needed: Y

### C-090 · example · Major · REQUIRED
- Location: L1113
- Evidence: 'Draw four random encounter tiles and arrange them so they are connected in a two by six tile grid with the bonfire tile and mini-boss tile on opposite corners' - 4 encounter tiles + bonfire tile + mini-boss tile = 6 tiles, which is a two-by-three grid; two by six would be 12 tiles. L1115 then describes 'a linear route along four sequential encounter tiles'.
- Current text: a two by six tile grid
- Proposed fix: 'a two-by-three grid of six tiles, with the bonfire tile and the mini-boss tile in opposite corners'
- Rationale: Arithmetic error in a setup instruction.
- Gameplay impact: Players cannot lay out the described grid
- Decision needed: N

### C-100 · heading · Major · REQUIRED
- Location: L1802; L1804; L1820; L1806-1834; L1075
- Evidence: Procedural steps set as H3 headings with trailing punctuation: '### Recover one stamina.' (1802), '### Minor Actions:' (1804), '### Major Action:' (1820), with the actions below as blockquotes joined by bold AND/OR; '### After Boss is Defeated:' (1075)
- Current text: ### Recover one stamina. / ### Minor Actions: / ### Major Action:
- Proposed fix: Replace 1802-1834 with one numbered procedure under '## Character Turn Sequence': '1. Recover one stamina. 2. Minor actions (any number, in any order): *walk*, *run*, *equip*, *heroic action*. 3. Major action (one): *attack*, *rest*, *drink estus*, *ember*.' Rename 1075 'Restocking After a Boss is Defeated'.
- Rationale: Headings are labels, never sentences or list items; no trailing punctuation.
- Gameplay impact: None
- Decision needed: N

### D-006 · underspecified-deviation · Major · REQUIRED
- Location: manuscript.md 1069, 1079, 1085 (Shop Setup)
- Evidence: Official card types are starting, common, class, transposed, legendary, boss (Core p.12); slots are one-handed, two-handed, armour (V2 p.10). 'Shield' and 'spell' are not card types; several shields carry attack options and spells occupy weapon slots. The stocking formula cannot be applied to a card deterministically.
- Current text: 3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells.
- Proposed fix: For shop stocking a card is classed in the first matching category: upgrade (upgrade icon); spell (scroll art); shield (weapon-slot card with a block or resist value and no attack dice); armour (armour icon); weapon (any other weapon-slot card). Draw cards until each category is filled; set aside cards of a filled category and shuffle them back afterwards.
- Rationale: The fixed-composition shop is original to the manuscript and replaces the 1E blind draw and the V2 four-card display; it needs a classification rule for the official card pool.
- Gameplay impact: Shop stocking is the game's main equipment source.
- Decision needed: N

### D-007 · hybrid · Major · REQUIRED
- Location: manuscript.md 1195 vs 1201 (Objective & Loss Conditions)
- Evidence: BDK/EC p.10 apply the standard boss rules (party defeated → rest at the bonfire, spark spent). The manuscript's Objective says the players lose only when all characters are dead and no sparks remain, but the mega-boss step says a character who dies is permanently removed and all dead = loss regardless of sparks.
- Current text: If a character dies they are permanently removed from play. If all characters die, the players lose the game.
- Proposed fix: A character who dies in the mega-boss encounter is removed from play for the remainder of that encounter. If every character dies, the encounter is failed and the characters rest at the bonfire at the cost of one spark; the mega-boss encounter is then set up again.
- Rationale: Reconciles the mega-boss rule with the manuscript's own loss condition and with the official mega-boss booklets; the alternative is to keep sudden death and amend the Objective.
- Gameplay impact: Decides whether sparks matter in the final fight.
- Decision needed: Y

### D-015 · dropped-rule · Major · REQUIRED
- Location: manuscript.md 1113–1117 (Encounter tiles) and 1152 (Setup After the mini-boss)
- Evidence: Core p.8 step 1: 'Take the Fog Gate token and place it on an empty portion of a wall on the tile farthest from the Bonfire tile.' The manuscript's initial tile setup never places the fog gate; step 4 after the mini-boss says 'Place the fog-gate as before', referring to a step that does not exist.
- Current text: Arrange the doorways of the encounter tiles so there are two open doorways that connect to an adjacent tile. This will create a linear route along four sequential encounter tiles between bonfire and boss tiles.
- Proposed fix: Place the fog gate token on the doorway between the fourth encounter tile and the boss tile.
- Rationale: The fog gate drives the manuscript's shortcut rule (2066) and campaign note (2230); its initial placement is a dropped official setup step.
- Gameplay impact: Setup cannot be completed as written.
- Decision needed: N

### D-032 · underspecified-deviation · Major · REQUIRED
- Location: manuscript.md 1183 (Setup After the main-boss, step 5)
- Evidence: No component called 'mega-boss Items' exists in the manuscript or in BDK/EC p.4; the official level 4 encounter rewards 8 souls per character (BDK/EC p.8) and no treasure.
- Current text: Shuffle mega-boss Items and deal one face-down to the encounter tile.
- Proposed fix: Deal one tier two treasure card per character face down to the level 4 encounter tile.
- Rationale: Brings the level 4 tile into line with the manuscript's own pre-dealt treasure rule (1135, 1163); alternatively the step is deleted.
- Gameplay impact: Level 4 reward.
- Decision needed: Y

### F-010 · external-reference · Major · CLEAN-UP
- Location: L1057 §Setup › Using Expansion Treasure
- Evidence: Product reference as framing: 'DStBG has many expansion sets available of which many include new treasure cards. Players should include…'
- Current text: DStBG has many expansion sets available of which many include new treasure cards. Players should include all treasure cards from expansion sets in their appropriate type of treasure deck as above.
- Proposed fix: REWRITE-IN-VOICE: 'Treasure cards from every expansion in the party's collection are sorted into the tier one and tier two decks by the rules in §6.2.'
- Rationale: The sentence describes the product line rather than stating the rule; 'as above' is a loose cross-reference.
- Gameplay impact: none
- Decision needed: N

### F-011 · external-reference · Major · CLEAN-UP
- Location: L1141 §Setup › Using Expansion Encounters
- Evidence: Product reference, advisory 'should', and an inline example: 'DStBG has many expansion sets available which include new encounter cards. By default, players should include only…'
- Current text: DStBG has many expansion sets available which include new encounter cards. By default, players should include only the encounter cards from the same set as the boss they will face next. For example, if the players selected the Gargoyle… However, players may elect to shuffle all encounter cards from available expansion sets together if they prefer more variety.
- Proposed fix: REWRITE-IN-VOICE: 'Each encounter deck contains only the encounter cards from the set of the next boss. The party may instead agree during setup to build each deck from all encounter cards in its collection.' Move the Gargoyle/Sif sentence to a labelled *Example.*
- Rationale: Rule first, option second, example set apart.
- Gameplay impact: none
- Decision needed: N

### F-012 · tone · Major · CLEAN-UP
- Location: L1107 §Setup › Boss Selection step 2
- Evidence: Conversational hedging: 'Players may now decide if they wish to pursue a longer adventure ending in an epic battle with a mega-boss if they like.'
- Current text: Players may now decide if they wish to pursue a longer adventure ending in an epic battle with a mega-boss if they like.
- Proposed fix: REWRITE-IN-VOICE: 'The party may add a mega-boss as the final boss (see §6.7).'
- Rationale: 'if they wish … if they like' doubles the permission; 'epic battle' is flavour in a procedure.
- Gameplay impact: none
- Decision needed: N

### F-013 · tone · Major · CLEAN-UP
- Location: L1109 §Setup › Boss Selection step 3
- Evidence: Advisory framing and conditional mood: 'For added challenge the players may forgo choice and instead randomly determine… This would be repeated…'
- Current text: For added challenge the players may forgo choice and instead randomly determine the bosses they will oppose by blindly shuffling available mini-boss data cards then revealing one at random. This would be repeated for the main-boss cards. If players want to pursue a mega-boss, this choice can also be randomised in the same way.
- Proposed fix: REWRITE-IN-VOICE: 'The party may instead select each boss at random: shuffle the data cards of the eligible bosses of that type and reveal one.'
- Rationale: One sentence states the option; the motive ('for added challenge') is advice.
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

### F-089 · tone · Major · CLEAN-UP
- Location: L765, L979, L1131, L1159, L1201, L1461, L1479, L1666, L1880, L2065, L2169, L2596 ff.
- Evidence: 'should' used as a rule modal: 'players should not interact with their character's inventory cards' (L765); 'Players should fill the basic nodes furthest from the tiles entry' (L979); 'Encounter levels should increase' (L1131); 'the character should mark the equipped item' (L1880); 'the fog gate tile should be removed' (L2065); 'The target character model should remain static' (L2169); 'players should add the Explorers and Characters expansions if available' (campaign headers ×9).
- Current text: Once the encounter has started players should not interact with their character's inventory cards.
- Proposed fix: Modal policy (Voice Guide §2): 'must' for obligations, 'may' for permissions, 'cannot' for prohibitions, 'is/are' for states. E.g. 'During an encounter the inventory cannot be accessed.'; 'Trap tokens are placed first on the basic nodes furthest from the entry.'; 'Encounter levels increase from the tile adjacent to the *bonfire* tile towards the boss tile.'; 'Mark the item with a red cube.'; campaign headers: 'Recommended additions: Explorers, Characters.'
- Rationale: 'should' is advisory and leaves the rule optional.
- Gameplay impact: none
- Decision needed: N

### A-004 · undefined-state · Minor · OPTIONAL
- Location: GAMEPLAY › Death & Hollowing (manuscript.md line 1213)
- Evidence: manuscript.md:1213, 1223, 1003
- Current text: If any character survives to clear an encounter, then the characters who died in that encounter are revived in a hollow state.
- Proposed fix: A character adventuring alone never becomes hollow: when that character dies, the encounter is failed and the character must spend a spark to rest at the bonfire.
- Rationale: The revival branch requires a surviving character; a solo death therefore always falls to the failed-encounter branch, which costs a spark. Stating this explicitly removes the question of whether a solo character ever hollows.
- Gameplay impact: Solo players need to know that every death costs a spark (the official 1E outcome).
- Decision needed: N

### A-014 · undefined-state · Minor · OPTIONAL
- Location: SETUP › Character Setup step 7 (manuscript.md line 1001); Encounter Start step 8 (line 1275); Encounter Turn Order step 2 (line 1289)
- Evidence: manuscript.md:1001, 1275, 1289, 3056–3058
- Current text: Each character takes their turn one-by-one in descending threat value.
- Proposed fix: If two or more characters share a threat value, the players choose which of them receives the aggro token and the order in which the tied characters take their turns.
- Rationale: Several character dashboards share threat values; no tie-break is given for either the aggro assignment or the turn order.
- Gameplay impact: Common with two characters of the same class family; cheap to fix.
- Decision needed: N

### A-047 · undefined-state · Minor · OPTIONAL
- Location: GAMEPLAY › Sparks (manuscript.md lines 1247–1253); Boss Death (line 2195)
- Evidence: manuscript.md:715, 1093, 1249, 2195, 2233; DS-Core-Rules-lores.txt p.33 (campaign maximum = starting sparks)
- Current text: Defeating a mini-boss or main-boss provides one additional spark.
- Proposed fix: The spark dial never shows more sparks than the characters' starting number; a spark gained beyond that maximum is lost.
- Rationale: The campaign chapter sets this maximum (2233) but the basic game does not; a solo character would reach six or seven, beyond the physical dial. Alternative: no maximum, track overflow with a token.
- Gameplay impact: Solo and two-character basic games only.
- Decision needed: Y

### A-051 · contradiction · Minor · REQUIRED
- Location: CAMPAIGN PLAY › Transposition (manuscript.md line 2346)
- Evidence: manuscript.md:1169, 2235, 2346
- Current text: Transposition is only available after the characters spend a spark to rest at the bonfire.
- Proposed fix: Transposition is available whenever the characters rest at the bonfire after the final boss of the first section has been defeated, whether or not a spark was spent for that rest.
- Rationale: The rest that immediately follows a section's final boss is free (2235, 1169), so the literal text denies transposition at the first moment it is unlocked.
- Gameplay impact: Delays the first legendary purchase by one spark for no evident reason.
- Decision needed: N

### A-052 · contradiction · Minor · CLEAN-UP
- Location: SETUP › Character Setup step 5 (manuscript.md line 997) vs CHARACTERS › Character Tokens (line 793)
- Evidence: manuscript.md:793, 997
- Current text: Place an ember token beside the character's board. / The ember tokens ... should be placed in the condition token supply at the start of the game.
- Proposed fix: Place the ember tokens in the token supply.
- Rationale: Two setup locations for the same token.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-065 · terminology · Minor · CLEAN-UP
- Location: SETUP › Tier One / Tier Two Treasure Deck (manuscript.md lines 1033–1045)
- Evidence: manuscript.md:1013, 1021, 1033–1045
- Current text: Include all common treasures without a required statistic =\> 25.
- Proposed fix: Include every common treasure card whose stat requirements are all below 25. / Include every common treasure card with at least one stat requirement of 25 or more.
- Rationale: '=\>' is a pandoc escape of '=>' which is itself the wrong operator (≥). Line 1013 states the rule correctly in words.
- Gameplay impact: Cosmetic, but '=>' reads as 'implies'.
- Decision needed: N

### A-076 · contradiction · Minor · REQUIRED
- Location: SETUP › Legendary Treasure (manuscript.md line 1025) vs Shop Setup › After Boss is Defeated step 2 (lines 1083–1089)
- Evidence: manuscript.md:1025, 1083–1089, 1935
- Current text: These represent exceedingly rare relics that do not appear in every game and cannot be purchased.
- Proposed fix: If a legendary treasure card is drawn while stocking a shop, shuffle it back into the tier two treasure deck and draw again.
- Rationale: Once legendaries are in the tier two deck, a later restock (before a mega-boss) draws from that deck and would put a legendary in the shop.
- Gameplay impact: Rare; only affects mega-boss games.
- Decision needed: N

### A-089 · omission · Minor · REQUIRED
- Location: SETUP › Encounter tiles (manuscript.md lines 1111–1117); Setup After the mini-boss step 4 (line 1151); BOSS ENCOUNTERS › The Fog Gate (line 2065)
- Evidence: manuscript.md:719, 1111–1117, 1151, 2065; DS-Core-Rules-lores.txt p.8
- Current text: Place the fog-gate as before.
- Proposed fix: Encounter tiles step 3: Place the fog gate token on the doorway of the boss tile.
- Rationale: The fog gate is a component, is moved by The Fog Gate rule and is placed 'as before' after the mini-boss, but the initial setup never places it.
- Gameplay impact: Setup omission.
- Decision needed: N

### A-092 · omission · Minor · CLEAN-UP
- Location: GAME COMPONENTS › Cards (manuscript.md lines 631–667)
- Evidence: manuscript.md:631–667, 1137, 2045; DS-Explorers-Rules-Web.txt p.4 (5x Mimic Ambush Cards); DS-Phantoms-Rules-lores.txt p.5 (invader tokens)
- Current text: (no entry)
- Proposed fix: Add to Cards: 5x Ambush cards (Explorers). Add to Tokens: 6x Standard invader tokens, 6x Advanced invader tokens, 3x Blank invader tokens (Phantoms).
- Rationale: Ambush cards and invader tokens are used by the rules but absent from the component list.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-095 · inherits-official-silently · Minor · OPTIONAL
- Location: SETUP › Setup After the main-boss step 3 (manuscript.md line 1179)
- Evidence: manuscript.md:1179, 1193, 2065; DS-EC-Rules-Web.txt p.9 (fog gate placed on the mega-boss board doorway after the Level 4 encounter)
- Current text: Place the Level 4 encounter tile associated with the chosen mega-boss adjacent to The Bonfire tile with the fog-gate placed at the entrance.
- Proposed fix: Place the mega-boss board, encounter side up, adjacent to the bonfire tile. After the Level 4 encounter is cleared, flip the board to its boss side and place the fog gate token on its doorway.
- Rationale: The fog gate marks the boss entrance; at the Level 4 entrance it is meaningless and its shortcut rule (2065) would trigger on the encounter, not the boss.
- Gameplay impact: Cosmetic ordering.
- Decision needed: N

### A-118 · omission · Minor · CLEAN-UP
- Location: SETUP › Setup After the mini-boss step 11 (manuscript.md line 1169); Shop Setup step 2.3 (line 1089)
- Evidence: manuscript.md:1089, 1169
- Current text: where they may now without spending a spark. / Shuffle five random legendary treasure cards.
- Proposed fix: ...where they now rest without spending a spark. / Shuffle five random legendary treasure cards into the tier two treasure deck.
- Rationale: Two truncated sentences in setup procedures.
- Gameplay impact: Cosmetic.
- Decision needed: N

### B-023 · economy · Minor · PROPOSED
- Location: L1067-1089 (Shop Setup procedure)
- Evidence: Filling 3/3/2/2/2 by drawing one card at a time needs about 22-28 draws from the tier-one deck under an assumed type mix (weapons 45%, armour 20%, shields 10%, upgrades 12%, spells 13%); the 2-shield quota is the bottleneck (P(<2 shields in 20 draws) = 0.39) and the tier-two deck may hold too few upgrades (Titanite Shards are tier one) to fill '2 upgrades' at all. About 15 drawn cards are reshuffled back each stocking.
- Current text: Draw tier one treasure cards one at a time to stock tier one shop: 3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells. ... Reshuffle extra treasures back into the tier one treasure deck.
- Proposed fix: "Draw cards one at a time until every category is filled or twelve cards have been drawn, whichever comes first. Place each card in its category if that category is not yet full; otherwise set it aside. Categories still unfilled after twelve draws remain empty. Shuffle the set-aside cards back into the deck."
- Rationale: Bounds the setup time and handles decks that cannot supply a category.
- Gameplay impact: Shop may open with fewer than 12 cards in rare cases; expected stocking time roughly halves.
- Decision needed: N

### C-012 · spelling · Minor · REQUIRED
- Location: L1141
- Evidence: 'Gargoyle (mini-boss) and Grey Wolf Sif (main-boss)'
- Current text: Grey Wolf Sif
- Proposed fix: Great Grey Wolf Sif
- Rationale: Component list (L515) and Darkroot booklet use the full name.
- Gameplay impact: None
- Decision needed: N

### C-023 · hedge · Minor · REQUIRED
- Location: L1017; L1021; L2223
- Evidence: 'might' x4: L1017/L1021 'to suggest which class might benefit most from its use'; L2223 'Players might expect to meet over multiple play sessions... A single section of a campaign might serve as a convenient amount of content'
- Current text: might
- Proposed fix: L1017/L1021: 'The emblem indicates the class for which the card is designed; it has no rules effect.' L2223: 'A campaign is designed for several sessions; one section is a convenient session.' (or delete as advice).
- Rationale: Speculation is not a rule; the only rule content is 'no gameplay difference'.
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

### C-043 · terminology · Minor · CLEAN-UP
- Location: L841; L1025; L1099; L1169; L1888; L1904; L1927; L1929; L2195; L2297; L2310; L2312; L2314; L2340
- Evidence: 'Blacksmith Andre' x7; bare 'Andre' x11 (e.g. 1099 'next to Andre'); 'Andre's Shop' x9; 'the shop' x3; heading 'Blacksmith Andre's Shop' (2310)
- Current text: Andre's Shop / the shop / Andre
- Proposed fix: 'Blacksmith Andre' at first mention in a section, 'Andre' thereafter; 'Andre's shop' (lower-case s) for the shop, 'the shop' acceptable after first mention
- Rationale: One NPC, one shop; choose capitalisation once. Recommend lower-case 'shop' to match other lower-cased game locations (bonfire, fog gate).
- Gameplay impact: None
- Decision needed: Y

### C-046 · terminology · Minor · CLEAN-UP
- Location: L1121
- Evidence: 'Encounter decks (level one, two, and three)' vs 'Level 1/2/3/4' numerals x194 everywhere else (component lists, tables, campaigns)
- Current text: level one, two, and three
- Proposed fix: Level 1, 2 and 3
- Rationale: Card labels are printed as numerals; use 'Level N' with capital L and numeral throughout.
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

### C-052 · terminology · Minor · CLEAN-UP
- Location: L1093
- Evidence: 'Set the *sparks* dial' vs 'spark dial' (715, 1167, 1185, 2195)
- Current text: sparks dial
- Proposed fix: spark dial
- Rationale: Component name is singular-attributive.
- Gameplay impact: None
- Decision needed: N

### C-054 · terminology · Minor · REQUIRED
- Location: L811; L1183; L1880; L1941; L597ff; L809ff
- Evidence: 'treasure card' x40 (deck/reward object) and 'equipment card' x24 (weapons, spells, shields, armour, items) are both legitimate but their relationship is never stated; bare 'item(s)' at 1183 'Shuffle mega-boss Items', 1880 'the equipped item', 1941 'Sold items'; bare 'treasure' x68
- Current text: Items / item / treasure
- Proposed fix: Define once: 'A *treasure card* is any card from a treasure deck. An *equipment card* is a treasure card that may be equipped to a dashboard slot.' Replace bare 'item(s)' with 'treasure card(s)'; allow bare 'treasure' only in reward contexts ('one treasure each').
- Rationale: Three words for overlapping sets; 'item' is also a card type name in the Community Update Pack ('legendary Item').
- Gameplay impact: None
- Decision needed: Y

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

### C-077 · table-text · Minor · CLEAN-UP
- Location: L679-723; L1277; L2205; L2055; L1997; L1137; L1975; L1315
- Evidence: Items used in rules but absent from Tokens & Terrain Elements: first player token (1277), pillar tokens (2205), Titanite Scale cards (2055), invader tokens and blank invader tokens (1997-2007), ambush cards (1137), phantom cards (1975), hollow cubes (781). L1315 'Mark the encounter card *cleared* with a black cube' uses a stamina cube as a marker.
- Current text: (absent)
- Proposed fix: Decide the scope of the component list (core only vs all supported content) and either add the expansion components under their expansion name or state that expansion components are listed in their own booklets; state that the cleared marker is a black stamina cube.
- Rationale: Component list is the reader's inventory check.
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

### C-085 · cross-ref · Minor · CLEAN-UP
- Location: L1169; L1171; L1187
- Evidence: 'They may visit the Firekeeper and Andre's Shop as usual after resting' (1169, 1187) and 'Resume encounters in the same way as before' (1171) point FORWARD to §Resting at The Bonfire (1892) and §Encounter Start (1257), which the reader has not yet seen
- Current text: as usual / as before
- Proposed fix: '(see §Resting at the Bonfire)' / '(see §Encounter Start)'
- Rationale: 'As usual' presupposes knowledge given later in the book.
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

### C-101 · heading · Minor · CLEAN-UP
- Location: L1111; L1119; L1143; L1173; L1680-1700; L523; L1015; L1041; L1091; L2454ff; L361; L2217
- Evidence: Case and whitespace: sentence-case H3s 'Encounter tiles' (1111), 'Encounter cards' (1119), 'Towards aggro', 'Away from aggro', 'Towards nearest', 'Away from nearest', 'Push-move', 'Push-attack' (1680-1700); mixed 'Setup After the mini-boss' (1143, 1173); 'Mega-bosses' (523) vs 'Mini-Bosses'/'Main-Bosses'; 'Class-specific Treasure' (1015); trailing spaces (1041, 1091, 2454, 2502, 2548, 2594, 2662, 2718, 2764, 2810, 2882, 2946, 2992); double space '#  INTRODUCTION' (361), '#  CAMPAIGN PLAY' (2217)
- Current text: Encounter tiles / Towards aggro / Mega-bosses
- Proposed fix: H1 ALL CAPS (chapter), H2 and H3 Title Case ('Encounter Tiles', 'Towards Aggro', 'Mega-Bosses', 'Setup After the Mini-Boss'); keyword italics permitted inside headings; no trailing or double spaces
- Rationale: One case convention per heading level.
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

### C-109 · punctuation · Minor · REQUIRED
- Location: L1033; L1035; L1043; L1045; L1563-1577; L3084-3094; L3182; L3184; L925
- Evidence: '=\>' used for 'greater than or equal to' (1033-1045: 'without a required statistic =\> 25'); '1 -&gt; 2' in the scaling table (1563-1577); '-\>' in the PvP list; escaped '\[25/25/0/0 Common\]' (3182, 3184); 'Range ∞ (inﬁnity)' (925)
- Current text: =\> 25; 1 -&gt; 2; -\>
- Proposed fix: '25 or more' in prose (or '≥ 25' in tables only); '1 → 2' or 'becomes 2'; tables for the PvP list; '[25/25/0/0, common]'; 'Range ∞ (infinity)' with the ligature removed
- Rationale: '=>' is not the symbol for 'greater than or equal'; ASCII arrows and escaped brackets are pandoc artefacts.
- Gameplay impact: L1033-1045 as written literally means 'equals-implies 25'
- Decision needed: N

### C-111 · punctuation · Minor · CLEAN-UP
- Location: L375; L529; L805; L835; L853; L1025; L1529; L1726; L1826; L1904; L1929; L1985; L2310; L2312; L2314; L837; L839; L2047
- Evidence: Mixed quotation marks: curly apostrophe ’ x146 in the body vs straight ' in ~20 lines (e.g. L529 'Executioner's Chariot (Executioner’s Chariot)' has both forms in one line); curly double quotes “ ” at 837, 839, 2047
- Current text: ' / ’ mixed
- Proposed fix: Policy: straight quotes in the Markdown source; the typesetter converts to curly. Until then, make every line consistent (curly).
- Rationale: Mixed glyphs show in print.
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

### D-014 · dropped-rule · Minor · OPTIONAL
- Location: manuscript.md 1179–1193 (Setup After the main-boss)
- Evidence: BDK/EC p.8: in a level 4 encounter all four nodes along the wall beside the doorway are entry nodes. BDK/EC p.9: the fog gate is placed on the doorway only after the level 4 encounter is cleared and the board is flipped. The manuscript places the fog gate before the level 4 encounter and says nothing about entry nodes.
- Current text: Place the Level 4 encounter tile associated with the chosen mega-boss adjacent to The Bonfire tile with the fog-gate placed at the entrance.
- Proposed fix: Place the level 4 encounter tile, encounter side up, adjacent to the bonfire tile. All four nodes along the wall beside the doorway are entry nodes. After the level 4 encounter is cleared, flip the tile to its mega-boss side and place the fog gate on its doorway.
- Rationale: Aligns with the mega-boss booklets; the fog gate timing matters because the manuscript's fog-gate shortcut (2066) triggers on first passage.
- Gameplay impact: Minor setup accuracy.
- Decision needed: N

### D-031 · underspecified-deviation · Minor · REQUIRED
- Location: manuscript.md 1113 (Encounter tiles)
- Evidence: Core p.8 lays four tiles around the bonfire; the manuscript intends a straight line of bonfire, four encounter tiles and boss tile (1115, 1152) but describes it as 'a two by six tile grid'.
- Current text: arrange them so they are connected in a two by six tile grid with the bonfire tile and mini-boss tile on opposite corners.
- Proposed fix: Arrange the bonfire tile, the four encounter tiles and the mini-boss tile in a straight line, with the bonfire tile and the mini-boss tile at opposite ends.
- Rationale: The later text (1152) confirms the linear layout.
- Gameplay impact: Setup clarity.
- Decision needed: N

### D-041 · underspecified-deviation · Minor · OPTIONAL
- Location: manuscript.md 1135, 1163 (setup) vs 1313, 1447 (rewards)
- Evidence: Treasure cards are dealt face down to each tile at setup, but the reward rules say characters 'draw' from the tier deck and never refer back to the dealt cards.
- Current text: Deal one tier one treasure per character face-down to each encounter tile. … Draw cards from the Tier one treasure deck before defeating the mini-boss
- Proposed fix: On the first clear of an encounter each character takes one of the treasure cards dealt to that tile at setup.
- Rationale: Links the setup step to the reward it exists for.
- Gameplay impact: None.
- Decision needed: N

### F-044 · tone · Minor · OPTIONAL
- Location: L1017, L1021 §Setup › Class-specific / Transposed Treasure
- Evidence: Explanatory hedging: 'to suggest which class might benefit most from its use. Aside from this suggestion of ideal character class, there are no gameplay differences from common treasures.'
- Current text: Class-specific treasures are marked with a tiny white emblem in the top right icon to suggest which class might benefit most from its use. Aside from this suggestion of ideal character class, there are no gameplay differences from common treasures.
- Proposed fix: REWRITE-IN-VOICE: 'Class-specific treasures bear a small white class emblem in the top-right icon. The emblem has no rules effect.'
- Rationale: 'suggest … might benefit' is commentary; the rule is that the emblem has no effect.
- Gameplay impact: none
- Decision needed: N

### F-045 · tone · Minor · OPTIONAL
- Location: L1025 §Setup › Legendary Treasure
- Evidence: Flavour in rules: 'These represent exceedingly rare relics that do not appear in every game and cannot be purchased.'
- Current text: These represent exceedingly rare relics that do not appear in every game and cannot be purchased.
- Proposed fix: REWRITE-IN-VOICE: 'Legendary treasures cannot be purchased. Only five enter the tier two deck in each game.'
- Rationale: Keep the two rules, drop 'exceedingly rare relics'.
- Gameplay impact: none
- Decision needed: N

### F-062 · prose-crossref · Minor · CLEAN-UP
- Location: L1057 §Setup › Using Expansion Treasure
- Evidence: Prose cross-reference: 'as above'
- Current text: as above
- Proposed fix: '(see §6.2)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §6.2 Treasure Deck Setup. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-063 · prose-crossref · Minor · CLEAN-UP
- Location: L1165 §Setup › Setup After the mini-boss step 9
- Evidence: Prose cross-reference: 'as previously described'
- Current text: as previously described
- Proposed fix: '(see §6.3)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §6.3 Shop Setup › After Boss is Defeated. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-064 · prose-crossref · Minor · CLEAN-UP
- Location: L1169, L1187 §Setup › After mini-boss step 11 / After main-boss step 7
- Evidence: Prose cross-reference: 'as usual'
- Current text: as usual
- Proposed fix: '(see §11)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §11 Returning to the Bonfire. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-065 · prose-crossref · Minor · CLEAN-UP
- Location: L1171 §Setup › Setup After the mini-boss step 12
- Evidence: Prose cross-reference: 'in the same way as before'
- Current text: in the same way as before
- Proposed fix: '(see §7.5)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §7.5 Encounters. Numbering per F_report.md §6 provisional map.
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

### A-030 · inherits-official-silently · Note · CLEAN-UP
- Location: SETUP › Character Setup step 8 (manuscript.md line 1003)
- Evidence: manuscript.md:1003; DS-Core-Rules-lores.txt p.13 (solo soul cache starts with 16); Hollowed_Edition_v1.3.txt p.4 ('Solo players begin with 6 souls')
- Current text: Characters adventuring alone start with six souls on their dashboard.
- Proposed fix: No change. Add to the glossary entry for souls: a character adventuring alone begins with six souls.
- Rationale: Deliberate departure from the official 16 (which fed a shared cache under 1-soul prices); follows the Hollowed Edition value and is coherent with the 2-soul shop price. Recorded for the preserve list.
- Gameplay impact: None.
- Decision needed: N

### A-123 · inherits-official-silently · Note · CLEAN-UP
- Location: SETUP › Setup After the main-boss step 4 (manuscript.md line 1181); CAMPAIGN PLAY
- Evidence: manuscript.md:1181, 1317; DS-EC-Rules-Web.txt p.8 and p.19 ('If the party rests at the bonfire, the level 4 encounter will not reset like level 1–3 encounters do')
- Current text: Characters then attempt to clear the Level 4 encounter as they have with previous encounters.
- Proposed fix: Level 4 encounters reset when the characters rest, like any other encounter. (Record as a deliberate departure; alternative: adopt the official no-reset rule.)
- Rationale: The official booklets exempt Level 4 encounters from resetting; the manuscript does not, and the generic reset rule therefore applies. Recording the choice prevents accidental 'correction'.
- Gameplay impact: Mega-boss approach is repeatable in the manuscript.
- Decision needed: Y

### B-010 · economy · Note · OPTIONAL
- Location: L1003 (Character Setup step 8)
- Evidence: Solo start 6 souls (from Hollowed Edition p.2). Official 1E solo bonus is 16 souls in the cache (Core p.13) because one character carries every activation. Under the manuscript's unscaled 1-character enemies 6 souls = three tier-one cards or Tier One in three stats.
- Current text: Characters adventuring alone start with six *souls* on their dashboard.
- Proposed fix: No change required; if solo play tests as too hard, raise to ten souls.
- Rationale: The reduced solo bonus is consistent with the manuscript's scaling (solo enemies are weakest).
- Gameplay impact: Negligible.
- Decision needed: N

### C-044 · terminology · Note · CLEAN-UP
- Location: L1169; L1187; L1888; L1902; L1912; L2195; L2297
- Evidence: 'Firekeeper' x8, no variants; matches Core/TG rulebooks ('Firekeeper' x16)
- Current text: Firekeeper
- Proposed fix: No change
- Rationale: Consistent; record in style sheet.
- Gameplay impact: None
- Decision needed: N

### C-093 · example · Note · CLEAN-UP
- Location: L1141
- Evidence: 'if the players selected the Gargoyle (mini-boss) and Grey Wolf Sif (main-boss)... only the encounters from the core setup until they defeat the Gargoyle and then only encounters from the Darkroot Basin expansion' - Gargoyle is Core (L491) and Sif is Darkroot Basin (L515): consistent.
- Current text: (verified)
- Proposed fix: Fix name only (see C-012).
- Rationale: Logic verified.
- Gameplay impact: None
- Decision needed: N

## Completion entries that apply (4) — approved at Gate 1

### [CMP-0005] BOSS SPECIAL RULES (chapter) — Proposed Completion (partly BLOCKED — source booklet not supplied)
- Read `04_completion_backlog.md` lines 563–682 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

### [CMP-0007] Truncated and defective sentences (several chapters) — Proposed Completion
- Read `04_completion_backlog.md` lines 711–749 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

### [CMP-0012] Game Components and owning chapters — Undefined components (event cards, ambush cards, mega-boss items, Level 4 tiles, pillar tokens, strafe and track cards) — Proposed Completion [PROPOSED-SYSTEMIC for event cards]
- Read `04_completion_backlog.md` lines 929–983 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

### [CMP-0023] Setup › Setup After the main-boss — Level 4 encounter rules — Proposed Completion
- Read `04_completion_backlog.md` lines 1194–1206 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

