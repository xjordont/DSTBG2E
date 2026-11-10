# Drafting pack — chapter 21 (glossary) — manuscript chapter "GLOSSARY"

Source text: `work/phase2a/source/21_glossary.md` (manuscript.md lines —–—).

## Tracker rows (section · status · notes)

- **(chapter)** · MISSING — promised · TOC lists GLOSSARY (p.74) and Introduction promises italic-term definitions; no glossary exists in body.

## Audit findings mapped to this chapter (0)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

## Completion entries that apply (1) — approved at Gate 1

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
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

