# 5. Tiles and Nodes

## 5.1 Tiles and Nodes

All combat takes place during encounters, which are fought on encounter tiles and boss tiles. Every tile has one or more doorways. Doorways allow the characters to travel between tiles.

Every tile except the *bonfire* tile is printed with a number of circular symbols called *nodes*. Nodes are used for setup and for movement during encounters, and take the place of the board spaces of other games. Each node is one of three types: basic, spawn or terrain.

- *Basic nodes* are the most common type. The basic nodes along the wall that adjoins the tile the characters come from are *entry nodes*, where the characters are placed when they enter the tile.
- *Spawn nodes* {{icon:ast-0006-primary-spawn-node}} {{icon:ast-0010-secondary-spawn-node}} are where enemy models are placed at the start of an encounter.
- *Terrain nodes* {{icon:ast-0014-primary-terrain-node}} {{icon:ast-0018-secondary-terrain-node}} are where terrain is placed at the start of an encounter.

The mini-boss tile has a *mini-boss* spawn node, where the mini-boss is placed at the start of its encounter. The main-boss tile has a *main-boss* spawn node, where the main-boss is placed at the start of its encounter.

Models move onto an empty spawn node or terrain node as onto a basic node.

## 5.2 Movement

During an encounter each model must always occupy a single *node*. A model moves by being placed on an adjacent node. An adjacent node is any node directly next to another: horizontally, vertically or diagonally.

Models do not block movement. Some terrain does (see §5.5). No model leaves the tile during an encounter.

## 5.3 Node Model Limits

Several models may share a *node*, but only three at a time, however many of them are friendly or enemy models. This is the *node model limit*.

- If a model moves onto a node that already holds three models, the players must *push* one of those three off the node (see §8.4).
- When the model moving in is a character, the players must push a friendly model if there is one.
- When the model moving in is an enemy, the players must push another enemy model if there is one.

Bosses have a limit of their own.

- Only one boss model may ever be on a node. If a boss moves onto a node that already holds a boss, the players must push the boss that was there first.
- A boss does not count towards the limit of three. A node may hold one boss and three characters.

## 5.4 Range

Attacks and effects have a maximum *range*, counted in *nodes* from one model to another, friendly or enemy.

- Range 0: the models must be on the same node.
- Range 1: the models must be on adjacent nodes, or closer.
- Range 2: the models may be up to two nodes apart, and so on.
- Range ∞ (infinity): the range is unlimited and reaches any model in the encounter.

Terrain and other models do not block range.

## 5.5 Terrain

Terrain is placed as the *encounter card* shows. A *rest* at the *bonfire* never moves a terrain piece or a *trap* token; what else it does is stated for each below (see §11.2).

### Gravestones

- Models cannot *walk*, *run*, *dodge* or be *pushed* onto a *node* containing a *gravestone* {{icon:ast-0017-gravestone}}.
- When an encounter containing a gravestone is *cleared*, the party may reveal one hidden card of its choice: the top card of either treasure deck, or one face-down encounter card or *event card* on any tile.
- A treasure card revealed this way goes back on top of its deck or to the bottom of it. An encounter card or event card goes back on its tile or is replaced with the top card of its deck.
- A rest does not change a gravestone.

### Barrels

- Models cannot walk or run onto a node containing a *barrel* {{icon:ast-0013-barrel}}.
- Models may dodge or be pushed onto a node containing a barrel. The barrel is then destroyed and its token removed.
- A rest returns every destroyed barrel to its node.

### Chests

- Models cannot walk, run, dodge or be pushed onto a node containing a *chest* {{icon:ast-0009-treasure-chest}}.
- A chest begins closed side up. When its encounter is cleared, the chest is flipped to its open side for good and its treasure is taken (see §7.7).
- With the Explorers expansion, a chest is opened as the *mimic* rules direct (see §13).
- A rest does not close or refill an open chest.

### Traps

- If an encounter card is marked with the trap symbol {{icon:ast-0021-trapped-encounter}}, trap tokens are placed when the encounter is set up.
- Shuffle all the trap tokens face down and deal one to each *basic node* of the tile, except the nodes along a tile edge that adjoins another tile.
- If several encounters have traps there may be too few tokens. Fill the basic nodes furthest from the tile's entry first and stop when the tokens run out.
- A trap token is blank or shows a damage value and a *dodge difficulty*. Traps do not affect movement.
- When a character moves or is pushed onto a node with a face-down trap token, flip the token. A blank token does nothing. Otherwise the trap is sprung and hits every model on that node, enemies included, for the damage shown.
- A character may dodge a trap (see §9.5). Trap damage cannot be *blocked* or *resisted*. A character who dodges a trap stays on the node.
- A rest turns every face-up trap token face down on its node.
