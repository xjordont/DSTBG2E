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

### [CMP-0004] COMMUNITY UPDATE PACK (appendix) — Proposed Completion
- Current state: Lines 3102–3366. A skeleton: a bold label "Treasure - Official" over 33 bare card names split by a stray comment marker (line 3154); "Treasure - Errata/Updated" over 13 one-line notes (Chloranthy Ring listed twice, lines 3188 and 3200; Demon Titanite with no note); one paragraph of prose (line 3208); a 60-row weapon stat table set as plain text with a bold header line (lines 3210–3330); "Enemy Data" (12 bare names, "Skeleton Beast" vs the component list's "Skeletal Beast", line 469) and "Boss Data & Behaviours" (4 bare names). No introduction, no card texts, no table formatting. SKELETON.
- Proposed completion (full appendix):

  > # COMMUNITY UPDATE PACK
  >
  > ## What the Pack Is
  >
  > The Community Update Pack is a set of print-and-play cards that accompanies this edition. It supplies three things that the published sets do not: additional treasure cards that bring equipment from the Tomb of Giants and Painted World of Ariamis sets into the shared treasure decks; revised treasure cards whose rules or requirements have changed in this edition; and replacement enemy and boss cards for the Tomb of Giants and Painted World of Ariamis sets, so that those enemies use the data card, behaviour card and health formats described in this book.
  >
  > Every card in the pack is used in place of, or in addition to, the card of the same name in the published sets, as stated in each list below. Where a card in the pack and a published card disagree, the pack card governs. Cards are sorted into the treasure decks by the rules in Setup › Treasure Deck Setup, using the requirements printed on the pack card.
  >
  > ## Additional Treasure
  >
  > The following treasure cards are added to the treasure decks. Each is sorted by its printed requirements and type.
  >
  > Weapons and shields: Throwing Knives · Velka's Rapier · Soul Spear · Pike · Lothric Knight Greatsword · Exile Greatsword · Bloodshield · Sunlight Shield · Black Knight Sword · Crescent Axe · Thorolund Talisman · Carthus Curved Greatsword · Black Knight Greataxe · Bonewheel Shield · Red and White Round Shield · Hollow Soldier Shield · Greatsword · Tower Shield · Priscilla's Dagger · Lifehunt Scythe · Black Knight Halberd · Black Knight Shield · Gravelord Sword.
  >
  > Armour: Xanthous Robes · Painting Guardian Armour · Paladin Armour · Cleric Armour · Steel Armour.
  >
  > Items, upgrades and spells: Red Tearstone Ring · Skull Lantern · Mask of the Child · Divine Blessing · Blue Titanite · Gravelord Sword Dance.
  >
  > ## Revised Treasure
  >
  > The following cards replace the published card of the same name. The rule text below is the text printed on the pack card. Where only part of a card changes, the unchanged parts are as printed on the published card.
  >
  > **Demon Titanite.** Weapon upgrade (Titanite). *Rule text, requirements and type as the published card; included in the pack so that the Titanite family is printed in one format.* [PROPOSED — the manuscript lists this card with no note; confirm whether a rule change is intended]
  >
  > **Blue Titanite.** Weapon upgrade (Titanite). Rule text as the published card. Requirements: INT 25. Legendary. *Changed from boss treasure to legendary treasure; INT requirement raised to 25.*
  >
  > **Titanite Chunk.** Weapon upgrade (Titanite). +2 to the attack value of every attack option. May be attached only to a weapon that has a Titanite Shard attached; the Titanite Shard is returned to the bottom of the tier one treasure deck. Requirements: STR 25, DEX 25. Common (tier two).
  >
  > **Titanite Slab.** Weapon upgrade (Titanite). +3 to the attack value of every attack option. May be attached only to a weapon that has a Titanite Chunk attached; the Titanite Chunk is returned to the bottom of the tier two treasure deck. Requirements: STR 25, DEX 25. Legendary.
  >
  > **Tiny Being's Ring.** Armour upgrade. At the start of the equipped character's turn, remove one damage cube from their endurance bar.
  >
  > **Chloranthy Ring.** Armour upgrade. At the start of the equipped character's turn, that character and every other character on the same node recover one additional stamina. *(The two manuscript notes on this card are merged into this single text.)*
  >
  > **Sellsword Twinblades.** Weapon. The one-handed version is used; the later two-handed version is not. Rule text as the one-handed published card.
  >
  > **Black Leather Armour.** Armour. The equipped character pays no stamina to attempt a *dodge*. Dice and requirements as the first published version.
  >
  > **Wolf Ring.** Armour upgrade. After rolling dodge dice, the equipped character may pay one stamina to reroll any or all of those dice. The reroll may be used once per dodge.
  >
  > **Eastern Armour.** Armour. The equipped character pays one additional stamina to attempt a *dodge*. Dice and requirements as the first published version.
  >
  > **Carthus Milkring.** Armour upgrade. +1 to the equipped character's dodge roll total.
  >
  > **Covetous Silver Serpent Ring.** Armour upgrade. When the equipped character receives a *soul* reward for *clearing* an encounter, they receive one additional *soul*.
  >
  > **Mon Ring.** Item. The printed effect may be used once between rests: flip the card face down when it is used and face up when the characters rest at the *bonfire*. [PROPOSED — the manuscript says "one use per floor"; "floor" is not a term of this edition and is read as the exploration between two rests]
  >
  > ## Revised Weapon Requirements
  >
  > Many published weapons carry intelligence or faith requirements although their attacks deal physical damage. This edition removes those requirements and, where a weapon then had no strength or dexterity requirement, adds one; where a weapon already had both, its primary requirement is raised so that its overall difficulty to equip is unchanged. The requirements below replace those printed on the published cards. A weapon is tier one if every requirement is below 25 and tier two otherwise.
  >
  > | Weapon | STR | DEX | INT | FTH | Tier |
  > |---|---|---|---|---|---|
  > | Avelyn | 23 | 30 | 0 | 0 | Two |
  > | Bewitched Alonne Sword | 18 | 24 | 0 | 0 | One |
  > | Black Knight Greataxe | 32 | 20 | 0 | 0 | Two |
  > | Black Knight Halberd | 32 | 18 | 0 | 0 | Two |
  > | Brigand Axe | 19 | 16 | 0 | 0 | One |
  > | Butcher Knife | 25 | 0 | 0 | 0 | Two |
  > | Caestus | 0 | 15 | 0 | 0 | One |
  > | Carthus Curved Greatsword | 19 | 30 | 0 | 0 | Two |
  > | Carthus Curved Sword | 25 | 35 | 0 | 0 | Two |
  > | Chariot Lance | 22 | 33 | 0 | 0 | Two |
  > | Claws | 0 | 20 | 0 | 0 | One |
  > | Crystal Straight Sword | 21 | 30 | 0 | 0 | Two |
  > | Dark Silver Tracer | 0 | 25 | 0 | 0 | Two |
  > | Dragon Tooth | 40 | 25 | 0 | 0 | Two |
  > | Drake Sword | 27 | 17 | 0 | 0 | Two |
  > | Drakewing Ultra Greatsword | 33 | 23 | 0 | 0 | Two |
  > | East-West Shield | 28 | 0 | 0 | 0 | Two |
  > | Falchion | 37 | 30 | 0 | 0 | Two |
  > | Four-Pronged Plough | 23 | 18 | 0 | 0 | One |
  > | Giant's Halberd | 27 | 16 | 0 | 0 | Two |
  > | Gold Tracer | 25 | 35 | 0 | 0 | Two |
  > | Gravelord Sword | 32 | 18 | 0 | 0 | Two |
  > | Great Mace | 28 | 0 | 0 | 0 | Two |
  > | Halberd | 31 | 18 | 0 | 0 | Two |
  > | Irithyll Rapier | 24 | 24 | 0 | 0 | One |
  > | Irithyll Straight Sword | 23 | 23 | 0 | 0 | One |
  > | Lifehunt Scythe | 32 | 23 | 0 | 0 | Two |
  > | Lucerne | 22 | 31 | 0 | 0 | Two |
  > | Mace | 16 | 0 | 0 | 0 | One |
  > | Manikin Claws | 24 | 24 | 0 | 0 | One |
  > | Morning Star | 16 | 0 | 0 | 0 | One |
  > | Murakumo | 27 | 17 | 0 | 0 | Two |
  > | Onikiri and Ubadachi | 26 | 36 | 0 | 0 | Two |
  > | Painting Guardian Curved Sword | 18 | 26 | 0 | 0 | Two |
  > | Parrying Dagger | 14 | 21 | 0 | 0 | One |
  > | Partizan | 28 | 17 | 0 | 0 | Two |
  > | Pike | 23 | 16 | 0 | 0 | One |
  > | Poison Throwing Knives | 0 | 14 | 0 | 0 | One |
  > | Priscilla's Dagger | 0 | 31 | 0 | 0 | Two |
  > | Rapier | 14 | 21 | 0 | 0 | One |
  > | Reinforced Club | 23 | 0 | 0 | 0 | One |
  > | Rotten Ghru Dagger | 17 | 17 | 0 | 0 | One |
  > | Rotten Ghru Spear | 12 | 21 | 0 | 0 | One |
  > | Royal Dirk | 18 | 31 | 0 | 0 | Two |
  > | Scimitar | 18 | 20 | 0 | 0 | One |
  > | Shield Crossbow | 33 | 20 | 0 | 0 | Two |
  > | Shotel | 26 | 29 | 0 | 0 | Two |
  > | Silver Knight Spear | 22 | 26 | 0 | 0 | Two |
  > | Silver Knight Straight Sword | 16 | 22 | 0 | 0 | One |
  > | Spiked Mace | 32 | 22 | 0 | 0 | Two |
  > | Spotted Whip | 23 | 30 | 0 | 0 | Two |
  > | Sunlight Straight Sword | 15 | 15 | 0 | 0 | One |
  > | Throwing Knives | 0 | 14 | 0 | 0 | One |
  > | Uchigatana | 14 | 32 | 0 | 0 | Two |
  > | Umbral Dagger | 18 | 35 | 0 | 0 | Two |
  > | Vordt's Great Hammer | 33 | 0 | 0 | 0 | Two |
  > | Warden Twinblades | 17 | 25 | 0 | 0 | Two |
  > | Washing Pole | 37 | 21 | 0 | 0 | Two |
  > | Winged Knight Halberd | 32 | 16 | 0 | 0 | Two |
  > | Winged Spear | 20 | 22 | 0 | 0 | One |
  >
  > ## Enemy Data Cards
  >
  > The pack supplies one replacement data card for each enemy below, in the format described in Combat Basics › Enemy Data Cards (threat, attack range, dodge difficulty, block and resist, behaviour icons, base health). The replacement card is used with the published miniature and in place of the published card or token.
  >
  > - Bonewheel Skeleton (Painted World of Ariamis) — replacement data card.
  > - Crow Demon (Painted World of Ariamis) — replacement data card.
  > - Engorged Zombie (Painted World of Ariamis) — replacement data card.
  > - Phalanx (Painted World of Ariamis) — replacement data card.
  > - Phalanx Hollow (Painted World of Ariamis) — replacement data card.
  > - Snow Rat (Painted World of Ariamis) — replacement data card.
  > - Giant Skeleton Archer (Tomb of Giants) — replacement data card.
  > - Giant Skeleton Soldier (Tomb of Giants) — replacement data card.
  > - Necromancer (Tomb of Giants) — replacement data card.
  > - Skeleton Archer (Tomb of Giants) — replacement data card.
  > - Skeleton Beast (Tomb of Giants) — replacement data card.
  > - Skeleton Soldier (Tomb of Giants) — replacement data card.
  >
  > ## Boss Data and Behaviour Cards
  >
  > The pack supplies, for each boss below, one replacement data card in the format described in Boss Encounters › Boss Data Cards (threat, behaviour deck size, heat-up point, block and resist, special ability, encounter levels, starting health, boss type) and a full set of behaviour cards in the format described in Boss Encounters › Boss Behaviour Cards. These are used with the published miniature and health dial in place of the published cards.
  >
  > - Black Knight (Tomb of Giants) — mini-boss; replacement data card and behaviour deck.
  > - Crossbreed Priscilla (Painted World of Ariamis) — main-boss; replacement data card and behaviour deck.
  > - Gravelord Nito (Tomb of Giants) — main-boss; replacement data card and behaviour deck.
  > - Heavy Knight (Painted World of Ariamis) — mini-boss; replacement data card and behaviour deck.

- Design rationale: The appendix is written so that a reader who owns the pack knows exactly which published card each pack card displaces and how to sort it, using only this book's vocabulary. Card texts are drafted from the manuscript's notes and follow the book's action grammar (start-of-turn triggers, stamina costs, deck returns). The two unexplained notes (Demon Titanite; "per floor") are translated and tagged rather than silently invented. The weapon list is unchanged except for one typographical normalisation ("Onikiri And Ubadachi" → "and"); tiers are computed from the ≥25 rule in Setup. "Skeleton Beast" follows the Tomb of Giants rulebook's component name; the component list (line 469, "Skeletal Beast") is to be aligned.
- Mechanical impact: Titanite Chunk/Slab chaining (Shard → Chunk → Slab) is now explicit; Wolf Ring reroll is limited to once per dodge; Covetous Silver Serpent Ring is tied to encounter clear rewards; Mon Ring is limited to once per rest. Tier assignments move nineteen revised weapons into tier one and forty-one into tier two.
- Follow-on changes required: Align Game Components › Enemies line 469 ("Skeletal Beast" → "Skeleton Beast"). Delete the stray comment marker at line 3154 and the duplicate Chloranthy entry. Confirm Demon Titanite and Mon Ring intent with the author. Confirm the "Painted World of Ariamis" and "Tomb of Giants" set names for the pack cards. Layout: set the table as a true table; consider landscape or two-column.
- Status: awaiting-approval

---

### [CMP-0005] BOSS SPECIAL RULES (chapter) — Proposed Completion (partly BLOCKED — source booklet not supplied)
- Current state: Lines 2199–2213 cover only "Asylum Demon & Stray Demon" (Pillar Smasher, Wind Up). Setup After the main-boss step 11 (line 1195) defers to "any special rules described in the mega-boss rule booklet" — an external reference. No rules exist for the Core bosses, Darkroot, Iron Keep, Explorers, Tomb of Giants or any other mega-boss, although all are listed in Game Components and used in CAMPAIGNS. Booklets supplied: Core, Tomb of Giants (V2), Darkroot, Iron Keep, Explorers, Phantoms, Black Dragon Kalameet, Executioner's Chariot. Not supplied: Asylum Demon, Four Kings, Gaping Dragon, Guardian Dragon, Manus, Old Iron King, Vordt, The Last Giant, Painted World of Ariamis.
- Proposed completion (full chapter replacement; the existing Asylum/Stray Demon text is retained and re-ordered; BLOCKED placeholders are given in the structure the finished entries use):

  > # BOSS SPECIAL RULES
  >
  > Every boss's data card carries a special ability that applies throughout its encounter. This chapter gives the further rules that particular bosses require. A boss that is not listed here has no rules beyond its data card and the general boss rules.
  >
  > Where this chapter and a data card disagree, this chapter governs.
  >
  > ## Rules Common to Several Bosses
  >
  > **Zero dodge difficulty.** When a behaviour card shows a dodge difficulty of 0, a character may pay one stamina to *dodge* the attack without rolling, even with no dodge dice, as the Dodge rules describe. The character may instead block or resist as usual.
  >
  > **Two boss models in one encounter.** When an encounter contains two boss models, the boss node limit applies to each model separately: a node may hold one boss model, and a boss model that moves onto a node containing the other pushes it. Characters sharing a node with a boss model are placed in that model's arcs.
  >
  > ## Core Set
  >
  > **Gargoyle, Titanite Demon, Boreal Outrider Knight, Winged Knight, Dancer of the Boreal Valley.** No rules beyond the data card.
  >
  > **Twin Gargoyles.** Some campaign sections list the Gargoyle twice. The two Gargoyle encounters form one boss encounter in two parts. When the first Gargoyle is slain, the encounter does not end: at once place the second Gargoyle on the boss spawn node facing the centre of the tile, set its health dial to its starting health, and build a new behaviour deck for it. The characters remain where they are, recover nothing, and characters who died remain dead. *Souls*, boss treasure, the *spark* and the *ember* tokens are awarded once, when the second Gargoyle is slain. If the characters are defeated by either Gargoyle, the boss encounter is *failed* and both Gargoyles must be fought again. [PROPOSED adaptation of the Core campaign footnote]
  >
  > **Dragonslayer Ornstein & Executioner Smough.** Ornstein & Smough are one boss: one data card, one health dial, one behaviour deck, one heat-up. Place both models on the main-boss tile as the data card directs; each behaviour card states which model acts and which model's arcs its attack uses. A character attacking either model attacks the boss; the weak-arc bonus is judged against the arcs of the model attacked. The rule for two boss models in one encounter applies. *The placement of the second model, the behaviour cards' model markings and the effect of heat-up on the pair are printed on the data card and behaviour cards; this chapter adds nothing to them.* BLOCKED — the Core rulebook prose contains no dual-boss rule; the data card is the only source and is not supplied.
  >
  > ## Asylum Demon Expansion — Asylum Demon and Stray Demon
  >
  > ### Pillar Smasher
  >
  > During the boss encounter setup, place one pillar token on each of the four pillar nodes found on the mega-boss game board. Pillars block movement.
  >
  > When the Asylum Demon or Stray Demon makes a physical attack with an *area* icon, check whether any pillar token lies within the affected arcs and range. Each character within one node of such a pillar token immediately suffers one damage and the *stagger* condition; then remove that pillar token from the tile. Resolve the *area* attack itself (including any pushes or dodges) after every pillar's destruction is resolved. A single attack may destroy several pillars, and a model may be hit by several shattering pillars at once.
  >
  > Once a pillar is destroyed, its node is a basic node for the rest of the encounter. When the characters rest at the *bonfire*, return every destroyed pillar to its pillar node.
  >
  > ### Wind Up
  >
  > When a Wind Up behaviour icon is resolved, each character may spend one stamina to move their model to an adjacent node. This movement counts as a *Run*.
  >
  > *The Asylum Demon booklet was not supplied; the two rules above are the manuscript's own text and are retained unchanged.* BLOCKED for any further rule the booklet defines (mega-boss game board layout, Level 4 encounter cards, treasure).
  >
  > ## Darkroot Expansion
  >
  > **Great Grey Wolf Sif (main-boss).** Several of Sif's behaviour cards have dodge difficulty 0. Sif's behaviour deck includes cool-down cards that show Sif weakened near death; they are used exactly as the data card directs. No other rules beyond the data card.
  >
  > **Artorias (main-boss).** Several of Artorias's behaviour cards have dodge difficulty 0. *Heat-up:* when Artorias's health is reduced to or below his heat-up point, do not shuffle in one heat-up card. Instead remove two random cards from his behaviour deck and return them to the box, then shuffle all three of his heat-up cards into the behaviour deck.
  >
  > ## Iron Keep Expansion
  >
  > **Smelter Demon (main-boss).** *Heat-up:* when the Smelter Demon's health is reduced to or below its heat-up point, do not shuffle in one heat-up card. Instead return the whole five-card behaviour deck and its discard pile to the box, and replace them with a new behaviour deck of five random heat-up cards, shuffled.
  >
  > **Sir Alonne (main-boss).** No rules beyond the data card.
  >
  > ## Explorers Expansion
  >
  > **Old Dragonslayer (mini-boss).** The Old Dragonslayer uses the Ornstein miniature with its own health dial, data card, eight behaviour cards and treasure cards. *Corrupted Dragonslayer:* the first three times the Old Dragonslayer loses four or more health from a single attack, place one random heat-up card face down on top of his behaviour deck. This is in addition to the ordinary heat-up at his heat-up point.
  >
  > **Pursuer (main-boss).** Several of the Pursuer's behaviour cards have dodge difficulty 0. *Ceaseless Pursuit:* on each of his turns the Pursuer draws and resolves two behaviour cards, one after the other; the second card's weak arcs apply to character attacks until his next turn. *Heat-up:* shuffle one random heat-up card into his behaviour deck as usual; from then on every attack value on his behaviour cards is increased by one.
  >
  > **Hungry Mimic and Voracious Mimic (mini-boss).** Mimics are fought as mini-boss encounters with these differences. Mimics have no arcs; their behaviour cards show no attack arcs or weak arcs and the weak-arc bonus is never gained. Mimics have no heat-up cards; when a mimic's health is reduced to or below its heat-up point, shuffle one random unused behaviour card into its behaviour deck. *Loot the Body:* when a mimic is slain, the characters receive two treasure cards of the current tier instead of the single card the chest held. See Mimics.
  >
  > ## Tomb of Giants Set
  >
  > **Black Knight (mini-boss) and Gravelord Nito (main-boss).** Use the data and behaviour cards from the Community Update Pack. No rules beyond the data card.
  >
  > ## Black Dragon Kalameet Expansion (mega-boss)
  >
  > **Components.** Kalameet's data card, health dial, thirteen behaviour cards (ten standard, two signature — *Mark of Calamity* and *Hellfire Blast* — and one heat-up card, *Hellfire Barrage*), eight strafe cards, two treasure cards, four *calamity* tokens, four Level 4 encounter cards and the mega-boss game board.
  >
  > **Setup.** Place the characters on the entry nodes beside the doorway, no more than three to a node, and give the aggro token to the character with the highest *threat*. Place Kalameet on the mega-boss spawn node with its front arc facing the centre of the game board. Build the behaviour deck: take four random standard behaviour cards, add the two signature cards, and shuffle these six together face down. Set the heat-up card aside. Shuffle the eight strafe cards and place them face down beside the behaviour deck.
  >
  > **Special ability — Calamity & Ruin.** Kalameet's behaviour deck always contains *Mark of Calamity* and *Hellfire Blast*. Attacks marked with the *calamity* icon place a *calamity* token on each character hit; the token's effect is given in Combat Basics › Conditions.
  >
  > **Heat-up.** When Kalameet's health is reduced to or below its heat-up point, shuffle *Hellfire Barrage* into the behaviour deck.
  >
  > **Strafe attacks.** The strafe icon is a magical attack that targets particular nodes instead of arcs. To resolve it: remove Kalameet from the game board, leaving any models that shared its node where they are; reveal the top strafe card; resolve the attack, at the value shown on the behaviour card, against every character on the nodes marked on the strafe card, each defending separately; discard the strafe card; then place Kalameet on the landing node shown on the strafe card, keeping its previous facing. Any character on the landing node is pushed to an adjacent node of that player's choice. If the strafe deck is empty when a strafe icon is resolved, turn its discard pile face down without shuffling to form the new strafe deck, then continue.
  >
  > ## Executioner's Chariot Expansion (mega-boss)
  >
  > **Components.** The Chariot's data card (two-sided), health dial, two models (the skeletal horse and the chariot), four track behaviour cards numbered 1 to 4, nine standard behaviour cards, three heat-up cards, a mega-boss setup card, two treasure cards, two Black Hollow Mages and four Falchion Skeletons with their data cards, four Level 4 encounter cards, six Level 1–3 encounter cards and the mega-boss game board.
  >
  > **The game board.** The centre of the Chariot's game board is not a node, and nodes are not adjacent across it. Treat the centre as a node containing a gravestone.
  >
  > **Setup.** Place the characters on the entry nodes beside the doorway, no more than three to a node, and give the aggro token to the character with the highest *threat*. Place both Chariot models together on the mega-boss spawn node and place the Black Hollow Mages and Falchion Skeletons on the enemy spawn nodes shown on the mega-boss setup card. Build two decks. The track deck: the four track behaviour cards in numerical order, card 1 on top, face down, not shuffled. The heat-up deck: four random standard behaviour cards and one random heat-up card, shuffled together face down and set aside.
  >
  > **Before heat-up — Death Race.** The Chariot's data card shows no starting health, block or resist on its front side. The Chariot cannot be attacked or damaged. After each character's turn, the Chariot and every other enemy on the board take a turn in descending *threat* order; the Chariot's turn is the top card of the track deck. To resolve a track behaviour card: move both Chariot models to the node shown, with the front arc facing away from the node they left; then make the card's physical attack against every character on the nodes marked on the card, including the node the Chariot left and the node it moved to, each defending separately; then push each character hit onto an adjacent node that is not marked on the card. Enemy models on marked nodes are pushed in the same way but suffer no damage. When the track deck is empty at the start of the Chariot's turn, turn its discard pile face down without shuffling to form the new track deck.
  >
  > **Raise Skeleton.** When a Black Hollow Mage resolves the Raise Skeleton icon, if fewer enemies with "Skeleton" in their name are on the board than there were at the start of the encounter, choose one defeated skeleton and place it, with no wound tokens, on the enemy spawn node closest to the Mage; if several spawn nodes are equally close, the players choose.
  >
  > **Heat-up — Chariot Crash.** When every Black Hollow Mage and Falchion Skeleton has been defeated, the Chariot heats up at once: remove the chariot model from the board, leaving the skeletal horse; flip the data card to its heat-up side, which shows the horse's starting health, block and resist; set the health dial to that starting health; and replace the track deck and its discard pile with the heat-up deck. The encounter continues as an ordinary boss encounter against the skeletal horse. The horse does not heat up again.
  >
  > **Special ability after heat-up — Crush.** When a character's block or resist roll prevents all of the damage of an attack from one of the horse's behaviour cards, that character suffers one damage.
  >
  > ## Mega-bosses Without Supplied Rules
  >
  > The following entries are BLOCKED — source booklet not supplied. Each is to be drafted in the structure used above (Components · Setup · Special ability · Heat-up · Unique icons) once its booklet is available. Until then the boss is played from its data card and the general boss rules.
  >
  > **The Four Kings (mega-boss, The Four Kings expansion).** BLOCKED. Known requirement: multiple boss models; the rule for two boss models in one encounter applies.
  >
  > **Gaping Dragon (mega-boss, Gaping Dragon expansion).** BLOCKED. Known requirement: *corrosion* condition (Combat Basics › Conditions).
  >
  > **Guardian Dragon (mega-boss, Guardian Dragon expansion).** BLOCKED.
  >
  > **Manus, Father of the Abyss (mega-boss, Manus expansion).** BLOCKED.
  >
  > **Old Iron King (mega-boss, Old Iron King expansion).** BLOCKED.
  >
  > **Vordt of the Boreal Valley (mega-boss, Vordt expansion).** BLOCKED. Known requirement: *frostbite* condition.
  >
  > **The Last Giant (mega-boss, The Last Giant expansion).** BLOCKED. Not listed in Game Components › Mega-bosses; see CMP-0008.
  >
  > **Crossbreed Priscilla (main-boss) and Heavy Knight (mini-boss), Painted World of Ariamis.** BLOCKED. Use the data and behaviour cards from the Community Update Pack; no further rules are available.

  Consequential edit to Setup › Setup After the main-boss step 11 (line 1195): replace "employing any special rules described in the mega-boss rule booklet" with "employing the rules for that mega-boss given in Boss Special Rules".
- Design rationale: Every drafted rule is taken from a supplied booklet and recast in the manuscript's turn structure (the Chariot's "enemy activation" becomes the enemy turn that follows each character's turn; the aggro token goes to the highest-threat character as the manuscript requires rather than to "one of the characters"). Two official steps are deliberately dropped because the manuscript's own design supersedes them: the per-gravestone reveal of behaviour cards at boss setup (the manuscript's Gravestones rule awards a scry on clearing instead) and the official Calamity removal-on-damage (the manuscript's Conditions chapter keeps Calamity to the end of the encounter). Artorias, Smelter Demon, Old Dragonslayer, Pursuer and the Mimics are drafted from explicit booklet or card text. Sif's cool-down and O&S's pairing live on data cards that were not supplied, so the entries state the boundary rather than invent. The Twin Gargoyles rule is an adaptation of the Core campaign footnote to the manuscript's boss-death sequence and is tagged.
- Mechanical impact: Kalameet and the Chariot become playable from this book alone. The Pursuer's double activation and the Chariot's unattackable first phase are significant difficulty rules now stated. The "two boss models" rule generalises the manuscript's existing boss-pushes-boss text.
- Follow-on changes required: Add strafe cards, track behaviour cards, mega-boss setup card, pillar tokens and Level 4 encounter cards to Game Components (CMP-0012). Add "The Last Giant" to Game Components › Mega-bosses or remove it from Big Game Hunting (CMP-0008). Obtain the missing booklets to unblock nine entries. Delete the empty heading at line 2215.
- Status: awaiting-approval

---

### [CMP-0006] Gameplay › Death & Hollowing — "Lost" state — Proposed Completion
- Current state: "Lost" is used but never defined: "keeping them from being *lost* to the *hollow*" (line 1890); "Resting at the *bonfire* also revives *lost* characters who have been removed from play due to dying while *hollow*" (line 1906); "The players lose the campaign if all characters are lost to the hollow without a *spark* to revive them" (line 2235). Death & Hollowing (line 1223) and Encounter Resolution (line 1305) say that when a *hollow* character dies the encounter is *failed* and the characters must spend a *spark* and rest. Setup After the main-boss step 11 (line 1195) says that in the mega-boss encounter "If a character dies they are permanently removed from play." Objective & Loss Conditions (line 1201) defines loss only as "all characters are dead and there are no remaining sparks".
- Proposed completion:

  New bullet group appended to Death & Hollowing (after line 1223):

  > - A *hollow* character who dies is *lost*.
  >
  >   - A *lost* character is removed from play: place the model on its side beside the *bonfire* tile, drop its *souls* on the encounter tile and discard its *ember* token as for any death.
  >
  >   - A *lost* character is not revived by *clearing* an encounter. A *lost* character is revived only when the characters rest at the *bonfire*; resting removes the *hollow* markers as usual.
  >
  >   - When a character becomes *lost*, the current encounter is *failed* at once and the characters must rest at the *bonfire* (see Encounter Resolution). If the *spark* dial shows zero, the players lose the game (see Objective & Loss Conditions).
  >
  >   - In a mega-boss encounter no rest follows: a character who dies or is *lost* in a mega-boss encounter is removed from play for the rest of the game.

  Replacement for the Encounter Resolution bullet at line 1305: "Encounters are *failed* if any *hollow* character dies; that character is *lost*."

  Replacement sentence for Returning to the Bonfire line 1906: "Resting at the *bonfire* also revives *lost* characters: characters who died while *hollow* and were removed from play."

  Addition to Objective & Loss Conditions (line 1201), as a second paragraph: "The players also lose if the characters are required to rest at the *bonfire* when the *spark* dial shows zero, and if every character is removed from play during a mega-boss encounter."
- Design rationale: The definition takes the three uses of "lost" as given and makes them one state. It keeps the manuscript's rule that a *hollow* death fails the encounter, so "lost" is a label for the interval between that death and the forced rest, and for permanent removal in the mega-boss fight. The zero-spark case is the one gap the body leaves (the forced rest cannot be paid); the ruling follows the manuscript's own loss condition rather than letting survivors continue without the lost character.
- Mechanical impact: None where sparks remain. With zero sparks, a hollow death now ends the game explicitly; previously the outcome was undefined.
- Follow-on changes required: Glossary entry "Lost" (CMP-0002) loses its [PROPOSED] tag on approval. F.A.Q. entries on forced rest and mega-boss death (CMP-0003) align. CMP-0020 carries the zero-spark rule into Encounter Recovery.
- Status: awaiting-approval

---

### [CMP-0007] Truncated and defective sentences (several chapters) — Proposed Completion
- Current state: Six sentences are cut short or carry a wrong word.
  1. Summons › Phantoms, line 1993: "Phantoms are removed from play if their health dial is reduced to or the encounter ends."
  2. Setup › Setup After the mini-boss step 11, line 1169: "Place all character models on the *bonfire* tile where they may now without spending a spark."
  3. Setup › Shop Setup › After Boss is Defeated step 2.3, line 1089: "Shuffle five random legendary treasure cards."
  4. Summons › Invader Encounter Setup step 2, line 2017: "deal a number equal to their starting decks deck size".
  5. Summons › Invader Encounter Setup step 4, line 2021: "If the central node is blocked by train".
  6. Mimics, line 2045: "they must reveal one an *ambush* card".
  Also: Summons › Phantoms step 7, line 1989, stray "i" after "behaviour deck."; steps 8 (line 1991) and Invader Combat step 4 (line 2031) say "each icon on the encounter card" where the behaviour card is meant; Soul Reward Table header, line 1412, "per characteri"; Mimics line 2047 "*cleared.*."; Game Components line 443 "1x HungryVoracious Mimic".
- Proposed completion (completed sentences, to be substituted in place):

  > 1. Phantoms are removed from play when their health dial is reduced to zero or when the encounter ends.
  >
  > 2. Place all character models on the *bonfire* tile, where they may now rest without spending a *spark*. They may visit the Firekeeper and Andre's Shop as usual after resting at the *bonfire*.
  >
  > 3. Shuffle five random legendary treasure cards into the tier two treasure deck. Return the remaining legendary treasure cards to the game box.
  >
  > 4. Shuffle the invader's behaviour cards and deal a number of them equal to the behaviour deck size on the invader's data card, face down, to create the invader behaviour deck. When the invader's health is reduced to or below its heat-up point, shuffle one unused invader behaviour card into the behaviour deck.
  >
  > 5. After the encounter card setup is complete, place the invader model on the encounter tile's central node. If the central node is blocked by terrain, place the invader model on a node adjacent to the central node, chosen by the players.
  >
  > 6. If the characters wish to open the chest, they must reveal the *ambush* card beside that encounter tile to determine whether the chest is a lurking mimic.
  >
  > Step 7 (line 1989): Each phantom turn, draw and resolve the top card of the phantom behaviour deck.
  >
  > Step 8 (line 1991) and Invader Combat step 4 (line 2031): After each icon on the behaviour card is resolved in left-to-right order, the phantom's [invader's] turn ends.
  >
  > Soul Reward Table header: "*Soul* reward per character".
  >
  > Mimics line 2047: "…and may mark the encounter *cleared*."
  >
  > Game Components line 443: "1x Hungry Mimic and 1x Voracious Mimic (Explorers)" — two data cards sharing two miniatures and one health dial.
- Design rationale: Each completion supplies the word the sentence's structure demands and that the surrounding rules confirm (zero health; rest; the tier two deck, as Legendary Treasure line 1025 already states; deck size; terrain; one ambush card). "Encounter card" in the phantom and invader turn steps is corrected to "behaviour card" because the phantom and invader rules draw from behaviour decks, not encounter cards.
- Mechanical impact: None; restores intended text.
- Follow-on changes required: None beyond substitution. Glossary (CMP-0002) and CMP-0018 reference the corrected phantom steps.
- Status: awaiting-approval

---

### [CMP-0008] Campaign Play › Setup and CAMPAIGNS list corrections — Proposed Completion
- Current state: Campaign Play › Setup (lines 2221–2225) says "the included campaigns are all three sections long" and "This rule-set includes three campaigns which require only the components available in the core set"; CAMPAIGNS (lines 2352–3034) lists thirteen campaigns of three to six sections, two of which need only the core set. "Facing the Abyss" appears twice (lines 2548 and 2764) with different preambles and a different Section Two (the first copy matches the Darkroot booklet; the second has Level 2 where Level 3 belongs). "A Hollow Pursuit" (line 2720) repeats Demon Hunting's requirements line ("core set and Asylum Demon expansion") although it is the Explorers campaign. Spellings: "Andor Londo" (2384, 2486, 2646; official: Anor Londo), "Earthern" (2736; the game location is Earthen Peak), "Jeramiah" (557) against "Jeremiah" (2492, 2528; the Phantoms booklet uses Jeremiah), "Do no place" (2456, 2504), "Old Dragon Slayer" (2734), "Bonfire Tiles" (2830), "Gaping Dragon(Mega Boss)" (2944), "Section Four- " and "Section Five Dark Champion" (2854, 2864). The Gauntlet's Section Three is titled "Invader Ruins" (2534) but the Phantoms booklet names it "Invader Spire". "Gargoyle (Mini-Boss)" is listed twice in three campaigns (2366–2368, 2468–2470, 2616–2618): the Core rulebook (p. 35) and the Phantoms booklet (p. 17) list the Gargoyle twice deliberately, with a footnote rule. "The Last Giant (Mega Boss)" (line 3018) is not in Game Components › Mega-bosses; The Last Giant is a published mega-boss expansion whose booklet was not supplied. The Undead Colosseum's Section Six (lines 2874–2880) omits the "Level 4 Encounter" that the Executioner's Chariot booklet (p. 19) lists before Vordt. "Ornstein & Smough (main-boss)" is listed as one boss (correct; see CMP-0005). Boss-rank labels vary ("Mini-Boss", "Mini Boss", "main-boss", "Main Boss", "Mega Boss").
- Proposed completion:

  Replacement for Campaign Play › Setup (lines 2219–2225):

  > ## Setup
  >
  > The setup for a campaign is the same as for the basic game except as stated in this chapter. A campaign is divided into sections. Each section lists, in order outward from the *bonfire* tile, the tiles to lay out: the *bonfire* tile, a number of encounter tiles with their encounter levels, and one or more bosses. Sections vary in length. The campaigns in this book are between three and six sections long, and some sections contain more than one boss or an encounter with special rules.
  >
  > When starting a campaign, the players choose one of the thirteen campaigns in CAMPAIGNS. Two of them, The First Journey and The Coiled Sword, require only the core set; each of the others states the expansions it requires.
  >
  > Lay out each section as Encounter Setup describes, using the number of encounter tiles the section lists and dealing encounter cards of the levels listed, in order from the *bonfire* tile. Where a section names an encounter, use that encounter card for that tile. Where a section lists a boss twice, see Boss Special Rules › Twin Gargoyles.
  >
  > A section is completed when its final boss is defeated or, for a section that ends in a named encounter instead of a boss, when that encounter is *cleared*. Completing a section restocks the shops and allows the characters to rest at the *bonfire* without spending a *spark*. A *spark* is gained only for a boss defeated. When a section is completed, perform Setup After the mini-boss for the next section, taking the next section's list in place of steps 4 and 6; for a section ending in a mega-boss, perform Setup After the main-boss instead. [PROPOSED — the section-completion sentence is inferred from Campaign Play › Sparks and › Blacksmith Andre's Shop]
  >
  > Players may expect to meet over several play sessions. One section is a convenient amount of play for a session.

  Merged entry replacing both "Facing the Abyss" entries (delete lines 2764–2808; replace lines 2548–2550 with):

  > ### Facing the Abyss - Dark Souls (Darkroot)
  >
  > This campaign requires the core set and the Darkroot expansion. Use encounters from the Darkroot expansion when setting up each section; players may add the Explorers and Characters expansions if available. Section One ends with the named Level 3 encounter Hydra Lake; the section is completed when that encounter is *cleared*.

  (Section lists as at lines 2552–2592: Section Two is Bonfire Tile, Level 1, Level 2, Level 3, Level 3, Great Grey Wolf Sif (main-boss).)

  Replacement for A Hollow Pursuit requirements (line 2720): "This campaign requires the core set and the Explorers expansion; players may add the Characters expansion if available." Replacement for line 2748: "Gallery of the Hidden Warrior — do not place an *ambush* card beside this tile; its chest is a Voracious Mimic. The section is completed when the mimic is slain."

  Footnote to attach to each doubled Gargoyle line (The First Journey, Ambush Lies Ahead, Demon Hunting): "* The two Gargoyle encounters are fought back-to-back as one boss encounter; see Boss Special Rules › Twin Gargoyles."

  The Undead Colosseum, Section Six (lines 2874–2880), corrected list: Bonfire Tile · Level 3 Encounter - Desolate Cemetery · Level 4 Encounter · Vordt of the Boreal Valley (mega-boss). Section Two, line 2830: "Bonfire Tile".

  Big Game Hunting, line 3018: retain "The Last Giant (mega-boss)" and add "The Last Giant (The Last Giant)" to Game Components › Mega-bosses (after line 535). Boss Special Rules entry for The Last Giant: BLOCKED — source booklet not supplied (CMP-0005).

  Spelling and label corrections, applied throughout CAMPAIGNS and Game Components: Anor Londo; Lower Earthen Peak; Xanthous King Jeremiah (line 557 and all campaign lines); "Do not place invader tokens"; Old Dragonslayer; Invader Spire (The Gauntlet, Section Three); "Section Four - Haunting Warrior"; "Section Five - Dark Champion"; "Gaping Dragon (mega-boss)"; boss-rank labels normalised to "(mini-boss)", "(main-boss)", "(mega-boss)" in every list; "Great Grey Wolf Sif" used in every list.
- Design rationale: The Setup paragraph is rewritten to describe what the CAMPAIGNS chapter actually contains and to state the one procedure the chapter never gives: how a section is laid out and ended. The first Facing the Abyss copy is kept because its section lists match the Darkroot booklet; the two preambles are merged so neither requirement nor encounter-source statement is lost. The doubled Gargoyle is confirmed deliberate by the Core rulebook and is kept, with the back-to-back rule made explicit in CMP-0005. The Last Giant is a published mega-boss and is kept in the campaign; adding it to the component list is the smaller change. Official spellings are taken from the Core and Phantoms booklets; "Earthen" follows the game location, since the Explorers booklet itself prints the typo.
- Mechanical impact: Section completion now explicitly grants a free rest and restock but no spark when a section ends in a named encounter (Facing the Abyss Section One, Playing with Fire Section One, A Hollow Pursuit Section Two). The Undead Colosseum gains its missing Level 4 encounter before Vordt.
- Follow-on changes required: Delete the empty headings at lines 2400 and 3036. Regenerate TOC (seven campaigns are missing from it). CMP-0022 adds The Undead Colosseum's special rules; CMP-0021 adds Kalameet's campaign section. Demon Hunting Section One deliberately has no Bonfire Tile (line 2608 explains); confirm with the author.
- Status: awaiting-approval

---

### [CMP-0009] PLAYER VS PLAYER (chapter) — Proposed Completion
- Current state: Lines 3038–3094: twenty-seven bullets and a six-line dodge-difficulty list. No prose. Gaps: how a character attacks a character (which defence rolls, which dodge difficulty, how damage is placed); parry and riposte; pushes; conditions; what "outermost available node" means; what a trap token does in PvP; simultaneous death; how the "+1 attack damage" carry-over is tracked; ties in threat; what the champion is; "intimate victor" (line 1201) for "ultimate". The bullet "First turn token is given to the character with the highest threat value" (line 3056) duplicates the turn-order bullet (see CMP-0011).
- Proposed completion (full chapter; the manuscript's bullets are the skeleton):

  > # PLAYER VS PLAYER
  >
  > Player versus player (PvP) is an optional contest fought between the characters after each boss is defeated. The players must agree during setup whether PvP encounters will be played. If they are, a PvP encounter is fought after every mini-boss, main-boss and mega-boss encounter that is won.
  >
  > ## Setup
  >
  > 1. Remove every enemy model, wound token and trap token from the boss encounter tile(s). Terrain tokens remain.
  > 2. Restore every surviving character as if they had rested at the *bonfire*: remove all damage cubes, stamina cubes, *hollow* markers and condition tokens, and flip *luck*, *estus flask* and *heroic action* tokens to the ready side. *Ember* tokens are kept.
  > 3. Characters who died in the boss encounter take no part in the PvP encounter. Summons and invaders take no part.
  > 4. Place each character on a different corner node of the boss encounter tile(s). The character with the highest *threat* chooses first, then the next highest, and so on.
  > 5. The *aggro* token is not used.
  > 6. Set the trap tokens face down beside the tile, shuffled.
  >
  > ## Turn Order
  >
  > Characters take turns one at a time in descending *threat* order. If two characters share a *threat* value, the players decide their order before the first turn; if they cannot agree, decide at random. The order is kept for the whole PvP encounter. After the last character has taken a turn, the first takes the next, and so on until one character remains.
  >
  > ## Character Turns
  >
  > A character's turn is unchanged from the basic rules: recover one stamina; take any minor actions (*Walk*, *Run*, *Equip*, *Heroic Action*); take one major action (*Attack*, *Rest*, *Drink Estus* or *Ember*). A character may not leave the tile(s). The limit of one spell attack option per turn applies.
  >
  > After a character's major action, that character's player draws one trap token and places it face down on an outermost available node. The outermost available nodes are the nodes along the tile's edges that contain no model, no terrain token and no trap token; when every edge node is occupied, the next ring of nodes inward is the outermost. If no trap token remains, none is placed.
  >
  > ## Attacking a Character
  >
  > A character attacks another character exactly as they would attack an enemy: choose an attack option, pay its stamina cost, nominate a character within the attack's range as the target, roll the dice, apply modifiers, and use any rerolls (two-handed, *luck*, equipment). The result is the attack value. Attack options with the *shaft* icon may not target a character on the attacker's node. An *AoE* attack option targets every other character on the chosen node; roll once and resolve each defence separately. A *scaled* weapon's +1 and any PvP victory bonus (below) apply.
  >
  > The target then defends as against an enemy attack, choosing one of the following before any dice are rolled.
  >
  > - *Block* or *resist*: roll the block dice (against a physical attack option) or resist dice (against a magical attack option) of every equipped card; the defence total is the sum of the two highest dice. The defender suffers damage equal to the attack value minus the defence total, to a minimum of zero. The defender is hit.
  > - *Dodge*: pay one stamina (or three stamina for one additional die) and roll dodge dice against the dodge difficulty given by the table below. On a success the attack misses entirely and the defender must move to an adjacent node. On a failure the defender is hit and rolls only their armour card's block or resist dice.
  > - *Parry*: pay one stamina. A *parry* is allowed only if the defender has a shield in the left weapon slot, shares a node with the attacker, and the attack option has no push icon and is not *AoE*. Roll dodge dice against the table below. On a success the attack misses, the attacker receives a *stagger* token and the defender may at once make one *riposte* with any attack option of the weapon in their right weapon slot, paying its stamina cost; the attacker defends against the *riposte* by blocking, resisting or dodging but may not *parry* it. On a failure the defender suffers the full attack value, with no defence roll, and receives a *stagger* token.
  > - Do nothing: the defender suffers the full attack value and is hit.
  >
  > Damage suffered is placed as damage cubes on the defender's endurance bar. An *embered* defender reduces damage of three or more from a single attack by one, as usual.
  >
  > **Dodge difficulty in PvP.** The dodge difficulty of a character's attack option is set by its stamina cost:
  >
  > | Stamina cost of the attack option | Dodge difficulty |
  > |---|---|
  > | 0 | 4 |
  > | 1 | 3 |
  > | 2 | 2 |
  > | 3 | 1 |
  > | 4 | 1 |
  > | 5 or more | 0 |
  >
  > A *riposte* uses the dodge difficulty of the attack option chosen for it.
  >
  > ## Pushes and Conditions
  >
  > An attack option with the push icon pushes each character it hits one node directly away from the attacker, as Pushing describes; a character is not pushed into a node containing a gravestone or chest, and a barrel in the destination node is destroyed. Condition icons on attack options place the matching condition token on each character hit. Conditions on characters are resolved as Combat Basics › Conditions describes: *bleed* deals three damage when a second token would be placed; *poison* deals damage at the end of the character's turn; *frostbite* stops stamina recovery; *stagger* subtracts one from every roll total.
  >
  > ## Traps
  >
  > When a character moves onto, dodges onto, shifts onto or is pushed onto a node containing a face-down trap token, flip the token. If it shows a trap, the character must attempt to *dodge* against the trap's printed dodge difficulty, paying one stamina as usual; a character who fails, or who cannot pay, dies. A trap token showing nothing has no effect. A flipped trap token stays on its node and does not trigger again.
  >
  > ## Death
  >
  > A character whose endurance bar is full of damage cubes, or who fails to dodge a trap, dies and is removed from the tile. Death in PvP has no cost: *souls* are not dropped, the *ember* token is not removed, and no *hollow* markers are placed. The character is restored with the others at the end of the PvP encounter.
  >
  > ## Victory
  >
  > The last character on the tile wins the PvP encounter. If the last two or more characters die at the same time, no character wins.
  >
  > The winner of a PvP encounter fought after a mini-boss or a non-final main-boss gains a PvP victory bonus: place one wound token beside the winner's dashboard. In every later PvP encounter the character adds one to the attack value of each attack option per wound token beside their dashboard. The bonus has no effect outside PvP and is cumulative.
  >
  > The winner of the PvP encounter fought after the final boss is the champion of the game. The players still share the victory over the final boss.
  >
  > ## After the PvP Encounter
  >
  > Return all trap tokens to the supply. Place every character, including those who died, on the *bonfire* tile and rest there without spending a *spark*, as after a boss. Remove the wound tokens used to mark PvP victory bonuses only when the game ends.

  Consequential edit to Gameplay › Objective & Loss Conditions (line 1201): "…to determine a single ultimate victor." Delete the bullet "*First* *turn* token is given to the character with the highest threat value" (line 3056; see CMP-0011).
- Design rationale: Every mechanic is the manuscript's own, applied symmetrically: the defender rolls exactly as against an enemy (two highest dice; armour-only after a failed dodge; parry conditions and stagger results from Enemy Turn › Parry & Riposte), and the attacker's fixed enemy-style dodge difficulty is replaced by the manuscript's stamina-cost table. The outermost-node ring rule gives the trap bullet a definite meaning that shrinks the arena and ends stalemates. Simultaneous death yields no winner so the carry-over bonus cannot be awarded twice. The bonus is tracked with a wound token because wound tokens are otherwise unused on characters and no new component is needed. "A riposte may not be parried" prevents an endless chain of parries between two shield-bearers.
- Mechanical impact: PvP becomes fully playable. The only numeric additions are the trap death rule (already in the bullets) and the cumulative +1 bonus tracking. Terrain is kept on the tile (the bullets remove only enemies and traps), which keeps gravestones and chests as cover.
- Follow-on changes required: Delete the empty heading at line 3096. Add "Resting at the *bonfire*" after PvP to Returning to the Bonfire line 1908 (already states it). Glossary entries Dodge difficulty and Riposte (CMP-0002) reference this chapter. If the editor prefers a dedicated marker to the wound token, add "4x PvP victory tokens" to Game Components.
- Status: awaiting-approval

---

### [CMP-0010] Gameplay › Souls / Campaign Play › Encounter Soul Rewards — Reduced soul reward — Proposed Completion
- Current state: Souls (line 1391): "Upon successfully *clearing* an encounter that has been previously *cleared*, reward the reduced *soul* reward to each character." Encounter Resolution (line 1327): "Characters gain *soul* rewards but not treasure." Campaign Play (line 2245): "repeated for *souls* rewards but not treasure rewards, just as in the basic game." Neither Soul Reward Table (lines 1401–1439) nor the Campaign Soul Reward Table (lines 2247–2285) has a reduced column; no value is ever given.
- Proposed completion:

  Replacement for line 1391: "Upon successfully *clearing* an encounter that has been previously *cleared*, reward the reduced *soul* reward to each character. The reduced reward is half the full reward, rounded down."

  Replacement for the Soul Reward Table:

  > ### Soul Reward Table
  >
  > | Encounter | Full reward per character | Reduced reward per character (already *cleared*) |
  > |---|---|---|
  > | Level 1 Encounter and Standard Invaders | 3 | 1 |
  > | Level 2 Encounter and Advanced Invaders | 4 | 2 |
  > | Level 3 Encounter | 5 | 2 |
  > | Level 4 Encounter and Bosses | 6 | 3 |
  >
  > Invaders and bosses are never *cleared* twice; their reduced reward is never used.

  Replacement for the Campaign Soul Reward Table:

  > ### Campaign Soul Reward Table
  >
  > | Encounter | Full reward per character | Reduced reward per character (already *cleared*) |
  > |---|---|---|
  > | Level 1 Encounter and Standard Invaders | 2 | 1 |
  > | Level 2 Encounter and Advanced Invaders | 3 | 1 |
  > | Level 3 Encounter | 4 | 2 |
  > | Level 4 Encounter and Bosses | 5 | 2 |

  Replacement for Encounter Resolution line 1327: "Characters gain the reduced *soul* reward but no treasure."
- Design rationale: Half rounded down is chosen over "one fewer" because the manuscript's stated aim is to remove grinding: at one fewer, repeating a Level 3 encounter would pay 4 souls per character, barely less than clearing it. Half makes repeats worth taking only when a character must retrieve dropped souls or wants a safe route to the boss. Rounding down keeps every value a whole number and never reduces a reward to zero. The alternative (one fewer: 2/3/4/5 and 1/2/3/4) is recorded here for the editor's decision.
- Mechanical impact: Repeat clears pay 1–3 souls (basic) or 1–2 souls (campaign) per character. Dropped-soul recovery is unaffected.
- Follow-on changes required: F.A.Q. answer on reduced rewards (CMP-0003) matches. Line 2243 ("reduced by one compared to the basic game") stands and refers to the full reward only; add "The reduced reward is half the campaign full reward, rounded down" after it.
- Status: awaiting-approval

---

### [CMP-0011] Gameplay › Encounter Start step 9 and Player vs Player — "First player token" — Proposed Completion
- Current state: Encounter Start step 9 (line 1277): "Place the *first player* token on the character with the highest threat value." Player vs Player (line 3056): "*First* *turn* token is given to the character with the highest threat value." No such token is listed in Game Components › Tokens & Terrain Elements (lines 679–723). Turn order is fixed by *threat* in both places (lines 1289, 3058), so the token has no function.
- Proposed completion: Remove the token. Delete Encounter Start step 9 and the PvP bullet at line 3056, and replace Encounter Start step 8 (line 1275) with:

  > 8. Place the *aggro* token on the character with the highest *threat* value. That character takes the first character turn of the encounter; ties in *threat* are settled by the players before the first turn and the order is kept for the encounter.

  Replacement for PvP turn-order bullet (line 3058), as drafted in CMP-0009: "Characters take turns one at a time in descending *threat* order. If two characters share a *threat* value, the players decide their order before the first turn; if they cannot agree, decide at random."
- Design rationale: Removal is recommended over definition. Threat order already fixes the first character, so a first-player token would duplicate information the dashboards carry; the Core rulebook's First Activation token existed only because its turn order went clockwise, which this edition has abandoned. Defining the token would also require adding a component. The tie rule supplies the one thing the token's position would have recorded.
- Mechanical impact: None.
- Follow-on changes required: Remove "first player" from the italicised-term inventory; no Glossary entry. Renumber Encounter Start.
- Status: awaiting-approval

---

### [CMP-0012] Game Components and owning chapters — Undefined components (event cards, ambush cards, mega-boss items, Level 4 tiles, pillar tokens, strafe and track cards) — Proposed Completion [PROPOSED-SYSTEMIC for event cards]
- Current state: Game Components lists "Event cards" (lines 659–667: 10 per level and 5 Special Trap cards) and "Level 4 encounter cards" (line 653) but no ambush cards, pillar tokens, mega-boss items, strafe cards, track behaviour cards, mega-boss setup card, phantom or invader components, or mega-boss game boards. Event cards are used at Setup (lines 1133, 1161), Encounter Start (line 1269), Gravestones (line 939) and Setup After the main-boss (line 1181, "No event card is used"), but no rule says what an event card does; the Tomb of Giants set's event cards (immediate/consumable/rendezvous, drawn as rewards) are a different component and its rules do not match the manuscript's levelled, tile-dealt deck. "Ambush card" is used (lines 1137, 1469–1473, 2045) and defined only by use. "Mega-boss Items" (line 1183) are never defined. "Level 4 encounter tile associated with the chosen mega-boss" (line 1179) is the double-sided mega-boss game board. "Pillar token" (line 2205) and "pillar nodes" are used only in Boss Special Rules.
- Proposed completion:

  (a) Additions to Game Components (insert after line 667 and within Tokens & Terrain Elements as marked):

  > ### Phantom cards and tokens (Phantoms)
  >
  > - 10x Summon data cards (5 standard, 5 advanced), 40x Summon behaviour cards, 1x Summon health dial
  > - 12x Invader data cards (6 standard, 6 advanced), 64x Invader behaviour cards, 12x Invader treasure cards, 1x Invader health dial
  > - 6x Standard invader tokens, 6x Advanced invader tokens, 3x Blank invader tokens
  >
  > ### Mimic cards (Explorers)
  >
  > - 2x Mimic data cards (Hungry, Voracious), 14x Mimic behaviour cards, 1x Mimic health dial, 5x Ambush cards
  >
  > ### Mega-boss components (one set per mega-boss expansion)
  >
  > - 1x Mega-boss game board (double-sided: Level 4 encounter side and mega-boss side)
  > - 4x Level 4 encounter cards
  > - 1x Mega-boss data card, 1x Health dial, behaviour cards as listed on the data card, 2x Mega-boss treasure cards
  > - Black Dragon Kalameet only: 8x Strafe cards, 4x *Calamity* tokens
  > - Executioner's Chariot only: 4x Track behaviour cards, 1x Mega-boss setup card
  > - Asylum Demon only: 4x Pillar tokens
  >
  > (Tokens & Terrain Elements, after line 713) - 4x Pillar tokens (Asylum Demon)

  (b) New sub-section in Game Components › Cards, after Event cards (line 667):

  > ### Ambush cards
  >
  > Five cards from the Explorers expansion, each showing Treasure or Mimic on its face. One is dealt face down beside each encounter tile when mimics are in play and is revealed only when the characters choose to open that tile's chest. See Mimics.

  (c) Rule paragraph for event cards, as a new sub-section Gameplay › Encounters › Event Cards (insert after Encounter Start, line 1277) [PROPOSED-SYSTEMIC]:

  > ### Event Cards
  >
  > Each encounter tile carries one face-down event card of the same level as its encounter card, dealt at setup. When the characters enter the tile, reveal the event card after the encounter card and before enemies and terrain are placed. The event card's text modifies that encounter and applies until the encounter ends, unless the card states otherwise. An event card that cannot be applied to its encounter (for example, one that refers to a terrain type the encounter does not place) has no effect. Event cards stay on their tiles, face up, after the encounter; when the characters rest at the *bonfire*, event cards are turned face down with their encounter cards and apply again when the encounter is next fought. Special Trap cards are event cards that replace the standard trap tokens of a trapped encounter with the trap layout printed on the card; if the encounter is not trapped, the Special Trap card has no effect. Level 4 encounters and boss encounters use no event card.

  (d) Definition of mega-boss items, replacing Setup After the main-boss step 5 (line 1183):

  > 5. Shuffle the mega-boss's treasure cards (its *mega-boss items*) and deal one face down to the Level 4 encounter tile. This card is the Level 4 encounter's treasure reward and is awarded, when the encounter is *cleared*, as a chest treasure is: the players decide which character receives it. No tier two treasure cards are dealt to the Level 4 tile. [PROPOSED]

  (e) Definition of the Level 4 tile, replacing Setup After the main-boss step 3 (line 1179):

  > 3. Place the mega-boss game board supplied with the chosen mega-boss adjacent to the *bonfire* tile, with its Level 4 encounter side (enemy spawn and terrain nodes) face up and a doorway aligned with the *bonfire* tile. Place the fog gate on that doorway. The game board's other side shows the mega-boss spawn node and is used for the mega-boss encounter.

  (f) Pillar tokens: the definition in Boss Special Rules › Pillar Smasher (line 2205) stands; add to Tiles & Nodes › Terrain, after Traps (line 981): "**Pillars.** Pillar tokens are placed only on the pillar nodes of the Asylum Demon mega-boss game board. Pillars block movement, dodging and pushes until destroyed; see Boss Special Rules."
- Design rationale: Items (a), (b), (e) and (f) are inventories and descriptions drawn from the supplied booklets, matched to the manuscript's existing lists. Item (d) resolves "mega-boss Items" as the mega-boss's own treasure cards, the only cards an expansion supplies that fit the phrase, and gives the Level 4 tile a reward in place of the per-character tier two cards the generic setup would otherwise deal. Item (c) is a new subsystem: the manuscript dealt, revealed and scried event cards without ever stating their effect, and the only published event cards (Tomb of Giants) work differently; the paragraph is the minimum needed for the component to function (when revealed, duration, reset, what a Special Trap card is, where no event is used) and does not design any card.
- Mechanical impact: Event cards gain a definite timing and reset. Level 4 encounters award one mega-boss treasure card instead of one tier two card per character (a reduction of up to three cards). Component counts allow the Game Components chapter to be checked against the boxes.
- Follow-on changes required: Decision needed on (c): confirm that the author's event deck exists (print-and-play in the Community Update Pack?) and supply card texts, or delete every event-card reference (lines 659–667, 939, 1133, 1161, 1181, 1269). Confirm (d) with the author. Glossary entries Event card and Ambush card (CMP-0002). Campaign Play: state whether campaign Level 4 encounters also receive a mega-boss item.
- Status: awaiting-approval

---

### [CMP-0013] INTRODUCTION / SECOND EDITION NOTES — Foreword options (OQ-01) and colophon credits — Proposed Completion
- Current state: SECOND EDITION NOTES (lines 371–381) is design-process commentary in the first person, with complaints about the publisher ("SFG had lied"), requests for comment, and a note about diagrams and copyright. The Introduction (lines 361–369) is four short paragraphs. The front matter byline (lines 1–3) reads "By PittedPanda / Based on related works by Steam Forged Games (SFG), Konami, Santuric, Wilhelm, Astray, Manuel, Chud, Winston, Jyace, Absolute Disgrace, Zed, Gorus, and the rest of the DStBG Community." Line 381 (the glossary promise) is the one sentence in the chapter that belongs in the book.
- Proposed completion:

  **Option A — Foreword (≤200 words), replacing SECOND EDITION NOTES in full:**

  > # FOREWORD
  >
  > Dark Souls: The Board Game was published in 2017 and grew, expansion by expansion, into a large and uneven body of rules. This Second Edition gathers those rules into one book, revises the mechanics that long play exposed as weak, and states every rule once, in one place, so that a table needs no other text.
  >
  > The core of the game is unchanged: a party of one to four characters explores a string of encounters, learns the patterns of its enemies, returns to the bonfire to rest and grow stronger, and at last faces a boss. What has changed is the pace and the balance. Enemies act first and in threat order. Blocking, resisting, dodging and parrying each cost something and each reward a different kind of equipment. The shop restocks only when a boss falls. Death drops souls, and the hollow fight with less endurance until they rest or find an ember.
  >
  > These rules were shaped by the community that kept the game alive. Every mechanic in this book has been played, argued over and played again. Where a term is set in italics, its definition is in the Glossary.
  >
  > Prepare to die.

  (171 words.)

  **Option B — Expanded Introduction (≤120 words), replacing INTRODUCTION in full, with SECOND EDITION NOTES cut entirely:**

  > # INTRODUCTION
  >
  > Dark Souls: The Board Game Second Edition is a cooperative dungeon crawl for one to four players. Each player controls one character. The characters explore a chain of encounters, defeat a mini-boss and then a main-boss, and, if the players choose, a mega-boss after that.
  >
  > To succeed the characters must learn their enemies' behaviours, raise their stats, seek out powerful weapons and work together through increasingly dangerous encounters. When a character dies they rise again hollow, weaker until they rest at the bonfire or consume an ember. The bonfire's sparks are few, and every rest spends one.
  >
  > This edition collects the rules of the original game and its expansions into one revised, self-contained book. Terms set in italics are defined in the Glossary.
  >
  > Nameless accursed undead, seek strength, and prepare to die.

  (119 words.)

  **Colophon credits block (two lines), replacing the byline at lines 1–3:**

  > Second Edition rules by PittedPanda, with the Dark Souls: The Board Game community: Santuric, Wilhelm, Astray, Manuel, Chud, Winston, Jyace, Absolute Disgrace, Zed and Gorus.
  > Based on Dark Souls: The Board Game by Steamforged Games Ltd. Dark Souls is a trademark of Bandai Namco Entertainment Inc. and FromSoftware, Inc. This is an unofficial, non-commercial fan work.

- Design rationale: Option A keeps a foreword's function (why the edition exists, what changed) without first person, process notes or grievance; its description of the changes is drawn from the manuscript's own chapters. Option B assumes the Notes chapter is cut and folds the one necessary sentence (the glossary promise) into the Introduction, preserving the original closing line. The credits block names the same contributors, drops "Konami" (the Dark Souls rights-holders are Bandai Namco and FromSoftware, as every supplied booklet states) and adds the fan-work disclaimer the original front matter lacks.
- Mechanical impact: None.
- Follow-on changes required: Editor decision on OQ-01 (A or B). Whichever is chosen, delete lines 371–381. Confirm the contributor list and the handle "PittedPanda" with the author. Regenerate TOC.
- Status: awaiting-approval

---
