# Verification A: chapters 01 to 11 and glossary A to M

Status: COMPLETE. Read in full: chapters 01 to 11, the glossary, and (for the rules they share with this half) chapters 12 to 16, 18, 20, 22 and 23, with the cited parts of chapters 17 and 19. The manuscript is quoted as it stands at commit 495a4d2, that is, after the three changes announced during the work: §8.5 Stagger (summon), §6.1 step 7 (the lone character's pre-departure spending withdrawn), and the second verifier's 25 corrections (§8.4, last paragraph but one). No manuscript file was edited.

Mechanical fixes are in `work/phase3/verify_a.json` (39 objects; each `old` occurs exactly once in its file; applied to a scratch copy, `tools/xref_check.py` reports 0 broken references and `tools/style_check.py` 0 violations). Four defects are judgement calls and are in this report only: VA-015, VA-024, VA-025, VA-026.

## The twelve changed rules named in the brief

| Rule | Result in chapters 01 to 11 and glossary A to M |
|---|---|
| Returning to the bonfire is resting (§11.1) | Agrees everywhere (§1, §7.5, §11.1, §11.2, §6.7, glossary Bonfire). |
| Hollow cubes are spare white cubes (§2.8, §7.2) | Agrees everywhere (§2.8, §3.4, §3.5, §6.1, §7.2, §7.5, §10.1, §11.2, glossary). One stale "only" about their removal: VA-021. |
| Shield in either slot; riposte with the other slot (§9.6, §3.2) | Agrees in rules and in both §9.6 examples. One hole at the edge: VA-025. |
| Enemy repeat icon repeats the whole row (§8.2, §9.1, §9.3); character's repeat "up to" (§10.3) | Agrees everywhere, example of §10.3 included. |
| Damage, then push, then condition (§9.3, §9.4, §8.5) | Agrees in §8.1, §8.4, §8.5, §9.3, §9.4, §9.6, §10.3 and the glossary. |
| One scry for each gravestone (§5.5, §7.5) | Agrees (§5.5, §7.5 step 5 and Scry, glossary Gravestone). |
| All-zero weapon never scaled (§10.5) | §3.3 restates the rule without it: VA-005 (and VA-042 for the glossary). |
| Shop stocked before tier two rewards (§6.6) | Agrees (§6.6 steps 13 and 14, §6.3, §6.2). |
| Titanite by name; parts from a sold weapon (§4.2, §11.4) | Agrees; one lower-case *titanite* (VA-013); the cards kept outside the decks are still swept into them by §6.2 (VA-011, VA-012) and have no stated price (VA-026). |
| Trap tokens off edges whose doorway is part of the route (§5.5) | Agrees; step 6 of Encounter Start lacks the "first time" limit of §5.5 (VA-019). |
| Lone character's pre-departure spending | Withdrawn by the coordinator; §6.1 step 7, §7.6, §11.1, §11.3, §11.4 and the glossary now agree. Nothing reported. |
| The route is a chain of any shape (§6.5, §6.6) | Five places still find the first encounter tile by its lying beside the bonfire tile: VA-006, VA-014, VA-016, VA-018, VA-027, VA-030. |

## Defects

### VA-001 · 10_manuscript_chapter_01_introduction.md · §1 · inconsistency
- Text: "The bonfire's *sparks* are few, and every rest spends one (see §7.4)."
- Problem: §7.4 and §11.2 state that the rest that follows the defeat of a boss costs no spark. Severity: low.
- Correction: "The bonfire's *sparks* are few, and every rest spends one, except the rest that follows the defeat of a boss (see §7.4)."

### VA-002 · 10_manuscript_chapter_02_game_components.md · §2.3 · inconsistency
- Text: "A boss fought with several models has a health dial for each of them (see §17.1)."
- Problem: §2.9 lists for a mega-boss "1x Mega-boss model (the Executioner's Chariot has two and The Four Kings four) ... 1x Health dial (The Four Kings has four)", and §17.9 gives the Chariot two models and one health dial. §17.1 limits the rule to a boss whose models stand on separate nodes. Severity: low.
- Correction: "A boss fought with several models that stand on separate nodes has a health dial for each of them (see §17.1); the two models of the Executioner's Chariot share one health dial (see §17.9)."

### VA-003 · 10_manuscript_chapter_02_game_components.md · §2.8, Tiles · inconsistency
- Text: "- 2x Boss tiles (Core), the mini-boss tile and the main-boss tile"
- Problem: §15.3 ("One boss tile is printed with the mini-boss *spawn node* and is the mini-boss tile. The other is printed with the main-boss spawn node." and "The two tiles are joined along one edge to form a single rectangular tile, the main-boss tile"), §6.6 step 6, §5.1 and the glossary entry Boss tile all make the main-boss tile the two boss tiles joined. The second tile alone is not the main-boss tile. Severity: medium.
- Correction: "- 2x Boss tiles (Core): the mini-boss tile, and a second boss tile that is joined to it to form the main-boss tile"

### VA-004 · 10_manuscript_chapter_03_characters.md · §3.1, Threat · cross-reference
- Text: "Characters act in descending order of threat, and the character with the highest threat takes the *aggro* token at the start of each encounter (see §7.5, Encounter Turn Order)."
- Problem: the placing of the aggro token at the start of an encounter, and the settling of ties, are stated in §7.5, Encounter Start, step 10. Encounter Turn Order states the turn order and the later movement of the token only. Severity: low.
- Correction: "Characters act in descending order of threat, and the character with the highest threat takes the *aggro* token at the start of each encounter (see §7.5, Encounter Start; §7.5, Encounter Turn Order)."

### VA-005 · 10_manuscript_chapter_03_characters.md · §3.3 · inconsistency
- Text: "A weapon whose highest stat requirement the character's stat exceeds by five or more is *scaled* (see §10.5)."
- Problem: by §10.5 a weapon whose four stat requirements are all zero has no relevant stat and is never scaled; read as written, §3.3 scales it for any character with a stat of five. Severity: low.
- Correction: "A weapon whose highest stat requirement the character's value in that stat exceeds by five or more is *scaled*; a weapon whose stat requirements are all zero is never scaled (see §10.5)."

### VA-006 · 10_manuscript_chapter_05_tiles_and_nodes.md · §5.1 · inconsistency
- Text: "Tiles are joined so that a doorway of each tile faces a doorway of the tile beside it (see §6.5)."
- Problem: the route is now a chain of any shape (§6.5, Encounter Tiles, steps 3 and 4). In a folded chain a tile lies beside tiles that are not next on the route, and "A doorway that faces neither of those tiles is not used". Severity: low.
- Correction: "Tiles are joined so that a doorway of each tile faces a doorway of the tile that follows it on the route; a tile that merely lies beside another is not joined to it (see §6.5)."

### VA-007 · 10_manuscript_chapter_05_tiles_and_nodes.md · §5.3 · example
- Text: "Then the Gargoyle moves onto a node that holds the Knight, the Herald, and the Assassin; the boss does not count towards the limit, so no model is pushed."
- Problem: the first half of the example is an encounter with a Hollow Soldier in which the Herald has just been pushed off the node. "Then" makes the Gargoyle part of the same scene, but the boss is the only enemy of a boss encounter (§15.2), and the Herald is no longer on the node. The outcome itself is right (§5.3; §16.2, Characters on a Node the Boss Enters). Severity: low.
- Correction: "In a later boss encounter the Gargoyle moves onto a node that holds the Knight, the Herald, and the Assassin; the boss does not count towards the limit, so no model is pushed."

### VA-008 · 10_manuscript_chapter_05_tiles_and_nodes.md · §5.5 (opening) · inconsistency
- Text: "There are five kinds: *gravestones*, *barrels*, *chests*, and pillars, which are placed on *terrain nodes* as the *encounter card* directs, and traps, which are dealt to *basic nodes* (see §7.5, Encounter Start)."
- Problem: by §5.5, Pillars and §17.3 pillar tokens are placed on the four pillar nodes of one game board at the start of a boss encounter, and no encounter card is dealt to a boss encounter (§15.2). Encounter Start (§7.5) places no pillar. Severity: low.
- Correction: "There are five kinds: *gravestones*, *barrels*, and *chests*, which are placed on *terrain nodes* as the *encounter card* directs (see §7.5, Encounter Start); pillars, which are placed on the pillar nodes of one game board (see §5.5, Pillars); and traps, which are dealt to *basic nodes* (see §5.5, Traps)."

### VA-009 · 10_manuscript_chapter_06_setup.md · §6.1 · inconsistency
- Text: "The number of characters in the party sets the scaling of enemy health and attack values (see §8.3) and the starting number of *sparks* (see §6.4, §7.4)."
- Problem: the table of §8.3 scales enemy movement as well (a movement value of 1 becomes 2 with two or more characters). Severity: low.
- Correction: "The number of characters in the party sets the scaling of enemy health, movement, and attack values (see §8.3) and the starting number of *sparks* (see §6.4, §7.4)."

### VA-010 · 10_manuscript_chapter_06_setup.md · §6.2 · cross-reference
- Text: "Every *treasure card* belongs to one of six types (see §2.5), and its type and its stat requirements (see §4.1) decide which deck, if any, it enters."
- Problem: §2.5 (as amended today), §4.1, §4.4 and the glossary count an ember card as a treasure card, and §7.7 and §11.4 count an invader's treasure card and a Titanite Scale card as treasure cards; none of them is one of the six types that §6.2 goes on to list. The cited §2.5 names five types and the ember card, not six types. Severity: low.
- Correction: "The *treasure cards* from which the decks are built are of the six types set out below, and a card's type and its stat requirements (see §4.1) decide which deck, if any, it enters; the number of cards of each type is given with the components (see §2.5). An *ember card*, an *invader*'s treasure card, and a Titanite Scale card are of none of the six types and enter neither deck (see §2.9; §4.4)."

### VA-011 · 10_manuscript_chapter_06_setup.md · §6.2, Treasure Card Types · inconsistency
- Text: "**Common treasure.** A treasure card that is not starting equipment, class-specific, transposed, legendary, or boss treasure."
- Problem: the catch-all makes an invader's treasure card and a Titanite Scale card common treasure, and "The tier one treasure deck holds every common treasure card ... whose stat requirements are all below 25". §11.4, Sales (as amended today) calls them cards "that came from no treasure deck"; §12.2, Invader Setup, step 1 takes the invader's treasure card with its model; §14 awards a Titanite Scale card "from the supply"; §2.5 counts both apart from the treasure table. Severity: medium (with VA-012).
- Correction: "**Common treasure.** A treasure card that is not starting equipment, class-specific, transposed, legendary, or boss treasure, and is not an *ember card*, an *invader*'s treasure card, or a Titanite Scale card."

### VA-012 · 10_manuscript_chapter_06_setup.md · §6.2, Building the Treasure Decks · inconsistency
- Text: "1. Set aside every boss treasure card, every legendary treasure card, every ember card, and every starting equipment card that is not equipped."
- Problem: step 3 sorts "the remaining treasure cards" into the two decks, so the 12 invader treasure cards and the three Titanite Scale cards (§2.9) are shuffled into the decks and dealt as ordinary rewards. §11.4, §12.2 and §14 require them to be outside the decks (see VA-011). Severity: medium.
- Correction: "1. Set aside every boss treasure card, every legendary treasure card, every ember card, every *invader*'s treasure card, every Titanite Scale card, and every starting equipment card that is not equipped."

### VA-013 · 10_manuscript_chapter_06_setup.md · §6.3, Stocking Categories · glossary
- Text: "- An upgrade is a card with the weapon-upgrade icon {{icon:ast-0044-weapon-upgrade}} or the armour-upgrade icon {{icon:ast-0046-armour-upgrade}}, including rings and *titanite*."
- Problem: the glossary headword and §4.1, §4.2 and §11.4 spell the term *Titanite*, and §4.2 now recognises the cards by that word in their names. Severity: low.
- Correction: "- An upgrade is a card with the weapon-upgrade icon {{icon:ast-0044-weapon-upgrade}} or the armour-upgrade icon {{icon:ast-0046-armour-upgrade}}, including rings and *Titanite*."

### VA-014 · 10_manuscript_chapter_06_setup.md · §6.5, Encounter Cards · ambiguity
- Text: "Encounter levels increase from the tile adjacent to the bonfire tile towards the boss tile."
- Problem: the route is a chain of any shape (§6.5, Encounter Tiles, step 3). In the book's own example, "two rows of three tiles, with the bonfire tile and the mini-boss tile in opposite corners", the only chain that fits runs down, across, up, across, down, so the bonfire tile lies beside two encounter tiles: the first of the route and the third. The phrase "the tile adjacent to the bonfire tile" then names no single tile. §15.1 and §18.2 already say "the first encounter tile". The same stale phrase is at VA-016, VA-018, VA-027 and VA-030. Severity: medium.
- Correction: "Encounter levels increase along the route, from the first encounter tile after the bonfire tile to the last encounter tile before the boss tile."

### VA-015 · 10_manuscript_chapter_06_setup.md · §6.5, Expansion Encounters · ambiguity (judgement call, not in the JSON)
- Text: "Each encounter deck is built only from the encounter cards of the set that supplies the next boss. Encounter cards of other sets are not used on that leg of the exploration."
- Problem: by §2.6 the Asylum Demon expansion supplies only four Level 4 encounter cards (the per-set list of Levels 1 to 3 leaves it out, and its figures sum to the table's 37), yet §2.3 lists the Asylum Demon as a mini-boss and §6.5, Encounter Tiles, step 6 sets it up as one. With the Asylum Demon chosen, steps 1 and 2 of Encounter Cards cannot be carried out unless mixed encounter decks happen to be in play. Severity: medium.
- Two readings: (a) the decks of that leg fall back on the core set, which every party owns and which §19.1, Section Four uses as its default; (b) mixed encounter decks apply of themselves on that leg. Reading (a) is preferred: it keeps the optional rule optional and gives every party the same decks.
- Correction (reading a), added after the quoted sentences: "If that set supplies no encounter cards of Levels 1 to 3, as when the Asylum Demon is the mini-boss, the encounter decks of that leg are built from the core set's encounter cards."

### VA-016 · 10_manuscript_chapter_06_setup.md · §6.6 · ambiguity
- Text: "19. Exploration resumes from the encounter tile adjacent to the bonfire tile (see §11.5)."
- Problem: as VA-014.
- Correction: "19. Exploration resumes from the first encounter tile of the route (see §11.5)."

### VA-017 · 10_manuscript_chapter_07_gameplay.md · §7.4 · inconsistency
- Text: "In the standard game sparks cannot be gained in any other way; campaign play varies these rules (see §18.3)."
- Problem: §18.4 states "The party gains one spark when a player leaves" and "A player joins or leaves a standard game in progress under the same rules"; §8.3 (changed today) already points to §18.4 for the standard game. Severity: medium.
- Correction: "In the standard game sparks are gained in no other way, except when a player leaves the game (see §18.4); campaign play varies these rules (see §18.3)."

### VA-018 · 10_manuscript_chapter_07_gameplay.md · §7.5 (opening) · ambiguity
- Text: "The characters begin at the encounter tile adjacent to the *bonfire* tile and advance one tile at a time towards the boss tile."
- Problem: as VA-014.
- Correction: "The characters begin at the first encounter tile of the route, the tile that follows the *bonfire* tile in the chain (see §6.5), and advance one tile at a time along the route towards the boss tile."

### VA-019 · 10_manuscript_chapter_07_gameplay.md · §7.5, Encounter Start · inconsistency
- Text: "6. If the encounter card shows the trap icon, deal *trap tokens* (see §5.5, Traps)."
- Problem: §5.5, Traps deals trap tokens "the first time the encounter is set up" and states "Trap tokens are not dealt to the same tile again when its encounter is reset". Step 6 is carried out at every arrival and has no such limit, where step 9 of the same list carries it for chests ("placed on the tile for the first time"). Severity: low.
- Correction: "6. If the encounter card shows the trap icon and the encounter is set up for the first time, deal *trap tokens* (see §5.5, Traps)."

### VA-020 · 10_manuscript_chapter_07_gameplay.md · §7.5, Encounter Start · inconsistency
- Text: "10. Place the *aggro token* on the character with the highest *threat* {{icon:ast-0026-threat-level}}."
- Problem: §3.1 prints a character's threat with the Taunt icon of the dashboard, {{icon:ast-0059-taunt}} ("The dashboard prints the character's threat as its Taunt Level"). The icon ast-0026 is the threat icon of enemy, boss and phantom data cards (§8.2, §9.1, §12.1, §15.4) and is not on a dashboard. Severity: low. If the fix is taken, the placement note "inline icon, §7.5" in `21_asset_manifest.csv` moves from AST-0026 to AST-0059.
- Correction: "10. Place the *aggro token* on the character with the highest *threat* {{icon:ast-0059-taunt}}."

### VA-021 · 10_manuscript_chapter_07_gameplay.md · §7.5, Encounter Recovery · inconsistency
- Text: "Recovery does not ready the *estus flask*, *luck*, or *heroic action* tokens, and does not remove the hollow cubes of a character who was already hollow; only resting at the bonfire does so (see §11.2)."
- Problem: §7.2 ("Hollow is removed only by resting at the bonfire (see §11.2) or by becoming *embered* (see §7.3)") and §7.3 step 3 remove hollow cubes by embering as well. The words "only resting at the bonfire does so" are right for the three tokens and wrong for the hollow cubes. Severity: medium.
- Correction: "Recovery does not ready the *estus flask*, *luck*, or *heroic action* tokens, which only resting at the bonfire readies (see §11.2). It does not remove the hollow cubes of a character who was already hollow, which are removed only by resting at the bonfire or by becoming *embered* (see §7.2)."

### VA-022 · 10_manuscript_chapter_08_combat_basics.md · §8.1 · example
- Text: "*Example.* An enemy attack with an *attack value* of 4 bears the push icon and targets the Knight and the Herald, who share a node within its range."
- Problem: by §8.1 "An attack has one target unless its icons give it more", and by §9.3 only a node attack targets every character on a node. The push icon adds no target, so the attack described cannot target both characters. Severity: low.
- Correction: "*Example.* An enemy attack with an *attack value* of 4 bears the node icon and the push icon and targets the Knight and the Herald, who share a node within its range."

### VA-023 · 10_manuscript_chapter_08_combat_basics.md · §8.4 (third example) · example
- Text: "The enemy then moves its second node, which holds no character, and no model is pushed."
- Problem: the example names no target. By §9.2, Push-Move the enemy "moves one node at a time towards or away from the target's current node", and the Knight has just been pushed "directly away from the node the enemy has left", that is, along the line of the enemy's advance. If the Knight is the target, or the path runs straight on, the second node entered is the Knight's and the Knight is attacked again ("A character pushed onto a node that the enemy enters afterwards in the same movement is attacked again on that node", §9.2, whose own example shows exactly this). The stated outcome follows only if another character is the target and the path turns, which the example does not say. Severity: medium.
- Correction: "The enemy's movement targets the Herald, and its path turns at that node, so the second node it enters is not the node to which the Knight was pushed. That node holds no character, and no model is attacked or pushed."

### VA-024 · 10_manuscript_chapter_08_combat_basics.md · §8.5, Frostbite · ambiguity (judgement call, not in the JSON)
- Text: "An enemy, boss, or phantom with a frostbite token reduces the value of each of its movement icons by one, after *enemy scaling* has been applied (see §8.3; §9.2)."
- Problem: §8.5, Stagger as changed today sorts a summon with the characters and an invader with the enemies, and §12.1 has a summon receive conditions "as a character does". The Frostbite paragraph (and the glossary entry Frostbite, "any other model") still puts every phantom on the enemy side. A summon has no stamina to recover and no movement icons; its behaviour cards carry *shift* icons (§12.1). Neither half of the Frostbite rule now says what the token does to a summon. Severity: low.
- Two readings: (a) enemy side: a frostbitten summon moves one node fewer for each shift icon; (b) character side: the token has no effect on a summon, which pays no stamina. Reading (a) is preferred: it keeps the present sentence true of every phantom and gives the token an effect.
- Correction (reading a): "An enemy, boss, or *invader* with a frostbite token reduces the value of each of its movement icons by one, after *enemy scaling* has been applied (see §8.3; §9.2). A *summon* with a frostbite token reduces by one the number of nodes of each *shift* icon on its behaviour cards (see §12.1)." The glossary entry Frostbite then reads: "any other model with a frostbite token reduces each of its movement values, or for a *summon* each of its *shift* values, by one."

### VA-025 · 10_manuscript_chapter_09_enemy_turn.md and 10_manuscript_chapter_10_character_turn.md · §9.6; §10.4 · ambiguity (judgement call, not in the JSON)
- Text: §9.6: "A character who wields a weapon *two-handed* has no shield equipped and cannot parry (see §10.4)." §10.4: "A character who wields a weapon two-handed has no shield equipped and therefore cannot *parry* (see §9.6)."
- Problem: a shield is a one-handed weapon (§4.1, Card Types), and by §3.2 and the second case of §10.4 a one-handed weapon equipped while the other weapon slot is empty is wielded two-handed. A character whose only equipped weapon card is a shield therefore wields a weapon two-handed and has a shield equipped. The two conditions of §9.6 permit the parry; the quoted sentences forbid it. Severity: low.
- Two readings: (a) the two listed conditions govern, the parry is permitted, and no riposte follows because the other weapon slot holds no weapon with an attack option (§9.6, Riposte); (b) the quoted sentences govern and a lone shield cannot parry. Reading (a) is preferred: it is the rule as ruled today ("a shield in either weapon slot").
- Correction (reading a): §9.6: "A character who wields a weapon other than a shield *two-handed* has no shield equipped and cannot parry (see §10.4)." §10.4: "A character who wields a weapon other than a shield two-handed has no shield equipped and therefore cannot *parry* (see §9.6)."

### VA-026 · 10_manuscript_chapter_11_returning_to_the_bonfire.md · §11.4, Sales and Prices · ambiguity (judgement call, not in the JSON)
- Text: "Andre pays one soul for a tier one or tier two treasure card and six souls for a boss treasure card, and the character takes the souls from the supply." and "- A sold boss treasure card is returned to the game box, and so is any other sold card that came from no treasure deck: an *invader*'s treasure card or a Titanite Scale card."
- Problem: the second sentence (added today) lets an invader's treasure card and a Titanite Scale card be sold, but the first sentence and the price table give a sell value only to tier one cards, tier two cards and boss treasure. Whether such a card is "a tier one or tier two treasure card" depends on the catch-all of §6.2 that VA-011 corrects; and if it is one, the first bullet ("placed face down at the bottom of the treasure deck of its tier") and the second bullet both claim it. Severity: medium.
- Two readings: (a) the card sells for one soul, as a card of the tier its stat requirements give, and goes to the game box (the reading of the core rulings memo, "it fetches one soul"); (b) the card has no sell value and cannot be sold, which the second bullet contradicts. Reading (a) is preferred.
- Correction (reading a): "Andre pays one soul for a tier one or tier two treasure card, one soul for an *invader*'s treasure card or a Titanite Scale card, and six souls for a boss treasure card, and the character takes the souls from the supply." First bullet: "- A sold tier one or tier two treasure card that came from a treasure deck or from the shop is placed face down at the bottom of the treasure deck of its tier (see §6.2)." New row of the price table, after the tier two row: "| *Invader*'s treasure card or Titanite Scale card | - | 1 |".

### VA-027 · 10_manuscript_chapter_11_returning_to_the_bonfire.md · §11.5 · ambiguity
- Text: "After the reset the characters leave the bonfire tile and enter the encounter tile adjacent to it, where that tile's encounter begins (see §7.5, Encounter Start)."
- Problem: as VA-014.
- Correction: "After the reset the characters leave the bonfire tile and enter the first encounter tile of the route, where that tile's encounter begins (see §7.5, Encounter Start)."

### VA-028 · 12_glossary.md · Attack option · glossary
- Text: "**Attack option.** One line of a weapon or spell card, showing a stamina cost, dice and modifiers. Using an attack option is the *Attack* major action."
- Problem: by §10.3 the Attack major action may use one attack option of each weapon slot, and by §9.6 a riposte uses an attack option and "is not the character's *Attack* major action". The entry cites no section. Severity: low.
- Correction: "**Attack option.** One line of a weapon or spell card, showing a stamina cost, the dice to roll, any fixed modifier, and any attack icons (see §4.1, Card Anatomy). A character uses one attack option for each attack of the *Attack* major action and for a *riposte* (see §10.3; §9.6)."

### VA-029 · 12_glossary.md · Common treasure · glossary
- Text: "**Common treasure.** A treasure card that is not starting, class-specific, transposed, legendary or boss treasure."
- Problem: as VA-011; the entry repeats the catch-all of §6.2.
- Correction: "**Common treasure.** A treasure card that is not starting equipment, class-specific, transposed, legendary, or boss treasure, and is not an *ember card*, an *invader*'s treasure card, or a Titanite Scale card."

### VA-030 · 12_glossary.md · Encounter level · glossary
- Text: "The levels of the encounters leading to a boss are printed on that boss's data card and increase from the tile adjacent to the bonfire tile towards the boss tile (see §6.5)."
- Problem: as VA-014.
- Correction: "The levels of the encounters leading to a boss are printed on that boss's data card and increase along the route from the first encounter tile to the last (see §6.5)."

### VA-031 · 12_glossary.md · Enemy scaling · glossary
- Text: "**Enemy scaling.** The adjustment of every enemy to the number of characters fixed at setup: more health with two or more characters, movement values of 1 resolved as 2 with two or more characters, and +1 attack value with four characters."
- Problem: §8.3 as changed today: the number "changes only when a player joins or leaves the game (see §18.4)", in the standard game as in a campaign. It is not fixed at setup. Severity: medium.
- Correction: "**Enemy scaling.** The adjustment of every enemy to the number of characters taking part in the game, which changes only when a player joins or leaves (see §18.4): more health with two or more characters, movement values of 1 resolved as 2 with two or more characters, and +1 attack value with four characters."

### VA-032 · 12_glossary.md · Main-boss · glossary
- Text: "Its defeat wins the standard game unless a mega-boss is in play (see §6.6; §15.3)."
- Problem: neither §6.6 nor §15.3 states the victory; §7.1 does (and §6.7). Severity: low.
- Correction: "Its defeat wins the standard game unless a mega-boss is in play (see §6.6; §7.1; §15.3)."

### VA-033 · 10_manuscript_chapter_05_tiles_and_nodes.md · §5.1, Spawn node · inconsistency
- Text: "The mini-boss tile has a mini-boss spawn node, the main-boss tile a main-boss spawn node, and a mega-boss game board a mega-boss spawn node; the *boss* is placed there at the start of its encounter (see §15.3)."
- Problem: §15.3 as corrected today places the boss on its spawn node "unless the boss's special rules name another node (see §15.2; §17)"; the Old Iron King, for one, is placed on an Iron King node (§17.10, Old Iron King). Severity: low.
- Correction: "The mini-boss tile has a mini-boss spawn node, the main-boss tile a main-boss spawn node, and a mega-boss game board a mega-boss spawn node; the *boss* is placed there at the start of its encounter, unless its special rules name another node (see §15.3; §17)."

### VA-034 · 10_manuscript_chapter_06_setup.md · §6.5, Optional Rules · inconsistency
- Text: "- Player versus player (PvP) encounters follow the defeat of each boss (see §20.1)."
- Problem: §20.1 as corrected today and §18.1, Player versus Player Encounters: in campaign play a PvP encounter follows only a boss whose defeat completes a section. §18.1, Campaign Setup sends campaign players to this list ("see §6.5, Optional Rules"). Severity: low.
- Correction: "- Player versus player (PvP) encounters follow the defeat of each boss or, in campaign play, of each boss whose defeat completes a *section* (see §20.1)."

### VA-035 · 10_manuscript_chapter_07_gameplay.md · §7.1 · inconsistency
- Text: "If the party chose player versus player (PvP) during setup, a PvP *encounter* is fought after each boss is defeated (see §20)."
- Problem: as VA-034.
- Correction: "If the party chose player versus player (PvP) during setup, a PvP *encounter* is fought after each boss is defeated or, in campaign play, after each boss whose defeat completes a *section* (see §20.1; §18.1, Player versus Player Encounters)."

### VA-036 · 12_glossary.md · Boss spawn node · glossary
- Text: "**Boss spawn node.** The spawn node of a boss's type: the mini-boss spawn node, the main-boss spawn node, or the mega-boss spawn node. The boss model is placed on it at the start of every boss encounter (see §15.3)."
- Problem: §15.3 now adds "unless the boss's special rules name another node (see §15.2; §17)", and by §17.3 the Asylum Demon, a mini-boss, is placed on the mega-boss spawn node of its expansion's game board, which is not the spawn node of its type. Severity: low.
- Correction: "**Boss spawn node.** The spawn node of a boss's type: the mini-boss spawn node, the main-boss spawn node, or the mega-boss spawn node. The boss model is placed on it at the start of every boss encounter, unless the boss's special rules name another node: the Asylum Demon, a mini-boss, is placed on the mega-boss spawn node of its expansion's game board (see §15.3; §17.3)."

### VA-037 · 12_glossary.md · Boss tile · glossary
- Text: "A mini-boss encounter is fought on the mini-boss tile alone; a main-boss encounter is fought on both boss tiles joined as one tile, the main-boss tile."
- Problem: §15.3: "A mini-boss encounter is fought on the mini-boss tile alone, unless the mini-boss's special rules name another tile (see §17.3)"; the Asylum Demon is fought on its expansion's game board (§17.3; §6.5 step 6; glossary Mini-boss). Severity: low.
- Correction: "A mini-boss encounter is fought on the mini-boss tile alone, unless the mini-boss's special rules name another tile, as for the Asylum Demon (see §17.3); a main-boss encounter is fought on both boss tiles joined as one tile, the main-boss tile."

### VA-038 · 12_glossary.md · Invasion · glossary
- Text: "no more than one is provoked before the mini-boss is defeated and no more than one after it (see §12.2)."
- Problem: the entry agrees with §12.2 for the standard game (both moments at which an invasion is provoked, and the face-down encounter cards with no black cube, are as §12.2 states them). It omits the campaign limit of §12.2 and §18.1, Section Setup: no more than one invasion in each section. Incomplete, not contradictory. Severity: low.
- Correction: "no more than one is provoked before the mini-boss is defeated and no more than one after it; in campaign play, no more than one is provoked in each *section* (see §12.2; §18.1)."

### VA-039 · 12_glossary.md · Mimic · glossary
- Text: "When the party opens a chest whose *ambush card* shows Mimic, the Hungry Mimic (before the mini-boss is defeated) or the Voracious Mimic (afterwards) is fought in a *mimic encounter*."
- Problem: the entry agrees with §13 for the standard game, and the entry Mimic encounter already states the removal of stamina cubes before the mimic's first turn as §13.2 does. The entry Mimic omits the campaign rule of §13.2: the Hungry Mimic while the current tier is tier one, the Voracious Mimic once it is tier two. Incomplete, not contradictory. Severity: low.
- Correction: "When the party opens a chest whose *ambush card* shows Mimic, the Hungry Mimic (before the mini-boss is defeated; in campaign play, while the current tier is tier one) or the Voracious Mimic (afterwards) is fought in a *mimic encounter*."

### Companions in glossary N to Z (outside this half; the same defect restated there)

### VA-040 · 12_glossary.md · Spark · glossary
- Text: "The party begins with six minus the number of characters, gains one for each boss defeated, and spends one each time the characters rest at the *bonfire* (see §7.4)."
- Problem: as VA-001; §7.4 and §11.2 make the rest that follows a boss's defeat free.
- Correction: "The party begins with six minus the number of characters, gains one for each boss defeated, and spends one each time the characters rest at the *bonfire*, except at the rest that follows the defeat of a boss (see §7.4)."

### VA-041 · 12_glossary.md · Threat · glossary
- Text: "The character with the highest threat takes the aggro token at the start of each encounter; the players settle ties (see §3.1; §7.5, Encounter Turn Order)."
- Problem: as VA-004; both statements are in §7.5, Encounter Start, step 10.
- Correction: "The character with the highest threat takes the aggro token at the start of each encounter; the players settle ties (see §3.1; §7.5, Encounter Start; §7.5, Encounter Turn Order)."

### VA-042 · 12_glossary.md · Relevant stat · glossary
- Text: "A weapon is *scaled* by comparing the character's relevant stat with that requirement (see §10.5)."
- Problem: as VA-005; by §10.5 a weapon whose four stat requirements are all zero has no relevant stat, where the entry's tie rule would let the character choose one of four tied stats.
- Correction: "A weapon is *scaled* by comparing the character's relevant stat with that requirement; a weapon whose stat requirements are all zero has no relevant stat (see §10.5)."

### VA-043 · 12_glossary.md · PvP encounter · glossary
- Text: "**PvP encounter.** An optional contest fought between the characters alone, without enemies, on the tile on which a boss has been defeated, after each boss's defeat and before the rest that follows it."
- Problem: as VA-034; §20.1 and §18.1 limit it in campaign play.
- Correction: "**PvP encounter.** An optional contest fought between the characters alone, without enemies, on the tile on which a boss has been defeated, after each boss's defeat (in campaign play, only a defeat that completes a *section*) and before the rest that follows it."

## Leads from the second verifier

- Glossary Boss spawn node: wrong as it stood; VA-036 (and §5.1, VA-033).
- Glossary Boss tile: wrong as it stood; VA-037.
- Glossary Mimic: right for the standard game, campaign clause missing; VA-039. Glossary Mimic encounter agrees with §13.2 (stamina cubes removed before the mimic's first turn; recovery and rewards deferred).
- Glossary Invasion: right for the standard game, campaign limit missing; VA-038. Glossary Invader token and §2.9 agree with §12.2 (one token on each face-down encounter card that carries no black cube).
- §7.1 and §6.5 "each boss": VA-034, VA-035 (and the glossary entry PvP encounter, VA-043). §6.6 and §6.7 need no change: each is the setup that follows a boss whose defeat, in campaign play, completes a section.
- §8.4 as changed (a boss model pushed by another boss model that "moves onto its node or is placed on it"): agrees with §17.1 and §17.10, The Four Kings, and with the list of reasons in §8.4, whose last bullet covers a push made by a rule of a boss. §5.3 states the first case only and does not say "only"; no defect.

## Counts

Defects: 43. By kind: example 3; table 0; inconsistency 16; cross-reference 2; glossary 14; ambiguity 8. In the JSON: 39. Judgement calls kept out of the JSON: 4 (VA-015, VA-024, VA-025, VA-026).

## Examples

53 worked examples checked (chapter 03: 4; 04: 4; 05: 3; 06: 2; 07: 2; 08: 10; 09: 11; 10: 14; 11: 3). 50 are right in arithmetic, sequence and outcome under the rules as now written. 3 are defective: §5.3 (VA-007), §8.1 (VA-022), §8.4 third example (VA-023).

Figures the examples take from elsewhere were checked at the source: dice faces (§2.7) for every roll quoted; Rapier 14 STR and 21 DEX, Morning Star 16 STR, Halberd 31 STR and 18 DEX, and their tiers (Appendix A); the Titanite Shard and Titanite Chunk (Appendix B, Titanite Replacement); Hollow Soldier base health 1, block 1, resist 1, attack value 4 (the same in §8.2, §8.3, §8.5, §9.6, §10.3 and §18.7).

## Tables

Checked, and all agree with their text and with every other statement of the same figures:

- §2.5 treasure cards: rows sum to 519; class-specific 40 and 120 agree with ten cards for each of 4 core and 12 expansion character sets (§2.1).
- §2.6 encounter cards: 36 + 111 + 40 = 187; the per-set figures sum to 37 for each of Levels 1 to 3; Level 4 is four for each of the ten mega-bosses of §2.3; the Executioner's Chariot's six cards agree with §2.9 and §17.9.
- §2.7 dice faces: against the text and every example roll.
- §2.8 and §2.9 component lists: condition tokens 5 x 4 + 4 + 4 = 28; summons 5 + 5 and 40 behaviour cards (four each, §12.1); invaders 6 + 6 data cards and 11 models (the two Kirks share one); invader tokens against §12.2; mimic, Kalameet, Chariot, Four Kings, Guardian Dragon, Old Iron King and Asylum Demon components against §13 and §17.3 to §17.10; enemies of §2.2 against Appendix B.
- §7.6 soul rewards: reduced reward is half rounded down in every row; against the examples of §7.6, §11.2 and §13.3 and against §12.2, §16.5 and §18.5.
- §8.3 enemy scaling: against the examples of §8.2, §8.3, §8.4, §8.5, §9.2 and §18.7, the glossary and the F.A.Q.
- §11.3 stat tier costs: against the examples of §3.3, §11.2 and §11.3, the glossary entry Firekeeper, and §18.6 (campaign costs are double).
- §11.4 prices: against the text of §11.4, the glossary entries Shop and Boss treasure, and §18.6, Shop Price Table.

## Observations that are not defects

1. §6.1 step 7 cites §7.6 for the six souls of a lone character; §7.6 says nothing of them (the glossary entry Souls does). As the book now stands the six souls can first be spent at a rest, which costs one of the five sparks. That is consistent everywhere.
2. §2.5 and §4.1 define a treasure card as a card "from a treasure deck or from Blacksmith Andre's shop" and then list starting equipment and boss treasure, which enter neither (§6.2). The list governs in practice. If VA-010 to VA-012 are taken, the definition in §2.5, §4.1 and the glossary entry Treasure card could name the invader's treasure card and the Titanite Scale card as well.
3. §2 gives no count of ember cards; §6.2 and §6.3 need one for each character.
4. §2.6 says the encounter level is shown by the icon for Level 1, 2 or 3; the table beneath it has a Level 4 row.
5. §7.6 gives a reduced reward of 3 for a Level 4 encounter, but a cleared Level 4 encounter is never fought again (§6.7; §18.1), so the figure is never paid.
6. §2.8 lists 4 + 5 + 8 = 17 terrain tokens and 18 terrain models that "stand in place of the corresponding tokens". The count could not be checked against the components.
7. §10.3, Area-of-Effect example: three damage kills a Hollow Soldier (base health 1) unless four characters are in play; the example places a wound token of value 3 on each and does not say whether they are killed.
8. §9.6 first example says "four *wound tokens* are placed"; the rule (§8.2) is wound tokens with a total value of 4. §5.5 trap example says the Knight "rolls a total of 1"; §9.5 counts dodge icons.
9. §6.6 step 2 returns the four encounter cards to the game box and step 11 builds the decks from the set of the main-boss; when one set supplies both bosses the text does not say whether those four cards rejoin the decks.
10. §11.2: "The party may rest whenever the characters are on the bonfire tile". Since returning is resting (§11.1), the characters stand on the bonfire tile without having just rested only at the start of the game.
11. The glossary entry Data card lists range and dodge difficulty for every kind of data card; a boss's are on its behaviour cards (§15.4; §15.5).
12. §7.5, Encounter Start, step 5 places terrain tokens at every arrival; on a reset tile they are already in place (§5.5). Harmless.
13. Italic terms: every italic term in chapters 01 to 11 and in the glossary has a glossary headword; headwords are in alphabetical order; no term was found in use with two meanings (*scaled* is used only of weapons, with Scaled health and Enemy scaling as separate headwords).
