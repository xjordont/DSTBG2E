# 5. Tiles and Nodes

Every encounter is fought on a tile, and every tile is a fragment of a ruined world: a crypt, a courtyard, a hall of fallen pillars. The circular nodes printed on the tiles are the ground on which the characters stand, fight, and fall. This chapter describes tiles and nodes, movement, range, and the terrain that stands in the way.

## 5.1 Tiles and Nodes

Every *encounter* is fought on one or more tiles: an encounter tile, the *boss tiles* (see §15.3), or the *mega-boss game board* (see §6.7). The *bonfire* tile has no nodes, and no encounter is fought on it (see §11.1).

The edge of every tile is a wall. A *doorway* is a gap in the wall through which the characters pass from one tile to the next. Tiles are joined so that a doorway of each tile faces a doorway of the tile beside it (see §6.5). A tile's orientation is fixed when the tile is placed, and the tile is neither rotated nor moved until the tiles are next laid out for setup.

Every tile except the bonfire tile is printed with circular spaces called *nodes*. During an encounter every model occupies exactly one node; a model is never between nodes or in a doorway. Each node is one of three types: basic, spawn, or terrain.

**Basic node.** The most common node type, printed in yellow. *Trap tokens* are dealt to basic nodes (see §5.5, Traps).

**Entry node.** A basic node along the tile edge that holds the doorway through which the characters entered the tile. When the characters enter a tile, they are placed on its entry nodes (see §7.5, Encounter Start).

**Spawn node.** {{icon:ast-0006-primary-spawn-node}} A node on which enemy models are placed at the start of an encounter, as the *encounter card* directs (see §7.5, Encounter Start). The mini-boss tile has a mini-boss spawn node, the main-boss tile a main-boss spawn node, and a mega-boss game board a mega-boss spawn node; the *boss* is placed there at the start of its encounter (see §15.3).

**Terrain node.** {{icon:ast-0014-primary-terrain-node}} A node on which a *terrain* token or model is placed at the start of an encounter, as the encounter card directs (see §5.5).

Tiles and encounter cards tell a primary spawn node from a secondary spawn node {{icon:ast-0010-secondary-spawn-node}}, and a primary terrain node from a secondary terrain node {{icon:ast-0018-secondary-terrain-node}}, by their icons. The difference shows which node receives which models or terrain and has no other effect.

A spawn node or terrain node that holds no enemy or terrain is entered, left, and counted for range exactly as a basic node is.

**Adjacent node.** A node directly next to another node: horizontally, vertically, or diagonally. Two nodes separated by a wall, whether the wall is the edge of the tile or a wall printed across a tile or a mega-boss game board, are not adjacent. Nodes on different tiles are not adjacent; the two boss tiles joined for a main-boss encounter form one tile (see §15.3).

## 5.2 Movement

A model *moves* when it leaves its *node* for an *adjacent node*. A model that moves several nodes moves one node at a time, and the rules of each node it enters apply as it enters that node.

**Move.** Any change of node that a model makes by the *Walk* or *Run* minor action (see §10.2), by a *shift* icon (see §10.3, Shift), or by an enemy or boss movement icon (see §9.2; §16.2). The movement that follows a successful *dodge* (see §9.5) and the forced movement of a *push* (see §8.4) are not moves; a rule that treats them differently names them.

**Valid node.** A node that a model may enter by a given form of movement: an adjacent node that no wall separates from the model's node and that holds no *terrain* blocking that form of entry (see §5.5). A model may move, dodge, or be pushed only into a valid node. If no valid node exists for a move, a dodge, or a push, the model stays on its node. A node at its *node model limit* is a valid node; a model that enters it displaces another model as §5.3 describes.

During an encounter, no model may leave the tile or tiles on which the encounter is fought, and no model may pass through a doorway. Models pass between tiles only when the party travels from one encounter to the next (see §7.5, Encounter Start).

The stamina cost and the limits of each form of movement are stated with that form (see §10.2 for Walk and Run; §10.3, Shift; §9.2 for enemy movement; §16.2 for boss movement; §9.5 for the dodge; §8.4 for pushes).

## 5.3 Node Model Limits

Several models may share one *node*. The *node model limit* is three non-boss models, friendly or hostile in any combination, and one *boss* model. A boss model does not count towards the three.

When a fourth non-boss model enters a node, the players must *push* one of the three models already on the node to a *valid node* chosen by the players (see §8.4). If the entering model is a character or a *summon*, the players must push a character or summon if one is on the node. If the entering model is an enemy or an *invader*, the players must push an enemy or invader if one is on the node. If no such model is on the node, the players push any model on it.

When a boss model moves onto a node that holds another boss model, the boss already on the node is pushed to a valid node chosen by the players (see §17.1).

*Example.* The Knight, the Herald, and a Hollow Soldier share a node. The Warrior walks onto it, so the players must push a character or summon: they choose the Herald, who is pushed to a valid node of their choice. The Hollow Soldier stays. Then the Gargoyle moves onto a node that holds the Knight, the Herald, and the Assassin; the boss does not count towards the limit, so no model is pushed.

## 5.4 Range

*Range* is the distance between two models, counted in *nodes*. It is counted along the shortest chain of *adjacent nodes* from one model's node to the other's, and each step along the chain counts one. Range is counted between models, friendly or hostile alike.

Range 0 is the same node. Range 1 is an adjacent node or the same node. A range of any number N reaches a model up to N nodes away, including every closer node. Range ∞ (infinity) is unlimited and reaches every model in the encounter.

Range is a maximum, never a minimum: an attack or effect with range 2 reaches models at range 0, 1, or 2, except where its own rules say otherwise (for example the *shaft* icon, see §10.3, Shaft).

Range is never blocked. *Terrain*, *trap tokens*, and other models on the nodes between two models do not block range and do not lengthen it. A wall blocks range only because the nodes on either side of it are not adjacent, so the chain of nodes is counted around the wall.

The range of a character's attack is printed on the equipment card or on the attack option (see §10.3, Range). The range of an enemy's attacks is printed on its data card (see §9.3), and a boss's range on each of its behaviour cards (see §16.3).

*Example.* The Assassin stands two nodes from a Hollow Soldier, and the node between them holds a *gravestone*. The Assassin's attack option has range 2. The gravestone does not block range, so the Hollow Soldier is within range. The Knight stands on the far side of a wall from the same Hollow Soldier; the two nodes touch across the wall but are not adjacent, and the Knight's attack option with range 1 cannot reach it.

## 5.5 Terrain

*Terrain* is the set of obstacles placed on a tile at the start of an *encounter*. There are five kinds: *gravestones*, *barrels*, *chests*, and pillars, which are placed on *terrain nodes* as the *encounter card* directs, and traps, which are dealt to *basic nodes* (see §7.5, Encounter Start). Each terrain token or model occupies one *node*.

The rules in this section apply to every model alike: characters, enemies, *phantoms*, and the *boss*. No terrain blocks *range* (see §5.4). An enemy or boss moves around terrain that blocks it, choosing its path as §9.2 or §16.2 describes.

When the characters rest at the *bonfire* and the encounters are reset (see §11.5), terrain stays on its nodes. What else happens to each kind of terrain at that time is stated under that kind.

### Gravestones

A gravestone {{icon:ast-0017-gravestone}} blocks its node completely. No model may *move*, *dodge*, or be *pushed* into a node containing a gravestone.

When an encounter is *cleared*, the players may *scry* one card for each gravestone on its tile. Each scry is resolved during Encounter Resolution, which states the cards that may be scried and what is done with them (see §7.5, Encounter Resolution).

When the characters rest at the bonfire, a gravestone stays on its node.

### Barrels

A barrel {{icon:ast-0013-barrel}} token has an intact side and a destroyed side, and a barrel begins every encounter intact. No model may move into a node containing an intact barrel.

A model may dodge or be pushed into a node containing an intact barrel. When it does, the barrel is destroyed: turn the token to its destroyed side, or remove a barrel model from the tile. A destroyed barrel blocks nothing, and its node is used as a basic node for the rest of the encounter.

When the characters rest at the bonfire and the encounters are reset, every barrel is restored: turn each destroyed token back to its intact side, and return each removed barrel model to its terrain node.

### Chests

A chest {{icon:ast-0009-treasure-chest}} token has a closed side and an open side. A chest is placed closed side up, and one face-down *treasure card* from the treasure deck of the current tier is placed beneath it (see §7.5, Encounter Start; §7.7). No model may move, dodge, or be pushed into a node containing a chest, whether the chest is closed or open.

A chest is opened, and the card beneath it awarded, only when the encounter that contains it is cleared (see §7.7). If *mimics* are in play, a chest is opened only as §13 describes. Opening a chest turns the token to its open side; an opened chest is never closed again and holds no further treasure.

When the characters rest at the bonfire and the encounters are reset, a chest stays on its node and on its current side.

### Traps

An encounter whose encounter card shows the trap icon {{icon:ast-0021-trapped-encounter}} is a trapped encounter. *Trap tokens* are dealt to its tile the first time the encounter is set up, as part of Encounter Start (see §7.5, Encounter Start), and thereafter stay on the tile. A trap token is blank or shows a *dodge difficulty* and a damage value. Trap tokens are dealt to the tile as follows.

1. Shuffle every trap token in the supply face down.
2. Deal one face-down trap token to each basic node of the tile, except the basic nodes along a tile edge whose doorway is part of the route (see §6.5), beginning with the nodes farthest from the *entry nodes*.
3. If the supply runs out before every such node has a token, leave the remaining nodes without a trap.

Traps do not block movement, dodging, or pushes. When a character enters a node holding a face-down trap token, whether by a *move*, by the movement that follows a successful *dodge*, or by a *push*, the token is turned face up at once, before anything else is resolved. If the token is blank, nothing happens. Otherwise each character on that node must either suffer the damage shown or attempt to dodge it as an attack with the dodge difficulty shown (see §9.5); each player chooses for their own character. The dodge follows every rule in §9.5, including the movement that follows a successful dodge. If the dodge fails, the character suffers the damage shown. Trap damage is not an attack, and it cannot be blocked or resisted.

A face-up trap token has no further effect during that encounter. Only characters trigger traps, and only characters are affected by them; enemies, bosses, and phantoms neither trigger traps nor suffer their damage.

When the characters rest at the bonfire and the encounters are reset, every face-up trap token is turned face down and stays on its node. Trap tokens are not dealt to the same tile again when its encounter is reset.

*Example.* The Knight runs onto a basic node holding a face-down trap token and turns it face up. The token shows dodge difficulty 1 and damage 3. The Knight chooses to dodge, pays one stamina, and rolls a total of 1: the dodge succeeds, the Knight suffers no damage and moves to an adjacent node. A Hollow Soldier then moves onto the same node; the face-up token has no effect on it.

### Pillars

*Pillar tokens* exist only in the Asylum Demon expansion. At the start of a boss encounter fought on the mega-boss side of that expansion's mega-boss game board, one pillar token is placed on each of its four pillar nodes (see §17.3). No model may move, dodge, or be pushed into a node containing a pillar token.

A pillar is destroyed only as §17.3 describes. Once destroyed, its node is used as a basic node for the rest of the encounter. When the characters rest at the bonfire, destroyed pillars are returned to their pillar nodes (see §17.3).
