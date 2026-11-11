# 7. Gameplay

The characters set out from the bonfire and fight their way, tile by tile, towards the boss that waits at the end of the road. Every death costs, every rest costs, and the sparks that pay for both are few. This chapter states how the game is won and lost and how every encounter begins, runs, and ends.

## 7.1 Objective and Loss Conditions

The players win the game when any character survives to defeat the *final boss*. In the standard game the final boss is the *main-boss*. During setup the party may instead add a *mega-boss*, fought after the main-boss, as the final boss (see §6.5 and §6.7). Victory over the final boss is shared by every player.

If the party chose player versus player (PvP) during setup, a PvP *encounter* is fought after each boss is defeated (see §20).

The players lose the game when the characters are required to rest at the *bonfire* and the *spark* dial shows zero. The characters are required to rest when an encounter is *failed*: when every character has died, or when a *hollow* character dies (see §7.5, Encounter Resolution). The party cannot choose to rest while the spark dial shows zero (see §7.4).

These conditions apply in every encounter, including boss and mega-boss encounters. A failed boss encounter is resolved as any other failed encounter.

## 7.2 Death and Hollowing

A character dies when they must place a *damage cube* on their *endurance bar* and no space is free (see §3.4). A dead character is out of play for the rest of the *encounter* and takes no *turns*.

When a character dies:

1. Place all of the character's *souls* on the encounter tile, in a pile separate from any other character's *dropped souls* (see §7.6).
2. Discard the character's *ember token*, if present (see §7.3).
3. If the character holds the *aggro token*, move it to the living character with the highest *threat* (see §7.5, Encounter Turn Order).
4. Remove the character's model from the tile and place it on its side beside the *bonfire* tile.

If the encounter is *cleared*, each character who died in it is revived *hollow* during Encounter Recovery (see §7.5, Encounter Recovery). If every character dies, the encounter is *failed* instead (see §7.5, Encounter Resolution); a character who adventures alone is therefore never revived hollow.

**Hollow cube.** One of eight cubes of a colour distinct from the damage, stamina, and stat cubes. Two *hollow cubes* block the two rightmost spaces of a hollow character's endurance bar.

A hollow character has two hollow cubes on the two rightmost spaces of their endurance bar, which reduce the bar from ten usable spaces to eight. *Stamina cubes* and damage cubes fill the remaining eight spaces as usual (see §3.4). Hollow cubes are not removed by the *Rest* major action (see §10.1), by the *estus flask* (see §3.5, Estus Flask), or by Encounter Recovery. Hollow is removed only by resting at the bonfire (see §11.2) or by becoming *embered* (see §7.3).

A hollow character who dies is *lost*. A lost character is removed from play exactly as any dead character: their souls are dropped, their ember token is discarded, and their model is placed beside the bonfire tile. When a character becomes lost, the encounter is failed at once (see §7.5, Encounter Resolution) and the characters must rest at the bonfire; if the *spark* dial shows zero, the players lose the game (see §7.1). A lost character is not revived by clearing an encounter but only when the characters rest at the bonfire (see §11.2), and the rest removes their hollow cubes as usual.

These rules apply in every encounter, including boss and *mega-boss* encounters. Death in a PvP encounter has no cost (see §20.7).

## 7.3 Embering

A character becomes *embered* by discarding an *ember card* from their back-up slot (see §4.4). The card may be discarded as the *Ember* major action during an encounter (see §10.1) or at any time outside an encounter.

To ember a character:

1. Discard the ember card.
2. Remove every *damage cube* from the character's *endurance bar*.
3. Remove the character's *hollow cubes*, if present.
4. Place an *ember token* in the ember slot of the character's dashboard (see §3.5, Ember).

When an embered character suffers three or more damage from a single attack, the character reduces that damage by one. An embered character may call a *summon* before a boss encounter (see §12.1). Embered characters draw *invaders* into their encounters (see §12.2).

An embered character cannot hold an ember card. If a character becomes embered while holding an ember card, that character must at once give the card to a character who is neither embered nor holding an ember card. If no such character exists, the card is returned to the tier one shop (see §6.3).

The ember token stays on the dashboard until the character dies (see §7.2); it is not removed by resting at the *bonfire*. When a boss is defeated, every character becomes embered without discarding an ember card (see §16.5).

## 7.4 Sparks

*Sparks* are the party's shared resource and are tracked on the *spark* dial (see §6.4). The party begins the game with sparks equal to six minus the number of characters.

Each time a *mini-boss*, *main-boss*, or *mega-boss* is defeated, the party gains one spark (see §16.5), and the characters then rest at the *bonfire* without spending a spark. Resting at the bonfire at any other time costs one spark (see §11.2). In the standard game sparks cannot be gained in any other way; campaign play varies these rules (see §18.3).

The party cannot rest at the bonfire while the spark dial shows zero. If the characters are required to rest while the dial shows zero, the players lose the game (see §7.1).

## 7.5 Encounters

An *encounter* is a battle fought on an encounter tile against the enemies set out by the tile's *encounter card* (see §2.6). The characters begin at the encounter tile adjacent to the *bonfire* tile and advance one tile at a time towards the boss tile. Boss encounters follow these rules except where the boss rules differ (see §15 and §16); PvP encounters follow their own rules (see §20).

### Encounter Start

The party may skip an encounter whose encounter card carries a black cube (an encounter marked *cleared*). Each character places one *stamina cube* on their *endurance bar* for each encounter skipped since the party last fought an encounter or rested at the bonfire, to a maximum of three. The cubes are placed when the characters enter the next encounter they fight.

The party may skip only if every character has enough free spaces on their endurance bar for the required stamina cubes (see §3.4). A skipped encounter is not fought and awards nothing.

*Example.* The first three encounters are marked cleared. The party skips all three and enters the fourth encounter. Each character begins the fourth encounter with three stamina cubes on their endurance bar.

When the characters arrive at an encounter tile:

1. Turn the tile's encounter card face up, if it is face down.
2. If the encounter card carries a black cube, the party may skip the encounter: the characters move on to the next tile and begin again from step 1.
3. Place each character model on an *entry node* of the tile (see §5.1), no more than three models to a node (see §5.3).
4. Place one stamina cube on each character's endurance bar for each encounter skipped since the party last fought or rested, to a maximum of three.
5. Place the enemy models, scaled for the number of characters (see §8.3), on the spawn nodes and the *terrain* tokens on the terrain nodes shown on the encounter card (see §5.1 and §5.5).
6. If the encounter card shows the trap icon, deal *trap tokens* (see §5.5, Traps).
7. If *invaders* are in play, reveal the tile's invader token (see §12.2).
8. If *crystal lizards* are in play and the encounter card shows the crystal lizard symbol, place the crystal lizards (see §14).
9. Place one face-down treasure card from the treasure deck of the current tier (see §6.2) beneath each *chest* token placed on the tile for the first time.
10. Place the *aggro token* on the character with the highest *threat* {{icon:ast-0026-threat-level}}. If two or more characters share the highest threat, the players choose which of them takes the aggro token and the order in which the tied characters take their *turns*; the order is kept for the whole encounter.

### Encounter Turn Order

An encounter is fought in *rounds*. In each round every enemy model takes a turn, then every character takes a turn. Rounds continue until every enemy model has been killed or the encounter is *failed* (see §7.5, Encounter Resolution).

Enemy models take their turns one at a time in descending threat order (see §9.1). If two or more enemy models share a threat value, the model nearest to a character takes its turn first. If those models are equidistant from the nearest character, the model with the most *wound tokens* takes its turn first. If they are still tied, the players choose which takes its turn first.

Characters then take their turns one at a time in descending threat order (see §10.1), in the order settled at Encounter Start. A dead character takes no turn. An invader takes a turn after each character's turn (see §12.2). In boss encounters the boss and the characters alternate turns (see §16.1).

The aggro token marks the character targeted by enemy behaviours that bear the skull icon (see §9.3). After the last character's turn of each round, the aggro token moves to the character who inflicted the most damage on enemy models during that round, counting wound tokens placed and damage recorded on an invader's health dial. If two or more characters tie for the most damage, or no character inflicted damage, the aggro token stays with its holder.

When the character holding the aggro token dies, the token moves at once to the living character with the highest threat; the players settle ties. In boss encounters the aggro token moves after any damage to the boss (see §16.4).

### Encounter Resolution

An encounter ends in one of two ways. The encounter is cleared when every enemy model has been killed and at least one character is alive; crystal lizards do not count (see §14). The encounter is failed when every character has died, or when a *hollow* character dies and is *lost* (see §7.2). A failed encounter awards no *souls* and no treasure.

An encounter is cleared for the first time while the treasure cards dealt to its tile at setup still lie on the tile (see §7.7). When an encounter is cleared for the first time:

1. Return to each surviving character their own *dropped souls* from the tile (see §7.6).
2. Award each character, including each character who died, the full soul reward for the encounter's level (see §7.6).
3. Give each character, including each character who died, one of the treasure cards dealt to the tile (see §7.7).
4. If the tile holds an unopened chest, open it and award its treasure card (see §7.7).
5. If the tile holds a *gravestone* {{icon:ast-0017-gravestone}}, the players may *scry* one card.
6. Place a black cube on the encounter card to mark it cleared.
7. Recover (see §7.5, Encounter Recovery).

If *mimics* are in play and the tile holds an unopened chest, the characters decide whether to open it before step 1, and a mimic that appears is fought before any reward is collected (see §13).

When an encounter is cleared again after its treasure cards have been collected, the same steps are followed with two differences: in step 2 each character gains the *reduced reward* instead of the full reward (see §7.6), and step 3 is omitted, because a repeated clear awards no treasure. This is so whether or not the encounter card carries a black cube: an encounter that was cleared, later failed, and then cleared again is a repeated clear, and step 6 marks it cleared once more.

When an encounter is failed:

1. Place all of each living character's souls on the tile, in a pile separate from any souls already there (see §7.6).
2. Turn the encounter card face down and remove its black cube, if it has one.
3. Rest at the bonfire (see §7.5, Encounter Recovery).

**Reset.** The state of an encounter after the characters have rested at the bonfire: its encounter card is face down, its enemy models have been removed, and its terrain tokens remain in place (see §11.5).

When the characters rest at the bonfire, every encounter is *reset* (see §11.5), except a cleared *Level 4 encounter*, which is not fought again (see §6.7). A cleared encounter keeps its black cube through a reset; when the characters next enter its tile, they may skip it or fight it again for the reduced reward (see §7.5, Encounter Start). A failed encounter has no black cube and must be fought.

**Scry.** To reveal one hidden card and then either return it to its place or send it away.

When an encounter containing a gravestone is cleared, the players may scry one card of their collective choice (see §5.5, Gravestones). The card is one of the following.

- The top card of either treasure deck. The players reveal it and either return it face down to the top of that deck or place it face down at the bottom of that deck.
- One face-down encounter card. The players reveal it and either return it face down to its tile or replace it with the top card of the encounter deck of the same level, placing the revealed card face down at the bottom of that deck.
- The top card of the next boss's behaviour deck (see §15.5). The players reveal it and either return it face down to the top of that deck or place it face down at the bottom of that deck.

### Encounter Recovery

Recovery follows every cleared encounter. If mimics are in play and the tile holds an unopened chest, recovery is deferred until the characters have decided whether to open it (see §13).

Each character who survived the encounter recovers as follows.

1. Remove all condition tokens from the character (see §8.5).
2. Remove all stamina cubes from the character's endurance bar.
3. Remove one *damage cube* from the character's endurance bar.

Each character who died in the encounter is revived hollow as follows.

1. Place the character's model upright on the tile beside the surviving characters.
2. Remove all condition tokens, stamina cubes, and damage cubes from the character.
3. Place two *hollow cubes* on the two rightmost spaces of the character's endurance bar (see §7.2).

Recovery does not ready the *estus flask*, *luck*, or *heroic action* tokens, and does not remove the hollow cubes of a character who was already hollow; only resting at the bonfire does so (see §11.2). A revived character's dropped souls stay on the tile (see §7.6).

When an encounter is failed, the characters must rest at the bonfire. If the *spark* dial shows zero, the characters cannot rest and the players lose the game (see §7.1). Otherwise the party spends one spark and rests (see §11.2): every character, including each dead or lost character, is placed on the bonfire tile and fully restored, and every encounter is reset (see §11.5).

After recovery the party chooses either to advance to the next encounter tile (see §7.5, Encounter Start) or to return to the bonfire tile and rest, spending one spark (see §7.4). After a boss is defeated, the characters rest without spending a spark (see §16.5).

## 7.6 Souls

*Souls* are the game's currency. Each character keeps their own souls as soul tokens on their dashboard. Souls cannot be transferred between characters. Souls are spent while resting at the *bonfire* (see §11.3 and §11.4). The one exception is the cost of calling a *summon* at the *fog gate*, which is paid before a boss encounter (see §12.1).

When an *encounter* is *cleared* for the first time, every character, including each character who died in it, gains the full soul reward for the encounter's level. When an encounter that has been cleared before is cleared again, every character gains the *reduced reward* instead, whether or not its encounter card still carries a black cube (see §7.5, Encounter Resolution).

**Reduced reward.** Half the full soul reward, rounded down.

When a boss is defeated, every character gains the boss reward (see §16.5). When an *invader* is killed, every character gains the invader reward in addition to the encounter reward (see §12.2). The rewards of the standard game are as follows; campaign play uses its own table (see §18.5).

| Encounter | Full reward per character | Reduced reward per character |
|---|---|---|
| Level 1 encounter and standard *invader* | 3 | 1 |
| Level 2 encounter and advanced *invader* | 4 | 2 |
| Level 3 encounter | 5 | 2 |
| Level 4 encounter and bosses | 6 | 3 |

The reduced reward applies to encounters only; invaders and bosses are rewarded in full.

**Dropped souls.** Souls placed on an encounter tile by a character who died there or, when an encounter was *failed*, by a living character.

When a character dies, all of the souls on their dashboard are dropped on the tile where they died, in a pile separate from any other character's *dropped souls* (see §7.2). When an encounter is failed, every living character also drops all of their souls on that tile (see §7.5, Encounter Resolution). Dropped souls stay on the tile through every *reset*. The souls a character drops at death are not forfeited by that death.

Only the character who dropped the souls may reclaim them, and only by surviving an encounter on that tile that ends cleared; the character retrieves them during Encounter Resolution (see §7.5, Encounter Resolution). A character who is dead or *lost* when the encounter is cleared does not retrieve them. If the character who dropped the souls dies before reclaiming them, the dropped souls are returned to the supply; souls dropped at the moment of that death remain on the tile.

*Example.* The Knight dies in the second encounter, a Level 2 encounter, holding seven souls, which are placed on that tile. The Herald survives and the encounter is cleared, so the Knight is revived hollow and gains the four souls of the full reward, but the seven souls stay on the tile. The party rests at the bonfire, returns, skips the first encounter, and fights the second again. The Knight survives and the encounter is cleared, so the Knight retrieves the seven souls and gains the reduced reward of two souls.

## 7.7 Treasure Rewards

Treasure cards (see §2.5) are gained as the reward for clearing an *encounter* for the first time, from a *chest* {{icon:ast-0009-treasure-chest}}, from a killed *invader* or *mimic*, from a killed *crystal lizard*, and from a defeated boss. A treasure card a character receives is placed in that character's inventory (see §4.1).

When an encounter is *cleared* for the first time, each character, including each character who died in it, takes one of the treasure cards dealt face down to that tile at setup (see §6.5 and §6.6). The dealt cards are the whole reward; no cards are drawn from the treasure decks at that time. The players decide which character takes which card; if they cannot agree, the character holding the *aggro token* decides.

An encounter cleared again awards no treasure. In the standard game the cards dealt before the *mini-boss* is defeated come from the *tier one treasure* deck and the cards dealt afterwards from the *tier two treasure* deck (see §6.2).

When an encounter containing an unopened chest is cleared, the chest is opened: flip the chest token to its open side and reveal the treasure card beneath it (see §5.5, Chests). The card is awarded to the party. If mimics are in play, a chest is opened only as the mimic rules describe, and the encounter is not resolved until the characters have decided whether to open it (see §13). A killed mimic awards two treasure cards in place of the chest's one (see §13).

Whenever a treasure card is awarded to the party rather than to a named character (a chest's card, a mimic's cards, a boss treasure card, or the *mega-boss* treasure card of a Level 4 encounter), the players decide which character receives it. If they cannot agree, the card goes to the character who holds the aggro token when the encounter ends.

If crystal lizards are in play, a character who kills a crystal lizard takes one Titanite Scale card at once (see §14). A killed invader awards its treasure (see §12.2).

When a boss is defeated, the party is awarded one of that boss's treasure cards, drawn at random (see §16.5). The treasure reward of a Level 4 encounter is the mega-boss treasure card dealt to its tile (see §6.7).
