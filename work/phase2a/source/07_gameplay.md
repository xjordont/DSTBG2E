<!-- manuscript.md lines 1197–1480 ; chapter "GAMEPLAY" -->
# GAMEPLAY

## Objective & Loss Conditions

The players lose collectively if at any point, all characters are dead and there are no remaining sparks to revive them. The players win if any character survives to defeat the selected final boss. By default, the final boss will be a main-boss and the players share victory. Players may choose to extend their adventure by adding a mega-boss after the main-boss to serve as the final boss instead. Players may also choose to add a player versus player (PvP) encounter after the final boss is defeated to determine a single intimate victor. Players should agree on whether they will include a mega-boss and/or PvP encounter during set-up.

## Death & Hollowing

- Characters die whenever they cannot add a damage cube to their endurance tracker because it is already full. Upon death, a character is temporarily removed from play.

  - Drop all *souls* from the dashboard onto the current encounter tile.

  - Remove the *ember* token from the dashboard if present.

  - Place the character model on its side next to the bonfire.

- If any character survives to *clear* an encounter, then the characters who died in that encounter are revived in a *hollow* state.

  - Place two white cubes on the right side of the stamina bar.

  - *Hollow* status reduces the total endurance of the character by two.

  - *Hollow* status cannot be removed by rest actions or healing.

  - *Hollow* status is only removed by using a *spark* or an *ember* token.

- If all characters die before the end of an encounter, or any character with *hollow* status dies, then the characters are forced to immediately spend one *spark* and rest at the *bonfire*.

## Embering

- *Ember* cards may be discarded as an action to *ember* a character.

  - Remove all damage cubes.

  - Remove all *hollow* cubes.

  - Place the *ember* token on their character dashboard.

- *Embered* characters are affected in multiple ways:

  - If suffering greater than two damage from an attack, reduce damage by one.

  - Phantoms can be summoned before a boss encounter.

  - Invaders will attempt to kill the characters.

  - Characters cannot carry an *ember* card while *embered*.

## Sparks

- Players begin *sparks* equal to six minus the number of characters.

- Defeating a mini-boss or main-boss provides one additional spark.

- Sparks can not be gained by any other means.

- Resting at the *bonfire* costs one *spark*.

## Encounters

### Encounter Start

1.  Characters start with the encounter closest to the *bonfire* tile and advance tile-by-tile towards their ultimate goal of the boss tile.

2.  Characters may skip previously *cleared* encounters at the cost of two stamina cubes placed in the endurance bar of each character.

    1.  For example, if the first three encounters are marked *cleared* then the characters could skip to the fourth encounter but would all start with 6 stamina expended.

3.  Characters enter an encounter tile by placing their models on one of the tile’s entry nodes. The basic nodes along the wall adjacent to the previous encounter tile are considered entry nodes. Only three characters can start on the same entry node due to node model limits.

4.  Reveal the tile’s encounter card, if not already revealed.

5.  Reveal the tile’s event card, if not already revealed.

6.  Populate the tile with enemies and terrain per encounter card directions.

7.  Place one face-down treasure card from the appropriate treasure deck underneath any newly revealed chest tokens. Draw from the tier one treasure deck before the mini-boss is defeated and tier two treasure deck thereafter.

8.  Place the *aggro* token on the character with the highest threat value.

9.  Place the *first player* token on the character with the highest threat value.

### Encounter Turn Order

1.  Each enemy model takes a turn one-by-one in descending *threat* value.

    1.  If multiple enemy models share a *threat* value, the closest model to a character model takes its turn first.

    2.  If multiple enemy models of the same *threat* order are equidistant to a character model, the model with the most damage tokens takes its turn first.

    3.  If multiple enemy models of the same *threat* order and damage are equidistant to a character model, the players may decide which model takes its turn first.

2.  Each character takes their turn one-by-one in descending *threat* value.

3.  After all characters have taken their turn, place the *aggro* token on the character who placed the most damage tokens on enemy models.

    1.  If multiple characters inflicted the same number of damage tokens, then the *aggro* token remains on the same character.

4.  Continue alternating between enemies and characters until either all enemy or character models are defeated.

### Encounter Resolution

- Encounters end in one of three ways:

  - Encounters are *cleared* if all enemy models are defeated.

  - Encounters are *failed* if either all characters die.

  - Encounters are *failed* if any character with *hollow* status dies.

- Encounters *cleared* for the first time resolve as follows:

  - Characters who died must drop their *souls* on that encounter tile.

  - Characters who survived retrieve their dropped *souls* from that tile.

  - Characters gain *soul* rewards and one treasure card each.

  - Mark the encounter card *cleared* with a black cube.

  - *Cleared* encounters are reset when characters rest at the *bonfire*.

  - *Cleared* encounters may be skipped thereafter.

- Encounters *cleared* that have already been *cleared* resolve as follows:

  - Characters who died must drop their *souls* on that encounter tile.

  - Characters who survived retrieve their dropped *souls* from that tile.

  - Characters gain *soul* rewards but not treasure.

- Encounters *failed* resolve as follows:

  - Characters must all drop their *souls* on that encounter tile.

  - *Failed* encounters do not reward *souls* or treasure.

  - *Failed* encounters flip their encounter card face-down.

  - *Failed* encounters are reset when characters rest at the *bonfire*.

  - *Failed* encounters may not be skipped once reset.

  - *C*haracters are forced to rest at a bonfire at the cost of a *spark*.

### Encounter Recovery

- Characters who survive to *clear an* encounter recover:

  - Remove one damage cube from each character.

  - Remove all stamina cubes from each character.

  - Remove all condition tokens from each character.

  - *Estus flask*, *luck*, and *heroic action* tokens are not restored.

  - *Hollow* status is not removed.

- Characters who died in a *cleared* encounter are revived:

  - Place the character model upright with the surviving characters.

  - Remove all damage and stamina cubes from the character.

  - Remove all condition tokens from the character.

  - *Estus flask*, *luck*, and *heroic action* tokens are not restored.

  - Mark the character *hollow* with two white cubes on the rightmost spaces of the endurance bar.

- All characters must rest at the bonfire if an encounter is *failed:*

  - Spend one *spark*.

  - Place all character models upright on the bonfire tile.

  - Remove all damage and stamina cubes from all characters.

  - Remove all condition tokens from all characters.

  - Remove all *hollow* tokens from all characters.

  - *Estus flask*, *luck*, and *heroic action* tokens are restored.

## Souls

- Characters track their personal supply of *souls* by placing *soul* tokens on their character dashboard.

- *Souls* cannot be transferred between characters.

- Upon successfully *clearing* an encounter that has not been previously *cleared*, reward the full *soul* reward to each character.

- Upon successfully *clearing* an encounter that has been previously *cleared*, reward the reduced *soul* reward to each character.

- Successfully defeated invaders provide additional *souls* per player.

- When a character dies, drop all of the *souls* from their character dashboard onto the encounter tile they died on separate from other characters’ dropped *souls*.

- The character who dropped them by successfully clearing or mastering the encounter on which they were dropped can reclaim dropped souls.

- Dropped *souls* are lost forever if the character who dropped them dies before reclaiming the *souls*.

### Soul Reward Table

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><p><em>Soul</em> Reward</p>
<p>per characteri</p></th>
</tr>
<tr class="odd">
<th><p>Level 1 Encounter</p>
<p>&amp;</p>
<p>Standard Invaders</p></th>
<th><strong>3</strong></th>
</tr>
<tr class="header">
<th><p>Level 2 Encounter</p>
<p>&amp;</p>
<p>Advanced Invaders</p></th>
<th><strong>4</strong></th>
</tr>
<tr class="odd">
<th>Level 3 Encounter</th>
<th><strong>5</strong></th>
</tr>
<tr class="header">
<th><p>Level 4 Encounter</p>
<p>&amp;</p>
<p>Bosses</p></th>
<th><strong>6</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

##  

## Treasure Rewards

- Treasure is awarded to the characters when they have successfully *cleared* an encounter that has not been previously marked as *cleared.*

  - Characters are awarded one treasure each.

  - Characters receive their treasure card reward even if they died.

  - Draw cards from the Tier one treasure deck before defeating the mini-boss, and Tier two treasure deck thereafter.

- Treasure is awarded to the characters if they successfully *clear* an encounter with an unopened chest token.

  - If playing with *mimics*, determine if a mimic is encountered and fight immediately before encounter recovery is resolved.

  - Flip the chest token to the opened side.

  - Reveal the treasure card placed face-down under the chest token.

  - Players decide which character should receive this treasure. If the players cannot decide, the treasure will be awarded to the character who ended the encounter with the *aggro* token.

- If playing with the option of mimics, any character who survives to open a chest risks being ambushed by a mimic.

  - If there is at least one surviving character on an encounter tile with a chest they may decide to open the chest or leave it closed.

  - The characters do not recover stamina, remove damage, draw treasure, or collect souls until a decision is made.

  - If any surviving character wishes to open a chest after an encounter ends, they must reveal the ambush card beside that encounter. If they choose to leave the chest closed they recover normally and then continue on to the next encounter.

  - If the ambush card shows treasure, they collect one treasure card from the appropriate tier treasure deck. They then recover and proceed to the next encounter normally.

  - If the ambush card shows a mimic, set up a mimic mini-boss encounter immediately. If a mini-boss has not been defeated, use the hungry mimic. If a mini-boss has already been defeated, use the voracious mimic.

  - Characters remain in the nodes they ended the encounter in and the mimic attacks with combat proceeding the same as any other mini-boss encounter. See the detailed rules on mimics later in these rules for details.

- If playing with the option of *crystal lizards*, award a Titanite Chunk card to any character who killed a *crystal lizard* during the encounter.

- If a boss was defeated the characters are awarded one of the treasure cards marked with the defeated boss’s icon drawn at random. Players decide which character should receive the treasure. If the players cannot decide, the treasure will be awarded to the character who ended the encounter with the *aggro* token.

