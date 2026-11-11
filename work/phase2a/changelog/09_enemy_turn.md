# Change log — chapter 09 (Enemy Turn)

### CH-09-001 · §9 Enemy Turn
- Type: style
- Before: "# ENEMY TURN" / "## Overview" / "### *Block* & *Resist*" / "### *Parry* & *Riposte*"
- After: "# 9. Enemy Turn" with H2s 9.1 Overview, 9.2 Enemy Movement, 9.3 Enemy Attacks, 9.4 Block and Resist, 9.5 Dodge, 9.6 Parry and Riposte; a chapter intro of 48 words with no rule in it
- Rationale: Titles follow the section map. The three defences become numbered sections of their own, with no ampersand and no italics in headings, and every H3 is in Title Case.
- Source: C-101, C-104, C-112, C-047; brief §4

### CH-09-002 · §9.1 Overview
- Type: cut
- Before: "For enemies with equal threat levels, the enemy model closer to a character model goes first, if multiple enemy models are equidistant to a character model then the enemy model with more wound token's goes first."
- After: "The round as a whole, and the order between enemy models that share a threat value, are stated with the encounter turn order (see §7.5, Encounter Turn Order)."
- Rationale: The round structure and the turn-order tie-breaks are owned by §7.5. The chapter cites them once and does not restate them.
- Source: cut/simplify list; A-124, C-015, C-020, C-036, A-113; chapter 07 issues list

### CH-09-003 · §9.1 Overview
- Type: correction
- Before: "If there is no valid target or the enemy behaviour otherwise cannot be reasonably executed, that enemy behaviour is skipped and the next icon to the right on the enemy behaviour card is then resolved."
- After: "An icon that has no valid *target*, or that cannot be resolved, is skipped, and the next icon to the right is resolved."
- Rationale: The hedge is removed so that the condition is mechanical. "Behaviour card" is corrected: a non-boss enemy's icons are printed on its data card.
- Source: C-024, A-116, F-113

### CH-09-004 · §9.1 Overview
- Type: clarification
- Before: "An enemy model ends its turn once all of the icons on its behaviour card have been resolved."
- After: "The enemy's turn ends when its last icon has been resolved or when the enemy is killed."
- Rationale: A riposte may kill an enemy during its own turn (§9.6); the turn then ends.
- Source: A-119

### CH-09-005 · §9.1 Overview
- Type: restructure
- Before: "Non-boss enemies follow the behaviour icons on their data cards. Bosses follow the icons on their behaviour cards instead."
- After: "Invaders do not take their turns with the enemies: an *invader* takes a turn after each character's turn (see §12.2)."
- Rationale: Bosses, invaders, summons, and mimics are sent to their owning sections (§16, §12.2, §12.1, §13) in one sentence each. The invader's cadence is a preserved rule.
- Source: preserve list; chapter instructions

### CH-09-006 · §9.1 Overview
- Type: clarification
- Before: new text
- After: "Enemies target only characters; an enemy never targets another enemy (see §8.1). An enemy's health, movement, and attack values are scaled for the number of characters (see §8.3)."
- Rationale: Targets, scaling, and the conditions that alter an enemy's icons are cited to their owning sections instead of being left implied.
- Source: A-079; brief §5

### CH-09-007 · §9.2 Enemy Movement
- Type: style
- Before: "The enemy movement icon shows how an enemy model will move. Various smaller icons can appear around the movement icon, modifying how the enemy moves."
- After: "The number printed in the arrow is the number of *nodes* the enemy moves. An arrow that points upwards moves the enemy towards the target; an arrow that points downwards moves it away from the target."
- Rationale: Copied explanatory prose and the future tense are replaced by the rule in the book's voice.
- Source: F-114, F-088

### CH-09-008 · §9.2 Enemy Movement
- Type: completion
- Before: "If two or more characters are tied for being nearest, the enemy moves towards the character with the aggro token." / "the enemy moves towards the character with the higher threat level."
- After: "**Nearest character.** The living character at the shortest *range* from the enemy (see §5.4). If two or more characters are tied for nearest, the nearest character is the one of them who holds the aggro token."
- Rationale: "Nearest" is defined once, by range and for living characters only, and serves movement and attacks alike. The manuscript's tie-break is kept; the players choose only between tied characters of equal threat, a case the manuscript left open.
- Source: D-008, A-023, F-116; chapter instructions

### CH-09-009 · §9.2 Enemy Movement (Paths)
- Type: completion
- Before: new text
- After: "When the icon moves the enemy towards its target, the enemy follows the shortest path of valid nodes from its own node to the target's node."
- Rationale: The manuscript did not say what an enemy does when the node its icon points to is blocked. The enemy now moves around blocking terrain by the shortest valid path and does not move when no path exists, as §5.5 requires of this section.
- Source: A-082; chapter 05 issues list; chapter instructions

### CH-09-010 · §9.2 Enemy Movement (Paths)
- Type: clarification
- Before: "If an enemy movement icon instructs an enemy to move away from a character that is already at maximum distance, then it simply does not move."
- After: "When the icon moves the enemy away from its target, each node the enemy enters must be a valid node at a greater range from the target than the node it leaves."
- Rationale: "Maximum distance" becomes a test on each node entered, measured in range, and the filler word is removed.
- Source: F-090, C-123

### CH-09-011 · §9.2 Enemy Movement (Paths)
- Type: style
- Before: "When two different nodes would take an enemy closer to where it is trying to go, the players can choose which node the enemy enters."
- After: "If two or more such paths are equally short, the players choose which path the enemy follows."
- Rationale: A verbatim official sentence is rewritten, and "can" is not used for a permission.
- Source: F-115

### CH-09-012 · §9.2 Enemy Movement (Paths)
- Type: restructure
- Before: new text
- After: "An enemy never leaves the tile and never passes through a *doorway* (see §5.2)."
- Rationale: The tile boundary, the node model limit, traps, scaling, and frostbite are owned by other sections; each is cited in one sentence.
- Source: chapter 05 issues list; brief §5

### CH-09-013 · §9.2 Enemy Movement (Towards Aggro, Away from Aggro, Towards Nearest, Away from Nearest)
- Type: style
- Before: "The enemy moves the stated number of nodes away from to the nearest character."
- After: "The enemy moves the number of nodes shown away from the nearest character. An enemy with no valid node farther from that character does not move."
- Rationale: The four sub-sections take Title Case and one wording. The typographical error and the verbatim official sentences are removed, and the tie-break moves to the definition of the nearest character.
- Source: C-101, F-116, C-015

### CH-09-014 · §9.2 Enemy Movement (Push-Move)
- Type: completion
- Before: "If the Movement icon includes the push icon, the enemy's movement pushes characters out of its way."
- After: "A push-move that shows no damage value is not an attack. The characters it pushes are not *hit*, and they cannot *block*, *dodge*, or *parry* it (see §8.4)."
- Rationale: The icon is defined here: the target is fixed before any character is pushed, and the enemy follows the target's current node. The push steps are owned by §8.4 and are cited, not restated. The rule that only a damaging behaviour may be dodged is stated with the icon it concerns.
- Source: F-117, A-023; manuscript Pushing (lines 1594–1596)

### CH-09-015 · §9.2 Enemy Movement (Push-Move with a Damage Value)
- Type: completion
- Before: "If the push icon includes a number, characters pushed out of the way suffer that amount of damage during the push."
- After: "Each time the enemy enters a node, it makes a physical attack against every character on that node before those characters are pushed (see §8.4)."
- Rationale: The damage number is defined as a physical attack that is defended as any attack is. Characters on the starting node are pushed but not attacked, and the value is scaled as an attack value is. The manuscript's sub-heading "Push-attack" is retitled, because §8.4 and the glossary keep that term for an attack icon that bears the push icon.
- Source: A-023, D-016, A-025

### CH-09-016 · §9.3 Enemy Attacks (Targets)
- Type: completion
- Before: "Additional symbols beside the attack type icon modify the attack with special rules detailed later."
- After: "If the target is not within the attack's range, the attack misses: the icon is skipped and has no effect. No other character is attacked in the target's place."
- Rationale: Enemy attack targeting was never defined. The skull icon, the nearest-character icon, the node icon, and the out-of-range miss are now stated, and the dangling pointer is replaced by section references.
- Source: A-023, D-008, F-070, C-083, C-084

### CH-09-017 · §9.3 Enemy Attacks
- Type: clarification
- Before: "The number in the centre of the attack icon is the enemy's attack value."
- After: "An enemy's attack value is fixed and is not rolled. It is scaled for the number of characters (see §8.3) and is reduced while the enemy holds a *stagger* token (see §8.5, Stagger)."
- Rationale: The two things that change a printed attack value are cited where the value is defined, and the attack's range is cited to the data card, as §5.4 expects.
- Source: A-079; chapter 05 §5.4

### CH-09-018 · §9.3 Enemy Attacks
- Type: clarification
- Before: new text
- After: "A repeat icon applies only to the attack icon beside it, not to a movement icon."
- Rationale: A printed repeat icon cannot multiply a push-move. Repeat 2 is no longer added by scaling.
- Source: B-005; Gate 1 — OQ-07

### CH-09-019 · §9.3 Enemy Attacks (Defence)
- Type: restructure
- Before: "Characters may *block*, *resist*, *dodge*, *parry*, or do nothing. Since the enemy attack values are fixed, the character's defensive dice rolls determine the ultimate result of enemy attacks. More on each defensive option listed below."
- After: "When an attack targets a character, the character's player must choose one defence before any dice are rolled. The choice cannot be changed once it is made."
- Rationale: The choice is given a moment and made binding. "Do nothing" is dropped because a block with no dice has the same result. The commentary and the prose pointer are cut.
- Source: F-071, C-084

### CH-09-020 · §9.3 Enemy Attacks (Defence)
- Type: clarification
- Before: new text
- After: "A character is hit by an attack unless the dodge or the parry succeeds, even if the attack deals no damage (see §8.1)."
- Rationale: The hit, damage cubes, the embered reduction, the attacks of bosses, invaders, and mimics, and PvP are tied to their owning sections.
- Source: A-032; brief §5

### CH-09-021 · §9.4 Block and Resist
- Type: clarification
- Before: "Determine the defence total by adding the number of sword pips on the highest two dice results. Additional dice beyond the two with the highest shown face value are ignored."
- After: "Add together the two highest results. If one die was rolled, its result is the sum. If no dice were rolled, the sum is zero."
- Rationale: The preserved two-highest-dice rule is kept and its two edge cases are stated.
- Source: preserve list; chapter instructions

### CH-09-022 · §9.4 Block and Resist
- Type: clarification
- Before: new text
- After: "A fixed modifier is applied after the two highest results are added, whether or not a die of its card is among the two highest."
- Rationale: The manuscript defined dice modifiers for attacks only. The point at which a defence modifier applies is now fixed, as §4.1 expects of this section.
- Source: D-033, A-120; chapter 04 issues list

### CH-09-023 · §9.4 Block and Resist
- Type: clarification
- Before: "Gather all dice of the appropriate type noted on the character's currently equipped armour, weapon(s), and shield(s)."
- After: "Cards in the *back-up slot* and in the *inventory* provide no dice (see §3.2). A *spell* stored in a *catalyst* provides no dice (see §4.3)."
- Rationale: The cards that provide dice are named: every equipped card with its attached upgrade cards, and nothing else.
- Source: A-070; chapter 03 §3.2

### CH-09-024 · §9.4 Block and Resist
- Type: clarification
- Before: "If the enemy's attack value is less than or equal to the character's defence value, the character takes no damage."
- After: "A character who blocks or resists is *hit* by the attack, whatever the defence total (see §8.1)."
- Rationale: "Defence value" becomes "defence total". A full block still counts as a hit, and a total of less than zero is treated as zero.
- Source: C-036; brief §3

### CH-09-025 · §9.5 Dodge
- Type: clarification
- Before: "Characters may spend two additional stamina (total of three stamina cost) before rolling dice to add a single additional *dodge* die to their roll, up to a maximum of four *dodge* dice."
- After: "The character may pay two further stamina to add one green die. This may be done once for each dodge, and no dodge is rolled with more than four dice."
- Rationale: The preserved cost is kept. The option is its own step and is taken before the roll.
- Source: preserve list; C-095

### CH-09-026 · §9.5 Dodge
- Type: clarification
- Before: "If the enemy dodge difficulty is zero, the character does not need to roll dice and the dodge automatically succeeds, even if they have no dice to roll."
- After: "A character whose equipped cards show no dodge dice may still attempt a dodge. If no dice are rolled, the count is zero, and the dodge fails unless the dodge difficulty is zero."
- Rationale: Both zero cases are stated, and a dodge is open only to a character with an empty space for the stamina cube (§3.4).
- Source: chapter instructions; chapter 03 §3.4

### CH-09-027 · §9.5 Dodge (Successful Dodge)
- Type: clarification
- Before: "The character must move to an adjacent node."
- After: "The character must then move to an *adjacent node* that is a *valid node*, chosen by the character's player (see §5.2). If no valid node exists, the character stays on their node."
- Rationale: The mandatory dodge movement gains its fallback. Its effect on barrels, traps, and the node model limit is cited, and it is stated not to be a move.
- Source: A-087; chapter 05 §5.2, §5.5

### CH-09-028 · §9.5 Dodge (Failed Dodge)
- Type: clarification
- Before: "Determine damage to the defending character as above."
- After: "The roll is resolved from step 2 of the block and resist procedure (see §9.4)"
- Rationale: The prose pointer becomes a section reference. The armour-only roll is stated to include the upgrade cards attached to the armour card.
- Source: F-072, C-084

### CH-09-029 · §9.5 Dodge (Traps)
- Type: completion
- Before: new text
- After: "A trap is dodged under the rules of this section, against the dodge difficulty shown on its trap token (see §5.5, Traps)."
- Rationale: §5.5 sends the trap dodge to this section; the section now receives it.
- Source: chapter 05 §5.5; chapter instructions

### CH-09-030 · §9.5 Dodge
- Type: clarification
- Before: new text
- After: "Only an attack that targets the character may be dodged; a *push-move* that shows no damage value is not an attack (see §9.2, Push-Move)."
- Rationale: The section states what may be dodged and defines the dodge difficulty in one place for enemies, bosses, and traps.
- Source: A-023; manuscript Pushing (line 1596)

### CH-09-031 · §9.6 Parry and Riposte
- Type: clarification
- Before: "Characters must be equipped with a shield as their left weapon."
- After: "A shield in the right weapon slot does not permit a parry. A character who wields a weapon *two-handed* has no shield equipped and cannot parry (see §10.4)."
- Rationale: The preserved requirement is tied to the named left weapon slot of §3.2, and the two cases the manuscript left open are closed.
- Source: A-068 (in part), D-030, B-022; chapter 03 issues list

### CH-09-032 · §9.6 Parry and Riposte
- Type: clarification
- Before: "*Push, area-of-effect,* and *boss-arc* attacks cannot be *parried*."
- After: "The attack made by a *push-move* that shows a damage value (see §9.2, Push-Move with a Damage Value)."
- Rationale: The excluded attacks are named in the book's terms: a push-attack, the attack of a push-move with a damage value, a node attack, and a boss's attack except where §15.6 allows.
- Source: C-027; chapter instructions

### CH-09-033 · §9.6 Parry and Riposte
- Type: restructure
- Before: "1. Pay one stamina to attempt to *parry* an attack. 2. Determine if current enemy attack can be *parried*."
- After: "A parry is permitted only if both of the following are true."
- Rationale: The conditions are tested before the stamina is paid. The procedure states that the extra die of a dodge is not available to a parry.
- Source: brief §2 (procedures)

### CH-09-034 · §9.6 Parry and Riposte (Riposte)
- Type: clarification
- Before: "The character may make one *riposte* attack out of turn against the attacker using any *attack option* on the weapon equipped to the right weapon slot after paying the associated stamina cost."
- After: "It is not the character's *Attack* major action, and it does not count against the attacks the character makes in their own turn (see §10.3)."
- Rationale: A riposte is an attack in every respect but two: it is made in the attacker's turn and it lies outside the character's own allowance. The stagger token is placed first, an enemy cannot dodge or parry a riposte, a riposte against a character is left to §20.4, and a killed attacker's turn ends.
- Source: A-119, A-078; Gate 1 — OQ-16

### CH-09-035 · §9.6 Parry and Riposte (Failed Parry)
- Type: style
- Before: "The character takes full damage without the option to block*/*resist."
- After: "When a parry fails, the character is hit and suffers damage equal to the full *attack value*. No block or resist dice are rolled."
- Rationale: Split italics are repaired. The failed parry is stated as a hit, so the attack's conditions apply.
- Source: C-028

### CH-09-036 · §9.2 to §9.6 (worked examples)
- Type: completion
- Before: new text (the manuscript chapter has no worked example)
- After: 11 examples: two for movement, one for a push-move with a damage value, two for targets, two for block and resist, two for the dodge, and two for the parry and riposte
- Rationale: Each procedure is shown with concrete numbers, succeeding once and failing once where it has two outcomes. A dodge example and a parry example were required. A named enemy is used only where its values match the example in §8.3; elsewhere the examples say "an enemy", so that no example reads as card data.
- Source: chapter instructions; brief §2

### CH-09-037 · §9 Enemy Turn (style sweep)
- Type: style
- Before: "wound token's"; "*Block* & *Resist*"; "flip their *luck* token face-down"; "it simply does not move"; "how an enemy model will move"; curly apostrophes
- After: "wound tokens"; "Block and Resist"; "flip the *luck* token"; "does not move"; present tense; straight quotes
- Rationale: Spelling, typography, tense, hedge words, and the italics policy (a headword italicised at its first use in each H2, the whole word, no punctuation inside) are applied throughout.
- Source: C-015, C-027, C-028, C-030, C-047, C-060, C-111, C-123, F-088, F-089, F-090

### CH-09-038 · §9 Enemy Turn (findings not applied here)
- Type: clarification
- Before: n/a
- After: not applied here
- Rationale: OPTIONAL findings skipped: D-039 (restoring "taunt" for characters conflicts with the single term "threat"); A-018 (riposte and boss aggro, owned by §16.4); A-042 (heat-up during the boss's own turn, owned by §15.5). Approved PROPOSED findings not applied: B-002 and B-033, which alter preserve-list rules. Owned elsewhere and cited only: A-013 (§7.5), A-032 (§20.4), A-078 and A-079 (§8.5), B-022 (§4.1). No change required: A-124, C-095.
- Source: brief §5; preserve list; chapter 09 issues list

### CH-09-039 · §9.1
- Type: ruling
- Before: "An icon that has no valid *target*, or that cannot be resolved, is skipped, and the next icon to the right is resolved. The enemy's turn ends when its last icon has been resolved or when the enemy is killed."
- After: "An icon that has no valid *target*, or that cannot be resolved, is skipped, and the next icon to the right is resolved. If the data card bears the *repeat* icon {{icon:ast-0061-repeat-behaviour-or-attack}}, the enemy resolves its whole row of icons the number of times shown, and the target of each icon is determined again each time. The enemy's turn ends when its last icon has been resolved for the last time or when the enemy is killed."
- Rationale: [MECHANICAL CHANGE] States the repeat rule for an enemy data card where the row of icons is described, in the words §16.1 uses for a boss.
- Source: final rulings, combat-E18 (`06_final_rulings.md`); As combat-E12.

### CH-09-040 · §9.3
- Type: ruling
- Before: "- A *condition* icon places the matching condition token on each character hit by the attack (see §8.5).
- A *repeat* icon {{icon:ast-0061-repeat-behaviour-or-attack}} causes the attack to be resolved the number of times shown, and the target is determined afresh each time. A repeat icon applies only to the attack icon beside it, not to a movement icon."
- After: "- A *condition* icon places the matching condition token on each character hit by the attack (see §8.5).

A *repeat* icon {{icon:ast-0061-repeat-behaviour-or-attack}} on the data card repeats the enemy's whole row of icons, not one attack (see §9.1)."
- Rationale: [MECHANICAL CHANGE] Deletes the attack-only special case, which was written for the scaling rule that Gate 1 removed.
- Source: final rulings, combat-E19 (`06_final_rulings.md`); As combat-E12; Gate 1 OQ-07.

### CH-09-041 · §9.3
- Type: clarification
- Before: "### Defence

When an attack targets a character, the character's player must choose one defence before any dice are rolled."
- After: "### Attack Sequence

An enemy attack is resolved as follows.

1. Determine the target (see §9.3, Targets).
2. Check the range. If the target is not within range, skip the icon.
3. Choose the character's defence (see §9.3, Defence).
4. Resolve the defence (see §9.4; §9.5; §9.6). If a dodge or a parry succeeds, the character is not hit, and the attack on that character ends.
5. Place the damage that the defence has not prevented (see §3.4).
6. If the attack is a push-attack, push the character (see §8.4).
7. Place any condition token the attack carries (see §8.5).

Steps 6 and 7 are resolved even if the character suffered no damage. A character who dies in step 5 is not pushed and receives no token. A node attack resolves steps 3 to 7 for one character at a time, in an order chosen by the players. The attack of a push-move with a damage value follows the same steps from […]"
- Rationale: States the order of an enemy attack once, as §10.3 does for a character attack, so that §8.4, §8.5, §9.4, §9.5, §9.6 and §16.3 have one sequence to match.
- Source: final rulings, combat-E20 (`06_final_rulings.md`); Official 2022 numbered attack steps (DS-TG 1667-1763); this book, §8.4 and §8.5 (damage, then push, then condition).

### CH-09-042 · §9.4
- Type: correction
- Before: "7. Place any *condition* token the attack carries (see §8.5) and resolve any *push* (see §8.4), even if the character suffered no damage."
- After: "7. Resolve any *push* (see §8.4), then place any *condition* token the attack carries (see §8.5), even if the character suffered no damage."
- Rationale: Step 7 gave the condition before the push; §8.5 and §10.3 give the push first, and the order decides whether a stagger token affects the dodge of a trap entered by the push.
- Source: final rulings, combat-E21 (`06_final_rulings.md`); This book, §8.5 second paragraph and §10.3 step 11.

### CH-09-043 · §9.6
- Type: ruling
- Before: "- A *shield* is equipped in the character's left *weapon slot* (see §3.2; §4.1)."
- After: "- A *shield* is equipped in one of the character's *weapon slots* (see §3.2; §4.1)."
- Rationale: [MECHANICAL CHANGE] The parry was the only rule in the book that depended on which weapon slot held a card; the choice of slot carried no decision.
- Source: final rulings, combat-E22 (`06_final_rulings.md`); Audit finding A-068 (approved, REQUIRED) proposed the same; no official or community ruleset has a left-hand rule.

### CH-09-044 · §9.6
- Type: ruling
- Before: "A shield in the right weapon slot does not permit a parry. A character who wields"
- After: "The shield may be in either weapon slot. A character who wields"
- Rationale: [MECHANICAL CHANGE] As combat-E22.
- Source: final rulings, combat-E23 (`06_final_rulings.md`); As combat-E22.

### CH-09-045 · §9.6, Riposte
- Type: ruling
- Before: "A riposte is one attack against the attacker, made with one *attack option* of the *weapon* equipped in the character's right weapon slot."
- After: "A riposte is one attack against the attacker, made with one *attack option* of the *weapon* equipped in the character's other weapon slot, the slot that does not hold the shield used for the parry. A *spell* cannot be used for a riposte, whether it is equipped in that slot or stored in a *catalyst* there (see §4.3)."
- Rationale: [MECHANICAL CHANGE] Follows the either-slot parry and states the spell exclusion that the word "weapon" only implied.
- Source: final rulings, combat-E24 (`06_final_rulings.md`); As combat-E22; this book, §4.1 and §4.3.

### CH-09-046 · §9.6, Riposte
- Type: ruling
- Before: "No riposte is made if the right weapon slot holds no weapon with an attack option,"
- After: "No riposte is made if the other weapon slot holds no weapon with an attack option,"
- Rationale: [MECHANICAL CHANGE] As combat-E22.
- Source: final rulings, combat-E25 (`06_final_rulings.md`); As combat-E22.
