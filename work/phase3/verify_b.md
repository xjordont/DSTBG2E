# Verification B: chapters 12 to 20, F.A.Q., appendices, glossary N to Z

Scope read in full: `10_manuscript_chapter_12` to `_20`, `_22_faq`, `_23_appendices`, `12_glossary.md`; governing rules read in full: chapters 05 to 11 (and §2.3, §2.5, §2.9, §3.3 to §3.5, §4.2). Booklets compared: Four Kings, Gaping Dragon, Guardian Dragon, Last Giant, Manus, Old Iron King, Vordt, Asylum Demon (rules and campaign pages), plus the campaign pages and component lists of Kalameet, Executioner's Chariot, Phantoms, Darkroot, Iron Keep, Explorers and the core rulebook. Memos read: `rulings_boss.md` (lead items, chapter 17, unsettled points), `rulings_campaign.md` (chapters 18 and 19, follow-up), `06_final_rulings.md` §3 to §5.

Note on the state of the files: chapters 12 to 20, 22 and 23 did not change during this verification. One commit landed while it ran (d664a01, §8.5 Stagger and the glossary entry Stagger: a staggered summon takes the roll-based penalty). The glossary entry Stagger was re-checked against the new §8.5 and agrees.

Severity is given in each Problem line: high (play stops or two rules give different results), medium (a reader following one section is misled), low (incomplete statement or citation).

---

## Chapter 12: Phantoms

### VB-001 · 10_manuscript_chapter_12_phantoms.md · §12.2, Invader Tokens, step 1 · inconsistency
- Text: "1. Draw one invader token at random and keep it face down: a standard invader token if the mini-boss has not been defeated, an advanced invader token if it has."
- Problem: low to medium. In campaign play the token is keyed to the current tier, not to the mini-boss (§12.2, opening paragraph; §18.1, Section Setup, last bullet: "a standard invader token until the *bonfire ascetic* is burnt"). The numbered step states only the standard-game test and gives the opposite answer in a campaign once a mini-boss has fallen (for example Section Two of The Coiled Sword before the bonfire ascetic is burnt). The memo `rulings_campaign.md`, part (c), asked for a pointer in this step; the opening paragraph received it and the step did not.
- Correction: "1. Draw one invader token at random and keep it face down: a standard invader token if the mini-boss has not been defeated, an advanced invader token if it has. In campaign play, draw a standard invader token while the current tier is tier one and an advanced invader token once it is tier two (see §18.1, Section Setup)."

### VB-002 · 10_manuscript_chapter_12_phantoms.md · §12.2, Invader Tokens · cross-reference
- Text: "Some campaigns place named invaders in listed encounters and use no invader tokens (see §19.3; §19.4)."
- Problem: low. §19.15 (Treasures of the Ice Cave), added today, is a third such campaign; §12.2, End of an Invasion already cites it.
- Correction: "Some campaigns place named invaders in listed encounters and use no invader tokens (see §19.3; §19.4; §19.15)."

Chapter 12 otherwise agrees with §7.5, §7.6, §15.5, §16.4, §18.1 and §2.4 (Eygon of Carim and Sword Master are standard summons; Maneater Mildred is a standard invader; three blank tokens exist).

## Chapter 13: Mimics

No defect. §13.2 (stamina cubes removed, damage kept, tier keying in campaign play), §13.3 and its example, and §13.4 agree with §7.5, §7.6 (Level 2 full reward 4), §7.7, §15.5 and §16.4.

## Chapter 14: Crystal Lizards

No defect. The award to the party agrees with §7.7 and §11.4, Sales.

## Chapter 15: Boss Encounters

### VB-003 · 10_manuscript_chapter_15_boss_encounters.md · §15.2 · ambiguity
- Text: "If a boss's special rules state where the boss is placed or how it faces, those rules replace step 6 (see §17)."
- Problem: medium. Several entries state the node and no facing: the Four Kings (§17.10, Setup, step 1), the Old Iron King (§17.10, Setup, step 1: "on the *Iron King node* opposite the doorway"), the Asylum Demon (§17.3, Setup: "placed on the mega-boss *spawn node*"), the Executioner's Chariot (§17.9, Setup, step 2). Read as written, each of these replaces the whole of step 6, and the starting facing is then stated nowhere. The Old Iron King's rule that no character stands in its back arc depends on that facing, and its booklet gives one (DS-OIK-Rules-web.txt, "Starting the Old Iron King Mega Boss Encounter", lines 349 to 356: "with its front arc facing the centre of the mega boss game board"). The memo (boss-014) intends the general facing of step 6 to apply to every such entry; the sentence must say so.
- Correction: "If a boss's special rules state where the boss is placed or how it faces, those rules replace that part of step 6, and the rest of the step applies (see §17)."

### VB-004 · 10_manuscript_chapter_15_boss_encounters.md · §15.3, Boss spawn node · inconsistency
- Text: "The boss model is placed on it at the start of every boss encounter (see §15.2)."
- Problem: low. Three entries place a boss model elsewhere: Smough on the mini-boss spawn node (§17.2, Setup), the Asylum Demon, a mini-boss, on the mega-boss spawn node (§17.3, Setup), the Old Iron King on an Iron King node (§17.10). The glossary entry Boss spawn node (other half) repeats the sentence.
- Correction: "The boss model is placed on it at the start of every boss encounter, unless the boss's special rules name another node (see §15.2; §17)."

### VB-005 · 10_manuscript_chapter_15_boss_encounters.md · §15.6, Defence · inconsistency
- Text: "A boss model is pushed only when another boss model moves onto its node (see §17.1)."
- Problem: medium. The royal summons places the next king on the mega-boss spawn node and pushes "every other model on that *node*" (§17.10, The Four Kings, step 2), which includes a king that stands there; a node holds at most one boss model (§5.3; §17.1). The booklet says the same ("Any other models on the node are pushed onto an adjacent node", DS-Four-Kings-Rules-web.txt, Royal Summons, step 1). A placed king does not "move onto" the node, so §15.6 forbids a push that §17.10 requires.
- Correction: "A boss model is pushed only when another boss model moves onto its node or is placed on it (see §17.1; §17.10, The Four Kings)."

### VB-006 · 10_manuscript_chapter_08_combat_basics.md · §8.4 · inconsistency (outside half B; consequential on VB-005)
- Text: "The only push that affects a boss model is the push caused by another boss model moving onto its node (see §17.1)."
- Problem: medium. Same contradiction with §17.10, The Four Kings, step 2 as VB-005.
- Correction: "The only push that affects a boss model is the push caused by another boss model that moves onto its node or is placed on it (see §17.1; §17.10, The Four Kings)."

All five examples of chapter 15 follow from the rules (see the count at the end).

## Chapter 16: Boss Turns

### VB-007 · 10_manuscript_chapter_16_boss_turns.md · §16.5 · inconsistency
- Text: "In campaign play the spark, the rest, and the setup that follow a boss differ (see §18.1; §18.3)."
- Problem: low. Step 6 of the same section orders a PvP encounter after every boss. In campaign play a PvP encounter follows only a boss whose defeat completes a section (§18.1, Player versus Player Encounters). The sentence lists what differs in campaign play and omits the PvP encounter.
- Correction: "In campaign play the PvP encounter, the spark, the rest, and the setup that follow a boss differ (see §18.1; §18.3)."

All six examples of chapter 16 follow from the rules. §16.4 agrees with §7.5, §8.5, §12.1 and §17.1.

## Chapter 17: Boss Special Rules

### VB-008 · 10_manuscript_chapter_17_boss_special_rules.md · §17.6, Pursuer · ambiguity
- Text: "When the Pursuer's health is reduced to or below its *heat-up* point {{icon:ast-0030-heat-up-point}}, one random heat-up card is shuffled into its behaviour deck, as for any *boss* (see §15.5). From that moment until the *encounter* ends, the *attack value* of every attack on the Pursuer's behaviour cards is increased by one."
- Problem: medium. Since today the heat-up is carried out at the start of the boss's next turn and gathers the discard pile (§15.5, Heat-Up). "From that moment" now has two readings: the moment the health falls (a second card of the same turn, after a riposte, would gain the +1) or the moment the heat-up is carried out. The Old Iron King's entry states the second ("takes effect when the heat-up is carried out"); the Pursuer's must match. "shuffled into its behaviour deck" also describes the old procedure. Booklet: "After heat up, add 1 card to the behaviour deck, and increase all damage by +1" (DS-Explorers-Rules-Web.txt, lines 215 to 221).
- Correction: "When the Pursuer's health is reduced to or below its *heat-up* point {{icon:ast-0030-heat-up-point}}, it heats up as the general rule directs (see §15.5, Heat-Up). From the moment the heat-up is carried out until the *encounter* ends, the *attack value* of every attack on the Pursuer's behaviour cards is increased by one."

§17.2 (two models, own health dials, heat-up when the first falls, healing of 10 or 15 capped at the starting health) agrees with §17.1, §16.5, §2.3 and F.A.Q. §22.5; its example is right (22 + 15 = 37, capped at 30).

Comparison of §17.3 and of the seven new entries of §17.10 with the booklets: see the table at the end. No number, count, setup step or special rule differs from its booklet, apart from the facing covered by VB-003 and the deliberate restatements listed in the memos (heat-up timing, "removes one *damage cube*" for "gains 1 Health", scry in place of the gravestone reveal, aggro token on the highest *threat*).

## Chapter 18: Campaign Play

### VB-009 · 10_manuscript_chapter_18_campaign_play.md · §18.1, Section Completion · ambiguity
- Text: "Each character who died in the boss encounter is revived as after any cleared encounter, except that the ember token of the boss's defeat keeps that character from becoming *hollow*, so no hollow cube is placed (see §7.5, Encounter Recovery; §16.5). The exploration then continues."
- Problem: medium. This is the case of a boss that does not complete its section (the Stray Demon in §19.16, Section Five). §16.5 states that "The recovery that follows a *cleared* encounter is not carried out after a boss", because a rest follows; here no rest follows. The paragraph restores the dead (all stamina cubes, damage cubes and condition tokens removed) and says nothing of the survivors, who by the letter keep every stamina cube into the next encounter. Two readings: (a) the survivors do not recover; (b) the survivors recover as after any cleared encounter. Reading (b) is the one to choose: it is what "as after any cleared encounter" already grants the dead, and under (a) a character is better off dead than alive when the boss falls.
- Correction (judgement call, not in the JSON): "Each surviving character recovers, and each character who died in the boss encounter is revived, as after any cleared encounter, except that the ember token of the boss's defeat keeps a revived character from becoming *hollow*, so no hollow cube is placed (see §7.5, Encounter Recovery; §16.5). The exploration then continues."

Chapter 18 otherwise agrees with itself and with §6.6, §6.7, §7.4, §7.6, §8.3, §11.2 to §11.4, §12.2, §13.2, §16.5 and §20. All three examples are right.

## Chapter 19: Campaigns

### VB-010 · 10_manuscript_chapter_19_campaigns.md · §19.15 · ambiguity
- Text: "Both invaders are part of that encounter every time the characters enter it, until both have been killed during one visit. If either invader vanishes, or the encounter is *failed*, both return the next time the characters enter it."
- Problem: high. In Section Three the paired invaders stand in a Level 4 encounter (Guarded Path). If a character dies, both invaders vanish (§12.2, Combat with an Invader); the survivors can then kill the remaining enemies, and the encounter is *cleared*. A cleared Level 4 encounter "is not fought again" (§18.1, Level 4 Encounters and Mega-Bosses; §6.7), yet the section "is completed only when that encounter is *cleared* and both of its invaders have been killed". The campaign cannot go on. The same event in Section One leaves a Level 2 encounter that carries a black cube and may be skipped (§7.5, Encounter Start), with nothing beyond it. Booklet: "If the party dies during this encounter both invaders will respawn. The party proceeds to Section 2 when the encounter is defeated" (DS-VotBV-Rules-web.txt, campaign pages, Sections 1 and 3). Two readings: (a) keep the vanishing rule of §12.2 and let such an encounter be fought again; (b) follow the booklet's narrower wording, so that the invaders do not vanish at a character's death and return only after a *failed* encounter. Reading (a) is the one to choose: it keeps §12.2 whole and needs one sentence.
- Correction (judgement call, not in the JSON), added to the end of the first bullet: "An encounter that is *cleared* before both of its invaders have been killed is fought again when the characters next enter it, the Level 4 encounter of Section Three included, and it is not skipped."

### VB-011 · 10_manuscript_chapter_19_campaigns.md · §19.16, Section Five · ambiguity
- Text: "The defeat of the Stray Demon does not complete Section Five."
- Problem: medium. Section Five lists Level 4 encounter, Stray Demon, Level 4 encounter, Black Dragon Kalameet. §18.1 states that a mega-boss "is set up when the section's last Level 4 encounter is cleared" and that two Level 4 encounters of a section are fought "one after the other" on one game board. Read with §18.1, the Stray Demon would follow the second Level 4 encounter. The booklet's order is the listed one (DS-GD-Rules-web.txt, Section 5, The Final Conflict). The section must say that the list order governs.
- Correction: "The encounters of Section Five are fought in the order listed: the Stray Demon is fought when the first Level 4 encounter is cleared, and the second Level 4 encounter is set up when the Stray Demon is defeated. The defeat of the Stray Demon does not complete Section Five."

### VB-012 · 10_manuscript_chapter_19_campaigns.md · §19.12 · ambiguity
- Text: "The party may replace the mega-boss of any of these three sections with another mega-boss it owns, and may add further sections of the same form."
- Problem: low. The paragraph before ends "The players win the campaign when all three are completed", which no longer holds when further sections are added.
- Correction: "The party may replace the mega-boss of any of these three sections with another mega-boss it owns, and may add further sections of the same form; the players then win the campaign when every such section is completed."

Every section list of §19.1 to §19.16 was compared with its booklet (encounter levels, order, named encounters, bosses, section names). All sixteen agree; see the table at the end.

## Chapter 20: Player versus Player

### VB-013 · 10_manuscript_chapter_20_player_versus_player.md · §20.1 · inconsistency
- Text: "When PvP encounters are in play, one *PvP encounter* is fought after each *mini-boss*, *main-boss*, and *mega-boss* is defeated."
- Problem: medium. In campaign play a PvP encounter follows only a boss whose defeat completes a section (§18.1, Player versus Player Encounters, changed today). §20.1 owns the rule and states it without the exception; the only pointer to §18.1 in the chapter (§20.9) concerns what follows a PvP encounter, not whether one is fought.
- Correction: "When PvP encounters are in play, one *PvP encounter* is fought after each *mini-boss*, *main-boss*, and *mega-boss* is defeated. In campaign play it is fought only after a boss whose defeat completes a *section* (see §18.1, Player versus Player Encounters)."

§20.4 (three defences; flat +1 in step 4) and §20.8 (one victory bonus, spare token, ultimate victor) agree with each other and with the glossary. All four examples are right.

## F.A.Q. (chapter 22)

### VB-014 · 10_manuscript_chapter_22_faq.md · §22.1 · faq
- Text: "**A.** Yes, while the characters are on the bonfire tile and at the cost of one *spark*. The new character begins with starting equipment, base stats, and no souls (see §18.4)."
- Problem: low. Incomplete against §18.4: the change is made only while no *encounter* is in progress, and "A player cannot join while the spark dial shows zero."
- Correction: "**A.** Yes, while the characters are on the bonfire tile, no encounter is in progress, and the spark dial shows one or more. The party spends one *spark* for each player who joins. The new character begins with starting equipment, base stats, and no souls (see §18.4)."

### VB-015 · 10_manuscript_chapter_22_faq.md · §22.6 · faq
- Text: "**A.** Yes. The invader vanishes at once and awards nothing, and the encounter continues against the remaining enemy models. The invader does not return (see §12.2, Combat with an Invader)."
- Problem: low to medium. Three points. The encounter does not continue when the death fails it (a *hollow* character, or the last living character; §7.2). "The invader does not return" is stated under End of an Invasion, not under the heading cited. Since today that rule carries an exception for two campaigns (§12.2, End of an Invasion: "unless a campaign states otherwise (see §19.4; §19.15)").
- Correction: "**A.** Yes, unless that death fails the encounter. The invader vanishes at once and awards nothing, and the encounter continues against the remaining enemy models. The invader does not return, unless a campaign states otherwise (see §12.2, Combat with an Invader; §12.2, End of an Invasion)."

### VB-016 · 10_manuscript_chapter_22_faq.md · §22.5 · faq
- Text: "**A.** Yes. The character is pushed to a valid adjacent node in the arc in which the character is placed. If a wall leaves no such node, the character is pushed to a valid adjacent node that touches the wall (see §15.6, Characters and Arcs)."
- Problem: low. The section cited ends with an exception that the answer omits: "The push that follows a *leap* is not limited by arcs" (§15.6, Characters and Arcs; §16.2, Leap).
- Correction: "**A.** Yes, except after a *leap*. The character is pushed to a valid adjacent node in the arc in which the character is placed. If a wall leaves no such node, the character is pushed to a valid adjacent node that touches the wall. The push that follows a leap is not limited by arcs (see §15.6, Characters and Arcs; §16.2, Leap)."

Every other answer of §22.1 to §22.7 agrees with the section it cites, and each cited section and sub-heading exists and states the rule (checked by script for the headings, by reading for the content).

## Appendices (chapter 23)

No defect. Appendix A: every Tier value follows from the 25 threshold of §6.2; the Rapier row agrees with the example of §10.5; the example is right (24 − 19 = 5). Appendix B: the step numbers cited for the dodge (steps 1, 5, 6 of §9.5) and for the turn (step 1 of §10.1) are the current ones; §17.7 and §17.10 state what the appendix says they state.

## Glossary, N to Z

### VB-017 · 12_glossary.md · Round · glossary
- Text: "**Round.** One pass of the encounter turn order: every enemy model takes a turn in descending threat order, then every character takes a turn in descending threat order (see §7.5, Encounter Turn Order)."
- Problem: medium. *Round* is used in italics for two other things that the entry does not cover: the round of a boss encounter (§16.1: every living character takes one turn, in an order the players choose, with a boss turn before each) and the round of a PvP encounter (§20.2; §20.8 counts "three consecutive *rounds*").
- Correction: "**Round.** One pass of the encounter turn order: every enemy model takes a turn in descending threat order, then every character takes a turn in descending threat order (see §7.5, Encounter Turn Order). In a boss encounter a round is one turn by each living character, in an order the players choose, with one boss turn before each of those turns (see §16.1). In a *PvP encounter* a round is one turn by each character still in play (see §20.2)."

### VB-018 · 12_glossary.md · PvP encounter · glossary
- Text: "after each boss's defeat and before the rest that follows it."
- Problem: medium. Omits the campaign rule changed today (§18.1, Player versus Player Encounters).
- Correction: "after each boss's defeat and before the rest that follows it (in campaign play, only after a boss whose defeat completes a *section*; see §18.1)."

### VB-019 · 12_glossary.md · Shop · glossary
- Text: "The tier one shop is stocked at setup and the tier two shop when the mini-boss is defeated; both are restocked only after a boss is defeated (in campaign play, after a section is completed), unsold cards going to the bottom of their deck first (see §6.3)."
- Problem: low to medium. The entry gives the campaign rule for restocking and not for opening: in campaign play the tier two shop is stocked when the *bonfire ascetic* is burnt and the defeat of a mini-boss does not open it (§18.6, Blacksmith Andre's Shop; §18.7). The campaign rules are stated in §18.6, which is not cited.
- Correction: "The tier one shop is stocked at setup and the tier two shop when the mini-boss is defeated (in campaign play, when the *bonfire ascetic* is burnt); both are restocked only after a boss is defeated (in campaign play, after a section is completed), unsold cards going to the bottom of their deck first (see §6.3; §18.6)."

### VB-020 · 12_glossary.md · Node · glossary
- Text: "**Node.** A circular space on a tile. Every model occupies exactly one node. Nodes are basic, spawn or terrain."
- Problem: low. No section cited; §5.1 states the rule ("During an encounter every model occupies exactly one node").
- Correction: "**Node.** A circular space on a tile. During an encounter every model occupies exactly one node. Each node is one of three types: basic, spawn, or terrain (see §5.1)."

### VB-021 · 12_glossary.md · Spawn node · glossary
- Text: "**Spawn node.** A node on which enemy models are placed at the start of an encounter. Boss tiles have a boss spawn node."
- Problem: low. No section cited, and a *mega-boss game board* also has a boss spawn node (§5.1; §15.3).
- Correction: "**Spawn node.** A node on which enemy models are placed at the start of an encounter, as the encounter card directs. The mini-boss tile, the main-boss tile, and each mega-boss game board have a boss spawn node (see §5.1; §15.3)."

### VB-022 · 12_glossary.md · Stamina cube · glossary
- Text: "**Stamina cube.** A black cube. Each point of stamina a character spends places one stamina cube on the endurance bar, filling from the left."
- Problem: low. No section cited; §3.4 states the rule.
- Correction: "**Stamina cube.** A black cube. Each point of stamina a character spends places one stamina cube on the endurance bar, filling from the left (see §3.4)."

### VB-023 · 12_glossary.md · Transposed treasure · glossary
- Text: "**Transposed treasure.** A class treasure card marked with a blue light. All transposed treasure is tier two."
- Problem: low. No section cited, and the headword of the parent type is *class-specific treasure* (§6.2: "A class-specific treasure card marked with a blue light in the top-right of the card").
- Correction: "**Transposed treasure.** A *class-specific treasure* card marked with a blue light in the top-right of the card. All transposed treasure is tier two (see §6.2)."

### VB-024 · 12_glossary.md · Tier one treasure · glossary
- Text: "Encounter rewards and chests draw from tier one until the mini-boss is defeated (in campaign play, until the *bonfire ascetic* is burnt) (see §6.2)."
- Problem: low. The campaign clause is stated in §18.5, not in §6.2.
- Correction: "Encounter rewards and chests draw from tier one until the mini-boss is defeated (in campaign play, until the *bonfire ascetic* is burnt) (see §6.2; §18.5)."

### VB-025 · 12_glossary.md · Tier two treasure · glossary
- Text: "Encounter rewards and chests draw from tier two once the mini-boss is defeated (in campaign play, once the *bonfire ascetic* is burnt) (see §6.2)."
- Problem: low. As VB-024.
- Correction: "Encounter rewards and chests draw from tier two once the mini-boss is defeated (in campaign play, once the *bonfire ascetic* is burnt) (see §6.2; §18.5)."

Every other entry from Nearest character to Wound token agrees with the rule as now written and cites a section that states it. Checked in particular against today's changes: Push, Reset, Resting at the bonfire, Section, Signature card, Spark, Stagger, Summon, Titanite, Trap token, Turn, Twin Gargoyles, Victory bonus, Weak arc, Wind Up.

## Cross-chapter checks

- Italic terms: every term set in italics in chapters 12 to 20, 22 and 23 has a glossary headword (script; "*AoE*" in §20.4 resolves to the headword Area-of-effect (AoE)). Every term defined in bold in any chapter has a glossary entry.
- Cross-references: every "§N.M" and every "§N.M, Sub-heading" cited in chapters 12 to 20, 22, 23 and the glossary exists (script). Content checked by reading; the two that fall short are VB-002 and VB-015.
- Step numbers: every reference to a numbered step was checked against the current numbering (§12.1 steps 1 and 3; §12.2 step 1; §13.3 step 3; §15.2 steps 2 and 6; §16.1 steps 1 and 5; §16.2 Leap step 3; §16.5 steps 4 and 7 against §6.6 step 17; §17.9 step 7; §17.10 Four Kings step 1 and Old Iron King steps 4 and 5; §18.8 step 4; §20.1 steps 2 and 3; §7.5 steps 1, 2, 3, 6; Appendix B). None has moved.

---

## Summary

### Examples

33 worked examples checked in half B (chapter 12: 3; 13: 1; 15: 5; 16: 6; 17: 10; 18: 3; 20: 4; Appendix A: 1). All 33 follow from the rules as now written. Re-derived with particular care: §13.3 (four stamina cubes removed, three damage cubes kept, 4 souls for Level 2); §15.5 (2 + 3 + 1 = 6 cards); §16.1 (fifth boss turn renews a four-card deck); §16.2 (push-move against a wall); §16.5 (dial 2 to 3); §17.2 (22 + 15 capped at 30); §17.3 (two pillars, two damage, one stagger token, block total less one); §17.10 Four Kings (4 − 1 + 2 = 5), Manus (card beneath the discard pile is drawn first after renewal), Old Iron King (5 and 1 become 6 and 2), Vordt (6 − 4 = 2, four prevented; 6 − 3 = 3, three prevented); §18.3 (6 + 2 + 4 = 12); §18.4 (maximum 4 to 3); §18.7 (1 + 2 + 2 = 5); §20.4 (failed dodge, armour dice only, 5 − 3 = 2); §20.8 (4 + 1 = 5).

### Boss entries compared with their booklets

| Entry | Booklet | Result |
|---|---|---|
| §17.3 Asylum Demon and Stray Demon | DS-AD-Rules-web-EN.txt | Agrees: game board in place of the mini-boss tile, four pillars, one damage and stagger within one node before the attack, pillars restored at the bonfire, Wind Up, ability name Pillars of Woe, ordinary deck and heat-up for the Stray Demon. Starting facing: see VB-003. |
| §17.10 The Four Kings | DS-Four-Kings-Rules-web.txt | Agrees: 4 models, 4 dials, 4 identifier tokens, 20 cards (8, 4, 4, 4), deck of four, numerical order, royal summons (remove one, add two), no threat value, the turn with no king in play. Push of a king already on the node: see VB-005. |
| §17.10 Gaping Dragon | DS-GaD-Rules-web.txt | Agrees: 14 cards (7, 2, 4, 1), 4 corrosion tokens, deck of three standard, one heat-up and two signature cards, second heat-up card at the heat-up, Crawling Charge ends the turn. |
| §17.10 Guardian Dragon | DS-GD-Rules-web.txt | Agrees: 11 cards (9, 2), 4 Fiery Breath cards, deck of five, both heat-up cards join, cage nodes, Inferno procedure and its facing, Bonus Behaviour, values printed on the Fiery Breath card. |
| §17.10 The Last Giant | DS-TLG-Rules.txt | Agrees: 16 cards (5, 5, 5, 1), deck of three and three, heat-up removes three Arm cards and adds Falling Slam and three heat-up cards (seven cards), Wind Up. |
| §17.10 Manus, Father of the Abyss | DS-MFA-Rules.txt | Agrees: 14 cards (9, 5), deck of five by the general procedure, one heat-up card on top of the deck and one beneath the discard pile without a shuffle, shaft, Overextended. |
| §17.10 Old Iron King | DS-OIK-Rules-web.txt | Agrees: 12 cards (6, 3, 3), 6 node cards, deck of three and three, +1 to attack value and dodge difficulty of Beam attacks after the heat-up, three Iron King nodes, lava as a wall, Beam procedure. The booklet's starting facing ("facing the centre") is not stated: see VB-003. |
| §17.10 Vordt of the Boreal Valley | DS-VotBV-Rules-web.txt | Agrees: 17 cards (6, 2, 6, 2, 1), movement deck of four and attack deck of three, movement card then attack card, first heat-up to the attack deck and second to the movement deck, Frostbreath at the start of the turn after each heat-up, Icy Blows. |
| §17.8 Kalameet, §17.9 Chariot, §17.6 Old Dragonslayer and Pursuer, §17.5 Smelter Demon (component counts and heat-up only) | DS-BDK, DS-EC, DS-Explorers, DS-IronKeep | Agree. Pursuer wording: see VB-008. |

### Campaigns compared with their booklets

| Campaign | Booklet | Result |
|---|---|---|
| §19.1 The First Journey (and Section Four) | core rulebook; DS-BDK | Agrees. |
| §19.2 The Coiled Sword | core rulebook | Agrees. |
| §19.3 Ambush Lies Ahead, §19.4 The Gauntlet | DS-Phantoms | Agree, lists and invader rules. |
| §19.5 Facing the Abyss | DS-Darkroot | Agrees. |
| §19.6 Demon Hunting | DS-AD | Agrees: five sections, bonfire tile in Section One, Northern Undead Asylum. |
| §19.7 Call of the Abyss | DS-Four-Kings | Agrees: five sections, Penultimate Trial (3, 3, 4, Ornstein & Smough), The Abyss (4, 4). |
| §19.8 A Hollow Pursuit | DS-Explorers | Agrees, Voracious Mimic included. |
| §19.9 The Undead Colosseum | DS-EC | Agrees: six sections, six named encounters, shared decks. |
| §19.10 Into the Depths | DS-GaD | Agrees: Outskirts of Blighttown as the Level 4 encounter, the option without Darkroot. |
| §19.11 Playing with Fire | DS-IronKeep | Agrees. |
| §19.12 Big Game Hunting | DS-MFA | Agrees: 16 souls, every boss on a game board, free order, substitution. Wording: see VB-012. |
| §19.13 Go Beyond Death | DS-OIK | Agrees: four sections, Fortress Gates, Blazing Furnace, shared decks. |
| §19.14 Footsteps of Giants | DS-TLG | Agrees: five sections, five listed enemies, two named Level 4 encounters. |
| §19.15 Treasures of the Ice Cave | DS-VotBV | Lists agree. The paired-invader rules leave a dead end: see VB-010. |
| §19.16 Demons and Dragons | DS-GD | Lists, stat table, spark for a Level 4 encounter agree. Order within Section Five: see VB-011. |

### Observations that are not defects

1. §17.10, Crossbreed Priscilla still reads "Apply the special rules supplied with that expansion", while §17.1 promises that the chapter states each boss's further rules. The memo (boss-009; part (b), item 1) records this as unsettled for want of the cards. It stays open.
2. §17.8 keeps a starting facing of its own for Kalameet ("facing the centre of the game board"), while the seven new entries rely on §15.2, step 6. Both give the same direction on the boards as the memo describes them; with VB-003 applied the two forms are consistent.
3. Several deck procedures "return" undrawn cards "to the game box" (§17.8, §17.9, §17.10) while §15.5, Deck Reset gathers "the standard behaviour cards set aside when the deck was built". The first line of that step ("Gather all of the boss's behaviour cards") covers them; no contradiction, but the reader must fetch cards back from the box for a second attempt.
4. §15.5 states "A boss heats up once in each attempt at its encounter"; Vordt (two heat-up points) and the Twin Gargoyles (each Gargoyle at its own point) are stated exceptions.
5. For the other verifier, glossary entries A to M that mirror points above: Boss spawn node (as VB-004); Boss tile ("A mini-boss encounter is fought on the mini-boss tile alone", no Asylum Demon exception); Mimic and Invasion (no campaign keying to the current tier or to the section); and, in the chapters, §7.1 and §6.5, Optional Rules, which state a PvP encounter "after each boss" without the campaign exception (as VB-013).
6. §8.5, Corrosion removes the token "when the affected model next suffers damage"; the booklet removes it when the character suffers damage from the attack against which the penalised block roll was made (DS-GaD-Rules-web.txt, Corrosion Condition). The book's form is broader and simpler; it reads as a deliberate restatement. Chapter 8 is outside this half.
7. §12.2 cites §11.5 for an invader token staying in place through a reset. §11.5 lists what a reset does and removes no token, so the reference holds by implication only.
8. §2.5 and the glossary entry Treasure card list five types and the ember card, while §6.2 speaks of "six types" and counts transposed treasure as one. Outside this half apart from the glossary entry, which follows §2.5.
9. `work/phase3/applied.json` marks campaign-E07, campaign-E12, campaign-E14, core-E08 and phantom-E15 as applied although their exact "new" text is not in the files; in each case a later edit rewrote the same sentence (for example "6x Beam cards" in §2.9). The text in the files is the intended final text.

### Counts

25 defects: inconsistency 6 (VB-001, 004, 005, 006, 007, 013); ambiguity 6 (VB-003, 008, 009, 010, 011, 012); cross-reference 1 (VB-002); faq 3 (VB-014 to 016); glossary 9 (VB-017 to 025); example 0; source 0 (the one booklet difference found, the Old Iron King's starting facing, is carried by VB-003). 23 have a mechanical fix in `verify_b.json`; VB-009 and VB-010 are judgement calls and are described above only.
