# Bloat audit: bosses group (chapters 12 to 16)

Auditor's note on method. Word figures are counted with `len(text.split())` per heading (headings included, HTML comments excluded). "Words it needs" is my estimate of the section written at the author's density: the author's rules, plus the short fixes the game cannot be played without. Classes are those of the brief (K, R, X, D, A, E, V, G). The report follows the shortened format set by the coordinator: section table with the main class of excess, added rules, three worst passages, unintuitive rules.

---

## Chapter 12: Phantoms

Source 543 words. Final 2,462 words. Needs about 845.

### Section table

| § | source words | final words | words it needs | X count | main class of excess |
|---|---|---|---|---|---|
| 12 (chapter opening) | 0 | 128 | 20 | 3 | V flavour intro (50), G "Phantom" definition repeated from the glossary (38), D "neither a character nor a boss" (40) |
| 12.1 Summons (opening) | 173 (whole of source "Phantoms") | 69 | 30 | 1 | R: optional-rule formula restates §6.5; standard/advanced split said here and again in Summoning step 2 |
| 12.1 Summoning | (in 173) | 306 | 110 | 3 | E (62-word example of a two-line rule), V (five source steps became eight), D (three "souls are not returned" type sentences), A (tie-break) |
| 12.1 Summon Turns | (in 173) | 285 | 110 | 4 | A (attack resolution, weak-arc die, shift, distract, deck renewal), R (shift paragraph restates "left to right"), E |
| 12.1 Summons in Combat | 0 | 315 | 70 | 5 | A: the whole subsection is new. R (defence bullets restate §9.4 and §9.5), D (list of eight things a summon does not have) |
| 12.1 Removal of a Summon | (in 173; 16 words) | 83 | 20 | 1 | D: 48 words on what a summon's death does not cause |
| 12.2 Invaders (opening) | 1 | 89 | 30 | 2 | R: standard/advanced and the campaign tier rule, both said again in Invader Tokens step 1 |
| 12.2 Invasions | (in 92) | 165 | 50 | 6 | A (two trigger moments, black-cube qualifier), D (boss-defeat embering paragraph), G ("Invasion") |
| 12.2 Invader Tokens | 92 | 380 | 110 | 6 | E (75-word example), A (blank-token shortfall, reset, mini-boss clean-up), D (no invader in a boss or mimic encounter) |
| 12.2 Invader Setup | 136 | 151 | 90 | 2 | V (steps split one action per step), D (doorway sentence) |
| 12.2 Invader Turns | about 75 | 197 | 95 | 5 | D (no arcs, "ability applies as printed"), V (heat-up at 50 words for the source's 21) |
| 12.2 Combat with an Invader | about 30 | 130 | 45 | 5 | R (restates "the rules for enemy models apply"), D (what continues when the invader vanishes) |
| 12.2 Invader Rewards | about 20 | 84 | 35 | 2 | R (party-card tie-break of §7.7), D |
| 12.2 End of an Invasion | about 15 | 80 | 30 | 3 | V: the source's 11-word rule now takes 40 |
| **Chapter 12** | **543** | **2,462** | **845** | **48** | |

Approximate split of the final text by class: K 610, A 550, D 450, R 350, V 295, E 175, G 50 (X: 48 references, about 150 words, counted inside the other classes).

### Added rules (class A)

- §12.1 Summoning · "A character pays no more than once"; one card per paying character · CH-12-003 (A-100, CMP-0018) · A1 · keep, seven words.
- §12.1 Summoning · if the players cannot agree, shuffle the drawn cards and draw one · CH-12-035 (phantom-E01) · A3 · delete. A co-operative table does not need a procedure for disagreeing; the author wrote "players must agree".
- §12.1 Summoning · payment is "an exception to the rule that souls are spent only at the bonfire"; souls are not returned · CH-12-003 · A3 · delete both sentences. The step already says the character pays.
- §12.1 Summoning · summon placed on an entry node "that holds fewer than three models" · CH-12-006 (C-033) · A3 · delete the qualifier; the node model limit is a general rule.
- §12.1 Summon Turns · one summon turn after each character's turn · CH-12-007 (Gate 1, OQ-32) · A1 · keep. The source's "after all character turns" names a phase a boss encounter does not have.
- §12.1 Summon Turns · empty deck: turn the discard pile over without shuffling · CH-12-008 (A-099, CMP-0018) · A2 · one clause in the draw step.
- §12.1 Summon Turns · attack resolved as a character's attack, no stamina; players make open choices · CH-12-009 (CMP-0018, D-010) · A1 · keep, one sentence.
- §12.1 Summon Turns · summon in the weak arc adds a black die · CH-12-009 · A3 · delete; "as a character's attack is" already gives it.
- §12.1 Summon Turns · shift icon before or after the dice resolves before or after the roll · CH-12-009 · A3 · delete; "left to right" says it.
- §12.1 Summon Turns · Distract icon · CH-12-009 (CMP-0018) · A1 · keep; the icon is printed on the cards and nothing else explains it.
- §12.1 Summons in Combat · boss treats a summon as a character (targeting, threat, push, conditions) · CH-12-010 (A-016, D-010) · A1 · keep as one sentence. Without it nobody knows whether the boss may hit the summon.
- §12.1 Summons in Combat · never holds the aggro token; its damage does not move it · CH-12-010 · A1 · keep, one sentence.
- §12.1 Summons in Combat · defence procedure (two highest dice, dodge to an adjacent valid node, full damage on a failed dodge) · CH-12-010 · A2 · "defends as a character does, with the dice on its data card; its dodge is free."
- §12.1 Summons in Combat · list of what a summon lacks (endurance bar, arcs, heat-up, scaling, minor and major actions, parry) · CH-12-036 (phantom-E02) · A3 · delete all but "does only what its behaviour cards and data card direct".
- §12.1 Summons in Combat · once-per-encounter ability marked with a wound token · CH-12-011 (CMP-0018) · A3 · delete; bookkeeping the card itself implies.
- §12.1 Removal · encounter not failed, nobody hollowed by a summon's death; party wipe still fails · CH-12-014 (CMP-0018, D-010) · A3 · delete.
- §12.2 opening and Tokens step 1 · in campaign play the standard/advanced switch is the current tier · CH-12-037, CH-12-048 (phantom-E03, VB-001) · A2 · needed for campaigns, but belongs once in chapter 18, not three times here.
- §12.2 Invasions · two named trigger moments (setup; discarding an ember card) · CH-12-017 (A-045) · A2 · one sentence: provoked as soon as a character is embered while an unfought encounter card lies face down.
- §12.2 Invasions · only encounter cards "that carry no black cube" count · CH-12-038, -040, -041 (phantom-E04, E06, E07) · A2 · say "unfought encounter card" once; the phrase is now repeated in four places.
- §12.2 Invasions · embering at a boss's defeat provokes nothing then; the next invasion comes at the next deal · CH-12-017 · A3 · delete; it follows from "while face-down encounter cards lie on the tiles".
- §12.2 Invasions · one invasion per campaign section · CH-12-039 (phantom-E05) · A2 · belongs in §18.1 only.
- §12.2 Invader Tokens · blank tokens run out: use other invader tokens as blanks · CH-12-034 (QA-010) · A2 · real component shortfall in one campaign layout; ten words, or a note in chapter 18.
- §12.2 Invader Tokens · tokens stay at a reset; unrevealed tokens return at the mini-boss's defeat · CH-12-018 (C-120, A-045) · A2 · one clause; the second half is obvious when the tiles are cleared away.
- §12.2 Invader Tokens · token revealed after enemies and terrain are placed, not on entering the tile · CH-12-019 (CMP-0007) · A4 · restore the author's order: flip the token on entering, then set up, then place the invader. The source was not contradictory.
- §12.2 Invader Tokens · no invader in a boss or mimic encounter · CH-12-020 (A-021) · A3 · delete; tokens go only on encounter cards.
- §12.2 Invader Turns · deck renewal; heat-up follows the boss procedure and timing · CH-12-025, CH-12-047 (lead-E17) · A2 · "heats up as a boss does, using one unused behaviour card at random."
- §12.2 Invader Turns · no arcs, no weak-arc die · CH-12-026 (C-097) · A3 · delete; the cards show no arcs.
- §12.2 Rewards · every character gains the invader reward; treasure to the party · CH-12-029 (Gate 1, OQ-29) · A1 · keep, one sentence.
- §12.2 End of an Invasion · encounter not cleared while the invader is on the tile · CH-12-030, -033, -045 (phantom-E11) · A2 · already given by "the rules for enemy models apply"; at most twelve words.

### Worst passages

**1. §12.1 Summons in Combat (315 words, nothing in the source).**

> "A summon's data card shows its *threat*, its starting health, its *block*, *resist*, and *dodge* dice, and a special ability. A summon has no *endurance bar* and pays no stamina. It has no *boss arcs* and no *heat-up* point, and its health is not scaled. A summon does only what its behaviour cards and its data card direct. It takes no *minor action* and no *major action*, and it cannot *parry*. … Block or resist: the summon rolls its block dice against physical damage or its resist dice against magical damage. Its *defence total* is the sum of the two highest dice. … Each point of damage that a summon suffers lowers its health dial by one. … Summons neither trigger traps nor suffer them (see §5.5, Traps)."

Source: none. As I would cut it (62 words):

> A summon does only what its behaviour cards and its data card direct. The boss's behaviours treat it as a character: it is targeted, hit, pushed, and given conditions as one. It defends as a character does, with the dice on its data card, and its dodge costs nothing. A summon never holds the aggro token, and the damage it deals does not move the token.

**2. §12.1 Summoning, closing paragraph and example (130 words).**

> "The players choose the summon together in step 3. If they cannot agree, the drawn data cards are shuffled face down and one is drawn. Souls paid in step 1 are not returned, whichever card is chosen. This payment is an exception to the rule that souls are spent only while resting at the *bonfire* (see §7.6). If no character pays, no summon joins the encounter. *Example.* The Knight and the Herald are embered, and the Assassin is not. Before the Gargoyle encounter the Knight and the Herald each pay two souls and draw Eygon of Carim and Sword Master. The players choose Eygon of Carim. …"

Source: "Embered characters may elect to pay two souls to draw a phantom card. … Players must agree on only one of the drawn phantoms to summon." As I would cut the whole Summoning procedure (75 words):

> At the fog gate, before a boss encounter, each embered character may pay two souls once to draw one summon data card at random: a standard summon before a mini-boss, an advanced summon before a main-boss or mega-boss. The players choose one of the drawn summons and return the rest. Set its health dial, shuffle its four behaviour cards into a deck, and place its model on an entry node after the characters are placed.

**3. §12.2 Invasions and the opening of Invader Tokens (the same condition four times).**

> "At setup: when the *encounter cards* are dealt to the tiles (see §6.5; §6.6), if one or more characters are embered. During the exploration: when a character becomes embered by discarding an *ember card* (see §7.3), if one or more face-down encounter cards that carry no black cube lie on the encounter tiles (see §7.5, Encounter Resolution). No more than one invasion is provoked before the mini-boss is defeated, and no more than one after it, however many characters are or become embered. The embering of every character at a boss's defeat provokes no invasion at that moment (see §16.5). The invasion that follows the mini-boss's defeat is provoked when the encounter cards of the next setup are dealt (see §6.6). In campaign play, no more than one invasion is provoked in each *section* (see §18.1)."

Source: "Embered characters provoke an invader if no invasion has occurred yet." As I would cut it (44 words):

> An invasion is provoked as soon as any character is embered while an unfought encounter card lies face down on the tiles. No more than one invasion is provoked before the mini-boss is defeated, and no more than one after it.

### Unintuitive or over-engineered rules

- **Token reveal moved to the end of encounter setup (CH-12-019).** The author flips the token when the party steps onto the tile. That is the natural beat: step in, flip, groan. The final text makes the party set up the whole encounter before it learns whether it is invaded. Restore the source order; nothing is lost.
- **Three vocabularies for "an encounter not yet beaten".** The chapter says "face-down encounter cards that carry no black cube" four times. A player has to go to §7.5 to learn what the cube means. "Unfought encounter card" says it.
- **Summon defence written out as a second defence procedure.** A player who has learnt character defence now reads a near-copy and must check it for differences. There is one difference (the dodge is free). Say that one difference.
- **Summon "is treated as a character" in one paragraph and "is not a character" in two others.** The opening says a phantom is not a character and rules apply only where the chapter says so; Summons in Combat says the boss treats it as a character; Removal says again it is not one. One sentence, placed once, does the work: the boss treats a summon as a character; nothing else does.
- **Standard game and campaign versions of the same switch, interleaved.** The standard/advanced rule appears as a pair (standard game, then campaign) in the opening of §12.2 and again in Tokens step 1. A player of the standard game reads the campaign rule twice for nothing. The campaign version belongs in chapter 18.
- **Tie-break by shuffled redraw (phantom-E01).** A rule for players who cannot agree which friendly helper to take is a rule no table will ever use.

---

## Chapter 13: Mimics

Source 438 words. Final 1,337 words. Needs about 520.

### Section table

| § | source words | final words | words it needs | X count | main class of excess |
|---|---|---|---|---|---|
| 13 (chapter opening) | 66 | 70 | 20 | 0 | V: 50 words of new flavour replace the author's advice; the optional-rule formula restates §6.5 |
| 13.1 Chests and Ambush Cards | about 150 | 272 | 150 | 7 | R (ambush cards dealt at setup, owned by §6.5 and §2.6), D ("the chest stays closed, and its ambush card stays face down"), X |
| 13.2 The Mimic Encounter | about 110 | 462 | 170 | 8 | R (steps 1 to 5 copy boss deck construction of §15.5 and the invader setup of §12.2), D (arcs, boss rewards, summons, invaders), A (stamina shed), G ("Mimic encounter") |
| 13.3 Mimic Rewards | about 45 | 372 | 120 | 6 | E (125-word example), R (step 2 said again as "Loot the Body"; recovery of §7.5 written out again), D ("no soul reward of its own") |
| 13.4 Failed Mimic Encounters | about 55 | 161 | 60 | 4 | V (four-step tidy-up), R (when an encounter is failed, §7.2), A (rematch made optional) |
| **Chapter 13** | **438** | **1,337** | **520** | **25** | |

Approximate split of the final text by class: K 430, R 300, A 185, D 150, E 125, V 115, G 25 (X: 25 references, about 80 words, inside the other classes).

### Added rules (class A)

- §13.1 · resolution and recovery deferred: "no dead character is revived, and no souls or treasure are collected" · CH-13-004 (A-060, CMP-0014) · A1 · keep as one clause. The deferral is the author's; what is deferred needed saying once.
- §13.1 · a forgone chest may be opened each later time the encounter is cleared · CH-13-010 (CMP-0014, A-102) · A1 · keep, one sentence.
- §13.1 · the chest's reward is the card dealt beneath it, not a fresh draw · CH-13-009 (Gate 1, OQ-11) · A1 · keep; author's answer.
- §13.2 · eight-step setup (take components, set dial, shuffle, deal, set aside, place model, keep token, leave characters) · CH-13-012 (CMP-0014, C-120) · A2 · two sentences: the deck is built as a boss's is; the mimic model replaces the chest token.
- §13.2 · before the mimic's first turn every character removes all stamina cubes; damage, conditions, tokens and aggro unchanged · CH-13-026 (phantom-E19, audit B-035) · A4 · the author wrote "characters do not recover". This creates a third recovery state that exists nowhere else and needs 55 words to fence. If the author wants it, it is one sentence; if not, restore "the characters recover nothing".
- §13.2 · campaign play: Hungry Mimic in tier one, Voracious Mimic in tier two · CH-13-027 (phantom-E20) · A2 · move to chapter 18.
- §13.2 · a mimic has no arcs; no weak-arc die · CH-13-014 (C-097, A-044) · A2 · five words: "A mimic has no arcs."
- §13.2 · a mimic's death grants "no boss soul reward, no boss treasure, no spark, no embering, and no rest" · CH-13-015 (CMP-0014) · A2 · "Killing a mimic is not the defeat of a boss."
- §13.2 · not scaled; no summon; no invader · CH-13-015 (A-021, §8.3) · A3 · delete. Summons are called at the fog gate and invaders come by token on an encounter card; neither can reach a mimic.
- §13.2 · the aggro token moves as in a boss encounter · CH-13-012 · A3 · delete; "fought as a mini-boss encounter" says it.
- §13.3 · four-step resolution; chest token returned open side up; ambush card to the supply · CH-13-016, CH-13-028 (phantom-E21) · A2 · one sentence.
- §13.3 · "A mimic has no soul reward of its own" · CH-13-018 (CMP-0014) · A3 · delete.
- §13.3 · characters who died in either encounter are revived hollow at the deferred recovery · CH-13-017 (A-060) · A2 · covered by "the encounter is resolved as a cleared encounter".
- §13.4 · a failed mimic encounter fails the encounter that held the chest; no souls, no treasure · CH-13-020 (A-060) · A1 · keep, one sentence.
- §13.4 · after a failure the party again chooses whether to open the chest · CH-13-021 (CMP-0014) · A4 · the author's rule is the opposite and is plain: "once the mimic has been fought once, it must be fought again at the end of the encounter until it is killed." The log calls the author's two sentences incompatible; they say the same thing twice. Restore the forced rematch. No Gate 1 answer covers this change.
- §13.4 · four-step return of the mimic to its chest · CH-13-021 · A2 · one sentence.

### Worst passages

**1. §13.2, setup list and "differs from a boss in three ways" (about 300 words).**

> "1. Take the *data card*, the *behaviour cards*, and the model of the Hungry Mimic or the Voracious Mimic, and the mimic *health dial*. 2. Set the health dial to the starting health … 3. Shuffle the mimic's behaviour cards. 4. Deal a number of behaviour cards equal to the behaviour deck size … 5. Set the remaining behaviour cards aside, face down. 6. Remove the chest token from its node and place the mimic model on that node. 7. Keep the chest token and the treasure card that lay beneath it beside the tile. 8. Leave every character model on the node it occupies. … A mimic differs from a boss in three ways. A mimic has no *boss arcs*. Its behaviour cards show no attack arcs and no *weak arc*, and no attack against a mimic gains the weak-arc die … The killing of a mimic is not the defeat of a boss. It grants no boss soul reward, no *boss treasure*, no *spark*, no embering, and no rest … A mimic's health is not scaled. No *summon* is called for a mimic encounter, and no *invader* takes part in one."

Source: "Characters remain on the nodes they occupied at the end of the encounter containing the chest. The mimic will take its turn first. Refer to 'Boss Encounter' rules for more details on how to manage the mimic's behaviour cards. The only difference is that the mimic does not have specific heat-up behaviour cards and instead just shuffles in one unused normal behaviour card when it heats-up."

As I would cut it (99 words, the whole of §13.2):

> A mimic encounter is fought as a mini-boss encounter, with these differences. The Hungry Mimic is fought if the mini-boss has not been defeated, and the Voracious Mimic if it has. Its behaviour deck is built as a boss's is, and its model replaces the chest token. The characters stay on their nodes and recover nothing. The mimic takes the first turn. A mimic has no arcs and no heat-up cards: when it heats up, one of its unused behaviour cards, taken at random, serves as its heat-up card. Killing a mimic is not the defeat of a boss.

**2. §13.3, everything after the numbered steps (about 250 words).**

> "The two treasure cards are the reward that the mimic's data card calls Loot the Body. They take the place of the single card that the chest held, and they are awarded to the party as a chest's card is (see §7.7). A mimic has no soul reward of its own. The *souls* and the treasure that the characters collect in step 3 are the deferred rewards of the encounter that contained the chest (see §7.6; §7.7). The recovery deferred since the encounter was cleared takes place at the end of step 3. Each surviving character removes all condition tokens, all stamina cubes, and one damage cube, and each character who died in either encounter is revived *hollow* … *Example.* The Knight and the Herald clear a Level 2 encounter …"

Source: "If the characters kill the mimic, they gain two tier appropriate treasures (instead of one), and may mark the encounter cleared."

As I would cut it (63 words, the whole of §13.3, with the example dropped or halved):

> When the mimic is killed, the party is awarded two treasure cards in place of the chest's one: the card that lay beneath the chest and one drawn from the treasure deck of the current tier. The chest token returns to its node, opened. The encounter that contained the chest is then resolved as a cleared encounter. A killed mimic does not return.

**3. §13.4 Failed Mimic Encounters (161 words).**

> "A *mimic encounter* is *failed* when every character has died, or when a *hollow* character dies and is *lost* (see §7.2). The *encounter* that contained the *chest* is then failed, although its enemies had been killed. … 1. Remove the mimic model from the tile. 2. Return the chest token, closed side up, to its node, with its *treasure card* beneath it. 3. Leave the *ambush card* face up beside the tile. 4. Return the mimic's data card, behaviour cards, and *health dial* to the supply. Each later time that encounter is *cleared*, the party again decides whether to open the chest (see §13.1). Opening the chest begins a new mimic encounter, set up afresh (see §13.2). The chest yields no treasure until the mimic is killed."

Source: "If the mimic kills all of the characters, the encounter is failed, and the characters will encounter the mimic next time they complete the normal encounter in which the mimic lives. However, once the mimic has been fought once, it must be fought again at the end of the encounter until it is killed."

As I would cut it (56 words, with the author's rematch restored):

> If a mimic encounter is failed, the encounter that contained the chest is failed with it and awards nothing. The chest token returns to its node, closed, with its treasure card beneath it, and the ambush card stays face up. Each time that encounter is cleared again, the mimic is fought again, until it is killed.

### Unintuitive or over-engineered rules

- **The stamina shed (phantom-E19).** A player now has to hold three recovery states: ordinary recovery, none, and "stamina only, and not conditions, and not tokens, and not the dead". The paragraph that fences it is longer than the rule. The author's "characters do not recover" is one state and four words. What is lost by restoring it: the first mimic turn is harsher, which the author's own opening calls "quite punishing" on purpose.
- **The optional rematch (CH-13-021).** With the ambush card left face up the party knows the chest is a mimic and may decline it for ever, so the tile carries a dead chest and a rule about it. The author's forced rematch needs no decision and no bookkeeping.
- **Eight setup steps for a model swap.** A player who has built one boss deck does not need steps 1 to 5; a player who has not will not learn it here. Steps 7 and 8 are instructions to do nothing.
- **Deferred resolution explained three times.** §13.1 defers it, §13.3 step 3 performs it, and three further paragraphs of §13.3 explain what step 3 meant. The single sentence "the encounter is then resolved as a cleared encounter" carries all of it.
- **"Loot the Body".** The card's name for its reward is introduced after the reward has been stated, which makes a reader check whether it is a second reward.

---

## Chapter 14: Crystal Lizards

Source 274 words. Final 397 words. Needs about 260. This is the least inflated chapter in the group; the excess is cross-references and three small additions.

### Section table

| § | source words | final words | words it needs | X count | main class of excess |
|---|---|---|---|---|---|
| 14 Crystal Lizards (no H2 sections) | 274 | 397 | 260 | 9 | X (nine references in 397 words, about 30 words), A (card-supply limit, party award), R (optional-rule formula; "enemy models apply"; party-card rule of §7.7), D ("makes no attack") |

Approximate split of the final text by class: K 240, A 60, R 45, X 30, D 12, V 10.

### Added rules (class A)

- §14 · the Titanite Scale card is awarded to the party, and the players choose who takes it · CH-14-012 (phantom-E24) · A4 · the author wrote that the character who kills the lizard takes the card. That is what any player would guess, and it rewards the chase. The ruling exists to cover a lizard killed by a condition; that case is rare enough to leave to the table.
- §14 · three Titanite Scale cards exist; when none remains a kill awards nothing and no lizard is placed again · CH-14-008 (CMP-0015, A-097) · A2 · "If no Titanite Scale card remains, crystal lizards are no longer placed." Twelve words.
- §14 · kill recorded by a damage cube on the encounter card, in place of the upside-down model · CH-14-013 (phantom-E25) · A1 · keep. Only two models are supplied, so the author's marker fails on a second marked tile.
- §14 · neither enemy scaling nor the bonfire ascetic changes "its health or its movement" · CH-14-005 (A-028) · A2 · "A crystal lizard is not scaled." The author wrote exactly that about health.
- §14 · "A crystal lizard makes no attack" · CH-14-004 · A3 · delete; its data card has no attack icon.

### Worst passages

**1. The award paragraph.**

> "When a crystal lizard is killed, the party is awarded one Titanite Scale card from the supply at once (see §4.2). The players decide which character receives it, as for any card awarded to the party (see §7.7). The Iron Keep expansion supplies three Titanite Scale cards. When none remains, a killed crystal lizard awards nothing, and no crystal lizard is placed in any later encounter."

Source: "Whenever a character kills a crystal lizard, they immediately place one Titanite Scale card into their inventory."

As I would cut it (29 words):

> A character who kills a crystal lizard takes one Titanite Scale card into their inventory at once. When no Titanite Scale card remains, crystal lizards are no longer placed.

**2. The placing and scaling paragraphs.**

> "The models are placed during Encounter Start (see §7.5, Encounter Start). A crystal lizard is an enemy model with its own *data card* (see §8.2), and the rules for enemy models apply to it except where this chapter says otherwise. A crystal lizard takes its *turn* with the other enemy models, in descending *threat* order (see §7.5, Encounter Turn Order). On its turn it resolves the *behaviour icons* on its data card, which move it away from the characters. A crystal lizard makes no attack. A crystal lizard is not scaled. Neither enemy scaling (see §8.3) nor the *bonfire ascetic* (see §18.7) changes its health or its movement."

Source: "Crystal lizards take their turns like any other enemy model in descending threat order. However, their behaviours dictate that they simply run from the characters … Crystal lizards do not scale their health depending on the number of characters."

As I would cut it (32 words):

> A crystal lizard is an enemy model and takes its turn with the others in descending threat order. Its behaviour moves it away from the characters. A crystal lizard is not scaled.

**3. The memory rule.**

> "Once a crystal lizard has been killed in an encounter, no crystal lizard is placed in that encounter again, however many times the encounter is *reset* and fought (see §11.5). To record the kill, one *damage cube* is placed on the encounter card of that encounter, where it stays until the card is returned to the game box. Until a crystal lizard has been killed there, the crystal lizards are placed again each time the encounter is set up."

As I would cut it (35 words):

> Crystal lizards are placed each time their encounter is set up, until one is killed there. From then on none is placed in that encounter; a damage cube on the encounter card records the kill.

### Unintuitive or over-engineered rules

- **Party award instead of the killer's prize.** See above. The author's version is shorter, is what the table expects, and gives a reason to race for the kill.
- **Nine cross-references in eight paragraphs.** One sentence ("the rules for enemy models apply") makes six of them unnecessary.
- **Global shut-off when the three cards run out.** Sound, but written as two consequences (awards nothing; never placed again). The second makes the first impossible; say only the second.

---

## Chapter 15: Boss Encounters

Source 1,327 words. Final 4,262 words. Needs about 1,615.

### Section table

| § | source words | final words | words it needs | X count | main class of excess |
|---|---|---|---|---|---|
| 15 (chapter opening) | 136 | 55 | 45 | 0 | none; the one place in the group where the pipeline cut |
| 15.1 The Fog Gate | 116 | 418 | 110 | 10 | R (placement of the token, owned by §6.5 to §6.7; summon pointer), E (85-word example of a one-sentence shortcut), D ("does not bar the shortcut") |
| 15.2 Overview | 0 | 627 | 130 | 28 | R: a hub that restates §15.1, §15.3, §15.4, §15.5, §16.1, §16.5, §7.5, §12.1 and §12.2. A: nine-step setup and reset paragraph. 28 references in 627 words |
| 15.3 Boss Tiles | 61 | 331 | 110 | 11 | G ("Boss tile", "Boss spawn node"), D ("one tile for every rule" spelt out four ways), R (no encounter card, said in §15.2) |
| 15.4 Boss Data Cards | 196 | 407 | 170 | 13 | V ("The value beside the … icon is …" ten times), R (dial set, dial lowered, zero defeats: each said elsewhere), E (55-word subtraction example) |
| 15.5 Boss Behaviour Cards | 278 | 974 | 330 | 17 | A (deck built at setup; Deck Reset; heat-up timing), E (95-word heat-up example), R (Deck Renewal repeats §16.1; heat-up point defined four times in the chapter), D ("without looking at them") |
| 15.6 Arcs and Defence | 538 | 1,450 | 720 | 29 | R (attack, block and dial restated; summon die; "no arcs" for mimics and phantoms), E (115-word arc example), A (turning under characters, parry, boss cannot be pushed), D |
| **Chapter 15** | **1,327** | **4,262** | **1,615** | **108** | |

Sub-sections of §15.5: introduction 51 (needs 20), Card Anatomy 243 (110), Deck Construction 191 (80), Deck Renewal 94 (35), Heat-Up 303 (70), Deck Reset 92 (15).
Sub-sections of §15.6: Boss Arcs 227 (120), Facing and Turning 174 (80), Arc Diagrams 138 (90), Weak Arcs 325 (120), Characters and Arcs 354 (230), Defence 228 (80).

Approximate split of the final text by class: K 1,500, R 750, A 700, D 450, E 395, V 350, G 120 (X: 108 references, about 330 words, inside the other classes).

### Added rules (class A)

- §15.1 · the party enters only through the fog gate, "and the party passes through it together" · CH-15-004 (C-058, A-089) · A3 · delete; the party always moves together.
- §15.1 · the token stays on the bonfire tile until the boss is defeated; the next setup moves it on · CH-15-005 · A2 · one clause; the second half is §6.6's.
- §15.1 · encounters bypassed by the shortcut are "neither fought nor skipped": no stamina cube · CH-15-006 (Gate 1, OQ-10) · A1 · keep as one clause.
- §15.1 · an uncleared encounter on the route "does not bar the shortcut" · CH-15-006 (A-054) · A3 · delete; nothing suggests it would.
- §15.2 · nine-step boss encounter setup · CH-15-008 (A-122) · A2 · four of the nine steps are new and needed (characters on entry nodes, dial, boss on its spawn node facing the entry, aggro token). The other five repeat §15.1, §7.5, §12.1 and §17 or say "begin".
- §15.2 · boss faces the adjacent node closest to the entry nodes; players choose on a tie · CH-15-008 · A1 · keep. The source never said how the boss starts.
- §15.2 · special rules that name only a node keep the facing rule of step 6 · CH-15-044 (VB-003) · A3 · delete; "unless its special rules say otherwise" in the step covers it.
- §15.2 · "This rule applies to every boss, a mega-boss included" · CH-15-010 (Gate 1, OQ-14) · A3 · delete. It answers a rule (mega-boss permadeath) that the book no longer contains.
- §15.2 · reset of a failed boss encounter: model removed, deck rebuilt, dial reset, souls stay, "set up again from step 2" · CH-15-011 (A-043) · A2 · one sentence.
- §15.3 · joined boss tiles: no wall on the join, adjacency, movement, pushes and range across it · CH-15-012 (F-090) · A3 · the author's "treated as one large tile for all purposes" already says all four.
- §15.3 · the unused mini-boss spawn node is a basic node in a main-boss encounter · CH-15-014 (A-122) · A1 · keep, twelve words.
- §15.3 · entry nodes of a boss encounter defined; the same by route or by shortcut · CH-15-014 (C-062) · A2 · one sentence.
- §15.5 · "current behaviour card" as a term with a two-case definition · CH-15-019 (F-088, C-047) · A2 · "the card the boss drew most recently" is the author's rule and needs no term.
- §15.5 · deck built during setup, "not built at the start of the boss encounter", kept face down, not looked at except by a scry · CH-15-020 (A-043) · A2 · the reason is the gravestone scry. Say "built during setup" once. It is now said in §15.2, in Deck Construction twice, and implied by Deck Reset.
- §15.5 · undealt standard cards are set aside, not boxed, for a rebuild · CH-15-021 (A-043, §17.1) · A3 · no player needs to be told where unused cards wait.
- §15.5 · a boss heats up once per attempt · CH-15-023 (A-042) · A1 · keep, six words.
- §15.5 · heat-up carried out at the start of the boss's next turn; deck and discard pile gathered and reshuffled with the heat-up card · CH-15-040, CH-15-041 (boss-E01, boss-E02) · A2 · the reshuffle of the discard pile is a real choice and can stay. The timing rule is a distinction without a difference: the deck is not touched between the damage and the boss's next draw. The sentence that the weak arcs "do not change" until then guards against a problem the timing rule itself created.
- §15.5 · Deck Reset: three-step rebuild after a failed attempt · CH-15-025 (A-043) · A2 · "Each attempt at a boss is fought against a newly built behaviour deck."
- §15.6 · where the arc lines run for an orthogonal and a diagonal facing · CH-15-027 (F-129, A-122) · A1 · keep; it replaces a diagram the book does not have.
- §15.6 · a boss turns only by a movement icon or a turn icon, never when it attacks; may be left facing a wall · CH-15-028 (F-133) · A2 · the first half in one clause; delete the wall sentence.
- §15.6 · a character on the boss's node stays put while the boss turns beneath them · CH-15-028 · A1 · keep; a real table question.
- §15.6 · with several arc diagrams on a card, the last one shows the weak arcs · CH-15-029 (F-131) · A1 · keep, one sentence.
- §15.6 · the weak-arc die applies at any range, to each roll of a repeat, and to a riposte; a summon gains it · CH-15-031 (A-037, A-119) · A2 · "every attack roll made from a weak arc, at any range".
- §15.6 · a character whose arc holds no valid adjacent node cannot leave the boss's node from that arc · CH-15-032 · A2 · keep as a clause; it follows from the author's same-arc rule.
- §15.6 · arc limit applies to pushes "whatever causes the push": push-move, push-attack, node model limit · CH-15-033 (A-036) · A3 · delete the list.
- §15.6 · a pushed character goes to a valid adjacent node of the players' choice in the arc (replaces "centre-most node") · CH-15-033 (A-036) · A1 · keep; this is simpler than the author's.
- §15.6 · parry only against a single-target attack; area, node and push-attacks cannot be parried · CH-15-035 (cross-reference from §9.6) · A2 · state it once, in §9.6 or here, not half in each.
- §15.6 · a boss cannot be pushed by characters; the push icon has no effect; not displaced by the node limit; pushed only by another boss model · CH-15-035, CH-15-046 (VB-005) · A3 here · §8.4 owns it; the Four Kings exception belongs in §17.10.
- §15.6 · mimics, invaders and summons have no arcs · CH-15-036 (A-044) · A3 · the fourth statement of this in the group; delete here.

### Worst passages

**1. §15.2 Overview (627 words, 28 cross-references, no source text).**

> "The boss's *behaviour deck* is built during setup, before the boss encounter begins, and is not built again at this point (see §15.5). When the characters pass through the *fog gate*, the boss encounter is set up as follows. 1. Move the fog gate token to the *bonfire* tile, if this is the first time … (see §15.1). 2. Place each character model on an *entry node* of the boss tile (see §15.3), no more than three models to a node (see §5.3). 3. Place on each character's *endurance bar* the *stamina cubes* owed for encounters skipped on the route (see §7.5, Encounter Start). 4. If the party called a *summon* at the fog gate, place the summon's model (see §12.1). … 7. Carry out any setup that the boss's special rules require (see §17). … 9. Begin the boss's first *turn* (see §16.1). … A summon takes its turns as §12.1 describes. No *invader* joins a boss encounter (see §12.2). When the boss's health is reduced to or below the *heat-up point* on its data card, the boss heats up, and a *heat-up card* joins its behaviour deck (see §15.5). A boss encounter ends in one of two ways. … This rule applies to every boss, a mega-boss included …"

Source: the author's overview held no rules. As I would cut it (118 words):

> A boss encounter is fought against a boss on a boss tile or on a mega-boss game board. It follows the rules for encounters except as this chapter and §16 state. When the characters pass through the fog gate, the encounter is set up as follows.
>
> 1. Place the character models on the entry nodes.
> 2. Set the boss's health dial to its starting health.
> 3. Place the boss model on its spawn node, facing the adjacent node closest to the entry nodes.
> 4. Place the aggro token on the character with the highest threat.
>
> The boss takes the first turn. A failed boss encounter is resolved and reset as any other, and the boss is fought again at full health with a newly built behaviour deck.

**2. §15.5 Heat-Up (303 words).**

> "**Heat-up point.** The health value, printed on a boss's data card, at or below which the boss heats up. A boss heats up when its health is reduced to or below its *heat-up point*. A boss heats up once in each attempt at its encounter. The heat-up is carried out at the start of the boss's next turn, before a card is drawn (see §16.1), as follows. 1. Gather the behaviour deck and the discard pile. 2. Take one card at random from the boss's heat-up cards, without looking at it, and add it to the gathered cards. 3. Shuffle the gathered cards face down to form the new behaviour deck. The boss then draws the top card of the new deck. Until that card is drawn, the boss's current behaviour card and its weak arcs do not change … The boss's other heat-up cards stay face down beside the boss tile and take no part in the encounter. … *Example.* A *mini-boss* has a heat-up point of 12 … [95 words]"

Source: "When the boss's health is reduced to (or below) its Heat Up point, take a random Heat Up behaviour card and shuffle it into the boss behaviour deck. Some bosses have special Heat Up rules which may allow them to Heat Up multiple times or otherwise override these rules."

As I would cut it (54 words):

> A boss heats up once, when its health is reduced to or below its heat-up point. One heat-up card, taken at random and unseen, is shuffled together with the behaviour deck and the discard pile to form a new behaviour deck. Some bosses heat up in other ways; their special rules replace this one.

**3. §15.1 The Fog Gate (418 words).**

> "The characters enter a boss encounter only by passing through the fog gate, and the party passes through it together. The boss encounter begins when the characters pass through (see §15.2). The party may pass through the fog gate when it advances from the last encounter tile of the route (see §7.5, Encounter Recovery). Before the characters pass through, an *embered* character may call a *summon* (see §12.1). … The encounters on the route are then neither fought nor skipped: no *stamina cube* is placed for them (see §7.5, Encounter Start). An encounter on the route that is not marked *cleared* does not bar the shortcut. The party may instead leave the shortcut unused and travel the route from the first encounter tile. Each encounter on the route is then fought or skipped as in any exploration … *Example.* … [85 words]"

Source (116 words): "The first time a character passes through the fog gate the fog gate tile should be removed from the boss-tile entryway and placed on the bonfire tile to serve as a shortcut. If the characters fail their first attempt at a boss encounter, they may use the fog gate to travel directly to the boss encounter … If the characters wish to forgo the fog gate to gain more souls and treasure they may proceed back to the boss encounter through their previous route encounter tiles."

As I would cut it (95 words):

> The characters enter a boss encounter by passing through the fog gate. The first time they pass through, the fog gate token is moved to the bonfire tile, where it stays until that boss is defeated. While it lies there it is a shortcut: a party setting out from the bonfire may pass through it and begin the boss encounter at once, and no stamina cube is placed for the encounters it bypasses. The party may instead travel the route to gain souls and treasure. In campaign play the fog gate is not a shortcut.

### Unintuitive or over-engineered rules

- **Heat-up "at the start of the boss's next turn".** A player expects the card to go in when the dial crosses the line, as the author wrote. Nothing reads the deck between that moment and the boss's next draw, so the delay changes nothing in play; it only adds a timing rule, a "weak arcs do not change" guard, and a second timing rule for bosses with special heat-ups. Drop the timing; keep the reshuffle if the author wants the discard pile included.
- **"Current behaviour card".** A term with a two-case definition ("the card being resolved during the boss's turn, and at every other time the card it resolved most recently") for what the author called "the most recently resolved behaviour card". The phrase "the card the boss drew most recently" needs no definition and is correct in both cases.
- **The deck is built at setup, and the book keeps apologising for it.** "Not built again at this point", "It is not built at the start of the boss encounter", cards "set aside … They take no part", then a Deck Reset procedure. One sentence in Deck Construction is enough, and the rebuild is one sentence in the reset rule.
- **§15.2 as a second table of contents.** A reader looking for how a boss fight starts must pick four real steps out of nine and then read six paragraphs that each summarise another section. Every summary is a second place for the rule to be looked up and a second place for it to drift.
- **Parry and "bosses cannot be pushed" split across chapters.** §9.6 forbids parrying a boss "except where §15.6 allows", and §15.6 allows it "when … the conditions for a parry are met (see §9.6)". A reader is sent in a circle. One section should hold the whole rule.
- **Same-arc push with the wall fallback.** This is the author's own rule, tidied (the "centre-most node" has gone, which is an improvement). The fallback, "pushed to any valid adjacent node that touches that wall", is still hard to apply at the table. Simpler: if the arc holds no valid adjacent node, the players choose any valid adjacent node. Lost: a small positional penalty in corners.
- **Joined boss tiles.** "The joined tiles are one tile for every rule" is followed by three sentences listing rules for which they are one tile. The list invites the question of what it leaves out.

---

## Chapter 16: Boss Turns

Source 910 words. Final 3,553 words. Needs about 915. This chapter has the highest ratio of restatement in the group: most of §16.3 and half of §16.2 repeat chapters 8, 9 and 15 "by reference".

### Section table

| § | source words | final words | words it needs | X count | main class of excess |
|---|---|---|---|---|---|
| 16 (chapter opening) | 0 | 54 | 0 | 0 | V: flavour added by the pipeline (CH-16-001) |
| 16.1 Overview | 173 | 595 | 170 | 16 | R (the equal-turns rule said twice; skipped icons of §9.1; heat-up timing a third time), E (115-word example), D ("A tie in threat is settled as in any encounter", in a section where threat order does not apply) |
| 16.2 Boss Movement and Symbols | 345 | 1,264 | 375 | 21 | E (two examples, 205 words, filed under Turn Icons), A (push-move differences, leap edge cases), R (path rules of §9.2; turn icons of §15.6; leap said three times), G ("Leap") |
| 16.3 Boss Attacks | 140 | 708 | 170 | 20 | R: Targets, Damage/Pushes/Conditions and Defence (470 words) restate §9.3, §9.4, §8.4, §8.5 and §15.6. E (130-word example), G ("Area attack") |
| 16.4 Boss Aggro | 125 | 367 | 70 | 7 | A (definition of "inflicts damage", riposte timing, other enemy models), R (summon and Distract, third statement), E |
| 16.5 Boss Death | 125 | 565 | 130 | 21 | R (steps 2, 5, 6, 7 are §7.7, §7.3, §20.1, §6.6), D (four closing paragraphs of "once", "not", "no"), E (105-word example of a checklist) |
| **Chapter 16** | **910** | **3,553** | **915** | **85** | |

Sub-sections of §16.2: introduction 110 (needs 25), Towards a Target 173 (90), Away from a Target 125 (60), Without a Target 83 (40), Characters on a Node the Boss Enters 94 (50), Push-Moves 210 (50), Leap 210 (60), Turn Icons 259 (0; §15.6 owns them).
Sub-sections of §16.3: introduction 95 (30), Targets 120 (15), Area Attacks 143 (65), Damage, Pushes, and Conditions 111 (0), Defence 239 (60, the example at half length).

Approximate split of the final text by class: R 1,050, K 900, E 615, A 450, D 300, V 180, G 60 (X: 85 references, about 270 words, inside the other classes).

### Added rules (class A)

- §16.1 · boss encounters are fought in "rounds"; the players choose the order; threat order does not apply · CH-16-003 (A-019, A-022) · A2 · the author's one sentence ("cannot take a turn until every other character has taken an equal number") already gives it. Add "living" and stop.
- §16.1 · a dead character takes no turn and is not counted · CH-16-003 (A-019) · A1 · keep; the literal source rule stalled the fight after a death.
- §16.1 · boss turn as five steps, with "place it face up beside the deck" and a discard step · CH-16-005 (C-120) · A2 · three steps: renew if empty, draw, resolve left to right (repeating if the card says so).
- §16.1 · on a repeat, each icon's target is determined again · CH-16-006 (A-024) · A1 · keep, one clause.
- §16.1 · an unresolvable icon is skipped; conditions affect a boss · CH-16-007 · A3 here · both are the enemy rules the chapter says apply.
- §16.1 · heat-up due is carried out before step 1; heat-up caused in the boss's own turn waits for its next turn · CH-16-034, CH-16-035 (boss-E04, boss-E05) · A3 · patches for the timing rule of boss-E01; they go when it goes.
- §16.1 · a boss defeated during its own turn (by a riposte) stops at once · CH-16-007 (A-018) · A2 · §16.5 says "the encounter ends at once"; that is enough.
- §16.2 · a boss follows the shortest path of valid nodes, as an enemy does; players choose between equal paths · CH-16-010 (A-082) · A1 · keep as one clause; the source's "adjacent node closest to the target" walked bosses into terrain.
- §16.2 · movement away: each node must be at greater range; blocked movement is lost · CH-16-010 · A2 · "as an enemy does".
- §16.2 · movement without a target stops at an invalid node · CH-16-012 (A-082) · A1 · keep, one sentence.
- §16.2 · a boss model does not count towards the node model limit · CH-16-013 · A3 here · §5.3 owns it.
- §16.2 · push-move "with three differences", including a two-stage fallback for a character who cannot be pushed directly away · CH-16-014 (A-036, dependency from §8.4) · A4 · see "Unintuitive rules" below.
- §16.2 · leap: three-step procedure; target on the boss's own node; a character with no valid adjacent node stays and picks an arc · CH-16-015 (A-038, C-033) · A2 · the author's sentence plus "A character who cannot be pushed stays on the node."
- §16.3 · attack value "fixed and not scaled"; range counted from the boss's node · CH-16-017 · A3 · restatement of §8.3 and §5.4.
- §16.3 · node attacks, nearest-character attacks, summon counted as a character · CH-16-018 · A3 here · owned by §9.3 and §12.1.
- §16.3 · area attack: a character on the boss's own node is targeted if their arc is an attack arc · CH-16-019 · A1 · keep, one sentence.
- §16.3 · "The aggro token and the nearest character play no part in an area attack" · CH-16-019 · A3 · delete.
- §16.4 · damage to another enemy model placed by a boss's special rules moves the token · CH-16-036 (boss-E06) · A2 · this exists for one boss (the Executioner's Chariot). Put it in that boss's entry.
- §16.4 · definition of "inflicts damage": bleed counts; an attack reduced to nothing does not · CH-16-023, CH-16-038 (A-018, lead-E13) · A3 · "inflicts damage" means what it says.
- §16.4 · riposte damage moves the token at the end of that boss turn; with several ripostes, the last · CH-16-023 (A-018) · A2 · covered by "the token moves to the last character to inflict damage on the boss".
- §16.4 · holder dies: token to the living character with the highest threat · CH-16-023 · A1 · keep, one sentence.
- §16.5 · characters who died in the encounter also gain the soul reward and the ember · CH-16-025, CH-16-027 · A1 · keep as two words: "dead or alive".
- §16.5 · unawarded boss treasure cards return to the box; no ember card is discarded · CH-16-025 · A3 · delete.
- §16.5 · the spark is added by the setup step, once, "whether or not a PvP encounter is fought"; cleared-encounter recovery is not carried out · CH-16-026 (Gate 1, OQ-15) · A2 · state the spark and the free rest as steps, as the author did.
- §16.5 · a boss with several models is defeated only as its own rules say · CH-16-037 (boss-E07) · A2 · one sentence, or leave it to §17.1.
- §16.5 · PvP encounter as step 6, and a last one after the final boss · CH-16-025, CH-16-039 (Gate 1, OQ-30; VB-007) · A2 · belongs in chapter 20; players who do not use PvP read it twice here.

### Worst passages

**1. §16.3: Targets; Damage, Pushes, and Conditions; Defence (470 words of restatement).**

> "An attack icon that shows the skull icon *targets* the character who holds the *aggro token*. An attack icon that shows the nearest-character icon targets the *nearest character* (see §9.2). A *summon* is counted as a character when the target is determined (see §12.1). The target is attacked in whatever *boss arc* they stand. If the target is not within the card's range, the icon is skipped … An attack icon that shows the *magical damage* icon deals magical damage, which a character *resists*. Every other boss attack deals *physical damage*, which a character *blocks* (see §9.4). … An attack icon that shows a *condition* icon places the matching condition token on each character it hits (see §8.5). … Each character targeted by a boss's attack chooses one defence before any dice are rolled, as against any enemy attack (see §9.3, Defence). … A character who dodges is not hit: the character suffers no damage, is not pushed, and receives no condition token (see §8.1)."

Source: "Boss attacks follow the same rules as enemy attacks but can contain additional symbols with more powerful effects." The change log says of these paragraphs that they are "stated by reference to their owning sections" (CH-16-018, CH-16-020).

As I would cut it (54 words, replacing the introduction and all three sub-sections; Area Attacks stays):

> A boss attacks as an enemy attacks, with the range and dodge difficulty printed on the behaviour card it drew. A boss does not change its facing when it attacks. A character who is hit by a push-attack while on the boss's own node is pushed within the arc in which they are placed.

**2. §16.5 Boss Death (565 words, 21 cross-references).**

> "1. Award each character, including each character who died in the encounter, the boss soul reward (see §7.6). 2. Shuffle the boss's *boss treasure* cards, draw one at random, and award it to the party (see §7.7). 3. Return the boss's other treasure cards to the game box. 4. Place an *ember token* in the ember slot of every character's dashboard, including each character who died in the encounter. Every character is *embered*, and no *ember card* is discarded (see §7.3). 5. Remove every *damage cube* and every *hollow cube* from each living character, as for any embering (see §7.3). 6. If PvP encounters are in play … 7. Carry out the setup that follows the boss … The setup of step 7 adds one *spark* to the spark dial. This is the spark that each defeated boss grants (see §7.4). … The spark is gained once and the rest is taken once for each defeated boss, whether or not a PvP encounter is fought (see §20.9). The recovery that follows a *cleared* encounter is not carried out after a boss … The embering of step 4 provokes no *invasion* at that moment (see §12.2). …"

Source: "When the boss's health dial is reduced to zero, the boss is slain and the encounter ends. If this was the final boss (main or mega), the characters are victorious and the players win. If not, determine boss treasures and collect soul rewards as previously described. Then, increase the spark dial by one and give each character an ember token to mark them as embered. Finally, the characters return to The Bonfire to rest at no spark cost. They may visit the Firekeeper and Andre if they wish."

As I would cut it (97 words):

> A boss is defeated when its health dial is reduced to zero, and the encounter ends at once. If it is the final boss, the players win the game. Otherwise its defeat is resolved as follows.
>
> 1. Every character, dead or alive, gains the boss soul reward.
> 2. One of the boss's treasure cards, drawn at random, is awarded to the party.
> 3. Every character becomes embered.
> 4. One spark is added to the spark dial.
> 5. The characters return to the bonfire and rest without spending a spark.
>
> The setup that follows the boss is then carried out (see §6.6, §6.7).

**3. §16.4 Boss Aggro (367 words).**

> "In a boss encounter the aggro token does not move at the end of a *round* as it does in other encounters (see §7.5, Encounter Turn Order). At the end of each character's *turn*, if that character inflicted damage on the boss during the turn, the aggro token moves to that character. Damage inflicted on another enemy model that the boss's special rules place in the encounter moves the token in the same way (see §17). If the character inflicted no such damage, the token stays with its holder. A character inflicts damage on a boss when the character's attack, or a *bleed* that the attack triggers, lowers the boss's *health dial* by one or more. An attack that the boss's *block* or *resist* reduces to no damage does not move the token. A *riposte* is made during the boss's turn (see §9.6). If a riposte inflicts damage on the boss, the aggro token moves to the character who made it at the end of that boss turn, after the behaviour card has been resolved. If more than one character ripostes in the same boss turn, the token moves to the last of them to inflict damage. …"

Source: "simply move the aggro token to a character's dashboard if they deal any damage to the boss during their turn. If no damage is dealt, the aggro token remains stationary for that turn."

As I would cut it (60 words):

> The aggro token is placed on the character with the highest threat when the boss encounter is set up. At the end of any turn in which a character inflicted damage on the boss, the token moves to the last character to have done so. If its holder dies, the token moves to the living character with the highest threat.

### Unintuitive or over-engineered rules

- **The push-move fallback cascade (§16.2, CH-16-014).** A character on a node the boss enters is pushed directly away; failing that, within the arc in which the node lay before the boss entered; failing that, along the wall. The book needs a 155-word example to show it, and the example ends with two characters sliding along a wall. Simpler: "A character on a node the boss enters is pushed directly away from the boss; if no valid node lies there, the character's player chooses any valid adjacent node." Lost: nothing a player would notice.
- **Two movements onto an occupied node with opposite results.** An ordinary move leaves the characters on the node, set against the boss's base; a push-move throws them off; a leap throws them off with different limits. Each is the author's, but the final text spreads them over three sub-sections with three sets of exceptions. A three-row table (move: stay, placed in arc; push-move: pushed away; leap: pushed anywhere) would carry all of it.
- **Leap said three times.** The bold definition, the numbered steps and the paragraph after them each say that the boss is placed on the target's node at any distance. The author's single sentence was complete apart from naming the icon.
- **Turn icons and Defence each live in two chapters.** §15.6 Facing and Turning and §16.2 Turn Icons; §15.6 Defence and §16.3 Defence. A player looking for either finds half an answer and a pointer.
- **Aggro timing by case.** Turn damage moves the token at the end of the character's turn; riposte damage at the end of the boss's turn; several ripostes, the last. One rule ("the last character to inflict damage, at the end of that turn") gives the same results without cases.
- **"Rounds" in a fight that has no round structure.** The boss chapter imports the word to restate the equal-turns rule, then has to say that the round-end aggro rule and the threat order of other encounters do not apply. The author's sentence about equal turns needs no "round".
- **Boss Death steps that are other chapters' steps.** The spark and the free rest, which the author states plainly, have become "the setup of step 7 adds one spark … This is the spark that each defeated boss grants". A player wants to read "add one spark; rest for free" at the moment the boss falls.

---

## Totals for the group

| Chapter | source words | final words | words needed | growth | excess |
|---|---|---|---|---|---|
| 12 Phantoms | 543 | 2,462 | 845 | ×4.5 | 1,617 |
| 13 Mimics | 438 | 1,337 | 520 | ×3.1 | 817 |
| 14 Crystal Lizards | 274 | 397 | 260 | ×1.4 | 137 |
| 15 Boss Encounters | 1,327 | 4,262 | 1,615 | ×3.2 | 2,647 |
| 16 Boss Turns | 910 | 3,553 | 915 | ×3.9 | 2,638 |
| **Group** | **3,492** | **12,011** | **4,155** | **×3.4** | **7,856** |

The group needs about 19% more words than the author wrote (4,155 against 3,492). That margin pays for the rules the source truly lacked: how a boss encounter is set up, how a summon is attacked, where a mimic stands, how to read an arc diagram. Everything above it is excess.

Split of the 7,856 excess words by class (approximate; cross-references are carved out of the classes they sit in):

| Class | words | share |
|---|---|---|
| R restated | 2,195 | 28% |
| D defensive | 1,270 | 16% |
| A added rules beyond the short fixes kept | 1,215 | 15% |
| E examples (15 examples, 1,310 words; about 155 kept) | 1,155 | 15% |
| V verbose | 985 | 13% |
| X cross-references (275 in the group; about 30 worth keeping) | 780 | 10% |
| G glossary-in-chapter | 255 | 3% |

## How it happened

1. **Silences were filled with sub-sections, not sentences.** Where the source said nothing, a completion finding produced a full procedure with its own edge cases. §12.1 Summons in Combat: 315 words from nothing (CH-12-010, CH-12-011; CMP-0018, D-010). §15.2 Overview: a nine-step setup and five summary paragraphs, 627 words from nothing (CH-15-008, CH-15-009; A-122). In each case three or four sentences were needed.

2. **"One owner, cited everywhere" doubled the text instead of halving it.** The pipeline gave each rule an owning section and then wrote a sentence plus a "(see §…)" in every other section that touched it. §16.3 Targets, Damage and Defence are 470 words "stated by reference to their owning sections" (CH-16-018, CH-16-020). §12.1 repeats the trap rule of §5.5 "as a pointer in the section where a reader looks for it" (CH-12-012). The result is 275 cross-references in 12,000 words, one every 44 words.

3. **One action per step.** The style rule that procedures be numbered with one action per step (C-120) turned sentences into lists. The author's four-item invader setup became seven steps (CH-12-018, CH-12-022); the mimic's return to its chest became four steps (CH-13-021); boss defeat became seven steps, four of which are other chapters' rules (CH-16-025). Steps such as "Leave every character model on the node it occupies" and "Begin the boss's first turn" exist only to complete a list.

4. **Defensive closure.** Each audit pass asked "could a player wonder whether…?" and answered in the text. The summon's list of eight things it lacks was written "so that no player asks whether a model with dodge dice may parry" (CH-12-036, phantom-E02). The mimic's list of five boss rewards it does not grant guards against the chapter's own phrase "fought as a mini-boss encounter" (CH-13-015). "Mimics, invaders, and summons have no arcs" is stated in four places (CH-12-026, CH-13-014, CH-15-036 and §12.1).

5. **Patches on patches.** A late ruling changed one rule, and every section that mentioned the rule received a sentence to stay in step. The heat-up timing of boss-E01 (CH-15-040) required a new example (CH-15-041, boss-E02), two insertions in §16.1 (CH-16-034, CH-16-035; boss-E04, boss-E05), and one each in §12.2 and §13.2 (CH-12-047, CH-13-031; lead-E17, lead-E18). The black-cube qualifier of phantom-E04 (CH-12-038) needed five follow-up entries (CH-12-040 to CH-12-043). The same mechanism wove campaign and single-boss exceptions into the base rules: campaign tiers in §12.2 and §13.2 (CH-12-037, CH-12-048, CH-13-027), the Executioner's Chariot in §16.4 (CH-16-036, boss-E06), three chapter 17 placements in §15.2, §15.3 and §15.6 (CH-15-044 to CH-15-046; VB-003 to VB-005).

6. **Examples and house apparatus added by policy.** Fifteen worked examples total 1,310 words, more than a third of the author's whole text for these chapters; the change log says of several that they "state no rule" (CH-12-015, CH-12-021, CH-13-019, CH-16-016). The same policy layer added the optional-rule formula to three chapters (CH-12-002, CH-13-002, CH-14-002; C-124), bold in-chapter definitions that duplicate the glossary (Phantom, CH-12-001; Leap, CH-16-015; Area attack, CH-16-019), and flavour introductions the source did not have (CH-16-001).

A seventh, smaller mechanism deserves a line: **rulings that changed the author's rule without being asked to.** The mimic rematch became optional (CH-13-021), the lizard's prize became a party award (CH-14-012), the invader token is revealed later (CH-12-019), and mimic stamina is shed (CH-13-026). Each then needed explanatory text the author's version did not.

## Ten cuts, in order of words saved

1. **Delete eleven of the fifteen worked examples and halve the rest** (keep, at half length: the mimic example in §13.3, the arc example in §15.6 Weak Arcs, the area attack example in §16.3, the same-node arc movement example in §15.6). About 1,150 words. Loss: none; the deleted examples illustrate rules of one or two sentences.
2. **Strip the cross-references** to roughly one per sub-section, keeping those that send the reader to a rule they cannot guess the place of. About 780 words (some overlap with the cuts below). Loss: none.
3. **Rewrite §15.2 Overview as the four-step setup and two sentences** (worst passage 1 of chapter 15). About 500 words. Loss: none; every summary paragraph has an owner elsewhere.
4. **Replace §16.3 Targets, Damage/Pushes/Conditions and Defence with three sentences.** About 420 words. Loss: none; "a boss attacks as an enemy attacks".
5. **Cut §13.2 to one paragraph and §13.3 to four sentences**, restoring the author's "recover nothing" and forced rematch. About 420 words. Loss: the stamina shed, if the author wants it back, costs one sentence.
6. **Cut §16.5 Boss Death to the author's five consequences as a list.** About 330 words. Loss: PvP and campaign pointers, which belong to chapters 18 and 20.
7. **Cut §12.2 Invasions and Invader Tokens to one trigger sentence and the author's five steps.** About 310 words. Loss: the blank-token shortfall note moves to chapter 18.
8. **Cut §12.1 Summons in Combat and Removal of a Summon to five sentences.** About 305 words. Loss: none.
9. **Cut §15.5 Heat-Up, Deck Renewal and Deck Reset to one short rule each**, dropping the "start of the next turn" timing. About 300 words, and a further 60 in §16.1, §12.2 and §13.2 where the timing is echoed. Loss: none in play.
10. **Cut §16.4 Boss Aggro to three sentences.** About 240 words. Loss: the Executioner's Chariot clause moves to that boss's entry.

Together these remove about 4,750 words (allowing for overlap between cut 2 and the others, about 4,400), or about 56% of the group's excess, without removing a rule the author wrote.
