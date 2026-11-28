<!-- manuscript.md lines 1660–1797 ; chapter "ENEMY TURN" -->
# ENEMY TURN

## Overview

Each encounter begins with each enemy model taking their turn before proceeding to the character’s turns. Enemy models take their turn beginning with the highest threat and ending with the model with the lowest threat. For enemies with equal threat levels, the enemy model closer to a character model goes first, if multiple enemy models are equidistant to a character model then the enemy model with more wound token’s goes first. If there are multiple enemy models with the same threat value, distance to a character, and number of wound tokens, then the players decide which model should go first.

Non-boss enemies follow the behaviour icons on their data cards. Bosses follow the icons on their behaviour cards instead. All behaviour icons are resolved left to right. An enemy’s behaviour can be as simple as making one attack or can have multiple moves and/or attacks. If there is no valid target or the enemy behaviour otherwise cannot be reasonably executed, that enemy behaviour is skipped and the next icon to the right on the enemy behaviour card is then resolved. An enemy model ends its turn once all of the icons on its behaviour card have been resolved.

## Enemy Movement

The enemy movement icon shows how an enemy model will move. Various smaller icons can appear around the movement icon, modifying how the enemy moves. This allows different enemies to move towards or away from characters in different patterns and at different speeds.

The four directions of the movement icon are oriented so the upward direction indicates movement toward the target character. The downward direction indicates movement away from the target character. The number in the direction arrow indicates how many nodes the enemy model will move in the indicated direction. The small icon in the top right of the movement behaviour icon indicates the target character. A small skull icon indicates that movement will target the character with the *aggro* token. A small ring icon indicates that movement will target the closest character.

If an enemy movement icon instructs an enemy to move towards a character it already shares a node with, then it simply does not move.

If an enemy movement icon instructs an enemy to move away from a character that is already at maximum distance, then it simply does not move.

When two different nodes would take an enemy closer to where it is trying to go, the players can choose which node the enemy enters.

### Towards aggro

The enemy moves the indicated number of nodes closer to the character with the aggro token.

### Away from aggro

The enemy moves the indicated number of nodes farther from the character with the aggro token.

### Towards nearest

The enemy moves the stated number of nodes closer to the nearest character. If two or more characters are tied for being nearest, the enemy moves towards the character with the aggro token. If the model with the aggro token is not tied for being the nearest, the enemy moves towards the character with the higher threat level. If the enemy movement covers multiple nodes, determine the nearest character at the start of the movement, not at each step.

### Away from nearest

The enemy moves the stated number of nodes away from to the nearest character. If two or more characters are tied for being nearest, the enemy moves away from the character with the aggro token. If the model with the aggro token is not tied for being the nearest, the enemy moves away from the character with the higher threat level. If the enemy movement covers multiple nodes, determine the nearest character at the start of the movement, not at each step.

### Push-move

If the Movement icon includes the push icon, the enemy’s movement pushes characters out of its way.

### Push-attack

If the push icon includes a number, characters pushed out of the way suffer that amount of damage during the push.

## Enemy Attacks

When resolving an attack icon as part of an enemy’s turn, determine which of the two types of attacks that enemy will make. Physical attacks cause physical damage and magical attacks cause magical damage. The crossed swords icon indicates physical damage and the white circle icon indicates magical damage. The number in the centre of the attack icon is the enemy’s attack value. If there is a condition token symbol, then characters hit by that enemy are marked with the matching condition token. Additional symbols beside the attack type icon modify the attack with special rules detailed later.

Whenever an enemy model attacks a character, that character must decide how to defend themselves. Characters may *block*, *resist*, *dodge*, *parry*, or do nothing. Since the enemy attack values are fixed, the character’s defensive dice rolls determine the ultimate result of enemy attacks. More on each defensive option listed below.

### *Block* & *Resist*

1.  Gather all dice of the appropriate type noted on the character’s currently equipped armour, weapon(s), and shield(s).

    1.  *Block* dice are used against physical attacks.

    2.  *Resist* dice are used against magical attacks.

2.  Roll *block* or *resist* dice permitted by equipment.

3.  Characters may flip their *luck* token face-down to reroll any or all dice.

4.  Determine the defence total by adding the number of sword pips on the highest two dice results. Additional dice beyond the two with the highest shown face value are ignored.

5.  Determine damage to the defending character.

    1.  If the enemy's attack value exceeds the character’s defence value, the character must place red damage cubes on their dashboard equal to the difference.

    2.  If the enemy’s attack value is less than or equal to the character’s defence value, the character takes no damage.

6.  Place any condition tokens indicated, even if no damage was dealt.

7.  Resolve any push effects.

### *Dodge*

1.  Pay one stamina to attempt to *dodge* an attack.

2.  Roll a number of *dodge* dice indicated by the character’s equipment.

    1.  If the enemy dodge difficulty is zero, the character does not need to roll dice and the dodge automatically succeeds, even if they have no dice to roll.

    2.  Characters may spend two additional stamina (total of three stamina cost) before rolling dice to add a single additional *dodge* die to their roll, up to a maximum of four *dodge* dice.

3.  Characters may use their *luck* token to reroll any or all dice.

4.  If the *dodge* total is equal to or greater than the enemy’s *dodge* difficulty, the attack does not hit.

    1.  No damage is taken.

    2.  No conditions are applied.

    3.  No push effects are applied.

    4.  The character must move to an adjacent node.

5.  If the *dodge* total is less than the enemy’s *dodge* difficulty, the attack hits.

    1.  Roll only the *block* or *resist* dice (depending on enemy attack type) provided by the character’s currently equipped armour. Do not include dice provided by equipped weapons, shields, or spells.

    2.  Determine damage to the defending character as above.

    3.  Place condition tokens associated with enemy attack, even if no damage was dealt.

    4.  Resolve any push effects.

### *Parry* & *Riposte*

1.  Pay one stamina to attempt to *parry* an attack.

2.  Determine if current enemy attack can be *parried*.

    1.  Characters must be equipped with a shield as their left weapon.

    2.  Characters must share the same node as the attacker.

    3.  *Push, area-of-effect,* and *boss-arc* attacks cannot be *parried*.

3.  Roll a number of *dodge* dice indicated by the character’s equipment.

4.  Characters may use their *luck* token to reroll any or all dice.

5.  If the *dodge* value is equal to or greater than the enemy’s *dodge* difficulty, the attack is successfully *parried*.

    1.  No damage is taken.

    2.  No conditions are applied.

    3.  Place a *stagger* token on the attacking model’s base.

    4.  The character may make one *riposte* attack out of turn against the attacker using any *attack option* on the weapon equipped to the right weapon slot after paying the associated stamina cost.

6.  If the *dodge* value is less than the enemy’s *dodge* difficulty, the attempt to *parry* fails.

    1.  The character takes full damage without the option to block*/*resist.

    2.  Place a *stagger* token on the defending character’s dashboard.

