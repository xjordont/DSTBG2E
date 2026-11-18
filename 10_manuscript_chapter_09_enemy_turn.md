# 9. Enemy Turn

## 9.1 Overview

Each round of an encounter begins with every enemy model taking a turn, highest *threat* first (see §7.5), before the characters take theirs.

Non-boss enemies follow the behaviour icons on their *data cards*. Bosses follow the icons on their *behaviour cards* instead. All behaviour icons are resolved from left to right. An enemy's behaviour can be as simple as one attack or can hold several moves and attacks. If an icon has no target or cannot otherwise be carried out, it is skipped and the next icon to the right is resolved. If the data card shows the *repeat* icon {{icon:ast-0061-repeat-behaviour-or-attack}}, the enemy resolves all of its icons the number of times shown. An enemy's turn ends once all of its icons have been resolved.

## 9.2 Enemy Movement

The movement icon {{icon:ast-0033-enemy-movement-composite-symbol}} shows how an enemy moves. Smaller icons around it modify the movement, so that different enemies move towards or away from characters in different patterns and at different speeds.

- An arrow pointing up moves the enemy towards the target character. An arrow pointing down moves it away from the target character.
- The number in the arrow is how many *nodes* the enemy moves in that direction.
- The small icon at the top right gives the target character: a skull for the character with the *aggro* token, a ring {{icon:ast-0032-target-nearest-character}} for the nearest character.

An enemy told to move towards a character whose node it already shares does not move. An enemy told to move away from a character who is already at the greatest distance does not move. When two nodes would take an enemy equally close to where it is going, the players choose which node it enters. The nearest character is found at the start of a movement, not at each node.

### Towards Aggro

The enemy moves the number of nodes shown closer to the character with the aggro token.

### Away from Aggro

The enemy moves the number of nodes shown farther from the character with the aggro token.

### Towards Nearest

The enemy moves the number of nodes shown closer to the nearest character. If two or more characters are tied for nearest, the enemy moves towards the one with the aggro token. If the character with the aggro token is not among them, it moves towards the one with the higher *threat*.

### Away from Nearest

The enemy moves the number of nodes shown farther from the nearest character. If two or more characters are tied for nearest, the enemy moves away from the one with the aggro token or, if that character is not among them, from the one with the higher threat.

### Push-Move

If the movement icon includes the *push* icon {{icon:ast-0058-push-affected-enemies}}, the movement is a *push-move* and pushes characters out of the enemy's way (see §8.4).

If the push icon includes a number {{icon:ast-0031-push-with-damage-satellite-glyph}}, the push-move is also a physical attack with that number as its attack value. It attacks each character it pushes, whether from the enemy's own node or from a node the enemy enters. A character is attacked once for that push-move, however many nodes the movement covers. The character defends before being pushed, and a successful *dodge* avoids the push.

## 9.3 Enemy Attacks

The attack icon {{icon:ast-0037-enemy-attack-composite-symbol}} shows the attack an enemy makes. Crossed swords mark a physical attack and a white circle {{icon:ast-0042-deal-magical-damage}} marks a magical attack. The number in the centre of the icon is the attack value. Smaller icons beside it modify the attack.

- A skull or a ring gives the target, as it does for movement (see §9.2). If the target is beyond the enemy's *range*, the attack is skipped.
- The node icon {{icon:ast-0054-node-attack}} makes a node attack, which targets every character on the target's *node*. Each defends separately.
- The *push* icon makes a *push-attack* (see §8.4).
- A *condition* icon marks each character hit with the matching condition token (see §8.5).

A character attacked by an enemy must decide how to defend: *block* or *resist*, *dodge*, or *parry*. The enemy's attack value is fixed, so the character's dice decide the result. Only an attack with a damage value can be dodged or parried.

When a character is hit, place the damage, then resolve the push, then place the condition token.

## 9.4 Block and Resist

- *Block* dice {{icon:ast-0048-block}} are used against physical attacks. *Resist* dice {{icon:ast-0050-resist}} are used against magical attacks.
- Roll every die of that type shown on the character's *equipped* cards.
- Keep the two highest results and add any fixed modifiers. Further dice are ignored.
- The damage is the attack value less that sum. The character places that many damage cubes on the *endurance bar* (see §3.4).
- If the sum equals or exceeds the attack value, the character takes no damage.

## 9.5 Dodge

- A *dodge* costs one *stamina*.
- Roll the dodge dice {{icon:ast-0062-dodge}} shown on the character's *equipped* cards against the attacker's *dodge difficulty*.
- Before rolling, the character may spend two more stamina, three in all, to add one die. A dodge is never rolled with more than four dice.
- Against a dodge difficulty of zero the dodge succeeds without a roll and needs no dodge dice.

If the dodge result equals or exceeds the dodge difficulty, the attack does not hit.

- No damage is taken.
- No *condition* is applied.
- No *push* is applied.
- The character must move to an adjacent *node* of the player's choice.

If the dodge result is less than the dodge difficulty, the attack hits.

- The character rolls only the *block* or *resist* dice of the armour card and its *upgrades*. The dice of weapons, shields and *spells* are left out.
- Keep the two highest results and work out the damage as for a block or resist (see §9.4).

*Example.* A Hollow Soldier with a dodge difficulty of 1 attacks the Assassin for 5. The Assassin's armour shows two dodge dice and one block die. The Assassin places one stamina cube and rolls a result of 1 on the two dodge dice: the attack does not hit, and the Assassin steps to an adjacent node. On a result of 0 the Assassin rolls the armour's one block die and suffers 5 damage less the result.

## 9.6 Parry and Riposte

A character may *parry* an attack only when all of these hold.

- The character has a weapon or shield in the left weapon slot. A character wielding a weapon *two-handed* cannot parry.
- The attacker is on the character's *node*.
- The attacker is not a boss.
- The attack is not a *push-attack*, a *push-move*, an *area-of-effect* attack or a node attack.

A parry is paid for and rolled as a *dodge* (see §9.5).

If the result equals or exceeds the attacker's *dodge difficulty*, the attack is parried.

- No damage is taken.
- No *condition* is applied.
- Place a *stagger* token {{icon:ast-0066-stagger}} on the attacker's base.
- The character may at once make a *riposte* out of turn: one attack option of the weapon in the right weapon slot against that attacker, paying its *stamina* cost. The attacker is already staggered when the riposte is rolled.

If the result is less than the dodge difficulty, the parry fails.

- The character suffers the full attack value as damage. No dice are rolled.
- Place a stagger token on the character's dashboard.

*Example.* A Hollow Soldier with a dodge difficulty of 1 attacks the Knight for 5 from the Knight's own node. The Knight carries a shield in the left weapon slot and a sword in the right. The Knight places one stamina cube and rolls a dodge result of 1: the attack is parried and the Hollow Soldier is staggered. The Knight then pays one stamina for an attack option of the sword and ripostes. On a result of 0 the Knight suffers 5 damage and is staggered.
