# E — Content Completion Backlog

Project: Dark Souls: The Board Game — Second Edition (homebrew) editorial pipeline. Audit Agent E (Content Completion).
Manuscript: `/home/user/DSTBG2E/work/docx/manuscript.md` (body from line 361; line numbers below refer to that file).
Official references consulted (text extracts in `work/text/`): 2017 core rulebook, 2022 Tomb of Giants rulebook, official FAQ (11 April 2017), Characters, Phantoms, Darkroot, Iron Keep, Explorers, Black Dragon Kalameet and Executioner's Chariot booklets. Community homebrews (Hollowed Edition v1.3, Extended Rules v45) were read for context only; no rule was adopted from them.

Conventions in this file:
- Every "Proposed completion" is full text in the manuscript's voice (lawbook, British English, no second person outside marked examples), ready to be lifted verbatim after approval.
- Chapter cross-references are given by chapter/section name; the editor converts them to section numbers at layout.
- `[PROPOSED]` marks a rule the manuscript never states and that the draft supplies by inference from its own mechanics. `[PROPOSED-SYSTEMIC]` marks a new subsystem. `BLOCKED — source booklet not supplied` marks an entry that cannot be drafted without a booklet that was not in the input set.
- Status of every entry: awaiting-approval.

Index: CMP-0001 Estus Flask · CMP-0002 Glossary · CMP-0003 F.A.Q. · CMP-0004 Community Update Pack · CMP-0005 Boss Special Rules · CMP-0006 Lost state · CMP-0007 Truncated sentences · CMP-0008 Campaign Play Setup and campaign list · CMP-0009 Player vs Player · CMP-0010 Reduced soul reward · CMP-0011 First player token · CMP-0012 Undefined components · CMP-0013 Foreword / Introduction / colophon · CMP-0014 Mimics and chests reconciliation · CMP-0015 Crystal Lizard reward name · CMP-0016 Spells duplicate heading · CMP-0017 Wind Up scope · CMP-0018 Phantom summoning procedure · CMP-0019 Encounter reset and skip reconciliation · CMP-0020 Forced rest with no sparks · CMP-0021 Bathed in Flame campaign (Kalameet) · CMP-0022 Undead Colosseum special rules · CMP-0023 Level 4 encounter rules.

---

### [CMP-0001] Characters › Character Tokens › Estus Flask — Proposed Completion
- Current state: The TOC (line 65) lists an "Estus Flask" sub-heading under Character Tokens; no such sub-section exists in the body. The rule survives only in the DOCX page footer ("The character may flip their estus flask token to the used side as a major action to remove all damage cubes from their endurance bar. Stamina cubes are not removed."). The Character Tokens paragraph (line 793) says "There are three different types of character tokens: heroic actions, luck, and estus flask", then "Each character has one of each of the four following tokens", then lists Heroic Action, Luck and Ember; it also says ember tokens "should be placed in the condition token supply", while Character Setup step 5 (line 997) says "Place an ember token beside the character's board". The Character Turn (line 1830) calls the action "Drink Estus: Restore all of the character's health".
- Proposed completion:

  Replacement for the Character Tokens paragraph (line 793):

  > ## Character Tokens
  >
  > There are four types of character token: *heroic action*, *luck*, *estus flask* and *ember*. Each token has a ready side and a used side. The ready side is printed in brighter colours than the used side. A token's effect is available only while its ready side is face up. When a character uses a token's effect, the token must be flipped to its used side.
  >
  > Each character has one token of each type. The *heroic action*, *luck* and *estus flask* tokens begin the game ready, in their slots on the character dashboard. The *ember* token begins the game beside the dashboard and is placed in its slot only when the character becomes *embered* (see Embering).

  New sub-section, inserted after *Luck* and before *Ember* (after line 801):

  > ### *Estus Flask*
  >
  > A character may flip their *estus flask* token to the used side as a major action (*Drink Estus*) to remove all damage cubes from their endurance bar. Stamina cubes are not removed. *Hollow* markers are not removed. Condition tokens are not removed.
  >
  > The *estus flask* token is not restored when an encounter is *cleared*. It is flipped to the ready side only when the characters rest at the *bonfire*.

  Consequential edit to Character Turn › Major Action (line 1830): "*Drink Estus*: Remove all damage cubes from the endurance bar; flip *estus flask* face-down."
- Design rationale: The footer text is the only surviving source and already matches the manuscript's terminology (damage cubes, endurance bar, major action). Making the Ember token the fourth type resolves the "three types / four tokens" contradiction without changing play. "Health" in the Major Action list is replaced by the manuscript's own unit (damage cubes) so the action text and the token text agree.
- Mechanical impact: None on play. Clarifies that Estus does not clear hollow markers or conditions (both already stated indirectly in Death & Hollowing and Conditions).
- Follow-on changes required: Delete the DOCX footer paragraph. Character Setup step 5 (line 997) stands. Add "Estus flask" to the Glossary (CMP-0002). Regenerate TOC.
- Status: awaiting-approval

---

### [CMP-0002] GLOSSARY (new chapter) — Proposed Completion
- Current state: The Introduction (line 381) promises "game terms that are written in italics will have quick reference definitions in a glossary at the end of the rule book". The TOC (line 355) lists GLOSSARY at p. 74. No glossary exists in the body. The manuscript italicises about 45 distinct terms inconsistently (see `00_intake_validation.md` §3.7).
- Proposed completion (full chapter; headwords in bold; owning chapter in brackets; `[PROPOSED]` marks a definition the manuscript implies but never states):

  > # GLOSSARY
  >
  > Terms set in *italics* in this book are defined here. Where a definition and a chapter disagree, the chapter governs.
  >
  > **Adjacent node.** A node directly next to another node horizontally, vertically or diagonally. Nodes separated by a wall or by the central wall of a mega-boss game board are not adjacent. [Tiles & Nodes]
  >
  > **Aggro.** The state of being the enemies' preferred target. Enemy behaviours marked with the skull icon target the character who holds the aggro token. [Enemy Turn; Boss Turns]
  >
  > **Aggro token.** The single token that marks the character with aggro. It is placed on the character with the highest threat at the start of each encounter and moves to the character who placed the most wound tokens on enemies during the preceding round of character turns; in boss encounters it moves to any character who damages the boss during their turn. [Gameplay › Encounter Start; Boss Turns › Boss Aggro]
  >
  > **Ambush card.** A face-down card dealt beside each encounter tile when playing with mimics. It is revealed when the characters choose to open that tile's chest and shows either Treasure or Mimic. [Mimics]
  >
  > **Area attack.** A boss attack marked with the area icon. It targets every character within range who occupies a node in one of the arcs marked on the behaviour card. [Boss Turns › Boss Attacks]
  >
  > **Area-of-effect (AoE).** A character attack option marked with the AoE icon. One attack roll is compared against the block or resist value of every enemy on the targeted node. [Character Turn › Character Attacks]
  >
  > **Armour.** An equipment card bearing the armour icon. One armour card may be equipped in the armour slot. Only the armour card's block or resist dice are rolled after a failed dodge. [Equipment; Enemy Turn › Dodge]
  >
  > **Attack option.** One line of a weapon or spell card, showing a stamina cost, dice and modifiers. Using an attack option is the *Attack* major action. [Equipment; Character Turn]
  >
  > **Attack value.** The number of sword icons rolled on an attack, after modifiers and rerolls. For enemies the attack value is the fixed number printed in the attack icon. [Character Turn; Enemy Turn]
  >
  > **Back-up slot.** The dashboard slot that holds up to two treasure cards that are carried but not equipped. Cards in the back-up slot may be swapped into the weapon or armour slots with the *Equip* minor action; an *ember* card must be in the back-up slot to be used. [Characters › Equipment Slots]
  >
  > **Barrel.** A terrain token or model. Models may not *walk*, *run* or *shift* into a node containing a barrel; a model that *dodges* or is pushed into the node destroys the barrel. Barrels are restored when the characters rest at the *bonfire*. [Tiles & Nodes › Terrain]
  >
  > **Basic node.** The most common node type. Basic nodes adjacent to a doorway are also entry nodes. [Tiles & Nodes]
  >
  > **Behaviour card.** A card drawn from a boss, mimic, invader or phantom behaviour deck at the start of that model's turn. Its icons are resolved left to right and it sets the model's attack range and dodge difficulty until the next card is drawn. [Boss Encounters › Boss Behaviour Cards]
  >
  > **Behaviour deck.** The face-down deck of behaviour cards built for a boss, mimic, invader or phantom at the start of its encounter. When it is empty, the discard pile is turned face down without shuffling to form the new deck. [Boss Encounters; Boss Turns]
  >
  > **Behaviour icon.** A movement or attack icon on an enemy data card or a behaviour card. Icons are resolved left to right; an icon with no valid target is skipped. [Enemy Turn › Overview]
  >
  > **Bleed.** A condition. A model may hold one bleed token. If a second bleed token would be placed, the model suffers three damage that ignores block and resist and all bleed tokens are removed. Bleed tokens are removed only when the encounter ends. [Combat Basics › Conditions]
  >
  > **Block.** The defence rolled against a physical attack. The defence total is the sum of the sword icons on the two highest block dice rolled from all equipped cards. For enemies, block is the fixed value subtracted from a physical attack value. [Enemy Turn › Block & Resist; Character Turn › Character Attacks]
  >
  > **Bonfire.** The characters' safe haven, represented by the *bonfire* tile. Resting at the *bonfire* costs one *spark* and fully restores the characters, resets every encounter and allows visits to the Firekeeper and Blacksmith Andre. [Returning to the Bonfire]
  >
  > **Bonfire ascetic.** In campaign play, a one-time communal payment of sixteen *souls* made while resting at the *bonfire* that unlocks tier two treasure and increases every non-boss enemy's attack value by one for the rest of the campaign. [Campaign Play › Bonfire Ascetic]
  >
  > **Boss.** A single powerful enemy whose turns are driven by a behaviour deck and whose base is divided into four arcs. There are three ranks: *mini-boss*, *main-boss* and *mega-boss*. Bosses do not scale with the number of characters and may not be pushed by characters. [Boss Encounters]
  >
  > **Boss arc.** One of the four sectors (front, left, right, back) of a boss's base. Each node on the tile lies in at least one arc; nodes on the line between two arcs lie in both. [Boss Encounters › Boss Arcs and Defence]
  >
  > **Boss tile.** The mini-boss tile or main-boss tile on which a boss encounter is fought. A main-boss encounter uses both boss tiles joined as one large tile. Mega-bosses use the mega-boss game board supplied with their expansion. [Boss Encounters › Boss Encounter Tiles]
  >
  > **Calamity.** A condition from the Black Dragon Kalameet expansion. A model may hold one calamity token, which reduces its block, resist and dodge roll results by one. Calamity tokens are removed only when the encounter ends. [Combat Basics › Conditions]
  >
  > **Catalyst.** A weapon card that stores spells of a matching school: pyromancer flames store pyromancies, staves and catalysts store sorceries, talismans and chimes store miracles. Up to three spells may be stored in a catalyst and their attack options are used as if equipped. [Equipment › Spells]
  >
  > **Chest.** A terrain token or model that blocks movement, dodging and pushes. A chest holds one face-down treasure card of the current tier, revealed when the encounter is *cleared*. With mimics in play, opening a chest requires revealing the tile's *ambush card*. [Tiles & Nodes › Terrain; Mimics]
  >
  > **Class-specific treasure.** A treasure card marked with a small white class emblem. It is sorted into the tier one or tier two deck by its stat requirements exactly as common treasure is. [Setup › Treasure Deck Setup]
  >
  > **Cleared.** The result of an encounter in which every enemy model is defeated and at least one character survives. A *cleared* encounter card is marked with a black cube, rewards *souls* and (the first time only) treasure, and may thereafter be skipped. [Gameplay › Encounter Resolution]
  >
  > **Common treasure.** A treasure card that is not starting, class-specific, transposed, legendary or boss treasure. Common treasure with any stat requirement of 25 or more is tier two; all other common treasure is tier one. [Setup › Treasure Deck Setup]
  >
  > **Condition.** A lasting effect marked by a token on a model: *bleed*, *poison*, *frostbite*, *stagger*, *calamity* or *corrosion*. Conditions are applied when a model is hit by an attack bearing the matching icon. [Combat Basics › Conditions]
  >
  > **Corrosion.** A condition from the Gaping Dragon expansion. A model may hold one corrosion token, which reduces its block roll results by one. The token is removed when the affected character suffers damage. [Combat Basics › Conditions]
  >
  > **Crystal lizard.** An optional enemy from the Iron Keep expansion placed on a terrain node. It flees rather than fights, does not scale its health, does not count towards clearing the encounter, and awards a Titanite card to the character who kills it. [Crystal Lizards]
  >
  > **Damage cube.** A red cube. Each point of damage a character suffers places one damage cube on the endurance bar, filling from the right. A character who must place a damage cube and has no space dies. [Characters › Endurance Bar]
  >
  > **Data card.** The card that defines an enemy, boss, invader or phantom: name, threat, range, dodge difficulty, block and resist, behaviour icons or deck size, health and special ability. [Combat Basics › Enemy Data Cards; Boss Encounters › Boss Data Cards]
  >
  > **Defence total.** The sum of the sword icons on the two highest block or resist dice rolled, after modifiers. Damage suffered equals the enemy's attack value minus the defence total, to a minimum of zero. [Enemy Turn › Block & Resist]
  >
  > **Dodge.** A defence against an attack that targets the character. The character pays one stamina, rolls their dodge dice and succeeds if the total equals or exceeds the attack's dodge difficulty. A successful dodge avoids the hit entirely and the character must move to an adjacent node. [Enemy Turn › Dodge]
  >
  > **Dodge difficulty.** The number a dodge roll must equal or exceed. It is printed on an enemy data card or boss behaviour card. In player versus player it is derived from the stamina cost of the attacker's attack option. [Combat Basics › Enemy Data Cards; Player vs Player]
  >
  > **Doorway.** A gap in a tile's wall through which characters pass between tiles. Basic nodes beside a doorway are entry nodes. [Tiles & Nodes]
  >
  > **Dropped souls.** *Souls* placed on an encounter tile by a character who died there. Only that character may reclaim them, by surviving to *clear* that encounter. They are lost if the character dies again first. [Gameplay › Souls]
  >
  > **Ember card.** A tier one shop card. Discarding an *ember* card from the back-up slot (the *Ember* major action, or outside an encounter) makes the character *embered*. A character may carry only one *ember* card and may not carry one while *embered*. [Equipment › Embers; Gameplay › Embering]
  >
  > **Ember token.** The token placed in the dashboard's ember slot when a character becomes *embered*. It is discarded when the character dies. [Characters › Character Tokens]
  >
  > **Embered.** The state of a character with an *ember* token. An *embered* character has no *hollow* markers, reduces any single attack's damage of three or more by one, may summon a phantom before a boss encounter, and provokes invaders. [Gameplay › Embering]
  >
  > **Encounter.** A battle fought on one or more tiles against the enemies set out by an encounter card. An encounter ends *cleared* or *failed*. [Gameplay › Encounters]
  >
  > **Encounter card.** The card dealt face down to each tile that lists the encounter's level, enemies, terrain and traps. It is revealed when the characters enter the tile. [Game Components › Cards; Setup › Encounter Setup]
  >
  > **Encounter level.** The difficulty of an encounter, from 1 to 4. The levels of the encounters leading to a boss are printed on that boss's data card. Level 4 encounters precede mega-bosses only. [Setup › Encounter Setup]
  >
  > **Endurance bar.** The eight-space track on the dashboard that holds both stamina cubes (filling from the left) and damage cubes (filling from the right). *Hollow* markers reduce it to six usable spaces. [Characters › Endurance Bar]
  >
  > **Entry node.** A basic node beside the doorway through which the characters entered the tile. Characters are placed on entry nodes at the start of an encounter, no more than three to a node. [Tiles & Nodes; Gameplay › Encounter Start]
  >
  > **Equip.** A minor action that swaps cards between the back-up slot and the weapon and armour slots. The inventory may not be used during an encounter. [Character Turn]
  >
  > **Estus flask.** A character token. Flipping it as a major action (*Drink Estus*) removes all damage cubes from the endurance bar. It is readied only by resting at the *bonfire*. [Characters › Character Tokens]
  >
  > **Event card.** A card dealt face down to each encounter tile beside the encounter card and revealed at Encounter Start. Its text modifies that encounter. [Game Components › Cards; Setup › Encounter Setup] [PROPOSED — see CMP-0012]
  >
  > **Failed.** The result of an encounter in which every character dies, or in which any *hollow* character dies. A *failed* encounter awards nothing, its card is turned face down, and the characters must rest at the *bonfire*. [Gameplay › Encounter Resolution]
  >
  > **Final boss.** The last boss of the game: the main-boss, or the mega-boss if the players chose to add one. Defeating the final boss wins the game. [Gameplay › Objective & Loss Conditions]
  >
  > **Firekeeper.** The figure at the *bonfire* who raises character stats in exchange for *souls*. [Returning to the Bonfire › The Firekeeper]
  >
  > **Fog gate.** The token marking the entrance to a boss encounter. In the basic game it moves to the *bonfire* tile after the first boss attempt and provides a shortcut back to the boss. In campaign play it has no effect. [Boss Encounters › The Fog Gate; Campaign Play › The Fog Gate]
  >
  > **Frostbite.** A condition. A frostbitten character cannot recover stamina; a frostbitten enemy reduces its movement values by one. The token is removed at the end of the model's turn. [Combat Basics › Conditions]
  >
  > **Gravestone.** A terrain token or model that blocks all movement and pushes. *Clearing* an encounter that contains a gravestone allows the players to *scry* one card. [Tiles & Nodes › Terrain]
  >
  > **Heat-up.** The point at which a boss, mimic or invader becomes more dangerous. When its health is reduced to or below its heat-up point, a heat-up card (or, for mimics and invaders, an unused standard card) is shuffled into its behaviour deck. Some bosses heat up differently; see Boss Special Rules. [Boss Encounters › Boss Behaviour Cards]
  >
  > **Heat-up card.** A behaviour card marked with the heat-up symbol. Heat-up cards are set aside when the behaviour deck is built and enter play only at heat-up. [Boss Encounters › Boss Behaviour Cards]
  >
  > **Heroic action.** A once-per-rest ability printed on the dashboard, used as a minor action by flipping the *heroic action* token. Its wording overrides other rules. [Characters › Character Tokens]
  >
  > **Hit.** A model is hit by an attack that was in range and that it did not successfully *dodge* or *parry*, even if the attack dealt no damage. Pushes and conditions apply only to models that are hit. [Combat Basics › Target versus Hit]
  >
  > **Hollow.** The state of a character revived after dying. Two white cubes block the two rightmost spaces of the endurance bar. *Hollow* is removed only by resting at the *bonfire* or by becoming *embered*. A *hollow* character who dies is *lost* and the encounter is *failed*. [Gameplay › Death & Hollowing]
  >
  > **Inventory.** A character's face-down stack of unequipped treasure cards. It may be rearranged or traded with only outside encounters. [Characters › Equipment Slots]
  >
  > **Invader.** A hostile phantom drawn by *embered* characters. An invader joins a standard encounter, acts after every character's turn using its own behaviour deck, and awards *souls* and its treasure when killed. [Summons › Invaders]
  >
  > **Legendary treasure.** A rare treasure card marked with an orange light under a chest. Five are shuffled into the tier two deck when the tier two shop is first stocked; in campaign play legendary treasure is obtained only by *transposition*. [Setup › Treasure Deck Setup; Campaign Play › Transposition]
  >
  > **Lost.** The state of a *hollow* character who has died. A *lost* character is removed from play and is revived only when the characters rest at the *bonfire*. [Gameplay › Death & Hollowing] [PROPOSED — see CMP-0006]
  >
  > **Luck.** A character token. Flipping it allows the character to reroll any or all dice of one attack or defence roll; the new results stand. It is readied only by resting at the *bonfire*. [Characters › Character Tokens]
  >
  > **Magical damage.** Damage from an attack marked with the white circle icon. Magical damage is reduced by resist. [Enemy Turn › Enemy Attacks; Character Turn › Character Attacks]
  >
  > **Main-boss.** The second boss of the basic game, fought on both boss tiles after the mini-boss. Its defeat wins the basic game unless a mega-boss follows. [Boss Encounters]
  >
  > **Major action.** The one principal action of a character's turn: *Attack*, *Rest*, *Drink Estus* or *Ember*. [Character Turn]
  >
  > **Mega-boss.** An optional final boss from a mega-boss expansion, fought on its own game board after a Level 4 encounter. Characters who die in a mega-boss encounter are permanently removed from play. [Setup › Setup After the main-boss; Boss Special Rules]
  >
  > **Mimic.** An optional enemy from the Explorers expansion that masquerades as a chest. The Hungry Mimic is fought before the mini-boss is defeated and the Voracious Mimic afterwards; both are fought as mini-boss encounters without arcs. [Mimics]
  >
  > **Mini-boss.** The first boss of the basic game, fought on the mini-boss tile. [Boss Encounters]
  >
  > **Minor action.** An action a character may take any number of times during their turn, subject to its own limits: *Walk* (once), *Run*, *Equip* and *Heroic Action*. [Character Turn]
  >
  > **Node.** A circular space on a tile. Every model occupies exactly one node. Nodes are basic, spawn or terrain. [Tiles & Nodes]
  >
  > **Node model limit.** At most three non-boss models and one boss model may occupy a node. A model entering a full node forces one occupant to be pushed. [Tiles & Nodes › Node Model Limits]
  >
  > **Parry.** A defence available to a character with a shield in the left weapon slot who shares a node with the attacker. The character pays one stamina and rolls dodge dice against the attack's dodge difficulty. Success staggers the attacker and allows a *riposte*; failure deals full damage and staggers the character. [Enemy Turn › Parry & Riposte]
  >
  > **Phantom.** A summoned ally (summon) or a hostile intruder (invader) from the Phantoms expansion. [Summons]
  >
  > **Physical damage.** Damage from an attack marked with the crossed swords icon. Physical damage is reduced by block. [Enemy Turn › Enemy Attacks]
  >
  > **Pillar token.** A terrain token placed on each pillar node of the mega-boss game board in the Asylum Demon expansion. Pillars block movement until destroyed. [Boss Special Rules › Asylum Demon & Stray Demon]
  >
  > **Poison.** A condition. At the end of its turn a model suffers one damage per poison token it holds, ignoring block and resist, then removes one poison token. [Combat Basics › Conditions]
  >
  > **Push.** Forced movement of a model to an adjacent node, caused by a push-attack (the hit model moves directly away from the attacker) or a push-move (characters on nodes the enemy enters move away from it). Pushes cost no stamina and may not move a model into a gravestone or chest. [Combat Basics › Pushing]
  >
  > **Range.** The maximum distance, counted in nodes, between an attacker and its target. Range 0 is the same node; range 1 is an adjacent node; range ∞ is unlimited. [Tiles & Nodes › Range]
  >
  > **Repeat.** An icon that causes an entire attack option or behaviour card to be resolved the number of times shown. [Character Turn › Repeat; Boss Turns › Boss Attacks]
  >
  > **Resist.** The defence rolled against a magical attack, resolved as block is. For enemies, resist is the fixed value subtracted from a magical attack value. [Enemy Turn › Block & Resist]
  >
  > **Rest (major action).** The character removes all stamina cubes from their endurance bar. *Rest* may not be taken in a turn in which the character took the *Run* minor action. [Character Turn]
  >
  > **Resting at the bonfire.** The party action, costing one *spark*, that restores every character, readies all character tokens, removes *hollow* markers, revives *lost* characters, and resets every encounter. [Returning to the Bonfire]
  >
  > **Riposte.** The out-of-turn attack a character makes against an attacker after a successful *parry*, using any attack option of the weapon in the right weapon slot and paying its stamina cost. A *riposte* may not be *parried*. [Enemy Turn › Parry & Riposte]
  >
  > **Run.** A minor action: move one node for one stamina. It may be repeated. A character who *runs* may not *Rest* that turn. [Character Turn]
  >
  > **Scaled (weapon).** A weapon equipped by a character whose relevant stat exceeds the weapon's highest requirement by ten or more. It is marked with a red cube and all its attack options gain +1 attack value. Spells are never scaled. [Character Turn › Stat Scaling]
  >
  > **Scry.** To reveal one hidden card (top card of a treasure deck, a face-down event or encounter card, or the top card of the next boss's behaviour deck) and either return it or send it away as the Gravestones rules describe. [Tiles & Nodes › Terrain › Gravestones]
  >
  > **Section.** In campaign play, one list of tiles ending in one or more bosses. The shop restocks and a free rest is granted only when a section's final boss is defeated. [Campaign Play]
  >
  > **Shaft.** A weapon icon. Attack options with the shaft icon may not target models on the attacker's own node. [Character Turn › Shaft]
  >
  > **Shift.** A weapon or phantom behaviour icon allowing movement of the number of nodes shown, before or after the dice are rolled according to its position on the line. *Shift* movement costs no stamina. [Character Turn › Shift]
  >
  > **Shop.** Blacksmith Andre's stock of face-up treasure cards, in tier one and tier two piles. Shops are stocked at setup and restocked only after a boss is defeated (in campaign play, after a section is completed). [Setup › Shop Setup; Returning to the Bonfire › Shop Rules]
  >
  > **Souls.** The currency of the game, tracked by soul tokens on each character's dashboard. *Souls* are gained by *clearing* encounters and killing invaders, dropped on death, and spent at the *bonfire*. *Souls* may not be transferred between characters. [Gameplay › Souls]
  >
  > **Spark.** The *bonfire*'s charges, tracked on the spark dial. The characters begin with six minus the number of characters, gain one for each boss defeated, and spend one each time they rest at the *bonfire*. [Gameplay › Sparks]
  >
  > **Spawn node.** A node on which enemy models are placed at the start of an encounter. Boss tiles have a boss spawn node. [Tiles & Nodes]
  >
  > **Stagger.** A condition. A staggered model subtracts one from its attack, block, resist and dodge totals. The token is removed at the end of the model's turn. A character who must place a stamina cube with no space available is staggered instead. [Combat Basics › Conditions; Characters › Endurance Bar]
  >
  > **Stamina cube.** A black cube. Each point of stamina a character spends places one stamina cube on the endurance bar, filling from the left. [Characters › Endurance Bar]
  >
  > **Starting equipment.** The three or four equipment cards a character begins with. Starting equipment may not be sold. [Setup › Treasure Deck Setup]
  >
  > **Stat tier.** A character's position on each stat track (base, tier one, two, three or four), marked with a white cube or, at tier four, a red cube. Tiers are bought in sequence from the Firekeeper. [Characters › Stat Progression Track; Returning to the Bonfire › The Firekeeper]
  >
  > **Strafe card.** A card from the Black Dragon Kalameet expansion drawn when a strafe icon is resolved; it shows the nodes attacked and the node on which Kalameet lands. [Boss Special Rules › Black Dragon Kalameet]
  >
  > **Summon.** A friendly phantom that an *embered* character may call at the fog gate before a boss encounter by paying two *souls*. A summon acts after the characters each round and leaves play when its health reaches zero or the encounter ends. [Summons › Phantoms]
  >
  > **Target.** The model an attack is directed at. Enemies never target enemies; characters target characters only in player versus player. [Combat Basics › Target versus Hit]
  >
  > **Terrain.** Gravestones, barrels, chests, pillars and traps. Terrain tokens are placed on terrain nodes at encounter setup and are not moved when encounters reset. [Tiles & Nodes › Terrain]
  >
  > **Threat.** The value that fixes turn order. Enemies act in descending threat before the characters, who then act in descending threat. The character with the highest threat takes the aggro token at the start of each encounter. [Gameplay › Encounter Turn Order]
  >
  > **Tier one / tier two treasure.** The two treasure decks. Tier one holds common and class-specific treasure with every stat requirement below 25; tier two holds the rest plus transposed treasure and five legendary cards. Encounter rewards and chests draw from tier one until the mini-boss is defeated and from tier two thereafter (in campaign play, after the *bonfire ascetic* is burnt). [Setup › Treasure Deck Setup]
  >
  > **Titanite.** A weapon upgrade (Titanite Shard, Chunk or Slab, and Titanite Scale) that is fused permanently to the weapon it is attached to and is returned to the bottom of the tier one treasure deck with that weapon when it is sold. [Equipment › Upgrades]
  >
  > **Track behaviour card.** A numbered card from the Executioner's Chariot expansion used, in fixed order, for the Chariot's turns before it heats up. [Boss Special Rules › Executioner's Chariot]
  >
  > **Transposed treasure.** A class treasure card marked with a blue light. All transposed treasure is tier two. [Setup › Treasure Deck Setup]
  >
  > **Transposition.** In campaign play, exchanging one boss treasure card and four *souls* for one of the five face-up legendary treasure cards while resting at the *bonfire* after the first section's final boss. [Campaign Play › Transposition]
  >
  > **Trap token.** A face-down token dealt to basic nodes when an encounter card shows the trap symbol. It is flipped and resolved against every model on its node when a character enters or is pushed onto the node. [Tiles & Nodes › Terrain › Traps]
  >
  > **Turn.** One model's activation. Enemies take their turns, then characters take theirs; in boss encounters the boss takes a turn after each character. [Gameplay › Encounter Turn Order; Boss Turns]
  >
  > **Two-handed.** A weapon bearing the two-handed icon, or a one-handed weapon equipped with the other weapon slot empty. Two-handed attacks may reroll one die. Spells are never two-handed. [Character Turn › Two-Handed Attacks]
  >
  > **Upgrade card.** A card attached beneath a weapon or armour card by Blacksmith Andre, up to the equipment's upgrade limit. Upgrade spells are instead attached as a main action during an encounter and return to the inventory afterwards. [Equipment › Upgrades]
  >
  > **Walk.** A minor action, once per turn: move one node for no stamina. [Character Turn]
  >
  > **Weak arc.** A boss arc shown in red on the most recently resolved behaviour card. A character attacking a boss from a weak arc adds one black die. [Boss Encounters › Attacking Bosses and Weak Arcs]
  >
  > **Wind Up.** A behaviour icon. When it is resolved, each character may spend one stamina to move to an adjacent node; the movement counts as a *Run*. [Boss Special Rules]
  >
  > **Wound token.** A token placed on an enemy's base for each point of damage it suffers. An enemy with wound tokens equal to or exceeding its scaled health is killed. Bosses use a health dial instead. [Combat Basics › Enemy Data Cards]

- Design rationale: Every definition restates a rule the manuscript already makes, in the manuscript's own terms, so the glossary never becomes a second rulebook that drifts from the first; the opening line makes the chapter subordinate to the rules text. Terms the manuscript uses without defining (event card, lost, pillar token) are tagged and tied to the CMP that defines them. Expansion-specific terms (strafe card, track behaviour card, calamity, corrosion) are included because the manuscript already uses or lists them.
- Mechanical impact: None; definitions only. Two definitions resolve ambiguities the body leaves open and are therefore marked: the aggro token's movement in standard encounters ("most wound tokens") and the summon's turn timing (after the characters each round, per Summons › Phantoms step 6).
- Follow-on changes required: Italicisation pass across the body so that the set of italicised terms equals the set of headwords (Phase 2A). Add "Pillar token", "Event card" and "Ambush card" to Game Components (CMP-0012). Convert bracketed chapter names to section numbers at layout.
- Status: awaiting-approval

---

### [CMP-0003] F.A.Q. (chapter) — Proposed Completion
- Current state: Line 3098 is a bare heading "# F.A.Q." followed by an empty page-break heading (line 3100). No content. STUB.
- Proposed completion (full chapter; each answer applies the manuscript's own rules; where the manuscript is silent the ruling is marked [PROPOSED] and is coordinated with the CMP named):

  > # F.A.Q.
  >
  > **Q.** May a *hollow* character skip previously *cleared* encounters?
  > **A.** Yes, subject to the endurance bar. Skipping costs every character two stamina cubes per encounter skipped. A character may never place a stamina cube when there is no space for it, so a *hollow* character (six spaces) may contribute to skipping at most three encounters and only while their bar is otherwise empty. If any character cannot pay, the characters may not skip that far.
  >
  > **Q.** Who holds the aggro token when its holder dies?
  > **A.** When the character with the aggro token dies, move the token at once to the surviving character with the highest *threat*. Enemy behaviours that target the aggro token target that character from then on. [PROPOSED]
  >
  > **Q.** Does *frostbite* stop the one stamina recovered at the start of a character's turn?
  > **A.** Yes. A frostbitten character recovers no stamina by any means, including the start-of-turn recovery and the *Rest* major action, until the token is removed at the end of their turn.
  >
  > **Q.** May a character *Rest* after *Walking*?
  > **A.** Yes. Only the *Run* minor action prevents *Rest* in the same turn. *Walk*, *Equip*, *Heroic Action* and *Shift* movement do not.
  >
  > **Q.** In a four-character game, does the added *Repeat* apply to push-moves and push-attacks?
  > **A.** No. The scaling *Repeat* is added only to attack icons (crossed swords or white circle). Movement icons, including push-moves that deal damage, are not repeated.
  >
  > **Q.** Does the one-spell-per-turn limit include upgrade spells?
  > **A.** Yes. Attaching an upgrade spell is a main action resolved like casting an attack spell and counts as the character's one spell attack option for the turn.
  >
  > **Q.** May the two-handed reroll be used together with the *luck* token?
  > **A.** Yes. The two-handed reroll rerolls one die; the *luck* token rerolls any or all dice. Each may be used once on the same roll, in either order, and each new result stands.
  >
  > **Q.** Are *Ornstein & Smough* one boss or two?
  > **A.** One boss. They share one data card, one health dial and one behaviour deck, and heat up once. Both models are placed on the main-boss tile and each behaviour card states which model acts. A character attacking either model attacks the boss, and the weak-arc bonus is judged against the model attacked. The boss node limit applies to each model separately. See Boss Special Rules.
  >
  > **Q.** May a character *dodge* into a node containing a barrel?
  > **A.** Yes. The barrel is destroyed and its token removed. A character may not *dodge* into a node containing a gravestone or chest, and a character who has no valid adjacent node may still roll to *dodge* but does not move.
  >
  > **Q.** Who decides ties?
  > **A.** The players decide, collectively. If they cannot agree, the character holding the aggro token decides. Ties in character *threat* are settled this way once at the start of the encounter and the order is kept for the whole encounter.
  >
  > **Q.** Can an invader appear in a boss encounter?
  > **A.** No. Invader tokens are placed only on face-down encounter cards on exploration tiles. Boss tiles never carry an invader token.
  >
  > **Q.** Can a summon and an invader be in the same encounter?
  > **A.** No. Summons are called only at the fog gate for boss encounters; invaders appear only in exploration encounters.
  >
  > **Q.** When does a summon act in a boss encounter?
  > **A.** After the last character in *threat* order has taken their turn and before the boss's next turn. The summon therefore acts once per round, not after each character.
  >
  > **Q.** A chest's ambush card reveals a mimic and every character dies. What happens?
  > **A.** The mimic encounter is *failed*: all *souls* are dropped on the tile, the encounter card is turned face down and the characters must rest at the *bonfire*. The chest stays closed. When the characters next *clear* that tile's encounter, the mimic must be fought again before the chest is opened, until it is killed.
  >
  > **Q.** What is the "reduced *soul* reward" for an encounter *cleared* a second time?
  > **A.** Half the full reward, rounded down. See the Reduced column of the Soul Reward Table and the Campaign Soul Reward Table. [PROPOSED — CMP-0010]
  >
  > **Q.** When may the characters transpose boss treasure in a campaign?
  > **A.** Only while resting at the *bonfire* after spending a *spark*, and only once the final boss of the first section has been defeated. The free rest granted on defeating a section's final boss does not allow transposition.
  >
  > **Q.** May a new player join a game in progress?
  > **A.** In campaign play, yes, at the cost of one *spark*; the new character begins with starting stats and equipment and the maximum number of *sparks* is recalculated. In the basic game a new character joins on the same terms, while the characters are resting at the *bonfire*. [PROPOSED]
  >
  > **Q.** Does *Drink Estus* remove *hollow* markers, condition tokens or stamina cubes?
  > **A.** No. It removes damage cubes only.
  >
  > **Q.** How is *stagger* applied to a roll?
  > **A.** Subtract one from the final total of the attack, block, resist or dodge roll, after the two highest dice are summed and after all rerolls. It is not applied to each die.
  >
  > **Q.** How is a block or resist roll resolved with one die or no dice?
  > **A.** With one die, the defence total is that die's result. With no dice, the defence total is zero and the character suffers the attack's full value.
  >
  > **Q.** May a character with no dodge dice attempt to *dodge*?
  > **A.** Yes. Against dodge difficulty 0 the dodge succeeds automatically for one stamina. Against any higher difficulty the character may pay one stamina and roll nothing (the dodge fails and the character is hit, blocking with armour dice only) or pay three stamina to roll one die.
  >
  > **Q.** After a failed *dodge*, do armour dice modifiers still apply?
  > **A.** Yes. Roll only the armour card's block or resist dice and apply the armour card's own modifiers. Dice and modifiers from weapons, shields and spells are ignored.
  >
  > **Q.** May a character with a two-handed weapon *parry*?
  > **A.** No. A *parry* requires a shield in the left weapon slot; a two-handed weapon occupies both weapon slots. A one-handed weapon wielded two-handed (other slot empty) also prevents a *parry*.
  >
  > **Q.** Which weapon slot is "left" and which is "right"?
  > **A.** The slot printed on the left of the dashboard is the left weapon slot and the slot printed on the right is the right weapon slot. Cards may be moved between them with the *Equip* minor action.
  >
  > **Q.** May an enemy *dodge* or *parry* a *riposte*?
  > **A.** No. Enemies never *dodge* or *parry*. A *riposte* is resolved as a normal character attack against the enemy's block or resist value. Against a boss, the weak-arc bonus applies if the character is in a weak arc.
  >
  > **Q.** Does the *embered* damage reduction apply to *bleed*, *poison* and trap damage?
  > **A.** No. It applies only to damage from a single attack that would deal three or more damage.
  >
  > **Q.** An invader is present and a character dies. Does the encounter continue?
  > **A.** Yes. The invader vanishes at once without reward and the encounter continues against the remaining enemies. The invader does not return.
  >
  > **Q.** After resting at the *bonfire*, may a *cleared* encounter still be skipped?
  > **A.** Yes. Resting resets every encounter (its enemies return), but the black cube marking an encounter *cleared* stays on its card. A reset encounter that was *cleared* may be skipped for two stamina per character or fought again for the reduced *soul* reward. A reset encounter that was *failed*, or never *cleared*, must be fought. See CMP-0019.
  >
  > **Q.** Does a Level 4 encounter reset when the characters rest?
  > **A.** No. Once *cleared*, a Level 4 encounter is not fought again; the mega-boss game board is flipped to its boss side. A *failed* Level 4 encounter resets as any other. [PROPOSED — CMP-0023]
  >
  > **Q.** Do dead and *lost* characters count for enemy scaling?
  > **A.** Yes. Enemy health, movement, attack and *Repeat* scaling use the total number of characters in the game, whether or not they are currently in play.
  >
  > **Q.** May a character pool *souls* with another character?
  > **A.** Only for the *bonfire ascetic*, which is paid communally. Firekeeper upgrades, purchases, phantom summoning and transposition are paid from the acting character's own *souls*.
  >
  > **Q.** Where does a sold boss treasure card go?
  > **A.** To the game box. Boss treasure never enters a treasure deck.
  >
  > **Q.** Do *crystal lizards* prevent an encounter being *cleared*?
  > **A.** No. The encounter is *cleared* when every other enemy model is defeated; surviving *crystal lizards* escape and award nothing.
  >
  > **Q.** Does a character who *dodges* onto a face-down trap token trigger it?
  > **A.** Yes. Any character movement onto the node, including *dodge*, *shift* and pushes, flips the token and resolves it against every model on the node.
  >
  > **Q.** The characters are forced to rest but the *spark* dial shows zero. What happens?
  > **A.** The players lose the game. See Objective & Loss Conditions and CMP-0020. [PROPOSED]
  >
  > **Q.** A character is pushed off a boss's node by a boss attack. Must they stay in the same arc?
  > **A.** Yes. A character pushed off a boss's node moves to the centre-most valid node in the arc they occupied, or to any valid node in that arc, or, if the arc holds no valid node because of a wall, to any adjacent node touching that wall.
  >
  > **Q.** May a *heroic action* be used during another model's turn?
  > **A.** Only if the dashboard says so. Otherwise it is a minor action taken during the character's own turn.

- Design rationale: Each question is one the body leaves open or answers in two places. Answers restate the governing rule and name the chapter so the F.A.Q. never carries a rule of its own; the four rulings the body does not reach (aggro on death, basic-game joining, Level 4 reset, zero-spark forced rest) are tagged and routed to their CMP. The official FAQ's rulings on dodge-with-zero-dice and failed-dodge pushes are compatible with the manuscript and are reflected; its ruling that a push from a boss attack ignores arcs conflicts with the manuscript's Character Arc Movement text and is not adopted. The O&S answer is limited to what the Core rulebook supports (one data card, one dial, one deck).
- Mechanical impact: None beyond the tagged rulings; those are resolved in CMP-0006, CMP-0010, CMP-0019, CMP-0020 and CMP-0023.
- Follow-on changes required: Delete the empty heading at line 3100. Cross-reference section numbers at layout. If any tagged CMP is rejected, delete or amend the corresponding answer.
- Status: awaiting-approval

---
