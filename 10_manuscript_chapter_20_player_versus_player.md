# 20. Player versus Player

When the boss lies dead, the bonfire's peace is not yet earned. The characters who brought it down turn their weapons on one another, and the last one standing takes the honours. This chapter states how such a contest is set up, fought, and won.

## 20.1 Setup

Player versus player (PvP) encounters are an optional rule. They require no expansion. The party decides during setup whether PvP encounters are in play (see §6.5, Optional Rules).

**PvP encounter.** A contest fought between the characters alone, without enemies, on the tile on which a boss has been defeated.

When PvP encounters are in play, one *PvP encounter* is fought after each *mini-boss*, *main-boss*, and *mega-boss* is defeated. It is fought on the tile on which that boss was defeated: the mini-boss tile, the main-boss tile, which is the two *boss tiles* joined as one (see §15.3), or the *mega-boss game board*. It follows the rewards for the boss's defeat (see §16.5) and precedes the rest at the *bonfire* that follows every boss but the *final boss* (see §20.9).

The winner of a PvP encounter gains a *victory bonus* for the PvP encounters that follow; the winner of the PvP encounter that follows the *final boss* is instead the *ultimate victor* (see §20.8). A PvP encounter awards no *souls* and no *treasure cards*. Death in a PvP encounter costs nothing, and the rest that follows the PvP encounter restores every character (see §20.7 and §20.9).

A character who died in the boss *encounter* takes no part in the PvP encounter that follows it. Every other character takes part. *Phantoms*, both *summons* and *invaders*, take no part. If fewer than two characters take part, no PvP encounter is fought and no character wins.

The PvP encounter is set up as follows.

1. Remove every enemy model, *wound token*, and *trap token* from the tile.
2. Remove every *damage cube*, *stamina cube*, *hollow cube*, and *condition* token from each character who takes part.
3. Turn the *luck*, *estus flask*, and *heroic action* tokens of each character who takes part to their ready sides.
4. Settle the turn order (see §20.2).
5. Place each character's model, in turn order, on a corner node chosen by that character's player and occupied by no other model.
6. Set the *aggro token* aside (see §20.2).
7. Shuffle the trap tokens in the supply face down and place them beside the tile.

A corner node is the *node* nearest to one of the four corners of the tile, among the nodes that hold no *terrain*. *Gravestones*, *barrels*, *chests*, and pillars stay on the tile as they stand and keep their effects (see §5.5).

Steps 2 and 3 restore the characters but are not a rest at the bonfire (see §11.2). No *spark* is spent, no encounter is *reset*, and the characters cannot visit the *Firekeeper* or Blacksmith Andre. An *embered* character keeps the *ember token*.

## 20.2 Turn Order

A *PvP encounter* has no enemy *turns*. The characters who take part take their turns one at a time in descending *threat* order (see §3.1). The order is kept for the whole PvP encounter.

If two or more characters share a threat value, the players decide the order of the tied characters before the first turn. If the players cannot agree, the order of the tied characters is decided at random.

In a PvP encounter a *round* is one turn by each character still in play. When the last character in the order has taken a turn, a new round begins with the first character in the order. A dead character takes no turn. Rounds continue until the PvP encounter ends (see §20.8).

The *aggro token* is not used in a PvP encounter.

## 20.3 Character Turns

A character's *turn* in a *PvP encounter* follows the rules of the standard game (see §10.1). The character recovers stamina, takes *minor actions*, takes one *major action*, and moves as in any other *encounter* (see §10.2). Every limit of the standard game applies, including the limit of one *spell* *attack option* per turn (see §4.3). No model leaves the tile (see §5.2).

The *Attack* major action is made against another character (see §20.4). The other major actions and every minor action are unchanged.

At the end of each character's turn, that character's player places one *trap token* (see §20.6).

## 20.4 Attacking a Character

In a *PvP encounter* the *target* of a character's attack is another character. The character who makes the attack is the attacker, and the targeted character is the defender. The attacker resolves the attack as an attack against an enemy (see §10.3), and the defender defends as against an enemy's attack (see §9.3), except as this section states.

The attacker makes the attack as follows.

1. Choose an *attack option* of an *equipped* card and pay its stamina cost.
2. Name one other character within the attack option's *range* as the target (see §5.4).
3. Roll the attack option's dice, apply every modifier, and use any rerolls.
4. Add one to the result if the attacker holds the *victory bonus* (see §20.8).

The final result is the *attack value*. The modifiers and rerolls of the standard game apply to the roll: the +1 of a *scaled* weapon (see §10.5), the reroll of a *two-handed* weapon (see §10.4), and the *luck* token (see §3.5, Luck).

The icons and text of an attack option apply to a defender as they apply to an enemy (see §10.3). In a PvP encounter, the word enemy in a *heroic action* or on a treasure card means another character. An attack option that bears the *shaft* icon {{icon:ast-0056-shaft}} cannot target a character on the attacker's *node*. An attack option that bears the *AoE* icon {{icon:ast-0054-node-attack}} targets every other character on the chosen node: the attacker rolls once, and each of those characters chooses and resolves a defence of their own against the same attack value. Each use of an attack option that bears the *repeat* icon {{icon:ast-0061-repeat-behaviour-or-attack}} is a separate attack, with its own roll and its own defence.

When the attack value is final, the defender chooses one of the following defences before rolling any dice.

- The defender may *block* an attack that deals *physical damage* or *resist* an attack that deals *magical damage* (see §9.4). The defender suffers damage equal to the attack value minus the *defence total*, to a minimum of zero, and is *hit*.
- The defender may *dodge* as against an enemy's attack (see §9.5). The *dodge difficulty* is given by the table in this section.
- The defender may *parry* as against an enemy's attack, with the attacker in the place of the enemy, if the conditions for a parry are met (see §9.6). The dodge difficulty is given by the same table.

A character has no fixed block or resist value. A defender who blocks or resists rolls the dice and takes the two highest (see §9.4).

A successful parry *staggers* the attacker and allows the defender one *riposte* against the attacker (see §9.6). The riposte is an attack under this section with the roles reversed, and its dodge difficulty is set by the stamina cost of the attack option chosen for it. The target of a riposte may block, resist, or dodge it but cannot parry it.

The defender places one *damage cube* on their *endurance bar* for each point of damage suffered (see §3.4). An *embered* defender reduces the damage of an attack as in any other encounter (see §7.3).

The dodge difficulty of a character's attack is set by the stamina cost printed on the attack option.

| Stamina cost of the *attack option* | *Dodge difficulty* |
|---|---|
| 0 | 3 |
| 1 or 2 | 2 |
| 3 or more | 1 |

*Example.* The Assassin attacks the Knight, who stands on an adjacent node, with an attack option that costs one stamina. The Assassin places one stamina cube and rolls two blue dice, which show 2 and 3, for an attack value of 5. An attack option that costs one stamina has dodge difficulty 2. The Knight chooses to dodge, places one stamina cube, and rolls two dodge dice, which show one success and one blank. The total of 1 is lower than the dodge difficulty, so the dodge fails and the Knight is hit. The Knight rolls only the block dice of the armour card, two black dice, which show 1 and 2, for a defence total of 3. The Knight suffers two damage and places two damage cubes.

*Example.* On the Knight's turn, the Knight attacks the Assassin with an attack option that costs four stamina and rolls an attack value of 6. An attack option that costs four stamina has dodge difficulty 1. The Assassin chooses to dodge, places one stamina cube, and rolls two dodge dice, which show one success and one blank. The total of 1 equals the dodge difficulty, so the dodge succeeds. The Assassin is not hit, suffers no damage, and moves to an adjacent node.

## 20.5 Pushes and Conditions

An *attack option* that bears the *push* icon {{icon:ast-0058-push-affected-enemies}} pushes each character it *hits*. The push follows the rules of the standard game (see §8.4), and *terrain* affects the pushed character as in any other encounter (see §5.5). A push onto a *node* that holds a face-down *trap token* triggers the trap (see §20.6).

A condition icon on an attack option places the matching *condition* token on each character it hits. A condition on a character has the same effect and the same duration as in any other encounter (see §8.5). Only a character who is hit is pushed or receives a condition token (see §8.1).

In a *PvP encounter*, a choice that a rule of the standard game leaves to the players is made by the player whose character makes the attack or the movement that calls for the choice.

## 20.6 Traps

At the end of each character's *turn*, that character's player draws one *trap token* from the supply without looking at its face and places it face down on an outermost available *node* of that player's choice. A trap token placed in a *PvP encounter* may occupy a node of any type.

A node is available when it holds no model, no trap token, and no other *terrain*. The outermost available nodes are the available nodes along the edges of the tile. When no node along the edges is available, the outermost available nodes are the available nodes of the next ring inward, and so on towards the centre of the tile. If no node is available, or if no trap token remains in the supply, no trap token is placed.

A character who enters a node that holds a face-down trap token triggers it as in the standard game, and the token is turned face up (see §5.5, Traps). A blank token has no effect. If the token is not blank, each character on that node must attempt to *dodge* it as an attack with the *dodge difficulty* shown on the token (see §9.5). The damage value shown on the token is not used.

A character cannot choose to suffer a trap's damage in a PvP encounter. A character whose dodge fails dies. A character who has no free space on their endurance bar for the stamina cube of the dodge cannot attempt it and dies (see §20.7). A face-up trap token stays on its node and has no further effect during the PvP encounter.

*Example.* The Herald's turn ends, and the Herald's player draws a trap token and places it face down on an empty node along the edge of the tile, adjacent to the Warrior's node. On the Knight's turn, the Knight's attack hits the Warrior and pushes the Warrior onto that node. The token is turned face up and shows dodge difficulty 1 and damage 3. The Warrior places one stamina cube and rolls two dodge dice, which show two blanks. The dodge fails and the Warrior dies.

## 20.7 Death

In a *PvP encounter* a character dies in one of two ways. The character dies when they must place a *damage cube* on their *endurance bar* and no space is free (see §3.4). The character also dies when a trap kills them (see §20.6).

Death in a PvP encounter costs nothing. The steps that follow a death in any other encounter are not carried out (see §7.2). The character drops no *souls*, keeps the *ember token*, receives no *hollow cubes*, and is not *lost*.

When a character dies, that character's player removes the model from the tile, and the character takes no further *turns* in that PvP encounter.

A PvP encounter is neither *cleared* nor *failed* (see §7.5, Encounter Resolution). However it ends, the party spends no *spark* for it and is not required to rest. Every character, including each character who died, is restored by the rest that follows the PvP encounter (see §20.9).

## 20.8 Victory

A *PvP encounter* ends when one character, or no character, remains on the tile. The last character on the tile wins the PvP encounter. If every remaining character dies at the same time, the PvP encounter ends and no character wins.

If no character suffers damage and no character dies during three consecutive *rounds*, each character still in play suffers one damage at the end of every round that follows, until the PvP encounter ends. A character cannot defend against this damage.

**Victory bonus.** The reward for winning a PvP encounter that follows the defeat of a boss other than the *final boss*: +1 to the attack value of each of the winner's attacks in every subsequent PvP encounter.

When a character wins a PvP encounter that follows the defeat of a boss other than the final boss, the character gains the *victory bonus*. A spare token of any kind is placed beside the winner's dashboard to mark it. In every subsequent PvP encounter, the character adds one to the *attack value* of each of their attacks (see §20.4). A character holds no more than one victory bonus, however many PvP encounters the character wins. The victory bonus has no effect outside PvP encounters and is kept until the game ends.

**Ultimate victor.** The character who wins the PvP encounter that follows the defeat of the final boss.

The winner of the PvP encounter that follows the defeat of the final boss is the *ultimate victor*. That PvP encounter awards no victory bonus. If no character wins it, the game has no ultimate victor. Victory over the final boss is shared by every player, whatever the outcome of the PvP encounter (see §7.1).

*Example.* The Assassin wins the PvP encounter that follows the mini-boss, and a spare token is placed beside the Assassin's dashboard. In the PvP encounter that follows the main-boss, which is the final boss of this game, the Assassin rolls a total of 4 for an attack and adds one for the victory bonus, for an attack value of 5. The Assassin is the last character on the tile and is the ultimate victor.

## 20.9 After the PvP Encounter

When a *PvP encounter* that follows the defeat of a boss other than the *final boss* ends:

1. Return every *trap token* on the tile to the supply.
2. Carry out the setup that follows that boss (see §6.6 and §6.7).

That setup ends with a rest at the *bonfire* that costs no *spark* (see §11.2). The rest restores every character, including each character who died in the PvP encounter and each character who died in the boss encounter. It is the one rest that follows the boss's defeat (see §16.5); a PvP encounter grants no second rest. In campaign play, what follows a PvP encounter is stated with the campaign rules (see §18.1, Player versus Player Encounters).

When the PvP encounter that follows the defeat of the final boss ends, the game ends. No setup and no rest follow it.
