# Drafting pack — chapter 11 (returning_to_the_bonfire) — manuscript chapter "RETURNING TO THE BONFIRE"

Source text: `work/phase2a/source/11_returning_to_the_bonfire.md` (manuscript.md lines 1884–1966).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 1884.
- **The Bonfire** · present — to audit · line 1886.
- **Resting at The Bonfire** · present — to audit · line 1892.
- **(empty heading)** · ORPHAN — delete · line 1910: empty H2 used as page break
- **The Firekeeper** · present — to audit · line 1912.
- **Stat Tier Costs** · present — balance query · line 1916. Tier Three and Tier Four both cost 8 — suspected error (campaign table is 4/8/16/20).
- **(empty heading)** · ORPHAN — delete · line 1925: empty H2 used as page break
- **Blacksmith Andre** · present — to audit · line 1927.
- **Shop Rules** · present — to audit · line 1933.
- **Shop Price Table** · present — to audit · line 1951.
- **(empty heading)** · ORPHAN — delete · line 1959: empty H2 used as page break
- **Resuming Exploration** · present — to audit · line 1961.
- **(empty heading)** · ORPHAN — delete · line 1965: empty H1 used as page break

## Audit findings mapped to this chapter (53)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### A-001 · undefined-state · Major · REQUIRED
- Location: RETURNING TO THE BONFIRE › Resting at The Bonfire (manuscript.md line 1906)
- Evidence: manuscript.md:1890, 1906, 1223, 1305, 2235
- Current text: Resting at the bonfire also revives lost characters who have been removed from play due to dying while hollow.
- Proposed fix: A character who dies while hollow is lost. A lost character's model is placed on its side beside the bonfire tile and takes no further part in the encounter. When a character is lost, the encounter is failed immediately and the characters must rest at the bonfire. Resting at the bonfire revives all dead and lost characters.
- Rationale: The term 'lost' appears at lines 1890, 1906 and 2235 but is never defined. Death & Hollowing (1223) already forces an immediate rest when a hollow character dies, so 'lost' is a transient state that must be named once and added to the glossary.
- Gameplay impact: Players cannot tell whether a lost character differs from a dead one or whether lost characters return after a free (post-boss) rest.
- Decision needed: N

### A-046 · undefined-state · Major · REQUIRED
- Location: SETUP › Shop Setup › After Boss is Defeated (manuscript.md lines 1077–1089); EQUIPMENT › Embers (line 891)
- Evidence: manuscript.md:891, 1039, 1049, 1067–1089, 1935
- Current text: Draw tier one treasure cards one at a time to restock tier one shop: 3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells.
- Proposed fix: When a shop is restocked, every card remaining in that shop is placed on the bottom of its treasure deck before new cards are drawn. Ember cards remaining in the tier one shop stay in the shop and are never replaced; no ember card is ever added to a shop after setup.
- Rationale: Nothing says what happens to unsold shop cards on restock, and the ember restriction ('limited supply', 891) only works if the restock neither adds nor removes embers. Alternative: unsold cards remain and the restock only tops up to the quotas.
- Gameplay impact: Shop contents after the first boss are undefined.
- Decision needed: Y

### A-054 · contradiction · Major · REQUIRED
- Location: RETURNING TO THE BONFIRE › Resuming Exploration (manuscript.md line 1963) vs Encounter Start step 2 (line 1261), Encounter Resolution (line 1319) and The Fog Gate (line 2065)
- Evidence: manuscript.md:1261, 1317–1319, 1339, 1963, 2065
- Current text: If the encounter card on the tile is face-down (cleared or failed), they must flip the card face-up and proceed with fighting the enemies of that encounter.
- Proposed fix: After the characters rest, every encounter card is face-down. When the characters enter a tile whose card is face-down, they reveal it. If the encounter is marked cleared, the characters may skip it for the stamina cost; otherwise they must fight it. The fog gate shortcut is unaffected.
- Rationale: 'Must ... proceed with fighting' contradicts the skip rule for cleared encounters (1261, 1319) and the fog gate shortcut (2065), both of which assume the party can bypass reset tiles.
- Gameplay impact: Decides whether the skip mechanic exists after the first rest.
- Decision needed: N

### A-104 · undefined-state · Major · PROPOSED
- Location: CAMPAIGNS › Demon Hunting Section One (manuscript.md lines 2598–2608)
- Evidence: manuscript.md:1223, 1341, 1894, 2598–2608
- Current text: Section One - Undead Asylum: Level 1 Encounter, Level 1 Encounter, Asylum Demon (Mini-Boss) ... Bonfire Tile (characters revive here if they die in Section One)
- Proposed fix: Demon Hunting, Section One: there is no bonfire tile. If the characters are forced to rest during Section One, they spend a spark, revive and restore their characters as if resting, and restart Section One from its first encounter tile; the Firekeeper, Andre and the shop are not available until Section Two.
- Rationale: Every forced rest in the manuscript sends the party to the bonfire tile; Section One has none, and the parenthetical only says where characters revive, not what happens to the section. Alternative: the party is moved to Section Two's bonfire and Section One is abandoned.
- Gameplay impact: The opening section of the campaign has no defeat procedure.
- Decision needed: Y

### B-007 · arithmetic · Major · REQUIRED
- Location: L1923 (Stat Tier Costs, basic)
- Evidence: Tier Three 8 and Tier Four 8 are equal; every other cost progression is strictly increasing. The campaign table (L2303-2306) is exactly double the basic row for Tiers One-Three (4/8/16) and gives Tier Four 20, implying basic Tier Four = 10. Cumulative basic cost one stat: 2/6/14/22 as written, 2/6/14/24 with 10.
- Current text: | Tier Four  | **8**           |
- Proposed fix: | Tier Four  | **10**          |
- Rationale: Preserves the author's own 1:2:4:5 ratio between the basic and campaign tables; 16 (doubling) would cost 30 cumulative, 68% of a character's whole-game income (44 souls), and would never be bought.
- Gameplay impact: Tier Four costs 24 cumulative (55% of basic income) instead of 22; reaching it remains a deliberate end-game choice.
- Decision needed: Y

### B-016 · balance · Major · PROPOSED
- Location: L1880 (Stat Scaling)
- Evidence: Threshold = highest requirement + 10. Tier-two weapons (requirement >= 25) need a stat >= 35; the highest Tier Four value is 40 (Core p.33) or Tier Three + 5 (L1914: Herald STR 42, DEX 39, INT 34, FTH 45). Only weapons with requirement <= 30 (STR/FTH) or <= 29 (DEX) can ever scale, and only at Tier Four; tier-one weapons scale at Tier Two-Three (Mace 16 -> STR 26 at Herald Tier Two 28; Rapier 21 -> DEX 31 at Tier Three 34). Uchigatana (32), Falchion (37), Dragon Tooth (40) can never scale.
- Current text: If the character's current stat value exceeds an equipment's highest stat requirement by ten or more points, the character should mark the equipped item with a red damage cube to indicate that it is scaled.
- Proposed fix: "If the character's current stat value exceeds the equipment's highest stat requirement by five or more points, mark the equipped item with a red damage cube to indicate that it is scaled."
- Rationale: A ten-point margin rewards keeping tier-one weapons into the end-game and excludes almost every tier-two weapon; five points lets a Tier Three or Four character scale the weapons the tier-two deck is meant to deliver.
- Gameplay impact: Uchigatana scales at DEX 37 (Tier Four), Carthus Curved Greatsword at DEX 35; tier-one weapons are unchanged in practice (Mace needs STR 21, still first reached at Herald Tier Two 28).
- Decision needed: Y

### B-017 · table-text-mismatch · Major · PROPOSED
- Location: L1914 (The Firekeeper)
- Evidence: Manuscript: Tier Four = Tier Three + 5 (Herald FTH 45, INT 34). Official 1E campaign: 'The value of any stat at Tier 4 is considered to be 40' (Core p.33); Hollowed Edition p.3: 'sets the attribute to 40 stat-points, i.e. the maximum'. The highest requirement in the manuscript's weapon table is 40 (Dragon Tooth). Under '+5' a Herald INT Tier Four (34) cannot equip a 35-requirement item that a '40' rule would allow; under '40' a Herald FTH Tier Four equals Tier Three (40) and buys nothing.
- Current text: Tier four stats are all considered 5 greater than the tier three stat value.
- Proposed fix: "A stat at tier four is treated as 40, or as five greater than its tier three value if that is higher."
- Rationale: Keeps the official value, guarantees Tier Four is always an improvement, and makes every printed requirement (max 40) reachable.
- Gameplay impact: Herald Tier Four: STR 42, DEX 40, INT 40, FTH 45.
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

### C-071 · table-text · Major · REQUIRED
- Location: L1918-1923; L2301-2306; L1914
- Evidence: Basic Stat Tier Costs: 2 / 4 / 8 / 8 (Tier Four = Tier Three). Campaign: 4 / 8 / 16 / 20. Prose example L1914 'pay two souls to reach tier one before paying four additional souls to reach tier two' matches the basic table.
- Current text: Tier Four **8**
- Proposed fix: Probable error: Tier Four 16 (doubling pattern), or state explicitly that tier four costs the same as tier three. Author decision.
- Rationale: Repeated value breaks the progression and differs in shape from the campaign table.
- Gameplay impact: Cost of the final stat tier
- Decision needed: Y

### C-088 · cross-ref · Major · REQUIRED
- Location: L1223; L1906; L1195; L1341
- Evidence: Hollow death: 'any character with *hollow* status dies, then the characters are forced to immediately spend one *spark* and rest' (1223, 1341) vs 'revives *lost* characters who have been removed from play due to dying while *hollow*' (1906) vs mega-boss 'If a character dies they are permanently removed from play' (1195)
- Current text: (three statements)
- Proposed fix: Make §Death & Hollowing the single source: define *lost*, state the forced rest, and have §Resting at the Bonfire and §Setup After the main-boss cite it (with the mega-boss exception stated as an exception).
- Rationale: Three sections describe the same event with different consequences.
- Gameplay impact: Whether the encounter ends immediately when a hollow character dies
- Decision needed: Y

### C-119 · voice · Major · REQUIRED
- Location: L1205-1253; L1299-1399; L1445-1479; L1935-1949; L859-887; L931-981; L1604-1658; L2243-2293; L2314-2322; L3040-3094
- Evidence: Rules stated as bullet fragments: Death & Hollowing, Embering, Sparks (1205-1253); Encounter Resolution/Recovery, Souls (1299-1399); Treasure Rewards (1445-1479); Shop Rules (1935-1949); Spells (859-887); Terrain (931-981); Conditions (1604-1658); campaign Soul/Treasure Rewards and Shop (2243-2322); the whole PLAYER VS PLAYER chapter (3040-3094) is 27 bullets with no sentence structure
- Current text: - Encounters are *failed* if either all characters die.
- Proposed fix: Policy: PROCEDURES (setup, turn sequence, defence rolls, encounter start, resting, transposition) = numbered steps; DEFINITIONS and component anatomies (dashboard parts, data-card fields, condition effects, terrain) = bulleted lists of complete sentences; RULES (everything else) = short declarative paragraphs in 'When [trigger], [subject] must/may [action].' form. Rewrite PvP as prose plus a dodge table.
- Rationale: Fragments omit the trigger and subject that lawbook syntax requires ('Encounters are failed if either all characters die' has a dangling 'either').
- Gameplay impact: None
- Decision needed: Y

### D-005 · hybrid · Major · REQUIRED
- Location: manuscript.md 1915–1923 (Stat Tier Costs, basic game)
- Evidence: Core p.15 basic game has three tiers (2/4/8). Core p.33 campaign adds tier 4 at 20 souls with a value of 40. HE p.5 has 2/4/6/8 with tier 4 = 40 stat points marked by a red cube. The manuscript charges 8 for tier three and 8 for tier four and defines tier four as 'considered 5 greater than the tier three stat value'.
- Current text: Tier Three 8 / Tier Four 8 … Tier four stats are all considered 5 greater than the tier three stat value.
- Proposed fix: Tier Four: 12 souls. A stat at tier four has a value of 40.
- Rationale: The red-cube marker is HE; the cost column is 1E with a duplicated 8; the '+5' value matches neither source and produces different tier-four values per class and per stat. The 40 value is shared by 1E campaign and HE and is already used by the manuscript's own campaign table (20 souls, Core p.33).
- Gameplay impact: Equip thresholds at 35–40 differ by class under the '+5' rule.
- Decision needed: Y

### F-020 · tone · Major · CLEAN-UP
- Location: L1890 §Returning to the Bonfire › The Bonfire ¶2
- Evidence: Advice and flavour in rules text: 'paramount', 'hard-earned souls', 'Sparks are the most precious resource in this game and the players must carefully weigh the timing of each spark spent.'
- Current text: The characters must collectively spend one *spark to* visit the *bonfire* to rest, improve stats, upgrade equipment, and shop. Resting at the *bonfire* is paramount to restoring the characters' strength and keeping them from being *lost* to the *hollow.* Characters cannot spend their hard-earned *souls* without resting at the *bonfire*. *Sparks* are the most precious resource in this game and the players must carefully weigh the timing of each *spark* spent.
- Proposed fix: REWRITE-IN-VOICE: 'The party spends one *spark* to rest at the *bonfire*. Only while resting may characters spend *souls*, attach upgrades or trade with Andre.' CUT the final two sentences.
- Rationale: Strategy advice ('carefully weigh the timing') is not a rule.
- Gameplay impact: none
- Decision needed: N

### F-021 · register-shift · Major · CLEAN-UP
- Location: L1963 §Returning to the Bonfire › Resuming Exploration
- Evidence: Conversational prose carrying a procedure: 'Once the characters are restored to strength and no longer wish to spend souls they are nearly ready to resume…'; 'At this point characters should move…'
- Current text: Once the characters are restored to strength and no longer wish to spend souls they are nearly ready to resume their exploration of encounters. Prior to setting out, flip all cleared and failed encounter tiles face-down to reset them… At this point characters should move their models to the closest encounter tile to the bonfire tile…
- Proposed fix: REWRITE as a numbered procedure 'Leaving the Bonfire': 1. Flip every *cleared* or *failed* encounter card face-down. 2. Remove any enemy models from the encounter tiles. Terrain is not moved. 3. Place the character models on the encounter tile adjacent to the *bonfire* tile. 4. Reveal that tile's encounter card and begin the encounter (see §7.5).
- Rationale: A procedure written as narrative; 'nearly ready', 'no longer wish' are conversational.
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

### A-056 · terminology · Minor · CLEAN-UP
- Location: RETURNING TO THE BONFIRE › Resuming Exploration (manuscript.md line 1963); Terrain › Traps (line 977)
- Evidence: manuscript.md:977, 1317, 1337, 1963
- Current text: flip all cleared and failed encounter tiles face-down to reset them.
- Proposed fix: Reset: an encounter is reset by turning its encounter card face-down and setting aside any enemy models; terrain, trap and chest tokens remain in place. Replace 'encounter tiles' with 'encounter cards' at line 1963.
- Rationale: Tiles are double-sided boards; flipping them would change the map. 'Reset' is used four times without a definition.
- Gameplay impact: Cosmetic but a literal reading flips the map.
- Decision needed: N

### A-063 · omission · Minor · REQUIRED
- Location: GAMEPLAY › Encounters (manuscript.md lines 1255–1341); MIMICS (line 2043)
- Evidence: manuscript.md:1255–1341, 1890, 2043
- Current text: The then are faced with the typical option of continuing onto the next encounter or returning to rest at the bonfire for the cost of one spark.
- Proposed fix: After an encounter is cleared, the characters choose either to continue to an adjacent tile or to return to the bonfire tile and rest, spending one spark.
- Rationale: The 'typical option' is referred to only inside the Mimics chapter; the Encounters chapter never states that a voluntary return is possible between encounters.
- Gameplay impact: The core exploration decision is undocumented in the chapter that owns it.
- Decision needed: N

### A-067 · arithmetic · Minor · REQUIRED
- Location: RETURNING TO THE BONFIRE › Stat Tier Costs (manuscript.md lines 1918–1923) vs Campaign Stat Tier Costs (lines 2301–2306)
- Evidence: manuscript.md:1914, 1918–1923, 2301–2306; DS-Core-Rules-lores.txt p.15 (2/4/8), p.33 (campaign 4/8/16/20); Hollowed_Edition_v1.3.txt p.3 (2/4/6/8)
- Current text: Tier Three 8 / Tier Four 8
- Proposed fix: Tier Four: 16 souls.
- Rationale: Tier four costing the same as tier three breaks the doubling pattern that the campaign table (4/8/16/20) follows. Alternative: 2/4/6/8 as in Hollowed Edition.
- Gameplay impact: Tier four is the strongest upgrade; mispricing it drives stat inflation.
- Decision needed: Y

### A-074 · contradiction · Minor · CLEAN-UP
- Location: EQUIPMENT › Upgrades (manuscript.md line 853); Shop Rules (line 1943); COMMUNITY UPDATE PACK (line 3182)
- Evidence: manuscript.md:853, 1941, 1943, 3182–3184
- Current text: Titanite upgrades (i.e.: Titanite Shards) attached to sold weapons are returned to the bottom of the tier one treasure deck.
- Proposed fix: Titanite upgrades attached to a sold weapon are returned, with the weapon, to the bottom of the treasure deck of the weapon's tier.
- Rationale: The Update Pack makes Titanite Chunk a 25/25 (tier two) card; the sell rule sends all titanite to tier one.
- Gameplay impact: Cosmetic deck-composition drift.
- Decision needed: N

### A-076 · contradiction · Minor · REQUIRED
- Location: SETUP › Legendary Treasure (manuscript.md line 1025) vs Shop Setup › After Boss is Defeated step 2 (lines 1083–1089)
- Evidence: manuscript.md:1025, 1083–1089, 1935
- Current text: These represent exceedingly rare relics that do not appear in every game and cannot be purchased.
- Proposed fix: If a legendary treasure card is drawn while stocking a shop, shuffle it back into the tier two treasure deck and draw again.
- Rationale: Once legendaries are in the tier two deck, a later restock (before a mega-boss) draws from that deck and would put a legendary in the shop.
- Gameplay impact: Rare; only affects mega-boss games.
- Decision needed: N

### A-077 · undefined-state · Minor · OPTIONAL
- Location: RETURNING TO THE BONFIRE › Shop Rules (manuscript.md line 1941)
- Evidence: manuscript.md:1937, 1941, 1957, 2332
- Current text: Sold items are placed at the bottom of their respective treasure deck.
- Proposed fix: Sold boss treasure and legendary treasure cards are returned to the game box; all other sold cards go to the bottom of the treasure deck of their tier.
- Rationale: Boss and legendary cards have no 'respective' deck.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-100 · contradiction · Minor · REQUIRED
- Location: SUMMONS › Phantoms steps 1–3 (manuscript.md lines 1973–1981); The Bonfire (line 1890)
- Evidence: manuscript.md:1890, 1973–1981
- Current text: Characters cannot spend their hard-earned souls without resting at the bonfire. / Embered characters may elect to pay two souls to draw a phantom card.
- Proposed fix: Souls are spent only while resting at the bonfire, except that an embered character may spend two souls at the fog gate to draw one phantom data card. The players choose one drawn phantom to summon and return the others to the supply; souls paid are not refunded.
- Rationale: The general restriction contradicts the summoning cost, and the outcome of several embered characters each drawing is unstated.
- Gameplay impact: Small; affects phantom summoning only.
- Decision needed: N

### C-027 · italics · Minor · REQUIRED
- Location: L793; L1369; L1445; L1776; L1840; L1890; L1906; L1963; L2043; L2047; L2099; L2185; L2195
- Evidence: Punctuation inside italics: '*heroic actions, luck, and estus flask.*' (793); '*failed:*' (1369); '*cleared.*' (1445); '*Push, area-of-effect,*' (1776); '*dodge,*' and '*walk, run,*' (1840); '*hollow.*' (1890, 1906); '*failed),*' (1963); '*spark.*' (2043); '*cleared.*.' (2047); '*threat, block,*' (2099); '*, resist,*' (2185); '*embered.*' (2195)
- Current text: *cleared.* etc.
- Proposed fix: Italicise the term only; punctuation outside: '*cleared*.' - and italicise each term separately in lists: '*walk*, *run*,'
- Rationale: Keyword italics must not include punctuation or spaces; it breaks glossary linking and search.
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

### C-045 · terminology · Minor · REQUIRED
- Location: L771; L1451; L2314; L2316; L1920-1923; L1955-1956; L2303-2306; L2330-2331; L689; L1914; L2299
- Evidence: 'tier one/two' lower-case x60 in prose; 'Tier One/Two' x10 in table and heading labels; 'Tier one/two' mid-sentence (1451, 2314, 2316). Separately, 'tier' has two senses: stat tier (771 'from base tier to tier two', 1914) and treasure tier (1013 'tier two treasure deck').
- Current text: Tier one treasure deck (mid-sentence); 'tier two' (stat sense) unqualified
- Proposed fix: Lower-case 'tier one/two' in prose; Title Case only in headings and table row labels. Always qualify the stat sense as 'stat tier' ('stat tier two') and the treasure sense as 'tier two' ('tier two treasure', 'tier two shop').
- Rationale: Ambiguity: L771 'tier two' means a stat tier while L1013 'tier two' means a treasure deck.
- Gameplay impact: Misreading stat tiers as treasure tiers
- Decision needed: Y

### C-051 · terminology · Minor · CLEAN-UP
- Location: L793; L797; L801; L995; L1099; L1900; L961ff
- Evidence: Tokens defined with a 'ready side' and 'used side' (793-801) but then 'flipped face-down' (793), 'face-up on each character's dashboard' (995), 'Flip ... tokens face-up' (1900); cards 'face-down' x37, 'face down' x1 (1181), 'face up' (1099)
- Current text: flip face-down (tokens); face up / face-down (mixed hyphenation)
- Proposed fix: Tokens: 'flip to the used side' / 'flip to the ready side'. Cards and tiles: 'face up' / 'face down' as predicates ('place the card face down'), hyphenated only as an attributive adjective ('a face-down card').
- Rationale: Two-sided tokens have named sides; cards do not. Hyphenation follows grammatical role.
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

### C-060 · terminology · Minor · CLEAN-UP
- Location: L801; L1720; L1744; L1780; L1876; L1846; L3194; L763; L805; L1814; L891; L1201; L1908; L373-379; L2225
- Evidence: 'reroll' x8 vs 're-roll' x2 (1846, 3194); 'back-up slot' x2 vs 'backup slot' (891); 'PvP' x10 vs 'player versus player (PvP)' (1201) vs 'player-versus-player (PvP)' (1908); 'rule set'/'ruleset'/'rule-set'; 'rule book'/'rulebook'/'rule-book'
- Current text: (variants)
- Proposed fix: reroll; back-up slot; define 'player versus player (PvP)' once (L1201) then 'PvP'; ruleset; rulebook
- Rationale: One spelling per compound.
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

### C-098 · heading · Minor · REQUIRED
- Location: L893; L983; L1059; L1441; L1842; L1882; L1910; L1925; L1959; L1965; L2049; L2059; L2215; L2308; L2324; L2336; L2400; L3036; L3096; L3100
- Evidence: 20 empty headings ('# ', '## ', '### ') used as page breaks
- Current text: #  (empty)
- Proposed fix: Delete all 20; page breaks belong to layout, not structure.
- Rationale: Empty headings produce blank TOC entries and broken numbering.
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

### C-111 · punctuation · Minor · CLEAN-UP
- Location: L375; L529; L805; L835; L853; L1025; L1529; L1726; L1826; L1904; L1929; L1985; L2310; L2312; L2314; L837; L839; L2047
- Evidence: Mixed quotation marks: curly apostrophe ’ x146 in the body vs straight ' in ~20 lines (e.g. L529 'Executioner's Chariot (Executioner’s Chariot)' has both forms in one line); curly double quotes “ ” at 837, 839, 2047
- Current text: ' / ’ mixed
- Proposed fix: Policy: straight quotes in the Markdown source; the typesetter converts to curly. Until then, make every line consistent (curly).
- Rationale: Mixed glyphs show in print.
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

### C-123 · voice · Minor · CLEAN-UP
- Location: L979; L1596; L1674; L1676; L2157; L2191; L2207; L1963
- Evidence: Conversational filler: 'simply stop adding trap tokens' (979); 'Of course,' (1596); 'it simply does not move' (1674, 1676); 'and so-on' (2157); 'one can assume... simply move' (2191); 'it is possible for a demon to smash through multiple pillars' (2207); 'nearly ready to resume' (1963)
- Current text: simply / Of course / and so-on / one can assume / it is possible
- Proposed fix: Delete the filler; state the rule: 'the enemy does not move'; 'A demon may destroy several pillars with one attack.'
- Rationale: Terse voice.
- Gameplay impact: None
- Decision needed: N

### D-011 · dropped-rule · Minor · OPTIONAL
- Location: manuscript.md 1913–1923 (The Firekeeper)
- Evidence: Core p.15: 'A character must spend 1 soul to flip their Luck token to the ready side' at the Firekeeper. The manuscript restores luck only by resting (1901) and gives no replacement.
- Current text: (absent)
- Proposed fix: At the Firekeeper a character may pay one soul to flip their luck token to the ready side.
- Rationale: Probably an intentional drop (luck is stronger in the manuscript, rerolling any number of dice), but it is not acknowledged; the author decides.
- Gameplay impact: Minor economy change.
- Decision needed: Y

### D-038 · underspecified-deviation · Minor · REQUIRED
- Location: manuscript.md 1906 (Resting at The Bonfire) vs 1224 (Death & Hollowing)
- Evidence: 'Lost' characters 'removed from play due to dying while hollow' are revived by resting, but 1224 says a hollow death forces an immediate rest, so no character is ever 'lost' between encounters; the term is undefined.
- Current text: Resting at the bonfire also revives lost characters who have been removed from play due to dying while hollow.
- Proposed fix: Resting at the bonfire revives every dead character.
- Rationale: Removes an undefined status; the forced rest already covers the case.
- Gameplay impact: None.
- Decision needed: N

### F-019 · tone · Minor · OPTIONAL
- Location: L1888 §Returning to the Bonfire › The Bonfire ¶1
- Evidence: Chapter-intro flavour, 93 words: 'The bonfire serves as a safe haven in an otherwise treacherous world… a mysterious blindfolded woman… a massive smith toiling endlessly at his forge.'
- Current text: The *bonfire* serves as a safe haven in an otherwise treacherous world. When the characters arrive, there are two strangers, who wish to help the characters on their journey. The first of which is the Firekeeper, a mysterious blindfolded woman… Andre runs a shop and will also upgrade the character's equipment, if they bring him suitable materials.
- Proposed fix: KEEP-AS-INTRO, trimmed to ≤60 words: 'The *bonfire* is a safe haven in a treacherous world. Two strangers wait beside it. The Firekeeper, blindfolded and silent, strengthens the characters in exchange for *souls*. Blacksmith Andre, toiling at his forge, sells equipment and fits upgrades.'
- Rationale: Intro flavour is permitted but must be short and must not carry rules ('will also upgrade… if they bring him suitable materials' is a rule stated in flavour).
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

### C-044 · terminology · Note · CLEAN-UP
- Location: L1169; L1187; L1888; L1902; L1912; L2195; L2297
- Evidence: 'Firekeeper' x8, no variants; matches Core/TG rulebooks ('Firekeeper' x16)
- Current text: Firekeeper
- Proposed fix: No change
- Rationale: Consistent; record in style sheet.
- Gameplay impact: None
- Decision needed: N

### C-092 · example · Note · OPTIONAL
- Location: L849; L771; L1914; L1918-1923
- Evidence: Upgrade-limit example (849: limit two -> up to two upgrade cards) correct. Stat-tier examples (771 'pay... tier one upgrade, and then the tier two upgrade'; 1914 'two souls to reach tier one before paying four additional souls to reach tier two') match the basic Stat Tier Costs table (2, 4). The campaign table (4, 8) differs; the 1914 example sits in the basic chapter.
- Current text: (verified)
- Proposed fix: Add to §The Bonfire Tile (campaign): 'In campaign play the same example costs four then eight souls.'
- Rationale: Examples verified; one clarifying sentence recommended.
- Gameplay impact: None
- Decision needed: N

### F-123 · copied-prose · Note · OPTIONAL
- Location: L1888 §Returning to the Bonfire › The Bonfire
- Evidence: Matches official text — phrase borrowing only; remainder is the author's flavour (blindfolded woman, toiling smith)
- Current text: The bonfire serves as a safe haven in an otherwise treacherous world…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: V2 p.26 ('The bonfire is a safe haven where characters can rest for a short time'). Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-124 · copied-prose · Note · OPTIONAL
- Location: L1931 §Returning to the Bonfire › Blacksmith Andre
- Evidence: Matches official text — loose paraphrase (8-word run)
- Current text: Characters may attach any weapon upgrade cards from their inventory to equipped weapon cards and armour upgrade cards to equipped armour…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: V2 p.27. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

## Completion entries that apply (2) — approved at Gate 1

### [CMP-0006] Gameplay › Death & Hollowing — "Lost" state — Proposed Completion
- Read `04_completion_backlog.md` lines 683–710 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

### [CMP-0019] Gameplay › Encounter Resolution / Returning to the Bonfire › Resuming Exploration — Reset and skip reconciliation — Proposed Completion
- Read `04_completion_backlog.md` lines 1128–1145 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

