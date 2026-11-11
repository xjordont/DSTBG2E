# 10. Character Turn

When the enemies have struck, the characters answer. A character's turn is a careful spending of breath and steel: a step taken, a blow struck, a moment's rest stolen. This chapter sets out the order of a character's turn, how characters move, how their attacks are resolved, and what two hands and a strong arm add to a blow.

## 10.1 Turn Order

In each *round* of an *encounter* the enemies take their *turns* first, and the characters then take theirs one at a time in descending order of *threat* (see §7.5, Encounter Turn Order). A dead character takes no turn. An *invader* takes a turn after each character's turn (see §12.2). In a *boss* encounter the boss and the characters alternate turns (see §16.1), and a *summon* acts after each character's turn (see §12.1).

Character turns in a player versus player (PvP) encounter follow this chapter with the changes stated for that encounter (see §20.3).

A character's turn is resolved as follows.

1. Recover one stamina: remove one *stamina cube* from the character's *endurance bar* (see §3.4). If the character holds a *frostbite* token, skip this step (see §8.5, Frostbite).
2. Take *minor actions* and up to one *major action*, in any order.
3. Resolve every *condition* that takes effect at the end of the character's turn (see §8.5).
4. End the turn.

**Minor action.** An action that a character may take before the major action, after it, or both. The four minor actions are *Walk*, *Run*, *Equip*, and *Heroic Action*.

- Walk: once per turn, the character *moves* one *node* without spending stamina (see §10.2).
- Run: any number of times per turn, the character spends one stamina and moves one node (see §10.2).
- Equip: once per turn, the character exchanges any number of cards among the *back-up slot*, the left and right *weapon slots*, and the *armour slot* (see §3.2).
- Heroic Action: once per turn, the character flips the heroic action token to its used side and resolves the heroic action printed on the dashboard (see §3.5, Heroic Action). Heroic Action may be taken only while the token shows its ready side.

**Major action.** The one principal action of a character's turn. The four major actions are *Attack*, *Rest*, *Drink Estus*, and *Ember*. A character may take one major action per turn.

- Attack: the character makes up to one attack with each *weapon* or *spell* *equipped* in a weapon slot (see §10.3).
- Rest: the character removes every stamina cube from their endurance bar. A character cannot Rest in a turn in which they have run, and a character who has rested cannot run for the remainder of that turn. A character who holds a frostbite token cannot Rest (see §8.5, Frostbite).
- Drink Estus: the character flips the *estus flask* token to its used side and removes every *damage cube* from their endurance bar (see §3.5, Estus Flask). Drink Estus may be taken only while the token shows its ready side.
- Ember: the character discards an *ember card* from their back-up slot and becomes *embered* (see §4.4, §7.3). An ember card in the *inventory* cannot be used during an encounter.

Rest removes stamina cubes only. Damage cubes, *hollow cubes*, and condition tokens stay where they are.

A character may take any, all, or none of these actions in a turn. Each action is resolved in full before another is begun: a character may walk, attack, and then run, but cannot take a minor action in the middle of an attack. A character cannot take Walk, Equip, or Heroic Action a second time in a turn, and cannot take a second major action.

The Equip minor action is the only way to change equipped cards during an encounter. Each card must go to a slot that accepts it, and the character must meet its *stat requirements* (see §3.2, §4.1). The inventory cannot be accessed during an encounter (see §3.2).

Stamina is spent by placing stamina cubes on the endurance bar (see §3.4). A character cannot choose to spend stamina that the bar has no empty space to hold: the character cannot run, and cannot choose an *attack option*, at a cost greater than the number of empty spaces. If a rule obliges a character to place a stamina cube and no empty space remains, the cube is not placed and the character is *staggered* {{icon:ast-0066-stagger}} instead (see §8.5, Stagger).

*Example.* The Knight begins the turn with four stamina cubes on the endurance bar and removes one. The Knight walks one node, takes the Attack major action with an attack option that costs two stamina, and then runs one node, placing one more stamina cube. The Knight ends the turn with six stamina cubes.

*Example.* The Herald begins the turn with seven stamina cubes and two damage cubes on the endurance bar. The Herald removes one stamina cube, walks one node, and takes the Rest major action, removing the remaining six stamina cubes. The two damage cubes stay, and the Herald does not run this turn.

*Example.* After recovering one stamina, the Assassin has five stamina cubes and four damage cubes, so one space of the endurance bar is empty. The Assassin's dagger has one attack option that costs one stamina and another that costs three. The Assassin chooses the first and places one stamina cube. The second is not available, because the bar has no room for three more cubes.

## 10.2 Character Movement

During an *encounter* a character changes *node* in five ways: by either of two *minor actions*, *Walk* and *Run*; by a *shift* icon {{icon:ast-0057-shift}} on an *attack option* (see §10.3, Shift); by the movement that follows a successful *dodge* (see §9.5); and by a *push* (see §8.4). Walk, Run, and shift are *moves*. The movement that follows a dodge and the movement of a push are not moves (see §5.2).

**Walk.** A minor action. The character moves to one *adjacent node* without spending stamina. A character may walk once per *turn*.

**Run.** A minor action. The character spends one stamina and moves to one adjacent node. A character may run any number of times in a turn, spending one stamina for each node. A character who has run cannot *Rest* in that turn (see §10.1).

A character may walk and run before the *major action*, after it, or both (see §10.1). A character may run without having walked.

Every move is made into a *valid node* (see §5.2). The *terrain* rules decide which nodes a character may enter: a character cannot move into a node that holds a *gravestone*, a *chest*, an intact *barrel*, or a *pillar token* (see §5.5). A character who moves into a node at its *node model limit* forces a model there to be pushed (see §5.3). A character who enters a node that holds a face-down *trap token* triggers it (see §5.5, Traps).

During an encounter a character cannot leave the tile on which the encounter is fought and cannot pass through a *doorway* (see §5.2).

*Example.* The Warrior stands three nodes from a Hollow Soldier. The Warrior walks one node without spending stamina, runs two nodes and places two *stamina cubes*, and attacks the Hollow Soldier on its node. After the attack the Warrior runs one node away and places a third stamina cube.

## 10.3 Character Attacks

A character attacks by taking the *Attack* major action (see §10.1). During that action the character may make up to one attack with each *weapon* or *spell* *equipped* in a *weapon slot*: one with the card in the left weapon slot and one with the card in the right weapon slot, in either order. Each attack uses one *attack option* of that card (see §4.1, Card Anatomy). A weapon that bears the *two-handed* icon {{icon:ast-0045-two-handed-weapon}} is one card in one weapon slot and makes one attack.

Spells are limited further (see §4.3). A character may use at most one spell attack option per *turn*. A spell stored in a *catalyst* is used as that catalyst's one attack. Attaching an *upgrade spell* is done as the Attack major action and uses the attack of the weapon slot that holds it (see §4.2, Upgrade Spells).

A character's attacks *target* hostile models: an enemy, a *boss*, an *invader*, a *mimic*, or a *crystal lizard*. In this section the word enemy covers all of these. Characters target other characters only in a PvP *encounter* (see §20.4).

Each attack is resolved as follows.

1. Choose one attack option of a weapon or spell equipped in a weapon slot.
2. Pay the stamina cost of the attack option by placing *stamina cubes* on the *endurance bar* (see §3.4).
3. If the attack option shows a *shift* icon {{icon:ast-0057-shift}} before its dice, resolve the shift (see §10.3, Shift).
4. Choose the target: one enemy within *range* of the attack (see §10.3, Range).
5. Roll the dice shown on the attack option (see §2.7).
6. The character may reroll one die if the weapon is wielded two-handed (see §10.4).
7. The character may flip the *luck* token to reroll any or all of the dice (see §3.5, Luck).
8. Work out the *attack value*: add together the values rolled, apply any fixed modifier printed on the attack option, add one if the weapon is *scaled* (see §10.5), and subtract one if the character is *staggered* {{icon:ast-0066-stagger}} (see §8.5, Stagger).
9. Subtract the target's *block* from the attack value if the attack deals *physical damage*, or the target's *resist* if the attack deals *magical damage*. The result is the damage the target suffers.
10. Place *wound tokens* with a total value equal to the damage on the target (see §8.2).
11. Apply to the target any *push* icon {{icon:ast-0058-push-affected-enemies}} and any *condition* icon shown on the attack option (see §8.4, §8.5).
12. If the attack option shows a shift icon after its dice, resolve the shift (see §10.3, Shift).

The character may take the rerolls of steps 6 and 7 in either order, and may take both on the same roll. A fixed modifier, +1 or −1 for example, is applied once to the total of the dice after every reroll; it is not applied to each die (see §4.1, Card Anatomy). An attack value below zero counts as zero.

An attack deals physical damage unless its attack option bears the magical damage icon {{icon:ast-0042-deal-magical-damage}}, in which case it deals magical damage. An enemy's block and resist are the fixed values printed on its *data card* (see §8.2). If the target's block or resist equals or exceeds the attack value, the target suffers no damage.

An enemy that is the target of an attack within range is *hit*, whether or not it suffers damage (see §8.1). An enemy whose wound tokens equal or exceed its scaled health is killed and removed from the tile (see §8.2, §8.3). Damage to a boss, an invader, or a mimic is recorded on its *health dial* in place of wound tokens (see §15.4).

An attack against a boss is resolved by the same steps. The *boss arc* from which the character attacks decides whether a black die {{icon:ast-0051-black-dice}} is added to the roll for a *weak arc* (see §15.6). In a PvP encounter the defending character rolls a defence in place of a fixed block or resist (see §20.4).

An attack that a rule grants outside the Attack major action, a *riposte* for example (see §9.6), is resolved by the same steps. It does not count towards the limit of one attack with each weapon slot.

Besides the magical damage icon, an attack option may show a push icon (see §8.4), a condition icon (see §8.5), and the icons set out in the remainder of this section: range, shift, area-of-effect, shaft, and repeat.

*Example.* The Warrior wields a great axe that bears the two-handed icon. The axe's highest *stat requirement* is 14 STR and the Warrior's strength is 20, so the axe is scaled. The Warrior chooses an attack option that costs two stamina and shows two blue dice and one black die with a +1 modifier, and places two stamina cubes. The Warrior targets a Silver Knight Swordsman on an *adjacent node*, within the axe's range of 1. The dice show 2, 1, and 0. The Warrior takes the two-handed reroll on the 0, which now shows 2, for a total of 5. The +1 modifier makes 6 and the scaling bonus makes 7, which is the attack value. The attack deals physical damage and the Silver Knight Swordsman's block is 2, so it suffers five damage and the Warrior places wound tokens with a total value of 5 on it.

### Range

Every weapon card and spell card prints a base range beside the range icon {{icon:ast-0060-attack-range}} (see §4.1, Card Anatomy). An attack option that prints a range of its own uses that range in place of the card's base range. The attack option's range applies to that attack option alone; the card's other attack options keep the base range.

Range is counted in *nodes* (see §5.4). The range of an attack is a maximum: a target at any shorter distance, including a target on the attacker's own node, is within range unless an icon on the attack option forbids it (see §10.3, Shaft). Range is checked when the target is chosen, after any shift resolved before the dice. A character cannot begin an attack unless a permitted target is within its range or a shift printed before its dice is able to bring one within range. If no permitted target is within range when the target is to be chosen, the attack ends without a roll, and the stamina paid is not returned.

*Example.* The Herald's spear prints a base range of 1, and one of its attack options prints a range of 2. With that attack option the Herald targets a Hollow Soldier two nodes away. With any other attack option of the spear the Herald targets an enemy on the Herald's own node or on an adjacent node.

### Shift

An attack option that bears the shift icon allows the character to *move* as part of the attack. The character may move up to the number of nodes shown with the icon, and may move fewer nodes or none. If the icon is printed before the attack option's dice, the shift is resolved before the target is chosen and the dice are rolled. If the icon is printed after the dice, the shift is resolved after the damage and every other effect of the attack.

A shift costs no stamina. A shift is a move (see §5.2): every node entered must be a *valid node*, and the rules for *terrain*, the *node model limit*, and *trap tokens* apply as they do to *Walk* and *Run* (see §10.2). A shift is separate from the Walk and Run minor actions and does not use them up.

*Example.* The Assassin stands two nodes from a Skeleton Soldier. The Assassin's attack option has a range of 1 and shows a shift icon with the number 1 before its dice. The Assassin pays the stamina cost, moves one node, chooses the Skeleton Soldier on the adjacent node as the target, and rolls the dice. The Assassin has not walked this turn and walks one node away after the attack.

### Area-of-Effect

An attack option that bears the *area-of-effect* icon {{icon:ast-0054-node-attack}} targets one node within range instead of one enemy. Every enemy on that node is a target of the attack and is hit by it. The dice are rolled once and one attack value is worked out. That attack value is compared separately with the block or resist of each enemy on the node, and each enemy suffers the damage that results.

A push icon or a condition icon on the attack option applies to every enemy on the node (see §8.4, §8.5). The attack may target the attacker's own node unless the attack option also bears the *shaft* icon {{icon:ast-0056-shaft}} (see §10.3, Shaft). Outside a PvP encounter, characters on the targeted node are not affected (see §20.4).

*Example.* The Herald uses a miracle whose attack option bears the area-of-effect icon and the magical damage icon and prints a range of 2. The Herald targets a node two nodes away that holds two Hollow Soldiers and a Silver Knight Swordsman, rolls once, and works out an attack value of 4. Each Hollow Soldier has a resist of 1 and suffers three damage, so the Herald places a wound token of value 3 on each. The Silver Knight Swordsman has a resist of 4 and suffers no damage, but it is hit.

### Shaft

An attack option that bears the shaft icon cannot target a model on the attacker's own node. An area-of-effect attack option that bears the shaft icon cannot target the attacker's own node. Every other node within range may be targeted.

*Example.* The Knight's bow prints a range of 3, and each of its attack options bears the shaft icon. One Hollow Soldier shares the Knight's node and another stands two nodes away. The Knight targets the second Hollow Soldier, because the first is not a permitted target.

### Repeat

An attack option that bears the *repeat* icon {{icon:ast-0061-repeat-behaviour-or-attack}} may be resolved in full up to the number of times shown in the icon. The character pays the stamina cost once, before the first resolution, resolves steps 3 to 12 of the attack for each resolution, and may stop after any resolution.

Each resolution is a separate attack roll with its own target: the character may target the same enemy again or a different enemy within range. The two-handed reroll applies to each roll (see §10.4). The luck token rerolls the dice of one roll only (see §3.5, Luck). All the resolutions together are that weapon's one attack for the turn.

*Example.* The Assassin's dagger has an attack option that costs one stamina and bears the repeat icon showing 2. The Assassin places one stamina cube and resolves the attack option twice. The first roll kills a Hollow Soldier on the Assassin's node. The Assassin targets a second Hollow Soldier on the same node with the second roll and places two wound tokens of value 1 on it.

## 10.4 Two-Handed Attacks

A *weapon* is wielded *two-handed* in either of two cases.

- The weapon card bears the two-handed weapon icon {{icon:ast-0045-two-handed-weapon}}. Such a weapon requires the other *weapon slot* to be empty (see §3.2).
- The weapon card bears the one-handed weapon icon {{icon:ast-0043-one-handed-weapon}} and is *equipped* while the other weapon slot holds no card.

Any card in the other weapon slot is equipment in the other hand. A one-handed weapon equipped beside a *shield*, a *catalyst*, a *spell*, or a second weapon is not two-handed (see §4.1, Card Types). Whether a weapon is wielded two-handed is judged when each attack is made.

When a character attacks with a weapon wielded two-handed, the character may reroll one die of the attack roll after rolling (see §10.3). The new result stands. The reroll is available on every attack roll made with that weapon, including each resolution of an *attack option* that bears the *repeat* icon {{icon:ast-0061-repeat-behaviour-or-attack}} (see §10.3, Repeat).

A spell is never two-handed (see §4.3). A spell card equipped while the other weapon slot is empty gains no reroll, and the attack options of a spell stored in a catalyst gain none. A catalyst is a weapon: an attack option printed on the catalyst card itself gains the reroll while the catalyst is wielded two-handed.

A character who wields a weapon other than a shield two-handed has no shield equipped and therefore cannot *parry* (see §9.6).

*Example.* The Knight has a one-handed sword in the right weapon slot and no card in the left weapon slot, so the sword is wielded two-handed. The Knight attacks a Hollow Soldier and rolls two black dice, which show 2 and 0. The Knight rerolls the 0, which now shows 1, and the *attack value* is 3. On the next *turn* the Knight takes the *Equip* minor action and equips a shield in the left weapon slot. The sword is no longer two-handed, and its attacks gain no reroll.

## 10.5 Stat Scaling

**Relevant stat.** The stat whose *stat requirement* is the highest of the four printed on a *weapon* card (see §4.1, Stat Requirements). If two or more requirements are tied for the highest, the character chooses one of the tied stats as the relevant stat.

A weapon is *scaled* while it is *equipped* by a character whose value in the relevant stat exceeds that highest stat requirement by five or more (see §3.3). When a weapon becomes scaled, the character must mark the weapon card with a red cube. The cube is removed when the weapon is no longer equipped.

Every *attack option* of a scaled weapon adds one to its *attack value* (see §10.3). The bonus is +1 and no more, however far the stat exceeds the requirement. Only the relevant stat is compared; the weapon's other stat requirements play no part in scaling.

A weapon whose four stat requirements are all zero has no relevant stat and is never scaled. *Spells* are never scaled (see §4.3).

*Example.* The Warrior's great axe prints requirements of 14 STR, 8 DEX, 0 INT, and 0 FTH, so strength is its relevant stat. The Warrior's strength is 20, which exceeds 14 by six. The axe is scaled: the Warrior marks it with a red cube, and each of its attack options adds one to its attack value.

*Example.* The Assassin's Rapier requires 14 STR and 21 DEX (see Appendix A), so dexterity is its relevant stat. The Assassin's dexterity is 24, which exceeds 21 by three, and the Rapier is not scaled. At the *bonfire* the Assassin raises dexterity to 29. The Rapier is now scaled, and the Assassin marks it with a red cube.

*Example.* The Knight's sword prints requirements of 18 STR and 18 DEX, tied for the highest. The Knight has 24 STR and 20 DEX and chooses strength as the relevant stat. The Knight's strength exceeds 18 by six, so the sword is scaled.
