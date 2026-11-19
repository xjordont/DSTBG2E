# Rewrite brief — the whole manuscript, to the settled rules (2026-11-18)

You are rewriting part of a fan-made second-edition rulebook for a dungeon-crawl board game. The author wrote 20,500 terse words. An earlier editorial pass (called "v2" below) blew that up to 77,500 words of lawbook prose and changed rules along the way. The rules have since been settled one by one with the author. Your job: write your chapters afresh, **in the author's own terse voice, to the settled rules in section 3 of this brief, inside your word budget.**

Read sections 1 to 4 fully before you write a word. Where this brief and any other file disagree, this brief wins.

## 1. Inputs

For each chapter you are given three things:

- **The author's original chapter**, `work/phase2a/source/NN_*.md`. This is the voice, the structure and the length ceiling. Start from it. Keep the author's sentences where they are right; tidy grammar and typos; convert its HTML tables to Markdown tables.
- **The v2 chapter**, `10_manuscript_chapter_NN_*.md` (you overwrite this file). Use it only as a quarry: for holes the author left that it filled in a sentence, for content the author asked to have added (boss entries, extra campaigns, appendix data), for corrected facts (component names, counts), and for `{{icon:…}}` tokens. Do not carry over its prose, its procedures, its examples or its cross-reference brackets.
- **This brief.** Section 3 is the rules. Where the author's chapter says something else, section 3 replaces it.

Do not read or edit files outside your assignment, except to look up a fact. Do not run git commands.

## 2. Voice and form

**Length is a hard requirement.** Each chapter has a word budget (section 4). Stay within 10% of it. If you are over, cut; do not ask.

- **The author's register:** short declarative sentences; bullets for lists of rules; numbered lists for setup steps and sequences; small tables for numbers. No flavour introduction unless the author wrote one, and then at most two sentences of it.
- **State a rule once.** Your chapter owns the rules listed for it in section 4. A rule another chapter owns is not restated, summarised or "recalled". Refer to it only where the reader must turn the page to act, as "(see §7.5)". Aim for fewer than one cross-reference per 100 words.
- **No sentences that answer questions nobody asks** ("even if", "whether or not", "this does not", "for the avoidance of doubt"). Rare corner cases go back to the table.
- **Examples:** only those section 4 names for your chapter. Each is one short paragraph beginning `*Example.*`.
- **No coined terms.** Do not use: Move (as a defined term), valid node, relevant stat, next complete turn, victory bonus, ultimate victor, defence total, attack sequence, scry. Say the thing in plain words.
- **No optional rules.** There is no "the party may decide during setup whether X is in play". Content from an expansion is in play whenever the party owns that expansion, and is introduced as "With the Explorers expansion, …" or under a heading that names the set.
- **Finished rulebook.** No editorial notes, tags in square brackets, design rationale, history, "this edition", or mention of other rulebooks, publishers, editions, page numbers, websites or the simulator.
- **British English** (armour, behaviour, defence, centre, colour, grey, randomise). Names printed on cards keep their printed spelling (Armorer Dennis, Marvelous Chester, Plow Scarecrow).
- **Never the words** should, might, could, probably, perhaps, maybe, likely, reasonably (a script rejects them). Use must, may, cannot, or the plain imperative. **No second person** (you, your) outside an `*Example.*` paragraph.
- **Numbers:** words for zero to nine in prose, digits from 10; digits always in tables, with signs (+1), beside dice and in labels (Level 1, 25 STR). Component lists: "2x Hollow Soldier".
- **Italics** mark game terms and nothing else. Italicise a term from the list below at its first use in each numbered section; plain afterwards. Do not italicise anything else (except `*Example.*`). No bold in running text except the lead-in of a definition or list item (**Bleed.**).

  Italic terms (these are the glossary's headwords): aggro, ambush card, area-of-effect, arc, back-up slot, barrel, basic node, behaviour card, bleed, block, bonfire, bonfire ascetic, boss treasure, calamity, chest, class treasure, cleared, common treasure, condition, corrosion, crystal lizard, data card, dodge, dodge difficulty, drink estus, ember, embered, encounter card, endurance bar, entry node, equipped, estus flask, event card, failed, fog gate, frostbite, gravestone, heat-up, heroic action, hollow, invader, inventory, leap, legendary treasure, lost, luck, main-boss, major action, mega-boss, mimic, mini-boss, minor action, node, node model limit, parry, phantom, poison, push, push-attack, push-move, range, repeat, reset, resist, rest, riposte, run, section, shaft, shift, shop, souls, spark, spawn node, spell, stagger, stamina, starting equipment, stat scaling, summon, terrain node, threat, tier one, tier two, Titanite, transposed treasure, transposition, trap, two-handed, upgrade, walk, weak arc.
- **Fixed names:** endurance bar; damage cube (red) and stamina cube (black) on a character; wound token on an enemy; hollow cube; stat cube; soul token; spark dial; health dial; aggro token; condition token; trap token; invader token; data card; behaviour card and behaviour deck; encounter card; treasure card; attack option (a line on a weapon card); turn (never "activation"); model (never "miniature"); mini-boss, main-boss, mega-boss; the party (the characters together); player versus player (PvP); setup (noun), set up (verb); reroll; tier one and tier two (treasure decks and shops); stat tier one to four; Level 1 to Level 4 encounters.
- **Headings:** `# N. Chapter Title`, `## N.M Section Title` exactly as in section 4, `### Sub-Section Title` unnumbered and only where the author had one or section 4 names one. No "&" in headings.
- **Cross-references:** "(see §N.M)", targets from section 4 only. Appendices: "(see Appendix A)".
- **Markdown:** GitHub tables, `1.` numbered lists, `-` bullets. No blockquotes, no HTML, no footnotes, no em dashes in rules text.
- **Icons:** where the v2 chapter puts an `{{icon:ast-NNNN-slug}}` token beside the first mention of a printed icon, keep one such token beside your first mention of that icon. Copy tokens exactly; never invent one.

## 3. The settled rules

Everything here is decided. Where the author's chapter differs, write this. Where this brief is silent, the author's chapter stands. Where both are silent and a player would be stuck in their first game, add one sentence using your judgement as a rulebook editor, and list it in your report.

### 3.1 Party size

| Characters | Sparks | Enemy health | Enemy attack damage |
|---|---|---|---|
| 1 | 4 | as printed | as printed |
| 2 | 3 | +2 | +1 |
| 3 | 2 | +4 | +2 |
| 4 | 1 | +6 | +2 |

(Table as ruled 2026-11-19, section 25 of 41_rules_workshop.md: bosses, mimics, invaders, summons and crystal lizards are never scaled.)

- This table replaces the author's whole scaling table. Enemy movement is never scaled and no attack is repeated because of party size.
- Bosses, mimics, invaders, summons and crystal lizards are never scaled.
- Sparks at the start: five less the number of characters. One spark is added each time a boss is defeated. Sparks are gained no other way.
- A character adventuring alone starts with six souls.

### 3.2 The round

- Ordinary encounter: every enemy takes a turn in descending threat; then every character, in any order the party chooses each round. There is no first player token.
- Boss encounter: the boss takes a turn before each character's turn. An invader and a summon take a turn after each character's turn.
- Aggro: at the start of an encounter the token goes to the character with the highest threat. After that it passes to the last character to deal damage. If no one deals damage it stays.

### 3.3 A character's turn

- Recover one stamina.
- Minor actions, any of them, in any order: *walk* one node free; *run* one further node for each stamina spent; equip (swap cards among the back-up, weapon and armour slots; the inventory is closed during an encounter); heroic action.
- One major action: attack (one attack option from the left weapon slot, the right, or both); *rest* (remove all stamina; only if the character did not run this turn); drink estus (remove all damage cubes, flip the token; it clears no stamina); ember (discard an ember card from the back-up slot).
- At most one spell attack a turn. A spell is never scaled, never two-handed and never used for a riposte.
- Stat scaling: a weapon's attacks gain +1 to the attack value while the character's stat for that weapon's highest stat requirement is ten or more above the requirement. Where two requirements tie for highest, either stat qualifies.
- Two-handed attacks (section 27 of 41_rules_workshop.md): an attack with a two-handed weapon may reroll any single die after the roll, and a one-handed weapon equipped with nothing in the other weapon slot gains the same reroll. Nothing else: no extra die, and a two-handed weapon leaves the other weapon slot empty unless a card's text says otherwise.
- Luck: flip the token to reroll any or all dice of one attack or defence roll, chosen at once; the new results stand.
- Heroic actions are printed on the dashboards and are not listed in the book. A heroic action is a minor action unless its text gives another moment.

### 3.4 Defence

- **Block or resist:** roll every block die (physical) or resist die (magical) on the character's equipped cards, keep the two highest results, add any fixed modifiers. The damage is the attack value less that sum.
- **Dodge:** costs one stamina. Roll the dodge dice on the equipped cards against the attack's dodge difficulty. One extra die may be bought for two more stamina; never more than four dice. Success: no damage, no condition, no push, and the character moves to an adjacent node of the player's choice. Failure: the character is hit and rolls only the block or resist dice of the armour card and its upgrades (two highest, as above).
- **Parry:** needs a weapon or shield in the left weapon slot (so never while wielding two-handed) and the attacker on the character's node. Not against a boss, and not against a push, area or node attack. Paid for and rolled as a dodge. Success: no damage, no condition, the attacker is staggered, and the character may at once make a riposte: one attack option of the right-hand weapon against that attacker, paying its stamina. Failure: the full attack value as damage with no dice rolled, and the character is staggered.
- Only attacks with a damage value can be dodged or parried.
- A character dies when a damage cube must be placed and no space is free. A bar that is exactly full is alive. Stamina that cannot be placed staggers the character instead (the author's rule), and a character may never choose to overspend.
- The endurance bar has ten spaces. A hollow character has eight: two hollow cubes fill the two rightmost spaces.

### 3.5 Conditions and pushes

- Bleed, calamity and corrosion: as the author wrote them.
- Poison: tokens stack. At the end of its turn a model suffers one damage for each poison token, then removes one token. Poison is not resolved once the last enemy has fallen.
- Frostbite: a frostbitten character recovers no stamina by any means and cannot take the rest action; a frostbitten enemy moves one node less. Removed at the end of the model's turn.
- Stagger: −1 to attack, block, resist and dodge. Removed at the end of the model's turn.
- A stagger or frostbite token placed during a model's own turn stays until the end of its next turn.
- Pushes: the author's rules. A boss cannot be pushed by a character.
- A push-move that shows a damage value attacks each character it pushes once for that push-move, however many nodes it covers. The character may defend; a dodge avoids the push.
- Heat-up: when a boss's health first reaches its heat-up point, shuffle one random heat-up card together with its behaviour deck and discard pile to form a new deck. Once per boss, at once.

### 3.6 Death and recovery

- A character who dies is removed from the encounter (model beside the bonfire), discards the ember token and keeps their souls.
- If the encounter is won, each character who died in it returns hollow: all damage, stamina and condition tokens removed, two hollow cubes placed. Tokens (estus, luck, heroic action) are not restored.
- A hollow character who dies is *lost* until the party next rests. The others fight on.
- An encounter is *failed* only when every character is dead. The party must then spend a spark and rest. If no spark remains, the players lose the game.
- After an encounter is *cleared*, every surviving character removes all stamina cubes and all condition tokens. No damage is healed. Tokens are not restored and hollow cubes stay.
- Hollow cubes are removed only by a rest or by an ember.
- Embering: the author's rules, with one change. An embered character cannot buy or use an ember card; one already held is kept. There is no limit on ember cards carried. When a boss is defeated every character becomes embered.

### 3.7 The road

- At setup one encounter card is dealt face down to each encounter tile, with two treasure cards face down on it (tier one before the mini-boss falls, tier two after). The two cards show that the encounter has never been cleared.
- The party fights the encounters in order from the bonfire towards the boss.
- First clear of an encounter: each character gains 3 / 4 / 5 souls for Level 1 / 2 / 3, and the party takes the tile's two treasure cards. Mark the encounter card with a black cube.
- A rest (section 3.8) resets every cleared and failed encounter.
- A reset encounter that has been cleared before may be fought again, any number of times over the game, for 1 / 2 / 3 souls each and no treasure. Or it may be skipped: each character suffers one damage and the party passes through. A character whose bar is full cannot skip.
- A failed encounter cannot be skipped: once reset, it must be fought.
- A Level 4 encounter and a boss pay six souls each. Standard invaders pay 3, advanced invaders 4.
- Souls are each character's own and cannot be given to another character.
- Dropped souls: when an encounter is failed, every character's souls are placed on that tile. When the party later clears that encounter, each character takes their own back. If the party fails an encounter where souls already lie, those souls are lost before the new ones are placed. Souls still lying on a tile when a boss is defeated go back to their owners.
- Treasure: the party decides which character takes each card; if it cannot agree, the character holding the aggro token decides. This holds for every shared reward in the book.
- Chests: one treasure card of the current tier is placed face down under each chest when the encounter is set up, and is taken when the encounter is cleared (mimics: section 3.11).
- The fog gate: the first time the party reaches a boss, the fog gate token moves to the bonfire tile. From then on the party may go straight from the bonfire to the boss, or walk the road again for souls. In a campaign the fog gate gives no shortcut.
- Encounter decks hold only the encounter cards of the set the next boss comes from. The party chooses its bosses; nothing is chosen at random.
- Event cards are those of the community Events Expansion II (49 event cards, 8 trap cards, 14 treasure cards), printed from `pnp/events/` with five cards' text changed (`pnp/events/edits.json`), in play when the players have it; its rules are in §7.5 (section 27 of 41_rules_workshop.md). Its treasure cards never enter a treasure deck or the shop. From the 2022 sets the book uses the Tomb of Giants and Painted World of Ariamis enemies, the Black Knight, Gravelord Nito, the Heavy Knight and Crossbreed Priscilla (Appendix B, §17.7, §17.10) and the new treasure cards; their printed encounter cards and event cards are not used. Two print-and-play encounter decks in the 2017 pattern (`pnp/encounters/`, 27 cards each) may replace the printed encounter decks, decided at the start of setup (§6.5); never mixed with printed cards.
- A gravestone lets the party reveal one hidden card: the top card of either treasure deck or of the next boss's behaviour deck (put back on top or on the bottom), or a face-down encounter card or event card on any tile (put back or replaced with the top card of its deck).
- Traps: placed as the author wrote. A trap is sprung when a character moves or is pushed onto its node and hits every model on that node, enemies included. A character may dodge it (trap damage cannot be blocked or resisted); a character who dodges a trap stays on the node.

### 3.8 The bonfire

- **A rest costs one spark.** It removes all damage, stamina, condition tokens and hollow cubes, flips luck, estus flask and heroic action tokens face up, returns lost characters, and resets every cleared and failed encounter. The party may rest whenever it is not in an encounter. After a boss is defeated the party rests without spending a spark.
- **Stats are raised only during a rest.** Each tier is paid for in order: 2, 4, 8 and 12 souls for tiers one to four. A tier four stat is the tier three value plus five, marked by a red cube.
- **Blacksmith Andre may be visited whenever the party is not in an encounter, without resting:** to buy, to sell and to fit upgrades.
- The shop is face up. Tier one cards cost two souls, tier two cards four. Any card that is not starting equipment sells for one soul and goes to the bottom of its deck. Starting equipment cannot be sold. Shops are restocked only when a boss is defeated.
- Shop stock (the author's): 3 weapons, 3 armour, 2 shields, 2 upgrades, 2 spells in each tier; the tier one shop also holds ember cards equal to the number of characters. Tier two is stocked when the mini-boss falls.
- Upgrades are fitted at Andre. Titanite stays on its weapon and is sold with it for no extra souls. Any other upgrade on a sold card returns to the character's inventory.

### 3.9 Treasure decks

- All treasure of every set the party owns is used. Only the starting equipment of characters not being played returns to the box. Only the cards that are new in the 2022 sets are added from them (see Appendix B); a reprint is not added twice.
- Tier one: every class treasure card, and every common treasure card that asks for less than 25 in every stat.
- Tier two: every transposed treasure card, and every common treasure card that asks for 25 or more in a stat.
- When the mini-boss falls and after the tier two shop is stocked, shuffle into the tier two deck: five legendary treasure cards drawn at random, the mini-boss's own treasure cards, and the main-boss's own treasure cards. They are found as treasure and never stocked in the shop. In the standard game no treasure card is handed over for defeating a boss.
- Requirements are those of Appendix A where it lists the weapon.

### 3.10 After a boss

When a mini-boss or a main-boss that is not the final boss is defeated, in this order: each character gains six souls; the PvP encounter is fought if there are two or more characters (section 3.12); add one spark; every character becomes embered; the party rests without spending a spark; the next stage is set up (the author's steps, amended by this brief). The players win when the final boss falls: the main-boss, or the mega-boss if the party chose one at setup.

Mega-boss stage: the author's steps, except that death works there as everywhere else. No character is removed for good; sparks are the retries.

### 3.11 Expansion content (in play whenever owned)

- **Summons (Phantoms):** only an embered character may summon, at the fog gate before a mini-boss or main-boss, for two souls. The summon takes a turn after each character's turn. The author's steps otherwise. Include in four sentences how a summon is targeted and damaged by the boss (the v2 chapter has this; condense it).
- **Invaders (Phantoms):** the author's rules. The invader token is flipped when the party enters the tile, before the encounter card is revealed. The invader takes a turn after each character's turn.
- **Mimics (Explorers):** the author's rules, with these: the characters do not recover before the fight; if the party loses to the mimic, it chooses on its next clear whether to open the chest again. A party that leaves the chest closed recovers as after any clear.
- **Crystal lizards (Iron Keep):** the character who kills a lizard takes a Titanite Scale at once.
- **Two-model bosses:** Ornstein and Smough, and the Twin Gargoyles in a campaign, are two models with a health dial each, played from their cards. About 80 words each.
- **Phalanx:** there is no Phalanx model. The Phalanx is shown by three Phalanx Hollow models placed together. One line in the component list.

### 3.12 Player versus player

Fought after every boss in every game with two or more characters. The author's rules as written, plus: the attacker's roll is the attack value and the defender blocks, resists, dodges or parries as against an enemy, with the dodge difficulty from the author's table; ties in threat for turn order are settled by a die roll. No stalemate rule and no round counter.

### 3.13 Campaign play

The author's chapter, with these:

- Sparks: start at five less the number of characters; that number is also the maximum; one is gained for each boss defeated, never above the maximum; never bought. The party rests free only after the last boss of a section.
- Every soul reward is one lower than in the standard game (first clear 2 / 3 / 4; a reset encounter fought again 0 / 1 / 2; Level 4 encounters and bosses 5). Stat costs are doubled (4 / 8 / 16 / 24).
- Reset encounters: fought again or skipped as in section 3.7.
- Treasure: two cards a tile as in section 3.7, from tier one until the bonfire ascetic is burnt.
- Bonfire ascetic: 16 souls from the party; afterwards every non-boss enemy attack has +1 damage, on top of the party-size table.
- A defeated boss gives the party one of its own treasure cards at random. Legendary treasure comes only by transposition. Every card sells for one soul.
- Joining and leaving: the author's four sentences, with sparks as above.
- A fourth stat tier costs 24 souls in a campaign.

## 4. Section map, owners and budgets

Use these headings exactly. A chapter owns the rules named after its sections.

**00 Front matter** (`10_manuscript_chapter_00_front_matter.md`; 250 words): title, colophon, foreword. Keep the v2 file's structure; bring the foreword into line with this brief (no optional rules, no mention of anything this brief removes).

**§1 Introduction** (140 words; no sections).

**§2 Game Components** (1,300 words): 2.1 Characters · 2.2 Enemies · 2.3 Bosses · 2.4 Phantoms · 2.5 Treasure Cards · 2.6 Encounter, Event and Ambush Cards · 2.7 Dice · 2.8 Tokens and Terrain Elements. A packing list: names and counts by set, as the author laid it out, with the v2 file's corrected names and its expansion entries folded into the lists. Says what a component is in a clause at most, never how it is used. Owns: the die faces (2.7, a small table).

**§3 Characters** (965 words): 3.1 Character Dashboards · 3.2 Equipment Slots · 3.3 Stat Progression Track · 3.4 Endurance Bar · 3.5 Character Tokens (### Heroic Action, Luck, Estus Flask, Ember). Owns: slots, inventory and trading, the endurance bar (ten and eight), what kills a character's bar and staggers it, luck. Does not say how tokens are restored (§11.2) or what embering does (§7.3).

**§4 Equipment** (880 words): 4.1 Equipment Cards · 4.2 Upgrades · 4.3 Spells · 4.4 Embers. Owns: reading an equipment card, upgrade slots and the Titanite rule, spells (one a turn; never scaled, two-handed or riposted), ember cards.

**§5 Tiles and Nodes** (955 words): 5.1 Tiles and Nodes · 5.2 Movement · 5.3 Node Model Limits · 5.4 Range · 5.5 Terrain (### Gravestones, Barrels, Chests, Traps). Owns: nodes, adjacency, what blocks movement, model limits, range, each terrain piece, trap placement and resolution. One example: range counted around a blocked node, if the author had one; otherwise none.

**§6 Setup** (1,715 words): 6.1 Character Setup · 6.2 Treasure Deck Setup · 6.3 Shop Setup · 6.4 Bonfire Setup · 6.5 Encounter Setup · 6.6 Setup After the Mini-Boss · 6.7 Setup After the Main-Boss. Owns: section 3.9 of this brief in full, shop stocking, the layout, dealing encounter, treasure, event and ambush cards and invader tokens, the two later setups. Numbered steps, as the author wrote them.

**§7 Gameplay** (1,680 words): 7.1 Objective and Loss Conditions · 7.2 Death and Hollowing · 7.3 Embering · 7.4 Sparks · 7.5 Encounters (### Encounter Start, Encounter Turn Order, Encounter Resolution, Encounter Recovery) · 7.6 Souls (with the soul reward table) · 7.7 Treasure Rewards. Owns: sections 3.2 (ordinary encounter), 3.6 and 3.7 of this brief except what §5, §6, §11 and §15 own; the event card rule (under Encounter Start); skipping a reset encounter; dropped souls.

**§8 Combat Basics** (1,260 words): 8.1 Target versus Hit · 8.2 Enemy Data Cards · 8.3 Scaling · 8.4 Pushing · 8.5 Conditions (### Bleed, Poison, Frostbite, Stagger, Calamity, Corrosion). Owns: the whole table of 3.1 (8.3), pushes, conditions. Examples: one for push direction, one for scaling.

**§9 Enemy Turn** (1,450 words): 9.1 Overview · 9.2 Enemy Movement · 9.3 Enemy Attacks · 9.4 Block and Resist · 9.5 Dodge · 9.6 Parry and Riposte. Owns: enemy movement and targeting, the push-move with a damage value, section 3.4 of this brief. The order of an attack's effects is one sentence: place the damage, then the push, then the condition. Examples: one dodge, one parry.

**§10 Character Turn** (1,130 words): 10.1 Turn Order · 10.2 Character Movement · 10.3 Character Attacks (### Range, Shift, Area-of-Effect, Shaft, Repeat) · 10.4 Two-Handed Attacks · 10.5 Stat Scaling. Owns: section 3.3 of this brief. Examples: one attack, one stat scaling.

**§11 Returning to the Bonfire** (830 words): 11.1 The Bonfire · 11.2 Resting · 11.3 The Firekeeper · 11.4 Blacksmith Andre · 11.5 Resuming Exploration. Owns: section 3.8 of this brief; 11.5 says only that encounters are reset and how the tiles are reset, and points to §7.5 and §15.1.

**§12 Phantoms** (845 words): 12.1 Summons · 12.2 Invaders.

**§13 Mimics** (520 words; no numbered sections). **§14 Crystal Lizards** (260 words; no numbered sections).

**§15 Boss Encounters** (1,615 words): 15.1 The Fog Gate · 15.2 Overview · 15.3 Boss Tiles · 15.4 Boss Data Cards · 15.5 Boss Behaviour Cards · 15.6 Arcs and Defence. Owns: the fog gate, how a boss encounter is set up (four sentences, in 15.2), boss cards, heat-up, arcs. Example: one for arcs.

**§16 Boss Turns** (915 words): 16.1 Overview · 16.2 Boss Movement and Symbols · 16.3 Boss Attacks · 16.4 Boss Aggro · 16.5 Boss Death. Owns: the boss's turn before each character's turn, boss movement symbols, boss aggro (one sentence), section 3.10 of this brief. Characters defend against a boss as against an enemy (§9); do not restate §9.

**§17 Boss Special Rules** (3,950 words): 17.1 Rules Common to Several Bosses · 17.2 Core Set · 17.3 Asylum Demon and Stray Demon · 17.4 Darkroot · 17.5 Iron Keep · 17.6 Explorers · 17.7 Tomb of Giants · 17.8 Black Dragon Kalameet · 17.9 Executioner's Chariot · 17.10 Bosses of Other Expansions. See the special instructions in your assignment.

**§18 Campaign Play** (1,415 words): 18.1 Setup · 18.2 The Fog Gate · 18.3 Sparks · 18.4 Adding and Dropping Players · 18.5 Encounter Rewards · 18.6 The Bonfire · 18.7 Bonfire Ascetic · 18.8 Transposition. Owns: section 3.13 of this brief.

**§19 Campaigns** (1,930 words): 19.1 The First Journey · 19.2 The Coiled Sword · 19.3 Ambush Lies Ahead · 19.4 The Gauntlet · 19.5 Facing the Abyss · 19.6 Demon Hunting · 19.7 Call of the Abyss · 19.8 A Hollow Pursuit · 19.9 The Undead Colosseum · 19.10 Into the Depths · 19.11 Playing with Fire · 19.12 Big Game Hunting · 19.13 Go Beyond Death · 19.14 Footsteps of Giants · 19.15 Treasures of the Ice Cave · 19.16 Demons and Dragons. One compact table per campaign.

**§20 Player versus Player** (500 words; no numbered sections needed, or at most 20.1 Setup · 20.2 The Fight · 20.3 Victory).

**§21 Glossary** (`12_glossary.md`; 2,200 words): one line per term with its section number.

**§22 F.A.Q.** (400 words; no numbered sections): ten answers.

**Appendix A. Weapon Stat Revisions · Appendix B. Card Amendments** (`10_manuscript_chapter_23_appendices.md`; 1,400 words).

## 5. Before you finish

1. Count the words of each file you wrote (`wc -w`) and compare with the budget. Cut if over by more than 10%.
2. Run `python3 tools/style_check.py <your files>` from the repository root and fix every violation except "undefined keyword" ones for terms that are in the italic list above.
3. Check every "(see §N.M)" against section 4.
4. Read the author's chapter once more beside yours. Every rule of the author's must either be in your chapter, be owned by another chapter per section 4, or be replaced by section 3. List in your report anything of the author's you dropped and why.

Your report (your final message, plain text, under 300 words): word count per file; rules of the author's dropped; sentences you added on your own judgement; anything in this brief you found contradictory or impossible to follow.
