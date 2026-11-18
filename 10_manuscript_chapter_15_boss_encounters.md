# 15. Boss Encounters

## 15.1 The Fog Gate

Once the party has reached a boss encounter it must pass through the *fog gate*, which stands in the doorway of the boss tile. An *embered* character may call a *summon* at the fog gate before the party passes through (see §12.1).

The first time the party passes through the fog gate, remove the fog gate token from the doorway and place it on the *bonfire* tile to serve as a shortcut. If the party fails its attempt at the boss, it may use the fog gate to travel straight from the bonfire tile to the boss encounter and try again without fighting any encounter on the way. A party that wishes to gain more *souls* first may forgo the fog gate and travel the road to the boss again through its encounter tiles.

The token stays on the bonfire tile until the boss is defeated. In a campaign the fog gate gives no shortcut.

## 15.2 Overview

A boss is a single large model with far more health and attack power than other enemies and a special ability of its own; it follows the rules for enemies except as this chapter and the next state. There are three types of boss: *mini-boss*, *main-boss* and *mega-boss*.

A boss's behaviour deck is built when the boss is set up on its tile, and built afresh each time the party *rests* after losing to that boss (see §15.5). It lies face down beside the tile.

Each time a boss encounter begins, place the character models on the *entry nodes* of the boss tile and the boss model on its *spawn node*, facing the adjacent *node* nearest the entry nodes. Set the boss's health dial to its starting health. Give the *aggro* token to the character with the highest *threat*.

## 15.3 Boss Tiles

A *mini-boss* encounter takes place on the single mini-boss tile, unless the boss's own rules name another. A *main-boss* encounter needs both boss tiles, placed side by side and treated as one large tile for all purposes. A *mega-boss* encounter is fought on the game board that comes with that mega-boss's expansion.

A boss is placed on the *spawn node* of its own type. During a main-boss encounter the mini-boss spawn node is a *basic node*.

## 15.4 Boss Data Cards

A boss *data card* holds much the same information as an enemy data card, but it shows no behaviours. A boss's behaviour varies, and is decided by its own deck of *behaviour cards* (see §15.5).

1. Name
2. *Threat* {{icon:ast-0026-threat-level}}
3. Behaviour deck size {{icon:ast-0027-behaviour-deck-size}}
4. *Heat-up* point {{icon:ast-0030-heat-up-point}}
5. *Block* and *resist* values {{icon:ast-0028-block-resist-shield}}
6. Special ability
7. Encounter levels
8. Starting health {{icon:ast-0029-starting-health}}
9. Boss type icon (mini, main or mega)
10. Set symbol

- Threat, block and resist work as they do on an enemy data card (see §8.2).
- Starting health works in the same way, but a boss's remaining health is tracked on the health dial of that boss in place of wound tokens.
- Behaviour deck size and heat-up point decide the make-up of the boss's behaviour deck.
- The special ability gives the boss a theme and often a power of its own (see §17).
- The encounter levels are those of the encounters on the road to that boss (see §6.5).

A boss's starting health, heat-up point and attack damage are raised for the number of characters (see §8.3).

## 15.5 Boss Behaviour Cards

Every boss *behaviour card* is laid out in the same way.

1. Name
2. Attack *range* {{icon:ast-0060-attack-range}}
3. *Dodge difficulty* {{icon:ast-0062-dodge}}
4. *Heat-up* symbol
5. Behaviour icons, for movement {{icon:ast-0033-enemy-movement-composite-symbol}} and for attacks {{icon:ast-0037-enemy-attack-composite-symbol}}

A boss's behaviour is dictated entirely by the behaviour card revealed from the top of its behaviour deck on its turn. The behaviour icons are like those on an enemy *data card*, but they include a few new icons, take account of the way the boss faces and are generally more powerful. Each behaviour card sets the boss's attack range and dodge difficulty until the next card is drawn.

A behaviour card that bears the heat-up symbol is a heat-up card. Heat-up cards are typically more powerful, and they are not in the behaviour deck at the start.

To build the behaviour deck:

1. Set aside all of the boss's heat-up cards.
2. Shuffle the other behaviour cards and deal a number of them equal to the boss's behaviour deck size, face down, into a pile. This pile is the behaviour deck.
3. Return the behaviour cards that were not dealt to the box, face down.
4. Shuffle the heat-up cards and place them face down beside the boss tile.

When a boss's health first falls to its heat-up point or below, at once shuffle one random heat-up card together with its behaviour deck and discard pile to form a new deck. Some bosses have heat-up rules of their own, which may let them heat up more than once or replace these rules (see §17).

## 15.6 Arcs and Defence

The base of a boss model is divided into four *arcs*: front, left, right and back. The arcs add a layer of tactics to fighting a boss.

A boss always faces an adjacent *node* directly: the centre of its front arc lines up with the centre of that node. This splits the tile into four areas, one for each of the boss's arcs. Every node on the tile is in at least one of the four arcs. A node on the line between two arcs is in both.

### Character Arc Movement

In a boss encounter characters move by these further rules.

- A character sharing a node with a boss is placed on the base of the boss model, in one of the four arcs.
- A character moving onto the boss's node stays in the arc of the node they leave. If that node is split between two arcs, the player chooses which of the two to move into.
- A character on the boss's node may move to an adjacent arc of the base in place of moving off the node. A character who moves more than one node, as with a *run*, may do this more than once: from the front arc to a side arc, for instance, and then to the back arc.
- A character moving off the boss's node stays in the same arc: a *walk* or a run takes them to an adjacent node within the arc they leave.
- A character *pushed* off the boss's node moves to the centre-most node of the arc they are in. If the boss cannot push a character directly away, the character moves to any adjacent node of the players' choice.
- A character who *dodges* a boss's attack moves to an adjacent node as usual, but need not stay in the same arc: the character may move to any adjacent node or onto any arc of the boss's base.

### Attacking Bosses and Weak Arcs

When a character attacks a boss, the *behaviour card* the boss resolved most recently shows which arcs are weak, marked in red {{icon:ast-0041-weak-boss-arc}}. An attack made from a *weak arc* gains one extra black die {{icon:ast-0051-black-dice}}.

A character on a node along the line between two arcs is in both of them. This makes the weak arc bonus easier to gain, but the character is also a target of attacks against either arc. The attack gains one black die only, however many weak arcs the character is in.

*Example.* The boss faces the node straight ahead of it, where the Herald stands in the front arc. The Knight stands on the node straight behind the boss, in the back arc. The Assassin's node lies on the line between the front arc and the left arc, so the Assassin is in both. The last behaviour card the boss resolved marks the left arc and the back arc as weak. The Knight and the Assassin each add one black die to an attack on the boss. The Herald adds none.
