# Bloat audit: campaign group (chapters 17, 18, 19)

Word figures are counted with `len(text.split())` on the body of each section (headings excluded). "Needs" is the auditor's estimate of the words the section requires. Booklet figures are counted on the booklet pages that carry the boss's own rules (contents list, "Starting the … encounter", "Custom Game Elements") and include some card-art debris from the PDF extraction, so they are upper bounds.

---

## Chapter 17: Boss Special Rules

Author's source: 212 words (two bosses). Final: 8,963 words (30 bosses). Needs: about 3,950.

### 1. Section table

| § | Source | Final | Needs | Main excess |
|---|---|---|---|---|
| Intro | 0 | 53 | 20 | flavour paragraph |
| 17.1 Rules Common to Several Bosses | 0 | 1,133 | 270 | A: Twin Gargoyles procedure (516), several-models framework (423) |
| 17.2 Core Set (Ornstein & Smough) | 0 | 649 | 230 | R of §17.1 and §15.5; example; setup prose |
| 17.3 Asylum Demon and Stray Demon | 198 | 699 | 230 | V and D: four-step procedure, negatives, example |
| 17.4 Darkroot | 0 | 206 | 110 | V: procedure for a one-sentence heat-up |
| 17.5 Iron Keep | 0 | 98 | 50 | V: same |
| 17.6 Explorers | 0 | 312 | 150 | D; pointer-only mimic entry |
| 17.7 Tomb of Giants | 0 | 38 | 20 | pointer only |
| 17.8 Black Dragon Kalameet | 0 | 645 | 300 | R: components, ability and heat-up restate setup; example |
| 17.9 Executioner's Chariot | 0 | 1,365 | 650 | V: three procedures of eight, eight and five steps; A: Raise Skeleton |
| 17.10 Bosses of Other Expansions (nine entries) | 0 | 3,765 | 1,920 | R: components lists, template sentences, the node-attack procedure written three more times |
| **Total** | **212** | **8,963** | **3,950** | |

Cross-references: 123 "(see …)" parentheticals, 338 words, plus about 180 words of pointer sentences ("The Level 4 encounter that precedes it and the placing of its game board are stated with the setup rules").

### 2. Is the book longer or shorter than the booklets?

| Boss | Book | Booklet (boss-specific pages) | Book ÷ booklet |
|---|---|---|---|
| Asylum Demon and Stray Demon | 699 | about 290 (the author's source is this text, 198 words) | 2.4 |
| Executioner's Chariot | 1,365 | about 930 | 1.5 |
| Guardian Dragon | 665 | about 495 | 1.3 |
| Black Dragon Kalameet | 645 | about 560 | 1.15 |
| The Four Kings | 670 | about 610 | 1.1 |
| Old Iron King | 644 | about 650 | 1.0 |
| Vordt of the Boreal Valley | 553 | about 620 | 0.9 |

The book is never materially shorter than the official text and is up to 2.4 times longer. That is the wrong result, because the booklet text is itself loose: about a third of it is flavour, generic setup ("place the character models on the entry nodes…") and asides ("Note that players will now need to relearn…"). The book removed all of that and still came out at the same length or longer. What filled the space: a components list per boss, a "Setup" procedure of four to eight numbered steps, a numbered procedure for each special attack, a "Special ability" paragraph that repeats the setup, a "Heat-up" paragraph that says the general rule applies, a worked example, and inline definitions that are also in the glossary. A tight restatement should run at 50 to 60 per cent of the booklet.

### 3. Components and Setup blocks

**Components: delete all of them.** Twelve entries carry a components list (about 520 words in all). Chapter 2 already lists the boss components, including the unusual ones (`- Black Dragon Kalameet only: 8x Strafe cards and 4x Calamity tokens (see §17.8)`, the Chariot's track cards and setup card, the pillar tokens). "1x Data card, 1x Health dial, 2x Mega-boss treasure cards, 4x Level 4 encounter cards, 1x Mega-boss game board" is printed seven times and tells the player nothing they need during the fight. The only component facts with rule value are the card counts by type, and those belong in the deck table below.

**Setup: one table for all mega-bosses.** Every Setup block opens with the same 16-word sentence ("The mega-boss encounter is set up as any mega-boss encounter (see §6.7), with the following differences.") and then spends 60 to 190 words on "shuffle, draw N, return the rest to the box". Nine procedures (about 1,000 words) reduce to this (about 230 words), which also absorbs every "Heat-up" paragraph that only restates the general rule:

| Boss | Behaviour deck at setup | Set aside | Heat-up |
|---|---|---|---|
| Black Dragon Kalameet | 4 of 10 standard, plus Mark of Calamity and Hellfire Blast | Hellfire Barrage; 8 strafe cards as a deck | Shuffle in Hellfire Barrage |
| Executioner's Chariot | Death Race 1 to 4 in order, not shuffled | 4 of 9 standard and 1 of 3 heat-up, shuffled, as the heat-up deck | When no Mage or Skeleton remains (see below) |
| The Four Kings | 4 of 8 standard | Three piles of 4 cards for kings two, three and four | None; royal summons (see below) |
| Gaping Dragon | 3 of 7 standard, 2 Stomach Slam, 1 of 4 heat-up | Crawling Charge, face up; 3 heat-up | Shuffle in 1 heat-up card |
| Guardian Dragon | 5 of 9 standard | 2 Cage Grasp Inferno; 4 Fiery Breath cards as a deck | Shuffle in both Cage Grasp Inferno |
| The Last Giant | 3 of 5 standard and 3 of 5 Arm | Falling Slam; 5 heat-up | Remove the Arm cards; shuffle in Falling Slam and 3 heat-up |
| Manus | 5 of 9 standard | 5 heat-up | 1 heat-up on top of the deck, 1 under the discard pile; no shuffle |
| Old Iron King | 3 of 6 standard and 3 Fire Beam | 3 heat-up; 6 Beam cards as a deck | Shuffle in 1 heat-up; Beam attacks gain +1 attack value and +1 dodge difficulty |
| Vordt | Movement deck: 4 of 6. Attack deck: 3 of 6 | 2 heat-up movement, 2 heat-up attack, Frostbreath | First: 1 heat-up attack card into the attack deck. Second: 1 heat-up movement card into the movement deck. Frostbreath is resolved at each |

(Manus's "5 of 9" is from the booklet; the book's entry says only "built by the general procedure", so the count should be checked against the data card when the table is built.) With the table in place each mega-boss entry is two to five short paragraphs: where the model starts if not the spawn node, the special attack, and anything in the last column marked "see below".

**The node-targeted attack is written four times.** Strafe (seven steps), Inferno (six), Beam (six) and the track card (eight) are one mechanism: if the side deck is empty turn its discard pile over unshuffled; reveal the top card; place the boss on the node the card shows; attack every character on a marked node; discard. Define it once in §17.1 (about 60 words) and give each boss only its differences (Kalameet lands after the attack; the Guardian Dragon perches on a cage node; the Old Iron King pushes models off its node first; the Chariot's attack is physical and pushes). Saving: about 350 words.

### 4. Added rules (class A)

The booklet rules are not on trial. These are the rules the pipeline added on top of the author's source and the booklets.

- §17.1 · "Where a rule in this chapter and a data card disagree, the rule in this chapter governs" · CH-17-003 (CMP-0005, C-081) · **A3** · Delete. It tells a player their card may be wrong without saying where; Appendix B owns card amendments.
- §17.1 Zero Dodge Difficulty · pay one stamina, dodge without rolling, even with no dodge dice; plus two sentences on blocking instead and on equipment that forbids dodging · CH-17-004 (CMP-0005) · **A2** · One sentence; cut the two defensive ones.
- §17.1 Several Boss Models in One Encounter · 423-word generic framework for two bosses (Ornstein & Smough, Four Kings) · CH-17-005 to 009, rewritten by CH-17-053 (boss-E08, which revised Gate 1 OQ-25) · **A2** · About 100 words. Cut "keeps its facing", "Damage inflicted on any of the boss's models is damage inflicted on the boss when the aggro token moves", "No character's movement or attack pushes a boss model", and the weak-arc paragraph (R of §15.6).
- §17.1 Twin Gargoyles · five-step change-over, list of what carries over, list of what is not awarded, PvP sentence, failure paragraph, example; 516 words for the author's two list lines · CH-17-010 to 014 (Gate 1 OQ-25, A-040, D-012) · **A2** · One paragraph of about 80 words (see worst passages).
- §17.2 · Ornstein on the main-boss spawn node, Smough on the mini-boss spawn node; heat-up deferred to the start of the next boss turn; "If the second model is defeated before the heat-up is carried out, the boss is defeated at once" · CH-17-054 (boss-E10) · **A1** for placement, **A3** for the last sentence (it exists only because the heat-up is deferred).
- §17.3 · pillar damage "is not an attack" and cannot be blocked, resisted or dodged; "A magical attack, or an attack that does not show the area icon, destroys no pillar" · CH-17-023 (CMP-0005 "clarified") · **A2** · Keep "which cannot be blocked, resisted, or dodged" as a clause; delete the second sentence (it restates the trigger in the negative).
- §17.3 · "A Wind Up icon printed on any other behaviour card is resolved in the same way"; "Each player decides for their own character"; "every rule that applies to a Run applies to it"; "The characters complete the movement before the next icon…" · CH-17-026, CH-17-027 (CMP-0017) · **A3** · Delete all four. The author's two sentences were complete.
- §17.6 Old Dragonslayer · "shows no heat-up point, and … does not heat up in any other way" · CH-17-059 (boss-E15) · **A3** · Delete.
- §17.6 Pursuer · weak arcs are those of the second card; deck renewed before either card · CH-17-032 · **A2** · Keep the first as a clause; the second is R of §16.1.
- §17.8 · Kalameet lands "facing as it faced before it was removed" · CH-17-037 · **A1** · Keep, five words.
- §17.9 · before the heat-up "each boss turn … is taken by every enemy model", in threat order · CH-17-040 (CMP-0005) · **A4** · See unintuitive rules.
- §17.9 · Raise Skeleton: count models "whose names include the word 'Skeleton'", compare with the count at the start, return one "with no wound tokens" to the nearest spawn node, tie-break, null case; plus a 100-word example · CH-17-043 (CMP-0005) · **A2** · "A Black Hollow Mage that resolves Raise Skeleton returns one killed Skeleton, at full health, to the enemy spawn node nearest to it."
- §17.10 Four Kings · "A royal summons is carried out whether or not the kings placed before it have been defeated" · CH-17-060 (boss-E20) · **A3** · Delete.
- §17.10 Gaping Dragon, Guardian Dragon, Vordt · which card is "the current behaviour card" after Crawling Charge, Bonus Behaviour, and Vordt's two cards; discard order · CH-17-061, 062, 066 · **A2** · One clause each ("the weak arcs are those of the last card drawn"); drop discard order.
- §17.10 Manus · the second heat-up card is "turned as the cards of that pile are turned"; "If the discard pile is empty, the second card starts it" · CH-17-064 (boss-E24) · **A3** · Delete.
- §17.10 Vordt · "The damage prevented is the attack value or the character's defence total, whichever is lower" and "A character who dodges the attack gains no token" · CH-17-066 (boss-E26) · **A2** · The example does this work; keep one or the other, not both.
- §17.10 Crossbreed Priscilla · "Apply the special rules supplied with that expansion" · CH-17-067 (boss-E27) · not bloat but a hole: the one place the chapter sends the reader to another rulebook.

### 5. Worst passages

**(a) §17.1 Twin Gargoyles (516 words).** Source: two lines in a campaign list, "Gargoyle (Mini-Boss) / Gargoyle (Mini-Boss)".

> "When the first Gargoyle's health dial reaches zero, the encounter does not end, and Boss Death is not resolved (see §16.5). 1. Remove the Gargoyle model from the tile and place it on the mini-boss *spawn node*, facing as at the start of a boss encounter (see §15.2). 2. Place any character on that node on the model's base, in an arc chosen by that character's player. 3. Set the health dial … 4. Gather all of the Gargoyle's behaviour cards and build a new behaviour deck (see §15.5). 5. Continue the encounter in the same turn order (see §16.1). The second Gargoyle takes its first turn after the turn of the character who defeated the first. Nothing else changes between the two parts. Each character stays on their node and keeps their *damage cubes*, *stamina cubes*, condition tokens, and used tokens. A character who died stays dead, a *summon* in play stays in play, and the *aggro token* stays with its holder. The characters do not rest at the *bonfire* between the two parts, and no *souls*, no treasure, and no *spark* are awarded. … at that time and not before. …"

As cut (78 words):

> **Twin Gargoyles.** Where a section lists the Gargoyle as fought twice, the two fights are one boss encounter. When the first Gargoyle's health reaches zero, its model returns to the spawn node, its health dial is reset, and a new behaviour deck is built. The fight continues in the same turn order, and nothing else changes. The boss is defeated when the second Gargoyle's health reaches zero. If the encounter is failed at any point, both Gargoyles are fought again.

**(b) §17.3 Setup, Special Ability, Unique Icons (596 words).** Source (198 words): "During the boss encounter setup, place one pillar token on each of the four pillar nodes … Pillars block movement. When the Asylum Demon or Stray Demon makes a physical attack with an *area* icon, check to see if there are any pillar tokens within the affected area. characters within one node range of the pillar token immediately suffer one damage and the stagger condition. Then remove that pillar token … Once a pillar is destroyed, pillar nodes are treated as basic nodes for the remainder of the encounter. When the party rests at the bonfire, return any destroyed pillars…"

Final, in part:

> "When either demon makes a physical *area attack*, that is, a physical attack that shows the area icon …, every pillar within the area of the attack is destroyed before the attack is resolved. A pillar is within the area of the attack if its node is within the attack's *range* of the demon and lies in one of the attack arcs marked on the *behaviour card* (see §16.3). 1. Find every pillar token within the area of the attack. 2. For each such pillar token, deal one damage … 3. Remove each such pillar token … 4. Resolve the area attack … The damage of a destroyed pillar is not an attack, and it cannot be *blocked*, *resisted*, or dodged. One attack may destroy several pillars. A character within range 1 of several destroyed pillars suffers one damage for each of them and holds one stagger token (see §8.5, Stagger). A magical attack, or an attack that does not show the area icon, destroys no pillar."

As cut (146 words, shorter than the author's own text and with the two real gaps closed):

> **Setup.** Both demons are fought on the mega-boss side of the expansion's game board; for the Asylum Demon it takes the place of the mini-boss tile. A pillar token is placed on each of the four pillar nodes. A pillar blocks movement.
>
> **Pillars of Woe.** When either demon makes a physical area attack, each pillar within the attack's range and arcs is destroyed before the attack is resolved. Every character within range 1 of a destroyed pillar suffers one damage, which cannot be blocked, resisted, or dodged, and gains stagger. The token is removed, and its node is a basic node from then on. One attack may destroy several pillars. Destroyed pillars return when the characters rest at the bonfire.
>
> **Wind Up.** When a Wind Up icon is resolved, each character may spend one stamina to move to an adjacent node. The movement counts as a Run.

**(c) §17.1 Several Boss Models in One Encounter (423 words).** No source text; the author's only sentence on the matter was "If a boss model moves onto a node that already contains a boss, the players must push the boss that was on the node first."

> "A character's attack is made against one boss model. The attack is resolved against the block and resist values of that model, its damage lowers that model's health dial, and any condition it inflicts is placed on that model. Damage inflicted on any of the boss's models is damage inflicted on the boss when the aggro token moves (see §16.4). On each boss *turn* one behaviour card is drawn, as for any boss (see §16.1), and every boss model in play acts on it, one model after another, in the order that the boss's entry states. Each model resolves its icons from its own node: its movement, its facing, the *range* of its attack, its attack arcs, and the direction of any push are taken from that model. The target of each icon is determined afresh for each model. …"

As cut (98 words):

> Ornstein & Smough and the Four Kings are each one boss with several models and one behaviour deck. Each model has its own health dial, arcs, and condition tokens, and a character attacks one model at a time. On the boss turn every model in play resolves the drawn card in the order its entry gives, measuring from its own node and facing. A model that moves onto the node of another boss model pushes it to a node the players choose. A model reduced to zero health is removed. The boss is defeated when its entry says so.

### 6. Unintuitive or over-engineered rules

- **The Chariot's turn before the heat-up (§17.9).** "Until the heat-up, each boss *turn* of the encounter (see §16.1) is taken by every enemy model on the game board … One character then takes a turn, and the enemy models take their turns again." A boss turn that is taken by seven models is a contradiction in terms, and the reader has to work out that this is simply the ordinary encounter sequence. Say that: "Until the heat-up the fight is played as an ordinary encounter, and the Chariot takes its turn among the enemies in threat order." Nothing is lost.
- **Heat-up timing is stated differently from entry to entry.** Ornstein & Smough, the Last Giant, Manus and Vordt say "carried out at the start of its next turn … in place of the general ones"; Artorias and the Smelter Demon say "When … health is reduced to or below its heat-up point:" and go straight to steps; the Pursuer says "From the moment the heat-up is carried out". A reader comparing entries will think the timing differs. It does not. State the timing once in §15.5 and never again.
- **Three names for one side deck procedure** (strafe, Inferno, Beam, plus the track card). See section 3. A player who has learned Kalameet has to re-read six steps to find that the Guardian Dragon does the same thing.
- **Wind Up and Overextended.** The same 45-word paragraph appears in §17.3 and under Manus, and the Last Giant points back to §17.3. The author's 36 words, placed once in §17.1, serve all three.
- **Twin Gargoyles step 2**, "Place any character on that node on the model's base, in an arc chosen by that character's player": a new sub-rule for a case the general boss rules already cover.
- **"Special ability" as a compulsory heading.** For Kalameet, the Gaping Dragon, the Guardian Dragon and the Last Giant the ability text only repeats the setup or the heat-up ("Every behaviour deck built for Kalameet includes both signature cards"). A reader looks for a rule and finds none. Print the ability's name in the deck table or drop it.
- **Entries that exist to say there is nothing to say**: §17.2 first paragraph, §17.5 "Sir Alonne has no rules beyond its data card", §17.6 Mimics (40 words pointing to §13), §17.7, Heavy Knight. §17.1 already says "A boss with no entry in this chapter has no rules beyond its data card." Keep that sentence and delete the entries (about 190 words).

---

## Chapter 18: Campaign Play

Author's source: 1,134 words. Final: 4,024 words. Needs: about 1,415.

### 1. Section table

| § | Source | Final | Needs | Main excess |
|---|---|---|---|---|
| Intro | 0 | 42 | 25 | flavour |
| 18.1 Setup (seven sub-headings) | 145 | 1,497 | 520 | A: Section Setup (419), Section Completion (270), Level 4 Encounters and Mega-Bosses (332), all new; R of §6, §15, §17 |
| 18.2 The Fog Gate | 32 | 124 | 40 | R: placement, summon, route after a rest |
| 18.3 Sparks | 105 | 507 | 150 | A: buy-back and its five limits; table; 115-word example |
| 18.4 Adding and Dropping Players | 102 | 460 | 130 | V: two six-step procedures; A: per-tile treasure adjustment; example |
| 18.5 Encounter Rewards | 165 | 227 | 70 | R: the section now says rewards are unchanged, at length |
| 18.6 The Bonfire (costs, shop, price table) | 290 | 505 | 230 | R of §6.3 and §11.4; D |
| 18.7 Bonfire Ascetic | 174 | 374 | 130 | R: tier rule repeated from §18.5; pooling exception; example |
| 18.8 Transposition | 109 | 288 | 120 | V: two numbered procedures; D |
| **Total** | **1,134** | **4,024** | **1,415** | |

Cross-references: 102 "(see …)" parentheticals, 297 words. §18.1 Section Setup alone has 13 in ten bullets.

Repetition inside the chapter: "legendary treasure … only by transposition" is stated four times (§18.1 Campaign Setup, §18.5, §18.6, §18.8); "boss treasure is gained only by defeating bosses" three times (§18.1, §18.5, §18.6); the free rest after a completed section three times (§18.1, §18.3 twice); the pooled-payment exception twice, each pointing at the other (§18.3, §18.7); the tier rule ("every treasure card dealt to an encounter tile or placed beneath a chest … Treasure cards already dealt are not replaced") twice, word for word (§18.5, §18.7).

### 2. Added rules (class A)

- §18.3 · spark maximum is the starting value plus one (source: "The starting number of sparks also serves as the maximum"), with a four-row table · CH-18-014 (B-013; Gate 1 OQ-22) · **A2** · If the author stands by the Gate 1 answer, one clause ("its maximum is one higher") and no table.
- §18.3 · spark buy-back at four souls per character, pooled; one per rest; not at maximum; after the rest's own spark is spent; allowed in a free rest; cannot prevent the loss · CH-18-015, CH-18-045 to 047 (B-013; OQ-22; campaign-E18 to E20) · **A4** · The author wrote "Sparks cannot be purchased or gained otherwise." This reverses it and costs about 250 words with its example and price-table row. Recommend removal; if kept, one sentence: "Once during each rest the party may buy one spark for four souls per character, paid together."
- §18.1 Campaign Setup · no boss selection; optional rules chosen at setup; a mega-boss is not chosen as an optional rule · CH-18-007 (CMP-0008) · **A2** · One sentence: "The bosses are those the campaign lists."
- §18.1 Section Setup · ten bullets: tiles drawn to the section's count; route in listed order; cards by listed level; decks from every required set (campaign-E30); treasure per tile; boss tiles; Twin Gargoyles; fog gate; shop and spark; one invasion per section and the invader token keyed to the ascetic (campaign-E33) · CH-18-008, 051, 053, 057 (CMP-0008, A-048, OQ-28) · **A1** for the first four (the source never said how a section is laid out), **R** for the next five, **A2** for the invader bullet (one clause in §18.7).
- §18.1 Section Completion · a section ending in an encounter is completed when that encounter is first cleared, with a free rest, a restock and no spark · CH-18-009 (CMP-0008, A-048) · **A1** · One sentence.
- §18.1 Section Completion · 80-word paragraph on a boss defeated before its section is completed (rewards, spark, survivors recover, the dead are revived, "the ember token of the boss's defeat keeps a revived character from becoming hollow, so no hollow cube is placed", no setup, no restock, no rest) · CH-18-041, lengthened by CH-18-058 (VB-009) · **A3** · The change log itself says "No published campaign lists two bosses in one section." The one later case (§19.16, Section Five) has its own rule. Keep one sentence: "A boss defeated before the end of its section grants its rewards and spark but no free rest."
- §18.1 Level 4 Encounters and Mega-Bosses · Level 4 encounters use the listed mega-boss's board and cards; no mega-boss treasure card for a Level 4 encounter in a campaign (campaign-E16); two Level 4 encounters share a board; a mega-boss that is not the final boss does not end the campaign · CH-18-010, CH-18-043 (A-049, OQ-14) · **A1** in substance, **A2** in size: 332 words for four facts; about 100.
- §18.1 The Final Boss · definition of the final boss; a campaign ending in an encounter "has no final boss" · CH-18-011 (A-049) · **A2** · "The players win the campaign when its last section is completed."
- §18.1 Player versus Player Encounters · a PvP encounter follows only a boss that completes a section; setup and rest order · CH-18-012, 055, 056 (OQ-15; lead-E02, lead-E03) · **A2** · One sentence, and it belongs in §20.
- §18.2 · "An embered character may call a summon at the fog gate, as in the standard game" · CH-18-013 · **A3** (pure R) · Delete.
- §18.4 · change only on the bonfire tile with no encounter in progress; the new character has no souls; cannot join at zero sparks; party of at most four · CH-18-019, 020, 049 · **A2** · First two are one clause each; the last two follow from the cost and from §1.
- §18.4 · step 6 of each procedure: deal or remove one treasure card on every encounter tile that still holds its cards · CH-18-022 (A-027, A-057) · **A2** · One clause.
- §18.4 · the same rules let a player join or leave a standard game · CH-18-039 (CMP-0003) · **A2** · Fine as one sentence, but it is a standard-game rule sitting in the campaign chapter.
- §18.4 and §18.6 · "No ember card is added to the shop after the setup of the campaign, whether a section is completed or a player joins" (said twice) · CH-18-022, CH-18-028 (A-046; OQ-27) · **A3** · Delete both unless §6.3 really adds one at a restock; then say it once.
- §18.6 Shop Price Table · where sold boss and legendary cards go; "An ember card is priced as a tier one card"; "Every other price … is that of the standard game" · CH-18-029 (C-070, A-077) · **A3** · The table is the rule. Delete the paragraph under it except "in place of the six of the standard game", which can be a table note.
- §18.7 · the ascetic raises enemy base health by two; the author's rule was +1 attack damage · CH-18-030 (B-031, A-064; OQ-07) · mechanical replacement, same length · Not bloat in itself, but it brought a 75-word example and the sentence "The bonfire ascetic does not change enemy attack values or movement values", which only makes sense to someone who knew the old rule. Delete that sentence.
- §18.5 · the author's rule "Encounter soul rewards are reduced by one" and its table were removed · CH-18-038 (OQ-21; B-011) · This is a deletion, not an addition, but the section was not shortened to match: 227 words now say that nothing changes. See worst passages.
- §18.8 · transposition during any rest, free rests included (source: "only available after the characters spend a spark to rest") · CH-18-034 (A-051) · **A1** · The source rule locked transposition out at the moment it unlocked. Keep.
- §18.8 · any number of times per rest; own souls; empty-deck case; "*Transposed treasure* is a kind of tier two treasure card and is not gained by transposition" · CH-18-035 · **A3** for the last two · Delete. The final sentence explains a clash of terms instead of removing it.

### 3. Worst passages

**(a) §18.1 Section Setup (419 words, 13 cross-references).** Source: none beyond "each section of a scenario has varying numbers of exploration tiles, may contain multiple bosses".

> "- A mini-boss is fought on the mini-boss tile, or on its expansion's game board when it is the Asylum Demon (see §17.3), and a *main-boss* on the two *boss tiles* joined as one (see §15.3). A mega-boss is fought on its game board (see §18.1, Level 4 Encounters and Mega-Bosses). - A section that lists the Gargoyle as fought twice sets the Twin Gargoyles encounter, which is one boss encounter (see §17.1, Twin Gargoyles). - The *fog gate* token is placed on the *doorway* to the boss's tile (see §18.2). A section that lists no boss has no fog gate. - The *shop* is restocked as campaign play directs (see §18.6, Blacksmith Andre's Shop), and no *spark* is added during the setup of a section (see §18.3). …"

As cut (104 words):

> A section is set up at the start of the campaign and each time the section before it is completed. The party lays out the bonfire tile, one random encounter tile for each encounter the section lists, and the tile or game board of each boss, as one route in the listed order. Each encounter tile is dealt an encounter card of its listed level, or the named card, and one treasure card per character. The encounter decks hold the cards of every set the campaign requires, unless the campaign says otherwise. If invaders are in play, no more than one invasion occurs in each section.

**(b) §18.3 Sparks (507 words).** Source (105 words): "The characters start a campaign with the same number of sparks used in the basic game (six minus the number of characters). The starting number of sparks also serves as the maximum number of sparks. Each time a mini-boss, main-boss, or mega-boss is defeated, the characters gain one *spark* … characters no longer rest at the *bonfire* for free after defeating a boss except for the final boss of each section. Sparks cannot be purchased or gained otherwise. The players lose the campaign if all characters are lost to the hollow without a *spark* to revive them."

> "While the party rests, it may buy back one spark. The cost is four *souls* for each character in the party, paid to the supply by any combination of the characters, and the spark dial is turned up by one. The spark is not bought unless the full cost is paid. This cost and the cost of the *bonfire ascetic* are the only costs that the characters pay together (see §18.7); souls are never passed from one character to another (see §7.6). The party may buy no more than one spark during each rest and cannot buy a spark while the dial shows its maximum. The spark is bought after the rest's own spark has been spent, and it may be bought during a free rest. Sparks are gained in no other way, except when a player leaves the campaign (see §18.4). If the characters are required to rest while the spark dial shows zero, the players lose the campaign (see §7.1). The party cannot rest while the dial shows zero, so no spark is bought to prevent that loss."

As cut, keeping both Gate 1 decisions (83 words):

> The spark dial starts at six minus the number of characters, and its maximum is one higher. The party gains one spark each time a boss is defeated. A rest costs one spark, except the rest that follows the completion of a section, which is free. Once during each rest the party may buy one spark for four souls per character, paid together. If the characters must rest while the dial shows zero, the players lose the campaign.

As cut on the author's own rule (no buy-back, maximum equal to the start): 60 words, and the table, the example and one price-table row go as well.

**(c) §18.4 Adding and Dropping Players (460 words).** Source (102 words): "New players can join a campaign that is in progress at the cost of one spark each. The new player begins the game with starting character stats and equipment. The new maximum number of sparks is based on the new number of characters. If a player character leaves the characters, the characters gain one spark, the character's equipment is added to the inventory, and the maximum number of sparks is changed to reflect the new number of characters."

> "1. Turn the spark dial down by one. 2. Set up the new character as at the start of the game, with *starting equipment*, every stat at the base tier, and no *souls* (see §6.1). 3. Place the new character's model on the bonfire tile. 4. Set the spark dial's maximum for the new number of characters (see §18.3). 5. If the spark dial shows more than the new maximum, turn it down to the new maximum. 6. Deal one *treasure card* of the current tier face down to each encounter tile that still holds its treasure cards (see §18.5). …" (and six mirror-image steps for leaving, a paragraph, and an example)

As cut (92 words):

> A player may join or leave while the characters are on the bonfire tile. When a player joins, the party spends one spark, and the new character starts with starting equipment, base stats, and no souls. When a player leaves, the party gains one spark, the character's treasure cards pass to the other characters, and the character's souls are lost. In both cases the spark maximum, enemy scaling, and every cost and reward counted per character follow the new number of characters, and each uncleared encounter tile gains or loses one treasure card.

**Also: §18.5 Encounter Rewards (227 words)** opens "*Encounters* are rewarded as in the standard game (see §7.6, §7.7). The *souls* awarded are those of the standard reward table: the full reward and the *reduced reward* for each *encounter level*, and the rewards for *invaders* and bosses, are not changed in campaign play (see §7.6). An encounter already marked *cleared* is skipped or fought again as in the standard game…". Once the author's reduced-reward table was removed, the only campaign rule left in the section is the treasure tier. As cut (38 words): "Encounters are rewarded as in the standard game, with one change. Every treasure card dealt to a tile or placed beneath a chest comes from the tier one deck until the bonfire ascetic is burnt, and from the tier two deck afterwards."

### 4. Unintuitive or over-engineered rules

- **Four ways for a stretch of play to end, each with a different bundle of consequences** (§18.1, §18.3): section completed by a boss (spark, restock, free rest); section completed by an encounter (no spark, restock, free rest); boss defeated mid-section (spark, no restock, no rest, but "recovery" and revival without hollowing); final section (nothing). A player will look this up every time. Two rules are enough: "A defeated boss grants one spark" and "A completed section grants a restock and a free rest."
- **The spark dial arithmetic in §18.4.** Steps 4 and 5 on joining ("Set the spark dial's maximum … If the spark dial shows more than the new maximum, turn it down") and steps 4 and 5 on leaving ("Turn the spark dial up by one, unless it shows the new maximum") are order-dependent and exist only because the maximum now differs from the starting value. The author's sentence ("The new maximum number of sparks is based on the new number of characters") needs no procedure.
- **Invader tokens keyed to the bonfire ascetic** (campaign-E33) sit in the last bullet of Section Setup. Nobody looking for what the ascetic does, or for which invader token to draw, will find it there. One clause in §18.7.
- **No mega-boss treasure for a Level 4 encounter in a campaign** (campaign-E16) is an exception to §6.7, stated in §18.1 and again in §18.5. Legitimate (two cards cannot pay for three encounters) but it should be said once, in §18.1.
- **"Current tier".** The chapter never defines it as a term but uses it eight times, and explains it twice. One sentence in §18.7 ("Until the ascetic is burnt every treasure card comes from the tier one deck; afterwards from the tier two deck") removes the need for the term.
- **The soul-pooling exception** is explained in both places it applies, each time naming the other: "This cost and the cost of the *bonfire ascetic* are the only costs that the characters pay together (see §18.7); souls are never passed from one character to another (see §7.6)." "Paid together" in each rule is enough.
- **Transposition and "transposed treasure"**: two near-identical terms with unrelated meanings, patched by a sentence. Either rename one or trust the reader; the sentence draws attention to a confusion most players would not have had.
- **Mechanical changes the author should confirm rather than discover**: soul rewards are no longer reduced by one (OQ-21); the ascetic raises health by two in place of attack by one (OQ-07); sparks can be bought and the maximum is one higher (OQ-22). All three are logged as Gate 1 answers, and all three replaced a one-sentence rule of the author's with a longer one.

---

## Chapter 19: Campaigns

Author's source: 1,821 words for 13 campaigns (one a duplicate; 12 distinct, about 1,710 words). Final: 3,938 words for 16 campaigns. Needs: about 1,930 with the lists as tables.

Composition of the final text: 1,493 words in numbered list items, 352 in the 65 section headings, 2,093 in prose. The chapter is 699 lines of Markdown, 501 of them non-empty; about 330 of those are single list items of three or four words ("Level 1 encounter").

### 1. Section table

| § | Source | Final | Needs | Main excess |
|---|---|---|---|---|
| Intro | 0 | 78 | 30 | flavour; pointer sentence |
| 19.1 The First Journey | 102 | 298 | 150 | R: Section Four tail restates §18.1 and §6.7 (135 words) |
| 19.2 The Coiled Sword | 120 | 131 | 60 | list format |
| 19.3 Ambush Lies Ahead | 153 | 179 | 80 | list format |
| 19.4 The Gauntlet | 177 | 271 | 110 | R: three "Section N is completed when…" sentences |
| 19.5 Facing the Abyss | 102 (and a 113-word duplicate) | 138 | 65 | list format; R: completion sentence |
| 19.6 Demon Hunting | 163 | 179 | 80 | list format; R of §17.3 |
| 19.7 Call of the Abyss | 137 | 154 | 70 | list format (one section restored) |
| 19.8 A Hollow Pursuit | 119 | 181 | 100 | V: mimic rule, 62 words for the booklet's 25 |
| 19.9 The Undead Colosseum | 198 | 327 | 150 | V: deck paragraph; list format |
| 19.10 Into the Depths | 162 | 197 | 95 | list format |
| 19.11 Playing with Fire | 112 | 117 | 55 | list format |
| 19.12 Big Game Hunting | 153 | 268 | 150 | A: variant paragraph; R of §17.3 and §18.1 |
| 19.13 Go Beyond Death | 0 | 185 | 85 | list format; R: Level 4 board |
| 19.14 Footsteps of Giants | 0 | 248 | 130 | list format |
| 19.15 Treasures of the Ice Cave | 0 | 406 | 220 | V and A: four bullets on paired invaders (210 words) |
| 19.16 Demons and Dragons | 0 | 581 | 300 | V: stat table in sentences; four bullets; closing paragraph |
| **Total** | **1,821** | **3,938** | **1,930** | |

Cross-references: 43 parentheticals, 121 words.

This chapter is the least bloated of the three in rules terms. The pipeline's work here was mostly correction against the booklets (a missing section in Call of the Abyss, a wrong requirement in A Hollow Pursuit, the Gauntlet's invader rule, a duplicate campaign), and that work should stay. The excess is format: the author's nested bullets were turned into an H3 heading plus a numbered list for each of 65 sections (CH-19-001, CH-19-005), which made the lists longer than the author's, and four campaigns were then added in the same form.

### 2. The list format: one table per campaign

**Recommendation: a compact table per campaign, not one table for all 16.** One table for the whole chapter (65 rows) cannot carry each campaign's requirement line and special rules, and those must sit beside the lists they govern. A per-campaign table can, and it carries every fact the lists carry:

- The bonfire tile opens every section, so it is stated once in the chapter introduction and never listed. (65 list lines gone.)
- Encounter levels are written in order as "1 · 1 · 2". A named encounter follows its level ("3 Hydra Lake"); an invader follows in brackets ("2 (Maneater Mildred)").
- The boss has its own column. Where the order is not "encounters, then boss" (§19.16, Section Five), the route is written in full in one cell.

§19.9 The Undead Colosseum as printed is 327 words and 38 non-empty lines. As a table (154 words, 11 lines, nothing lost):

> ## 19.9 The Undead Colosseum
>
> **Requires** the core set, Darkroot, Explorers, Vordt of the Boreal Valley, and Executioner's Chariot. **Optional:** Characters.
>
> Level 1 to 3 encounter cards come from the core set, Darkroot, and Explorers; Level 4 cards from both mega-boss expansions. The six named encounters are Executioner's Chariot cards.
>
> A cleared encounter does not reset and is passed at no cost. Each cleared encounter awards two souls more than the reward for its level.
>
> | Section | Encounters, in order from the bonfire | Boss |
> |---|---|---|
> | 1 Warm Welcome | 1 · 1 · 1 Silent Pathway · 2 | Gargoyle (mini-boss) |
> | 2 Guardian's Gate | 1 Quiet Graveyard · 2 · 2 | Old Dragonslayer (mini-boss) |
> | 3 Trained Beast | 2 · 2 · 2 Mausoleum Ruins · 3 | Great Grey Wolf Sif (main-boss) |
> | 4 Haunting Warrior | 2 Misty Burial Site · 3 | Pursuer (main-boss) |
> | 5 Dark Champion | 3 Corrupted Crypt · 4 | Executioner's Chariot (mega-boss) |
> | 6 Terror of the Ring | 3 Desolate Cemetery · 4 | Vordt of the Boreal Valley (mega-boss) |

How the awkward cases look as rows:

> | 2 Sen's Fortress | 1 · 1 (Kirk, Knight of Thorns) · 2 · 2 (Maneater Mildred) | Titanite Demon (mini-boss) |
> | 1 Undead Burg | 1 · 1 · 2 | Gargoyle (mini-boss), fought twice |
> | 1 Invader Ruins | 1 · 1 · 1 (Melinda the Butcher) · 1 (Maldron the Assassin) · 2 (Kirk, Knight of Thorns) | none |
> | 5 The Final Conflict | 4, then Stray Demon (mega-boss), then 4 | Black Dragon Kalameet (mega-boss) |

Effect on the whole chapter: lists and section headings fall from 1,845 words to about 800, and from about 400 printed lines to about 100. Sixteen campaigns then fit on four or five pages in place of about twelve. A one-page index of the 16 campaigns (name, required sets, number of sections, last boss) would be a useful addition at the head of the chapter and costs about 200 words; it is optional.

### 3. Added rules (class A)

- §19.1 Section Four · optional Kalameet section, with a 135-word tail on board alignment, the flip, no reset, and Darkroot cards · CH-19-009, CH-19-010 (CMP-0021; the Kalameet booklet's "Bathed in Flame") · **A1** for the section, **R** for the tail · "Section Four is optional and requires the Black Dragon Kalameet expansion" is said twice (campaign opening and under the list). The alignment, flip and no-reset sentences repeat §18.1 and §6.7. Keep: "Section Four is optional. Its Level 3 encounters use Darkroot cards if the party owns that expansion."
- §19.4, §19.5, §19.11 · "Section N is completed when … is cleared (see §18.1)", five times · CH-19-014, CH-19-018 (A-048, CMP-0008) · **A3** (R) · §18.1 states the rule for every section that ends in an encounter. Delete all five; "Boss: none" in the table says it.
- §19.4 · a listed invader returns every time until killed · CH-19-034 (campaign-E35; Phantoms booklet) · **A1** · Correct and needed; the source had copied the rule of Ambush Lies Ahead. It runs to 65 words where 30 serve: "Each listed invader is part of its encounter every time the characters enter it, until that invader is killed."
- §19.8 · no ambush card; the chest is a Voracious Mimic; "a *mimic* encounter begins as if an ambush card showing Mimic had been revealed"; "A failed mimic encounter returns the mimic to the chest" · CH-19-021, CH-19-043 (A-102; campaign-E44) · **A2** · The booklet's 25 words do it: "No ambush card is placed beside this tile: the chest is always a mimic. The section is completed when the mimic is killed."
- §19.6, §19.12, §19.16 (and §18.1) · "the Asylum Demon is fought on the mega-boss side of the Asylum Demon expansion's game board (see §17.3)", four statements of a §17.3 rule · CH-19-035, CH-19-040, CH-19-045, CH-18-057 · **A3** (R) · Delete all four.
- §19.12 · "The party may replace the mega-boss of any of these three sections with another mega-boss it owns, and may add further sections of the same form; the players then win the campaign when every such section is completed. Each such section uses the game board and the Level 4 encounter cards of its own mega-boss." · CH-19-040, CH-19-047 (campaign-E41; VB-012) · **A2** · An invitation in the booklet became a rule with a win condition and then needed a verification fix. One sentence: "The party may swap in, or add, any other mega-boss it owns."
- §19.13 to §19.16 · "Both *Level 4 encounters* are fought on the … expansion's *mega-boss game board* (see §18.1)" · CH-19-045 · **A3** (R of §18.1) · Delete.
- §19.15 · paired invaders: second invader on an adjacent node; own behaviour deck each; "The health of the second invader is recorded on any *health dial* that is not in use"; rewards when the second is killed; a cleared encounter with a surviving invader "is fought again … and it is not skipped" · CH-19-045 (campaign-E48), CH-19-048 (VB-010) · **A1** in substance (the VB-010 dead-end is real), **A2** in size: 210 words, about 80 needed (see worst passages).
- §19.16 · the closing paragraph on the order of Section Five · CH-19-046 (VB-011) · **A1**, needed only because §18.1 was written to say a mega-boss follows the section's last Level 4 encounter. With the route in one table cell, one sentence remains.

### 4. Worst passages

**(a) The lists.** See section 2. As the author wrote it, a section was a bullet with nested bullets. As printed now:

> "### Section Two: Guardian's Gate
>
> 1. Bonfire tile
> 2. Level 1 encounter: Quiet Graveyard
> 3. Level 2 encounter
> 4. Level 2 encounter
> 5. Old Dragonslayer (mini-boss)"

As cut: `| 2 Guardian's Gate | 1 Quiet Graveyard · 2 · 2 | Old Dragonslayer (mini-boss) |`

**(b) §19.15, paired invaders (about 230 words with the lead-in).**

> "- Both invaders are part of that encounter every time the characters enter it, until both have been killed during one visit. If either invader vanishes, or the encounter is *failed*, both return the next time the characters enter it. An encounter that is *cleared* before both of its invaders have been killed is fought again when the characters next enter it, the Level 4 encounter of Section Three included, and it is not skipped. - The first invader is placed as the invader rules state, and the second on a node adjacent to it, chosen by the players. Each invader has its own *behaviour deck*, and each takes a turn after each character's turn, in the order the players choose. The health of the second invader is recorded on any *health dial* that is not in use. - The *souls* and the treasure cards of both invaders are awarded when the second of them is killed, and not before. - The section is completed only when that encounter is *cleared* and both of its invaders have been killed (see §18.1)."

As cut (84 words):

> The party places no invader tokens. Two encounters each hold two invaders. Both appear every time the characters enter that encounter, until both are killed in one visit; until then the encounter is fought again each time and cannot be skipped, and its section is not completed. The second invader is placed adjacent to the first. Each has its own behaviour deck and takes a turn after each character's turn. Their souls and treasure are awarded together, when the second is killed.

**(c) §19.16, special rules (about 330 words of prose and table).**

> "| One | Two stats from the base tier to stat tier one, then one stat from stat tier one to stat tier two | | Two | Two stats from the base tier to stat tier one, then one stat from stat tier one to stat tier two | | Three | One stat from stat tier one to stat tier two, then one stat from stat tier two to stat tier three | | Four | One stat from stat tier one to stat tier two, then one stat from stat tier two to stat tier three | | Five | Two stats from stat tier two to stat tier three |" … "The encounters of Section Five are fought in the order listed: the Stray Demon is fought when the first Level 4 encounter is cleared, and the second Level 4 encounter is set up when the Stray Demon is defeated. The defeat of the Stray Demon does not complete Section Five. The players win the campaign when Black Dragon Kalameet is defeated (see §18.1)."

As cut (118 words):

> Encounters award no souls in this campaign; bosses and invaders award souls as usual. Clearing a Level 4 encounter gains the party one spark. A cleared Level 4 encounter and a defeated mega-boss are never fought again. At the start of each section each character raises stats at no cost:
>
> | Section | Free raises for each character |
> |---|---|
> | One, Two | two stats to tier one, then one stat to tier two |
> | Three, Four | one stat to tier two, then one stat to tier three |
> | Five | two stats to tier three |
>
> In Section Five the Stray Demon is fought as soon as the first Level 4 encounter is cleared, and the second Level 4 encounter is set up when it falls.

### 5. Unintuitive or over-engineered rules

- **Three invader regimes that look alike on the page.** Ambush Lies Ahead (each listed invader appears once, whatever happens), The Gauntlet (returns until killed), Treasures of the Ice Cave (a pair returns until both are killed in one visit). These are the official designs and should stay, but each is introduced by the same sentence ("The party does not place *invader tokens* during this campaign (see §12.2). An *encounter* that lists an *invader*…") and the difference is buried in the second or third sentence. Put the difference first: "Listed invaders appear once." / "Listed invaders return until killed." / "Paired invaders return until both are killed in one visit."
- **Encounter-deck sources are phrased five ways** ("built only from", "built from … together", "The party may add the encounter cards of any other expansion", "If the party owns the Darkroot expansion, they are built from … instead", and silence, which §18.1 now fills with a default). A fixed line per campaign ("Encounter cards: core set only") in the header block ends the variation and saves about 150 words.
- **"The party may add the Explorers and Characters expansions"** appears in 13 campaigns. It is not a rule: a party may always add characters it owns, and whether Explorers encounter cards join the decks is already decided by the deck line. One sentence in the chapter introduction.
- **§19.12, "Section Two A, Section Two B, Section Two C"**, and the sentence "sets up each of them when the section before it is completed (see §18.1, Section Setup)": the labels are the booklet's, but the second half restates §18.1. "Sections Two A, B, and C are played in any order" is the whole rule.
- **§19.1**: the reader is told three times that Section Four needs the Kalameet expansion and twice that it is optional.

---

## Totals for the group

| | Source | Final | Needs | Excess |
|---|---|---|---|---|
| 17 Boss Special Rules | 212 | 8,963 | 3,950 | 5,013 |
| 18 Campaign Play | 1,134 | 4,024 | 1,415 | 2,609 |
| 19 Campaigns | 1,821 | 3,938 | 1,930 | 2,008 |
| **Group** | **3,167** | **16,925** | **7,295** | **9,630** |

(Whole-file counts including headings: source 3,343, final 17,122.) The group can lose 57 per cent of its words. Of the 7,295 words needed, about 4,450 are content the author did not write but asked for (the boss entries other than the two demons, and four campaigns); the author's own material, tightened, is about 2,850 words, a little under the 3,167 it started at.

Split of the 9,630 excess words, by class (estimates):

| Class | Ch. 17 | Ch. 18 | Ch. 19 | Group | Share |
|---|---|---|---|---|---|
| R restated | 1,400 | 750 | 330 | 2,480 | 26% |
| V verbose (procedures, lists that should be tables, template sentences) | 550 | 170 | 1,300 | 2,020 | 21% |
| A added rules beyond the source and the booklets | 900 | 600 | 130 | 1,630 | 17% |
| D defensive | 700 | 450 | 120 | 1,270 | 13% |
| X cross-reference clutter (268 parentheticals, 756 words, plus pointer sentences) | 520 | 380 | 130 | 1,030 | 11% |
| E examples (13 examples, about 1,130 words; three worth keeping at half length) | 700 | 220 | 0 | 920 | 10% |
| G glossary-in-chapter (12 bold definitions, all also in `12_glossary.md`) | 240 | 40 | 0 | 280 | 3% |

## How it happened

1. **A fixed template was imposed on every boss.** CH-17-018: "Every boss entry in the chapter uses the same five-part structure" (Components / Setup / Special Ability / Heat-Up / Unique Icons). When the placeholders were replaced by booklet rules (CH-17-060 to CH-17-066, boss-E20 to boss-E26), each boss got a components list that chapter 2 already holds, a "Special ability" paragraph even where the ability only repeats the setup (Kalameet, Gaping Dragon, Guardian Dragon, Last Giant), and a "Heat-up" paragraph even where the general rule applies unchanged (Kalameet, Old Iron King, Pursuer).
2. **Sentences were turned into numbered procedures.** CH-17-021 made the author's pillar sentence "a four-step procedure"; CH-17-011 gave the Twin Gargoyles a five-step change-over; CH-17-037 a seven-step strafe; CH-18-019 "two numbered procedures" of six steps each for joining and leaving; CH-18-035 two more for transposition. Each step needs a subject, an object and usually a cross-reference, so a 20-word sentence becomes 60 words.
3. **Every gap found by an audit was filled with a new sub-section, written to serve other chapters.** CH-18-008 Section Setup (CMP-0008, A-048, OQ-28), CH-18-010 Level 4 Encounters and Mega-Bosses ("§6.7 relies on this section"), CH-18-011 The Final Boss ("on which §7.1 and §20.8 depend"), CH-18-012 PvP (OQ-15), CH-17-005 ("dependency of §5.3"), CH-18-022 ("§8.3 relies on this section"). §18.1 grew from 145 words to 1,497 this way, and each dependency left a restatement and a cross-reference at both ends.
4. **Rulings were made, then reversed or patched, and each round left text behind.** Ornstein & Smough were first ruled one boss with a shared dial (Gate 1 OQ-25; CH-17-006 to 009, 016, 017), then restored to the official two-dial fight (boss-E08, boss-E10; CH-17-053, 054) inside a new general framework. The spark buy-back (CH-18-015) was re-ruled as a pooled payment (campaign-E18 to E21; CH-18-045 to 048) and its example recomputed. The mid-section boss paragraph (CH-18-041), admitted to arise "only in a campaign of the players' own design", was lengthened by VB-009 (CH-18-058). A special rest rule for Demon Hunting was written (CH-19-019) and deleted (CH-19-035). Verification added VB-010, VB-011 and VB-012 to chapter 19.
5. **Mechanical changes replaced one-sentence rules with rules that need explaining.** Spark maximum plus one and the buy-back (B-013, OQ-22; CH-18-014, 015) brought a table, five limits and a 115-word example. The ascetic's change from +1 attack to +2 health (B-031, OQ-07; CH-18-030) brought an example and a sentence denying the old rule. Dropping the author's reduced soul rewards (OQ-21; CH-18-038) left §18.5 as 227 words that say nothing changes.
6. **Worked examples were a standing instruction.** CH-17-014 and CH-17-025 cite "brief §2 (worked examples)"; CH-18-018 and CH-18-033 cite "chapter instructions". Result: ten examples in chapter 17 and three in chapter 18, about 1,130 words, most of them walking through a procedure that had just been listed step by step.
7. **Pre-emptive negatives.** CH-17-023 ("A magical attack, or an attack that does not show the area icon, destroys no pillar"), CH-17-026 (Wind Up "on any other behaviour card"), CH-17-059 ("so that no reader looks for a heat-up point"), CH-18-031 (the pooling exception named in both places), CH-18-028 (no ember card, the omitted legendary step).
8. **Lists were standardised, not compressed.** CH-19-001 and CH-19-005 replaced the author's bullets with an H3 and a numbered list per section in "five fixed forms", and CH-19-004 gave every campaign a full requirement sentence. Four campaigns were then added in the same form (CH-19-045). The format, not the rules, is why chapter 19 doubled.

## Ten cuts, largest first

Savings overlap slightly (cross-references are counted in the sections they sit in as well as in cut 8); together they recover about 7,500 of the 9,630 excess words.

1. **Chapter 17: one deck table for the nine mega-bosses; delete every Components list and every "set up as any mega-boss encounter … with the following differences" lead-in; fold "as the general rule directs" heat-ups into the table.** About 1,150 words. Loss: none; chapter 2 holds the components.
2. **Chapter 19: one compact table per campaign in place of 65 headings and numbered lists; requirements and deck sources as a two-line header.** About 1,050 words and about 300 printed lines. Loss: none.
3. **§18.1: Section Setup to one paragraph, Section Completion to two sentences, Level 4 and mega-bosses to about 100 words, Final Boss and PvP to a sentence each.** 1,497 to about 520; saves about 975. Loss: the mid-section-boss recovery detail, which no campaign but §19.16 uses.
4. **§17.1: Twin Gargoyles to one paragraph, the several-models framework to one paragraph, Zero Dodge Difficulty to one sentence, drop the data-card precedence rule.** 1,133 to about 270; saves about 860. Loss: none in play.
5. **§18.5 to §18.8: say each rule once (tier rule, boss treasure, legendary treasure, pooled payment); delete the paragraph under the price table; transposition as one paragraph.** 1,394 to about 550; saves about 840.
6. **§18.3 and §18.4: sparks in five sentences, joining and leaving in four; drop the table and both examples.** 967 to about 280; saves about 690. If the author restores "Sparks cannot be purchased", a further 60 go.
7. **Chapter 17 examples: keep the pillars, the Ornstein & Smough heat-up and the royal summons at half length; delete the other seven.** Saves about 650.
8. **Cross-reference sweep across the three chapters: 268 "(see …)" parentheticals, 756 words.** Keep those that send the reader to a rule they must read to play the passage (perhaps 40). Saves about 600 gross, about 300 beyond the other cuts.
9. **§17.3 Asylum Demon and Stray Demon back to the author's length.** 699 to about 230; saves about 470. Loss: the example.
10. **Define the node-targeted attack once in §17.1 and give Kalameet, the Guardian Dragon, the Old Iron King and the Chariot only their differences; in the same pass put Wind Up and Overextended in §17.1 once, and delete the "no rules beyond its data card" entries.** Saves about 350 + 80 + 190, about 620.
