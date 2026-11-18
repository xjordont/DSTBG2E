# 7. Gameplay

## 7.1 Objective and Loss Conditions

- The players win if any character survives to defeat the final boss. The victory is shared.
- The final boss is the *main-boss*, or the *mega-boss* if the party chose one at setup.
- With two or more characters, a player versus player (PvP) encounter is fought after every boss (see §20).
- The players lose if an encounter is *failed* and no *spark* remains.

## 7.2 Death and Hollowing

- A character who dies is removed from the encounter and takes no further turns in it.
  - The character keeps their *souls*.
  - Remove the *ember* token from the dashboard, if present.
  - Place the character model on its side next to the *bonfire*.
  - If the character held the *aggro* token, it passes to the living character with the highest *threat*.
- If the encounter is *cleared*, the characters who died in it return *hollow* (see §7.5).
  - A hollow character has two hollow cubes on the *endurance bar* (see §3.4).
  - Hollow cubes are removed only by a *rest* at the bonfire or by an ember.
- A hollow character who dies is *lost* until the party next rests at the bonfire. The other characters fight on.

## 7.3 Embering

- A character discards an *ember* card to become *embered* (see §4.4).
  - Remove all damage cubes.
  - Remove all *hollow* cubes.
  - Place the ember token on the character's dashboard.
- While a character is embered:
  - If the character suffers three or more damage from one attack, reduce that damage by one.
  - The character cannot buy or use an ember card (see §4.4).
  - With the Phantoms expansion, the character may call a *summon* before a boss encounter (see §12.1) and provokes *invaders* (see §12.2).
- The ember token stays on the dashboard until the character dies.
- When a boss is defeated, every character becomes embered without discarding a card.

## 7.4 Sparks

- The party begins with *sparks* equal to five less the number of characters.
- Each boss defeated adds one spark.
- Sparks cannot be gained by any other means.
- A *rest* at the *bonfire* costs one spark (see §11.2).

## 7.5 Encounters

### Encounter Start

1. The party fights the encounters in order, from the tile closest to the *bonfire* towards the boss tile.
2. A *reset* encounter that has been *cleared* before carries a black cube on its *encounter card*. The party may fight it again, any number of times over the game, or skip it.
   - To skip, each character suffers one damage and the party passes through to the next tile. A skipped encounter gives no *souls* and no treasure.
   - Several encounters may be skipped one after another, each at the same cost.
   - The party cannot skip while any character's *endurance bar* is full.
   - A *failed* encounter cannot be skipped. Once reset, it must be fought.
3. The characters enter the tile by placing their models on its *entry nodes* (see §5.1). No more than three characters may start on the same node.
4. Reveal the tile's encounter card. With the Phantoms expansion, flip the tile's *invader* token first (see §12.2).
5. With a 2022 core set (Tomb of Giants, Painted World of Ariamis or The Sunless City), reveal the tile's *event card* the first time the party enters the tile.
   - An immediate card is resolved and discarded.
   - A consumable card is taken by one character.
   - A rendezvous card stays on the tile and applies to that encounter.
   - Where a card names a soul cache, it means the characters' souls, shared as the party chooses. The *inventory* is a character of the party's choice. The next encounter is the tile the card lies on.
   - A card that still cannot be applied is discarded.
6. Place the enemy models on the *spawn nodes* and the terrain on the *terrain nodes* that the encounter card shows. Each icon on the card matches the icon printed on a node of the tile.
7. Place one face-down treasure card under each *chest* {{icon:ast-0009-treasure-chest}} placed for the first time. Draw from the *tier one* treasure deck before the *mini-boss* is defeated and from the *tier two* treasure deck afterwards.
8. Place the *aggro* token on the character with the highest *threat* {{icon:ast-0059-taunt}}. The party settles a tie.

### Encounter Turn Order

Every encounter is fought in rounds, and every round runs in the same order. A step with no model to act is passed over.

1. Each enemy model takes a turn, one by one, in ascending threat: the lowest first.
   - If several enemies share a threat value, the one closest to a character takes its turn first.
   - If those enemies are equally close, the one with the most wound tokens takes its turn first.
   - If they are still tied, the players decide.
2. Each *invader* takes a turn (see §12.2).
3. The boss takes a turn (see §16.1).
4. Each character takes a turn, one by one, in ascending threat: the lowest first, the highest last.
5. Each *summon* takes a turn (see §12.1).

The aggro token passes to the last character to deal damage. If no character deals damage, it stays where it is. Rounds continue until every enemy model or every character is dead.

### Encounter Resolution

- An encounter is cleared when every enemy model has been killed.
- An encounter is failed only when every character is dead.
- An encounter is on its first clear while the two treasure cards dealt to its tile still lie there. They stay on the tile until the party takes them.
- When an encounter is cleared, resolve it as follows.
  1. Each character takes back any souls of their own that lie on the tile.
  2. Each character gains the soul reward for the encounter's level, those who died in the encounter included.
  3. On a first clear, the party takes the tile's two treasure cards. A reset encounter fought again gives no treasure.
  4. The party takes the treasure card under each unopened chest.
  5. Mark the encounter card with a black cube.
  6. The characters recover.
- When an encounter is failed, resolve it as follows.
  1. Place every character's souls on the tile (see §7.6).
  2. The party gains no souls and no treasure.
  3. Flip the encounter card face down and remove its black cube, if it has one.
  4. The party must spend a *spark* and *rest* at the bonfire.

### Encounter Recovery

- Each character who survives to clear an encounter recovers.
  - Remove all *stamina* cubes.
  - Remove all *condition* tokens.
  - No damage is healed.
- Each character who died in a cleared encounter and is not *lost* returns *hollow*.
  - Place the character model upright with the surviving characters.
  - Remove all damage cubes, stamina cubes and condition tokens.
  - Place two hollow cubes on the two rightmost spaces of the endurance bar.
- *Estus flask*, *luck* and *heroic action* tokens are not restored.
- The hollow cubes of a character who was already hollow stay.
- The party then goes on to the next tile. Before it does, it may rest at the bonfire or visit Blacksmith Andre (see §11.4).

## 7.6 Souls

- Each character tracks their own *souls* by placing soul tokens on their dashboard.
- Souls cannot be given to another character.
- Every soul reward is paid in full to each character.
- When an encounter is *failed*, every character's souls are dropped on that tile, each character's in a separate pile.
- When the party later clears that encounter, each character takes their own souls back.
- If the party fails an encounter where dropped souls already lie, those souls are lost before the new ones are placed.
- Dropped souls still lying on a tile when a boss is defeated go back to their owners.

### Soul Reward Table

| Souls for each character | First clear | *Reset* encounter fought again |
|---|---|---|
| Level 1 encounter | 3 | 1 |
| Level 2 encounter | 4 | 2 |
| Level 3 encounter | 5 | 3 |

- A Level 4 encounter and a boss give six souls.
- A standard *invader* gives three souls and an advanced invader four, in addition to the encounter's reward.

## 7.7 Treasure Rewards

- The first time an encounter is *cleared*, the party takes the two treasure cards dealt face down to its tile at setup (see §6.5).
- When an encounter with an unopened *chest* is cleared, flip the chest token to its open side and take the treasure card under it.
- The party decides which character takes each card. If it cannot agree, the character holding the *aggro* token decides. This holds for every shared reward in the book.
- A treasure card goes into the *inventory* of the character who takes it.
- With the Explorers expansion, a chest may hide a *mimic*. The party decides whether to open the chest before it recovers or collects any reward (see §13).
- With the Iron Keep expansion, a *crystal lizard* killed during the encounter gives *Titanite* (see §14).
- In the standard game no treasure card is handed over for defeating a boss. Each boss's own treasure cards are found in the *tier two* treasure deck.
