<!-- manuscript.md lines 1481–1659 ; chapter "COMBAT BASICS" -->
# COMBAT BASICS

## Target versus Hit

When a character or an enemy attacks, the model defending the attack is considered the attack’s target. Attacks have a single target by default but some attacks have special modifiers that allow them to target all models on a node or multiple nodes. Characters may only target other characters if playing a PvP encounter per the optional rules detailed later. Enemies never target other enemies.

A model is considered hit by an attack even if the attack deals zero damage so long as the attack was in range and the target model did not successfully dodge the attack. Therefore, targets who successfully *dodge* an attack are not considered hit and therefore are not pushed or afflicted with conditions associated with being hit by the attack.

## Enemy Data Cards

Each enemy type in the game has a data card breaking down how it works in the game. Enemy data cards give the information necessary to activate that enemy or to resolve a character’s attack against it.

Each enemy data card includes the following information:

1.  Name

2.  Threat level

3.  Attack range

4.  *Dodge* difficulty

5.  *Block* and *resist* values

6.  Behaviour icons

7.  Base health

8.  Enemy icon

9.  Set symbol

The behaviour icons are the core element of any enemy which determine how the enemy behaves during its turn.

An enemy’s threat level determines the order in which it takes a turn in combat with higher values taking their turn first. The attack range is the maximum range at which the enemy model can attack characters. The dodge difficulty determines how hard it is for characters to dodge the attack. The enemy’s block value reduces the damage it suffers from physical attacks, and its resist value reduces the damage it suffers from magical attacks.

An enemy’s base health is how much damage the enemy can suffer before being defeated in a single character game. When playing with more than one character, calculate a scaled health value by adding one health for each character (including dead characters) in play. When an enemy suffers damage, place one wound token on the base of that enemy model for each point of damage not prevented by the enemies *block* or *resist*. Once an enemy model has wounds equal to (or exceeding) its scaled health, it is considered killed and removed from the tile.

## Enemy Scaling

- Non-boss enemies gain benefits depending on the number of total characters in a game to ensure balance.

  - Increase each non-boss enemy’s base health by the number of characters (including dead characters) beyond one.

  - If playing with two or more characters, increase any non-boss enemy behaviour of one movement to two movements.

  - If playing with three or more characters, increase all non-boss attack values by one.

  - If playing with four characters, add *repeat to* each non-boss enemy's attack behaviour.

- Boss enemies (mini, main, and mega) do NOT modify their base health or receive scaling benefits otherwise.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Character</p>
<p>Number</p></th>
<th><p>Enemy</p>
<p>Health</p></th>
<th>Enemy Movement</th>
<th><p>Enemy</p>
<p>Damage</p></th>
<th><p>Enemy Attack</p>
<p>Repeats</p></th>
</tr>
<tr class="odd">
<th>1</th>
<th>Base Health</th>
<th>-</th>
<th>-</th>
<th>-</th>
</tr>
<tr class="header">
<th>2</th>
<th>Base + 1</th>
<th>1 -&gt; 2</th>
<th>-</th>
<th>-</th>
</tr>
<tr class="odd">
<th>3</th>
<th>Base + 2</th>
<th>1 -&gt; 2</th>
<th>+1</th>
<th>-</th>
</tr>
<tr class="header">
<th>4</th>
<th>Base + 3</th>
<th>1 -&gt; 2</th>
<th>+1</th>
<th><em>Repeat</em> 2</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Pushing

Certain movements and attacks are labelled as push-movements and push-attacks (respectively). These special push effects may push a model from its current node to an adjacent node. Push movement does not cost stamina.

Boss models cannot be pushed by a character’s movement or attack. The only way a boss model can be pushed is if another boss model moves onto its node.

If the push icon appears on an attack, the model(s) hit by the attack are pushed. The pushed model(s) must move to the adjacent node most directly opposite of the attacking model. If there are multiple adjacent nodes equally opposite to the attacking model the players choose the node. A model being pushed directly into a corner remains on the corner node.If the attacker is on the same node as the model hit by the push attack, the players choose any adjacent node for the model to be pushed into.

If the push icon appears on an enemy’s movement, first immediately move each character on that enemy’s node onto an adjacent node chosen by the players. Then, the enemy moves one node in the direction dictated by the enemy or boss data card. If a push-movement causes the enemy to move onto a node that contains any character(s), the character(s) must move to the adjacent node most directly opposite to the direction from which the enemy model is push-moving. In other words, a character being pushed by an enemy's push-movement must move into the adjacent node further from the node the enemy started their movement on. If there are multiple valid nodes the players choose which node the character is pushed into. If an enemy performing a push-movement moves multiple times as part of their move, the above process is repeated separately for each single node moved.

Players should take note that only enemy behaviours that deal damage can be dodged. Therefore, only enemy behaviours with an associated attack value can be dodged to permit the character to avoid the associated push effect. Of course, characters who block or resist a push behaviour are pushed regardless of damage dealt.

## Conditions

Some attacks inflict conditions on their target. When an attack has a condition icon, place the corresponding condition token on the model(s) hit by that attack. When a model ends its turn, remove one poison token and any *frostbite*/*stagger* tokens. Each condition has its own rules and effects listed below.

### *Bleed*

- *Bleed* tokens are limited to one per model.

- *Bleed* tokens are not removed at the end of activations.

- *Bleed* tokens are only removed at the end of the encounter.

- If a second *bleed* token would be placed on a model, deal three damage and remove all *bleed* tokens from that model.

- *Bleed* damage is not affected by *block* or *resist*.

### *Poison*

- *Poison* tokens are not limited to one per model.

- A model suffers one damage for each *poison* token it has at the end of its activation, then removes only one *poison* token.

- *Poison* damage is not affected by *block* or *resist*.

### *Frostbite*

- *Frostbite* tokens are limited to one per model.

- *Frostbite* affected characters cannot recover stamina.

- *Frostbite* affected enemies reduce their movement values by one.

- *Frostbite* tokens are removed at the end of the model’s turn.

### *Stagger*

- *Stagger* tokens are limited to one per model.

- *Staggered* models subtract one from *attack*, *block*, *resist*, and *dodge*.

- *Stagger* tokens are removed at the end of the model’s turn.

### *Calamity (*Kalameet Expansion*)*

- *Calamity* tokens are limited to one per model.

- *Calamity* reduces a model’s *block*, *resist*, and *dodge* roll results by one.

- *Calamity* tokens are not removed at the end of a model’s turn.

- *Calamity* tokens are only removed at the end of the encounter.

### *Corrosion (*Gaping Dragon Expansion*)*

- *Corrosion* tokens are limited to one per model.

- *Corrosion* tokens reduce the affected model’s block roll results by one.

- *Corrosion* tokens are not removed at the end of a model’s turn.

- *Corrosion* tokens are removed if the affected character takes damage.

