# Rulings memo — cluster `phantom`

Scope: lead items 2, 6, 7, 14, 22 of `14_open_issues.md`; every item in the issue lists of chapters 00, 01, 12, 13, 14, 20, 21, 22; the designer's points set for the cluster. Edits are in `work/phase3/edits_phantom.json` (41 entries, `phantom-E01` to `phantom-E41`; each `old` verified to occur exactly once; the patched copies pass `tools/style_check.py` with zero violations).

Ruling labels: CONFIRM means the rule stands as drafted (a wording edit may still be attached and is then marked "Mechanical: no"); CHANGE, ADD and DELETE mean the rule itself moves.

## Sources and their reach

- Official booklets read in full for this cluster: Phantoms (`work/text/DS-Phantoms-Rules-lores.txt`), Explorers (`DS-Explorers-Rules-Web.txt`, lines 290–620), Iron Keep (`DS-IronKeep-Rules-Web.txt`, lines 40–148), official F.A.Q. of 11 April 2017 (`Dark_Souls_The_Board_Game_FAQ.txt`, all 86 lines).
- Official rulebooks 2017 and 2022: searched for invader, summon, phantom, mimic, ambush, crystal lizard, PvP, versus. Both are silent on every one of them (those rules live only in the booklets), and neither has any player-versus-player mode. They were used for pushes (2017 line 968; 2022 line 1497), chests (2017 lines 780–798), traps (2017 lines 811–825) and adding players (2017 lines 1609–1620).
- Extended Rules V45: summons only (lines 43–51); nothing on invaders, mimics, crystal lizards or PvP beyond scenario text.
- Hollowed Edition v1.3: lines 49–58 (summary), 339–392 (invaders, summons, mimics, crystal lizards), 406–410 (turn order).
- Online: web search was available. Reddit is closed to the search tool, the two Reddit mirrors of the house-rules megathreads returned 404 and 503, and no BoardGameGeek thread on these points surfaced in nine searches (results were retailer pages). Reached and used: the community "DSBG – Unofficial Guide & Rules FAQ" (https://docs.google.com/document/d/1DmbTaM68OoosZcSCFW0bTNgBWCaHSP2UE9Um-X4XF54/mobilebasic), the publisher's F.A.Q. blog page (nothing on these topics), and a house-rules round-up (https://gamerant.com/dark-souls-board-game-house-rules/ : four popular house rules, all on the soul economy, none on phantoms, mimics, crystal lizards or PvP). One search summary reported a fan PvP variant on BoardGameGeek "with treasure drafting and bluffing"; the thread could not be opened and is not relied on. Where an entry says "online: nothing found", this is what it means.
- The author's source manuscript (`work/phase2a/source/12_*`, `13_*`, `14_*`, `20_*`) and the audit rows B-024, B-035, A-034, A-035 were read for each point.

---

## Lead items

### phantom-001 · Lead 2 · invader and clearing an encounter
- Question: Must an invader be killed before its encounter counts as cleared, or does it leave when the other enemies are dead?
- This book now: An invader is an enemy model and counts towards clearing; the encounter is cleared when every enemy, the invader included, is killed, or when the invader has vanished and the rest are killed (§12.2, End of an Invasion). It vanishes without reward the moment any character dies (§12.2, Combat with an Invader).
- Evidence: official Phantoms booklet: the invader "will fight alongside the other enemies present in the encounter" (lines 492–495); reward "even if other enemies still remain" and removal only "if the party is defeated before killing the invader" (lines 527–533); campaign text "you have no choice but to defeat them in battle before you may resume the path" (lines 553–557). Official 2017 / 2022: silent. Extended: silent. Hollowed: invaders "fight you alongside normal enemies"; "if any players are defeated during an invasion, the invader leaves" (lines 351–367). Source manuscript: "If any character dies, the invader immediately vanishes without award." Online: the community guide says only that invaders "act as an additional challenge in encounters".
- Ruling: CONFIRM as written.
- Why: The general rule of §7.5 (every enemy model killed) already gives this answer with no special case, and every source that speaks treats the invader as one of the enemies. The alternative turns the invader into a second crystal lizard: the party kills the weak enemies and the hunter walks away, which removes the fight the rule exists to cause. The author's vanish-on-a-death rule is the only exit the design needs. The paragraph is shortened; the rule does not move.
- Mechanical: no
- Edits: phantom-E11 (wording), phantom-E40 (F.A.Q. answer reworded to match)

### phantom-002 · Lead 6 · PvP stalemate rule
- Question: Is the rule that burns every character after three quiet rounds needed, and is three the right number?
- This book now: After three consecutive rounds with no damage and no death, each character still in play suffers one undefendable damage at the end of every further round (§20.8).
- Evidence: official 2017 / 2022 / F.A.Q. / booklets: no PvP mode exists. Extended, Hollowed: silent. Source manuscript: no such rule; its only clock is the trap token placed after each turn. Audit A-035 (optional): "Two ranged characters can retreat indefinitely; traps shrink the arena only slowly and a player may choose placements that never threaten themself." Online: nothing found.
- Ruling: CONFIRM as written.
- Why: The hole is real. A block costs nothing and an attack costs stamina that fills the same bar as damage, so the defender is favoured and two careful players can stop hurting each other; the trap supply is only what is left after trapped encounters have taken their share of the 20 tokens, and may be nil. The rule is two sentences, bites only when nothing is happening, needs no marker once triggered, and rewards the character who is ahead, which is the right incentive. A clock tied to the trap supply was considered and rejected: it either starts on the first turn when the supply is empty or waits ten rounds when it is full.
- Mechanical: no
- Edits: none

### phantom-003 · Lead 7 · PvP dodge table
- Question: Are the values 3 / 2 / 2 / 1 / 1 / 1 right, against the manuscript's 4 / 3 / 2 / 1 / 1 / 0?
- This book now: Dodge difficulty by the stamina cost of the attack option: 0 → 3, 1 → 2, 2 → 2, 3 → 1, 4 → 1, 5 or more → 1 (§20.4).
- Evidence: no official or community source has PvP. Source manuscript: 4 / 3 / 2 / 1 / 1 / 0. Audit B_report.md §10.1: with the green die at three successes in six, difficulty 4 succeeds 6 % of the time on the maximum of four dice and never on fewer; difficulty 3 is impossible on two dice; difficulty 0 succeeds with no dice at all. Proposed 3 / 2 / 2 / 1 / 1 / 1 "keeps the inversion but stays inside the dice range" (B-024, approved at Gate 1).
- Ruling: CONFIRM as written (values); the table is condensed to three rows.
- Why: The author's idea is sound and worth its place: a cheap attack is quick and hard to dodge, a heavy one is slow and easy to dodge, so attacker and defender each have a real choice between force and certainty. The manuscript's end values break it: a free attack that cannot be dodged and a heavy attack that is dodged automatically for one stamina. The drafted values keep every result on the dice. Six rows carry only three values, so the table is cut to "0", "1 or 2", "3 or more"; no result changes.
- Mechanical: no
- Edits: phantom-E29

### phantom-004 · Lead 14 · the mimic's reward
- Question: Does a killed mimic pay souls of its own, or only treasure?
- This book now: No soul reward of its own. Killing it awards two treasure cards (the chest's card and one drawn from the treasure deck of the current tier) and releases the deferred reward of the encounter (§13.3).
- Evidence: official Explorers booklet: "do not add any souls to the soul cache. Instead, the party gains treasure cards as if they had opened two chests" (lines 549–554); data card ability Loot the Body, same words (lines 417–420). Official 2017 / 2022: silent. Extended: silent. Hollowed: "Mimic rewards count as opening two chests" (lines 386–388). Source manuscript: "they gain two tier appropriate treasures (instead of one)"; its soul table has no mimic row. Online: nothing found.
- Ruling: CONFIRM as written.
- Why: Four sources agree and none gives a soul value; inventing one adds a row to the soul table for no gain. Double treasure is the right prize for a chest that bites: it is what the party came to the chest for, and it needs no arithmetic. The risk side of the bargain is dealt with at phantom-026.
- Mechanical: no
- Edits: none

### phantom-005 · Lead 22 · shortage of blank invader tokens
- Question: What happens when an invasion needs more than the three blank tokens supplied?
- This book now: Invader tokens of the kind not drawn stand in as blanks and are treated as blank when revealed (§12.2, Invader Tokens, step 2).
- Evidence: official Phantoms booklet: 3 blank, 6 standard, 6 advanced tokens (lines 103–105); "take one random … invader token and enough blank tokens to have one token for each unexplored encounter tile" (lines 363–377); one picture of the token back serves all three kinds (line 332), so the kinds cannot be told apart face down. The official game has four encounters to a leg, so three blanks always suffice there. Extended: silent. Hollowed: "All but one token must be empty" (lines 342–345), no count given. Online: nothing found.
- Ruling: CONFIRM as written.
- Why: Substitution is what a table would do unprompted, costs one sentence, needs no notion of which tiles go without, and keeps the invader hidden among every eligible card. The alternative (tokens only on the four nearest cards) tells the party that the far encounter is safe. With the ruling at phantom-009 a cleared encounter takes no token, so the shortage can arise only in a campaign section of five or more encounters (§19.1, §19.2, §19.5, §19.6, §19.11) when an invasion is provoked at its setup.
- Mechanical: no
- Edits: none (the sentence is carried unchanged inside phantom-E06)

---

## Chapter 00 — front matter

### phantom-006 · Chapter 00 · no open items
- Question: None; the issue list reads "None."
- This book now: Foreword and colophon only.
- Evidence: `work/phase2a/issues/00_front_matter.md`.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: The chapter holds no rule.
- Mechanical: no
- Edits: none

## Chapter 01 — introduction

### phantom-007 · Chapter 01 · no open items
- Question: None; the issue list reads "None."
- This book now: Introduction without rules sections.
- Evidence: `work/phase2a/issues/01_introduction.md`.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Nothing was raised.
- Mechanical: no
- Edits: none

---

## Chapter 12 — phantoms

### phantom-008 · Chapter 12 · invader and clearing (duplicate)
- Question: Same as phantom-001, as first raised by the chapter's drafter.
- This book now: See phantom-001. The drafter's note describes an earlier draft (invader does not count); the lead editor reversed it at integration (CH-12-033).
- Evidence: see phantom-001.
- Ruling: CONFIRM as written.
- Why: See phantom-001. §7.5 and the glossary entry Cleared need no mention of invaders, because an invader is an enemy model.
- Mechanical: no
- Edits: phantom-E11

### phantom-009 · Chapter 12 · invasion trigger and eligible cards
- Question: Are the two trigger moments right, and which encounter cards receive a token?
- This book now: An invasion is provoked when encounter cards are dealt while a character is embered, or when a character discards an ember card while a face-down encounter card lies on a tile; tokens go on every face-down encounter card (§12.2, Invasions; Invader Tokens).
- Evidence: official Phantoms booklet: "When a character gains an Ember token, if there are no invader tokens already in play and there is at least one unexplored tile" (lines 363–367); tokens on "each unexplored encounter tile". Hollowed: "Whenever any player becomes embered, place invader tokens on all undefeated encounters" (lines 341–343). Source manuscript: "Embered characters provoke an invader if no invasion has occurred yet." This book, §11.5 step 1: a rest turns every encounter card face down, cleared ones included; §7.5: only an encounter whose card carries a black cube may be skipped.
- Ruling: CHANGE (the two moments are confirmed; tokens go only to face-down encounter cards that carry no black cube).
- Why: The two moments are the only two at which "an embered character and an unfought encounter" can first come together, and players cannot miss either, so they stay. "Face down" is not this book's equivalent of the official "unexplored": after a rest every card is face down. As drafted, a character who embers at the bonfire after a rest spreads the tokens over cleared encounters as well, the party skips those, and half the time the invader is never met; embering at the bonfire becomes the correct and dull play. Adding "that carries no black cube" restores the official and Hollowed meaning, makes the invader certain to be met, and makes the skip clause unnecessary.
- Mechanical: yes
- Edits: phantom-E04, phantom-E06, phantom-E07, phantom-E09, phantom-E16 (§2.9), phantom-E33 and phantom-E34 (glossary)

### phantom-010 · Chapter 12 · first setup, step 5 of §6.5
- Question: Does "place the invader tokens" in the setup lists read as unconditional?
- This book now: §6.5 Encounter Cards step 5 and §6.6 step 15: "If invaders are in play, place the invader tokens on the encounter cards (see §12.2)."
- Evidence: §12.2: tokens are placed at setup only if a character is embered. No character is embered at the first setup; every character is embered at the setup after a boss (§16.5 step 4). Official Phantoms booklet: no tokens until a character gains an Ember token (lines 363–366).
- Ruling: CONFIRM as written (rule); both steps gain the condition in words.
- Why: The rule is right and the pointer is in the right place; five words stop a first-time reader from laying tokens on the opening route.
- Mechanical: no
- Edits: phantom-E14, phantom-E15

### phantom-011 · Chapter 12 · souls spent away from the bonfire
- Question: Does §7.6 allow the summoning payment at the fog gate?
- This book now: §7.6 already states it: "The one exception is the cost of calling a summon at the fog gate" and §11.3 repeats it.
- Evidence: this book §7.6, §11.3, §12.1; glossary Souls.
- Ruling: CONFIRM as written.
- Why: The dependency was satisfied at integration. Nothing remains.
- Mechanical: no
- Edits: none

### phantom-012 · Chapter 12 · blank invader tokens (duplicate)
- Question: Same as phantom-005.
- This book now: See phantom-005.
- Evidence: see phantom-005.
- Ruling: CONFIRM as written.
- Why: See phantom-005.
- Mechanical: no
- Edits: none

### phantom-013 · Chapter 12 · summon defence, pushes and conditions
- Question: Does a summon whose dodge fails suffer full damage, and is a hit summon pushed and given conditions as a character is?
- This book now: Yes to both (§12.1, Summons in Combat).
- Evidence: official Phantoms booklet: "summons, like characters, roll dice to block, resist, or dodge that damage" and have taunt levels "enabling players to know which character or summon the boss will attack" (lines 141–158). Official F.A.Q.: a character's failed dodge takes "the attack's full damage as well as any pushes or conditions" (lines 31–34). This book §9.5: a character with no armour card suffers the full attack value after a failed dodge. Extended, Hollowed: silent on the point.
- Ruling: CONFIRM as written.
- Why: A summon has no armour card, so this book's own rule for a failed dodge already yields full damage; no exception is being made. Treating the summon as a character for pushes and conditions is the reading a player would guess from "the boss's behaviours treat a summon as a character", and it lets a summon be knocked about by the boss as its allies are.
- Mechanical: no
- Edits: none

### phantom-014 · Chapter 12 · summon attacks
- Question: Are a summon's attacks resolved as character attacks (dice on the card against the boss's block or resist)?
- This book now: Yes, with the weak-arc die and no stamina cost (§12.1, Summon Turns).
- Evidence: official Phantoms booklet: summon behaviour cards are used as boss behaviour cards are, without heat-up, arcs or dodge difficulty "since bosses never dodge attacks" (lines 179–196); "Summons, like characters, gain an additional black die on attacks in the weak arc" (lines 264–266); shift icons "before the dice icons" and "after the dice" (lines 293–299). The behaviour cards themselves were not supplied.
- Ruling: CONFIRM as written.
- Why: Dice icons, a weak-arc die and the absence of a dodge difficulty are all marks of a character-style attack roll, so the drafted reading is the only one that fits the booklet. The author should still glance at one card; nothing in the rule depends on what it shows.
- Mechanical: no
- Edits: none

### phantom-015 · Chapter 12 · choice of summon, no tie-break
- Question: Who decides which drawn summon joins if the players disagree?
- This book now: The players choose together; no tie-break (§12.1, Summoning).
- Evidence: official Phantoms booklet: the summon is taken at random from the five cards (lines 238–240). Hollowed: "Summons are chosen at random" (line 389). Gate 1 OQ-29 sends contested treasure to the aggro holder, but the aggro token is not assigned at the fog gate.
- Ruling: ADD (if the players cannot agree, the drawn cards are shuffled and one is drawn).
- Why: Each payer has bought a card and has a stake in it, so this is the one joint choice in the chapter that can stick. A random draw among the cards already on the table needs no token and no new term, and it is what both other rulesets do in every case.
- Mechanical: yes
- Edits: phantom-E01

### phantom-016 · Chapter 12 · invader treasure tie-break wording
- Question: The invader's card is awarded during the encounter; §7.7 breaks ties by the aggro holder "when the encounter ends". Which moment governs?
- This book now: §12.2 says the holder "at that moment"; §7.7 says "when the encounter ends" and its list of party awards omits the invader's card.
- Evidence: Gate 1 OQ-29 (aggro holder everywhere). Official Phantoms booklet: the card is gained "immediately" (lines 528–533).
- Ruling: CONFIRM as written (rule); the tie-break is stated once, in §7.7, as "when the card is awarded".
- Why: One sentence in the owning section covers a card won at the end of an encounter and a card won in the middle of one. §12.2 then cites it instead of restating it with a different phrase.
- Mechanical: no
- Edits: phantom-E10, phantom-E12

### phantom-017 · Chapter 12 · invader as an enemy model
- Question: May characters push an invader and place conditions on it, or does it resist pushes as a boss does?
- This book now: The rules for enemy models apply to an invader except where §12.2 says otherwise, so it is pushed and takes conditions (§12.2).
- Evidence: official 2017: "Boss models cannot be pushed by a character's movement or attack" (line 968), likewise 2022 (line 1497); the Phantoms booklet never calls an invader a boss and has it "fight alongside the other enemies". Extended, Hollowed: silent. Online: nothing found.
- Ruling: CONFIRM as written.
- Why: The push immunity belongs to boss models, which fill a node; an invader is a character-sized model that shares nodes. Leaving it under the enemy rules needs no sentence at all and gives the party a tactic against a model that acts after every character's turn.
- Mechanical: no
- Edits: none

### phantom-018 · Chapter 12 · cross-chapter dependencies
- Question: Have the other chapters taken up what §12 needs from them?
- This book now: §15.2 places characters, then the summon (steps 2 and 4); §16.1 admits the summon's turn; §16.4 keeps a summon's damage from moving the aggro token; §15.6 gives a summon the weak-arc die; §8.3 and §18.7 exempt phantoms and crystal lizards; §19.3 and §19.4 place no invader tokens; §12.2 itself keeps tokens in place at a reset.
- Evidence: the sections named, read for this memo.
- Ruling: CONFIRM as written.
- Why: Every dependency is met. The one loose end is that §16.4 says a summon "does not hold the aggro token" without a nod to the Distract icon, which makes the boss treat it as the holder for one turn; one sentence points to §12.1.
- Mechanical: no
- Edits: phantom-E17

### phantom-019 · Chapter 12 · glossary entries owned elsewhere
- Question: Do Cleared, Weak arc, Behaviour deck, Behaviour card, Shift and Turn agree with §12?
- This book now: Behaviour deck, Behaviour card and Shift were corrected at reconciliation. Cleared needs no change (phantom-008). Weak arc still names characters only; Turn omits the turns of invaders and summons.
- Evidence: `12_glossary.md` lines 37, 39, 75, 265, 319, 339; official Phantoms booklet lines 264–266 (weak-arc die for summons).
- Ruling: CONFIRM as written (rules); two glossary entries are corrected to say what the chapters say.
- Why: The chapters are right and the two entries lag behind them.
- Mechanical: no
- Edits: phantom-E35 (Weak arc), phantom-E36 (Turn)

### phantom-020 · Chapter 12 · notes "resolved at integration"
- Question: Do the lead editor's two integration decisions (the invader counts towards clearing; substitute blanks) stand?
- This book now: Both are in §12.2.
- Evidence: see phantom-001 and phantom-005.
- Ruling: CONFIRM as written.
- Why: Both are the right calls, for the reasons given there.
- Mechanical: no
- Edits: none

### phantom-021 · Chapter 12 · the invasion procedure at its shortest (designer's point)
- Question: Is there a shorter procedure that keeps the party unsure where the invader waits?
- This book now: Trigger (two moments, one per leg), four placement steps, a paragraph on tokens through resets and skips, reveal at Encounter Start (§12.2, Invasions; Invader Tokens).
- Evidence: official Phantoms booklet lines 362–382 (one invader token and blanks dealt to the unexplored encounter cards) and 478–490 (set up the encounter, then flip the token). Hollowed lines 341–349 (same). Source manuscript: same, with the token revealed before the encounter card.
- Ruling: CONFIRM as written (procedure), with two trims.
- Why: Two simpler schemes were weighed. A die rolled at each encounter drops the tokens but can fail to produce the invader and adds a roll to every encounter. A face-down stack of four tokens beside the board, one flipped at each fight, removes the count of cards and the shortage of blanks, but it loses the picture on the table (one of those tiles holds the hunter), it burns a token on every repeated attempt, and with fewer than four fights left it can leave the invader in the stack. Tokens on the cards are what the components were made for, and with phantom-009 they need no rule for skipped encounters. The text loses about 60 words: two paragraphs on the limit merge into one, and the skip clause goes.
- Mechanical: no
- Edits: phantom-E05, phantom-E08 (with the edits of phantom-009)

### phantom-022 · Chapter 12 · summons: cost, timing, limits (designer's point)
- Question: Is the cost right, when does a summon act, and what may it not do?
- This book now: Each embered character may pay two souls at the fog gate to draw one summon card; the players pick one of the drawn cards; the summon acts after each character's turn, attacks and defends with its card's dice, is pushed and takes conditions as a character, never holds the aggro token, and leaves when its health reaches zero or the encounter ends (§12.1).
- Evidence: official Phantoms booklet: cost is the whole soul reward of the fog-gate encounter (lines 200–218); "a summon activation after each character activation" (lines 232–254); Distract (lines 293–298); death of a summon costs nothing (lines 303–305). Extended: "the cost of a summon is two souls per player … only one summon active per spark" (lines 43–51). Hollowed: once per floor per tombstone, halves the soul reward (lines 54–56, 377–397). Community guide: the official cost "makes it a variable cost since encounters reward varying amounts of souls". Gate 1 OQ-32 (acts after each character's turn).
- Ruling: ADD (one sentence on what a summon cannot do); cost and timing CONFIRMED.
- Why: Two souls from each embered character who wants a say is the best cost on offer: it is fixed where the official cost varies with the last encounter, it makes the ember the real price (and the invasion that an early ember invites), and extra payers buy choice, not extra bodies. The timing is official and was settled at Gate 1. The chapter listed what a summon does but not what it cannot: a model with dodge dice invites the question whether it may parry, and a model the players steer invites the question whether it may walk or attack off its card. One sentence closes both.
- Mechanical: no
- Edits: phantom-E02

### phantom-023 · Chapter 12 · what an invader awards, and when it vanishes (designer's point)
- Question: What does a killed invader pay, and is "vanishes when any character dies" sound?
- This book now: Every character gains three souls (standard) or four (advanced) at once, and the party gains the invader's treasure card at once; an invader vanishes without reward when any character dies and never returns (§12.2; §7.6).
- Evidence: official Phantoms booklet: treasure card and three souls to the shared cache "immediately … even if other enemies still remain"; if the party is defeated the invader is removed and "will not return" (lines 527–533). Hollowed: one shared soul per player (standard), two (advanced), items at once; "If any players are defeated during an invasion, the invader leaves" (lines 356–367). Source manuscript: soul table rows for standard and advanced invaders; "If any character dies, the invader immediately vanishes without award."
- Ruling: CONFIRM as written.
- Why: The reward equals a Level 1 or Level 2 encounter, which is fair pay for a model that acts as often as a boss, and paying it at once means nothing has to be remembered. Vanishing on the first death is the author's rule and Hollowed's; it caps the damage an invasion can do to a run and keeps the invader a one-time visitor with no state to carry.
- Mechanical: no
- Edits: none

### phantom-024 · Chapter 12 · standard and advanced invaders in campaign play (designer's point)
- Question: A campaign has several mini-bosses or none. When do advanced invaders replace standard ones?
- This book now: "A standard invader token if the mini-boss has not been defeated, an advanced invader token if it has" (§12.2); §18.1 says only that each section has at most one invasion.
- Evidence: official Phantoms booklet ties the split to "the mini boss" of the one-mini-boss game (lines 363–377); its own campaign puts standard invaders in the section after the first mini-boss (lines 590–598). This book §18.5 and §18.7: in campaign play tier two opens only when the bonfire ascetic is burnt, "whatever bosses have been defeated".
- Ruling: ADD (in campaign play: standard while the current tier is tier one, advanced once it is tier two).
- Why: "The mini-boss" names no moment in a campaign, so a rule is needed. The current tier is the one switch every campaign has, the party throws it knowingly, and it already raises enemy health; letting it also bring the advanced invaders keeps the threat in step with the equipment the characters can hold. The alternative (advanced after the first boss of the campaign) sends advanced invaders against tier one equipment for most of a campaign.
- Mechanical: yes (campaign play only)
- Edits: phantom-E03

---

## Chapter 13 — mimics

### phantom-025 · Chapter 13 · "the mimic's souls" (duplicate)
- Question: Same as phantom-004.
- This book now: See phantom-004.
- Evidence: see phantom-004.
- Ruling: CONFIRM as written.
- Why: See phantom-004. §7.6 needs no mimic row.
- Mechanical: no
- Edits: none

### phantom-026 · Chapter 13 · B-035, stamina before the mimic's first turn
- Question: Do the characters shed their stamina cubes before the mimic acts, or fight it exactly as the cleared encounter left them?
- This book now: Nothing is recovered: each character keeps damage cubes, stamina cubes and condition tokens, and the mimic takes the first turn (§13.2). B-035 was approved at Gate 1 but not applied (CH-13-022), because deferred recovery is on the preserve list.
- Evidence: official Explorers booklet: "players remove all black and red cubes from the characters' endurance bars and gain souls normally. Then, flip over the Ambush card" (lines 464–467), a full recovery before the mimic. Hollowed: "Players heal as normal, but do not have the opportunity to change equipment, recharge tokens, or move before opening" (lines 378–381). Source manuscript: "characters do not recover normally and remain in their current node … The mimic will take its turn first." Audit B-035: after a scaled encounter a character carries "typically 4-6 stamina and 2-4 damage"; proposed "remove all stamina cubes, but no damage cubes, before the mimic takes its first turn". This book §10.1: a turn recovers one stamina, and the Rest major action clears the bar.
- Ruling: CHANGE (each character removes every stamina cube before the mimic's first turn; damage cubes, condition tokens, used tokens and dead characters stay as they are).
- Why: The author's idea is that the chest is opened in the state the fight left the party in, and that idea is kept: wounds, conditions, spent estus and the dead all carry over, so a battered party still thinks twice. Stamina is different. It is the one part of that state the party can clear by rote: leave the last weak enemy standing for a round while everyone takes the Rest action, then kill it and open the chest. A rule whose best answer is a stall with no risk is bookkeeping, so the book does the stall for the players. It also stops the opening turn from killing a character who cannot act, which both other rulesets avoid by healing far more than this. This revises the reading of the preserve list recorded in CH-13-022; it applies a finding the author approved at Gate 1.
- Mechanical: yes
- Edits: phantom-E18, phantom-E19, phantom-E23 (worked example recomputed), phantom-E38 (glossary), phantom-E41 (new F.A.Q. answer)

### phantom-027 · Chapter 13 · failed mimic encounter and the cleared marker
- Question: When a mimic encounter is failed, does the encounter that held the chest keep a black cube from an earlier clear?
- This book now: No. The containing encounter is failed and resolved as any failed encounter: no souls, no treasure, card face down, black cube removed, rest (§13.4; §7.5).
- Evidence: official Explorers booklet: "If the party is defeated, the mimic returns to its terrain node … If the party returns to the tile and successfully defeats the encounter, they may choose to engage the mimic again" (lines 549–556). Source manuscript: "If the mimic kills all of the characters, the encounter is failed." A-060 proposed keeping the marker; CMP-0014 turns the card face down.
- Ruling: CONFIRM as written.
- Why: "A failed encounter has no black cube" is a rule without exceptions in §7.5, and the mimic fight is part of that encounter's resolution. An exception for one optional expansion would cost a sentence in three sections and buy nothing: the treasure cards still lie on the tile, so the next clear pays the full reward.
- Mechanical: no
- Edits: none

### phantom-028 · Chapter 13 · the chest token after the mimic is killed
- Question: What happens to the chest token and its node once the mimic is dead?
- This book now: The chest token returns to the supply, is not placed again at a reset, and its node becomes a basic node (§13.3). §5.5 and §11.5 say that terrain stays through a reset and have no exception for this.
- Evidence: official Explorers booklet: "When a mimic is defeated, remove it from the tile … A defeated mimic does not return to the tile" (lines 549–556), which removes the mimic and says nothing of the chest. This book §5.5: "an opened chest is never closed again and holds no further treasure"; a chest blocks its node "whether the chest is closed or open".
- Ruling: CHANGE (the chest token goes back on its node, open side up).
- Why: The book already has a state for a chest that has given up its treasure: an opened chest, which stays where it is for the rest of the game. Using it for the looted mimic means that §5.5, §7.5 step 5 and §11.5 need no exception and no pointer, and the tile needs no record that its chest is gone. The cost is that the node stays blocked, as it would be behind any other opened chest.
- Mechanical: yes (the node stays blocked)
- Edits: phantom-E21, phantom-E22

### phantom-029 · Chapter 13 · deferred resolution and §7.5
- Question: Does §7.5 accept that an encounter whose enemies are all dead can still end failed, if the mimic fight that follows is failed?
- This book now: §7.5: with mimics in play "the characters decide whether to open it before step 1, and a mimic that appears is fought before any reward is collected"; §13.4 states the failure.
- Evidence: §7.5, Encounter Resolution and Encounter Recovery; §13.1; §13.4.
- Ruling: CONFIRM as written.
- Why: §7.5 defers to §13 at exactly the right step and contradicts nothing in it. The failure conditions of §7.5 (every character dead, or a hollow character dead) are the same ones §13.4 uses.
- Mechanical: no
- Edits: none

### phantom-030 · Chapter 13 · the closed mimic model as a marker
- Question: After a failed mimic encounter, is the known mimic marked by the closed mimic model or by the face-up ambush card?
- This book now: The chest token goes back closed with its card beneath it, and the ambush card stays face up beside the tile as the record (§13.4).
- Evidence: official Explorers booklet pictures a "Closed Mimic (after the party is defeated by a Mimic)" model (lines 144–145).
- Ruling: CONFIRM as written.
- Why: The face-up ambush card is already on the table, cannot be mistaken, and works whether the party uses tokens or the plastic terrain. Players who own the model will put it on the node without being told.
- Mechanical: no
- Edits: none

### phantom-031 · Chapter 13 · several chests on one tile
- Question: One ambush card is dealt per tile. What if an encounter card places two chests?
- This book now: Written for one chest; silent on two.
- Evidence: official Explorers booklet: one ambush card "beside each tile" (lines 381–385). The core set supplies four chest tokens for four encounter tiles (§2.8), where barrels are eight and so two to a tile. The encounter cards were not supplied.
- Ruling: CONFIRM as written (no rule added).
- Why: The token count points to one chest per encounter card, so the case is not known to arise, and a rule for a case that may not exist is bloat. If a two-chest card is found, the sentence to add to §13.1 is: "If a tile holds more than one unopened chest, the ambush card applies to one of them, chosen by the players before the party decides; every other chest on that tile holds treasure and is opened when the encounter is resolved (see §7.7)." It is recorded under "not settled" and is not in the JSON.
- Mechanical: no
- Edits: none

### phantom-032 · Chapter 13 · mimic values not restated
- Question: Should the chapter print the mimics' threat, health, deck size and heat-up point?
- This book now: They are read from the data cards.
- Evidence: official Explorers booklet shows the Hungry Mimic at threat 10, health 18, deck size 4, heat-up point 8, block 1, resist 1 (lines 408–416).
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: The book restates no boss's printed values, and the mimics follow suit.
- Mechanical: no
- Edits: none

### phantom-033 · Chapter 13 · cross-chapter dependencies
- Question: Do §17.6, §19.8, §16.1, §16.4 and §6.6 say what §13 needs?
- This book now: §17.6 defers to §13; §19.8 makes the chest of Gallery of the Hidden Warrior a Voracious Mimic with no ambush card and completes the section on its death; §16.1 and §16.4 hold the alternation and aggro rules; §6.6 step 4 gathers the ambush cards.
- Evidence: the sections named.
- Ruling: CONFIRM as written.
- Why: All are in place. With phantom-028 the dependency on §5.5 and §11.5 for a removed chest token falls away.
- Mechanical: no
- Edits: none

### phantom-034 · Chapter 13 · glossary entry Chest
- Question: Does the entry Chest agree with §13.1?
- This book now: "With mimics in play, opening a chest requires revealing the tile's ambush card (see §13)."
- Evidence: `12_glossary.md` line 71; §13.1.
- Ruling: CONFIRM as written.
- Why: It agrees.
- Mechanical: no
- Edits: none

### phantom-035 · Chapter 13 · is the chest worth opening? (designer's point)
- Question: Do the reward and the risk make a live decision, with no bookkeeping?
- This book now: After a clear the party opens or forgoes; a forgone chest may be tried after any later clear; treasure pays one card, a killed mimic pays two; a failed mimic fight fails the whole encounter and the mimic waits, known, for the next attempt (§13.1 to §13.4).
- Evidence: official Explorers booklet (lines 369–385, 463–498, 548–556): the card is flipped after a full recovery; a beaten party "may choose to engage the mimic again". Hollowed (lines 369–392): open or forgo, heal first, and a forgone chest is lost until the encounter repopulates. Source manuscript: "once the mimic has been fought once, it must be fought again at the end of the encounter until it is killed"; mimics are for "increased challenge".
- Ruling: CONFIRM as written (with the change at phantom-026).
- Why: The decision works because it is taken on what the party can see: its wounds, its spent tokens, and after a failure the face-up card. The drafted "decides again after each later clear" is better than the manuscript's forced rematch, which can lock a weakened party into a fight it has already lost once and end the game on an optional rule. The prize is modest (one extra card), but the stake is modest too once stamina is cleared: nothing won is forfeited, only the spark a failure costs. Nothing is tracked beyond the cards on the table.
- Mechanical: no
- Edits: none

### phantom-036 · Chapter 13 · Hungry and Voracious Mimic in campaign play (designer's point)
- Question: Which mimic is fought in a campaign, where "the mini-boss" names no single moment?
- This book now: "The Hungry Mimic is fought if the mini-boss has not been defeated, and the Voracious Mimic if it has" (§13.2). §19.8 names the Voracious Mimic for one chest.
- Evidence: official Explorers booklet: "have not yet defeated a mini boss … have already defeated a mini boss" (lines 476–482). Source manuscript, Gameplay: "If a mini-boss has not been defeated, use the hungry mimic." This book §13.3 step 2: the mimic's extra card comes from the treasure deck of the current tier; §18.5: tier two only after the bonfire ascetic.
- Ruling: ADD (in campaign play: Hungry Mimic while the current tier is tier one, Voracious Mimic once it is tier two).
- Why: Same hole and same answer as phantom-024, so that invaders and mimics switch together. It also keeps the bargain honest: the stronger mimic guards a tier two card. Under the official wording a campaign party would meet the Voracious Mimic from its second section on while still drawing tier one treasure. A campaign's own text still wins (§19.8).
- Mechanical: yes (campaign play only)
- Edits: phantom-E20

---

## Chapter 14 — crystal lizards

### phantom-037 · Chapter 14 · the data card
- Question: Does the chapter describe the crystal lizard's behaviour correctly, the card not having been supplied?
- This book now: It takes its turn with the enemies in threat order, its behaviour icons move it away from the characters, and it makes no attack (§14).
- Evidence: official Iron Keep booklet: crystal lizards "spawn on terrain nodes instead of spawn nodes, do not actively attack the party when they activate, and do not need to be killed in order to defeat the encounter" (lines 124–132). Source manuscript: "their behaviours dictate that they simply run from the characters". Community guide: "Crystal Lizards act as an additional objective in some encounters."
- Ruling: CONFIRM as written.
- Why: The chapter states nothing the booklet and the manuscript do not, and leaves threat, health and movement to the card. The author should compare one card; no rule depends on the result.
- Mechanical: no
- Edits: none

### phantom-038 · Chapter 14 · marker for a tile where a crystal lizard was killed
- Question: What marks the encounter, given that only two crystal lizard models exist?
- This book now: "The party marks the tile to record the kill, for example by laying the killed model upside down beside the tile's encounter card."
- Evidence: this book §2.2: 2x Crystal Lizard. Official Iron Keep booklet: "Players may wish to place an opened chest token beside the tile" (lines 128–131). Source manuscript: an upside-down crystal lizard model. This book §7.5: a black cube on the encounter card marks a cleared encounter.
- Ruling: CHANGE (one damage cube is placed on the encounter card).
- Why: The example given fails the second time it is needed. The book already marks an encounter's history with a cube on its card, so a red cube beside the black one is the idiom the players know, it travels with the card through every reset, 32 are supplied, and it cannot be confused with the invader tokens that lie on the same cards. A definite marker also suits the book's voice better than "for example".
- Mechanical: no
- Edits: phantom-E25

### phantom-039 · Chapter 14 · supply of Titanite Scale cards
- Question: Is the reward capped at the three cards supplied, with one card for each kill?
- This book now: One card per killed crystal lizard; when none remains a kill awards nothing and no crystal lizard is placed again (§14).
- Evidence: official Iron Keep booklet: one card per encounter, and only if every crystal lizard is killed and the encounter is then won; "Once the party has defeated three different encounters with Crystal Lizards, there will be no Titanite Scale cards remaining. Ignore all Crystal Lizard icons on future encounters" (lines 133–141). Source manuscript: "Whenever a character kills a crystal lizard, they immediately place one Titanite Scale card into their inventory." Hollowed: "Players must defeat lizards before ending the encounter to receive their items" (lines 365–367).
- Ruling: CONFIRM as written.
- Why: A card for each kill, paid at once, is the author's rule and the simpler one: the official condition (all of them, and then win) needs the party to remember a result until the encounter ends. The three cards are the cap in every source, and substituting another card would put a weaker prize on the same risk.
- Mechanical: no
- Edits: none

### phantom-040 · Chapter 14 · who receives the card
- Question: Who takes the Titanite Scale when the crystal lizard dies to a condition, or to an attack that hits several models?
- This book now: "When a character kills a crystal lizard, that character takes one Titanite Scale card"; silent on a kill that no attack made (§14; §7.7).
- Evidence: official Iron Keep booklet: "add one Titanite Scale card to the inventory" (lines 125–127), the party's shared inventory in the official game. This book §7.7: cards awarded to the party go where the players decide, the aggro holder breaking a tie; §3.2: characters trade cards one for one outside an encounter.
- Ruling: CHANGE (the card is awarded to the party).
- Why: Every other card won from a kill (invader, mimic, boss) is awarded to the party; the crystal lizard was the odd one out, and it was the one with a hole. An award to the party needs no rule for bleed, poison or a shared attack, and it puts the upgrade on the weapon that wants it at once instead of after a trade at the bonfire.
- Mechanical: yes
- Edits: phantom-E24, phantom-E13 (§7.7), phantom-E12 (§7.7 list), phantom-E37 (glossary)

### phantom-041 · Chapter 14 · cross-chapter dependencies
- Question: Do §18.7, §8.3, §7.5 and §7.7 say what §14 needs?
- This book now: §8.3 and §18.7 exempt crystal lizards; §7.5 Encounter Start step 8 places them and Encounter Resolution excludes them from clearing; §7.7 awards the card at once.
- Evidence: the sections named.
- Ruling: CONFIRM as written.
- Why: All are in place. §7.7 changes only as phantom-040 requires. The failed-encounter steps of §7.5 remove the black cube and nothing else, so the damage cube of phantom-038 stays without a new rule.
- Mechanical: no
- Edits: none

### phantom-042 · Chapter 14 · is the chase worth it? (designer's point)
- Question: Do the reward and the escape rule make a real choice without bookkeeping?
- This book now: A crystal lizard flees on its turns, escapes the moment the last other enemy dies, pays a Titanite Scale when killed, and returns at every set-up of its encounter until one has been killed there (§14).
- Evidence: official Iron Keep booklet (lines 124–141); source manuscript ("the crystal lizards will respawn on repeated attempts until one dies"); Hollowed ("Lizards do not come back if the encounter is reset, even if not killed", lines 367–369).
- Ruling: CONFIRM as written.
- Why: The escape rule is the whole game here and it is right: to catch the crystal lizard the party must leave an enemy alive and take its attacks, so greed is paid for in damage. Letting the crystal lizards return until one is caught gives a repeated clear, which otherwise pays only the reduced reward, something to play for; the Hollowed rule (one chance ever) is harsher and no simpler. Ending the hunt at the first kill, with three cards in all, stops one tile from yielding the lot. After phantom-038 and phantom-040 the only thing to track is one cube.
- Mechanical: no
- Edits: none
