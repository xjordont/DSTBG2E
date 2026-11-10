# Drafting pack — chapter 08 (combat_basics) — manuscript chapter "COMBAT BASICS"

Source text: `work/phase2a/source/08_combat_basics.md` (manuscript.md lines 1481–1659).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 1481.
- **Target versus Hit** · present — to audit · line 1483.
- **Enemy Data Cards** · present — to audit · line 1489.
- **Enemy Scaling** · present — to audit · line 1519.
- **Pushing** · present — to audit · line 1586.
- **Conditions** · present — to audit · line 1598.
- **Bleed** · present — to audit · line 1602.
- **Poison** · present — to audit · line 1614.
- **Frostbite** · present — to audit · line 1622.
- **Stagger** · present — to audit · line 1632.
- **Calamity (Kalameet Expansion)** · present — to audit · line 1640.
- **Corrosion (Gaping Dragon Expansion)** · present — to audit · line 1650.

## Audit findings mapped to this chapter (60)

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

### B-003 · scaling · Blocker · REQUIRED
- Location: L1529 and table row 4 (L1556-1559) (Enemy Scaling)
- Evidence: Hollow Soldier (Core p.20: attack 4). At 4 characters: attack 5 with Repeat 2. Expected damage per activation vs 2 black block dice (best two) = 2 x 2.67 = 5.33 of an 8-box bar; P(kill full-health character in one activation) = 0.058; P(kill hollow character) = 0.444. At 1-2 characters the same enemy deals 1.67. Official 1E (Core pp.17-25) and V2 (p.16, player-count symbol = extra models) never add attack value or Repeat.
- Current text: If playing with four characters, add *repeat to* each non-boss enemy's attack behaviour. [table: 4 | Base + 3 | 1 -> 2 | +1 | Repeat 2]
- Proposed fix: Delete the Repeat row. Replace with: "If playing with four characters, increase each non-boss enemy's base health by one further point (Base + 4)." Table row 4: "4 | Base + 4 | 1 -> 2 | +1 | -".
- Rationale: Repeat doubles damage on top of the +1; with the two-highest-dice block cap no build can absorb it. A health step keeps the 4-player encounter longer without making single activations lethal.
- Gameplay impact: 4-player expected damage per Hollow Soldier activation falls from 5.33 to 2.67; one-activation kill chance on a full bar falls from 5.8% to 0%.
- Decision needed: Y

### B-031 · scaling · Blocker · REQUIRED
- Location: L2342-2344 (Bonfire Ascetic) with L1527-1529 (Enemy Scaling)
- Evidence: 'This effect is cumulative with stat scaling for character count.' Hollow Soldier (Core p.20, attack 4) in a 4-character campaign after the Ascetic: attack 6 with Repeat 2. Expected damage per activation vs 2 black block dice = 2 x 3.67 = 7.33 of an 8-box bar; P(kill a full-health character in one activation) = 0.444; P(kill a hollow character) = 0.914. An icon-key 5-attack enemy (Core p.25) becomes 7 x2 = 9.33 expected, lethal to a full bar on average. At 3 characters: attack 6, 3.67 per activation.
- Current text: After the bonfire ascetic has been burnt, all non-boss enemies increase their attack damage by one for the remainder of the campaign. This effect is cumulative with stat scaling for character count.
- Proposed fix: "After the bonfire ascetic has been burnt, all non-boss enemies increase their base health by two for the remainder of the campaign. This increase is cumulative with the health scaling for character count. Enemy attack values are not changed."
- Rationale: A second +1 attack on top of player-count scaling pushes every ordinary enemy past what the two-highest-dice block cap can absorb; a health increase lengthens fights without making single activations lethal and matches the 'stronger enemies' flavour.
- Gameplay impact: 4-player post-Ascetic Hollow Soldier: health 6 instead of 4, expected damage per activation 2.67 (if B-003 is adopted) instead of 7.33.
- Decision needed: Y

### D-008 · dropped-rule · Blocker · REQUIRED
- Location: manuscript.md 1706 (Enemy Attacks), 1485 (Target versus Hit)
- Evidence: Core p.25 defines enemy attack targeting: skull icon = character with the aggro token, ring icon = nearest character (ties → aggro, then higher taunt); an attack whose target is out of range misses; the Node icon attacks every character on the target's node, each rolling separately. V2 p.25 repeats this. The manuscript explains these icons only for movement (1672–1694) and says attack modifiers are 'detailed later', but no such section exists.
- Current text: Additional symbols beside the attack type icon modify the attack with special rules detailed later.
- Proposed fix: An attack with the skull icon targets the character with the aggro token. An attack with the ring icon targets the nearest character; if two or more characters are tied for nearest, the attack targets the one with the aggro token, and otherwise the tied character with the higher threat level. If the target is not within the attack's range, the attack misses and has no effect. An attack with the node icon targets every character on the target's node; each defends separately.
- Rationale: Silently dropped from Core p.25 while the movement half of the same page was copied; without it an enemy turn cannot be resolved.
- Gameplay impact: Every enemy attack.
- Decision needed: N

### A-024 · undefined-state · Major · REQUIRED
- Location: COMBAT BASICS › Enemy Scaling (manuscript.md line 1529); Character Attacks › Repeat (line 1872); Boss Attacks (line 2187)
- Evidence: manuscript.md:1529, 1579, 1872, 2187; DS-Core-Rules-lores.txt p.40 ('Repeat behaviour or attack' icon exists on official cards)
- Current text: If playing with four characters, add repeat to each non-boss enemy's attack behaviour.
- Proposed fix: When Repeat 2 is added by scaling, each attack icon on the enemy's data card is resolved twice in succession against the same target before the next icon is resolved. The damage value of a push-movement is not an attack icon and is not repeated. If an attack icon already bears a Repeat icon, increase its value by one.
- Rationale: Repeat is defined for weapons (entire option) and bosses (entire card) but not for non-boss enemies, and official data cards already carry Repeat icons. Alternative: Repeat added by scaling does not stack with a printed Repeat icon.
- Gameplay impact: Four-player games double or quadruple some enemy damage output depending on the reading.
- Decision needed: Y

### A-028 · undefined-state · Major · REQUIRED
- Location: SUMMONS › Invader Encounter Setup step 3 (manuscript.md line 2019); CRYSTAL LIZARDS (line 2055); Enemy Scaling (line 1521)
- Evidence: manuscript.md:1521–1529, 2019, 2055, 2342; DS-Phantoms-Rules-lores.txt p.12; DS-IronKeep-Rules-Web.txt p.5
- Current text: Invaders do not multiply their health by the number of characters like other enemy models.
- Proposed fix: Invaders and crystal lizards are never modified by enemy scaling or by the bonfire ascetic.
- Rationale: Both exemptions cover health only; invaders are 'non-boss enemies' and would otherwise gain +1 attack and Repeat 2, and crystal lizards would gain movement 1→2, which defeats the chase. The bonfire ascetic (2342) already exempts invaders from +1 attack, which shows the intent. Alternative: invaders receive attack scaling but not health scaling.
- Gameplay impact: A Repeat-2 invader with +1 attack acting after every character turn is lethal at four players.
- Decision needed: Y

### A-078 · procedural · Major · REQUIRED
- Location: COMBAT BASICS › Conditions (manuscript.md line 1600); Stagger (line 1638); Parry & Riposte (line 1788)
- Evidence: manuscript.md:1600, 1638, 1664, 1788, 1796; DS-Core-Rules-lores.txt p.21; DS-TG-Rulebook p.21
- Current text: When a model ends its turn, remove one poison token and any frostbite/stagger tokens.
- Proposed fix: A stagger or frostbite token is removed at the end of the affected model's next complete turn. A token placed on a model during that model's own turn remains until the end of the model's following turn.
- Rationale: A successful parry staggers the attacking enemy during that enemy's own turn; the token is then removed at the end of the same turn, before any character attacks, so the parry's stagger has no effect unless the enemy has further attack icons. Alternative: keep the end-of-own-turn removal and state that the parry stagger applies to the remainder of the enemy's current turn only.
- Gameplay impact: The parry reward is largely void under the literal text.
- Decision needed: Y

### A-115 · omission · Major · PROPOSED
- Location: BOSS SPECIAL RULES (manuscript.md lines 2199–2213); Setup After the main-boss step 11 (line 1195)
- Evidence: manuscript.md:1195, 1640, 2199–2213; DS-BDK-Rules-web.txt p.12–13 (Strafe cards, Signature cards, Calamity); DS-EC-Rules-Web.txt p.12–15 (track deck, No Starting Health, Death Race, Central Wall, Chariot Crash)
- Current text: The characters now begin combat with the mega-boss employing any special rules described in the mega-boss rule booklet.
- Proposed fix: Replace the external reference with sections under Boss Special Rules for each supported mega-boss. For the supplied booklets: Black Dragon Kalameet (Signature cards always in the deck; Strafe deck; Strafe attack targets the nodes shown and lands the boss on the landing node, pushing characters there to any adjacent node; Calamity condition). Executioner's Chariot (track behaviour deck resolved in numbered order; the boss has no health until every other enemy is slain; track attacks target the nodes shown and push hit characters to untargeted adjacent nodes; the board centre is treated as a gravestone node; on heat-up remove the chariot, flip the data card and switch to the heat-up deck).
- Rationale: The manuscript's own goal (line 375) is a rulebook that needs no other text, yet nine mega-bosses are listed and only the Asylum/Stray Demon is covered. The Calamity condition (1640) is defined but the Strafe mechanic that delivers it is not.
- Gameplay impact: Mega-boss games are unplayable from the manuscript alone.
- Decision needed: N

### B-002 · balance · Major · PROPOSED
- Location: L1722 (Enemy Attacks > Block & Resist, step 4)
- Evidence: Defence total = two highest dice. With black dice the ceiling is 4 (2+2); mean of 2 black = 2.33, best-two-of-3 black = 2.88, best-two-of-4 black = 3.19. Official 1E (Core p.25) sums all dice (3 black mean 3.50). Combined with the Enemy Scaling table (L1519) this caps what any block build can absorb.
- Current text: Determine the defence total by adding the number of sword pips on the highest two dice results. Additional dice beyond the two with the highest shown face value are ignored.
- Proposed fix: Keep the rule but state the consequence in the Enemy Scaling section (see B-003/B-004) or raise the cap: "Determine the defence total by adding the number of sword pips on the highest two dice results. A shield adds its block dice to the pool and, if the character has a shield equipped, the three highest dice are used instead."
- Rationale: Hollowed Edition p.7 introduced the two-dice cap to tame armour stacking, but it was paired with unscaled enemy attack values. The manuscript adds +1 attack at 3 players and Repeat at 4 players against the same cap, so damage leaks through on every hit at 3-4 players.
- Gameplay impact: At 4 players a scaled Hollow Soldier (attack 5, Repeat 2) deals an expected 5.3 damage per activation to a 2-black-die blocker (see §2).
- Decision needed: Y

### B-004 · scaling · Major · PROPOSED
- Location: L1527 and table row 3 (Enemy Scaling)
- Evidence: +1 attack at 3 characters raises Hollow Soldier expected damage from 1.67 to 2.67 (+60%) and removes the zero-damage block outcome (P(0) 0.111 -> 0). The health step (+1) is a +33% change at the same player count. Three characters also absorb three times the enemy activations of one character because all enemies act between every character turn (L1297-1311).
- Current text: If playing with three or more characters, increase all non-boss attack values by one. [table: 3 | Base + 2 | 1 -> 2 | +1 | -]
- Proposed fix: "If playing with four characters, increase all non-boss enemy attack values by one." Table: row 3 "3 | Base + 2 | 1 -> 2 | - | -"; row 4 "4 | Base + 3 | 1 -> 2 | +1 | -".
- Rationale: Moves the attack step to the player count where the party has the most defensive redundancy and keeps each step of the table roughly equal in expected-damage terms.
- Gameplay impact: 3-player encounters return to 1-2 player per-hit lethality while keeping +2 health per enemy.
- Decision needed: Y

### B-025 · balance · Major · REQUIRED
- Location: L1616-1620 (Conditions > Poison)
- Evidence: Each poison token deals 1 damage at end of activation and only one token is removed, so n tokens inflict n + (n-1) + ... + 1 damage: 2 tokens = 3, 3 tokens = 6, 4 tokens = 10 (more than a full 8-box bar). Official 1E/V2: 1 damage per activation (V2 discards the token). Hollowed p.8 consumes all tokens at once for n damage.
- Current text: *Poison* tokens are not limited to one per model. A model suffers one damage for each *poison* token it has at the end of its activation, then removes only one *poison* token.
- Proposed fix: "Poison tokens are not limited to one per model. At the end of its activation a model suffers one damage for each poison token it has, then removes all of its poison tokens."
- Rationale: Adopts the Hollowed Edition value the manuscript otherwise follows; stacking remains meaningful (n tokens = n damage) without triangular growth.
- Gameplay impact: Three poison hits deal 3 damage instead of 6.
- Decision needed: Y

### C-036 · terminology · Major · REQUIRED
- Location: L1285; L1291; L1293; L1850
- Evidence: 'the model with the most damage tokens' (1285); 'the character who placed the most damage tokens on enemy models' (1291, 1293); 'place a number of damage tokens onto the target enemy model's base' (1850) vs 'wound token' (681, 1517, 1664, 2099) and 'damage cubes' for characters (x16)
- Current text: damage tokens
- Proposed fix: wound tokens (enemies); damage cubes (characters)
- Rationale: Two components, two names: enemies take wound tokens (L1517), characters take red damage cubes (L779). 'Damage token' is neither.
- Gameplay impact: Avoids confusion between the two damage-tracking components
- Decision needed: N

### C-066 · table-text · Major · REQUIRED
- Location: L1517; L1523; L1555-1578
- Evidence: L1517 'When playing with more than one character, calculate a scaled health value by adding one health for each character (including dead characters) in play' (2 characters -> Base+2) vs L1523 'Increase each non-boss enemy's base health by the number of characters... beyond one' and table (2 -> Base+1, 3 -> Base+2, 4 -> Base+3)
- Current text: adding one health for each character (including dead characters) in play
- Proposed fix: 'adding one health for each character (including dead characters) beyond the first'
- Rationale: Prose contradicts the bullet and table; the table is the intended rule.
- Gameplay impact: Enemy health off by one in every multiplayer game if L1517 is followed
- Decision needed: N

### C-067 · table-text · Major · REQUIRED
- Location: L1529; L1550-1551; L1579; L1527; L1548-1549
- Evidence: Bullet L1529 'If playing with four characters, add *repeat to* each non-boss enemy's attack behaviour' (no value) vs table L1579 '*Repeat* 2'; bullet L1527 'increase all non-boss attack values by one' vs table column 'Enemy Damage +1'
- Current text: add *repeat to* each non-boss enemy's attack behaviour; Enemy Damage
- Proposed fix: 'add *repeat* 2 to each non-boss enemy attack'; column header 'Enemy Attack Value'
- Rationale: Bullets and table must state the same value with the same term.
- Gameplay impact: Four-player enemies attack once or twice depending on which is read
- Decision needed: N

### C-119 · voice · Major · REQUIRED
- Location: L1205-1253; L1299-1399; L1445-1479; L1935-1949; L859-887; L931-981; L1604-1658; L2243-2293; L2314-2322; L3040-3094
- Evidence: Rules stated as bullet fragments: Death & Hollowing, Embering, Sparks (1205-1253); Encounter Resolution/Recovery, Souls (1299-1399); Treasure Rewards (1445-1479); Shop Rules (1935-1949); Spells (859-887); Terrain (931-981); Conditions (1604-1658); campaign Soul/Treasure Rewards and Shop (2243-2322); the whole PLAYER VS PLAYER chapter (3040-3094) is 27 bullets with no sentence structure
- Current text: - Encounters are *failed* if either all characters die.
- Proposed fix: Policy: PROCEDURES (setup, turn sequence, defence rolls, encounter start, resting, transposition) = numbered steps; DEFINITIONS and component anatomies (dashboard parts, data-card fields, condition effects, terrain) = bulleted lists of complete sentences; RULES (everything else) = short declarative paragraphs in 'When [trigger], [subject] must/may [action].' form. Rewrite PvP as prose plus a dodge table.
- Rationale: Fragments omit the trigger and subject that lawbook syntax requires ('Encounters are failed if either all characters die' has a dangling 'either').
- Gameplay impact: None
- Decision needed: Y

### F-015 · tone · Major · CLEAN-UP
- Location: L1596 §Combat Basics › Pushing ¶4
- Evidence: Reader address and conversational connectives: 'Players should take note that…', 'Therefore…', 'Of course, characters who block or resist…'
- Current text: Players should take note that only enemy behaviours that deal damage can be dodged. Therefore, only enemy behaviours with an associated attack value can be dodged to permit the character to avoid the associated push effect. Of course, characters who block or resist a push behaviour are pushed regardless of damage dealt.
- Proposed fix: REWRITE-IN-VOICE: 'A character may dodge a push effect only if the behaviour has an attack value. A character who blocks or resists a push attack is pushed whether or not damage is dealt.'
- Rationale: Two rules, two sentences; no address to the reader.
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

### A-010 · procedural · Minor · REQUIRED
- Location: COMBAT BASICS › Conditions › Frostbite (manuscript.md line 1626) vs CHARACTER TURN › Recover one stamina (line 1802), Rest (line 1826), Encounter Recovery (lines 1349–1351)
- Evidence: manuscript.md:1626, 1630, 1802, 1826, 1349–1351; DS-TG-Rulebook p.21 (frostbitten characters recover one less stamina)
- Current text: Frostbite affected characters cannot recover stamina.
- Proposed fix: A frostbitten character does not recover stamina at the start of their turn and may not take the Rest major action. At the end of an encounter, condition tokens are removed before stamina cubes are removed.
- Rationale: The mandatory 'Recover one stamina' step and the Rest action are both stamina recovery; the text must say that both are blocked. Encounter Recovery lists stamina removal before condition removal, so a frostbitten survivor is blocked from the end-of-encounter recovery by the literal order.
- Gameplay impact: Clarifies a condition that otherwise silently disables a whole turn step.
- Decision needed: N

### A-025 · undefined-state · Minor · OPTIONAL
- Location: COMBAT BASICS › Enemy Scaling (manuscript.md line 1527); CAMPAIGN PLAY › Bonfire Ascetic (line 2342)
- Evidence: manuscript.md:1527, 1594, 1702, 2342
- Current text: If playing with three or more characters, increase all non-boss attack values by one.
- Proposed fix: Attack value increases from scaling and from the bonfire ascetic apply to every attack icon and to the damage value of push-movements.
- Rationale: Push-movement damage (1702) is a number inside a movement icon, not an 'attack value'; the scaling text does not say whether it is increased. Alternative: push-movement damage is never modified.
- Gameplay impact: Trampling enemies (Sentinel, Smelter-type) are the ones where the +1 matters most.
- Decision needed: Y

### A-026 · arithmetic · Minor · REQUIRED
- Location: COMBAT BASICS › Enemy Data Cards (manuscript.md line 1517) vs Enemy Scaling (line 1523 and table at 1533–1584)
- Evidence: manuscript.md:1517, 1523, 1562–1576
- Current text: When playing with more than one character, calculate a scaled health value by adding one health for each character (including dead characters) in play.
- Proposed fix: When playing with more than one character, add one health for each character in play beyond the first (including dead characters).
- Rationale: Literal reading of 1517 gives Base+2 for two characters; the table and line 1523 give Base+1.
- Gameplay impact: Off-by-one on every enemy's health in multiplayer.
- Decision needed: N

### A-027 · undefined-state · Minor · OPTIONAL
- Location: CAMPAIGN PLAY › Adding & Dropping Players (manuscript.md line 2239) vs Enemy Scaling (line 1523)
- Evidence: manuscript.md:1523, 2239; DS-Core-Rules-lores.txt p.33
- Current text: If a player character leaves the characters, the characters gain one spark, the character's equipment is added to the inventory, and the maximum number of sparks is changed...
- Proposed fix: A character who has left the campaign is not counted for enemy scaling, per-character rewards, shop ember cards or the spark maximum from the moment the player leaves. A new character is counted from the moment the player joins.
- Rationale: Scaling counts 'dead characters' but nothing addresses departed ones; per-character treasure already dealt to tiles also changes count.
- Gameplay impact: Prevents a dropped player inflating enemy health for the rest of the section.
- Decision needed: N

### A-029 · terminology · Minor · CLEAN-UP
- Location: SUMMONS › Invader Encounter Setup step 3 (manuscript.md line 2019)
- Evidence: manuscript.md:1523, 2019
- Current text: Invaders do not multiply their health by the number of characters like other enemy models.
- Proposed fix: Invaders do not increase their health for the number of characters.
- Rationale: Enemy scaling adds, it does not multiply.
- Gameplay impact: Cosmetic; avoids a reader inferring a multiplicative rule.
- Decision needed: N

### A-064 · terminology · Minor · CLEAN-UP
- Location: CAMPAIGN PLAY › Bonfire Ascetic (manuscript.md line 2342)
- Evidence: manuscript.md:1519, 1878, 2342
- Current text: This effect is cumulative with stat scaling for character count.
- Proposed fix: This effect is cumulative with enemy scaling for character count.
- Rationale: 'Stat scaling' is the weapon rule at line 1878; the intended cross-reference is Enemy Scaling.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-079 · undefined-state · Minor · REQUIRED
- Location: COMBAT BASICS › Conditions › Stagger (manuscript.md line 1636)
- Evidence: manuscript.md:1636, 1515, 1708; DS-Core-Rules-lores.txt p.21 (enemy stagger: attack damage −1)
- Current text: Staggered models subtract one from attack, block, resist, and dodge.
- Proposed fix: A staggered enemy reduces its attack value and its dodge difficulty by one, and its block and resist values by one. A staggered character subtracts one from the result of each attack, block, resist and dodge roll.
- Rationale: Enemies have fixed values and a dodge difficulty rather than rolls; the single sentence has to be read two ways.
- Gameplay impact: Affects every parry and every stagger weapon.
- Decision needed: N

### A-080 · terminology · Minor · CLEAN-UP
- Location: COMBAT BASICS › Conditions › Corrosion and Calamity (manuscript.md lines 1640–1658)
- Evidence: manuscript.md:1644–1648, 1654–1658; DS-BDK-Rules-web.txt p.13 (official Calamity is removed when the character suffers damage from the attack)
- Current text: Corrosion tokens are removed if the affected character takes damage.
- Proposed fix: Corrosion tokens are removed when the affected model suffers damage. (Calamity: no change; the manuscript's encounter-long Calamity is a deliberate departure from the official removal-on-damage and is kept.)
- Rationale: 'Character' breaks the 'model' wording used by every other condition; and the Calamity departure is recorded so that it is not 'corrected' back to official.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-081 · undefined-state · Minor · OPTIONAL
- Location: COMBAT BASICS › Conditions › Poison (manuscript.md line 1616); GAME COMPONENTS › Tokens (line 703)
- Evidence: manuscript.md:703, 1616–1618
- Current text: Poison tokens are not limited to one per model.
- Proposed fix: If no poison tokens remain in the supply, further poison tokens are not placed.
- Rationale: Seven poison tokens exist; unlimited stacking across several models exhausts them.
- Gameplay impact: Rare; four-character games with poison weapons.
- Decision needed: N

### A-085 · undefined-state · Minor · REQUIRED
- Location: COMBAT BASICS › Pushing (manuscript.md line 1592)
- Evidence: manuscript.md:931, 959, 1592; DS-Core-Rules-lores.txt p.21; FAQ (push: any node farther from the attacker)
- Current text: The pushed model(s) must move to the adjacent node most directly opposite of the attacking model. ... A model being pushed directly into a corner remains on the corner node.
- Proposed fix: If the node most directly opposite the attacker is not a valid node, the pushed model moves to the valid adjacent node that is farthest from the attacker, chosen by the players if several are tied. If no valid adjacent node exists, the model is not pushed.
- Rationale: Gravestones and chests forbid entry; the push rule gives no fallback except for corners.
- Gameplay impact: Occurs on most tiles with terrain.
- Decision needed: N

### A-113 · terminology · Minor · CLEAN-UP
- Location: GAME COMPONENTS › Tokens (manuscript.md line 681); Encounter Turn Order (line 1285); Character Attacks (line 1850); Enemy Turn Overview (line 1664)
- Evidence: manuscript.md:681, 1285, 1291, 1517, 1664, 1850
- Current text: Wound tokens / damage tokens / wounds
- Proposed fix: Use 'wound token' throughout for the tokens placed on enemies and 'damage cube' for the red cubes on endurance bars.
- Rationale: Three terms for one component.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-125 · terminology · Minor · CLEAN-UP
- Location: CHARACTERS › Character Dashboards item 7 (manuscript.md line 745)
- Evidence: manuscript.md:745, 1289, 1515; DS-Core-Rules-lores.txt p.11 ('Taunt Level'); DS-Phantoms-Rules-lores.txt p.6
- Current text: Threat Level
- Proposed fix: Glossary: Threat – the value printed as 'Taunt' on official character dashboards and summon cards; the manuscript uses 'threat' for characters, phantoms and enemies alike.
- Rationale: Physical dashboards say Taunt; without the glossary note readers cannot find the character's threat value.
- Gameplay impact: Cosmetic.
- Decision needed: N

### B-005 · undefined-value · Minor · REQUIRED
- Location: L1529 (Enemy Scaling) with L1627-1690 (Push-move / Push-attack)
- Evidence: Skeleton Soldier (V2 p.24) has no attack icon; its only damage is a push attack inside its move. The rule adds Repeat to the 'attack behaviour'; it is undefined whether a push-move with damage counts, and the 2-player move 1 -> 2 rule already doubles that enemy's possible hits.
- Current text: If playing with four characters, add *repeat to* each non-boss enemy's attack behaviour.
- Proposed fix: If Repeat is retained: "Repeat applies to attack icons only. Movement behaviours, including push-moves that deal damage, are never repeated."
- Rationale: Removes an ambiguity that otherwise quadruples push-mover damage at 4 players (two moves x Repeat 2).
- Gameplay impact: Prevents a 2-damage push enemy becoming an 8-hit threat.
- Decision needed: N

### B-006 · table-text-mismatch · Minor · REQUIRED
- Location: L1511 vs L1523 (Enemy Data Cards vs Enemy Scaling)
- Evidence: L1511 says scaled health = base + one per character 'in play'; L1523 says base + characters 'beyond one'. For 1 character these give base+1 and base respectively; the table (row 1 'Base Health') agrees with L1523.
- Current text: When playing with more than one character, calculate a scaled health value by adding one health for each character (including dead characters) in play.
- Proposed fix: "When playing with more than one character, calculate a scaled health value by adding one health for each character (including dead characters) beyond the first."
- Rationale: Makes the two statements and the table agree.
- Gameplay impact: Removes a one-health discrepancy at every player count.
- Decision needed: N

### B-026 · balance · Minor · PROPOSED
- Location: L1642-1648 (Conditions > Calamity)
- Evidence: Manuscript: -1 to block, resist and dodge results, not removed until the encounter ends. Official (DS-BDK-Rules-web, text lines 452-458): -1 success on the roll; the token is removed when the character suffers damage from the attack. Per-hit cost with 2 black block dice is +0.97 expected damage; over a five-hit boss fight the persistent version costs about +4.9 damage against about +1 for the official version.
- Current text: *Calamity* tokens are not removed at the end of a model's turn. *Calamity* tokens are only removed at the end of the encounter.
- Proposed fix: "Calamity tokens are not removed at the end of a model's turn. A Calamity token is removed when the affected model suffers damage from an attack."
- Rationale: Restores the official duration; Kalameet already applies the token repeatedly (BDK: Mark of Calamity is always in the deck).
- Gameplay impact: Reduces Kalameet's effective damage by roughly 4 per fight per character.
- Decision needed: Y

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

### C-047 · terminology · Minor · CLEAN-UP
- Location: L2115; L3082; L831; L1501; L1734
- Evidence: 'Dodge difficulty' plain capital (2115, 3082); '*Dodge*' italic capital in lists/headings (831, 1501, 1734); '*dodge*' x22 and plain 'dodge' x16 elsewhere
- Current text: Dodge
- Proposed fix: *dodge* (lower-case keyword; capital only at sentence start or in a heading)
- Rationale: Keyword case must be uniform.
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

### C-063 · terminology · Minor · CLEAN-UP
- Location: L787; L701; L793; L1351; L1600
- Evidence: 'the appropriate condition marker' / 'a staggered condition marker' (787) vs 'condition token' x10
- Current text: condition marker
- Proposed fix: condition token
- Rationale: Component name.
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

### C-120 · voice · Minor · REQUIRED
- Location: L1963; L2043-2047; L2055-2057; L2065; L2125; L2340; L2348; L1592-1594
- Evidence: Procedures written as long prose paragraphs: Resuming Exploration (1963); mimic chest procedure (2043-2047); crystal lizard spawn/escape (2055-2057); fog gate (2065); behaviour deck construction (2125); bonfire ascetic (2340); transposition 'First, ... Second, ... Third, ... Fourth, ...' (2348); push resolution (1592-1594)
- Current text: First, players gather all available legendary treasure cards... Second, ... Third, ... Fourth, ...
- Proposed fix: Numbered steps, one action per step.
- Rationale: Multi-step procedures are read at the table mid-game; numbered steps are scannable.
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

### D-036 · underspecified-deviation · Minor · REQUIRED
- Location: manuscript.md 2020 (Invader Encounter Setup)
- Evidence: Enemy scaling is additive (+1 health per extra character, 1523); the invader rule says invaders 'do not multiply their health by the number of characters'.
- Current text: Invaders do not multiply their health by the number of characters like other enemy models.
- Proposed fix: Invaders do not receive enemy scaling.
- Rationale: Aligns wording with the scaling rule.
- Gameplay impact: None.
- Decision needed: N

### F-068 · prose-crossref · Minor · CLEAN-UP
- Location: L1485 §Combat Basics › Target versus Hit
- Evidence: Prose cross-reference: 'per the optional rules detailed later'
- Current text: per the optional rules detailed later
- Proposed fix: '(see §20)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §20 Player vs Player. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-069 · prose-crossref · Minor · CLEAN-UP
- Location: L1600 §Combat Basics › Conditions
- Evidence: Prose cross-reference: 'listed below'
- Current text: listed below
- Proposed fix: Permitted: 'below' may be used only for material within the same numbered section. — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: same section (§8.5 sub-headings). Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-085 · register-shift · Minor · CLEAN-UP
- Location: L1203–1479 §Gameplay; L1598–1658 §Combat Basics › Conditions; L3038–3094 §PvP
- Evidence: Bullet-fragment register ('- Remove all damage cubes.', '- Souls cannot be transferred between characters.', '- Aggro token is not used.') alongside declarative-prose chapters (§3, §4, §8–§10) and numbered-procedure chapters (§6).
- Current text: - Drop all *souls* from the dashboard onto the current encounter tile. / - *Aggro* token is not used. / - Dying in PvP does not cause any penalty.
- Proposed fix: Normalise per the Voice Guide: sequences → numbered steps; standing rules → full declarative sentences with a subject ('The *aggro* token is not used in PvP.'); keep bullets only for unordered lists of conditions or components.
- Rationale: Three registers for the same kind of content; readers cannot tell a procedure from a standing rule.
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

### B-036 · scaling · Note · OPTIONAL
- Location: L1531 (Enemy Scaling: bosses do not scale) with L2184 (Boss Turn Overview)
- Evidence: Boss health is fixed (consistent with Core p.26 and V2 p.28). Because the boss acts after every character turn, the number of boss activations needed to kill it is independent of player count (example boss 24 health / block 2: about 11 character turns with Shortsword [2], 6 with tier-two weapons), so each character absorbs 1/N of the boss's attacks. Combined with the ordinary-encounter scaling of L1519-1560, the route is harder than the boss at 4 players and easier than the boss at 1 player.
- Current text: Boss enemies (mini, main, and mega) do NOT modify their base health or receive scaling benefits otherwise.
- Proposed fix: No change to the boss rule; adopt B-003/B-004 so that encounter difficulty does not invert relative to bosses. Optionally: "At four characters, increase a mini-boss's or main-boss's starting health by four."
- Rationale: Both official editions leave bosses unscaled; the inversion is caused by the encounter table, not by the boss rule.
- Gameplay impact: None unless the optional sentence is adopted (adds about two boss activations at 4 players).
- Decision needed: N

### B-038 · balance · Note · OPTIONAL
- Location: L1610 (Conditions > Bleed) and L1636 (Stagger)
- Evidence: Bleed: 3 unblockable damage on the second token (Hollowed p.8) vs official +2 when next damaged (Core p.21, V2 p.21): 3 damage = 37.5% of an 8-box bar, and two bleed hits kill any enemy with scaled health <= 3 outright. Stagger -1 to dodge turns a one-die dodger into an automatic failure. Both are deliberate departures and internally consistent.
- Current text: If a second *bleed* token would be placed on a model, deal three damage and remove all *bleed* tokens from that model. ... *Staggered* models subtract one from *attack*, *block*, *resist*, and *dodge*.
- Proposed fix: No numeric change. Add: "Bosses can hold bleed tokens." or "Bosses are immune to bleed." so the 3-damage trigger against a 24-health boss is defined.
- Rationale: The strongest condition in the game needs an explicit boss ruling; the values themselves are a reasonable design choice.
- Gameplay impact: Clarifies whether bleed weapons are the best anti-boss tool.
- Decision needed: Y

### F-108 · copied-prose · Note · OPTIONAL
- Location: L1485–1487 §Combat Basics › Target versus Hit
- Evidence: Matches official text — paraphrase (section structure and phrasing)
- Current text: When a character or an enemy attacks, the model defending the attack is considered the attack's target… A model is considered hit by an attack even if the attack deals zero damage…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.20. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-109 · copied-prose · Note · OPTIONAL
- Location: L1491–1493 §Combat Basics › Enemy Data Cards
- Evidence: Matches official text — verbatim (33-word run, 88%)
- Current text: Each enemy type in the game has a data card breaking down how it works in the game. Enemy data cards give the information necessary… Each enemy data card includes the following information:
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.20. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-110 · copied-prose · Note · OPTIONAL
- Location: L1513–1517 §Combat Basics › Enemy Data Cards
- Evidence: Matches official text — near-verbatim (24-word run; 'heart of any enemy' → 'core element')
- Current text: The behaviour icons are the core element of any enemy… An enemy's threat level determines the order in which it takes a turn in combat with higher values taking their turn first… The enemy's block value reduces the damage it suffers from physical attacks, and its resist value reduces the damage it suffers from magical attacks… An enemy's base health is how much damage the enemy can suffer before being defeated…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.20. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-111 · copied-prose · Note · OPTIONAL
- Location: L1588–1594 §Combat Basics › Pushing
- Evidence: Matches official text — near-verbatim (L1590 58%; L1594 16-word run)
- Current text: Certain movements and attacks are labelled as push-movements and push-attacks… Push movement does not cost stamina. / Boss models cannot be pushed by a character's movement or attack. The only way a boss model can be pushed is if another boss model moves onto its node. / If the push icon appears on an attack, the model(s) hit by the attack are pushed… most directly opposite…
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.21 (L1590 also V2 p.21). Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

### F-112 · copied-prose · Note · OPTIONAL
- Location: L1600 §Combat Basics › Conditions
- Evidence: Matches official text — near-verbatim (10-word run)
- Current text: Some attacks inflict conditions on their target. When an attack has a condition icon, place the corresponding condition token on the model(s) hit by that attack.
- Proposed fix: No change required for copyright (rights held). For voice: rewrite into the house pattern when the passage is touched; verbatim passages (≥90%) carry the official 'explanatory' voice and its reader-address habits.
- Rationale: Official source: Core p.21. Detected by 6-word shingle overlap against work/text/*.txt; page = PDF page index = printed page number (verified).
- Gameplay impact: none
- Decision needed: N

## Completion entries that apply (0) — approved at Gate 1

