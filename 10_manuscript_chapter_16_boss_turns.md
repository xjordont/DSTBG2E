# 16. Boss Turns

A boss does not take its place in the line of lesser foes. It answers every blow, and each card it turns shows a new way to die. This chapter states how a boss takes its turns, how it moves and attacks, whom it hunts, and what follows when it falls.

## 16.1 Overview

The *boss* takes the first *turn* of a boss *encounter* (see §15.2). After each boss turn one character takes a turn, and the boss then takes its next turn. The boss and the characters alternate in this way until the boss is defeated (see §16.5) or the encounter is *failed* (see §15.2).

A boss encounter is fought in *rounds*. In each round every living character takes one turn, and the boss takes one turn before each of those turns. The players choose which living character takes each character turn; the descending *threat* order of other encounters does not apply to the characters (see §7.5, Encounter Turn Order). No living character takes a second turn in a round until every other living character has taken one. A dead character takes no turn and is not counted.

A character's turn in a boss encounter is resolved as in any encounter (see §10.1). If a *summon* is in play, it takes a turn after each character's turn and before the boss's next turn (see §12.1). A tie in threat is settled as in any encounter (see §7.5, Encounter Start).

A boss's turn is resolved as follows.

1. If the *behaviour deck* is empty, turn the discard pile face down, without shuffling it, to form the behaviour deck (see §15.5, Deck Renewal).
2. Draw the top card of the behaviour deck and place it face up beside the deck. This card is the boss's current *behaviour card* (see §15.5, Card Anatomy).
3. Resolve each icon on the card, one at a time from left to right: each movement icon (see §16.2) and each attack icon (see §16.3).
4. If the card bears the *repeat* icon {{icon:ast-0061-repeat-behaviour-or-attack}}, resolve the whole row of icons again from left to right, until the row has been resolved the number of times the icon shows.
5. Place the card face up on top of the discard pile.

Each icon is resolved in full before the next. An icon that has no valid *target*, or that cannot be resolved, is skipped, and the next icon to its right is resolved (see §9.1). The repeat icon on a behaviour card repeats the whole card, not one attack. Each time the row is resolved, the target of each icon is determined again.

The boss's turn ends when step 5 is complete. *Conditions* affect a boss as they affect any enemy (see §8.5). If the boss heats up during its own turn, the *heat-up card* joins the behaviour deck after step 5 (see §15.5, Heat-Up). If the boss is defeated during its own turn, as a *riposte* may cause, the turn ends at once and no further icon is resolved (see §16.5).

*Example.* The Knight, the Herald, and the Assassin fight a *mini-boss* whose behaviour deck holds four cards. The boss takes the first turn. The players choose the Herald to act, and the boss takes its second turn. The Knight acts, the boss takes its third turn, and the Assassin acts. Every character has taken a turn, so the round is complete. The boss takes its fourth turn, and the players choose any of the three characters to act next. At the start of its fifth turn the boss's behaviour deck is empty: the discard pile is turned face down without shuffling, and the boss draws the card it drew on its first turn.

## 16.2 Boss Movement and Symbols

A *boss* *moves* as an enemy moves (see §9.2), with the differences stated in this section. The number of *nodes* a boss moves is not scaled for the number of characters (see §8.3). Each node a boss enters must be a *valid node* (see §5.2).

Each movement icon {{icon:ast-0033-enemy-movement-composite-symbol}} on a *behaviour card* shows a direction and a number of nodes. A movement icon that names a *target* shows the skull icon, for the character who holds the *aggro token*, or the nearest-character icon {{icon:ast-0032-target-nearest-character}}, for the *nearest character* (see §9.2). A *summon* is counted as a character when the target is determined (see §12.1).

### Movement Towards a Target

When a movement icon moves a boss towards its target, the boss follows the shortest path of valid nodes to the target's node, as an enemy does (see §9.2, Paths). Each node of the movement is resolved in two steps.

1. Turn the boss so that the centre of its front arc faces the next node of its path.
2. Move the boss forwards onto that node.

The boss stops when it has moved the number of nodes shown or when it stands on the target's node. If two or more paths are equally short, the players choose the path (see §9.2, Paths).

When the target is on the boss's own node, the boss does not leave its node. The boss turns in place until the arc in which the target is placed is its front arc: 90° towards a target in a side arc, or 180° for a target in the back arc. No character on the node moves while the boss turns (see §15.6, Facing and Turning).

### Movement Away from a Target

When a movement icon moves a boss away from its target, each node the boss enters must be a valid node at a greater *range* from the target than the node it leaves, as for an enemy (see §9.2, Paths). Each node of the movement is resolved in two steps.

1. Turn the boss so that the centre of its back arc faces the node it is to enter.
2. Move the boss backwards onto that node, without turning it further.

If two or more such nodes are open to the boss, the players choose one of them. If no such node is open to the boss, it stops, and the rest of the movement is lost (see §9.2, Paths).

### Movement Without a Target

A movement icon that names no target moves the boss the number of nodes shown in the direction shown: forwards, backwards, to its left, or to its right. The boss does not change its *facing*. Each node it enters is the *adjacent node* at the centre of its front arc, its back arc, its left arc, or its right arc. If that node is not a valid node, the boss stops, and the rest of the movement is lost.

### Characters on a Node the Boss Enters

When a boss moves onto a node that holds one or more characters, and the movement is not a *push-move*, the characters stay on that node. Each character is placed against the boss's base in the arc in which the node lay immediately before the boss entered it. If the node lay in two arcs, the character's player chooses one of the two (see §15.6, Characters and Arcs).

A boss model does not count towards the *node model limit*, and its arrival displaces no model (see §5.3).

### Push-Moves

A movement icon that bears the push icon {{icon:ast-0058-push-affected-enemies}} is a push-move. A boss resolves a push-move one node at a time, as an enemy does (see §8.4), with three differences.

- The boss turns before each node of the movement, as this section describes for movement towards or away from a target.
- A character *pushed* off the boss's own node before the boss moves must be pushed within the arc in which the character is placed (see §15.6, Characters and Arcs).
- A character on a node the boss enters is pushed directly away from the node the boss has left (see §8.4). If no valid node lies directly away, the character is pushed as a character on the boss's own node is pushed: within the arc in which the node lay immediately before the boss entered it, or along the wall if that arc holds no valid adjacent node (see §15.6, Characters and Arcs).

If the push icon carries a damage value {{icon:ast-0031-push-with-damage-satellite-glyph}}, each character on a node the boss enters is attacked before being pushed (see §8.4). The damage value is not scaled, and a *dodge* of the attack is rolled against the *dodge difficulty* of the boss's current behaviour card (see §15.5, Card Anatomy).

### Leap

**Leap.** A boss movement marked with the leap icon. The boss is placed directly on the node of its target, at any distance.

A *leap* names its target as any movement icon does: the character who holds the aggro token or the nearest character. A leap is resolved as follows.

1. Remove the boss model from its node.
2. Place the boss model on the target's node, without changing its facing.
3. Push every character on that node to a valid adjacent node chosen by that character's player.

A leap has no limit of distance, and no model or *terrain* on the nodes between blocks it. The characters pushed in step 3 are not placed in an arc, and the arc limit on pushes does not apply to them (see §15.6, Characters and Arcs). A character who has no valid adjacent node stays on the node and is placed in an arc of their player's choice.

If the target is on the boss's own node, the boss stays on its node and keeps its facing, and step 3 is carried out. If the push icon of a leap carries a damage value, each character on the target's node is attacked before being pushed, as for a push-move (see §8.4).

### Turn Icons

The turn 90° right icon {{icon:ast-0034-turn-90-right}}, the turn 90° left icon {{icon:ast-0035-turn-90-left}}, and the turn around icon {{icon:ast-0036-turn-around}} turn the boss in place on its node. The boss does not move, and no other model moves (see §15.6, Facing and Turning).

*Example.* The boss draws a behaviour card whose first icon is a push-move of two nodes towards the character who holds the aggro token. The Knight holds the aggro token and stands two nodes straight ahead of the boss, on a node against the wall. The Assassin stands on the node between them, and the Herald is on the boss's own node, in the left arc. The Herald is pushed first, to a valid adjacent node in the left arc that the players choose. The boss already faces the Assassin's node and moves forwards onto it without turning. The Assassin is pushed directly away from the node the boss has left, onto the Knight's node. The boss moves forwards again, onto the Knight's node. No valid node lies directly away from the boss, and the front arc holds no valid adjacent node because of the wall. The Knight and the Assassin are each pushed to a valid adjacent node that touches the wall.

*Example.* A boss's movement icon moves it one node towards the nearest character. The Warrior is the nearest character and is on the boss's own node, in the back arc. The boss does not leave its node. It turns 180°, and the Warrior, who has not moved, is now in the front arc.

## 16.3 Boss Attacks

A *boss* attacks as an enemy attacks (see §9.3), with the differences stated in this section. The number printed in the attack icon {{icon:ast-0037-enemy-attack-composite-symbol}} is the *attack value*, which is fixed and is not scaled for the number of characters (see §8.3). The *range* {{icon:ast-0060-attack-range}} and the *dodge difficulty* {{icon:ast-0062-dodge}} of the attack are those printed on the *behaviour card* that bears the icon (see §15.5, Card Anatomy).

A boss does not change its *facing* when it attacks (see §15.6, Facing and Turning). Range is counted from the boss's *node* (see §5.4).

### Targets

An attack icon that shows the skull icon *targets* the character who holds the *aggro token*. An attack icon that shows the nearest-character icon {{icon:ast-0032-target-nearest-character}} targets the *nearest character* (see §9.2). A *summon* is counted as a character when the target is determined (see §12.1).

The target is attacked in whatever *boss arc* they stand. If the target is not within the card's range, the icon is skipped, and no other character is attacked in the target's place (see §9.3, Targets).

An attack icon that bears the node icon {{icon:ast-0054-node-attack}} is a *node attack*. It targets every character on the node of the character named by the icon, and each of those characters is attacked separately (see §9.3, Targets).

### Area Attacks

**Area attack.** A boss attack whose icon bears the area icon {{icon:ast-0038-area-attack-icon}}. It is made into one or more of the boss's arcs, not against one character.

An *area attack* targets every character who is within the card's range of the boss and who is in an *attack arc* {{icon:ast-0040-attack-boss-arc}} of the arc diagram beneath the icon (see §15.6, Arc Diagrams). A character on a node that lies in two arcs is targeted if either arc is an attack arc. A character on the boss's own node is targeted if the arc in which they are placed is an attack arc.

The aggro token and the nearest character play no part in an area attack. Each targeted character is attacked separately with the full attack value, and each defends on their own. If no character is targeted, the icon is skipped.

### Damage, Pushes, and Conditions

An attack icon that shows the *magical damage* icon {{icon:ast-0042-deal-magical-damage}} deals magical damage, which a character *resists*. Every other boss attack deals *physical damage*, which a character *blocks* (see §9.4).

An attack icon that bears the push icon {{icon:ast-0058-push-affected-enemies}} is a *push-attack*. Each character it *hits* is *pushed* directly away from the boss after the damage has been resolved (see §8.4). A character who is hit while on the boss's own node is pushed within the arc in which they are placed (see §15.6, Characters and Arcs).

An attack icon that shows a *condition* icon places the matching condition token on each character it hits (see §8.5).

### Defence

Each character targeted by a boss's attack chooses one defence before any dice are rolled, as against any enemy attack (see §9.3, Defence). The character blocks or resists (see §9.4), attempts to *dodge* (see §9.5), or attempts to *parry* where a parry is allowed (see §15.6, Defence).

A dodge or a parry is rolled against the dodge difficulty of the behaviour card that bears the attack icon. A character who dodges is not hit: the character suffers no damage, is not pushed, and receives no condition token (see §8.1). The movement that follows the dodge ignores arcs (see §15.6, Defence).

*Example.* The boss's current behaviour card shows range 1, dodge difficulty 2, and an area attack with attack value 5 and physical damage. Its arc diagram shows the front arc and the right arc as attack arcs. The Knight stands on the node the boss faces. The Assassin stands on an *adjacent node* on the line between the right arc and the back arc. The Herald stands two nodes from the boss, in the front arc. The Knight and the Assassin are targeted; the Herald is out of range and is not attacked. The Knight blocks with a *defence total* of 3 and suffers two damage. The Assassin pays one stamina and rolls two dodge dice, which show two dodge icons. Two equals the dodge difficulty, so the Assassin is not hit and moves to an adjacent node.

## 16.4 Boss Aggro

The *aggro token* marks the character whom a *boss*'s *behaviour cards* *target* with the skull icon (see §16.2; §16.3). When a boss *encounter* is set up, the token is placed on the character with the highest *threat* (see §15.2).

In a boss encounter the aggro token does not move at the end of a *round* as it does in other encounters (see §7.5, Encounter Turn Order). At the end of each character's *turn*, if that character inflicted damage on the boss during the turn, the aggro token moves to that character. If the character inflicted no damage on the boss, the token stays with its holder.

A character inflicts damage on a boss when an attack lowers the boss's *health dial* by one or more. An attack that the boss's *block* or *resist* reduces to no damage does not move the token.

A *riposte* is made during the boss's turn (see §9.6). If a riposte inflicts damage on the boss, the aggro token moves to the character who made it at the end of that boss turn, after the behaviour card has been resolved. If more than one character ripostes in the same boss turn, the token moves to the last of them to inflict damage.

When the character who holds the aggro token dies, the token moves at once to the living character with the highest threat (see §7.5, Encounter Turn Order). A *summon* does not hold the aggro token, and damage inflicted by a summon does not move it (see §12.1).

*Example.* The Knight holds the aggro token. The Herald attacks the boss and inflicts two damage, and at the end of the Herald's turn the token moves to the Herald. The boss takes its turn and attacks the Herald. The Assassin then attacks the boss, and the boss's block reduces the attack to no damage. The token stays with the Herald.

## 16.5 Boss Death

A *boss* is defeated when its *health dial* is reduced to zero (see §15.4). The boss *encounter* ends at once. The boss model is removed from the tile, and no further icon of its *behaviour card* is resolved.

A boss fought with two models, and the *Twin Gargoyles*, are defeated as their own rules state (see §17.1).

If the defeated boss is the *final boss*, the players win the game (see §7.1), and the numbered steps of this section are not carried out. If player versus player (PvP) encounters are in play, a last *PvP encounter* is then fought (see §20.1).

When any other boss is defeated, its defeat is resolved as follows.

1. Award each character, including each character who died in the encounter, the boss soul reward (see §7.6).
2. Shuffle the boss's *boss treasure* cards, draw one at random, and award it to the party (see §7.7).
3. Return the boss's other treasure cards to the game box.
4. Place an *ember token* in the ember slot of every character's dashboard, including each character who died in the encounter. Every character is *embered*, and no *ember card* is discarded (see §7.3).
5. Remove every *damage cube* and every *hollow cube* from each living character, as for any embering (see §7.3).
6. If PvP encounters are in play, fight a PvP encounter on the tile on which the boss was defeated (see §20.1).
7. Carry out the setup that follows the boss: the setup after the *mini-boss* (see §6.6) or, when a *mega-boss* is in play, the setup after the *main-boss* (see §6.7).

The setup of step 7 adds one *spark* to the spark dial. This is the spark that each defeated boss grants (see §7.4). The setup ends with the characters on the *bonfire* tile, where they rest without spending a spark (see §11.2) and may visit the *Firekeeper* (see §11.3) and Blacksmith Andre (see §11.4).

The spark is gained once and the rest is taken once for each defeated boss, whether or not a PvP encounter is fought (see §20.9). The recovery that follows a *cleared* encounter is not carried out after a boss (see §7.5, Encounter Recovery). A character who died in the boss encounter stays out of play until the rest, which restores every character (see §11.2).

The embering of step 4 provokes no *invasion* at that moment (see §12.2). In campaign play the spark, the rest, and the setup that follow a boss differ (see §18.1; §18.3).

*Example.* The Knight, the Herald, and the Assassin defeat the mini-boss, and the Assassin died during the encounter. Each of the three characters gains the boss soul reward. One of the mini-boss's treasure cards is drawn at random, and the players give it to the Herald. All three characters receive an ember token, and the Knight removes four damage cubes. No PvP encounter is in play, so the party carries out the setup after the mini-boss. The spark dial, which shows two, is turned to three. The characters rest at the bonfire without spending a spark, and the rest restores the Assassin.
