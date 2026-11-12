# Bloat audit — core group (chapters 02 to 07)

Auditor's note on method. Word figures are `len(text.split())` over the body of each H2 section (heading lines excluded). "Needs" is my estimate of the words the section requires to state the author's rules, plus the few additions the game cannot be played without. Following the lead's instruction to shorten the deliverable, each section table gives source words, final words, words needed and the main class of excess; per-class word columns are replaced by a group split in the Totals.

Classes: R restated · X cross-reference clutter · D defensive · A added rule (A1 needed, A2 one sentence would do, A3 not needed, A4 less intuitive) · E example · V verbose · G glossary-in-chapter.

---

## Chapter 02 — Game Components

### Section table

| § | source words | final words | words it needs | main excess |
|---|---|---|---|---|
| intro | 0 | 54 | 23 | V: a sentence listing the chapter's contents |
| 2.1 Characters | 61 | 81 | 62 | R: transposed treasure (owned by §6.2) |
| 2.2 Enemies | 203 | 251 | 220 | A: a Phalanx formation rule inside a list |
| 2.3 Bosses | 139 | 299 | 165 | R: 100 words of chapter 15 and 17 rules (dials, tiles, Ornstein & Smough, Stray Demon); X 10 |
| 2.4 Phantoms | 82 | 176 | 105 | R: when summons and invaders appear (owned by §12.1, §12.2) |
| 2.5 Treasure Cards | 59 | 188 | 85 | G: "Treasure card" definition; R: five-and-five split said twice in the chapter |
| 2.6 Encounter and Ambush Cards | 72 | 233 | 105 | R: what an encounter card does (owned by §6.5, §7.5); V: per-set card arithmetic |
| 2.7 Dice | 12 | 126 | 62 | R: what each die is rolled for, four pointers |
| 2.8 Tokens and Terrain | 121 | 592 | 235 | R: every token's use explained (190 words); A: white-cube rules; X 19 |
| 2.9 Expansion Components | 0 | 452 | 240 | R: six components listed a second time; rules of §12.2, §6.7 restated; X 20 |
| **Chapter** | **749** | **2,452** | **1,302** | |

The author's chapter is a packing list. The final chapter is a packing list with a rules summary of chapters 5 to 17 threaded through it: 61 "(see §…)" pointers, and a reader meets invasions, black cubes, mega-boss game boards and transposed treasure before any of them is defined.

### Added rules

- §2.2 · The Phalanx has a data card and no model, "shown by three Phalanx Hollow models placed together" · CH-02-034 (campaign-E05) · **A4** · The author listed "5x Phalanx, 1x Phalanx Hollow". The final text reverses the two and adds a formation rule that no other chapter mentions or supports. List the models and the data cards; delete the formation clause or put it where the enemy's rules are.
- §2.3 · A boss with several models "that stand on separate nodes" has a health dial for each; the Executioner's Chariot's two models share one · CH-02-047 (lead-E14), CH-02-048 (VA-002) · **A3 here** · A rule, its qualifier and its exception, all owned by §17. The component line "1x health dial (The Four Kings has four)" in §2.9 already says it.
- §2.3 · Ornstein & Smough paragraph (two models, own cards and dials, one deck, both act each boss turn) · CH-02-008 (OQ-25), CH-02-044 (boss-E42) · **A2** · The list correction is right. The paragraph is §17.2. One list line: "Ornstein & Smough (Core), two models".
- §2.5 · Bold definition of "treasure card" extended to "or from Blacksmith Andre's shop … or an ember card" · CH-02-013, CH-02-043 (lead-E08) · **A3** · Nobody at the table asks whether an ember card is a treasure card. The glossary carries it.
- §2.6 · Ambush cards · CH-02-015 (CMP-0012(b)) · **A1 as a list line**, the 35-word rule sentence is §13 restated.
- §2.6 · Per-set breakdown of encounter cards ("the Darkroot and Iron Keep expansions supply six cards each, the Explorers expansion five …") · CH-02-040 (campaign-E11) · **A3** · Written "so that the total can be checked". That is an audit trail, not rulebook text.
- §2.7 · Die face table · CH-02-017 (B-001, OQ-23) · **A1** · Keep the table (24 words). Cut the paragraph saying which roll uses which die.
- §2.8 · Hollow cubes are spare white cubes; "a white cube is placed on an endurance bar for no other purpose, so a hollow cube cannot be taken for a damage cube or a stamina cube"; fallback to "any other markers that are neither red nor black" · CH-02-019, CH-02-030, CH-02-031 (core-E01, core-E02) · **A2** · Three change-log entries to arrive back at the author's seven words: "a marker such as white cubes".
- §2.8 · "The supply … is not a limit" stated three times (white cubes, soul tokens, condition tokens) · CH-02-021 (B-028), CH-02-033 (campaign-E04), CH-02-031 · **A2** · One sentence for all components.
- §2.9 · New section listing expansion components · CH-02-024 (CMP-0012), CH-02-035 to 037 (campaign-E06 to E08), CH-02-045 (boss-E44) · **A1 for the lists, A2 for the layout** · Ambush cards, pillar tokens, calamity tokens, corrosion tokens, terrain models, Level 4 cards and Titanite Scale cards are each listed twice in the chapter (once by type in §2.5 to §2.8, once by set here). List each once.
- §2.9 · Invader token placement "on each face-down encounter card that carries no black cube, and each is revealed when the characters fight that encounter" · CH-02-027 (QA-006), CH-02-042 (phantom-E16) · **A3 here** · A §12.2 rule kept "in step" in a component list across two rulings. Every later change to §12.2 has to be mirrored here.

### Worst passages

**1. §2.8, cubes (95 words).**

> "*Damage cubes* and *stamina cubes* are placed on the *endurance bar* (see §3.4). *Stat cubes* mark each character's *stat tier* on the stat progression track (see §3.3). *Hollow cubes* are white cubes that are not in use as stat cubes; two are placed on the endurance bar of a character who is *hollow* (see §7.2). A white cube is placed on an endurance bar for no other purpose, so a hollow cube cannot be taken for a damage cube or a stamina cube. The supply of white cubes is not a limit: when every white cube is in use, the players mark the blocked spaces with any other markers …"

Source: "32x Red damage cubes / 32x Black stamina cubes / 16x Stat tier cubes" and, in the Characters chapter, "a marker such as white cubes".

Cut version (28 words):

> Red cubes mark damage, black cubes mark stamina, and white cubes mark stat tiers. No component is limited by its supply; when one runs out, any substitute serves.

**2. §2.3, opening paragraph (100 words).**

> "Each *boss* has a model, a *health dial*, a *data card* (see §15.4), a *behaviour deck* (see §15.5), and two or more *boss treasure* cards (see §2.5). A boss fought with several models that stand on separate nodes has a health dial for each of them (see §17.1); the two models of the Executioner's Chariot share one health dial (see §17.9). A *mini-boss* or *main-boss* is fought on the *boss tiles* (see §15.3). A *mega-boss* is fought on the *mega-boss game board* supplied with its expansion (see §2.9), after a Level 4 encounter (see §6.7)."

Source: no text; lists only.

Cut version (21 words):

> Each boss has a model, a health dial, a data card, a behaviour deck, and two or more boss treasure cards.

**3. §2.6, encounter cards (135 words around a four-row table).**

> "An *encounter card* lists the level, enemies, terrain, and traps of one encounter. One encounter card is dealt face down to each encounter tile at setup (see §6.5) and is revealed when the characters enter the tile (see §7.5, Encounter Start). The *encounter level* is shown by the card's level icon … In all, 187 encounter cards are available. Of each of Levels 1 to 3, the Darkroot and Iron Keep expansions supply six cards each, the Explorers expansion five, the Executioner's Chariot expansion two, and ToG and PWA nine each. Level 4 encounter cards are supplied only by the mega-boss expansions, four with each, and are used only for the encounter that precedes a mega-boss (see §6.7)."

Source: the counts and "Total 169 encounter cards in all available content."

Cut version (the table, then 22 words):

> In all, 187 encounter cards are available. Each mega-boss expansion supplies four Level 4 cards. A trapped encounter shows the trap icon.

### Unintuitive or over-engineered

- **A white cube has three names.** It is a stat cube on the track, a hollow cube on the endurance bar and a white cube in the supply, with a rule about what it can be "taken for". Simpler: "a hollow character blocks the two rightmost spaces with any spare marker". Nothing is lost.
- **The Phalanx.** A player who owns the box will count models against this list. The final list disagrees with the author's, and the "three models placed together" clause is a rule with no home. Needs the author's eye, not more text.
- **Components listed by type and again by set.** A player checking the box reads §2.6 for ambush cards and finds them again in §2.9 with a different pointer. One list, each line tagged with its set as the author did.
- **Rules terms ten chapters early.** "Carries no black cube", "provoked", "transposed", "mega-boss side face up" appear here undefined. A component list should name pieces, not operate them.

---

## Chapter 03 — Characters

### Section table

| § | source words | final words | words it needs | main excess |
|---|---|---|---|---|
| intro | 0 | 59 | 0 | V: flavour and a table of contents in prose |
| 3.1 Character Dashboards | 72 | 260 | 95 | G: bold "Threat" definition (75 words, owned by §7.5); X 10 |
| 3.2 Equipment Slots | 252 | 515 | 250 | A: left and right weapon slots; R: shields, parry, spells, Equip, two-handed; E 77 |
| 3.3 Stat Progression Track | 133 | 357 | 140 | R: stat tier four, costs, scaling (owned by §11.3, §10.5); E 62 |
| 3.4 Endurance Bar | 313 | 468 | 260 | E: two examples, 117 words; D: "the cube is not placed" |
| 3.5 Character Tokens | 229 | 426 | 220 | R: refresh rule said with its converse and its consequence; Ember sub-section is four pointers |
| **Chapter** | **1,070** | **2,085** | **965** | |

This is the one chapter of the group where the author's own text was already wordy (the Endurance Bar section says each placement rule twice). A tight edit would come in under the source. The final text instead doubles it.

### Added rules

- §3.2 · "Left weapon slot" and "right weapon slot" as named terms, "the weapon slot on the left of the dashboard as its player reads it" · CH-03-005 (A-068, D-030), CH-03-031 (CMP-0003) · **A3** · Introduced because the parry was to depend on which slot held the shield. Ruling combat-E22 (CH-03-036) then made a shield in either slot permit a parry. No rule in the book now depends on left or right; the terms survive in three examples and the glossary. Delete: "two weapon slots".
- §3.2 · "A one-handed weapon equipped while the other weapon slot is empty is wielded two-handed" · restated from §10.4 (the author's rule, in the Character Turn chapter) · R, not A · Keep in §10.4 only.
- §3.2 · "An armour card cannot be equipped in a weapon slot." · CH-03-005 sweep · **A3** (D) · The slot holds weapon cards.
- §3.2 · "During an encounter, characters cannot trade or give cards in any way." · author's rule, kept · K.
- §3.3 · Stat tier four: "replaces the stat cube in the stat tier three space with a red cube … value of 40, or the stat tier three value plus five, whichever is higher" · CH-03-012 (Gate 1 OQ-09) · **A2 here** · The author's decision, so the rule stays, but it is a campaign-length matter stated in full in a dashboard description. One clause here; the value formula belongs with the costs in §11.3.
- §3.3 · "a weapon whose stat requirements are all zero is never scaled" · CH-03-013, CH-03-038 (VA-005) · **A3 here** · An exception to a rule this section does not own, added by a verification pass to keep a pointer sentence "in step" with §10.5.
- §3.4 · "A recovery that finds no cube of the right kind to remove has no effect." · CH-03-018 · **A3** (D) · Nothing else could happen.
- §3.4 · "the cube is not placed" (twice) · CH-03-017 · **A3** (D).
- §3.4 · Endurance bar of 10 spaces, hollow leaves eight (source: eight and six) · CH-03-014 (Gate 1 OQ-08) · author's decision · K.
- §3.5 · Estus Flask sub-section · CH-03-027 (CMP-0001) · **A1** · The source had the heading in its contents and no text. The first sentence is the rule. "Stamina cubes are not removed. Hollow cubes are not removed. Condition tokens are not removed." is three defensive sentences after "remove all damage cubes".
- §3.5 · "so each is used at most once between rests. Clearing an encounter does not ready them" · CH-03-024, CH-03-032 (core-E12) · **A2** · The rule is "readied only at the bonfire". Its consequence and its converse are each a further sentence.
- §3.5 · Luck: "one of their own … (a block, resist, dodge, or parry roll)" · CH-03-026 (F-096), CH-03-035 (core-E18) · **A2** · "Own" is a real clarification, one word. The list of defence rolls had to be patched once already when parry was left out; a list that needs maintaining is a list to cut.
- §3.5 · Ember token "begins the game beside the dashboard, not in its slot" · CH-03-023 (CMP-0001) · **A1**, one clause (source said "condition token supply").

### Worst passages

**1. §3.2, weapon slots and shields (150 words).**

> "**Weapon slots.** The left weapon slot and the right weapon slot: the weapon slot on the left of the dashboard as its player reads it, and the weapon slot on its right. Each holds one weapon card, marked with the one-handed weapon icon … or the two-handed weapon icon …. A one-handed weapon may be equipped in either weapon slot, and the other weapon slot may hold a second one-handed weapon. A two-handed weapon may be equipped in either weapon slot, and the other weapon slot must then be empty. A one-handed weapon equipped while the other weapon slot is empty is wielded *two-handed* (see §10.4). Shields are weapon cards and occupy a weapon slot (see §4.1). A shield in either weapon slot permits a *parry*, and the *riposte* is made with the weapon in the other weapon slot (see §9.6). Spell cards are equipped in a weapon slot or stored in an equipped *catalyst* (see §4.3)."

Source: "Weapon cards … may only be equipped to the weapon slots. If a two-handed weapon is equipped to a weapon slot, the other weapon slot must remain empty. If a one-handed weapon card is equipped … the other weapon slot may contain another one-handed weapon card. Only a single weapon card may be equipped to each weapon slot at any given time."

Cut version (35 words):

> **Weapon slots.** Each of the two weapon slots holds one weapon card. Two one-handed weapons may be equipped together. While a two-handed weapon is equipped, the other weapon slot stays empty. Shields are weapon cards.

**2. §3.1, Threat (75 words) and the two lines after it.**

> "**Threat.** The value that fixes a model's place in the turn order. Characters act in descending order of threat, and the character with the highest threat takes the *aggro* token at the start of each encounter (see §7.5, Encounter Start; §7.5, Encounter Turn Order). The dashboard prints the character's threat as its Taunt Level. Enemies and *phantoms* also have a threat value, printed on their *data cards* (see §8.2, §12). The character's *souls* are kept on the dashboard as soul tokens (see §7.6). The character's inventory is kept beside the dashboard (see §3.2)."

Source: "7. *Threat* Level".

Cut version (17 words, as the list item):

> - The threat value (printed as Taunt Level), which fixes the character's place in the turn order.

**3. §3.5, the general paragraphs and Ember (190 words).**

> "The heroic action, luck, and estus flask tokens begin the game ready, in their slots on the dashboard (see §6.1). They are flipped back to the ready side only when the characters rest at the *bonfire* (see §11.2), so each is used at most once between rests. Clearing an encounter does not ready them (see §7.5, Encounter Recovery). The ember token marks a character who is *embered*. It begins the game beside the dashboard, not in its slot, and is placed in its slot only when the character becomes embered (see §7.3). … **Ember.** The ember token marks an embered character. When a character becomes embered, the character places the ember token in its slot on the dashboard; when an embered character dies, the ember token is removed from the dashboard (see §7.3). A character becomes embered by using an *ember card* (see §4.4). The effects of being embered, and when it ends, are stated with the embering rules (see §7.3). An embered character may summon a *phantom* before a boss encounter and attracts *invaders* (see §12)."

Cut version (44 words, and no Ember sub-section):

> The heroic action, luck, and estus flask tokens begin the game ready and are readied again only when the characters rest at the bonfire. The ember token begins beside the dashboard and is placed in its slot while the character is embered (see §7.3).

### Unintuitive or over-engineered

- **Left and right weapon slots.** A player reads a defined pair of terms and looks for the rule that uses them. There is none. Lost by cutting: nothing.
- **Stat tier four on the dashboard.** "Replaces the stat cube … with a red cube and returns the stat cube to the supply. A stat at stat tier four has a value of 40, or the stat tier three value plus five, whichever is higher." A red cube on the stat track sits on the same dashboard as red damage cubes, and the value needs a comparison. Simpler: "Tier four: +5 to the tier three value; turn the cube on its edge or mark it with any spare token." What is lost: the flat 40, which only matters for a stat whose tier three value is below 35; the author should say whether that case exists.
- **The Equip example (§3.2).** It shows a single minor action moving three cards (sword and shield out, axe in). If that is the rule, it is a rule and should be one sentence in §10.1; if it is not, the example is wrong. Either way the example is carrying a ruling.
- **The hollow endurance example (§3.4).** Seventy words to show that a character with one empty space can spend one stamina. Cut it. The death example earns half its length.
- **Ember in three chapters.** §3.5 Ember, §4.4 Embers and §7.3 Embering each say how a character becomes embered and what the token does. The change log notes it ("Embering is defined in three places in the manuscript", CH-03-028); the restructure kept all three sections and turned two into pointer paragraphs. One section should own it.

---

## Chapter 04 — Equipment

### Section table

| § | source words | final words | words it needs | main excess |
|---|---|---|---|---|
| intro | 0 | 37 | 0 | V: flavour and contents |
| 4.1 Equipment Cards | 301 | 788 | 300 | R: attacking, defending, scaling, two-handed, treasure tiers all summarised (130 words); X 28; G: treasure card defined a second time; E 47 |
| 4.2 Upgrades | 273 | 499 | 270 | A: Titanite name test, replacement, sale routing; E: two examples that show nothing (77 words) |
| 4.3 Spells | 187 | 451 | 230 | D: the two-handed spell paragraph; A: stored-spell restrictions |
| 4.4 Embers | 61 | 201 | 80 | A: carry limit, box disposal; D: inventory sentence; closing pointer sentence |
| **Chapter** | **822** | **1,976** | **880** | |

### Added rules

- §4.1 · Five card kinds, with the shield defined as "a one-handed weapon that shows block or resist dice and has no attack option" · CH-04-005 (A-069, B-022) · **A1 for the shield, A2 for the rest** · The parry needs a shield and the source never said what one is. That is one sentence. The other four bullets say that a weapon bears a weapon icon and armour the armour icon.
- §4.1 · "The stat requirements of the weapons listed in Appendix A are those given there, in place of the printed values" · CH-04-033 (core-E27) · **A1, but misplaced** · A rule that overrides what is printed on the cards is the least guessable rule in the chapter, and it is the fourth sentence of a paragraph about something else. Give it its own line.
- §4.1 · "A part that does not apply to a card is not printed on it." · CH-04-004 · **A3** (D).
- §4.2 · A Titanite card is any weapon upgrade "whose name includes the word Titanite", with six names listed · CH-04-016, CH-04-035 (core-E34, mechanical change) · **A2** · The author already wrote the name test ("any upgrade card, including the word Titanite"). The ruling says the test avoids "a second list", and then the text prints the list.
- §4.2 · Titanite cannot be removed "except when a Titanite Chunk or a Titanite Slab takes its place (see Appendix B, Titanite Replacement)" · CH-04-027, CH-04-028 (QA-002) · **A2** · Exception imported from an appendix into the rule and again into the example.
- §4.2 · Sold Titanite "adds nothing to the sell value. The weapon and the Titanite are separated, and each goes where a sold card of its kind goes" · CH-04-014 (A-074), CH-04-034 (core-E31, mechanical change) · **A4** · The author: Titanite goes to the bottom of the deck with its weapon. The final rule fuses the card permanently, then un-fuses it at the point of sale and routes the two halves separately, with the destination in another chapter. The author's version is one motion.
- §4.2 · Attaching an upgrade spell costs its stamina, is the Attack major action, is the turn's one spell attack option, "and the weapon slot that holds the upgrade spell or its catalyst makes no other attack that turn"; "occupies no upgrade slot" · CH-04-015 (D-034, A-071) · **A2** · The author said "as a main action similar to casting an attack spell". "It is cast as a spell" carries every one of these consequences.
- §4.3 · "A stored spell provides only its attack options; its block, resist, and dodge dice are not rolled. Using a stored spell's attack option counts as the catalyst's one attack for that turn." · CH-04-019 (A-070, CMP-0016) · **A2** · The author's "may use their attack options as if equipped" already limits a stored spell to its attack options. The one-attack-per-slot rule is §10.3's.
- §4.3 · "A character who does not meet a stored spell's stat requirements cannot use it" · CH-04-019 · **A2**, a clause.
- §4.3 · A spell with the two-handed icon needs the other slot empty "and it gains no reroll by this"; "a spell equipped with the other weapon slot empty is not two-handed" · CH-04-032 (core-E26) · **A3** (D) · Fifty-five words defending the author's eleven: "Spells cannot be two-handed and do not receive two-handed bonuses."
- §4.4 · "A character may carry at most one ember card at a time, in the back-up slot or in the inventory." · CH-04-023 (A-046, A-006) · **A3** · Not in the source. The author's two limits are the shop's stock and "characters cannot carry an ember card while embered" (the source's Embering section, kept here as the next sentence). A one-card limit needs policing at every purchase and trade and prompted the hand-off rule of §7.3.
- §4.4 · "The consumed card is returned to the game box and takes no further part in the game." · CH-04-031 (core-E24) · **A3** · The author said "discarding".
- §4.4 · "The *Ember* major action" · CH-04-024 (Gate 1 OQ-30) · author's decision · K.

### Worst passages

**1. §4.3, spells and hands (85 words).**

> "Spells are never *scaled* (see §10.5). Spells are never *two-handed*: a spell gains no two-handed reroll, and a spell equipped with the other weapon slot empty is not two-handed (see §10.4). A spell card that bears the two-handed weapon icon requires the other weapon slot to be empty while it is equipped in a weapon slot (see §3.2), and it gains no reroll by this. A spell attack option that bears the *magical damage* icon … deals magical damage, which the target reduces with its *resist* rather than its *block* (see §9.4)."

Source: "Spells cannot be affected by scaling and do not receive scaling bonuses. Spells cannot be two-handed and do not receive two-handed bonuses."

Cut version (9 words):

> Spells are never scaled and never gain two-handed bonuses.

**2. §4.1, the three paragraphs after the stat requirement rule (135 words).**

> "A character's stat is the value marked on their stat progression track (see §3.3). A card's stat requirements also decide its treasure tier, split at a requirement of 25 (see §6.2). The stat requirements of the weapons listed in Appendix A are those given there, in place of the printed values (see Appendix A). A character whose stat exceeds a weapon's requirements by a wide margin wields it as a *scaled* weapon and gains a bonus to its attacks (see §10.5). A character attacks by using one attack option of a weapon or spell equipped in a weapon slot as the *Attack* major action (see §10.3). A weapon that bears the two-handed icon requires the other weapon slot to be empty (see §3.2), and attacks with a *two-handed* weapon may reroll one die (see §10.4). When an enemy attacks the character, the block, resist, or dodge dice of the character's equipped cards are rolled in defence (see §9.4, §9.5)."

Source: "Each line on the card represents a separate attack option … explained in detail later"; "An equipment card provides defensive capabilities including block, resist, and dodge … explained in detail later".

Cut version (18 words):

> The weapons listed in Appendix A use the stat requirements given there in place of their printed values.

**3. §4.4, Embers (the whole section, 201 words).**

> "… A character may carry at most one ember card at a time, in the *back-up slot* or in the *inventory*. An embered character cannot carry an ember card. During an *encounter*, a character may consume an ember card only from the back-up slot (see §3.2). During an encounter, the inventory cannot be accessed, so an ember card there cannot be consumed until the encounter ends. A character consumes an ember card by discarding it from the back-up slot, as the *Ember* major action during an encounter or at any time outside an encounter. The consumed card is returned to the game box and takes no further part in the game. The character then becomes embered and places an *ember token* on their dashboard (see §7.3). The ember token and the effects of being embered are set out with the character tokens (see §3.5, Ember) and with embering (see §7.3)."

Source (61 words): "Ember cards may only be purchased from the tier one shop and are in limited supply. Ember cards may be stored in a player's inventory, but must be equipped to the backup slot to be available for use during an encounter. Discarding an ember card permits the character to place an ember token on their character dashboard …"

Cut version (47 words):

> An ember card is bought from the tier one shop, which is stocked with embers at setup only. A character discards an ember card from the back-up slot to become embered (see §7.3): as the Ember major action during an encounter, or at any time outside one.

### Unintuitive or over-engineered

- **Selling a weapon with Titanite.** "Fuses permanently", "cannot be removed, except", "sold with it and adds nothing", "separated, and each goes where a sold card of its kind goes". Four states for one card. The author's rule: it goes to the bottom of the deck with the weapon. What the ruling bought (a Titanite Chunk returning to the tier two deck) is not worth a rule a player must look up in two chapters and an appendix.
- **Card anatomy as eleven bold-headed bullets with nine pointers.** The author's eleven-item numbered list keyed to a picture is the right form. Each final bullet adds a sentence of rule from the owning chapter ("are rolled against physical attacks (see §9.4)"). A labelled diagram and the author's list do the job in a quarter of the words.
- **"Treasure card" versus "equipment card".** Defined in §2.5, again in bold in §4.1, and in the glossary, in order to say that an ember card is a treasure card that is not an equipment card. No rule turns on the distinction that "ember card" does not already carry. Use "card" or "equipment card" and drop the taxonomy.
- **Upgrade examples.** "The Chloranthy Ring fills one upgrade slot, and one upgrade slot remains free." An example that restates the sentence above it with a card name. Both §4.2 examples and the §4.1 example (18 is less than 31) can go; the catalyst example in §4.3 earns about half its length.

---

## Chapter 05 — Tiles and Nodes

### Section table

| § | source words | final words | words it needs | main excess |
|---|---|---|---|---|
| intro | 0 | 60 | 0 | V: flavour and contents |
| 5.1 Tiles and Nodes | 183 | 460 | 230 | A: walls, tile orientation, route joins; D: "exactly as a basic node is", "nodes on different tiles are not adjacent" |
| 5.2 Movement | 38 | 278 | 75 | A: two defined terms ("Move", "Valid node") and a seven-pointer paragraph |
| 5.3 Node Model Limits | 157 | 235 | 130 | E: a two-scene example (77 words) for a rule the author illustrated in a clause |
| 5.4 Range | 70 | 299 | 120 | D: "a maximum, never a minimum", "never blocked"; R: where ranges are printed; E 75 |
| 5.5 Terrain | 550 | 1,001 | 400 | V: traps (164 to 400 words); R: "stays on its node" said five times; A: Pillars sub-section restating §17.3 |
| **Chapter** | **998** | **2,333** | **955** | |

Note on §5.5: about 170 words of the source's gravestone text (the scry procedure) moved to §7.5 and the event-card scry was cut (Gate 1 OQ-06), so the like-for-like source figure for what remains is about 380 words against 1,001.

### Added rules

- §5.1 · "The edge of every tile is a wall"; nodes separated by a wall are not adjacent · CH-05-004, CH-05-008 (A-085, A-082) · **A1** · Pushes and range need it. One sentence. The final text takes five across two paragraphs.
- §5.1 · "A tile's orientation is fixed when the tile is placed, and the tile is neither rotated nor moved until the tiles are next laid out for setup" · CH-05-004 · **A3** (D) · Nobody rotates a tile mid-game.
- §5.1 · "a tile that merely lies beside another is not joined to it" · CH-05-042 (VA-006) · **A3** · A verification pass patching a consequence of §6.5's route rule into a definition.
- §5.1 · Primary and secondary spawn and terrain nodes · CH-05-038 (combat-E09) · **A1**, and it is the right length (two sentences).
- §5.1 · Entry node redefined as "a basic node along the tile edge that holds the doorway through which the characters entered" · CH-05-006, CH-05-037 (combat-E05) · **A2** · The correction is sound (the author's "adjacent to doorways" is loose). It could read: "the basic nodes along the edge by which the characters entered".
- §5.1 · "A spawn node or terrain node that holds no enemy or terrain is entered, left, and counted for range exactly as a basic node is." · CH-05-008 · **A3** (D).
- §5.2 · **Move** as a defined term that excludes dodge movement and pushes ("are not moves; a rule that treats them differently names them") · CH-05-009 (C-086) · **A4** · See below. This definition later produced a bug (a dodge onto a trap did not trigger it), fixed by CH-05-034 and re-fixed by CH-05-039 (combat-E10).
- §5.2 · **Valid node** as a defined term, "by a given form of movement" · CH-05-010 (A-085, A-086) · **A2** · One sentence: a model with no node it may enter stays where it is.
- §5.2 · "no model may pass through a doorway" during an encounter · CH-05-011 (C-088) · **A1**, one clause.
- §5.3 · Summons count as characters and invaders as enemies for the push · sweep under CH-05-013 · **A2**, belongs in §12 ("a summon is treated as a character").
- §5.4 · "counted along the shortest chain of adjacent nodes"; "Range is never blocked … A wall blocks range only because the nodes on either side of it are not adjacent" · CH-05-016 (A-082) · **A2** · One sentence, not a paragraph that says "never blocked" and then how a wall blocks it.
- §5.4 · "Range is a maximum, never a minimum … except where its own rules say otherwise (for example the shaft icon …)" · CH-05-015 sweep · **A3** (D) · The author's "maximum range" and "(or closer)" already say it.
- §5.5 · One scry "for each gravestone on its tile" (author: one scry for the encounter) · CH-05-036 (combat-E01, mechanical change) · changed rule, not bloat · The author should confirm the change; it costs no words.
- §5.5 · Trap token content and resolution: blank or dodge difficulty and damage; each character chooses to suffer or dodge; "not an attack … cannot be blocked or resisted" · CH-05-027 (A-083, D-009), CH-05-035 · **A1** · The source said "resolve its effect" and never said what the effect is. Needed, at about 45 words.
- §5.5 · Traps affect characters only (author: "all models on that node") · CH-05-027 (D-009) · changed rule · Stated twice in one sentence ("Only characters trigger traps, and only characters are affected by them; enemies, bosses, and phantoms neither trigger traps nor suffer their damage").
- §5.5 · "The dodge follows every rule in §9.5, including the movement that follows a successful dodge." · CH-05-034, CH-05-039 (combat-E10) · **A4** · A character who dodges a trap is moved off the node, possibly onto the next face-down trap. See below.
- §5.5 · "turned face up at once, before anything else is resolved" · CH-05-034 · **A3** (D).
- §5.5 · Trap exclusion re-keyed from "a tile edge adjacent to another tile" to "a tile edge whose doorway is part of the route (see §6.5)" · CH-05-040 (lead-E01, mechanical change) · **A2** · "The edges by which the party enters and leaves" says it without the route concept.
- §5.5 · "Trap tokens are not dealt to the same tile again when its encounter is reset." · CH-05-029 · **A3** (R) · Already said: "thereafter stay on the tile".
- §5.5 · Barrel tokens and barrel models handled separately ("turn the token to its destroyed side, or remove a barrel model … return each removed barrel model to its terrain node") · CH-05-024 · **A2** · "The barrel is destroyed and removed; it is put back when the encounter is reset."
- §5.5 · Pillars sub-section · CH-05-030 (CMP-0012(f)), CH-05-041 (boss-E45), CH-05-044 (VA-008) · **A3 here** · Three entries to keep 85 words in step with §17.3, which owns every word of it and is cited three times in two paragraphs.

### Worst passages

**1. §5.2, Movement, last four paragraphs (245 words).**

> "**Move.** Any change of node that a model makes by the *Walk* or *Run* minor action (see §10.2), by a *shift* icon (see §10.3, Shift), or by an enemy or boss movement icon (see §9.2; §16.2). The movement that follows a successful *dodge* (see §9.5) and the forced movement of a *push* (see §8.4) are not moves; a rule that treats them differently names them. **Valid node.** A node that a model may enter by a given form of movement: an adjacent node that no wall separates from the model's node and that holds no *terrain* blocking that form of entry (see §5.5). A model may move, dodge, or be pushed only into a valid node. If no valid node exists for a move, a dodge, or a push, the model stays on its node. A node at its *node model limit* is a valid node; a model that enters it displaces another model as §5.3 describes. … The stamina cost and the limits of each form of movement are stated with that form (see §10.2 for Walk and Run; §10.3, Shift; §9.2 for enemy movement; §16.2 for boss movement; §9.5 for the dodge; §8.4 for pushes)."

Source (38 words): "During encounters, each model must always occupy a single node. When a character moves, they place their model on an adjacent node. An adjacent node is any node located directly next to another node: horizontally, vertically, or diagonally."

Cut version (42 words):

> A model moves one node at a time, from its node to an adjacent node. A model that has no node it may enter stays where it is. During an encounter, no model leaves the tile on which the encounter is fought.

**2. §5.5, Traps, resolution (185 words over three paragraphs).**

> "Traps do not block movement, dodging, or pushes. When a character enters a node holding a face-down trap token, whether by a *move*, by the movement that follows a successful *dodge*, or by a *push*, the token is turned face up at once, before anything else is resolved. If the token is blank, nothing happens. Otherwise each character on that node must either suffer the damage shown or attempt to dodge it as an attack with the dodge difficulty shown (see §9.5); each player chooses for their own character. The dodge follows every rule in §9.5, including the movement that follows a successful dodge. If the dodge fails, the character suffers the damage shown. Trap damage is not an attack, and it cannot be blocked or resisted. A face-up trap token has no further effect during that encounter. Only characters trigger traps, and only characters are affected by them; enemies, bosses, and phantoms neither trigger traps nor suffer their damage. … Trap tokens are not dealt to the same tile again when its encounter is reset."

Source: "Traps do not affect models' movement. When a character is pushed onto or moves into a node containing a face-down trap token, flip the token face-up and resolve its effect on all models on that node."

Cut version (64 words):

> Traps do not block movement. When a character enters a node that holds a face-down trap token, the token is turned face up. A blank token does nothing. Otherwise each character on the node either dodges against the difficulty shown or suffers the damage shown, which cannot be blocked or resisted. Only characters spring traps or suffer them. A face-up trap does nothing more.

**3. §5.4, Range, paragraphs three to five (115 words).**

> "Range is a maximum, never a minimum: an attack or effect with range 2 reaches models at range 0, 1, or 2, except where its own rules say otherwise (for example the *shaft* icon, see §10.3, Shaft). Range is never blocked. *Terrain*, *trap tokens*, and other models on the nodes between two models do not block range and do not lengthen it. A wall blocks range only because the nodes on either side of it are not adjacent, so the chain of nodes is counted around the wall. The range of a character's attack is printed on the equipment card or on the attack option (see §10.3, Range). The range of an enemy's attacks is printed on its data card (see §9.3), and a boss's range on each of its behaviour cards (see §16.3)."

Source: "Range 1 means the models must be on adjacent nodes (or closer)."

Cut version (23 words):

> Terrain and models do not block range. Range is counted around a wall, because nodes on either side of it are not adjacent.

### Unintuitive or over-engineered

- **"Move" does not include all movement.** A model that dodges "moves to an adjacent node" by "the movement that follows a successful dodge", which "is not a move". A player has to hold three words (move, dodge, push) and a fourth concept (entering) and remember which terrain rule names which. The definition was written so that "every terrain rule can use one verb", and every terrain rule still lists "move, dodge, or be pushed". Simpler, and what the author did: no definition; each terrain rule says what it blocks. "No model may enter a gravestone node. A model may enter a barrel node only by a dodge or a push, which destroys the barrel." Nothing is lost, and the trap bug (CH-05-034) cannot occur.
- **"Valid node … by a given form of movement".** A term whose meaning changes with the kind of movement is a lookup every time it appears (it appears in §5.3, §8.4, §9.5). "A node the model may enter" is plain English and needs no entry.
- **Dodging a trap moves the character.** By the final text a successful trap dodge carries "the movement that follows a successful dodge", so the character leaves the node, may enter a second trapped node, and dodges again; and since the choice is to "suffer the damage or attempt to dodge", standing still means taking the damage. A new player will not guess this. Simpler: a trap dodge is the roll alone, with no movement. What is lost: the trap as a forced-movement hazard, which nothing in the source asks for.
- **Which basic nodes get no trap.** "Except the basic nodes along a tile edge whose doorway is part of the route (see §6.5)." The players must know the route concept to deal tokens. "Except the nodes along the edges by which the party enters and leaves the tile" is the same rule in table language.
- **Every terrain kind ends with a bonfire sentence.** The section opens by saying terrain stays on its nodes through a reset, and "what else happens … is stated under that kind"; the gravestone and chest entries then state that nothing else happens. Keep the general sentence and the two exceptions (barrels are restored, traps are turned face down).
- **Pillars in the terrain chapter.** A player fighting the Asylum Demon reads §17.3. A player not fighting it never needs pillars. The sub-section serves neither.

---

## Chapter 06 — Setup

### Section table

| § | source words | final words | words it needs | main excess |
|---|---|---|---|---|
| intro | 0 | 55 | 15 | V: flavour; keep the campaign pointer |
| 6.1 Character Setup | 92 | 194 | 105 | X 11; R: what the character count scales |
| 6.2 Treasure Deck Setup | 442 | 724 | 260 | R: each deck's contents stated three times (types, deck paragraphs, building steps); three excluded card kinds named three times |
| 6.3 Shop Setup | 142 | 521 | 230 | A: stocking categories (a second card taxonomy) and a draw loop; R: "no ember cards added" three times |
| 6.4 Bonfire Setup | 55 | 114 | 65 | E: an example of six minus three |
| 6.5 Encounter Setup | 393 | 923 | 480 | V: the three-sentence "optional rule" formula, three times; R: an Optional Rules list of seven pointers; A: free-form chain |
| 6.6 Setup After the Mini-Boss | 226 | 419 | 230 | R: nineteen steps, twelve of them §6.5 again; X 19 |
| 6.7 Setup After the Main-Boss | 263 | 813 | 330 | A: Level 4 Encounters sub-section (230 words); R: campaign and boss-encounter rules; X 30 |
| **Chapter** | **1,613** | **3,763** | **1,715** | |

The source figure includes about 60 words of event-card steps that were cut (Gate 1 OQ-06). The author's §6.2 already said the tier rules twice (once by type, once by deck); the final text added a third telling.

### Added rules

- §6.2 · Ember cards, invader treasure cards and Titanite Scale cards "are of none of the six types and enter neither deck", restated in the Common treasure definition and in step 1 of the procedure · CH-06-073, CH-06-074, CH-06-075 (VA-010, VA-011, VA-012) · **A2** · Three verification findings, each patching the same exclusion into a different paragraph, because the deck contents are stated in three places. State the contents once and the exclusion once.
- §6.2 · "Return the starting equipment cards that are not equipped to the game box." · CH-06-009 · **A3**, a clause at most.
- §6.2 · Appendix B cards "added or amended … before the decks are built" · CH-06-063 (core-E28) · **A1**, one sentence, as written.
- §6.3 · Stocking Categories: five definitions, "a treasure card belongs to the first of the following categories that describes it" · CH-06-012 (A-069, B-022, D-006) · **A2** · §4.1 Card Types defines the same five kinds in a different order and different words. One list, in §4.1, and the shop cites it.
- §6.3 · Stocking as a five-step draw loop, "A category still unfilled when the deck is exhausted stays short" · CH-06-013 (B-023) · **A2** · The author: "Draw tier one treasure cards one at a time to stock tier one shop … Reshuffle extra treasures back."
- §6.3 · Step 4.1, a legendary card drawn while stocking is set aside · CH-06-016 (A-076), CH-06-056 · **A1**, as a clause ("a legendary card is never placed in a shop"), not a numbered sub-step with its own follow-up sentence.
- §6.3 · Unsold shop cards go to the bottom of their deck before a restock · CH-06-014 (Gate 1 OQ-27) · author's decision · K.
- §6.5 · Tiles laid "in a single chain … The chain may run straight or turn at any tile, as the table allows" in place of the author's two rows of three (first leg) and straight line (second leg) · CH-06-057, CH-06-058, CH-06-059 (core-E05, core-E06, core-E07) · **A2** · A fair loosening, but it introduced "the route" as a concept and five follow-on patches: §5.1 (VA-006), §5.5 traps (lead-E01), §6.5 levels (VA-014), §6.6 step 19 (VA-016), and step 4's "a doorway that faces neither of those tiles is not used". "Lay the tiles in a chain from the bonfire tile to the boss tile, doorway to doorway" is the whole rule.
- §6.5 · Fog gate placed at first setup · CH-06-027 (C-080, D-015) · **A1** · The source said "place the fog-gate as before" with no before.
- §6.5 · Behaviour deck built at setup and placed on the boss tile · CH-06-028 (A-043) · **A1** · The boss-behaviour scry needs a deck. One step.
- §6.5 · "Keep the rest of each encounter deck face down beside the bonfire tile." · CH-06-064 (core-E29) · **A1**, one clause.
- §6.5 · Step 5, invader tokens placed "if invaders are in play and any character is embered" · CH-06-034, CH-06-066 (phantom-E14) · **A3** · No character can be embered at the first setup: ember tokens start beside the dashboard and ember cards start in the shop. The step can never apply where it stands. §12.2 owns it.
- §6.5 · "When the Asylum Demon is the mini-boss, its expansion's game board takes the place of the mini-boss tile throughout this setup" · CH-06-070 (lead-E15) · **A3 here** · One boss's exception inside the general procedure. §17.3.
- §6.5 · A set with no Level 1 to 3 cards uses the core set's · CH-06-080 (VA-015, mechanical change) · **A1**, but it is the same single boss; it belongs in §17.3.
- §6.5 · "X is an optional rule. It requires … The party decides during setup whether X is in play", three times, and an Optional Rules list of seven pointers · CH-06-034, CH-06-035, CH-06-042 (C-124) · **A3** · A house formula applied mechanically. The author: "Players may now decide if they wish …".
- §6.7 · Level 4 Encounters sub-section: bold definition, four entry nodes, "the card is followed as printed", soul reward, treasure reward, redraw for an unowned set, "cleared is not fought again", "failed resets as any other", two campaign pointers · CH-06-047 (CMP-0023), CH-06-068 (lead-E07) · **A2** · Two real rules (the four entry nodes; the redraw). The rest says a Level 4 encounter is an encounter.
- §6.7 · The Level 4 treasure is one of the mega-boss's boss treasure cards · CH-06-045 (CMP-0012(d)) · **A1** · The source's "mega-boss Items" was undefined. "No tier two treasure cards are dealt to the game board" is defensive.
- §6.7 · Mega-boss permadeath replaced by ordinary death and hollowing · CH-06-049 (Gate 1 OQ-14) · author's decision · K, one sentence.
- §6.1 · Lone character may spend the six souls before leaving the bonfire · lead-E10, withdrawn by lead-E22 (CH-06-069, CH-06-071) · no net text; noted as an instance of rulings generating rulings.

### Worst passages

**1. §6.2, the deck contents told three times (about 480 of the section's 724 words).** The third telling:

> "The tier one treasure deck holds every common treasure card and every class-specific treasure card whose stat requirements are all below 25. It holds no starting equipment, ember cards, transposed treasure, legendary treasure, or boss treasure. … The tier two treasure deck holds every common treasure card and every class-specific treasure card with at least one stat requirement of 25 or more, and every transposed treasure card. It holds no starting equipment, ember cards, or boss treasure. … 1. Set aside every boss treasure card, every legendary treasure card, every ember card, every *invader*'s treasure card, every Titanite Scale card, and every starting equipment card that is not equipped. … 3. Sort the remaining treasure cards into two piles: cards whose stat requirements are all below 25, and cards with at least one stat requirement of 25 or more. 4. Add every transposed treasure card to the second pile."

Cut version (one table and 27 words, about 110 in all):

> | Treasure | Mark | Deck |
> |---|---|---|
> | Starting equipment | class icon | none; equipped at setup |
> | Common | none | tier one; tier two if any stat requirement is 25 or more |
> | Class-specific | white class emblem | as common |
> | Transposed | blue light | tier two |
> | Legendary | orange light beneath a chest | none; five join the tier two deck when the tier two shop is first stocked |
> | Boss | boss silhouette | none; kept with its boss |
>
> Ember cards, invader treasure cards, and Titanite Scale cards enter neither deck. Shuffle each deck. Treasure from every expansion owned is included, amended as Appendix B states.

**2. §6.3, Stocking Categories and Stocking at the Start of the Game (225 words).**

> "Each shop is stocked by category: three weapons, three armour cards, two shields, two upgrades, and two spells. For stocking, a treasure card belongs to the first of the following categories that describes it (see §4.1). - An upgrade is a card with the weapon-upgrade icon … - A weapon is any other card that is equipped in a weapon slot, including *catalysts* and throwable cards. … 1. Draw one card from the tier one treasure deck. 2. If the card's category is not yet full, place it face up in the tier one shop; otherwise set it aside. 3. Repeat steps 1 and 2 until every category is full or the deck is exhausted. A category still unfilled when the deck is exhausted stays short. 4. Shuffle the set-aside cards back into the tier one treasure deck. 5. Add one *ember card* per character …"

Source: "Draw tier one treasure cards one at a time to stock tier one shop: 3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells. Add ember cards equal to the number of characters. Reshuffle extra treasures back into the tier one treasure deck."

Cut version (80 words):

> A shop holds three weapons, three armour cards, two shields, two upgrades, and two spells (see §4.1). Cards are drawn from the deck one at a time; a card of a kind still wanted is placed face up in the shop, and any other is set aside. When the shop is full, the cards set aside are shuffled back into the deck. At the start of the game, one ember card per character is added to the tier one shop.

**3. §6.7, Level 4 Encounters (230 words).**

> "**Level 4 encounter.** The single encounter fought on the Level 4 encounter side of a mega-boss game board, after the main-boss is defeated and before the mega-boss encounter. A Level 4 encounter is set up and fought as any other encounter (see §7.5), with the following differences. All four basic nodes along the wall beside the doorway are *entry nodes*. The encounter card places more enemies, *terrain*, and *trap tokens* than a Level 1 to 3 card, and the card is followed as printed. The encounter's soul reward is the Level 4 reward (see §7.6). Its treasure reward is the single mega-boss treasure card dealt to the game board, which is awarded when the encounter is *cleared* in the same way as a chest's treasure card (see §7.7). In campaign play … A Level 4 encounter that is cleared is not fought again and does not reset when the characters rest at the bonfire. A Level 4 encounter that is *failed* resets as any other encounter does (see §11.2). In campaign play, …"

Source: "Characters then attempt to clear the Level 4 encounter as they have with previous encounters."

Cut version (55 words):

> The Level 4 encounter is fought as any other encounter. The four basic nodes along the wall beside the doorway are its entry nodes, and its treasure reward is the mega-boss treasure card dealt to the board. If its card calls for a set the party does not own, another is dealt in its place.

### Unintuitive or over-engineered

- **Two taxonomies of the same cards.** §4.1 lists weapon, shield, spell, armour, upgrade; §6.3 lists upgrade, spell, shield, armour, weapon with a first-match rule and slightly different definitions (a shield "shows block or resist dice" in one, "shows a block or resist value" in the other). A player sorting cards for the shop will check both. One list.
- **Setup after the mini-boss as nineteen steps.** The table is mid-game and the checklist is longer than the opening setup. Twelve steps repeat §6.5. Simpler: "Repeat Encounter Setup for the main-boss, with these changes: the same four tiles are flipped and shuffled; the two boss tiles are joined; tier two treasure is dealt; the shops are restocked; one spark is added; the party rests at the bonfire at no cost." Nothing is lost.
- **The free-form chain and "the route".** The author's two layouts can be pictured at once. "A single chain … may run straight or turn at any tile" needs the reader to work out which doorways are "used", which tile is "first", and which edges take no traps. If the freedom is wanted, give it in one sentence and show the author's two layouts as the diagrams.
- **The optional-rule formula.** "Mixed encounter decks are an optional rule. They require at least one expansion that supplies encounter cards. The party decides during setup whether mixed encounter decks are in play. When they are in play, …" Four sentences where "The party may instead shuffle together the encounter cards of every set it owns" does the work. The same goes for "Random boss selection … requires no expansion."
- **A setup step that cannot happen.** §6.5 Encounter Cards step 5 asks whether any character is embered before the first encounter has been fought.
- **§6.7 opens by saying what happens when its subject is absent.** "If no mega-boss is in play, the main-boss is the final boss, and its defeat wins the game (see §7.1)." That is §7.1.

---

## Chapter 07 — Gameplay

### Section table

| § | source words | final words | words it needs | main excess |
|---|---|---|---|---|
| intro | 0 | 58 | 0 | V: flavour and contents |
| 7.1 Objective and Loss Conditions | 108 | 177 | 100 | R: PvP timing with its campaign exception; the zero-spark rule said twice in the section |
| 7.2 Death and Hollowing | 168 | 416 | 170 | A: the "lost" state (95 words); G: hollow cube defined for the third time; D: lone character, PvP |
| 7.3 Embering | 80 | 226 | 110 | A: ember card hand-off rule, box disposal; R: boss defeat embers everyone |
| 7.4 Sparks | 40 | 136 | 60 | R: free rest after a boss; D: imported exceptions from §18 |
| 7.5 Encounters | 771 | 1,754 | 800 | R: skip rule said twice, scry trigger three times, zero-spark loss, boss and invader turn rules, Level 4 exception; G: Reset, Scry; X 50 |
| 7.6 Souls | 197 | 545 | 230 | R: dropping said in a bold definition and again in the paragraph under it; D: "not forfeited" twice; E 91 |
| 7.7 Treasure Rewards | 436 | 396 | 210 | R: mimic, lizard, invader, boss and Level 4 rewards restated from their chapters |
| **Chapter** | **1,800** | **3,708** | **1,680** | |

Like-for-like notes: §7.5 took in about 170 words of scry text from the source's Terrain chapter; §7.7 gave about 250 words of mimic bullets to §13. With those moved, §7.5 is roughly 940 source words against 1,754 and §7.7 roughly 190 against 396.

### Added rules

- §7.1 · The players lose "when the characters are required to rest at the bonfire and the spark dial shows zero" · CH-07-002 (A-002, B-012, CMP-0020) · **A1** · Better than the author's wording, which missed the hollow death. It is then said again in §7.1's next sentence but one, in §7.2, in §7.4 and in §7.5 Encounter Recovery.
- §7.2 · Aggro token passes to the highest-threat living character when its holder dies · CH-07-009 (A-013) · **A1**, one line; it is given in §7.2 step 3 and again in §7.5.
- §7.2 · **Lost**: "A hollow character who dies is lost. A lost character is removed from play exactly as any dead character … is not revived by clearing an encounter but only when the characters rest at the bonfire" · CH-07-007 (CMP-0006, A-001) · **A3** · A named state whose every property is that of a dead character in a failed encounter. The author's rule is one clause: if a hollow character dies, the encounter is failed. The term costs this paragraph, a glossary entry, and "dead or lost" wherever "dead" would do.
- §7.2 · "a character who adventures alone is therefore never revived hollow" · CH-07-008 (A-004, optional finding, applied) · **A3** (D).
- §7.2 · Hollow removed "by resting at the bonfire" rather than "by using a spark" · CH-07-006 (A-005) · **A1**, wording only.
- §7.3 · "Return the ember card to the game box. It takes no further part in the game." · CH-07-062 (core-E23) · **A3**.
- §7.3 · A character embered while holding an ember card "must at once give the card to a character who is neither embered nor holding an ember card. If no such character exists, the card is returned to the tier one shop" · CH-07-011 (A-007) · **A4** · A three-branch procedure for a corner made by two other rules (boss defeat embers everyone; one card each). Simpler: "An embered character cannot use an ember card." A card already held stays where it is.
- §7.3 · The ember token stays through a rest, until the character dies · CH-07-013 · **A1**, one sentence.
- §7.4 · Spark gained on a mega-boss's defeat "and the game does not end"; "except when a player leaves the game (see §18.4)" · CH-07-014, CH-07-055, CH-07-069 (VA-017) · **A3 here** · Two exceptions imported from other chapters to protect the sentence "sparks are gained in no other way".
- §7.5 Start · Skip cost of one stamina per skipped encounter, maximum three (author: two each) · CH-07-016 (Gate 1 OQ-10) · author's decision · K, but stated in prose and again as steps 2 and 4.
- §7.5 Start · "The party may skip only if every character has enough free spaces" · CH-07-016 · **A2**, a clause.
- §7.5 Start · Tied threat: the players choose the aggro holder and the turn order, kept for the encounter · CH-07-019 (CMP-0011) · **A1**, one sentence, in place of the author's first player token.
- §7.5 Turn Order · Aggro counted by "the total value of the wound tokens placed and the damage recorded on an invader's health dial" · CH-07-022, CH-07-066 (combat-E32) · **A2** · "Inflicted the most damage" says it.
- §7.5 Resolution · A failed encounter loses its black cube; a first clear is one made "while the treasure cards dealt to its tile at setup still lie on the tile"; "This is so whether or not the encounter card carries a black cube: an encounter that was cleared, later failed, and then cleared again is a repeated clear" · CH-07-025 (CMP-0019, A-055), CH-07-051 (review of PR #2) · **A2** · The first ruling made the cube unreliable as a record of a first clear; the second added a new test and a paragraph to explain the gap. One sentence does both jobs: "Treasure and the full soul reward are given only the first time an encounter is cleared."
- §7.5 Resolution · Several scries "are resolved one at a time" · CH-07-064 (combat-E03) · **A3**.
- §7.5 Resolution · "where a single card was dealt to the tile, award it to the party" · CH-07-057 (core-E15) · **A3 here**; it is the Level 4 rule of §6.7.
- §7.5 Recovery · After recovery the party advances or returns to rest · CH-07-033 (A-063) · **A1**, one sentence.
- §7.6 · Reduced reward of half, rounded down · CH-07-035 (Gate 1 OQ-05) · **A1** · The source named a reduced reward and gave no figure. It is now a bold definition and a table column, and the column needs a correcting sentence (below).
- §7.6 · Dead characters also gain the soul reward · CH-07-029 (A-121, optional finding, applied) · **A1**, a clause; the author said it of treasure.
- §7.6 · Souls dropped earlier are lost if their owner dies again, "souls dropped at the moment of that death remain on the tile" · CH-07-038 (A-003) · **A2** · The author's rule with one clarifying clause. The final text gives the clause twice in one paragraph.
- §7.6 · Summon cost as "the one exception" to spending at the bonfire · CH-07-050 (A-100) · **A3 here**.
- §7.7 · Dealt cards are turned face up and shared out; "if they cannot agree, the character holding the aggro token decides" · CH-07-058 (core-E16) · **A4 as it stands** · For party awards two paragraphs later the card "goes to" the aggro holder. Two tie-breaks for one situation. Use the author's: it goes to the aggro holder.
- §7.7 · Parenthetical list of six kinds of party award · CH-07-067 (phantom-E12) · **A3** · A list that must be extended whenever another chapter adds an award.

### Worst passages

**1. §7.5, Encounter Start: the skip rule in prose, then again as steps (110 words before the steps begin).**

> "The party may skip an encounter whose encounter card carries a black cube (an encounter marked *cleared*). Each character places one *stamina cube* on their *endurance bar* for each encounter skipped since the party last fought an encounter or rested at the bonfire, to a maximum of three. The cubes are placed when the characters enter the next encounter they fight. The party may skip only if every character has enough free spaces on their endurance bar for the required stamina cubes (see §3.4). A skipped encounter is not fought and awards nothing. *Example.* …" followed by "2. If the encounter card carries a black cube, the party may skip the encounter: the characters move on to the next tile and begin again from step 1. … 4. Place one stamina cube on each character's endurance bar for each encounter skipped since the party last fought or rested, to a maximum of three."

Source: "Characters may skip previously cleared encounters at the cost of two stamina cubes placed in the endurance bar of each character."

Cut version: delete the three paragraphs and keep the steps, with the author's example after them.

> 2. If the card carries a black cube, the party may skip the encounter and move on to the next tile.
> 4. Each character places one stamina cube for each encounter just skipped, to a maximum of three.

**2. §7.2, the lost character (95 words).**

> "A hollow character who dies is *lost*. A lost character is removed from play exactly as any dead character: their souls are dropped, their ember token is removed, and their model is placed beside the bonfire tile. When a character becomes lost, the encounter is failed at once (see §7.5, Encounter Resolution) and the characters must rest at the bonfire; if the *spark* dial shows zero, the players lose the game (see §7.1). A lost character is not revived by clearing an encounter but only when the characters rest at the bonfire (see §11.2), and the rest removes their hollow cubes as usual."

Source: "If all characters die before the end of an encounter, or any character with hollow status dies, then the characters are forced to immediately spend one spark and rest at the bonfire."

Cut version (11 words):

> When a hollow character dies, the encounter is failed at once.

**3. §7.6, dropped souls (205 words in a definition and two paragraphs).**

> "**Dropped souls.** Souls placed on an encounter tile by a character who died there or, when an encounter was *failed*, by a living character. When a character dies, all of the souls on their dashboard are dropped on the tile where they died, in a pile separate from any other character's *dropped souls* (see §7.2). When an encounter is failed, every living character also drops all of their souls on that tile (see §7.5, Encounter Resolution). Dropped souls stay on the tile through every *reset*. The souls a character drops at death are not forfeited by that death. Only the character who dropped the souls may reclaim them, and only by surviving an encounter on that tile that ends cleared; … The one exception is the setup that follows the defeat of a boss … A character who is dead or *lost* when the encounter is cleared does not retrieve them. If the character who dropped the souls dies before reclaiming them, the dropped souls are returned to the supply; souls dropped at the moment of that death remain on the tile."

Source: "When a character dies, drop all of the souls from their character dashboard onto the encounter tile they died on separate from other characters' dropped souls. The character who dropped them … can reclaim dropped souls. Dropped souls are lost forever if the character who dropped them dies before reclaiming the souls."

Cut version (63 words):

> A character who dies drops all their souls on the tile, in a pile of their own. When an encounter is failed, every living character does the same. Dropped souls stay on the tile through every reset. A character reclaims their own dropped souls by surviving a cleared encounter on that tile. If the character dies again first, the earlier pile is lost.

### Unintuitive or over-engineered

- **"Lost".** A new player meets dead, hollow, lost and embered as four states. Lost is dead. Remove the word.
- **Two records of "cleared".** The black cube says an encounter may be skipped; the treasure cards lying on the tile say whether a clear is the first. They agree until an encounter is cleared, failed and cleared again, and a paragraph exists for that case alone. Simpler: the cube stays once placed and means "cleared before" (reduced souls, no treasure); a failed encounter cannot be skipped until it is cleared again, which the face-down card already shows at the tile. What is lost: nothing the author asked for.
- **The soul table's second column.** Rows are labelled "Level 1 encounter and standard invader" and "Level 4 encounter and bosses", each with a reduced figure, and the next sentence says invaders and bosses have no reduced reward. Drop the column; "half, rounded down" is the rule.
- **Two tie-breaks for a treasure card.** The aggro holder "decides" for encounter treasure and "receives" party treasure. One rule.
- **The ember hand-off.** See Added rules. A player holding a spare ember card when the boss falls must find who is "neither embered nor holding an ember card" at a moment when everyone has just been embered, so the card always returns to the shop. The rule has one outcome and three branches.
- **The losing condition in four places.** §7.1, §7.2, §7.4 and §7.5 Encounter Recovery each say that a forced rest at zero sparks loses the game, in different words. A reader comparing them will ask whether they differ. §7.1 only.
- **The scry trigger in three places.** §5.5 Gravestones, §7.5 Resolution step 5, and the paragraph under the Scry definition. Step 5 and the three bullets are enough.
- **Encounter Turn Order as a digest.** Half the sub-section is other chapters: the skull icon (§9.3), invader turns (§12.2), boss alternation (§16.1), boss aggro (§16.4). The author's four numbered lines are the rule.

---

## Totals — core group (chapters 02 to 07)

| Chapter | source words | final words | words needed |
|---|---|---|---|
| 02 Game Components | 749 | 2,452 | 1,302 |
| 03 Characters | 1,070 | 2,085 | 965 |
| 04 Equipment | 822 | 1,976 | 880 |
| 05 Tiles and Nodes | 998 | 2,333 | 955 |
| 06 Setup | 1,613 | 3,763 | 1,715 |
| 07 Gameplay | 1,800 | 3,708 | 1,680 |
| **Group** | **7,052** | **16,317** | **7,497** |

The final text is 2.3 times the source. The words needed are 6 per cent above the source: the legitimate additions (die faces, expansion component lists, trap resolution, shield definition, fog gate, reduced reward, the zero-spark loss rule, threat ties) come to about 1,100 words and are largely paid for by tightening the author's own repetitions and by the event cards cut at Gate 1.

Excess: 16,317 − 7,497 = **8,820 words**. Split by class (X and E are counted; the others are my estimates from the section-by-section reading, to the nearest 10):

| Class | words | % of excess |
|---|---|---|
| R restated | 3,230 | 37 |
| A added rules (the words beyond what an A1 needs, plus all A3 and A4) | 2,180 | 25 |
| X cross-reference clutter (405 pointers, 1,004 words; about 850 removable) | 850 | 10 |
| D defensive | 800 | 9 |
| V verbose (includes 285 words of chapter intros) | 770 | 9 |
| E examples (14 examples, 882 words; about 220 worth keeping) | 660 | 7 |
| G glossary-in-chapter | 330 | 4 |
| **Total** | **8,820** | **100** |

## How it happened

1. **"One owning section, cite it everywhere else" became "summarise it everywhere else".** The author's forward references ("explained in detail later") were replaced by a one-sentence digest of the owning rule plus a pointer, in every section that touches it. Each chapter became a précis of the others.
   - §4.1 Stat Requirements: three paragraphs summarising treasure tiers, scaling, the Attack action, two-handed rerolls and defence rolls (CH-04-007).
   - §2.3 Bosses: tiles, boards, Level 4, health dials and Ornstein & Smough, in a component list (CH-02-010, CH-02-047, CH-02-044). Also §3.5 Ember, four pointers and no rule (CH-03-028).

2. **Keep-in-step cascades.** Once a rule lives in several places, every later ruling has to be mirrored in each, and each mirror picks up the qualifiers.
   - The hollow marker: added as a component (CH-02-019), removed as a component (CH-02-030, core-E01), redefined as a spare white cube with a fallback (CH-02-031, core-E02), then echoed into §3.4 (CH-03-015), §6.1 (CH-06-062, core-E20) and §7.2 (CH-07-056, core-E03). The author's text: "a marker such as white cubes".
   - Invader tokens: §2.9 (CH-02-027, then CH-02-042 phantom-E16), §6.5 step 5 (CH-06-066 phantom-E14), §6.6 step 16 (CH-06-067 phantom-E15), all restating §12.2.

3. **Defined-term machinery.** To make the prose deterministic the edit minted headword terms, and the terms needed rules of their own, produced bugs, or outlived their purpose.
   - **Move** and **Valid node** (§5.2, CH-05-009, CH-05-010): the definition of "move" excluded dodge movement, which broke traps (fixed by CH-05-034, corrected again by CH-05-039 combat-E10).
   - **Left weapon slot** and **right weapon slot** (§3.2, CH-03-005, CH-03-031 CMP-0003): made for the parry, orphaned when combat-E22 let either slot parry (CH-03-036). Also **lost** (§7.2, CH-07-007 CMP-0006), a name for "dead".

4. **Silence answered with a sub-section, not a sentence.** Where the source had a gap, the completion wrote out a full procedure with its own definitions and edge cases.
   - Level 4 Encounters, 230 words for two rules (§6.7, CH-06-047 CMP-0023).
   - Stocking Categories and the five-step draw loop for the author's three lines (§6.3, CH-06-012, CH-06-013). Also the trap procedure, 164 to 400 words (§5.5, CH-05-027, CH-05-034, CH-05-035).

5. **Verification passes that only ever add.** Each consistency pass found that two restatements disagreed and reconciled them by adding a clause or an exception to one, never by deleting the restatement. Edge-case findings marked optional were applied as defensive sentences.
   - §6.2: three findings (VA-010, VA-011, VA-012; CH-06-073 to 075) each inserting the same three excluded card kinds into a different paragraph.
   - The free-form tile chain (core-E05, CH-06-057) followed by VA-006 (§5.1), VA-014 (§6.5), VA-016 (§6.6), VA-018 (§7.5) and lead-E01 (§5.5 traps), each rewording "adjacent to the bonfire" as "the route". Also "a character who adventures alone is therefore never revived hollow" (CH-07-008, A-004 optional).

6. **House templates applied to every chapter.** The editorial brief asked for a chapter introduction, worked examples, full-sentence lists and a fixed form for optional rules, and each was applied whether or not the material needed it.
   - Six flavour introductions, 323 words (CH-03-001 and its siblings); examples that restate the sentence above them (§4.2 Chloranthy Ring, CH-04-016; §6.4 six minus three, CH-06-021).
   - The optional-rule formula, three sentences each for random bosses, mixed decks and the mega-boss, plus a list of seven pointers (§6.5, §6.7; CH-06-034, CH-06-035, CH-06-042, finding C-124). Also the author's numbered anatomy lists turned into bold-headed bullets with a rule and a pointer each (CH-03-002, CH-04-004).

## Ten cuts

In order of words saved for least loss. Savings are approximate.

1. **Chapter 2 back to a packing list (about 1,150 words).** Delete every sentence that explains what a component does. List each component once, tagged with its set, as the author did; keep the die face table and the expansion lists.
2. **§7.5 said once (about 950).** Delete the prose skip rule (the steps have it), the boss, invader and skull-icon digests in Turn Order, the "whether or not" paragraph, the Reset definition and Level 4 exception, the repeated scry trigger, and the zero-spark and free-rest restatements in Recovery.
3. **Chapter 3 pointers and scaffolding (about 700).** Delete the Threat definition, left and right weapon slots, the shield, spell and two-handed sentences in §3.2, the tier-four and scaling paragraphs of §3.3, the Ember sub-section, the three "not removed" sentences, and three of the four examples.
4. **§5.5 Terrain (about 600).** Traps to about 190 words; delete Pillars, the per-kind bonfire sentences that say nothing happens, and two of the three introductory paragraphs.
5. **§7.6 and §7.2 (about 560).** Dropped souls as five sentences; drop the reduced-reward column and its correcting sentence; halve the example; remove "lost", the hollow cube definition and the lone-character and PvP sentences.
6. **§4.1 Equipment Cards (about 490).** The author's anatomy list keyed to a picture; one sentence defining a shield; delete Card Types, the three digest paragraphs and the example; keep the Appendix A sentence on its own line.
7. **§6.7 (about 480).** Level 4 Encounters to about 55 words; delete the opening optional-rule formula, the campaign pointers and the closing paragraph of restatements.
8. **§6.3 and §6.6 (about 480).** Shop stocking as one paragraph citing §4.1 for the kinds; Setup After the Mini-Boss as "repeat §6.5 with these six changes".
9. **§6.2 as one table (about 460).** Six rows and two sentences in place of type definitions, deck paragraphs and a building procedure.
10. **§6.5 (about 440).** Delete the optional-rule formula and the Optional Rules list, the invader step that cannot apply, and the Asylum Demon exceptions (to §17.3); state the tile chain in one sentence.

Together these remove about 6,300 of the 8,820 excess words. Most of the remainder is §5.1 to §5.4 (the Move and Valid node definitions, range paragraphs, examples), §4.2 to §4.4 (Titanite, spell hands, embers), the six chapter introductions, and the pointers left standing once the sentences around them are gone.
