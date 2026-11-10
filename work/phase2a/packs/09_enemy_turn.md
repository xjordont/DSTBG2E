# Drafting pack — chapter 09 (enemy_turn) — manuscript chapter "ENEMY TURN"

Source text: `work/phase2a/source/09_enemy_turn.md` (manuscript.md lines 1660–1797).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 1660.
- **Overview** · present — to audit · line 1662.
- **Enemy Movement** · present — to audit · line 1668.
- **Towards aggro** · present — to audit · line 1680.
- **Away from aggro** · present — to audit · line 1684.
- **Towards nearest** · present — to audit · line 1688.
- **Away from nearest** · present — to audit · line 1692.
- **Push-move** · present — to audit · line 1696.
- **Push-attack** · present — to audit · line 1700.
- **Enemy Attacks** · present — to audit · line 1704.
- **Block & Resist** · present — to audit · line 1710.
- **Dodge** · present — to audit · line 1734.
- **Parry & Riposte** · present — to audit · line 1766.

## Audit findings mapped to this chapter (54)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### A-023 · inherits-official-silently · Blocker · REQUIRED
- Location: ENEMY TURN › Enemy Attacks (manuscript.md line 1706)
- Evidence: manuscript.md:1672, 1706, 1596; DS-Core-Rules-lores.txt p.25 (attack target icons, node icon, out-of-range miss, movement attacks); DS-TG-Rulebook p.25
- Current text: Additional symbols beside the attack type icon modify the attack with special rules detailed later.
- Proposed fix: An enemy attack targets the character shown by the small icon beside the attack icon: the skull icon targets the character with the aggro token; the ring icon targets the nearest character, with ties resolved as for enemy movement. If the target is not within the attack's range, the attack misses and has no effect. An attack with the node icon targets every character on the target's node; each targeted character defends separately. A push-movement that shows a damage value is a physical attack against every character on each node the enemy moves into, resolved separately for each character and defended as a normal attack.
- Rationale: The promised 'special rules detailed later' never appear. Target selection, node (area) attacks and the out-of-range miss are defined only for movement, and the manuscript's push-movement paragraph (1594) never says that the damage number is an attack. Every enemy data card depends on these icons.
- Gameplay impact: Enemy attacks cannot be resolved from the manuscript alone.
- Decision needed: N

### A-032 · undefined-state · Blocker · REQUIRED
- Location: PLAYER VS PLAYER (manuscript.md lines 3040–3094)
- Evidence: manuscript.md:1485, 1708–1797, 1846–1872, 3060, 3082–3094
- Current text: Character turn structure is unchanged from basic rules. ... Dodge difficulty is based on an the attacker attack option's stamina cost
- Proposed fix: When a character attacks another character, the attacker resolves the attack option as if against an enemy and determines the final attack value. The defender then chooses to block, resist, dodge or parry exactly as against an enemy attack whose attack value equals that final attack value and whose dodge difficulty is given by the stamina-cost table. Damage suffered equals the attack value minus the defence total. Push, condition, shift and area-of-effect icons apply to characters as they apply to enemies; an area-of-effect attack targets every other character on the target node. A parry requires the attacker to share the defender's node; a successful parry staggers the attacker and permits a riposte. Block and resist values of defenders are never subtracted from the attack value; defence is always rolled.
- Rationale: The PvP chapter supplies turn order, traps and a dodge table but never says how a character-versus-character attack is resolved: the enemy-attack procedure assumes a fixed attack value, the character-attack procedure assumes a fixed block value, and neither covers push, AoE, conditions or parry against a character.
- Gameplay impact: PvP cannot be played from the text.
- Decision needed: N

### D-008 · dropped-rule · Blocker · REQUIRED
- Location: manuscript.md 1706 (Enemy Attacks), 1485 (Target versus Hit)
- Evidence: Core p.25 defines enemy attack targeting: skull icon = character with the aggro token, ring icon = nearest character (ties → aggro, then higher taunt); an attack whose target is out of range misses; the Node icon attacks every character on the target's node, each rolling separately. V2 p.25 repeats this. The manuscript explains these icons only for movement (1672–1694) and says attack modifiers are 'detailed later', but no such section exists.
- Current text: Additional symbols beside the attack type icon modify the attack with special rules detailed later.
- Proposed fix: An attack with the skull icon targets the character with the aggro token. An attack with the ring icon targets the nearest character; if two or more characters are tied for nearest, the attack targets the one with the aggro token, and otherwise the tied character with the higher threat level. If the target is not within the attack's range, the attack misses and has no effect. An attack with the node icon targets every character on the target's node; each defends separately.
- Rationale: Silently dropped from Core p.25 while the movement half of the same page was copied; without it an enemy turn cannot be resolved.
- Gameplay impact: Every enemy attack.
- Decision needed: N

### A-013 · undefined-state · Major · REQUIRED
- Location: GAMEPLAY › Encounters › Encounter Turn Order step 3 (manuscript.md line 1291); ENEMY TURN › Enemy Movement (line 1672)
- Evidence: manuscript.md:1275, 1291–1293, 1672, 1682; DS-Core-Rules-lores.txt p.22 (aggro passes on activation)
- Current text: After all characters have taken their turn, place the aggro token on the character who placed the most damage tokens on enemy models.
- Proposed fix: When the character holding the aggro token dies, immediately place the aggro token on the living character with the highest threat value; if several are tied, the players choose. The aggro token is never held by a dead character.
- Rationale: Enemy movement and attacks target the aggro holder; nothing says what happens when that character is removed from play mid-round. In the official game the token moves every character activation, so the state never arises.
- Gameplay impact: Enemy behaviours become unresolvable for the rest of the round after a death.
- Decision needed: N

### A-068 · inherits-official-silently · Major · REQUIRED
- Location: ENEMY TURN › Parry & Riposte (manuscript.md lines 1772, 1790); CHARACTER TURN › Major Action › Attack (line 1822); CHARACTERS › Equipment Slots (line 761)
- Evidence: manuscript.md:757–763, 1772, 1790, 1822; DS-Core-Rules-lores.txt p.12 (left-hand and right-hand slots); DS-TG-Rulebook p.8 (hand slots)
- Current text: Characters must be equipped with a shield as their left weapon. ... using any attack option on the weapon equipped to the right weapon slot.
- Proposed fix: Equipment Slots: The two weapon slots are the left-hand slot and the right-hand slot; a one-handed card may be placed in either. Parry: Characters must have a shield equipped in one weapon slot and a weapon with at least one attack option in the other; the riposte uses that weapon.
- Rationale: Left and right slots exist on the official dashboards but the manuscript's Equipment Slots section never names them; the parry rule then depends on which physical slot holds the shield, which is a player choice with no rule attached.
- Gameplay impact: Players cannot tell whether a shield in the right slot permits a parry.
- Decision needed: N

### A-078 · procedural · Major · REQUIRED
- Location: COMBAT BASICS › Conditions (manuscript.md line 1600); Stagger (line 1638); Parry & Riposte (line 1788)
- Evidence: manuscript.md:1600, 1638, 1664, 1788, 1796; DS-Core-Rules-lores.txt p.21; DS-TG-Rulebook p.21
- Current text: When a model ends its turn, remove one poison token and any frostbite/stagger tokens.
- Proposed fix: A stagger or frostbite token is removed at the end of the affected model's next complete turn. A token placed on a model during that model's own turn remains until the end of the model's following turn.
- Rationale: A successful parry staggers the attacking enemy during that enemy's own turn; the token is then removed at the end of the same turn, before any character attacks, so the parry's stagger has no effect unless the enemy has further attack icons. Alternative: keep the end-of-own-turn removal and state that the parry stagger applies to the remainder of the enemy's current turn only.
- Gameplay impact: The parry reward is largely void under the literal text.
- Decision needed: Y

### A-082 · undefined-state · Major · REQUIRED
- Location: TILES & NODES › Terrain › Gravestones, Barrels, Chests (manuscript.md lines 931, 949, 959); Character Movement (line 1840)
- Evidence: manuscript.md:931, 949, 951, 959, 1670–1678, 1840, 2175; DS-Core-Rules-lores.txt p.17 ('Gravestones block movement')
- Current text: Models cannot walk, run, dodge, or be pushed into nodes containing a gravestone. / Models cannot walk or run into nodes containing barrels. / Models cannot move, dodge, or be pushed into nodes containing a chest.
- Proposed fix: No model, including enemies and bosses, may move, leap, dodge or be pushed into a node containing a gravestone or a chest. No model may walk, run, shift or move into a node containing an intact barrel; a model that dodges or is pushed into such a node destroys the barrel and the token is removed.
- Rationale: Enemy movement is 'move', which is not in the gravestone or barrel lists; whether enemies and leaping bosses are blocked by terrain is unstated.
- Gameplay impact: Enemy pathing around terrain is decided every encounter.
- Decision needed: N

### B-002 · balance · Major · PROPOSED
- Location: L1722 (Enemy Attacks > Block & Resist, step 4)
- Evidence: Defence total = two highest dice. With black dice the ceiling is 4 (2+2); mean of 2 black = 2.33, best-two-of-3 black = 2.88, best-two-of-4 black = 3.19. Official 1E (Core p.25) sums all dice (3 black mean 3.50). Combined with the Enemy Scaling table (L1519) this caps what any block build can absorb.
- Current text: Determine the defence total by adding the number of sword pips on the highest two dice results. Additional dice beyond the two with the highest shown face value are ignored.
- Proposed fix: Keep the rule but state the consequence in the Enemy Scaling section (see B-003/B-004) or raise the cap: "Determine the defence total by adding the number of sword pips on the highest two dice results. A shield adds its block dice to the pool and, if the character has a shield equipped, the three highest dice are used instead."
- Rationale: Hollowed Edition p.7 introduced the two-dice cap to tame armour stacking, but it was paired with unscaled enemy attack values. The manuscript adds +1 attack at 3 players and Repeat at 4 players against the same cap, so damage leaks through on every hit at 3-4 players.
- Gameplay impact: At 4 players a scaled Hollow Soldier (attack 5, Repeat 2) deals an expected 5.3 damage per activation to a 2-black-die blocker (see §2).
- Decision needed: Y

### B-022 · undefined-value · Major · REQUIRED
- Location: L1069/L1079/L1085 (Shop Setup) with L823-829 (Equipment Cards), L747-753 (Equipment Slots), L1769 (Parry)
- Evidence: The stock list requires '2 shields' per shop and the parry rule requires 'a shield as their left weapon', but the card-typing rules define only one-handed weapon, two-handed weapon, armour (by icon) and spell (by scroll art). No rule says how a shield is recognised; shields are weapon-typed cards in 1E (East-West Shield appears in the manuscript's own weapons table, L3244).
- Current text: Equipment cards include weapons, spells, shields, armour, and items which the character equips to improve their combat capabilities. ... 3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells.
- Proposed fix: Add to Equipment Cards: "A shield is a one-handed weapon card that shows a block or resist value and has no attack option. Shields count as weapons for equipment slots and as shields for shop stocking and parrying."
- Rationale: The shop and parry procedures cannot be executed without a test for 'shield'.
- Gameplay impact: Makes the 12-card stock list and the parry prerequisite determinable.
- Decision needed: Y

### C-024 · hedge · Major · REQUIRED
- Location: L1666
- Evidence: 'If there is no valid target or the enemy behaviour otherwise cannot be reasonably executed, that enemy behaviour is skipped'
- Current text: cannot be reasonably executed
- Proposed fix: 'If an enemy behaviour has no valid target or cannot be executed, skip that icon and resolve the next icon to the right.'
- Rationale: 'Reasonably' invites table argument about enemy AI; the condition must be mechanical.
- Gameplay impact: Enemy behaviour resolution
- Decision needed: N

### C-036 · terminology · Major · REQUIRED
- Location: L1285; L1291; L1293; L1850
- Evidence: 'the model with the most damage tokens' (1285); 'the character who placed the most damage tokens on enemy models' (1291, 1293); 'place a number of damage tokens onto the target enemy model's base' (1850) vs 'wound token' (681, 1517, 1664, 2099) and 'damage cubes' for characters (x16)
- Current text: damage tokens
- Proposed fix: wound tokens (enemies); damage cubes (characters)
- Rationale: Two components, two names: enemies take wound tokens (L1517), characters take red damage cubes (L779). 'Damage token' is neither.
- Gameplay impact: Avoids confusion between the two damage-tracking components
- Decision needed: N

### D-030 · underspecified-deviation · Major · REQUIRED
- Location: manuscript.md 1772, 1790, 1822 (Parry; Major Action) vs 757–763 (Equipment Slots)
- Evidence: Core p.12 names left-hand and right-hand slots; the manuscript's Equipment Slots section names only 'the weapon slots' but the parry rule requires a shield in the 'left weapon slot' and the riposte uses the 'right weapon slot'.
- Current text: Characters must be equipped with a shield as their left weapon … using any attack option on the weapon equipped to the right weapon slot
- Proposed fix: The two weapon slots are the left-hand slot and the right-hand slot. A card equipped in either slot is in hand.
- Rationale: Parry and riposte cannot be applied without named slots.
- Gameplay impact: Defensive option availability.
- Decision needed: N

### F-070 · prose-crossref · Major · CLEAN-UP
- Location: L1706 §Enemy Turn › Enemy Attacks
- Evidence: Prose cross-reference: 'with special rules detailed later'
- Current text: with special rules detailed later
- Proposed fix: '(see §8.4, §8.5 and §16.3)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: IMPRECISE — targets are §8.4 Pushing and §8.5 Conditions (earlier), and §16.3 Boss Attacks (later). Numbering per F_report.md §6 provisional map.
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

### A-018 · undefined-state · Minor · OPTIONAL
- Location: BOSS TURNS › Boss Aggro (manuscript.md line 2191); Parry & Riposte (line 1790)
- Evidence: manuscript.md:1790, 2191
- Current text: ...simply move the aggro token to a character's dashboard if they deal any damage to the boss during their turn.
- Proposed fix: Damage inflicted on a boss by a riposte during the boss's turn moves the aggro token to the riposting character at the end of that boss turn.
- Rationale: A riposte is an out-of-turn attack; the boss aggro rule only covers damage dealt 'during their turn'.
- Gameplay impact: Edge case created by the manuscript's own parry rule.
- Decision needed: N

### A-025 · undefined-state · Minor · OPTIONAL
- Location: COMBAT BASICS › Enemy Scaling (manuscript.md line 1527); CAMPAIGN PLAY › Bonfire Ascetic (line 2342)
- Evidence: manuscript.md:1527, 1594, 1702, 2342
- Current text: If playing with three or more characters, increase all non-boss attack values by one.
- Proposed fix: Attack value increases from scaling and from the bonfire ascetic apply to every attack icon and to the damage value of push-movements.
- Rationale: Push-movement damage (1702) is a number inside a movement icon, not an 'attack value'; the scaling text does not say whether it is increased. Alternative: push-movement damage is never modified.
- Gameplay impact: Trampling enemies (Sentinel, Smelter-type) are the ones where the +1 matters most.
- Decision needed: Y

### A-042 · undefined-state · Minor · OPTIONAL
- Location: BOSS ENCOUNTERS › Boss Behaviour Cards (manuscript.md line 2125); Parry & Riposte (line 1790)
- Evidence: manuscript.md:1790, 2125, 2159
- Current text: When the boss's health is reduced to (or below) its Heat Up point, take a random Heat Up behaviour card and shuffle it into the boss behaviour deck.
- Proposed fix: If the boss heats up during its own turn (for example from a riposte), finish resolving the current behaviour card, then shuffle the Heat Up card into the remaining behaviour deck. If the behaviour deck is empty at that moment, the Heat Up card becomes the behaviour deck and the discard pile is not yet renewed.
- Rationale: A riposte can damage the boss mid-card; and the deck may be empty (all cards in the discard) when heat-up occurs.
- Gameplay impact: Edge case that arises once in most boss fights with a parrying character.
- Decision needed: N

### A-070 · undefined-state · Minor · OPTIONAL
- Location: EQUIPMENT › Spells (manuscript.md lines 877–887); Character Attacks (line 1846)
- Evidence: manuscript.md:861, 877–887, 1712, 1846
- Current text: Spells stored within their respective catalyst may use their attack options as if equipped.
- Proposed fix: A stored spell provides only its attack options; its block, resist and dodge values are ignored. Using a stored spell's attack option counts as the catalyst's one attack for that turn.
- Rationale: Block and Resist gather dice from 'equipped' cards; 'as if equipped' invites counting stored spells' defence values and a second attack from the same slot.
- Gameplay impact: Prevents a catalyst with three stored spells becoming a multi-attack slot.
- Decision needed: N

### A-079 · undefined-state · Minor · REQUIRED
- Location: COMBAT BASICS › Conditions › Stagger (manuscript.md line 1636)
- Evidence: manuscript.md:1636, 1515, 1708; DS-Core-Rules-lores.txt p.21 (enemy stagger: attack damage −1)
- Current text: Staggered models subtract one from attack, block, resist, and dodge.
- Proposed fix: A staggered enemy reduces its attack value and its dodge difficulty by one, and its block and resist values by one. A staggered character subtracts one from the result of each attack, block, resist and dodge roll.
- Rationale: Enemies have fixed values and a dodge difficulty rather than rolls; the single sentence has to be read two ways.
- Gameplay impact: Affects every parry and every stagger weapon.
- Decision needed: N

### A-087 · undefined-state · Minor · OPTIONAL
- Location: ENEMY TURN › Dodge step 4.4 (manuscript.md line 1754)
- Evidence: manuscript.md:1754, 1840, 2145; Dark_Souls_The_Board_Game_FAQ.txt (official dodge: 'can move one node')
- Current text: The character must move to an adjacent node.
- Proposed fix: If no valid adjacent node exists, the dodging character remains on their node.
- Rationale: The mandatory dodge move (a deliberate change from the official optional move) has no fallback when terrain and node limits block every adjacent node.
- Gameplay impact: Rare.
- Decision needed: N

### A-113 · terminology · Minor · CLEAN-UP
- Location: GAME COMPONENTS › Tokens (manuscript.md line 681); Encounter Turn Order (line 1285); Character Attacks (line 1850); Enemy Turn Overview (line 1664)
- Evidence: manuscript.md:681, 1285, 1291, 1517, 1664, 1850
- Current text: Wound tokens / damage tokens / wounds
- Proposed fix: Use 'wound token' throughout for the tokens placed on enemies and 'damage cube' for the red cubes on endurance bars.
- Rationale: Three terms for one component.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-116 · terminology · Minor · CLEAN-UP
- Location: ENEMY TURN › Overview (manuscript.md line 1666)
- Evidence: manuscript.md:1666
- Current text: If there is no valid target or the enemy behaviour otherwise cannot be reasonably executed, that enemy behaviour is skipped
- Proposed fix: If an icon has no valid target or cannot be resolved, skip it and resolve the next icon.
- Rationale: Hedge word in a rule.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-119 · undefined-state · Minor · OPTIONAL
- Location: ENEMY TURN › Parry & Riposte step 5.4 (manuscript.md line 1790)
- Evidence: manuscript.md:1790, 1846, 1876, 2149
- Current text: The character may make one riposte attack out of turn against the attacker using any attack option on the weapon equipped to the right weapon slot after paying the associated stamina cost.
- Proposed fix: A riposte is an attack for all purposes (two-handed reroll, luck, weak-arc die, conditions) except that it does not count towards the limit of one attack per weapon per turn.
- Rationale: Nothing says whether the riposte consumes the weapon's attack for the character's next turn or benefits from attack modifiers.
- Gameplay impact: Arises on every successful parry.
- Decision needed: N

### A-120 · undefined-state · Minor · OPTIONAL
- Location: ENEMY TURN › Block & Resist step 4 (manuscript.md line 1722); Equipment Cards (line 843)
- Evidence: manuscript.md:843, 1722
- Current text: Determine the defence total by adding the number of sword pips on the highest two dice results.
- Proposed fix: Fixed modifiers printed on equipment defence values are applied after the two highest dice are summed.
- Rationale: Dice modifiers (843) are defined for attacks; the two-highest-dice defence rule does not say where a defensive modifier applies.
- Gameplay impact: Affects a handful of armour cards.
- Decision needed: N

### B-005 · undefined-value · Minor · REQUIRED
- Location: L1529 (Enemy Scaling) with L1627-1690 (Push-move / Push-attack)
- Evidence: Skeleton Soldier (V2 p.24) has no attack icon; its only damage is a push attack inside its move. The rule adds Repeat to the 'attack behaviour'; it is undefined whether a push-move with damage counts, and the 2-player move 1 -> 2 rule already doubles that enemy's possible hits.
- Current text: If playing with four characters, add *repeat to* each non-boss enemy's attack behaviour.
- Proposed fix: If Repeat is retained: "Repeat applies to attack icons only. Movement behaviours, including push-moves that deal damage, are never repeated."
- Rationale: Removes an ambiguity that otherwise quadruples push-mover damage at 4 players (two moves x Repeat 2).
- Gameplay impact: Prevents a 2-damage push enemy becoming an 8-hit threat.
- Decision needed: N

### B-033 · balance · Minor · PROPOSED
- Location: L1742 (Dodge step 2.2)
- Evidence: Two extra stamina buy one extra green die (p = 0.5). Against dodge difficulty 2 (Hollow Soldier, Core p.20) a two-dice character rises from 0.25 to 0.50; expected damage avoided = 0.25 x 1.67 = 0.42 for 2 stamina, which also buys a full Shortsword [2] attack (3.50 raw). Against difficulty 1: 0.75 -> 0.875.
- Current text: Characters may spend two additional stamina (total of three stamina cost) before rolling dice to add a single additional *dodge* die to their roll, up to a maximum of four *dodge* dice.
- Proposed fix: "Characters may spend one additional stamina (total of two stamina) before rolling dice to add a single additional dodge die to their roll, up to a maximum of four dodge dice."
- Rationale: At 2 extra stamina the option is almost never worth taking; at 1 it is a real decision.
- Gameplay impact: Dodge-build characters gain an affordable emergency option; expected stamina spent on dodging rises slightly.
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

### C-047 · terminology · Minor · CLEAN-UP
- Location: L2115; L3082; L831; L1501; L1734
- Evidence: 'Dodge difficulty' plain capital (2115, 3082); '*Dodge*' italic capital in lists/headings (831, 1501, 1734); '*dodge*' x22 and plain 'dodge' x16 elsewhere
- Current text: Dodge
- Proposed fix: *dodge* (lower-case keyword; capital only at sentence start or in a heading)
- Rationale: Keyword case must be uniform.
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

### C-083 · cross-ref · Minor · REQUIRED
- Location: L1706
- Evidence: 'Additional symbols beside the attack type icon modify the attack with special rules detailed later.' Push (1586) and Conditions (1598) are earlier; only Boss Attacks (2181) is later.
- Current text: special rules detailed later
- Proposed fix: '(see §Pushing, §Conditions and §Boss Attacks)'
- Rationale: Direction word is wrong for two of three targets.
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

### C-101 · heading · Minor · CLEAN-UP
- Location: L1111; L1119; L1143; L1173; L1680-1700; L523; L1015; L1041; L1091; L2454ff; L361; L2217
- Evidence: Case and whitespace: sentence-case H3s 'Encounter tiles' (1111), 'Encounter cards' (1119), 'Towards aggro', 'Away from aggro', 'Towards nearest', 'Away from nearest', 'Push-move', 'Push-attack' (1680-1700); mixed 'Setup After the mini-boss' (1143, 1173); 'Mega-bosses' (523) vs 'Mini-Bosses'/'Main-Bosses'; 'Class-specific Treasure' (1015); trailing spaces (1041, 1091, 2454, 2502, 2548, 2594, 2662, 2718, 2764, 2810, 2882, 2946, 2992); double space '#  INTRODUCTION' (361), '#  CAMPAIGN PLAY' (2217)
- Current text: Encounter tiles / Towards aggro / Mega-bosses
- Proposed fix: H1 ALL CAPS (chapter), H2 and H3 Title Case ('Encounter Tiles', 'Towards Aggro', 'Mega-Bosses', 'Setup After the Mini-Boss'); keyword italics permitted inside headings; no trailing or double spaces
- Rationale: One case convention per heading level.
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

### C-112 · punctuation · Minor · CLEAN-UP
- Location: L679; L895; L1199; L1203; L1710; L1766; L2161; L2201; L2237; L449; L2398
- Evidence: '&' in nine headings and in list items 'Mushroom Child & Parent' (449), 'Ornstein & Smough' (2398, 2500, 2660, 2934)
- Current text: &
- Proposed fix: 'and' in headings and prose; '&' only inside an official product or card name
- Rationale: Ampersand is a logo/label device, not prose.
- Gameplay impact: None
- Decision needed: N

### C-123 · voice · Minor · CLEAN-UP
- Location: L979; L1596; L1674; L1676; L2157; L2191; L2207; L1963
- Evidence: Conversational filler: 'simply stop adding trap tokens' (979); 'Of course,' (1596); 'it simply does not move' (1674, 1676); 'and so-on' (2157); 'one can assume... simply move' (2191); 'it is possible for a demon to smash through multiple pillars' (2207); 'nearly ready to resume' (1963)
- Current text: simply / Of course / and so-on / one can assume / it is possible
- Proposed fix: Delete the filler; state the rule: 'the enemy does not move'; 'A demon may destroy several pillars with one attack.'
- Rationale: Terse voice.
- Gameplay impact: None
- Decision needed: N

### D-016 · dropped-rule · Minor · OPTIONAL
- Location: manuscript.md 1594, 1702 (Push-move, Push-attack)
- Evidence: FAQ p.1: a movement attack 'only targets all characters on each node the enemy moves into' — characters on the enemy's starting node are moved but not damaged. The manuscript moves them first (1594) and then says all pushed characters suffer the damage (1702), leaving the starting node ambiguous.
- Current text: If the push icon includes a number, characters pushed out of the way suffer that amount of damage during the push.
- Proposed fix: Characters moved from the enemy's starting node suffer no damage. Each character on a node the enemy moves onto is pushed and suffers the damage shown; the damage may be blocked or dodged.
- Rationale: Adopts the FAQ ruling the manuscript otherwise follows (1596).
- Gameplay impact: Damage from trampling enemies.
- Decision needed: N

### D-033 · underspecified-deviation · Minor · OPTIONAL
- Location: manuscript.md 843 (Equipment Cards) and 1722 (Block & Resist)
- Evidence: Core p.12 modifiers add or subtract from 'the die roll'. HE p.9 'Choose any two rolled dice' is silent on modifiers. Under the manuscript's two-highest-dice rule it is unstated whether a card's fixed block modifier applies after the two dice are selected.
- Current text: Determine the defence total by adding the number of sword pips on the highest two dice results. Additional dice beyond the two with the highest shown face value are ignored.
- Proposed fix: The defence total is the sum of the two highest dice results plus any fixed modifiers on the equipment used.
- Rationale: Closes a gap created by combining the 1E modifier rule with the HE dice cap.
- Gameplay impact: Minor defence maths.
- Decision needed: Y

### D-039 · underspecified-deviation · Minor · OPTIONAL
- Location: manuscript.md 745, 1690, 1282 (Threat Level)
- Evidence: Core p.11 and V2 p.8 call the character value 'taunt level' and the enemy value 'threat level'. The manuscript uses 'threat' for both, so 'higher threat level' at 1690 (copied from Core p.24 'higher Taunt level') now reads as an enemy statistic.
- Current text: 7. Threat Level … the enemy moves towards the character with the higher threat level.
- Proposed fix: Characters have a taunt level; enemies have a threat level. (Restore 'taunt' at 745, 1003, 1275, 1277, 1289, 1690, 1694, 2192, 3056, 3058.)
- Rationale: Avoids one word meaning two different statistics; optional if the author prefers a single term and defines it.
- Gameplay impact: Clarity of targeting rules.
- Decision needed: Y

### F-071 · prose-crossref · Minor · CLEAN-UP
- Location: L1708 §Enemy Turn › Enemy Attacks
- Evidence: Prose cross-reference: 'More on each defensive option listed below.'
- Current text: More on each defensive option listed below.
- Proposed fix: CUT the fragment; the sub-headings follow. — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: same section. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-072 · prose-crossref · Minor · CLEAN-UP
- Location: L1760 §Enemy Turn › Dodge step 5.2
- Evidence: Prose cross-reference: 'Determine damage to the defending character as above.'
- Current text: Determine damage to the defending character as above.
- Proposed fix: 'as in Block & Resist step 5' (same section) or '(see §9.3, step 5)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §9.3 Block & Resist step 5. Numbering per F_report.md §6 provisional map.
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

### A-124 · inherits-official-silently · Note · CLEAN-UP
- Location: ENEMY TURN › Overview (manuscript.md line 1664); Encounter Turn Order (lines 1281–1295) — turn structure
- Evidence: manuscript.md:1281–1295, 1664, 2025–2027; DS-Core-Rules-lores.txt p.19; Hollowed_Edition_v1.3.txt p.7 ('Enemies always activate first')
- Current text: Each encounter begins with each enemy model taking their turn before proceeding to the character's turns.
- Proposed fix: No change.
- Rationale: The manuscript's round structure (all enemies, then every character in threat order, then aggro reassignment) is complete and internally consistent and differs from both official editions by design. Recorded for the preserve list together with the invader-after-each-character rule.
- Gameplay impact: None.
- Decision needed: N

### C-095 · example · Note · CLEAN-UP
- Location: L1742
- Evidence: Dodge: 'spend two additional stamina (total of three stamina cost)... add a single additional *dodge* die... up to a maximum of four *dodge* dice' - 1 + 2 = 3: consistent.
- Current text: (verified)
- Proposed fix: No change.
- Rationale: Verified.
- Gameplay impact: None
- Decision needed: N

### F-113 · copied-prose · Note · OPTIONAL
- Location: L1664–1666 §Enemy Turn › Overview
- Evidence: Matches official text — close paraphrase (20-word run)
- Current text: …beginning with the highest threat and ending with the model with the lowest threat. For enemies with equal threat levels… / Non-boss enemies follow the behaviour icons on their data cards. Bosses follow the icons on their behaviour cards instead. All behaviour icons are resolved left to right… If there is no valid target or the enemy behaviour otherwise cannot be reasonably executed, that enemy behaviour is skipped…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.24 (also p.27, p.29). Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-114 · copied-prose · Note · OPTIONAL
- Location: L1670–1672 §Enemy Turn › Enemy Movement
- Evidence: Matches official text — verbatim (47%; first three sentences identical)
- Current text: The enemy movement icon shows how an enemy model will move. Various smaller icons can appear around the movement icon, modifying how the enemy moves. This allows different enemies to move towards or away from characters in different patterns and at different speeds.
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.24. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-115 · copied-prose · Note · OPTIONAL
- Location: L1678 §Enemy Turn › Enemy Movement
- Evidence: Matches official text — verbatim (100%)
- Current text: When two different nodes would take an enemy closer to where it is trying to go, the players can choose which node the enemy enters.
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.24. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-116 · copied-prose · Note · OPTIONAL
- Location: L1682–1694 §Enemy Turn › Towards/Away from aggro/nearest
- Evidence: Matches official text — verbatim (L1682/L1686 100%; L1690 92%, 56-word run; L1694 68%)
- Current text: The enemy moves the indicated number of nodes closer to the character with the aggro token. / …farther from the character with the aggro token. / The enemy moves the stated number of nodes closer to the nearest character. If two or more characters are tied for being nearest, the enemy moves towards the character with the aggro token… determine the nearest character at the start of the movement, not at each step.
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.24–25 (repeated p.29–30, p.40). Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-117 · copied-prose · Note · OPTIONAL
- Location: L1698–1702 §Enemy Turn › Push-move / Push-attack
- Evidence: Matches official text — near-verbatim (50%)
- Current text: If the Movement icon includes the push icon, the enemy's movement pushes characters out of its way. / If the push icon includes a number, characters pushed out of the way suffer that amount of damage during the push.
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.24. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

## Completion entries that apply (0) — approved at Gate 1

