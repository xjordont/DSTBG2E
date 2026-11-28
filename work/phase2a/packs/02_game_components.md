# Drafting pack — chapter 02 (game_components) — manuscript chapter "GAME COMPONENTS"

Source text: `work/phase2a/source/02_game_components.md` (manuscript.md lines 383–724).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 383.
- **Characters** · present — to audit · line 385.
- **Enemies** · present — defect · line 409. "1x HungryVoracious Mimic" typo; "2X" capitalisation; counts to verify vs official.
- **Bosses** · present — to audit · line 481.
- **Mini-Bosses** · present — to audit · line 483.
- **Main-Bosses** · present — to audit · line 501.
- **Mega-bosses** · present — to audit · line 523.
- **Phantoms** · present — to audit · line 543.
- **Invaders (Standard)** · present — to audit · line 545.
- **Invaders (Advanced)** · present — to audit · line 559.
- **Summons (Standard)** · present — to audit · line 573.
- **Summons (Advanced)** · present — to audit · line 585.
- **Treasure Cards** · present — to audit · line 597.
- **Cards** · present — to audit · line 631.
- **Encounter cards** · present — to audit · line 633.
- **Event cards** · present — to audit · line 659.
- **Dice** · present — to audit · line 669.
- **Tokens & Terrain Elements** · present — defect · line 679. Condition token arithmetic: 7×4 + 4×2 = 36, text says 35. "first player token" used later but absent here.

## Audit findings mapped to this chapter (65)

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

### A-083 · omission · Major · REQUIRED
- Location: TILES & NODES › Terrain › Traps (manuscript.md lines 967–981)
- Evidence: manuscript.md:713, 967–981, 3064; DS-Core-Rules-lores.txt p.18 (trap tokens: blank or damage; dodge or suffer; cannot be blocked; no effect on enemies)
- Current text: When a character is pushed onto or moves into a node containing a face-down trap token, flip the token face-up and resolve its effect on all models on that node.
- Proposed fix: A trap token shows either nothing (blank) or a dodge difficulty and a damage value. When a trap token is revealed, each character on that node must either suffer the damage or attempt to dodge it as an attack with that dodge difficulty; trap damage is not reduced by block or resist. A blank token has no effect. Enemy models on the node suffer the trap's damage without rolling. A revealed trap does not trigger again until the encounter is reset.
- Rationale: What a trap token shows and how it is resolved is never described; 'resolve its effect on all models' extends traps to enemies, which the official rule forbids, so the intent must be stated. Alternative: traps have no effect on enemies.
- Gameplay impact: Traps appear on roughly a third of encounter cards.
- Decision needed: Y

### A-088 · arithmetic · Major · REQUIRED
- Location: SETUP › Encounter tiles step 1 (manuscript.md line 1113)
- Evidence: manuscript.md:721–723, 1113–1115; DS-Core-Rules-lores.txt p.8
- Current text: arrange them so they are connected in a two by six tile grid with the bonfire tile and mini-boss tile on opposite corners.
- Proposed fix: Arrange the six tiles (the bonfire tile, four encounter tiles and the mini-boss tile) in a grid of two rows of three, with the bonfire tile and the mini-boss tile in opposite corners.
- Rationale: Six tiles cannot form a 2×6 grid; the intended layout is 2×3.
- Gameplay impact: Setup instruction is impossible as printed.
- Decision needed: N

### A-108 · omission · Major · REQUIRED
- Location: CAMPAIGNS › Big Game Hunting (manuscript.md lines 2994, 3018); GAME COMPONENTS › Mega-bosses (lines 523–541)
- Evidence: manuscript.md:523–541, 2994, 3018
- Current text: The Last Giant (Mega Boss)
- Proposed fix: Add 'The Last Giant (The Last Giant)' to the Mega-bosses component list and 'the Last Giant expansion' to the campaign's requirements.
- Rationale: A boss used by a campaign is absent from the components and from the campaign's own requirements line.
- Gameplay impact: Campaign cannot be assembled from the component list.
- Decision needed: N

### B-001 · undefined-value · Major · REQUIRED
- Location: L669-677 (Game Components > Dice)
- Evidence: The component list gives die counts only (5 black, 4 blue, 2 orange, 4 green). No section of the manuscript states the faces of any die; the Introduction promises a standalone rulebook. Faces reconstructed from DS-Extended-Rules-V45 p.27 card images, Core p.12 and V2 p.25 examples (see B_report §1).
- Current text: - 5x Black
- 4x Blue
- 2X Orange
- 4x Green
- Proposed fix: Add after the dice list: "Each die shows the following faces. Black: 0, 1, 1, 1, 2, 2. Blue: 1, 1, 2, 2, 2, 3. Orange: 1, 2, 2, 3, 3, 4. Green (dodge): three blank faces and three faces showing one dodge symbol." Also correct "2X Orange" to "2x Orange".
- Rationale: A standalone rulebook must define the randomisers it uses; every balance figure in this audit depends on these faces. The listed sets are the only sorted six-face sets consistent with all supplied evidence; the author must confirm against the physical dice.
- Gameplay impact: None if confirmed; if the author's dice differ, every probability in B_report must be re-run.
- Decision needed: Y

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

### C-075 · table-text · Major · REQUIRED
- Location: L523-541; L3018; L2994
- Evidence: Mega-bosses component list (523-541) omits The Last Giant, used at L3018 'The Last Giant (Mega Boss)'; 'Big Game Hunting' requirements (L2994) list 'Core set, Manus expansion, and Asylum Demon expansion' only
- Current text: (absent from list; absent from requirements)
- Proposed fix: Add '- The Last Giant (The Last Giant)' to Mega-bosses; add 'The Last Giant expansion' to the Big Game Hunting requirements
- Rationale: A campaign uses a boss that the component list and the requirements line do not mention. (The Last Giant is a Kickstarter mega-boss expansion; verify against its booklet, which is not among the supplied sources.)
- Gameplay impact: Players cannot play Section Two A without the expansion
- Decision needed: Y

### A-017 · omission · Minor · REQUIRED
- Location: GAMEPLAY › Encounters › Encounter Start step 9 (manuscript.md line 1277); PLAYER VS PLAYER (line 3056)
- Evidence: manuscript.md:679–723 (no such component), 1277, 1289, 3056; DS-Core-Rules-lores.txt p.7 (1x First Activation Token exists officially)
- Current text: Place the first player token on the character with the highest threat value.
- Proposed fix: Delete Encounter Start step 9. In PLAYER VS PLAYER replace the first turn token bullet with: Characters take their turns in descending threat order; ties are broken by the players' choice.
- Rationale: The first player token is not in the component list and is never used: character order is fixed by threat value (1289), so the token has no function. PvP calls the same object a 'First turn token'.
- Gameplay impact: Removes a phantom component and a contradiction between two names.
- Decision needed: N

### A-047 · undefined-state · Minor · OPTIONAL
- Location: GAMEPLAY › Sparks (manuscript.md lines 1247–1253); Boss Death (line 2195)
- Evidence: manuscript.md:715, 1093, 1249, 2195, 2233; DS-Core-Rules-lores.txt p.33 (campaign maximum = starting sparks)
- Current text: Defeating a mini-boss or main-boss provides one additional spark.
- Proposed fix: The spark dial never shows more sparks than the characters' starting number; a spark gained beyond that maximum is lost.
- Rationale: The campaign chapter sets this maximum (2233) but the basic game does not; a solo character would reach six or seven, beyond the physical dial. Alternative: no maximum, track overflow with a token.
- Gameplay impact: Solo and two-character basic games only.
- Decision needed: Y

### A-081 · undefined-state · Minor · OPTIONAL
- Location: COMBAT BASICS › Conditions › Poison (manuscript.md line 1616); GAME COMPONENTS › Tokens (line 703)
- Evidence: manuscript.md:703, 1616–1618
- Current text: Poison tokens are not limited to one per model.
- Proposed fix: If no poison tokens remain in the supply, further poison tokens are not placed.
- Rationale: Seven poison tokens exist; unlimited stacking across several models exhausts them.
- Gameplay impact: Rare; four-character games with poison weapons.
- Decision needed: N

### A-089 · omission · Minor · REQUIRED
- Location: SETUP › Encounter tiles (manuscript.md lines 1111–1117); Setup After the mini-boss step 4 (line 1151); BOSS ENCOUNTERS › The Fog Gate (line 2065)
- Evidence: manuscript.md:719, 1111–1117, 1151, 2065; DS-Core-Rules-lores.txt p.8
- Current text: Place the fog-gate as before.
- Proposed fix: Encounter tiles step 3: Place the fog gate token on the doorway of the boss tile.
- Rationale: The fog gate is a component, is moved by The Fog Gate rule and is placed 'as before' after the mini-boss, but the initial setup never places it.
- Gameplay impact: Setup omission.
- Decision needed: N

### A-091 · undefined-state · Minor · PROPOSED
- Location: GAME COMPONENTS › Event cards (manuscript.md line 667)
- Evidence: manuscript.md:667
- Current text: 5x Special Trap cards
- Proposed fix: Delete, or define within the Event Cards chapter: a Special Trap card is an event card that places the stated trap effect on the nodes it names when revealed.
- Rationale: Never mentioned again.
- Gameplay impact: Orphan component.
- Decision needed: Y

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

### A-113 · terminology · Minor · CLEAN-UP
- Location: GAME COMPONENTS › Tokens (manuscript.md line 681); Encounter Turn Order (line 1285); Character Attacks (line 1850); Enemy Turn Overview (line 1664)
- Evidence: manuscript.md:681, 1285, 1291, 1517, 1664, 1850
- Current text: Wound tokens / damage tokens / wounds
- Proposed fix: Use 'wound token' throughout for the tokens placed on enemies and 'damage cube' for the red cubes on endurance bars.
- Rationale: Three terms for one component.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-114 · omission · Minor · CLEAN-UP
- Location: BOSS SPECIAL RULES › Pillar Smasher (manuscript.md line 2205); GAME COMPONENTS (lines 679–723)
- Evidence: manuscript.md:679–723, 2205–2209
- Current text: place one pillar token on each of the four pillar nodes found on the mega-boss game board.
- Proposed fix: Add to Tokens & Terrain Elements: 4x Pillar tokens (Asylum Demon expansion). Add to The Basics: pillar nodes are terrain nodes printed on the Asylum Demon mega-boss board.
- Rationale: Pillar tokens and pillar nodes are used but never listed or located.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-117 · arithmetic · Minor · CLEAN-UP
- Location: GAME COMPONENTS › Tokens (manuscript.md lines 701–705)
- Evidence: manuscript.md:701–705; DS-Core-Rules-lores.txt p.7 (5 each of four conditions); DS-BDK-Rules-web.txt p.4 (4 Calamity)
- Current text: 35x Condition tokens: 7x each of poison, Bleed, Stagger, and frostbite tokens; 4x each of Calamity and 4x Corrosion tokens
- Proposed fix: 36x Condition tokens: 7x each of poison, bleed, stagger and frostbite; 4x calamity; 4x corrosion.
- Rationale: 7×4 + 4×2 = 36.
- Gameplay impact: Cosmetic.
- Decision needed: N

### B-026 · balance · Minor · PROPOSED
- Location: L1642-1648 (Conditions > Calamity)
- Evidence: Manuscript: -1 to block, resist and dodge results, not removed until the encounter ends. Official (DS-BDK-Rules-web, text lines 452-458): -1 success on the roll; the token is removed when the character suffers damage from the attack. Per-hit cost with 2 black block dice is +0.97 expected damage; over a five-hit boss fight the persistent version costs about +4.9 damage against about +1 for the official version.
- Current text: *Calamity* tokens are not removed at the end of a model's turn. *Calamity* tokens are only removed at the end of the encounter.
- Proposed fix: "Calamity tokens are not removed at the end of a model's turn. A Calamity token is removed when the affected model suffers damage from an attack."
- Rationale: Restores the official duration; Kalameet already applies the token repeatedly (BDK: Mark of Calamity is always in the deck).
- Gameplay impact: Reduces Kalameet's effective damage by roughly 4 per fight per character.
- Decision needed: Y

### B-027 · arithmetic · Minor · REQUIRED
- Location: L701-705 (Tokens & Terrain Elements > Condition tokens)
- Evidence: 7 x 4 (poison, bleed, stagger, frostbite) + 4 x 2 (calamity, corrosion) = 36, not 35. Core set supplies 5 of each basic condition (Core p.7) = 20; BDK supplies 4 Calamity.
- Current text: - 35x Condition tokens
  - 7x each of poison, *Bleed*, *Stagger*, and frostbite tokens
  - 4x each of *Calamity* and *4x Corrosion* tokens
- Proposed fix: - 36x Condition tokens
  - 7x each of poison, bleed, stagger and frostbite tokens
  - 4x each of calamity and corrosion tokens
- Rationale: Sum must equal the itemised list; the stray '4x' inside the second sub-item is removed.
- Gameplay impact: None.
- Decision needed: N

### B-028 · economy · Minor · REQUIRED
- Location: L683 (Soul tokens) with L1383 (Souls are individual)
- Evidence: Supply 10x1 + 5x3 + 3x5 + 1x8 = 19 tokens, total face value 48 (the Core set's shared-cache supply, Core p.7). The manuscript makes souls individual and non-transferable; four characters each holding 15-20 souls (B_report §4.2) need 60-80 in face value.
- Current text: - 10x1, 5x3, 3x5, and 1x8 Soul tokens
- Proposed fix: Add after the token list: "Soul tokens are not limited. If the supply runs out, use any convenient counters or record souls on paper."
- Rationale: Individual soul tracking exceeds the printed supply in ordinary play.
- Gameplay impact: Avoids an artificial cap of 48 souls across the party.
- Decision needed: N

### B-029 · table-text-mismatch · Minor · REQUIRED
- Location: L689 (Stat tier cubes) with L781, L1215, L1367 (hollow markers 'white cubes')
- Evidence: 16 white cubes = 4 characters x 4 stats, all placed on dashboards at setup (L771). Hollow status is marked with two white cubes per hollow character; in a four-character game none are spare.
- Current text: When a character dies and is revived *hollow*, they block off the two furthest right spaces of the endurance bar with a marker such as white cubes.
- Proposed fix: "...block off the two furthest right spaces of the endurance bar with two hollow markers (use the Tier Four red cube from a stat track that has not reached tier four, or any two counters)." and add "8x Hollow markers" to the component list.
- Rationale: A marker must exist in the component list; white cubes are fully committed at four players.
- Gameplay impact: None.
- Decision needed: N

### B-030 · table-text-mismatch · Minor · REQUIRED
- Location: L1277 (Encounter Start step 9) and L3058 (PvP 'First turn token') vs component list L681-716
- Evidence: A 'first player' token (and in PvP a 'First turn token') is used but not listed among components. Core p.7 lists '1x First Activation Token'.
- Current text: 9.  Place the *first player* token on the character with the highest threat value.
- Proposed fix: Add "1x First player token" to Tokens & Terrain Elements; use the term "first player token" in both the Encounter Start and Player vs Player sections.
- Rationale: Component used in play must be listed; one term throughout.
- Gameplay impact: None.
- Decision needed: N

### C-005 · spelling · Minor · REQUIRED
- Location: L557
- Evidence: 'Xanthous King Jeramiah' vs L2492/L2528 'Xanthous King Jeremiah'
- Current text: Xanthous King Jeramiah
- Proposed fix: Xanthous King Jeremiah
- Rationale: Phantoms booklet prints 'Xanthous King Jeremiah' (x3); the manuscript is internally inconsistent.
- Gameplay impact: None
- Decision needed: N

### C-006 · spelling · Minor · REQUIRED
- Location: L443
- Evidence: '1x HungryVoracious Mimic (Explorers)'
- Current text: 1x HungryVoracious Mimic (Explorers)
- Proposed fix: 1x Mimic (Explorers) - Hungry Mimic and Voracious Mimic data cards
- Rationale: Two names run together; Explorers ships one model with two data cards (booklet: 'Hungry Mimic' x5, 'Voracious Mimic' x3).
- Gameplay impact: None
- Decision needed: N

### C-007 · spelling · Minor · REQUIRED
- Location: L469; L3354
- Evidence: L469 'Skeletal Beast (ToG)'; L3354 'Skeleton Beast'
- Current text: Skeletal Beast
- Proposed fix: Skeleton Beast
- Rationale: Tomb of Giants rulebook prints 'Skeleton Beast' (x3); manuscript uses both.
- Gameplay impact: None
- Decision needed: N

### C-008 · spelling · Minor · REQUIRED
- Location: L593
- Evidence: 'Sirris of the Sunless Realm'
- Current text: Sirris of the Sunless Realm
- Proposed fix: Sirris of the Sunless Realms
- Rationale: Phantoms booklet: 'Sirris of the Sunless Realms'.
- Gameplay impact: None
- Decision needed: N

### C-009 · spelling · Minor · REQUIRED
- Location: L2734
- Evidence: 'Old Dragon Slayer (Mini-Boss)' vs L495/L2838 'Old Dragonslayer'
- Current text: Old Dragon Slayer
- Proposed fix: Old Dragonslayer
- Rationale: Explorers booklet: 'Old Dragonslayer' (x11); manuscript inconsistent.
- Gameplay impact: None
- Decision needed: N

### C-010 · spelling · Minor · OPTIONAL
- Location: L561; L569; L457
- Evidence: L561 'Armourer Dennis'; L569 'Marvellous Chester'; L457 'Plough Scarecrow'
- Current text: Armourer Dennis / Marvellous Chester / Plough Scarecrow
- Proposed fix: Armorer Dennis / Marvelous Chester / Plow Scarecrow (as printed on the cards) - OR keep British forms with a style-sheet note that card names are anglicised
- Rationale: Official cards print US spellings (Phantoms booklet 'Armorer Dennis' x3, 'Marvelous Chester' x3; Darkroot 'Plow Scarecrow'). Proper nouns normally follow the printed component so players can find the card.
- Gameplay impact: Players searching for the card by name
- Decision needed: Y

### C-011 · spelling · Minor · REQUIRED
- Location: L583
- Evidence: 'Sword Master Sabre'
- Current text: Sword Master Sabre
- Proposed fix: Sword Master
- Rationale: Phantoms booklet names this summon 'Sword Master' only (pp.1,4). 'Sabre' is not on the card.
- Gameplay impact: Card lookup
- Decision needed: Y

### C-013 · spelling · Minor · CLEAN-UP
- Location: L2452; L2398; L2500; L2660; L2934
- Evidence: L2452 'The Dancer of the Boreal Valley' vs L507 'Dancer of the Boreal Valley'; 'Ornstein & Smough' vs components 'Dragonslayer Ornstein' (L509) and 'Executioner Smough' (L511)
- Current text: The Dancer of the Boreal Valley; Ornstein & Smough
- Proposed fix: Dancer of the Boreal Valley; Dragonslayer Ornstein and Executioner Smough (one boss encounter, two models) - state this once in the Main-Bosses component list
- Rationale: Boss names must match the component list so a reader can find the models and data cards.
- Gameplay impact: None
- Decision needed: N

### C-014 · spelling · Minor · CLEAN-UP
- Location: L445
- Evidence: '3x Ironclad Soldiers (Iron Keep)' - only plural entry in a list of singular names
- Current text: Ironclad Soldiers
- Proposed fix: Ironclad Soldier
- Rationale: List convention is 'Nx Singular Name'.
- Gameplay impact: None
- Decision needed: N

### C-029 · italics · Minor · REQUIRED
- Location: L705; L1529; L1890; L1345; L3056; L1640; L1650; L1808-L1832
- Evidence: Italicised fragments/non-terms: '*4x Corrosion*' (705, repeats quantity); '*repeat to*' (1529); '*spark to*' (1890); '*clear an*' (1345); '*First* *turn*' (3056); headings '*Calamity (*Kalameet Expansion*)*' and '*Corrosion (*Gaping Dragon Expansion*)*' (1640, 1650); bold **AND**/**OR** connectors (1808-1832)
- Current text: *4x Corrosion*
- Proposed fix: '4x each of *calamity* and *corrosion* tokens'; '*repeat* to'; '*spark* to'; '*clear* an'; '*first player* token'; '*Calamity* (Kalameet expansion)'; replace AND/OR connectors with a numbered procedure
- Rationale: Italics mark glossary keywords only.
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

### C-041 · terminology · Minor · CLEAN-UP
- Location: L483; L501; L523; L2073; L2366ff; L2692ff; L2716ff; L2826ff; L2996
- Evidence: mini-boss x47 / Mini-Boss x15 / Mini Boss x5 / mini boss x1 / 'mini bosses'; main-boss x31 / Main-Boss x1 / Main Boss x11; mega-boss x28 / Mega-boss x2 / Mega Boss x7 / 'mega boss' x1 (L2996)
- Current text: Mini Boss / Main Boss / Mega Boss / mini boss
- Proposed fix: mini-boss, main-boss, mega-boss (lower-case, hyphenated) in prose and campaign lists; Title Case 'Mini-Boss' only as a heading word
- Rationale: Six spellings of three terms; the campaign lists (L2692-3034) use the unhyphenated Title Case form throughout.
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

### C-054 · terminology · Minor · REQUIRED
- Location: L811; L1183; L1880; L1941; L597ff; L809ff
- Evidence: 'treasure card' x40 (deck/reward object) and 'equipment card' x24 (weapons, spells, shields, armour, items) are both legitimate but their relationship is never stated; bare 'item(s)' at 1183 'Shuffle mega-boss Items', 1880 'the equipped item', 1941 'Sold items'; bare 'treasure' x68
- Current text: Items / item / treasure
- Proposed fix: Define once: 'A *treasure card* is any card from a treasure deck. An *equipment card* is a treasure card that may be equipped to a dashboard slot.' Replace bare 'item(s)' with 'treasure card(s)'; allow bare 'treasure' only in reward contexts ('one treasure each').
- Rationale: Three words for overlapping sets; 'item' is also a card type name in the Community Update Pack ('legendary Item').
- Gameplay impact: None
- Decision needed: Y

### C-058 · terminology · Minor · CLEAN-UP
- Location: L719; L1151; L1179; L2063; L2065; L2227; L2229
- Evidence: 'Fog Gate token' (719), 'fog-gate' (1151, 1179), 'fog gate' x11, 'the fog gate tile should be removed' (2065) vs 'fog gate token' (719, 2229)
- Current text: fog-gate / Fog Gate / fog gate tile
- Proposed fix: fog gate (lower-case, no hyphen); the component is the 'fog gate token'
- Rationale: One component, one name; it is a token not a tile.
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

### C-073 · table-text · Minor · REQUIRED
- Location: L701-705
- Evidence: '35x Condition tokens' vs itemised '7x each of poison, Bleed, Stagger, and frostbite' (28) + '4x each of Calamity and Corrosion' (8) = 36
- Current text: 35x Condition tokens
- Proposed fix: 36x Condition tokens (or correct the itemisation)
- Rationale: Total does not equal the sum of its parts.
- Gameplay impact: None
- Decision needed: Y

### C-077 · table-text · Minor · CLEAN-UP
- Location: L679-723; L1277; L2205; L2055; L1997; L1137; L1975; L1315
- Evidence: Items used in rules but absent from Tokens & Terrain Elements: first player token (1277), pillar tokens (2205), Titanite Scale cards (2055), invader tokens and blank invader tokens (1997-2007), ambush cards (1137), phantom cards (1975), hollow cubes (781). L1315 'Mark the encounter card *cleared* with a black cube' uses a stamina cube as a marker.
- Current text: (absent)
- Proposed fix: Decide the scope of the component list (core only vs all supported content) and either add the expansion components under their expansion name or state that expansion components are listed in their own booklets; state that the cleared marker is a black stamina cube.
- Rationale: Component list is the reader's inventory check.
- Gameplay impact: None
- Decision needed: Y

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

### C-108 · punctuation · Minor · CLEAN-UP
- Location: L447; L675; L621; L681
- Evidence: '2X Large Hollow Soldier' (447), '2X Orange' (675) vs lower-case 'x' everywhere else; '20 (Expansions)' (621) missing 'x'; '6x1 , 3x3, and 1x5 Wound tokens' (681, space before comma)
- Current text: 2X; 20; 6x1 ,
- Proposed fix: 2x; 20x; '6x 1-wound, 3x 3-wound and 1x 5-wound tokens' (or a small table)
- Rationale: One quantity format: 'Nx Name'.
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

### C-112 · punctuation · Minor · CLEAN-UP
- Location: L679; L895; L1199; L1203; L1710; L1766; L2161; L2201; L2237; L449; L2398
- Evidence: '&' in nine headings and in list items 'Mushroom Child & Parent' (449), 'Ornstein & Smough' (2398, 2500, 2660, 2934)
- Current text: &
- Proposed fix: 'and' in headings and prose; '&' only inside an official product or card name
- Rationale: Ampersand is a logo/label device, not prose.
- Gameplay impact: None
- Decision needed: N

### D-018 · component-count · Minor · REQUIRED
- Location: manuscript.md 679–723 (Tokens & Terrain Elements) vs 1277, 3056
- Evidence: Core p.7 lists 1x First Activation Token. The manuscript's component list omits it but uses a 'first player token' (1277) and a 'first turn token' (3056).
- Current text: (absent from list)
- Proposed fix: 1x First Activation token
- Rationale: Either list the token or delete the two references (characters act in threat order, so the token has no function outside PvP).
- Gameplay impact: None if removed.
- Decision needed: Y

### D-019 · component-count · Minor · REQUIRED
- Location: manuscript.md 443 (Enemies)
- Evidence: EXP p.4: 2x Mimic Miniatures, 2x Mimic Data Cards (Hungry Mimic, Voracious Mimic).
- Current text: 1x HungryVoracious Mimic (Explorers)
- Proposed fix: 2x Mimic — Hungry Mimic and Voracious Mimic (Explorers)
- Rationale: Official count is two.
- Gameplay impact: None.
- Decision needed: N

### D-020 · component-count · Minor · REQUIRED
- Location: manuscript.md 701–705 (Tokens)
- Evidence: Core p.7: 5x each of Bleed, Poison, Frostbite and Stagger (20 total). BDK p.4: 4x Calamity. The manuscript states 7 of each and a total of 35, but 7×4 + 4 + 4 = 36.
- Current text: 35x Condition tokens / 7x each of poison, Bleed, Stagger, and frostbite tokens / 4x each of Calamity and 4x Corrosion tokens
- Proposed fix: 28x Condition tokens: 5x each of bleed, poison, frostbite and stagger (Core); 4x Calamity (Black Dragon Kalameet); 4x Corrosion (Gaping Dragon)
- Rationale: The core set supplies five of each; if the extra two per condition come from another expansion the source must be named.
- Gameplay impact: None.
- Decision needed: Y

### D-022 · component-count · Minor · REQUIRED
- Location: manuscript.md 509–511 (Main-Bosses)
- Evidence: Core p.5: one main boss, 'Dragon Slayer Ornstein & Executioner Smough', with one data card, one behaviour deck and one treasure set.
- Current text: Dragonslayer Ornstein (Core) / Executioner Smough (Core)
- Proposed fix: Dragonslayer Ornstein & Executioner Smough (Core)
- Rationale: One boss entry, two miniatures.
- Gameplay impact: Boss selection list.
- Decision needed: N

### D-023 · component-count · Minor · REQUIRED
- Location: manuscript.md 523–541 (Mega-bosses) vs 3018
- Evidence: The Big Game Hunting campaign lists 'The Last Giant (Mega Boss)' (3018); The Last Giant is absent from the mega-boss component list.
- Current text: (absent)
- Proposed fix: The Last Giant (The Last Giant)
- Rationale: A boss used by a listed campaign must appear in the component list.
- Gameplay impact: None.
- Decision needed: N

### D-024 · component-count · Minor · REQUIRED
- Location: manuscript.md 679–723 (Tokens & Terrain Elements)
- Evidence: Components used by the manuscript's rules but absent from its lists: invader tokens (PH p.5: 6 standard, 6 advanced, 3 blank), 5 ambush cards (EXP p.4), 3 Titanite Scale cards (IK p.3), pillar tokens (2205), boss/summon/invader health dials, mega-boss game boards (BDK/EC p.4).
- Current text: (absent)
- Proposed fix: Add to the component list: 6x Standard invader tokens, 6x Advanced invader tokens, 3x Blank invader tokens (Phantoms); 5x Ambush cards (Explorers); 3x Titanite Scale cards (Iron Keep); 4x Pillar tokens (Asylum Demon); 1x Health dial per boss, summon and invader; 1x Mega-boss game board per mega-boss expansion.
- Rationale: Every component referenced by a rule must be listed.
- Gameplay impact: None.
- Decision needed: N

### D-026 · component-count · Minor · REQUIRED
- Location: manuscript.md 449 (Enemies)
- Evidence: DR p.4: 14 enemy miniatures and 7 data cards; the Mushroom Child and Mushroom Parent are separate enemies with separate data cards.
- Current text: 1x Mushroom Child & Parent (Darkroot Basin)
- Proposed fix: 1x Mushroom Child (Darkroot Basin) / 1x Mushroom Parent (Darkroot Basin)
- Rationale: Two enemies written as one line.
- Gameplay impact: None.
- Decision needed: N

### B-037 · table-text-mismatch · Note · OPTIONAL
- Location: L659-667 (Event cards) and L489-511 (Tomb of Giants enemy counts)
- Evidence: The Core 1E set has no event cards (Core pp.6-7); V2 has 30 event cards of a different system (V2 p.6). The manuscript lists 10/10/10 level event cards and 5 trap cards without a source set. V2 p.6 lists Tomb of Giants enemy tokens as 4 Skeleton Soldier, 4 Skeleton Archer, 2 Giant Skeleton Soldier, 2 Giant Skeleton Archer, 2 Skeleton Beast, 2 Necromancer; the manuscript lists 3, 3, 2, 2, 1, 2.
- Current text: - 10x Level 1 event cards
- 10x Level 2 event cards
- 10x Level 3 event cards
- 5x Special Trap cards ... 3x Skeleton Archer (ToG) ... 3x Skeleton Soldier (ToG) ... 1x Skeletal Beast (ToG)
- Proposed fix: Mark the event cards with their source set (or "Second Edition print-and-play") and align the Tomb of Giants counts with the published component list: 4x Skeleton Soldier, 4x Skeleton Archer, 2x Skeletal Beast.
- Rationale: Component lists must match a set the player can own.
- Gameplay impact: None.
- Decision needed: Y

### C-078 · table-text · Note · CLEAN-UP
- Location: L597-629; L631-657; L621
- Evidence: Treasure total 534 = 13+45+40+120+60+145+10+20+18+63 (verified); encounter total 169 = 12+31+12+31+12+31+40 (verified). L621 '20 (Expansions)' lacks the 'x' used on every other line.
- Current text: 20 (Expansions)
- Proposed fix: 20x (Expansions)
- Rationale: Arithmetic correct; format defect only.
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

### D-025 · component-count · Note · OPTIONAL
- Location: manuscript.md 635–657 (Encounter cards)
- Evidence: Supplied booklets give DR 18, IK 18, EXP 15, EC 10 (incl. 4 level 4), BDK 4 level 4, ToG 29 (V2 p.6); PWA and the other mega-boss sets are not supplied. The stated 31 per level and 40 level-4 cards cannot be reconciled from the supplied sources (9 listed mega-bosses × 4 = 36).
- Current text: Level 1 encounter cards … 31x (Expansions) … Level 4 encounter cards 40x (Expansions)
- Proposed fix: (author to confirm the per-level and level-4 totals against the physical sets, or state the totals per expansion)
- Rationale: Unverifiable rather than wrong; recording for completeness.
- Gameplay impact: None.
- Decision needed: Y

### D-027 · component-count · Note · OPTIONAL
- Location: manuscript.md 557, 561, 569, 2492, 2528 (Phantoms)
- Evidence: PH p.5 spells the names 'Xanthous King Jeremiah', 'Armorer Dennis', 'Marvelous Chester'. The manuscript uses 'Jeramiah' (557) and 'Jeremiah' (2492, 2528), 'Armourer Dennis', 'Marvellous Chester'.
- Current text: Xanthous King Jeramiah / Armourer Dennis / Marvellous Chester
- Proposed fix: Xanthous King Jeremiah / Armorer Dennis / Marvelous Chester
- Rationale: Card names are proper nouns and should match the printed cards even in a British-English text; 'Jeramiah' is a misspelling in any case.
- Gameplay impact: None.
- Decision needed: Y

### F-054 · external-reference · Note · OPTIONAL
- Location: L387–L723 §Game Components
- Evidence: Set abbreviations in component lists are undefined: '(Characters & PWA)', '(ToG)', '(Core)', '(Explorers)'.
- Current text: - Sorcerer (Characters & PWA) … - Cleric (Characters & ToG)
- Proposed fix: Add a one-line key at the head of §2: 'Set codes: Core; Characters; PWA — Painted World of Ariamis; ToG — Tomb of Giants; …'. Component-set tags are legitimate and stay.
- Rationale: Component identification is permitted; abbreviations must be defined in-book.
- Gameplay impact: none
- Decision needed: N

### F-093 · copied-prose · Note · OPTIONAL
- Location: L387 §Game Components › Characters
- Evidence: Matches official text — close paraphrase (10-word run)
- Current text: Each character has a unique miniature, character dashboard, three to four starting equipment cards…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.4. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

## Completion entries that apply (3) — approved at Gate 1

### [CMP-0007] Truncated and defective sentences (several chapters) — Proposed Completion
- Read `04_completion_backlog.md` lines 711–749 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

### [CMP-0011] Gameplay › Encounter Start step 9 and Player vs Player — "First player token" — Proposed Completion
- Read `04_completion_backlog.md` lines 915–928 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

### [CMP-0012] Game Components and owning chapters — Undefined components (event cards, ambush cards, mega-boss items, Level 4 tiles, pillar tokens, strafe and track cards) — Proposed Completion [PROPOSED-SYSTEMIC for event cards]
- Read `04_completion_backlog.md` lines 929–983 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

