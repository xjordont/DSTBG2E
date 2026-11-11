# 8. Combat Basics

Every fight turns on the same few questions: who is struck, how hard, and what the blow leaves behind. This chapter sets out the terms on which all combat rests: the target and the hit, the enemy data card, the scaling of enemies to the party, the push, and the conditions that linger after a blow has landed.

## 8.1 Target versus Hit

**Target.** The model at which an attack is directed.

When a model attacks, the model that must defend against the attack is the attack's *target*. An attack has one target unless its icons give it more. Some attacks target every opposing model on one *node* (see §9.3; §10.3, Area-of-Effect), and some *boss* attacks target every character on several nodes (see §16.3).

A character targets hostile models: enemies, bosses, *invaders*, *mimics*, and *crystal lizards* (see §10.3). A character targets another character only in a player versus player (PvP) *encounter* (see §20). An enemy never targets another enemy. The targeting of *phantoms* is stated with their rules (see §12).

**Hit.** An attack hits its target when the target is within the attack's *range* (see §5.4) and does not avoid the attack by a successful *dodge* (see §9.5) or a successful *parry* (see §9.6).

A hit does not depend on damage. An attack whose damage is reduced to zero by *block* or *resist* still *hits* its target (see §9.4; §10.3).

A target that is out of range, or that dodges or parries the attack, is not hit. An attack has no effect on a target it does not hit: it deals no damage, does not *push* the target, and places no *condition* token on it.

A push (see §8.4) and a condition (see §8.5) carried by an attack apply only to a model that the attack hits. They apply to every model the attack hits, whether or not the attack dealt damage to it.

*Example.* An enemy attack with an *attack value* of 4 bears the push icon and targets the Knight and the Herald, who share a node within its range. The Knight blocks and rolls a *defence total* of 4, so the Knight suffers no damage; the Knight is hit all the same and is pushed. The Herald dodges successfully, is not hit, and is not pushed.

## 8.2 Enemy Data Cards

Each kind of enemy has a *data card* (see §2.2). The data card holds everything needed to resolve that enemy's *turn* and to resolve a character's attack against it. An enemy data card shows the following.

- The name identifies the kind of enemy.
- The *threat* value {{icon:ast-0026-threat-level}} fixes the order in which enemies take their turns (see §7.5, Encounter Turn Order).
- The attack *range* {{icon:ast-0060-attack-range}} is the greatest range at which the enemy's attacks reach a *target* (see §5.4; §9.3).
- The *dodge difficulty* {{icon:ast-0062-dodge}} is the total that a character's *dodge* roll must equal or exceed to avoid the enemy's attacks (see §9.5).
- The *block* and *resist* values {{icon:ast-0028-block-resist-shield}} reduce the damage of physical and magical attacks against the enemy (see §10.3).
- The *behaviour icons* are the enemy's movement icons {{icon:ast-0033-enemy-movement-composite-symbol}} and attack icons {{icon:ast-0037-enemy-attack-composite-symbol}}, resolved from left to right during its turn (see §9.1).
- The *base health* {{icon:ast-0029-starting-health}} is the enemy's health before *enemy scaling* (see §8.3).
- The enemy icon is the picture by which *encounter cards* show the enemy (see §2.6).
- The set symbol shows the set that supplies the enemy (see §2.2).

Smaller icons printed around a behaviour icon modify it, as follows.

- The skull icon directs the movement or attack at the character who holds the *aggro token* (see §9.2; §9.3).
- The nearest-character icon {{icon:ast-0032-target-nearest-character}} directs the movement or attack at the nearest character (see §9.2; §9.3).
- The *node* icon makes an attack target every character on the target's node (see §9.3).
- The *push* icon makes a movement a *push-move* and an attack a *push-attack* (see §8.4).
- A push icon that carries a number {{icon:ast-0031-push-with-damage-satellite-glyph}} makes a push-move deal that damage (see §8.4).
- The *repeat* icon {{icon:ast-0061-repeat-behaviour-or-attack}} modifies no single icon: it shows the number of times the enemy's whole row of behaviour icons is resolved (see §9.1).
- A *condition* icon places that condition on each model the attack *hits* (see §8.5).

The attack icon itself shows whether the attack deals *physical damage* or *magical damage* {{icon:ast-0042-deal-magical-damage}} (see §9.3).

A *boss* data card shows a *behaviour deck* size {{icon:ast-0027-behaviour-deck-size}} in place of behaviour icons and adds a *heat-up* point {{icon:ast-0030-heat-up-point}} (see §15.4). The data cards of *phantoms* and *mimics* are described with those models (see §12; §13).

**Scaled health.** An enemy's base health plus the increase that enemy scaling gives for the number of characters (see §8.3).

Damage to an enemy is recorded with *wound tokens*. When an enemy suffers damage, place wound tokens with a total value equal to that damage on the base of the enemy model (see §10.3). Wound tokens stay on the model until the enemy is killed or the *encounter* ends.

When the total value of the wound tokens on an enemy model equals or exceeds its *scaled health*, the enemy is killed. Remove the model and its wound tokens from the tile at once. Damage beyond the enemy's scaled health has no further effect.

A boss, a phantom, and a mimic record their health on a *health dial* in place of wound tokens (see §15.4).

*Example.* The Knight, the Herald, and the Assassin fight a Hollow Soldier whose data card shows a base health of 1. With three characters its scaled health is 3. The Knight's attack deals two damage, and two wound tokens of value 1 are placed on the Hollow Soldier's base. The Herald's attack deals one damage. The wound tokens now total 3, so the Hollow Soldier is killed, and its model and wound tokens are removed from the tile.

## 8.3 Enemy Scaling

*Enemy scaling* matches the enemies to the size of the party. The number of characters is the number taking part in the game (see §6.1). It does not change when a character dies: a dead character and a *lost* character still count. It changes only when a player joins or leaves the game (see §18.4). Each enemy is scaled for that number when its model is placed (see §7.5, Encounter Start).

| Characters | Enemy health | Enemy movement | Enemy *attack value* |
|---|---|---|---|
| 1 | *Base health* | No change | No change |
| 2 | Base health + 1 | 1 becomes 2 | No change |
| 3 | Base health + 2 | 1 becomes 2 | No change |
| 4 | Base health + 4 | 1 becomes 2 | +1 |

An enemy's *scaled health* is its base health plus the increase shown in the table (see §8.2).

With two or more characters, every movement icon on an enemy's *data card* that shows a value of 1 is resolved with a value of 2. A *push-move* is scaled in the same way (see §8.4). A movement icon that shows a value of 2 or more is not changed.

With four characters, every attack value on an enemy's data card is increased by one. The increase applies to each attack icon and to the damage value of a push-move (see §8.4).

Every enemy is scaled, with four exceptions. A *boss*, a *mimic*, a *phantom*, and a *crystal lizard* are never scaled (see §15.4; §13; §12; §14).

In campaign play, the *bonfire ascetic* further increases the health of every enemy that is subject to enemy scaling (see §18.7).

*Example.* A Hollow Soldier's data card shows a base health of 1, a movement value of 1, and an attack value of 4. Against the Knight alone it has a health of 1, moves one *node*, and attacks with a value of 4. Against the Knight and the Herald its scaled health is 2 and it moves two nodes. Against the Knight, the Herald, and the Assassin its scaled health is 3. Against the Knight, the Herald, the Assassin, and the Warrior its scaled health is 5 and its attack value is 5. The Warrior dies during the *encounter*, and the enemies of the next encounter are still scaled for four characters.

## 8.4 Pushing

**Push.** Forced movement of a model from its *node* to an *adjacent node*.

A *push* forces a model from its node to a *valid node* (see §5.2). A push is not a *move*, and it costs no stamina. A model is pushed from the node it occupies when the push is resolved. A model is pushed for one of the following reasons.

- A *push-attack* *hits* the model.
- A *push-move* begins on the model's node or enters it.
- A fourth non-boss model enters the model's node, and the *node model limit* displaces the model (see §5.3).
- A *boss* model moves onto the node of another boss model (see §17.1).
- A rule of a boss pushes the model, as a *leap* does (see §16.2, Leap; §17).

A model is pushed only into a valid node. A node containing a *gravestone*, a *chest*, or a *pillar token* is not a valid node for a push, and a model pushed into a node containing an intact *barrel* destroys the barrel (see §5.5). A character pushed onto a node that holds a face-down *trap token* triggers the trap (see §5.5, Traps). A model pushed into a node at its node model limit displaces a model already on that node (see §5.3).

If no valid node exists for a push, the push does not happen and the model stays on its node. Every other effect of the attack or movement that caused the push is still resolved.

**Push-attack.** An attack that bears the push icon.

When a push-attack {{icon:ast-0058-push-affected-enemies}} hits a model, the model is pushed after the attack's damage has been resolved (see §8.1). The model is pushed whether or not the attack dealt damage. A model that the attack does not hit is not pushed.

A push-attack pushes the model directly away from the attacker. A node is farther from the attacker when its *range* from the attacker's node is greater (see §5.4). The model is pushed into the valid node most directly opposite the attacker's node, chosen from the adjacent nodes that are farther from the attacker than the model's own node. If two or more such nodes are equally opposite the attacker, the players choose one of them.

If no valid node is farther from the attacker than the model's own node, the model is not pushed. If the attacker shares the model's node, every adjacent node is farther from the attacker, and the players choose any valid node.

**Push-move.** An enemy or boss movement that bears the push icon.

An enemy resolves a push-move one node at a time (see §9.2). For each node of the movement, the following steps are resolved in order.

1. Push each character on the enemy's node to a valid node chosen by the players.
2. Move the enemy one node, as its movement icon directs.
3. If the push icon carries a damage value {{icon:ast-0031-push-with-damage-satellite-glyph}}, resolve a physical attack with that *attack value* against each character on the node the enemy has entered, one character at a time.
4. Push each character hit in step 3. If the push icon carries no damage value, push each character on the node the enemy has entered.

The characters pushed in step 1 are not attacked and suffer no damage. A character pushed in step 4 is pushed directly away from the node the enemy has left, as for a push-attack made from that node.

A push-move without a damage value is not an attack: a character cannot *dodge*, *block*, or *resist* it. The attack of a push-move with a damage value is defended by a block or a dodge, as any other enemy attack is (see §9.4; §9.5). No *parry* of it is permitted (see §9.6). A character who blocks that attack is hit and is pushed whether or not damage is dealt. A character who dodges it is not hit and is not pushed.

A boss resolves a push-move in the same way, with the differences stated for boss movement (see §16.2). When a boss pushes a character off the boss's own node, the boss's arcs limit the nodes to which the character is pushed (see §15.6).

A push caused by the node model limit, or by a boss model moving onto the node of another boss model, sends the displaced model to any valid node chosen by the players. The model to be displaced is chosen as §5.3 and §17.1 state.

A boss model cannot be pushed by a character's attack. The only push that affects a boss model is the push caused by another boss model moving onto its node (see §17.1).

In a PvP *encounter*, a push-attack pushes a character it hits (see §20.5).

*Example.* An enemy, the Knight, and a gravestone occupy three nodes in a straight line, with the Knight in the middle. The enemy hits the Knight with a push-attack. The node most directly opposite the enemy holds the gravestone and is not a valid node. The two nodes on either side of the gravestone are valid nodes, are farther from the enemy than the Knight's node, and are equally opposite the enemy, so the players choose one of them and the Knight is pushed there.

*Example.* The Herald stands on a corner node, and an enemy on the diagonally adjacent node hits the Herald with a push-attack. The two other nodes adjacent to the Herald are no farther from the enemy than the corner node is, so the Herald is not pushed. The attack's damage is resolved in full.

*Example.* The Knight, the Herald, and the Assassin are in play, so an enemy's push-move with a movement value of 1 is resolved as two nodes. Its push icon carries a damage value of 5. The Assassin shares the enemy's node: the players push the Assassin to a valid node, and the Assassin suffers no damage. The enemy moves onto the Knight's node, and the Knight is attacked with an attack value of 5. The Knight blocks with a *defence total* of 3, suffers two damage, and is pushed directly away from the node the enemy has left. The enemy then moves its second node, which holds no character, and no model is pushed.

## 8.5 Conditions

**Condition.** A lasting effect marked by a condition token on a model.

A *condition* is one of six lasting effects: *bleed* {{icon:ast-0063-bleed}}, *poison* {{icon:ast-0065-poison}}, *frostbite* {{icon:ast-0064-frostbite}}, *stagger* {{icon:ast-0066-stagger}}, *calamity*, and *corrosion*. Each condition is marked by a condition token of its own kind (see §2.8). Any model may hold condition tokens: a character, an enemy, a *boss*, or a *phantom*.

When an attack that bears a condition icon *hits* a model, place the matching condition token on that model (see §8.1). The token is placed after the attack's damage and any *push* have been resolved, and it is placed whether or not the attack dealt damage. Some rules place a condition token without an attack; the token then has the same effect.

A model holds at most one token of each condition, and it may hold tokens of different conditions at the same time. When a token of a condition is to be placed on a model that already holds a token of that condition, the token is not placed and has no effect. Bleed and poison are exceptions, each stated under its own heading below.

Damage dealt by a condition is recorded as any other damage is: with *damage cubes* for a character (see §3.4), with *wound tokens* for an enemy (see §8.2), and on the *health dial* for a boss, a phantom, or a *mimic* (see §15.4). A value reduced by a condition cannot fall below zero. When the *aggro token* is assigned, bleed damage counts as damage inflicted by the character whose attack triggered it, and poison damage counts for no character (see §7.5, Encounter Turn Order; §16.4).

Each condition lasts until the rule under its heading removes it. The end of the affected model's own *turn* is the only moment at which a turn acts on a condition: poison is then resolved, and frostbite and stagger tokens are then removed. Where a token is removed at the end of a model's next complete turn, a token placed during that model's own turn is not removed at the end of that turn; it is removed at the end of the model's following turn. Every condition token still in play is removed when the *encounter* ends (see §7.5, Encounter Recovery).

In a PvP encounter, conditions apply between characters (see §20.5).

### Bleed

A model holds at most one bleed token, and the token alone has no effect. When a bleed token is to be placed on a model that already holds one, the token is not placed. The model suffers three damage at once instead, and its bleed token is removed.

Bleed damage is not an attack: it is not reduced by *block* or *resist*, and a character cannot *dodge* it. A bleed token is not removed at the end of any turn. It stays on the model until a second token triggers it or the encounter ends.

*Example.* Four characters are in play, so a Hollow Soldier has a *scaled health* of 5. The Assassin hits it with an *attack option* that bears the bleed icon and deals two damage: two wound tokens of value 1 and a bleed token are placed on it. In the next *round* the Assassin hits it again with the same attack option, and the Hollow Soldier's block reduces the attack's damage to zero. The second bleed token is not placed. The Hollow Soldier suffers three damage, which its block does not reduce, and its bleed token is removed. Its wound tokens now total 5, so the Hollow Soldier is killed.

### Poison

A model may hold any number of poison tokens: each attack that bears the poison icon and hits the model places one more. At the end of each of its turns, a model that holds poison tokens suffers one damage for each poison token it holds and then removes all of them. Poison damage is not an attack: it is not reduced by block or resist, and a character cannot dodge it.

*Example.* During the enemies' turns the Herald is hit by three attacks that bear the poison icon and holds three poison tokens. At the end of the Herald's next turn, the Herald suffers three damage, places three damage cubes on the *endurance bar*, and removes all three poison tokens.

### Frostbite

A character with a frostbite token cannot recover stamina by any means. The character does not recover one stamina at the start of their turn and cannot take the *Rest* *major action* (see §10.1). An enemy, boss, or phantom with a frostbite token reduces the value of each of its movement icons by one, after *enemy scaling* has been applied (see §8.3; §9.2).

A frostbite token is removed at the end of the affected model's next complete turn.

*Example.* An enemy attack that bears the frostbite icon hits the Herald during the enemies' turns, and a frostbite token is placed on the Herald. At the start of the Herald's turn the Herald recovers no stamina, and the Herald cannot take the Rest major action during that turn. At the end of that turn the frostbite token is removed.

### Stagger

A character with a stagger token subtracts one from the total of each attack roll and of each block, resist, and dodge roll that the character makes. An enemy, boss, or phantom with a stagger token reduces each of its *attack values*, its block and resist values, and its *dodge difficulty* by one.

A stagger token is removed at the end of the affected model's next complete turn.

Stagger is placed by an attack that bears the stagger icon, by stamina overflow (see §10.1), and by a *parry* (see §9.6).

*Example.* During a Hollow Soldier's turn the Knight parries its attack, and a stagger token is placed on the Hollow Soldier. The token was placed during the Hollow Soldier's own turn, so it is not removed at the end of that turn. During the characters' turns the Hollow Soldier's block of 1 is reduced to zero. On the Hollow Soldier's next turn its attack value is 3 in place of 4 and its dodge difficulty is reduced by one, and the stagger token is removed at the end of that turn.

### Calamity

Calamity is a condition of the Black Dragon Kalameet expansion (see §17.8). A model with a calamity token subtracts one from the total of each block, resist, and dodge roll that it makes. A calamity token is not removed at the end of any turn or when the model suffers damage. It is removed only when the encounter ends.

### Corrosion

Corrosion is a condition of the Gaping Dragon expansion (see §17.10). A model with a corrosion token subtracts one from the total of each block roll that it makes. A corrosion token is not removed at the end of any turn. It is removed when the affected model next suffers damage, after that damage has been recorded.
