# 10. Character Turn

## 10.1 Turn Order

1. Recover one *stamina*.
2. Take any of the *minor actions*, in any order, before or after the major action.
   - *Walk*, once a turn: move to an adjacent *node* at no cost.
   - *Run*: move one further node for each stamina spent.
   - Equip: swap equipment cards among the *back-up slot*, the weapon slots and the armour slot. The *inventory* is closed during an encounter.
   - *Heroic action*: carry out the ability on the dashboard and flip the heroic action token to its used side.
3. Take one *major action*.
   - Attack: use one attack option from the left weapon slot, the right, or both.
   - *Rest*: remove all stamina cubes. A character who runs in a turn cannot rest in it, and a character who rests cannot then run.
   - *Drink estus*: remove all damage cubes and flip the *estus flask* token to its used side. Stamina cubes stay.
   - *Ember*: discard an ember card from the back-up slot to become *embered* (see §7.3).
   - Cast an upgrade *spell* (see §4.2).

At the end of the turn the character's *conditions* take effect (see §8.5).

## 10.2 Character Movement

During an encounter a character moves from *node* to node by a *walk*, a *run*, a *dodge* or a *shift*. Movement is limited by terrain (see §5.5) and by the *node model limit* (see §5.3).

## 10.3 Character Attacks

With the attack action a character may make one attack with the weapon or *spell* in each weapon slot. The two attacks are made one after the other, in either order, each with its own target. Spell attacks are limited further (see §4.3).

To attack, choose an attack option on the *equipped* card, pay its *stamina* cost and name an enemy within the weapon's *range* as the target. Roll the dice shown on the attack option, add up the results and apply any modifiers. The result is the attack value. The player may now use any reroll available, from the *luck* token (see §3.5) or otherwise.

All weapons do physical damage. An attack option marked with the magical damage icon {{icon:ast-0042-deal-magical-damage}}, as on certain weapons and most spells, does magical damage instead. Subtract the enemy's *block* from a physical attack value, or its *resist* from a magical one; both are printed on its *data card*. Place one wound token on the enemy's base for each point of damage left (see §8.2). An attack on a boss also depends on the arc it is made from (see §15.6).

Many weapons simply deal damage. Some have special abilities given in the text on their cards or by icons: the magical damage icon, the *push* icon {{icon:ast-0058-push-affected-enemies}} (see §8.4), the *condition* icons and the icons below.

*Example.* In a game with two characters, the Knight faces a Hollow Soldier with 3 health and a block of 1 on an adjacent *node*. The Knight holds a sword with a range of 1 and nothing in the other weapon slot. The Knight pays one stamina for one of its attack options and rolls two black dice, which show 0 and 2. Wielding the sword *two-handed*, the Knight rerolls the 0 and gets 2. The attack value is 4. Less the block of 1, the Hollow Soldier takes three wound tokens and dies.

### Range

Some attack options show a range {{icon:ast-0060-attack-range}} that differs from the range of their weapon. That range replaces the weapon's range for that attack.

### Shift

An attack option with the *shift* icon {{icon:ast-0057-shift}} lets the character move up to the number of nodes shown. A shift icon before the dice icons is used before the dice are rolled; one after the dice icons is used after the roll. A shift costs no stamina and is separate from the character's *walk* and *run*.

### Area-of-Effect

An attack with the *area-of-effect* icon {{icon:ast-0054-node-attack}} targets every enemy on a single node within range in place of one enemy. Make the attack roll once and compare it with the block or resist of each enemy on the node.

### Shaft

Bows, polearms and other unwieldy weapons are hard to use at close quarters. An attack with the *shaft* icon {{icon:ast-0056-shaft}} cannot target a model on the character's own node.

### Repeat

The *repeat* icon {{icon:ast-0061-repeat-behaviour-or-attack}} lets the character use the whole attack option the number of times shown in the circle. This is a rapid flurry of blows, as from an agile sword or a repeating crossbow. The stamina cost is paid once. Each use is rolled separately and may have a different target.

## 10.4 Two-Handed Attacks

A character with a *two-handed* weapon is decidedly on the offensive. An attack with a two-handed weapon {{icon:ast-0045-two-handed-weapon}} may reroll any single die after the roll. A one-handed weapon {{icon:ast-0043-one-handed-weapon}} *equipped* with nothing in the other weapon slot is wielded two-handed and gains the same reroll.

## 10.5 Stat Scaling

*Stat scaling* gives a weapon extra damage in the hands of a character whose stats far exceed what it asks for.

- A weapon is scaled while the character's stat is ten or more above the weapon's highest stat requirement.
- If two requirements are tied for highest, either stat qualifies.
- Mark a scaled weapon with a red damage cube. Remove the cube when the weapon is no longer scaled.
- Every attack option of a scaled weapon gains +1 to its attack value. There is no further bonus for a higher stat.

*Example.* A weapon asks for 16 STR and 12 DEX. A character with 26 STR marks it with a red damage cube and adds 1 to the attack value of each of its attacks. The character's DEX plays no part.
