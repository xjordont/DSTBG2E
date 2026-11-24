# 7. Gameplay

## 7.1 Objective and Loss Conditions

- The players win when the final boss is defeated. The victory is shared.
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
  - Hollow cubes are removed by a *rest* at the bonfire or by an ember.
- A hollow character who dies is *lost*: out of play until the party next rests at the bonfire.

## 7.3 Embering

- A character discards an *ember* card to become *embered* (see §4.4).
  - Remove all damage cubes.
  - Remove all *hollow* cubes.
  - Place the ember token on the character's dashboard.
- While a character is embered:
  - If the character suffers three or more damage from one attack, reduce that damage by one.
  - With the Phantoms expansion, the character may call a *summon* before a boss encounter (see §12.1) and provokes *invaders* (see §12.2).
- The ember token stays on the dashboard until the character dies.
- When a boss is defeated, every character becomes embered without discarding a card.

## 7.4 Sparks

- The party begins with *sparks* equal to five less the number of characters.
- Each boss defeated adds one spark.
- Sparks cannot be gained by any other means, unless an *event card* gives one.
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
5. With the Events Expansion II, reveal the tile's *event card*.
6. Place the enemy models on the *spawn nodes* and the terrain on the *terrain nodes* that the encounter card shows. Each icon on the card matches the icon printed on a node of the tile. Deal *trap* tokens to a trapped encounter that has none yet (see §5.5).
7. Place one face-down treasure card under each *chest* {{icon:ast-0009-treasure-chest}} placed for the first time. Draw from the *tier one* treasure deck before the *mini-boss* is defeated and from the *tier two* treasure deck afterwards.
8. Place the *aggro* token on the character with the highest *threat* {{icon:ast-0059-taunt}}. The party settles a tie.

### Encounter Turn Order

An encounter is fought in rounds.

1. Each enemy model takes a turn, one by one, in descending threat.
   - If several enemies share a threat value, the one closest to a character takes its turn first.
   - If those enemies are equally close, the one with the most wound tokens takes its turn first.
   - If they are still tied, the players decide.
2. Each character takes a turn, in any order the party chooses each round.
3. Rounds continue until every enemy model is dead or the encounter is *failed*.

Whenever a character deals damage, the aggro token passes to that character. If no character deals damage, it stays where it is.

A boss and an *invader* take their turns between the characters' turns (see §16.1, §12.2).

### Encounter Resolution

- An encounter is cleared when every enemy model has been killed.
- An encounter is failed when two characters have died in it, or when its last character dies.
- An encounter is on its first clear while the two treasure cards dealt to its tile still lie there. They stay on the tile until the party takes them.
- When an encounter is cleared, resolve it as follows.
  1. Each character takes back their dropped souls (see §7.6).
  2. Each character gains the soul reward for the encounter's level, those who died in the encounter included.
  3. On a first clear, the party takes the tile's two treasure cards. A reset encounter fought again gives no treasure.
  4. The party takes the treasure card under each chest it opens (see §5.5).
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
  - Place two hollow cubes on the endurance bar (see §3.4).
- *Estus flask*, *luck* and *heroic action* tokens are not restored.
- The hollow cubes of a character who was already hollow stay.
- The party then goes on to the next tile. Before it does, it may rest at the bonfire or visit Blacksmith Andre (see §11.4).

### Event Cards

The Events Expansion II (see §2.6) is in play if the players have it. Its cards are used as printed, but for five whose text is changed in the print-and-play file kept with this book. A card overrides this book where the two differ.

- The event card beside an *encounter card* is revealed each time the party enters that tile and is resolved as its text says. Its effect lasts for that encounter unless the card gives another end.
- When the encounters are *reset*, gather every revealed event card. A card with the discard icon is set aside until a boss is defeated. The others are shuffled back into the decks of their levels. Then deal a new card face down to each of those encounters that has never been *cleared*. A cleared encounter has no event card.
- Six cards bring a traveller to the *bonfire*: Rebirth, Maiden of the Sable Church, Loyal Swindler, Transposition, Draw Out True Strength and The Great Deceiver. Such a card stays beside the bonfire tile for the rest of the game. A traveller is visited whenever the party may visit Blacksmith Andre.
- The expansion's treasure cards never enter a treasure deck or the *shop*. All six Purging Stones are Yuria's (Maiden of the Sable Church): she sells no more than four for each boss and gives the Irreverent Morion Blade as her card says. Patches (The Great Deceiver) sells the Red Tearstone Ring, Divine Blessing, Great Heal Excerpt and the Horsehoof Ring, and the three Masks once his card allows.
- A Hollowing card limits each character's *endurance bar* to the number of spaces it names, *hollow* cubes included. Only one Hollowing card applies at a time. A Purging Stone removes that limit, and every hollow cube, from the character who uses it.
- A node diagram is read with the foot of the card towards the *entry nodes*.
- A card that calls for an *invader* or a *mimic* is discarded and replaced if the players lack the Phantoms or the Explorers expansion.
- A cost in *souls* is paid by one character, and a reward in souls goes to each character. The treasure deck is the deck of the current tier. A party that is defeated or perishes has *failed* the encounter. An activation is a turn, health gained is damage removed, a stamina bar is the endurance bar, taunt is *threat*, and both green icons are *poison*.
- Reparations is fought by the rules of player versus player (see §20.2). Dying in it carries no penalty, and the encounter is then cleared.

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

- The party decides which character takes each treasure card it gains. If it cannot agree, the character holding the *aggro* token decides. This holds for every shared reward in the book.
- A treasure card goes into the *inventory* of the character who takes it.
- With the Explorers expansion, a *chest* may hide a *mimic*. The party decides whether to open the chest before it recovers or collects any reward (see §13).
- With the Iron Keep expansion, a *crystal lizard* killed during the encounter gives *Titanite* (see §14).
