# 8. Combat Basics

## 8.1 Target versus Hit

When a character or an enemy attacks, the model defending against the attack is the attack's target. An attack has a single target unless an icon lets it target every model on a *node* or on several nodes. Characters target other characters only in a player versus player (PvP) encounter (see §20). Enemies never target other enemies.

A model is hit by an attack so long as the attack was in *range* and the model did not *dodge* or *parry* it. An attack that deals zero damage still hits. A model that is not hit is not *pushed* and receives no *condition* token.

## 8.2 Enemy Data Cards

Each enemy type has a *data card*. It gives what is needed to take that enemy's turn and to resolve a character's attack against it:

1. Name.
2. *Threat* {{icon:ast-0026-threat-level}}. Enemies with higher threat take their turn first.
3. Attack *range* {{icon:ast-0060-attack-range}}. The maximum range at which the enemy can attack a character.
4. *Dodge difficulty* {{icon:ast-0062-dodge}}. How hard the enemy's attacks are to *dodge*.
5. *Block* and *resist* values {{icon:ast-0028-block-resist-shield}}. Block reduces the damage the enemy suffers from physical attacks; resist reduces the damage it suffers from magical attacks.
6. Behaviour icons. The movement icons {{icon:ast-0033-enemy-movement-composite-symbol}} and attack icons {{icon:ast-0037-enemy-attack-composite-symbol}} that determine what the enemy does during its turn.
7. Base health {{icon:ast-0029-starting-health}}. The damage the enemy can suffer before it is killed in a game with one character.
8. Enemy icon.
9. Set symbol.

When an enemy suffers damage, place one wound token on the base of its model for each point of damage not prevented by its block or resist. The enemy dies when its wound tokens equal its scaled health (see §8.3) and is removed from the tile.

The Phalanx of Painted World of Ariamis has no model of its own. Three Phalanx Hollow models on one node stand for it, and it moves, attacks and takes wounds as one enemy.

## 8.3 Scaling

Enemies grow stronger with the number of characters in the game. Dead characters are counted.

| Characters | Sparks | Enemy health | Enemy attack damage |
|---|---|---|---|
| 1 | 4 | as printed | as printed |
| 2 | 3 | +2 | +1 |
| 3 | 2 | +4 | +1 |
| 4 | 1 | +6 | +1 |

- The *sparks* are those the party starts with (see §7.4).
- The damage is added to every enemy attack, and to the damage value of a *push-move*.
- Bosses, *mimics*, *invaders*, *summons* and *crystal lizards* are never scaled. They are played as printed at every party size.
- Nothing else printed on a *data card* changes.

*Example.* With three characters, a Hollow Soldier printed with 1 health and an attack of 4 has 5 health and an attack of 5. A boss is the same boss for one character or four.

## 8.4 Pushing

Movements and attacks marked with the *push* icon {{icon:ast-0058-push-affected-enemies}} are *push-moves* and *push-attacks*. A push moves a model from its *node* to an adjacent node. Being pushed costs no *stamina*.

A boss cannot be pushed by a character. A boss is pushed only when another boss model moves onto its node.

Each model hit by a push-attack is pushed to the adjacent node most directly opposite the attacker. If several adjacent nodes are equally opposite, the players choose one. A model pushed towards a corner, or towards a node it cannot enter, stays where it is. If the attacker is on the same node as the model it hits, the players choose any adjacent node.

An enemy making a push-move first moves each character on its own node to an adjacent node chosen by the players. The enemy then moves one node in the direction its card gives. If it enters a node that contains characters, each of them is pushed to the adjacent node most directly opposite the node the enemy came from; if several nodes are equally opposite, the players choose. A push-move of several nodes repeats all of this for each node.

A character who *blocks* or *resists* a push-attack is pushed whatever the damage dealt.

*Example.* An enemy hits the Knight with a push-attack from the node to the Knight's left. The Knight is pushed to the node on the right. Where no node lies directly to the right and the two nodes diagonally to the right are equally opposite the enemy, the players choose between them.

## 8.5 Conditions

Some attacks inflict *conditions*. When an attack shows a condition icon, place the matching condition token on each model it hits: on an enemy's base or on a character's dashboard.

A *frostbite* {{icon:ast-0064-frostbite}} or *stagger* {{icon:ast-0066-stagger}} token placed during a model's own turn stays until the end of its next turn.

### Bleed

- A model holds at most one *bleed* {{icon:ast-0063-bleed}} token.
- If a second bleed token would be placed on a model, the model suffers three damage and its bleed token is removed.
- Bleed damage is not reduced by *block* or *resist*.
- A bleed token is not removed at the end of a turn. It stays until the end of the encounter.

### Poison

- A model may hold any number of *poison* {{icon:ast-0065-poison}} tokens.
- At the end of its turn a model suffers one damage for each poison token it holds, then removes one token.
- Poison damage is not reduced by block or resist.
- Poison is not resolved once the last enemy has fallen.

### Frostbite

- A model holds at most one frostbite token.
- A frostbitten character recovers no *stamina* by any means and cannot take the *rest* action.
- A frostbitten enemy moves one *node* less.
- The token is removed at the end of the model's turn.

### Stagger

- A model holds at most one stagger token.
- A staggered model subtracts one from attack, block, resist and *dodge*.
- The token is removed at the end of the model's turn.

### Calamity

With the Black Dragon Kalameet expansion:

- A model holds at most one *calamity* token.
- Calamity reduces the results of a model's block, resist and dodge rolls by one.
- A calamity token is not removed at the end of a turn. It stays until the end of the encounter.

### Corrosion

With the Gaping Dragon expansion:

- A model holds at most one *corrosion* token.
- Corrosion reduces the results of a model's block rolls by one.
- A corrosion token is not removed at the end of a turn. It is removed when the affected character takes damage.
