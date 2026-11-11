# 9. Enemy Turn

The dead do not wait. Each enemy follows the icons on its data card without pause or pity, and the characters are left to choose how to meet what comes. This chapter states how enemies move and attack, and how a character blocks, resists, dodges, or parries an attack.

## 9.1 Overview

Each *round* of an *encounter* begins with the enemies: every enemy model takes a *turn* before any character does, one model at a time in descending order of *threat* {{icon:ast-0026-threat-level}}. The round as a whole, and the order between enemy models that share a threat value, are stated with the encounter turn order (see §7.5, Encounter Turn Order).

Each enemy's behaviour is printed on its *data card* as a row of *behaviour icons*: movement icons (see §9.2) and attack icons (see §9.3). The other values on the data card are described with the card (see §8.2). During its turn the enemy resolves its icons one at a time from left to right, and each icon is resolved in full before the next.

An icon that has no valid *target*, or that cannot be resolved, is skipped, and the next icon to the right is resolved. If the data card bears the *repeat* icon {{icon:ast-0061-repeat-behaviour-or-attack}}, the enemy resolves its whole row of icons the number of times shown, and the target of each icon is determined again each time. The enemy's turn ends when its last icon has been resolved for the last time or when the enemy is killed.

Enemies target only characters; an enemy never targets another enemy (see §8.1). An enemy's health, movement, and attack values are scaled for the number of characters (see §8.3). An enemy that holds a *stagger* or *frostbite* token resolves its icons with the penalty stated for that *condition* (see §8.5).

Invaders do not take their turns with the enemies: an *invader* takes a turn after each character's turn (see §12.2). A *summon* acts as §12.1 describes. A *boss* takes its turns under its own rules (see §16), and a *mimic* under §13.

## 9.2 Enemy Movement

The movement icon {{icon:ast-0033-enemy-movement-composite-symbol}} moves an enemy towards or away from one character, the *target* of the movement. The number printed in the arrow is the number of *nodes* the enemy moves. An arrow that points upwards moves the enemy towards the target; an arrow that points downwards moves it away from the target.

The small icon at the top right of the movement icon names the target. The skull icon names the character who holds the *aggro token*; a living character always holds it (see §7.5, Encounter Turn Order). The nearest-character icon {{icon:ast-0032-target-nearest-character}} names the *nearest character*.

**Nearest character.** The living character at the shortest *range* from the enemy (see §5.4). If two or more characters are tied for nearest, the nearest character is the one of them who holds the aggro token. If none of them holds it, the nearest character is the one of them with the highest *threat*; if they share the highest threat, the players choose.

The target is determined once, when the icon begins to be resolved, and is not determined again as the enemy moves.

### Paths

An enemy *moves* one node at a time, and each node it enters must be a *valid node* (see §5.2). The *terrain* that blocks a move is stated with each kind of terrain (see §5.5). An enemy never leaves the tile and never passes through a *doorway* (see §5.2). An enemy that enters a node at its *node model limit* displaces a model as §5.3 describes.

When the icon moves the enemy towards its target, the enemy follows the shortest path of valid nodes from its own node to the target's node. It stops when it has moved the number of nodes shown or when it stands on the target's node. If two or more such paths are equally short, the players choose which path the enemy follows. If the enemy already stands on the target's node, or if no path of valid nodes leads to that node, the enemy does not move.

When the icon moves the enemy away from its target, each node the enemy enters must be a valid node at a greater range from the target than the node it leaves. If two or more such nodes are open to the enemy, the players choose which node it enters. If no such node is open to the enemy, it stops, and the rest of its movement is lost.

The number of nodes shown is adjusted by scaling for the number of characters (see §8.3) and is reduced while the enemy holds a *frostbite* token (see §8.5, Frostbite). Enemies neither trigger traps nor suffer them (see §5.5, Traps).

### Towards Aggro

The enemy moves the number of nodes shown towards the character who holds the aggro token. An enemy on that character's node does not move.

### Away from Aggro

The enemy moves the number of nodes shown away from the character who holds the aggro token. An enemy with no valid node farther from that character does not move.

### Towards Nearest

The enemy moves the number of nodes shown towards the nearest character. An enemy on that character's node does not move.

### Away from Nearest

The enemy moves the number of nodes shown away from the nearest character. An enemy with no valid node farther from that character does not move.

*Example.* The Knight and the Herald face a Hollow Soldier whose movement icon shows an upward arrow, the number 1, and the nearest-character icon. With two characters in play the Hollow Soldier moves two nodes. The Herald stands two nodes from the Hollow Soldier and the Knight stands three nodes from it, so the Herald is the nearest character. The node between the Hollow Soldier and the Herald holds a *gravestone* and is not a valid node. The Hollow Soldier moves two nodes along the shortest path of valid nodes that leads around the gravestone towards the Herald's node.

*Example.* An enemy's movement icon shows a downward arrow, the number 2, and the nearest-character icon. The Knight and the Assassin each stand one node from the enemy, and the Knight holds the aggro token, so the Knight is the nearest character. Two valid nodes lie at range 2 from the Knight; the players choose one of them, and the enemy moves onto it. One valid node beyond it lies at range 3 from the Knight, and the enemy moves onto that node.

### Push-Move

When the push icon {{icon:ast-0058-push-affected-enemies}} is printed on a movement icon, the movement is a *push-move*. The target of a push-move is determined as for any movement icon, before any character is *pushed*. The enemy then moves one node at a time towards or away from the target's current node, as the arrow shows.

At each node of a push-move, the characters in the enemy's way are pushed as §8.4 describes: the characters on the enemy's node before it moves, and the characters on the node it enters after it moves. A push-move pushes characters only. An enemy model on a node the enemy enters stays there, unless the node model limit displaces it (see §5.3).

A push-move that shows no damage value is not an attack. The characters it pushes are not *hit*, and they cannot *block*, *dodge*, or *parry* it (see §8.4).

### Push-Move with a Damage Value

When the push icon on a movement icon shows a damage value {{icon:ast-0031-push-with-damage-satellite-glyph}}, the push-move includes an attack. Each time the enemy enters a node, it makes a physical attack against every character on that node before those characters are pushed (see §8.4). The damage value is the *attack value* of that attack, and it is scaled as any attack value is (see §8.3).

Each attacked character defends separately, choosing to block or to dodge; the attack cannot be parried (see §9.3, Defence; §9.6). A character who is hit is then pushed. A character who dodges successfully is not hit, is not pushed, and moves as §9.5 describes.

The characters pushed from the enemy's node before it moves are not attacked. A character pushed onto a node that the enemy enters afterwards in the same movement is attacked again on that node.

*Example.* An enemy's movement icon shows an upward arrow, the number 2, the skull icon, and a push icon with the damage value 4. The Warrior holds the aggro token and stands two nodes from the enemy, and the Assassin stands on the node between them. The enemy enters the Assassin's node and attacks the Assassin with attack value 4. The Assassin blocks with a defence total of 3, suffers one damage, and is pushed directly away from the node the enemy has left, onto the Warrior's node. The enemy then enters the Warrior's node and attacks the Warrior and the Assassin separately, each with attack value 4.

## 9.3 Enemy Attacks

The attack icon {{icon:ast-0037-enemy-attack-composite-symbol}} is an attack by the enemy against one or more characters. The crossed swords icon marks an attack that deals *physical damage*, and the magical damage icon {{icon:ast-0042-deal-magical-damage}} marks an attack that deals *magical damage*. The number printed in the centre of the attack icon is the *attack value*.

An enemy's attack value is fixed and is not rolled. It is scaled for the number of characters (see §8.3) and is reduced while the enemy holds a *stagger* token (see §8.5, Stagger).

The *range* of an enemy's attacks is printed on its *data card* (see §8.2) and is counted as §5.4 describes.

The small icons printed around the attack icon modify the attack.

- The skull icon or the nearest-character icon {{icon:ast-0032-target-nearest-character}} names the *target* (see §9.3, Targets).
- The node icon {{icon:ast-0054-node-attack}} makes the attack a *node attack*.
- The push icon {{icon:ast-0058-push-affected-enemies}} makes the attack a *push-attack*: each character *hit* by the attack is *pushed* away from the enemy after the damage is resolved (see §8.4).
- A *condition* icon places the matching condition token on each character hit by the attack (see §8.5).

A *repeat* icon {{icon:ast-0061-repeat-behaviour-or-attack}} on the data card repeats the enemy's whole row of icons, not one attack (see §9.1).

### Targets

An attack marked with the skull icon targets the character who holds the *aggro token*. An attack marked with the nearest-character icon targets the *nearest character*, determined as for movement (see §9.2). The target is determined when the attack icon begins to be resolved.

If the target is not within the attack's range, the attack misses: the icon is skipped and has no effect. No other character is attacked in the target's place.

**Node attack.** An attack that bears the node icon. It targets every character on the node of the character named by its skull icon or nearest-character icon.

If the node targeted by a node attack is not within range, the attack is skipped. Each character on the node is attacked separately: each defends on their own, and the full attack value is applied to each.

### Attack Sequence

An enemy attack is resolved as follows.

1. Determine the target (see §9.3, Targets).
2. Check the range. If the target is not within range, skip the icon.
3. Choose the character's defence (see §9.3, Defence).
4. Resolve the defence (see §9.4; §9.5; §9.6). If a dodge or a parry succeeds, the character is not hit, and the attack on that character ends.
5. Place the damage that the defence has not prevented (see §3.4).
6. If the attack is a push-attack, push the character (see §8.4).
7. Place any condition token the attack carries (see §8.5).

Steps 6 and 7 are resolved even if the character suffered no damage. A character who dies in step 5 is not pushed and receives no token. A node attack resolves steps 3 to 7 for one character at a time, in an order chosen by the players. The attack of a push-move with a damage value follows the same steps from step 3 (see §8.4).

### Defence

When an attack targets a character, the character's player must choose one defence before any dice are rolled. The choice cannot be changed once it is made. The defences are as follows.

- Block or resist: the character *blocks* an attack that deals physical damage and *resists* an attack that deals magical damage (see §9.4).
- Dodge: the character attempts to *dodge* the attack (see §9.5).
- Parry: the character attempts to *parry* the attack, if a parry is permitted (see §9.6).

A character is hit by an attack unless the dodge or the parry succeeds, even if the attack deals no damage (see §8.1). Conditions and pushes apply only to a character who is hit. Damage suffered is placed as *damage cubes* on the character's *endurance bar* (see §3.4; §7.2). An *embered* character reduces the damage of an attack as §7.3 describes.

The attacks of an *invader*, a *mimic*, or a *boss* are defended under §9.4, §9.5, and §9.6, except where their own rules differ (see §12.2; §13; §16.3). A character's attack on another character in a player versus player (PvP) encounter is defended as §20.4 describes.

*Example.* An enemy's attack icon shows the crossed swords icon, attack value 4, and the skull icon, and the enemy's range is 1. The Knight holds the aggro token and stands two nodes from the enemy. The Herald stands on a node adjacent to the enemy. The attack targets the Knight, who is not within range, so the attack is skipped. The Herald is not attacked.

*Example.* An enemy's attack icon shows attack value 2, the nearest-character icon, and the node icon, and the enemy's range is 3. The Assassin and the Warrior share a node two nodes from the enemy, and the Knight stands three nodes from it. The Assassin and the Warrior are tied for nearest. The Warrior holds the aggro token, so the Warrior is the nearest character and the attack targets the Warrior's node. The Warrior blocks and the Assassin dodges, each against attack value 2. The Knight is not attacked.

## 9.4 Block and Resist

A character *blocks* an attack that deals physical damage with the dice shown beside the block icon {{icon:ast-0048-block}} on their *equipped* cards. A character *resists* an attack that deals magical damage with the dice shown beside the resist icon {{icon:ast-0050-resist}} on their equipped cards (see §4.1, Card Anatomy). Blocking and resisting cost no stamina. The roll is resolved as follows.

1. Gather the block dice, against physical damage, or the resist dice, against magical damage, shown on every equipped card: the *armour* card, the card in each *weapon slot*, and every *upgrade card* attached to them (see §3.2; §4.2).
2. Roll the dice.
3. The character may flip the *luck* token to reroll any or all of the dice (see §3.5, Luck).
4. Add together the two highest results. If one die was rolled, its result is the sum. If no dice were rolled, the sum is zero.
5. Apply to the sum every fixed modifier printed with the block or resist dice of the equipped cards. The result is the *defence total*.
6. Subtract the defence total from the *attack value*. The character suffers the difference as damage, to a minimum of zero (see §3.4).
7. Resolve any *push* (see §8.4), then place any *condition* token the attack carries (see §8.5), even if the character suffered no damage.

Dice beyond the two highest are ignored. A fixed modifier is applied after the two highest results are added, whether or not a die of its card is among the two highest. A defence total of less than zero is treated as zero. A condition token on the character may reduce the defence total (see §8.5).

Cards in the *back-up slot* and in the *inventory* provide no dice (see §3.2). A *spell* stored in a *catalyst* provides no dice (see §4.3).

A character who blocks or resists is *hit* by the attack, whatever the defence total (see §8.1). A defence total that equals or exceeds the attack value prevents all of the damage and nothing else.

*Example.* A Hollow Soldier attacks the Knight with attack value 4 and physical damage. The Knight's armour shows two black block dice, and the shield in the Knight's left weapon slot shows one blue block die with a +1 modifier. The Knight rolls the three dice and they show 1, 2, and 2. The two highest results add to 4, and the +1 modifier makes the defence total 5. The Knight suffers no damage and is hit by the attack all the same.

*Example.* An enemy attacks the Herald with attack value 3 and magical damage. The Herald's equipped cards show one blue resist die between them and no modifier. The Herald rolls the die and it shows 2, so the defence total is 2. The Herald suffers one damage and places one damage cube on the endurance bar.

## 9.5 Dodge

A character targeted by an attack may attempt to *dodge* it in place of a *block* or a *resist*. Only an attack that targets the character may be dodged; a *push-move* that shows no damage value is not an attack (see §9.2, Push-Move). A dodge is rolled with green dice (see §2.7), one for each die shown beside the dodge icon {{icon:ast-0062-dodge}} on the character's *equipped* cards.

**Dodge difficulty.** The number of dodge icons a dodge roll must equal or exceed. The dodge difficulty of an enemy's attacks is printed on its *data card* (see §8.2), that of a *boss*'s attack on its *behaviour card* (see §16.3), and that of a trap on its *trap token* (see §5.5, Traps).

A dodge is resolved as follows.

1. Place one *stamina cube* on the character's *endurance bar* to pay one stamina (see §3.4).
2. Gather one green die for each dodge die shown on the character's equipped cards (see §3.2).
3. The character may pay two further stamina to add one green die. This may be done once for each dodge, and no dodge is rolled with more than four dice.
4. If the dodge difficulty is zero, the dodge succeeds and no dice are rolled. Otherwise roll the dice.
5. The character may flip the *luck* token to reroll any or all of the dice (see §3.5, Luck).
6. Count the dodge icons rolled. If the count equals or exceeds the dodge difficulty, the dodge succeeds. Otherwise the dodge fails.

A character may attempt a dodge only if the stamina cube of step 1 has an empty space on the endurance bar, and may add the die of step 3 only if both further cubes have empty spaces (see §3.4). A character whose equipped cards show no dodge dice may still attempt a dodge. If no dice are rolled, the count is zero, and the dodge fails unless the dodge difficulty is zero. A *condition* token on the character may reduce the count (see §8.5).

### Successful Dodge

When a dodge succeeds, the attack does not hit the character (see §8.1). The character suffers no damage, receives no condition token, and is not *pushed*. The character must then move to an *adjacent node* that is a *valid node*, chosen by the character's player (see §5.2). If no valid node exists, the character stays on their node.

The movement that follows a dodge is not a *move*, and it costs no stamina beyond the cost of the dodge. It destroys an intact *barrel* on the node entered (see §5.5, Barrels) and turns a face-down trap token on that node face up (see §5.5, Traps). If the node entered is at its *node model limit*, a model is displaced as §5.3 describes.

### Failed Dodge

When a dodge fails, the character is *hit*. The character rolls only the block or resist dice, as the damage type requires, of their *armour* card and of the *upgrade cards* attached to it. The dice of weapons, *shields*, and *spells* are not rolled. The roll is resolved from step 2 of the block and resist procedure (see §9.4): the two highest results and the fixed modifiers of the dice rolled form the *defence total*, and conditions and pushes apply.

The stamina paid for a failed dodge is not returned. A character with no armour card, or whose armour provides no dice of the kind required, suffers the full *attack value*.

### Traps

A trap is dodged under the rules of this section, against the dodge difficulty shown on its trap token (see §5.5, Traps). Trap damage cannot be blocked or resisted. A character who fails to dodge a trap rolls no dice and suffers the damage shown on the token.

*Example.* An enemy attacks the Assassin with attack value 3 and physical damage, and the enemy's dodge difficulty is 2. The Assassin's equipped cards show two dodge dice. The Assassin pays one stamina, pays two further stamina for a third green die, and rolls three dice: two dodge icons and one blank. Two equals the dodge difficulty, so the dodge succeeds. The Assassin suffers no damage and moves to an adjacent valid node.

*Example.* An enemy attacks the Warrior with attack value 4 and physical damage, and the enemy's dodge difficulty is 1. The Warrior's equipped cards show one dodge die. The Warrior pays one stamina and rolls one green die, which shows a blank, so the dodge fails. The Warrior's armour shows one black block die, and the shield's two blue block dice are not rolled. The black die shows 1, so the defence total is 1 and the Warrior suffers three damage.

## 9.6 Parry and Riposte

A character targeted by an attack may attempt to *parry* it in place of a *block*, a *resist*, or a *dodge*. A parry is permitted only if both of the following are true.

- A *shield* is equipped in one of the character's *weapon slots* (see §3.2; §4.1).
- The attacker is on the character's node.

The shield may be in either weapon slot. A character who wields a weapon *two-handed* has no shield equipped and cannot parry (see §10.4).

The following attacks cannot be parried.

- A *push-attack* (see §9.3).
- The attack made by a *push-move* that shows a damage value (see §9.2, Push-Move with a Damage Value).
- A *node attack* (see §9.3, Targets).
- An attack by a *boss*, except where §15.6 allows.

A parry is resolved as follows.

1. Place one *stamina cube* on the character's *endurance bar* to pay one stamina (see §3.4).
2. Gather one green die for each dodge die shown on the character's *equipped* cards (see §3.2). No further die may be added.
3. Roll the dice.
4. The character may flip the *luck* token to reroll any or all of the dice (see §3.5, Luck).
5. Count the dodge icons rolled. If the count equals or exceeds the attack's *dodge difficulty*, the parry succeeds. Otherwise the parry fails.

A character may attempt a parry only if the stamina cube of step 1 has an empty space on the endurance bar (see §3.4). If no dice are rolled, the count is zero. A *condition* token on the character may reduce the count (see §8.5).

### Successful Parry

When a parry succeeds, the attack misses. The character is not *hit*: the character suffers no damage, receives no condition token, and is not *pushed*. A *stagger* token {{icon:ast-0066-stagger}} is placed on the attacker, which is staggered (see §8.5, Stagger). The character may then make a *riposte* at once.

### Riposte

A riposte is one attack against the attacker, made with one *attack option* of the *weapon* equipped in the character's other weapon slot, the slot that does not hold the shield used for the parry. A *spell* cannot be used for a riposte, whether it is equipped in that slot or stored in a *catalyst* there (see §4.3). The character pays the stamina cost of the attack option and resolves the attack as §10.3 describes. The attacker's stagger token is in place before the riposte is resolved. An enemy cannot dodge or parry a riposte.

A riposte is made during the attacker's *turn*. It is not the character's *Attack* major action, and it does not count against the attacks the character makes in their own turn (see §10.3). In every other respect a riposte is an attack: the character may flip the luck token to reroll its dice, and the icons of the attack option apply. A riposte against a character in a PvP encounter is defended as §20.4 describes.

A riposte is optional. No riposte is made if the other weapon slot holds no weapon with an attack option, if the character cannot pay the stamina cost, or if no attack option of that weapon may target the character's own node, as with the *shaft* icon (see §10.3, Shaft). The parry succeeds all the same, and the attacker is staggered.

If the riposte kills the attacker, the attacker's turn ends at once, and its remaining icons are not resolved (see §9.1).

### Failed Parry

When a parry fails, the character is hit and suffers damage equal to the full *attack value*. No block or resist dice are rolled. Any condition token the attack carries is placed on the character (see §8.5). A stagger token is then placed on the character, who is staggered (see §8.5, Stagger); the stamina paid for the parry is not returned.

*Example.* An enemy on the Knight's node attacks the Knight with attack value 4 and physical damage, and the enemy's dodge difficulty is 1. The Knight has a shield in the left weapon slot and a sword in the right weapon slot. The Knight pays one stamina and rolls the one dodge die shown on the Knight's armour, which shows a dodge icon. One equals the dodge difficulty, so the parry succeeds: the Knight suffers no damage, and a stagger token is placed on the enemy. The Knight ripostes with the sword's attack option that costs one stamina, pays that stamina, and rolls an attack value of 4. The stagger token reduces the enemy's block from 1 to 0, so four *wound tokens* are placed on the enemy.

*Example.* An enemy on the Herald's node attacks the Herald with attack value 4 and physical damage, and the enemy's dodge difficulty is 2. The Herald has a shield in the left weapon slot and a spear in the right weapon slot. The Herald pays one stamina and rolls two dodge dice: one dodge icon and one blank. One is less than 2, so the parry fails. The Herald rolls no block dice, suffers four damage, and is staggered.
