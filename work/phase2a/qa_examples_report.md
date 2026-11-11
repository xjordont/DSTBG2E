# QA report: worked examples, tables, and cross-chapter consistency

Scope: `10_manuscript_chapter_00` to `_20`, `_22`, `_23`, and `12_glossary.md`, verified against themselves only. The audit files and the original manuscript were not consulted. Read-only pass: no manuscript file was changed.

Status: COMPLETE. All 23 chapter files and the glossary were read in full.

Result: 80 worked examples re-derived, 78 correct, 2 inconsistent with another part of the book. No impossible die face, no wrong sum, no wrong cost and no wrong order of steps was found in any example. 11 defects in all: 0 errors, 9 inconsistencies, 2 ambiguities.

## Examples checked per chapter

| Chapter | Examples checked | Defective |
|---|---|---|
| 00 Front matter | 0 | 0 |
| 01 Introduction | 0 | 0 |
| 02 Game components | 0 | 0 |
| 03 Characters | 4 | 0 |
| 04 Equipment | 4 | 1 (QA-002) |
| 05 Tiles and nodes | 3 | 0 |
| 06 Setup | 2 | 0 |
| 07 Gameplay | 2 | 0 |
| 08 Combat basics | 10 | 0 |
| 09 Enemy turn | 11 | 0 |
| 10 Character turn | 14 | 1 (QA-001) |
| 11 Returning to the bonfire | 3 | 0 |
| 12 Phantoms | 3 | 0 |
| 13 Mimics | 1 | 0 |
| 14 Crystal lizards | 0 | 0 |
| 15 Boss encounters | 5 | 0 |
| 16 Boss turns | 6 | 0 |
| 17 Boss special rules | 4 | 0 |
| 18 Campaign play | 3 | 0 |
| 19 Campaigns | 0 | 0 |
| 20 Player versus player | 4 | 0 |
| 22 F.A.Q. | 0 | 0 |
| 23 Appendices | 1 | 0 |
| 12 Glossary | 0 | 0 |
| Total | 80 | 2 |

## Tables checked

All of the following agree with their own prose and with every example and section that cites them, except where a defect entry says otherwise.

- §2.5 treasure cards: columns sum to 141 and 393, total 534 as stated. Class-specific 40 and 120 match ten cards for each of 4 and 12 character copies. Boss treasure row: see QA-007.
- §2.6 encounter cards: 36 core and 133 expansion, total 169 as stated; 40 Level 4 cards match four for each of ten mega-boss expansions.
- §2.7 dice faces: every die result quoted in an example is a face of the die named.
- §2.8 condition tokens: 4 x 7 + 4 + 4 = 36 as stated. Eight hollow cubes and 16 stat cubes match four characters.
- §2.9 against §17.8 and §17.9: Kalameet 10 + 2 + 1 = 13 behaviour cards, 8 strafe cards, 4 calamity tokens; Chariot 4 track cards, 9 + 3 behaviour cards, 6 encounter cards of Levels 1 to 3 (the six named encounters of §19.9).
- §7.6 soul rewards (3/4/5/6 and 1/2/2/3): used correctly in §7.6, §11.2, §13.3 and §16.5 examples; §18.5 and §22.4 agree.
- §8.3 scaling: used correctly in §6.4, §8.2, §8.3, §8.4, §8.5 and §18.7 examples.
- §11.3 stat tier costs (2/4/8/10) and §18.6 (4/8/16/20): §3.3, §11.2 and §11.3 examples and the glossary agree.
- §11.4 prices (2/4, sell 1, boss treasure 6) and §18.6 price table (boss treasure 4, legendary 4, ascetic 16): prose agrees. Glossary Shop entry: see QA-008.
- §18.3 spark table: six minus characters, maximum one more; §6.4, §11.2, §16.5 and both §18 examples agree.
- §20.4 PvP dodge difficulty: both §20.4 examples use the table correctly.
- Appendix A: all 60 rows have the Tier value that the 25 threshold gives, and 0 INT and 0 FTH as the closing sentence states. Morning Star and Halberd match the §4.1 example; Brigand Axe matches the appendix example. Rapier: see QA-001.
- §19: 12 campaigns, three to six sections each, as §18.1 states; every boss listed belongs to a set its campaign requires; §19.4 uses each of the 12 invaders once.

## Defects

### QA-001 · 10_manuscript_chapter_10_character_turn.md · line 166 · inconsistency
- Text: "The Assassin's rapier prints requirements of 10 STR and 20 DEX, so dexterity is its relevant stat. The Assassin's dexterity is 24, which exceeds 20 by four, and the rapier is not scaled."
- Problem: Appendix A lists the Rapier at 14 STR and 21 DEX and states that its values replace the printed ones and that a listed weapon is scaled against them. The example computes the margin from the superseded value (the outcome is the same, the numbers are not). §11.2 line 45 uses the named card Rapier.
- Rule: Appendix A (line 3 and Rapier row, line 50); §10.5.
- Suggested correction: "The Assassin's Rapier requires 14 STR and 21 DEX (see Appendix A), so dexterity is its relevant stat. The Assassin's dexterity is 24, which exceeds 21 by three, and the Rapier is not scaled. At the *bonfire* the Assassin raises dexterity to 29. The Rapier is now scaled, and the Assassin marks it with a red cube."

### QA-002 · 10_manuscript_chapter_04_equipment.md · lines 57 and 61 · inconsistency
- Text: "Once attached, a Titanite card cannot be removed." and, in the example, "the Titanite Shard stays attached for the rest of the game."
- Problem: Appendix B, Titanite Replacement (lines 147 to 149) lets a Titanite Chunk replace an attached Shard and a Slab replace a Chunk, states "A replaced *Titanite* card does not remain fused to the weapon", and returns the replaced card to a treasure deck. The glossary entry Titanite agrees with the appendix. §4.2 states no exception, and §11.4 line 108 refers to §4.2 for "the permanence of Titanite".
- Rule: Appendix B, Titanite Replacement; §4.2, Titanite.
- Suggested correction: line 57: "Once attached, a Titanite card cannot be removed, except when a Titanite Chunk or a Titanite Slab takes its place (see Appendix B, Titanite Replacement)." Line 61: "The Morning Star holds no further upgrade card, and the Titanite Shard stays attached unless a Titanite Chunk later takes its place (see Appendix B)."

### QA-003 · 10_manuscript_chapter_07_gameplay.md · line 179 · inconsistency
- Text: "Only the character who dropped the souls may reclaim them, and only by surviving an encounter on that tile that ends cleared"
- Problem: §6.6 step 1 (line 160) and §6.7 step 1 (line 186) return every pile of dropped souls still on the tiles to the character who dropped it when a boss is defeated, including souls dropped on the boss tile by a character who died in the boss encounter. That is a second way to reclaim them, which "only" excludes. The glossary entry Dropped souls (line 101) repeats the absolute wording.
- Rule: §6.6 step 1; §6.7 step 1; §7.6.
- Suggested correction: add after the sentence: "The one exception is the setup that follows the defeat of a boss, which returns all dropped souls still on the tiles to the characters who dropped them (see §6.6, §6.7)." Glossary: "...by surviving to clear that encounter, or when a boss is defeated (see §6.6)."

### QA-004 · 10_manuscript_chapter_22_faq.md · line 191 · inconsistency
- Text: "**A.** Yes. While the invader is on the tile, the encounter is not cleared (see §12.2, End of an Invasion)."
- Problem: the section cited says the encounter is also cleared "when the invader has vanished and every other enemy model has been killed", and the answer two questions earlier (line 187) says the invader vanishes when a character dies and the encounter continues. An invader need not be killed.
- Rule: §12.2, End of an Invasion (line 159); §12.2, Combat with an Invader (line 149).
- Suggested correction: "**A.** Not always. While the invader is on the tile, the encounter is not cleared. It is cleared when every enemy model, the invader included, has been killed, or when the invader has vanished and every other enemy model has been killed (see §12.2, End of an Invasion)."

### QA-005 · 10_manuscript_chapter_07_gameplay.md · line 96 · inconsistency
- Text: "In boss encounters the aggro token moves after any damage to the boss (see §16.4)."
- Problem: §16.4 moves the token at the end of a character's turn, and only if that character inflicted damage; a riposte moves it at the end of the boss turn; damage by a summon never moves it. "After any damage" gives a different moment and a wider cause. F.A.Q. line 169 and the glossary follow §16.4.
- Rule: §16.4 (lines 137 to 143).
- Suggested correction: "In boss encounters the aggro token moves at the end of the turn of each character who inflicted damage on the boss during that turn (see §16.4)."

### QA-006 · 10_manuscript_chapter_02_game_components.md · line 255 · inconsistency
- Text: "When invaders are in play, one invader token is placed face down on each face-down encounter card and is revealed when the characters enter that tile (see §12.2)."
- Problem: §12.2 places tokens only when an invasion is provoked by an embered character ("If no character is embered when the encounter cards are dealt, no invader token is placed"), and reveals a token only when the encounter is fought; it stays face down when the party skips the encounter. The glossary entry Invader token follows §12.2.
- Rule: §12.2, Invasions and Invader Tokens (lines 86 to 106).
- Suggested correction: "When an invasion is provoked, one invader token is placed face down on each face-down encounter card, and each is revealed when the characters fight that encounter (see §12.2)."

### QA-007 · 10_manuscript_chapter_02_game_components.md · line 154 · inconsistency
- Text: "| *Boss treasure* | 18 | 63 |" with "Each boss has between two and four boss treasure cards" (lines 62 and 156)
- Problem: the stated limits cannot give 63. The expansions supply 21 bosses: ten mega-bosses with two cards each (§2.9 line 276), the Old Dragonslayer with two (§17.6 line 143), and ten others with at most four. The maximum is 20 + 2 + 40 = 62. Either the count, the range, or one of the per-boss figures is wrong, or the 63 includes cards of another kind (the 12 invader treasure cards, or cards added by Appendix B). The total of 534 depends on it.
- Rule: §2.3; §2.5; §2.9; §17.6.
- Suggested correction: cannot be settled from the book alone; recount against the components. If 63 is right and one boss has five cards: "Each boss has between two and five boss treasure cards" in both places. If the range is right, correct 63 and the total of 534.

### QA-008 · 12_glossary.md · line 267 · inconsistency
- Text: "a treasure card other than starting equipment sells for one soul (see §11.4)"
- Problem: §11.4 pays six souls for a boss treasure card, which is a treasure card (§2.5), and the glossary entry Boss treasure says six. In campaign play a legendary treasure card sells for four (§18.6).
- Rule: §11.4, Sales and Prices; §18.6, Shop Price Table.
- Suggested correction: "a tier one or tier two treasure card sells for one soul and a boss treasure card for six; starting equipment cannot be sold (see §11.4)"

### QA-009 · 12_glossary.md · line 305 · inconsistency
- Text: "The treasure deck that holds every treasure card with a stat requirement of 25 or more, the transposed treasure and the five legendary cards."
- Problem: §6.2 puts only common and class-specific treasure into the deck by stat requirement; boss treasure enters neither deck whatever its requirements (Appendix A, Treasure Type, says the same). The companion entry Tier one treasure is worded correctly.
- Rule: §6.2, Tier Two Treasure Deck (line 43).
- Suggested correction: "The treasure deck that holds common and class-specific treasure with a stat requirement of 25 or more, all transposed treasure, and the five legendary cards."

### QA-010 · 10_manuscript_chapter_12_phantoms.md · line 100 · ambiguity
- Text: "Add blank invader tokens, face down, until there is one token for each face-down encounter card on the encounter tiles."
- Problem: §2.9 (line 253) supplies three blank invader tokens, which is enough for the four encounters of a standard route. §18.1 (line 40) allows one invasion in each section, and several sections in §19 list five encounters (for example §19.1 Section Three and every section of §19.2), which need four blank tokens. The step cannot be completed and no rule says what to do.
- Rule: §12.2, Invader Tokens; §2.9; §18.1, Section Setup.
- Suggested correction: add after step 2: "If the blank tokens run out, use invader tokens of the other kind as blanks; when one is revealed, it is treated as blank."

### QA-011 · 10_manuscript_chapter_04_equipment.md · lines 101 and 103 · ambiguity
- Text: "An ember card in the inventory cannot be consumed until the encounter ends." and "A character consumes an ember card by discarding it, as the *Ember* major action during an encounter or at any time outside an encounter."
- Problem: §4.4 implies that outside an encounter an ember card may be consumed from the inventory. §3.2 (line 33) says "An *ember card* must be in the back-up slot to be used", and §7.3 (line 38) and the glossary say it is discarded "from their back-up slot" in both cases. The practical effect is small, because cards move freely outside an encounter, but the two sections answer the question differently.
- Rule: §3.2, Back-up slot; §7.3; §4.4.
- Suggested correction: line 101: "During an *encounter*, the inventory cannot be accessed, so an ember card there cannot be consumed until the encounter ends." Line 103: "A character consumes an ember card by discarding it from the back-up slot, as the *Ember* major action during an encounter or at any time outside an encounter."

## Observations that are not counted as defects

These are not contradictions between two statements, and no action is required. They are listed in case the editor wishes to tighten the wording.

- §7.6 table (line 171): the reduced reward of 3 for a Level 4 encounter can never be paid, because a cleared Level 4 encounter is not fought again (§6.7 line 207; §18.1 line 58).
- §17.1, §17.2, §18.1 and the glossary define the Twin Gargoyles by a section "that lists the Gargoyle twice in succession". The lists in §19.1, §19.3 and §19.6 name it once: "Gargoyle (*mini-boss*), fought twice (see §17.1)". The cross-reference makes the meaning clear.
- §8.2 line 44 says the repeat icon "shows the number of times the behaviour is resolved"; §9.3 line 89 limits it to the attack icon beside it and excludes movement icons.
- F.A.Q. line 93 says trap damage is not an attack and cites §5.5, Traps. §5.5 does not say so; it says a trap is dodged "as an attack". The ruling is not contradicted anywhere.
- F.A.Q. line 47 says "With no dice, the defence total is zero" and then "Fixed modifiers are applied in either case". §9.4 steps 4 and 5 call the zero "the sum" and the result after modifiers "the defence total".
- §18.1 line 52 (a boss defeated before its section is completed) revives a dead character "as after any cleared encounter", that is hollow, while §16.5 step 4 gives the same character an ember token and the glossary says an embered character is not hollow. No campaign in §19 lists two bosses in one section, so the case does not arise.
- §6.1 step 7 cites §7.6 for the six souls of a lone character; §7.6 does not mention them. The glossary entry Souls cites §6.1.
- §7.4 line 57 and §20.1 line 11 speak of a spark and a rest after every boss; §16.5 and §20.9 correctly exclude the final boss.
