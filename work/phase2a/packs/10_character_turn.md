# Drafting pack — chapter 10 (character_turn) — manuscript chapter "CHARACTER TURN"

Source text: `work/phase2a/source/10_character_turn.md` (manuscript.md lines 1798–1883).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 1798.
- **Character Turn Order** · present — TOC mismatch · line 1800. TOC lists Overview / Character Actions / Character Movement; body uses Turn Order / Minor / Major.
- **Recover one stamina.** · present — structural · line 1802. Procedural step rendered as an H3 heading.
- **Minor Actions:** · present — structural · line 1804. Heading with trailing colon; list body in blockquote.
- **Major Action:** · present — structural · line 1820. Heading with trailing colon.
- **Character Movement** · present — to audit · line 1836.
- **(empty heading)** · ORPHAN — delete · line 1842: empty H2 used as page break
- **Character Attacks** · present — to audit · line 1844.
- **Range** · present — to audit · line 1854.
- **Shift** · present — to audit · line 1858.
- **Area-of-Effect (AoE)** · present — TOC mismatch · line 1862. TOC calls it "Node".
- **Shaft** · present — to audit · line 1866.
- **Repeat** · present — to audit · line 1870.
- **Two-Handed Attacks** · present — to audit · line 1874.
- **Stat Scaling** · present — to audit · line 1878.
- **(empty heading)** · ORPHAN — delete · line 1882: empty H1 used as page break

## Audit findings mapped to this chapter (58)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### A-032 · undefined-state · Blocker · REQUIRED
- Location: PLAYER VS PLAYER (manuscript.md lines 3040–3094)
- Evidence: manuscript.md:1485, 1708–1797, 1846–1872, 3060, 3082–3094
- Current text: Character turn structure is unchanged from basic rules. ... Dodge difficulty is based on an the attacker attack option's stamina cost
- Proposed fix: When a character attacks another character, the attacker resolves the attack option as if against an enemy and determines the final attack value. The defender then chooses to block, resist, dodge or parry exactly as against an enemy attack whose attack value equals that final attack value and whose dodge difficulty is given by the stamina-cost table. Damage suffered equals the attack value minus the defence total. Push, condition, shift and area-of-effect icons apply to characters as they apply to enemies; an area-of-effect attack targets every other character on the target node. A parry requires the attacker to share the defender's node; a successful parry staggers the attacker and permits a riposte. Block and resist values of defenders are never subtracted from the attack value; defence is always rolled.
- Rationale: The PvP chapter supplies turn order, traps and a dodge table but never says how a character-versus-character attack is resolved: the enemy-attack procedure assumes a fixed attack value, the character-attack procedure assumes a fixed block value, and neither covers push, AoE, conditions or parry against a character.
- Gameplay impact: PvP cannot be played from the text.
- Decision needed: N

### A-006 · contradiction · Major · REQUIRED
- Location: GAMEPLAY › Embering (manuscript.md line 1229) vs CHARACTERS › Ember (line 805) and CHARACTER TURN › Major Action › Ember (line 1834)
- Evidence: manuscript.md:805, 891, 1227–1233, 1834
- Current text: Ember: Place ember token on dashboard; discard equipped ember card.
- Proposed fix: Ember (major action, or at any time outside an encounter): Discard an ember card from the back-up slot. Remove all damage cubes and all hollow markers from the endurance bar and place an ember token on the dashboard. The character is now embered.
- Rationale: Three passages define embering; only Embering (1229) says it removes all damage cubes. A full heal as a major action is a major tactical resource and must be stated identically everywhere. Alternative: delete 'Remove all damage cubes' at 1229 so that embering only removes hollow markers (Hollowed Edition precedent, p.5).
- Gameplay impact: Groups will disagree on whether embering heals; the difference is up to eight health in combat.
- Decision needed: Y

### A-012 · omission · Major · REQUIRED
- Location: CHARACTERS › Character Tokens (manuscript.md line 793) — Estus Flask absent from body; DOCX footer only
- Evidence: manuscript.md:793, 1830; DOCX footer ('The character may flip their estus flask token to the used side as a major action to remove all damage cubes from their endurance bar. Stamina cubes are not removed.'); DS-Core-Rules-lores.txt p.11
- Current text: There are three different types of character tokens: heroic actions, luck, and estus flask. ... Each character has one of each of the four following tokens
- Proposed fix: Estus Flask: A character may flip their estus flask token to the used side as a major action to remove all damage cubes from their endurance bar. Stamina cubes and hollow markers are not removed. There are four character tokens: heroic action, luck, estus flask and ember.
- Rationale: The only Estus rule lives in the page footer. The body also says 'three types' then 'four following tokens'. The hollow interaction (markers stay) must be explicit because hollow markers occupy endurance spaces.
- Gameplay impact: Without the body text, the Drink Estus major action (1830) has no definition of what 'health' it restores.
- Decision needed: N

### A-024 · undefined-state · Major · REQUIRED
- Location: COMBAT BASICS › Enemy Scaling (manuscript.md line 1529); Character Attacks › Repeat (line 1872); Boss Attacks (line 2187)
- Evidence: manuscript.md:1529, 1579, 1872, 2187; DS-Core-Rules-lores.txt p.40 ('Repeat behaviour or attack' icon exists on official cards)
- Current text: If playing with four characters, add repeat to each non-boss enemy's attack behaviour.
- Proposed fix: When Repeat 2 is added by scaling, each attack icon on the enemy's data card is resolved twice in succession against the same target before the next icon is resolved. The damage value of a push-movement is not an attack icon and is not repeated. If an attack icon already bears a Repeat icon, increase its value by one.
- Rationale: Repeat is defined for weapons (entire option) and bosses (entire card) but not for non-boss enemies, and official data cards already carry Repeat icons. Alternative: Repeat added by scaling does not stack with a printed Repeat icon.
- Gameplay impact: Four-player games double or quadruple some enemy damage output depending on the reading.
- Decision needed: Y

### A-068 · inherits-official-silently · Major · REQUIRED
- Location: ENEMY TURN › Parry & Riposte (manuscript.md lines 1772, 1790); CHARACTER TURN › Major Action › Attack (line 1822); CHARACTERS › Equipment Slots (line 761)
- Evidence: manuscript.md:757–763, 1772, 1790, 1822; DS-Core-Rules-lores.txt p.12 (left-hand and right-hand slots); DS-TG-Rulebook p.8 (hand slots)
- Current text: Characters must be equipped with a shield as their left weapon. ... using any attack option on the weapon equipped to the right weapon slot.
- Proposed fix: Equipment Slots: The two weapon slots are the left-hand slot and the right-hand slot; a one-handed card may be placed in either. Parry: Characters must have a shield equipped in one weapon slot and a weapon with at least one attack option in the other; the riposte uses that weapon.
- Rationale: Left and right slots exist on the official dashboards but the manuscript's Equipment Slots section never names them; the parry rule then depends on which physical slot holds the shield, which is a player choice with no rule attached.
- Gameplay impact: Players cannot tell whether a shield in the right slot permits a parry.
- Decision needed: N

### A-069 · undefined-state · Major · REQUIRED
- Location: SETUP › Shop Setup (manuscript.md line 1069); EQUIPMENT › Equipment Cards (line 811)
- Evidence: manuscript.md:811, 1069, 1079, 1085, 1876
- Current text: 3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells.
- Proposed fix: For stocking the shop: a shield is a weapon-slot card bearing the shield icon; a spell is a card whose art shows a scroll; an upgrade is a card with the weapon-upgrade or armour-upgrade icon, including rings and titanite; every other weapon-slot card, including catalysts and throwable items, is a weapon; an armour card is a card with the armour icon. A shield counts as equipment in the other hand for the two-handed rule.
- Rationale: Five shop categories are used but only armour, weapon and spell are defined; 'shield' and 'item' never are, and catalysts and consumables fall between categories.
- Gameplay impact: Shop stocking is the only treasure source before the first boss.
- Decision needed: Y

### A-073 · undefined-state · Major · REQUIRED
- Location: CHARACTER TURN › Character Turn Order (manuscript.md lines 1800–1834); Character Movement (line 1838)
- Evidence: manuscript.md:1800–1838; DS-Core-Rules-lores.txt p.22 (move before or after attacking, not both); DS-TG-Rulebook p.20 (move then action, or action then move)
- Current text: Minor Actions: Walk AND Run AND Equip AND Heroic Action / Major Action: Attack OR Rest OR Drink Estus OR Ember
- Proposed fix: During their turn a character first recovers one stamina, then may take minor actions before and after their major action in any order. Walk, Equip and Heroic Action may each be taken once per turn; Run may be taken any number of times.
- Rationale: The turn is a list of actions with no sequencing rule; whether a character can walk, attack and then run away is the most common tactical question in the game and is unanswered. Alternative: all movement either before or after the major action, as in both official editions.
- Gameplay impact: Defines hit-and-run tactics for every character turn.
- Decision needed: Y

### A-082 · undefined-state · Major · REQUIRED
- Location: TILES & NODES › Terrain › Gravestones, Barrels, Chests (manuscript.md lines 931, 949, 959); Character Movement (line 1840)
- Evidence: manuscript.md:931, 949, 951, 959, 1670–1678, 1840, 2175; DS-Core-Rules-lores.txt p.17 ('Gravestones block movement')
- Current text: Models cannot walk, run, dodge, or be pushed into nodes containing a gravestone. / Models cannot walk or run into nodes containing barrels. / Models cannot move, dodge, or be pushed into nodes containing a chest.
- Proposed fix: No model, including enemies and bosses, may move, leap, dodge or be pushed into a node containing a gravestone or a chest. No model may walk, run, shift or move into a node containing an intact barrel; a model that dodges or is pushed into such a node destroys the barrel and the token is removed.
- Rationale: Enemy movement is 'move', which is not in the gravestone or barrel lists; whether enemies and leaping bosses are blocked by terrain is unstated.
- Gameplay impact: Enemy pathing around terrain is decided every encounter.
- Decision needed: N

### B-016 · balance · Major · PROPOSED
- Location: L1880 (Stat Scaling)
- Evidence: Threshold = highest requirement + 10. Tier-two weapons (requirement >= 25) need a stat >= 35; the highest Tier Four value is 40 (Core p.33) or Tier Three + 5 (L1914: Herald STR 42, DEX 39, INT 34, FTH 45). Only weapons with requirement <= 30 (STR/FTH) or <= 29 (DEX) can ever scale, and only at Tier Four; tier-one weapons scale at Tier Two-Three (Mace 16 -> STR 26 at Herald Tier Two 28; Rapier 21 -> DEX 31 at Tier Three 34). Uchigatana (32), Falchion (37), Dragon Tooth (40) can never scale.
- Current text: If the character's current stat value exceeds an equipment's highest stat requirement by ten or more points, the character should mark the equipped item with a red damage cube to indicate that it is scaled.
- Proposed fix: "If the character's current stat value exceeds the equipment's highest stat requirement by five or more points, mark the equipped item with a red damage cube to indicate that it is scaled."
- Rationale: A ten-point margin rewards keeping tier-one weapons into the end-game and excludes almost every tier-two weapon; five points lets a Tier Three or Four character scale the weapons the tier-two deck is meant to deliver.
- Gameplay impact: Uchigatana scales at DEX 37 (Tier Four), Carthus Curved Greatsword at DEX 35; tier-one weapons are unchanged in practice (Mace needs STR 21, still first reached at Herald Tier Two 28).
- Decision needed: Y

### C-019 · hedge · Major · REQUIRED
- Location: L765; L793; L979; L1131; L1159; L1201; L1880; L1963; L2065; L2169
- Evidence: 10 'should' in procedural rules, e.g. L1131 'Encounter levels should increase from the tile adjacent to The Bonfire tile'; L2065 'the fog gate tile should be removed... and placed on the bonfire tile'; L1880 'the character should mark the equipped item with a red damage cube'; L765 'players should not interact with their character's inventory cards'
- Current text: should
- Proposed fix: must / imperative: 'Encounter levels must increase from the tile adjacent to the bonfire tile towards the mini-boss tile.' / 'Move the fog gate token from the boss tile's entrance to the bonfire tile.' / 'Mark the equipped card with a red damage cube.' / 'During an encounter a character may not access their inventory.' Full list in C_report.md Task 2.
- Rationale: These are mandatory steps; 'should' makes them optional.
- Gameplay impact: Setup order, fog-gate shortcut, inventory access and scaling marker become mandatory as intended
- Decision needed: N

### C-034 · italics · Major · REQUIRED
- Location: L1830
- Evidence: '*Drink Estus*: Restore all of the character's health; flip *estus flask* face-down.' - 'health' is the enemy/boss term; characters have an endurance bar and damage cubes. The only full Estus rule is the DOCX footer ('remove all damage cubes from their endurance bar. Stamina cubes are not removed').
- Current text: Restore all of the character's health
- Proposed fix: '*Drink Estus*: flip the *estus flask* token to its used side and remove all damage cubes from the endurance bar. Stamina cubes are not removed.'
- Rationale: 'Health' is undefined for characters; the footer wording is the rule.
- Gameplay impact: Clarifies that Estus does not restore stamina
- Decision needed: N

### C-036 · terminology · Major · REQUIRED
- Location: L1285; L1291; L1293; L1850
- Evidence: 'the model with the most damage tokens' (1285); 'the character who placed the most damage tokens on enemy models' (1291, 1293); 'place a number of damage tokens onto the target enemy model's base' (1850) vs 'wound token' (681, 1517, 1664, 2099) and 'damage cubes' for characters (x16)
- Current text: damage tokens
- Proposed fix: wound tokens (enemies); damage cubes (characters)
- Rationale: Two components, two names: enemies take wound tokens (L1517), characters take red damage cubes (L779). 'Damage token' is neither.
- Gameplay impact: Avoids confusion between the two damage-tracking components
- Decision needed: N

### C-038 · terminology · Major · REQUIRED
- Location: L837; L851; L1820; L1838
- Evidence: 'used as a character's main action' (837); 'attached... as a main action' (851) vs heading 'Major Action:' (1820) and 'during an *attack* major action' (1838)
- Current text: main action
- Proposed fix: major action
- Rationale: 'Main action' is never defined; the turn structure defines Minor and Major actions.
- Gameplay impact: Readers cannot find the 'main action' rule
- Decision needed: Y

### C-086 · cross-ref · Major · REQUIRED
- Location: L931; L949; L959; L1840
- Evidence: Terrain rules differ between §Terrain and §Character Movement: Gravestones 'cannot *walk*, *run*, *dodge*, or be pushed' (931); Barrels 'cannot *walk* or *run*' (949) and 'may be pushed or *dodge*' (951); Chests 'cannot move, dodge, or be pushed' (959); Character Movement: 'not permitted to *walk, run,* or *shift* to a node containing a barrel' and 'pushed or *dodge* into a node with a barrel' (1840). *Shift* is never mentioned in §Terrain.
- Current text: (four different verb sets)
- Proposed fix: Define 'move' once as 'walk, run or shift' and use it in every terrain rule: Gravestone/Chest: 'Models may not move, dodge or be pushed into this node.' Barrel: 'Models may not move into this node; a model that dodges or is pushed into it destroys the barrel.' Then L1840 cites §Terrain.
- Rationale: Same rule stated twice with different verb lists.
- Gameplay impact: Whether a character may *shift* onto a gravestone or chest
- Decision needed: N

### C-100 · heading · Major · REQUIRED
- Location: L1802; L1804; L1820; L1806-1834; L1075
- Evidence: Procedural steps set as H3 headings with trailing punctuation: '### Recover one stamina.' (1802), '### Minor Actions:' (1804), '### Major Action:' (1820), with the actions below as blockquotes joined by bold AND/OR; '### After Boss is Defeated:' (1075)
- Current text: ### Recover one stamina. / ### Minor Actions: / ### Major Action:
- Proposed fix: Replace 1802-1834 with one numbered procedure under '## Character Turn Sequence': '1. Recover one stamina. 2. Minor actions (any number, in any order): *walk*, *run*, *equip*, *heroic action*. 3. Major action (one): *attack*, *rest*, *drink estus*, *ember*.' Rename 1075 'Restocking After a Boss is Defeated'.
- Rationale: Headings are labels, never sentences or list items; no trailing punctuation.
- Gameplay impact: None
- Decision needed: N

### D-017 · dropped-rule · Major · REQUIRED
- Location: manuscript.md 1802–1834 (Character Turn Order)
- Evidence: Core p.22: 'a character may move before attacking or after attacking (but not both)'. V2 p.20: move then action or action then move. HE p.9: 'Actions can be done in any order.' The manuscript lists minor actions joined by AND and major actions joined by OR without stating whether minor actions may be taken both before and after the major action.
- Current text: Minor Actions: Walk AND Run AND Equip AND Heroic Action. Major Action: Attack OR Rest OR Drink Estus OR Ember.
- Proposed fix: During a character's turn, minor actions and the major action may be taken in any order; each minor action may be taken once, except run, which may be repeated.
- Rationale: The manuscript's action economy is HE-derived; HE's free ordering is the natural completion, but the 1E restriction is equally coherent and changes hit-and-run tactics, so the author decides.
- Gameplay impact: Whether a character can walk, attack, then run away.
- Decision needed: Y

### D-030 · underspecified-deviation · Major · REQUIRED
- Location: manuscript.md 1772, 1790, 1822 (Parry; Major Action) vs 757–763 (Equipment Slots)
- Evidence: Core p.12 names left-hand and right-hand slots; the manuscript's Equipment Slots section names only 'the weapon slots' but the parry rule requires a shield in the 'left weapon slot' and the riposte uses the 'right weapon slot'.
- Current text: Characters must be equipped with a shield as their left weapon … using any attack option on the weapon equipped to the right weapon slot
- Proposed fix: The two weapon slots are the left-hand slot and the right-hand slot. A card equipped in either slot is in hand.
- Rationale: Parry and riposte cannot be applied without named slots.
- Gameplay impact: Defensive option availability.
- Decision needed: N

### F-016 · tone · Major · OPTIONAL
- Location: L1868 §Character Turn › Shaft
- Evidence: Flavour sentence embedded in a rule (official Core p.23 voice): 'Bows, polearms, and other unwieldy weapons are difficult to use effectively at short range.'
- Current text: Bows, polearms, and other unwieldy weapons are difficult to use effectively at short range. Weapons with the *shaft* icon cannot target enemy models on the character's node.
- Proposed fix: CUT first sentence. Keep: 'An attack option with the *shaft* icon cannot target a model on the attacker's node.'
- Rationale: Flavour is permitted only in chapter intros.
- Gameplay impact: none
- Decision needed: N

### F-017 · tone · Major · OPTIONAL
- Location: L1872 §Character Turn › Repeat
- Evidence: Flavour sentence embedded in a rule: 'This represents a rapid flurry of attacks such as from an agile sword or a repeating crossbow.'
- Current text: The *repeat* icon allows the character to use that entire weapon option the number of times indicated in the circle. This represents a rapid flurry of attacks…
- Proposed fix: CUT second sentence. Keep: 'An attack option with the *repeat* icon is resolved in full the number of times shown.'
- Rationale: Flavour is permitted only in chapter intros.
- Gameplay impact: none
- Decision needed: N

### F-018 · tone · Major · CLEAN-UP
- Location: L1876 §Character Turn › Two-Handed Attacks
- Evidence: Tone slip: 'Characters equipped with a two-handed weapon are decidedly on the offensive.'
- Current text: Characters equipped with a two-handed weapon are decidedly on the offensive. Attack actions with two-handed weapons may reroll any single die after rolling to attack. Additionally, if a character equips a one-handed weapon without equipment to their other hand, that weapon is considered to be wielded as two-handed…
- Proposed fix: CUT first sentence. REWRITE rest: 'When a character attacks with a two-handed weapon, they may reroll one die after rolling. A one-handed weapon equipped with the other weapon slot empty is wielded two-handed and gains the same reroll.'
- Rationale: Editorialising opener; the rule follows.
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

### A-010 · procedural · Minor · REQUIRED
- Location: COMBAT BASICS › Conditions › Frostbite (manuscript.md line 1626) vs CHARACTER TURN › Recover one stamina (line 1802), Rest (line 1826), Encounter Recovery (lines 1349–1351)
- Evidence: manuscript.md:1626, 1630, 1802, 1826, 1349–1351; DS-TG-Rulebook p.21 (frostbitten characters recover one less stamina)
- Current text: Frostbite affected characters cannot recover stamina.
- Proposed fix: A frostbitten character does not recover stamina at the start of their turn and may not take the Rest major action. At the end of an encounter, condition tokens are removed before stamina cubes are removed.
- Rationale: The mandatory 'Recover one stamina' step and the Rest action are both stamina recovery; the text must say that both are blocked. Encounter Recovery lists stamina removal before condition removal, so a frostbitten survivor is blocked from the end-of-encounter recovery by the literal order.
- Gameplay impact: Clarifies a condition that otherwise silently disables a whole turn step.
- Decision needed: N

### A-011 · undefined-state · Minor · REQUIRED
- Location: CHARACTER TURN › Major Action › Rest (manuscript.md line 1826)
- Evidence: manuscript.md:1806–1826, 1838
- Current text: Rest: Restore all of the character's stamina, if no run action was taken this turn.
- Proposed fix: Rest: Remove all stamina cubes from the endurance bar. A character who rests may not run during the same turn, before or after resting. Walk, Equip and Heroic Action remain available.
- Rationale: The condition 'taken this turn' only forbids running before the Rest; a character resting first and then running to full stamina would exploit the ordering.
- Gameplay impact: Prevents a free full-stamina sprint every other turn.
- Decision needed: N

### A-037 · undefined-state · Minor · OPTIONAL
- Location: BOSS ENCOUNTERS › Attacking Bosses and Weak Arcs (manuscript.md line 2149)
- Evidence: manuscript.md:1864, 1872, 2149–2151
- Current text: If the character is attacking a weak arc, the attack gains an additional black die.
- Proposed fix: The additional black die is rolled for each attack roll made against a weak arc, including each repetition of a Repeat attack and each riposte.
- Rationale: A Repeat option is 'that entire weapon option' used several times; whether each roll gains the die is unstated.
- Gameplay impact: Small but constant in boss fights with Repeat weapons.
- Decision needed: N

### A-064 · terminology · Minor · CLEAN-UP
- Location: CAMPAIGN PLAY › Bonfire Ascetic (manuscript.md line 2342)
- Evidence: manuscript.md:1519, 1878, 2342
- Current text: This effect is cumulative with stat scaling for character count.
- Proposed fix: This effect is cumulative with enemy scaling for character count.
- Rationale: 'Stat scaling' is the weapon rule at line 1878; the intended cross-reference is Enemy Scaling.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-066 · undefined-state · Minor · OPTIONAL
- Location: CHARACTER TURN › Stat Scaling (manuscript.md line 1880)
- Evidence: manuscript.md:1880, 3212–3330 (several weapons with 0/0/0/0 or single requirements)
- Current text: If the character's current stat value exceeds an equipment's highest stat requirement by ten or more points, the character should mark the equipped item...
- Proposed fix: Equipment whose highest stat requirement is zero cannot be scaled.
- Rationale: A card with no requirement has a 'highest requirement' of zero, so every starting character scales it at once. Alternative: allow it (treat zero as a requirement).
- Gameplay impact: Affects throwables and a few low-end weapons.
- Decision needed: Y

### A-070 · undefined-state · Minor · OPTIONAL
- Location: EQUIPMENT › Spells (manuscript.md lines 877–887); Character Attacks (line 1846)
- Evidence: manuscript.md:861, 877–887, 1712, 1846
- Current text: Spells stored within their respective catalyst may use their attack options as if equipped.
- Proposed fix: A stored spell provides only its attack options; its block, resist and dodge values are ignored. Using a stored spell's attack option counts as the catalyst's one attack for that turn.
- Rationale: Block and Resist gather dice from 'equipped' cards; 'as if equipped' invites counting stored spells' defence values and a second attack from the same slot.
- Gameplay impact: Prevents a catalyst with three stored spells becoming a multi-attack slot.
- Decision needed: N

### A-072 · undefined-state · Minor · OPTIONAL
- Location: CHARACTER TURN › Minor Actions › Equip (manuscript.md line 1814)
- Evidence: manuscript.md:763, 1806–1818; DS-Core-Rules-lores.txt p.22 (swap only between backup and hand slots)
- Current text: Equip: Swap equipment cards between the back-up slot, weapon slots, and armour slots on the character dashboard. Inventory is unavailable.
- Proposed fix: Equip may be taken once per turn and exchanges any number of cards among the back-up, weapon and armour slots.
- Rationale: Each minor action is listed with 'AND' but no frequency; Run is explicitly repeatable, the others are not addressed. Armour swapping mid-encounter is a deliberate extension of the official rule and is kept. Alternative: Equip may be taken any number of times.
- Gameplay impact: Stops repeated swap-attack-swap sequences within one turn.
- Decision needed: Y

### A-086 · undefined-state · Minor · OPTIONAL
- Location: TILES & NODES › Node Model Limits (manuscript.md line 919); Character Movement (line 1840)
- Evidence: manuscript.md:919, 1840
- Current text: the players must push one of the three models already on the node.
- Proposed fix: A model pushed to make room moves to any valid adjacent node chosen by the players.
- Rationale: Direction and validity of the overcrowding push are unstated.
- Gameplay impact: Cosmetic.
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

### A-119 · undefined-state · Minor · OPTIONAL
- Location: ENEMY TURN › Parry & Riposte step 5.4 (manuscript.md line 1790)
- Evidence: manuscript.md:1790, 1846, 1876, 2149
- Current text: The character may make one riposte attack out of turn against the attacker using any attack option on the weapon equipped to the right weapon slot after paying the associated stamina cost.
- Proposed fix: A riposte is an attack for all purposes (two-handed reroll, luck, weak-arc die, conditions) except that it does not count towards the limit of one attack per weapon per turn.
- Rationale: Nothing says whether the riposte consumes the weapon's attack for the character's next turn or benefits from attack modifiers.
- Gameplay impact: Arises on every successful parry.
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

### C-028 · italics · Minor · REQUIRED
- Location: L787; L1341; L1794; L1880; L2145; L3082
- Evidence: Split or partial italics: 'stagger*ed*' x2 (787); '*C*haracters' (1341); 'block*/*resist' (1794); 'attack option*s*' (1880); 'dodge*s*' (2145); 'attack option*'s*' (3082)
- Current text: stagger*ed*
- Proposed fix: *staggered*; Characters; *block*/*resist*; *attack options*; *dodges*; *attack option*'s
- Rationale: Italicise the whole inflected word or none.
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

### C-039 · terminology · Minor · REQUIRED
- Location: L1606; L1618; L1860; L2191
- Evidence: 'not removed at the end of activations' (1606); 'at the end of its activation' (1618); 'during their activation' (1860); 'prior to the boss's activation' (2191) vs 'turn' x65 incl. L1600 'When a model ends its turn'
- Current text: activation
- Proposed fix: turn
- Rationale: One word for one concept; 'turn' is the manuscript's dominant and defined term (L1279-1295, L1800).
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

### C-055 · terminology · Minor · REQUIRED
- Location: L1872; L1856; L1876; L1838
- Evidence: 'use that entire weapon option' (1872); 'for that attack action' (1856); 'Attack actions with two-handed weapons' (1876) vs '*attack option*' x15 and 'the *attack* major action' (1838)
- Current text: weapon option / attack action
- Proposed fix: *attack option* for a line on a card; 'attack' (the major action) for the action; 'during an *attack*' not 'attack action'
- Rationale: One name for the card line; the action is simply 'attack'.
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

### C-117 · punctuation · Minor · CLEAN-UP
- Location: L875; L3154; L1806-1834
- Evidence: Pandoc list-separator comments '<!-- -->' (875, 3154) and blockquote '>' markup used for the turn-structure list (1806-1834)
- Current text: <!-- --> / > *Walk*: ...
- Proposed fix: Delete the comments; replace blockquotes with the numbered procedure proposed in the heading row.
- Rationale: Conversion artefacts.
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

### F-073 · prose-crossref · Minor · CLEAN-UP
- Location: L1852 §Character Turn › Character Attacks
- Evidence: Prose cross-reference: 'the magical damage icon explained above, the conditions explained prev…'
- Current text: the magical damage icon explained above, the conditions explained previously, and the following weapon icons
- Proposed fix: 'the magical damage icon (above), conditions (see §8.5), and the following icons' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §10.3 (same section); §8.5 Conditions. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-084 · register-shift · Minor · CLEAN-UP
- Location: L1800–1834 §Character Turn › Character Turn Order
- Evidence: Unique format: blockquoted fragments joined by bold 'AND'/'OR' connectors under sub-headings 'Recover one stamina.' / 'Minor Actions:' / 'Major Action:'
- Current text: > *Walk*: Move character model to an adjacent node. > **AND** > *Run*: Move one additional node per stamina spent. …
- Proposed fix: REWRITE as a numbered procedure: '1. Recover one stamina. 2. Minor actions, in any order and any number of times unless stated: *Walk*…; *Run*…; *Equip*…; *Heroic Action* (once). 3. One major action: *Attack*, *Rest*, *Drink Estus* or *Ember*.'
- Rationale: The AND/OR connectors are a diagram convention, not prose; every other chapter uses numbered steps or bullets.
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

### F-118 · copied-prose · Note · OPTIONAL
- Location: L1838, L1846 §Character Turn › Movement / Attacks
- Evidence: Matches official text — loose paraphrase (8–10-word runs only)
- Current text: Characters have four methods of moving from node to node… / During the character's turn they may make up to one attack with each weapon or spell equipped…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.22. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-119 · copied-prose · Note · OPTIONAL
- Location: L1852–1856 §Character Turn › Character Attacks / Range
- Evidence: Matches official text — verbatim (L1852 74%, 28-word run)
- Current text: Though many weapons simply deal damage, some have special abilities explained in text on their cards or with icons. This includes the magical damage icon explained above, the conditions explained previously, and the following weapon icons. / Some attack options specify a range that is different from the weapon's default range…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.23. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-120 · copied-prose · Note · OPTIONAL
- Location: L1860 §Character Turn › Shift
- Evidence: Matches official text — verbatim (93%, 63-word run)
- Current text: When a character makes an attack with the shift icon, they may move up to the number of nodes shown. Shift icons that appear before the dice icons allow a character to move before rolling the dice. Those that appear after the dice allow the character to move after rolling the dice…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.23 (also Phantoms p.9, V2 p.22). Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-121 · copied-prose · Note · OPTIONAL
- Location: L1864 §Character Turn › Area-of-Effect
- Evidence: Matches official text — near-verbatim (49%, 16-word run)
- Current text: Attacks with the AoE icon can target all enemies on a single node within range instead of targeting just one enemy. Make the attack roll once, and compare it to the block or resist value of each enemy…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.23. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-122 · copied-prose · Note · OPTIONAL
- Location: L1868–1872 §Character Turn › Shaft / Repeat
- Evidence: Matches official text — close paraphrase (12-word run; 'polearms' flavour is Core's)
- Current text: Bows, polearms, and other unwieldy weapons are difficult to use effectively at short range… / The repeat icon allows the character to use that entire weapon option the number of times indicated in the circle…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.23. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

## Completion entries that apply (1) — approved at Gate 1

### [CMP-0001] Characters › Character Tokens › Estus Flask — Proposed Completion
- Read `04_completion_backlog.md` lines 8–35 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

