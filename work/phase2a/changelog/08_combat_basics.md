# Change log — chapter 08 (Combat Basics)

### CH-08-001 · §8 Combat Basics
- Type: style
- Before: "# COMBAT BASICS" / "## Target versus Hit" (unnumbered headings, no chapter intro)
- After: "# 8. Combat Basics" / "## 8.1 Target versus Hit" … "## 8.5 Conditions"; a chapter intro of 58 words with no rule in it
- Rationale: Chapter and section titles follow the section map; every reference in the book targets these numbers.
- Source: C-104; brief §4

### CH-08-002 · §8.1 Target versus Hit
- Type: restructure
- Before: "When a character or an enemy attacks, the model defending the attack is considered the attack's target. Attacks have a single target by default but some attacks have special modifiers …"
- After: "**Target.** The model at which an attack is directed." … "Some attacks target every opposing model on one *node* (see §9.3; §10.3, Area-of-Effect), and some *boss* attacks target every character on several nodes (see §16.3)."
- Rationale: Target is stated as a definition in the glossary's form and the copied explanatory prose is rewritten in the book's voice; the multi-target attacks are cited in their owning sections instead of being left as "special modifiers".
- Source: F-108, C-119, A-023, D-008

### CH-08-003 · §8.1 Target versus Hit
- Type: style
- Before: "Characters may only target other characters if playing a PvP encounter per the optional rules detailed later."
- After: "A character targets another character only in a player versus player (PvP) *encounter* (see §20)."
- Rationale: The positional cross-reference becomes a numbered one, and PvP is spelt out at its first use in the chapter. The resolution of a character's attack on a character is owned by §20.4.
- Source: F-068, C-084, A-032

### CH-08-004 · §8.1 Target versus Hit
- Type: clarification
- Before: "A model is considered hit by an attack even if the attack deals zero damage so long as the attack was in range and the target model did not successfully dodge the attack."
- After: "**Hit.** An attack hits its target when the target is within the attack's *range* (see §5.4) and does not avoid the attack by a successful *dodge* (see §9.5) or a successful *parry* (see §9.6)."
- Rationale: Hit is stated once as a definition with its two tests; a successful parry avoids the hit exactly as a successful dodge does, as the glossary already stated. An out-of-range target is stated to be not hit.
- Source: D-008, A-023, C-047; glossary Hit

### CH-08-005 · §8.1 Target versus Hit
- Type: style
- Before: "Therefore, targets who successfully *dodge* an attack are not considered hit and therefore are not pushed or afflicted with conditions associated with being hit by the attack."
- After: "An attack has no effect on a target it does not hit: it deals no damage, does not *push* the target, and places no *condition* token on it."
- Rationale: The connectives are removed and each outcome is stated as a rule; the companion rule (pushes and conditions apply to every model hit, with or without damage) is its own sentence.
- Source: F-091, F-108

### CH-08-006 · §8.1 Target versus Hit
- Type: clarification
- Before: new text
- After: "*Example.* An enemy attack with an *attack value* of 4 bears the push icon and targets the Knight and the Herald, who share a node within its range. …"
- Rationale: A worked example shows a hit that deals no damage and a dodge that avoids the push.
- Source: brief §2 (worked examples)

### CH-08-007 · §8.2 Enemy Data Cards
- Type: restructure
- Before: "Each enemy type in the game has a data card breaking down how it works in the game. … Each enemy data card includes the following information: 1. Name 2. Threat level 3. Attack range …"
- After: "An enemy data card shows the following. - The name identifies the kind of enemy. - The *threat* value fixes the order in which enemies take their turns (see §7.5, Encounter Turn Order). …"
- Rationale: The copied anatomy list and its four explanatory paragraphs are merged into one bulleted list of full sentences, each carrying its icon and the section that resolves it.
- Source: F-109, F-110, C-119, A-125

### CH-08-008 · §8.2 Enemy Data Cards
- Type: completion
- Before: "The behaviour icons are the core element of any enemy which determine how the enemy behaves during its turn."
- After: "Smaller icons printed around a behaviour icon modify it, as follows. - The skull icon directs the movement or attack at the character who holds the *aggro token* (see §9.2; §9.3). …"
- Rationale: The satellite icons (skull, nearest character, node, push, push with damage, repeat, condition) and the physical or magical attack icon are named here with the icon slugs; each is resolved in the section cited.
- Source: A-023, D-008; brief chapter instructions

### CH-08-009 · §8.2 Enemy Data Cards
- Type: completion
- Before: new text
- After: "A *boss* data card shows a *behaviour deck* size in place of behaviour icons and adds a *heat-up* point (see §15.4). The data cards of *phantoms* and *mimics* are described with those models (see §12; §13)."
- Rationale: The reader is told where the other data cards differ; their anatomy is owned by §15.4, §12, and §13.
- Source: brief chapter instructions

### CH-08-010 · §8.2 Enemy Data Cards
- Type: correction
- Before: "When playing with more than one character, calculate a scaled health value by adding one health for each character (including dead characters) in play."
- After: "**Scaled health.** An enemy's base health plus the increase that enemy scaling gives for the number of characters (see §8.3)."
- Rationale: The prose gave Base + 2 for two characters where the table gave Base + 1. Scaled health is now defined by reference to the one table in §8.3.
- Source: C-066, A-026, B-006

### CH-08-011 · §8.2 Enemy Data Cards
- Type: correction
- Before: "place one wound token on the base of that enemy model for each point of damage not prevented by the enemies *block* or *resist*. Once an enemy model has wounds equal to (or exceeding) its scaled health …"
- After: "When the total value of the wound tokens on an enemy model equals or exceeds its *scaled health*, the enemy is killed. Remove the model and its wound tokens from the tile at once."
- Rationale: Wound tokens have values of 1, 3, and 5, so the rule counts their total value; "wounds" and "the enemies block" are corrected; enemies are killed; the calculation of damage is left to §10.3. Bosses, phantoms, and mimics are pointed to the health dial.
- Source: C-015, C-036, A-113, C-061

### CH-08-012 · §8.2 Enemy Data Cards
- Type: clarification
- Before: new text
- After: "*Example.* The Knight, the Herald, and the Assassin fight a Hollow Soldier whose data card shows a base health of 1. With three characters its scaled health is 3. …"
- Rationale: A worked example shows scaled health, wound tokens, and the kill.
- Source: brief §2 (worked examples)

### CH-08-013 · §8.3 Enemy Scaling
- Type: mechanical change
- Before: "If playing with three or more characters, increase all non-boss attack values by one." … "If playing with four characters, add *repeat to* each non-boss enemy's attack behaviour." Table row 4: Base + 3, movement 1 to 2, +1, *Repeat* 2
- After: Table rows "3 | Base health + 2 | 1 becomes 2 | No change" and "4 | Base health + 4 | 1 becomes 2 | +1"; "With four characters, every attack value on an enemy's data card is increased by one."
- Rationale: Repeat 2 at four characters is deleted with its table column; the +1 attack moves from three characters to four; four characters give Base + 4 health. The undefined Repeat for enemies and its interaction with push-moves fall away with it.
- Source: Gate 1 — OQ-07; B-003, B-004, B-002, C-067, A-024, B-005

### CH-08-014 · §8.3 Enemy Scaling
- Type: restructure
- Before: bulleted fragments and an HTML table with the columns Character Number, Enemy Health, Enemy Movement, Enemy Damage, and Enemy Attack Repeats, and the cell "1 -&gt; 2"
- After: one four-column table ("Characters | Enemy health | Enemy movement | Enemy *attack value*") followed by one short paragraph for each column
- Rationale: The rule is stated once, in a table with the prose explaining each column; "Enemy Damage" becomes attack value, the term used everywhere else; ASCII arrows are replaced by "1 becomes 2".
- Source: C-067, C-109, C-119

### CH-08-015 · §8.3 Enemy Scaling
- Type: clarification
- Before: "Non-boss enemies gain benefits depending on the number of total characters in a game to ensure balance." … "Increase each non-boss enemy's base health by the number of characters (including dead characters) beyond one."
- After: "The number of characters is fixed at setup (see §6.1) and does not change when a character dies: a dead character and a *lost* character still count."
- Rationale: States when the number is fixed, that dead and lost characters count, and when scaling is applied; the design motive ("to ensure balance") is removed.
- Source: A-026, B-006; brief chapter instructions

### CH-08-016 · §8.3 Enemy Scaling
- Type: clarification
- Before: "If playing with two or more characters, increase any non-boss enemy behaviour of one movement to two movements."
- After: "With two or more characters, every movement icon on an enemy's *data card* that shows a value of 1 is resolved with a value of 2. A *push-move* is scaled in the same way (see §8.4)."
- Rationale: Names the icons affected and those left alone. The attack increase is likewise stated to cover each attack icon and the damage value of a push-move.
- Source: A-025

### CH-08-017 · §8.3 Enemy Scaling
- Type: completion
- Before: "Boss enemies (mini, main, and mega) do NOT modify their base health or receive scaling benefits otherwise."
- After: "Every enemy is scaled, with four exceptions. A *boss*, a *mimic*, a *phantom*, and a *crystal lizard* are never scaled (see §15.4; §13; §12; §14)."
- Rationale: The exemptions for invaders and crystal lizards covered health only and were worded as multiplication; the full list of unscaled models is stated in the owning section and the capitals are removed.
- Source: A-028, A-029, D-036, B-036

### CH-08-018 · §8.3 Enemy Scaling
- Type: completion
- Before: new text
- After: "In campaign play, the *bonfire ascetic* further increases the health of every enemy that is subject to enemy scaling (see §18.7). The number of characters in a campaign changes only when a player joins or leaves it (see §18.4)."
- Rationale: The ascetic's increase (health, not attack) and the effect of adding or dropping a player are owned by §18.7 and §18.4 and are cited, not restated.
- Source: Gate 1 — OQ-07; B-031, A-064, A-027

### CH-08-019 · §8.3 Enemy Scaling
- Type: clarification
- Before: new text
- After: "*Example.* A Hollow Soldier's data card shows a base health of 1, a movement value of 1, and an attack value of 4. …"
- Rationale: A worked example walks one enemy through all four character counts and shows that a dead character still counts.
- Source: brief §2 (worked examples)

### CH-08-020 · §8.4 Pushing
- Type: completion
- Before: "Certain movements and attacks are labelled as push-movements and push-attacks (respectively). These special push effects may push a model from its current node to an adjacent node. Push movement does not cost stamina."
- After: "A *push* forces a model from its node to a *valid node* (see §5.2). A push is not a *move*, and it costs no stamina. … A model is pushed for one of four reasons."
- Rationale: Push, push-attack, and push-move are defined in the glossary's form, and all four causes of a push are listed in the owning section, including the node model limit (§5.3) and two boss models on one node (§17.1).
- Source: F-111; chapter 05 issues list; brief chapter instructions

### CH-08-021 · §8.4 Pushing
- Type: completion
- Before: "A model being pushed directly into a corner remains on the corner node."
- After: "A node containing a *gravestone*, a *chest*, or a *pillar token* is not a valid node for a push … If no valid node exists for a push, the push does not happen and the model stays on its node."
- Rationale: The push rule gave no outcome for blocked nodes other than a corner. Terrain, traps, and a full node are cited in their owning sections, and a push with no valid node is stated not to happen.
- Source: A-085

### CH-08-022 · §8.4 Pushing
- Type: clarification
- Before: "The pushed model(s) must move to the adjacent node most directly opposite of the attacking model. If there are multiple adjacent nodes equally opposite to the attacking model the players choose the node."
- After: "The model is pushed into the valid node most directly opposite the attacker's node, chosen from the adjacent nodes that are farther from the attacker than the model's own node."
- Rationale: The direction rule is kept and given its fallback: when the opposite node is blocked, the model goes to another valid node farther from the attacker, and when none is farther (the corner case) it is not pushed. "Farther" is defined by range.
- Source: A-085, F-111

### CH-08-023 · §8.4 Pushing
- Type: restructure
- Before: "If the push icon appears on an enemy's movement, first immediately move each character on that enemy's node onto an adjacent node chosen by the players. Then, the enemy moves one node …"
- After: "For each node of the movement, the following steps are resolved in order. 1. Push each character on the enemy's node to a valid node chosen by the players. 2. Move the enemy one node …"
- Rationale: The push-move paragraph becomes a numbered procedure resolved once for each node moved; "In other words" and the duplicate statement of the direction are removed.
- Source: C-120, F-091

### CH-08-024 · §8.4 Pushing
- Type: completion
- Before: new text
- After: "… resolve a physical attack with that *attack value* against each character on the node the enemy has entered, one character at a time." … "The characters pushed in step 1 are not attacked and suffer no damage."
- Rationale: The manuscript never said that the number on a push icon is an attack, nor whether characters on the enemy's starting node are damaged. The damage is an attack against the characters on each node entered; characters moved from the starting node are not attacked.
- Source: A-023, D-016, D-008

### CH-08-025 · §8.4 Pushing
- Type: style
- Before: "Players should take note that only enemy behaviours that deal damage can be dodged. … Of course, characters who block or resist a push behaviour are pushed regardless of damage dealt."
- After: "A push-move without a damage value is not an attack: a character cannot *dodge*, *block*, or *resist* it. … A character who blocks that attack is hit and is pushed whether or not damage is dealt."
- Rationale: The advisory frame and connectives are removed and the rules are stated one to a sentence.
- Source: F-015, C-021, C-123, F-091

### CH-08-026 · §8.4 Pushing
- Type: clarification
- Before: "Boss models cannot be pushed by a character's movement or attack. The only way a boss model can be pushed is if another boss model moves onto its node."
- After: "A boss model cannot be pushed by a character's attack. The only push that affects a boss model is the push caused by another boss model moving onto its node (see §17.1)."
- Rationale: Rewritten in voice with the owning section cited; the arc limit on a push off a boss's node and boss push-moves are cited in §15.6 and §16.2, and pushes between characters in §20.5.
- Source: F-111, A-032

### CH-08-027 · §8.4 Pushing
- Type: clarification
- Before: new text
- After: three *Example.* paragraphs (a push-attack with a gravestone behind the Knight; the Herald on a corner node; a push-move of two nodes with a damage value of 5)
- Rationale: Worked examples show the fallback node, the push that does not happen, and a push-move resolved node by node.
- Source: A-085; brief §2 (worked examples)

### CH-08-028 · §8.5 Conditions
- Type: restructure
- Before: "*Bleed* tokens are limited to one per model." … "*Bleed* tokens are not removed at the end of activations." … "*Bleed* tokens are only removed at the end of the encounter."
- After: "A model holds at most one bleed token, and the token alone has no effect. … A bleed token is not removed at the end of any turn."
- Rationale: The bullet fragments of all six conditions are rewritten as short paragraphs with a subject, a trigger, and an outcome; "activation" becomes turn; the sub-headings lose their italics and expansion tags.
- Source: C-119, F-085, C-039, C-029, C-030

### CH-08-029 · §8.5 Conditions
- Type: correction
- Before: "When a model ends its turn, remove one poison token and any *frostbite*/*stagger* tokens. Each condition has its own rules and effects listed below."
- After: "Where a token is removed at the end of a model's next complete *turn*, a token placed during that model's own turn is not removed at the end of that turn …"
- Rationale: The general removal sentence contradicted the poison rule and removed a parry's stagger before it had any effect. Each condition now states its own timing once, and "next complete turn" is explained once.
- Source: A-078, F-069, F-112; Gate 1 — OQ-16

### CH-08-030 · §8.5 Conditions
- Type: completion
- Before: "Some attacks inflict conditions on their target. When an attack has a condition icon, place the corresponding condition token on the model(s) hit by that attack."
- After: "The token is placed after the attack's damage and any *push* have been resolved, and it is placed whether or not the attack dealt damage." … "Any model may hold condition tokens …"
- Rationale: States when the token is placed, that bosses and phantoms hold conditions, how condition damage is recorded, that a reduced value stops at zero, and that all tokens are removed when the encounter ends.
- Source: F-112, B-038, C-063

### CH-08-031 · §8.5 Conditions
- Type: clarification
- Before: "*Stagger* tokens are limited to one per model."
- After: "When a token of a condition is to be placed on a model that already holds a token of that condition, the token is not placed and has no effect."
- Rationale: The one-token limit is stated once for every condition with its outcome, which also settles a second stagger from stamina overflow.
- Source: A-009

### CH-08-032 · §8.5 Conditions, Bleed
- Type: clarification
- Before: "If a second *bleed* token would be placed on a model, deal three damage and remove all *bleed* tokens from that model." … "*Bleed* damage is not affected by *block* or *resist*."
- After: "When a bleed token is to be placed on a model that already holds one, the token is not placed. … Bleed damage is not an attack: it is not reduced by *block* or *resist* …"
- Rationale: The mechanic is unchanged; the second token is stated not to be placed and the damage is stated not to be an attack. A worked example is added.
- Source: C-119, B-038

### CH-08-033 · §8.5 Conditions, Poison
- Type: mechanical change
- Before: "A model suffers one damage for each *poison* token it has at the end of its activation, then removes only one *poison* token."
- After: "At the end of each of its turns, a model that holds poison tokens suffers one damage for each poison token it holds and then removes all of them."
- Rationale: A model with n poison tokens suffers n damage once and removes them all, in place of the triangular total of the manuscript. A worked example is added.
- Source: Gate 1 — OQ-13; B-025, C-039

### CH-08-034 · §8.5 Conditions, Frostbite
- Type: clarification
- Before: "*Frostbite* affected characters cannot recover stamina." … "*Frostbite* affected enemies reduce their movement values by one."
- After: "The character does not recover one stamina at the start of their turn and cannot take the *Rest* *major action* (see §10.1). … after *enemy scaling* has been applied (see §8.3; §9.2)."
- Rationale: Names the two recoveries that are blocked and fixes the order of the movement reduction and enemy scaling. Condition tokens are already removed before stamina cubes in §7.5, Encounter Recovery.
- Source: A-010

### CH-08-035 · §8.5 Conditions, Frostbite
- Type: mechanical change
- Before: "*Frostbite* tokens are removed at the end of the model's turn."
- After: "A frostbite token is removed at the end of the affected model's next complete turn."
- Rationale: The approved fix for the removal timing covers stagger and frostbite alike; a frostbite token placed during a model's own turn (for example by a riposte) now lasts through that model's following turn. The outcome is unchanged for a token placed outside the model's turn.
- Source: A-078; Gate 1 — OQ-16

### CH-08-036 · §8.5 Conditions, Stagger
- Type: clarification
- Before: "*Staggered* models subtract one from *attack*, *block*, *resist*, and *dodge*."
- After: "An enemy, boss, or phantom with a stagger token reduces each of its *attack values*, its block and resist values, and its *dodge difficulty* by one."
- Rationale: Characters roll and enemies have fixed values, so the single sentence is stated once for each.
- Source: A-079

### CH-08-037 · §8.5 Conditions, Stagger
- Type: mechanical change
- Before: "*Stagger* tokens are removed at the end of the model's turn."
- After: "A stagger token is removed at the end of the affected model's next complete turn."
- Rationale: A stagger placed by a parry during the enemy's own turn was removed at the end of that turn, before it had any effect. The causes of stagger outside attacks (stamina overflow, parry) are cited, and a worked example shows the parry case.
- Source: Gate 1 — OQ-16; A-078

### CH-08-038 · §8.5 Conditions, Calamity
- Type: clarification
- Before: "### *Calamity (*Kalameet Expansion*)*" … "*Calamity* tokens are only removed at the end of the encounter."
- After: "### Calamity" … "A calamity token is not removed at the end of any turn or when the model suffers damage. It is removed only when the encounter ends."
- Rationale: The encounter-long calamity is kept and is stated not to be removed by damage, so that it is not read as the corrosion rule. The expansion is named in the first sentence, not in the heading.
- Source: Gate 1 — OQ-24; A-080, C-029, A-115

### CH-08-039 · §8.5 Conditions, Corrosion
- Type: correction
- Before: "*Corrosion* tokens are removed if the affected character takes damage."
- After: "It is removed when the affected model next suffers damage, after that damage has been recorded."
- Rationale: "Character" broke the "model" wording used by every other condition; the token is stated to apply to the roll against the damaging attack before it is removed.
- Source: A-080, C-029

### CH-08-040 · §8 Combat Basics (style sweep)
- Type: style
- Before: curly apostrophes; "node.If"; "the enemies *block*"; "*Dodge* difficulty"; "condition marker"; "-&gt;"; "do NOT"; italicised fragments ("*repeat to*")
- After: straight quotes; corrected spacing and possessives; lower-case keywords italicised at first use in each section; "condition token"; no capitals for emphasis
- Rationale: Spelling, typography, and keyword italics follow the style sheet.
- Source: C-111, C-015, C-047, C-063, C-109, C-029, C-030, C-061

### CH-08-041 · §8 Combat Basics (findings not applied in this chapter)
- Type: clarification
- Before: n/a
- After: n/a
- Rationale: OPTIONAL findings skipped: A-081 (no supply limit on poison tokens is stated; the manuscript's "not limited" stands and substitutes serve when the seven tokens run out), B-036 (the optional boss health increase is not adopted; bosses never scale). Superseded by Gate 1: A-024 and B-005 (Repeat 2 is deleted by OQ-07, so its definition is moot), B-026 (OQ-24 keeps the encounter-long calamity). B-002's alternative (three highest dice with a shield) is not adopted because it alters the preserved two-highest-dice rule, which §9.4 owns. Owned by other chapters and only cited here: A-032 (§20.4, §20.5), A-115 (§17.8), B-031 and A-064 (§18.7), A-027 (§18.4), A-125 (§3.1 and the glossary).
- Source: A-081, B-036, A-024, B-005, B-026, B-002, A-032, A-115, B-031, A-064, A-027, A-125
