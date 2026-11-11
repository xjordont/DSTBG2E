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
- Why: The book already has a state for a chest that has given up its treasure: an opened chest, which stays where it is for the rest of the game. Using it for the looted mimic means that §5.5, §7.5 (Encounter Start, step 5) and §11.5 need no exception and no pointer, and the tile needs no record that its chest is gone. The cost is that the node stays blocked, as it would be behind any other opened chest.
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
- Evidence: official Explorers booklet: one ambush card "beside each tile" (lines 381–385). The core set supplies four chest tokens for four encounter tiles, against eight barrels (§2.8). The encounter cards were not supplied.
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

---

## Chapter 20 — player versus player

No official ruleset, booklet, or F.A.Q., and neither community ruleset, has a player-versus-player mode. For every entry in this chapter "official 2017 / 2022 / Extended / Hollowed" is therefore "silent", and the evidence is the author's source manuscript (27 bullets and a dodge list), the approved completion CMP-0009, the audit rows, and the standard rules of this book that the chapter borrows.

### phantom-043 · Chapter 20 · stalemate rule (duplicate)
- Question: Same as phantom-002.
- This book now: See phantom-002.
- Evidence: see phantom-002.
- Ruling: CONFIRM as written.
- Why: See phantom-002. "And no character dies" is rightly part of the test, so that a trap death counts as progress.
- Mechanical: no
- Edits: none

### phantom-044 · Chapter 20 · dodge-difficulty table (duplicate)
- Question: Same as phantom-003.
- This book now: See phantom-003.
- Evidence: see phantom-003.
- Ruling: CONFIRM as written (values).
- Why: See phantom-003. CH-20-018 stands as a mechanical change from the manuscript.
- Mechanical: no
- Edits: phantom-E29

### phantom-045 · Chapter 20 · characters who died in the boss encounter
- Question: Do characters who died fighting the boss take part in the PvP encounter that follows?
- This book now: No; if fewer than two characters take part, no PvP encounter is fought (§20.1).
- Evidence: source manuscript: "Dead characters are excluded from PvP." This book §16.5: "A character who died in the boss encounter stays out of play until the rest." Audit A-034 called the exclusion unreachable, on the premise that a defeated boss revives the dead; §16.5 does not revive them.
- Ruling: CONFIRM as written.
- Why: The author wrote the rule, §16.5 makes it reachable, and it gives dying to the boss a small extra cost without any new machinery. A-034's premise does not hold in the book as drafted.
- Mechanical: no
- Edits: none

### phantom-046 · Chapter 20 · order of events after a boss
- Question: Does the PvP encounter fall between the boss's rewards and the setup with its free rest, with one rest only?
- This book now: Yes: §16.5 steps 6 and 7, §20.1, §20.9.
- Evidence: §16.5 ("The spark is gained once and the rest is taken once for each defeated boss, whether or not a PvP encounter is fought"); §6.6 and §6.7 name the PvP encounter in their openings.
- Ruling: CONFIRM as written.
- Why: The three sections agree, and the order is the only one in which "restore as if rested" before the contest and one real rest after it both make sense.
- Mechanical: no
- Edits: none

### phantom-047 · Chapter 20 · choices the standard rules leave to the players
- Question: In a contest, who makes a choice that the standard game gives to the players jointly (equal push directions, the model displaced from a full node)?
- This book now: The player whose character makes the attack or the movement that calls for the choice (§20.5).
- Evidence: this book §8.4 and §5.3 ("the players choose"); no source for PvP.
- Ruling: CONFIRM as written.
- Why: A joint choice cannot survive in a contest, and "whoever caused it chooses" is the answer a table would reach on its own: the one who shoves aims the shove. One sentence covers every such choice.
- Mechanical: no
- Edits: none

### phantom-048 · Chapter 20 · heroic actions and card text that name enemies
- Question: Do heroic actions and card effects that name "an enemy" work against another character?
- This book now: §20.4 applies the icons and text of an attack option to a defender; heroic actions and other card text are not mentioned, although the setup readies every heroic action token (§20.1 step 3).
- Evidence: this book §3.5, Heroic Action ("the printed wording of a heroic action overrides any other rule"); §20.1 step 3; source manuscript: "Character turn structure is unchanged from basic rules."
- Ruling: ADD (in a PvP encounter the word enemy in a heroic action or on a treasure card means another character).
- Why: The setup hands every character a ready heroic action, so the first PvP encounter will raise the question. One sentence extends to all card text the rule the chapter already applies to attack options; effects that name a boss stay idle, and effects that help another character are the player's to withhold.
- Mechanical: yes
- Edits: phantom-E26

### phantom-049 · Chapter 20 · luck
- Question: May a character spend luck on an opponent's roll?
- This book now: No; a character rerolls only their own rolls (§3.5; §20.4).
- Evidence: this book §3.5, Luck ("one of their own attack rolls or defence rolls"); lead item 12 of `14_open_issues.md`, which belongs to another cluster.
- Ruling: CONFIRM as written.
- Why: Own rolls only is the simple rule, and in a contest the other reading would turn luck into a veto. If the cluster holding lead item 12 widens luck for co-operative play, §20.4 should keep "own rolls" for PvP in one sentence.
- Mechanical: no
- Edits: none

### phantom-050 · Chapter 20 · parry
- Question: Which weapon slot must hold the shield for a parry in PvP?
- This book now: §20.4 names no slot and defers to §9.6 (shield in the left weapon slot, attacker on the defender's node; riposte with the weapon in the right slot).
- Evidence: this book §9.6; the left-slot question is open in the chapter 03 and 09 lists (A-068).
- Ruling: CONFIRM as written.
- Why: Deferring is right: whatever §9.6 rules for a parry against an enemy holds against a character, and §20.4 need never change. Parry and riposte earn their four sentences in this chapter, because the dodge table makes a heavy attack the easiest to parry and gives the defender a way to punish it.
- Mechanical: no
- Edits: none

### phantom-051 · Chapter 20 · trap tokens
- Question: Are only the tokens in the supply used, does every character on the node dodge, is the printed damage unused, and does a full endurance bar kill?
- This book now: Yes to all four (§20.6).
- Evidence: source manuscript: "Players place a trap token on an outermost available node after each turn. Characters that move onto a trap token may attempt to dodge. Characters that fail to dodge a trap immediately die." CMP-0009: a character with no space for the dodge's stamina cube dies. This book §5.5, Traps ("each character on that node"); §9.5 (a dodge needs an empty space); §18.1 (a boss may fall mid-section, with trapped tiles still ahead).
- Ruling: CONFIRM as written.
- Why: The trap ring is the author's centrepiece: it turns pushes and forced dodge-moves into the way a contest is won, and death on a failed dodge is what makes it bite. Taking tokens off encounter tiles would break trapped encounters that a campaign section still has to fight, so the supply is the right source. "Each character on the node" is the standard rule and matters only when one push sends two characters to the same node. An exhausted character cannot dodge under §9.5, and since PvP removes the option of taking the damage, death is the only consistent result.
- Mechanical: no
- Edits: none

### phantom-052 · Chapter 20 · corner node
- Question: Is "the node nearest to one of the four corners of the tile, among the nodes that hold no terrain" a workable definition?
- This book now: As quoted (§20.1).
- Evidence: source manuscript: "Place each character in a corner of the boss encounter board."
- Ruling: CONFIRM as written.
- Why: It says what the author's bullet means and gives at most four characters four places. On a game board of irregular outline the players can still find the node nearest each corner; a board on which they cannot has not been identified.
- Mechanical: no
- Edits: none

### phantom-053 · Chapter 20 · victory marker
- Question: What marks a victory bonus, given that the core set has six wound tokens of value 1 and enemies need them?
- This book now: One wound token of value 1 beside the winner's dashboard (§20.8).
- Evidence: this book §2.8 (6x wound tokens of value 1, 3x of value 3, 1x of value 5); audit A-034 proposed a soul token; the official Phantoms booklet uses "a spare wound token" as a reminder only within one boss encounter (lines 160–167).
- Ruling: CHANGE (a spare token of any kind).
- Why: The marker stays beside the dashboard for the rest of the game, through every encounter in which wound tokens are scarce. Since the bonus is now a single flag (phantom-058), any spare token set beside the dashboard does the job, and neither §2.8 nor the glossary entry Wound token has to take on a second use.
- Mechanical: no
- Edits: phantom-E30, phantom-E31, phantom-E39

### phantom-054 · Chapter 20 · PvP in campaign play
- Question: Are PvP encounters played in a campaign, and which boss is the final boss there?
- This book now: §18.1, Player versus Player Encounters settles it: optional, after each boss, the campaign's final boss decides the ultimate victor, and a boss that does not complete its section is followed by no rest. §20 does not point there.
- Evidence: this book §18.1; glossary Final boss.
- Ruling: CONFIRM as written; a pointer is added to §20.9.
- Why: The rule exists and is sound in outline; the chapter that owns PvP did not cite it. One point in §18.1 is flagged for the campaign cluster under cross-cluster effects (a mid-section PvP encounter hands the party a full restoration).
- Mechanical: no
- Edits: phantom-E32

### phantom-055 · Chapter 20 · threat ties
- Question: Is "decided at random" enough, with no method named?
- This book now: Tied characters are ordered by agreement or, failing that, at random (§20.2).
- Evidence: CMP-0011; this book §7.5 (ties in threat settled by the players).
- Ruling: CONFIRM as written.
- Why: Any fair method serves, and naming one would be a rule about dice for a decision made once per contest.
- Mechanical: no
- Edits: none

### phantom-056 · Chapter 20 · glossary entries owned elsewhere
- Question: Must Aggro token, Encounter and Area-of-effect mention the PvP exceptions?
- This book now: Encounter already does; the headword PvP encounter states the rest.
- Evidence: `12_glossary.md` lines 9, 15, 111, 227.
- Ruling: CONFIRM as written.
- Why: The exceptions are stated once under PvP encounter, which is where a reader looks. Repeating them under three general headwords would lengthen entries that are right for every other encounter.
- Mechanical: no
- Edits: none

### phantom-057 · Chapter 20 · icon slugs
- Question: Do §20 and the standard chapters use the same icon tokens?
- This book now: `ast-0054-node-attack` for the AoE icon (§10.3 and §20.4) and `ast-0058-push-affected-enemies` for the push icon (§8.4, §10.3 and §20.5).
- Evidence: checked in the three files.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: The slugs match.
- Mechanical: no
- Edits: none

### phantom-058 · Chapter 20 · victory bonuses (designer's point)
- Question: Does the victory bonus earn its place, and may bonuses pile up?
- This book now: Each win after a boss other than the final boss gives +1 to the attack value of every later PvP attack; bonuses are cumulative (§20.8; §20.4 step 4).
- Evidence: source manuscript: "Victory on non-final bosses provides +1 attack damage in future PvP only." Cumulation comes from CMP-0009, not from the author. This book §19: campaigns list up to six bosses; §18.1: a PvP encounter follows each.
- Ruling: CHANGE (kept, but a character holds no more than one victory bonus).
- Why: Kept, because without it only the last contest of a game means anything and the earlier ones are skippable. Capped, because attack values in this game run from about 2 to 7 against blocks of about 3: +1 is already a large edge, +2 decides the last contest of a three-boss game before it starts, and a campaign of five or six bosses would reach +4 or +5. A single flag is also what the author's bullet says, costs one sentence less than cumulation, and removes a multiplication from every attack.
- Mechanical: yes
- Edits: phantom-E27, phantom-E30, phantom-E39

### phantom-059 · Chapter 20 · the option to decline a defence (designer's point)
- Question: Does "the defender may decline to defend" add anything?
- This book now: Fourth bullet of the defender's options: suffer the full attack value and be hit (§20.4).
- Evidence: this book §9.4: a block or resist costs no stamina, and with no dice the defence total is zero.
- Ruling: DELETE.
- Why: A free block can never leave the defender worse off than no defence, so the option is never chosen. It is a line of rules that carries no play.
- Mechanical: no
- Edits: phantom-E28

### phantom-060 · Chapter 20 · pushes and conditions between characters (designer's point)
- Question: Do pushes and conditions between characters earn their place?
- This book now: A push icon pushes each character hit and a condition icon places its token, both under the standard rules; terrain and traps apply (§20.5).
- Evidence: this book §8.4, §8.5, §5.5; source manuscript (traps on the outermost nodes; death on a failed trap dodge).
- Ruling: CONFIRM as written.
- Why: This is not a special rule but the absence of one: attack icons do to a character what they do to an enemy. Cutting it would need a sentence of its own and would gut the trap ring, which only pushes and forced dodge-moves make dangerous. The section is three short paragraphs of pointers and one rule (phantom-047).
- Mechanical: no
- Edits: none

### phantom-061 · Chapter 20 · the chapter as a design (designer's point)
- Question: Read whole, is anything else in the chapter length without play?
- This book now: Nine sections: setup with full restoration and corner placement, threat-order turns, standard character turns plus one trap, attack against block, resist, dodge or parry, pushes and conditions, the trap ring, costless death, victory, and the return to the game.
- Evidence: source manuscript (every one of these is one of the author's 27 bullets except the attack procedure, which the manuscript left undefined: audit A-032, a blocker); CMP-0009.
- Ruling: CONFIRM as written, with the cuts at phantom-003, phantom-058 and phantom-059.
- Why: The contest has three working parts that reinforce each other: a bar on which stamina and wounds compete, so that attacking exposes the attacker; a dodge difficulty that falls as the attack grows; and a ring of lethal traps that makes position matter. Everything else is the standard game by reference. The restoration at setup is needed for a fair start, costless death is needed for an optional mode inside a co-operative game, and the stalemate rule is needed for an end. After the three cuts no paragraph is left that a table would not miss.
- Mechanical: no
- Edits: none

---

## Chapter 21 — glossary

### phantom-062 · Chapter 21 · headwords defined in bold but never italicised
- Question: Boss spawn node, Distract, Pillar node and Character dashboard are defined in bold and not set in italics elsewhere. Does anything need to change?
- This book now: As described.
- Evidence: `work/phase2a/issues/21_glossary.md`.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: A typesetting note for the layout. The new sentence for §16.4 (phantom-E17) leaves "Distract" in roman, as §12.1 does.
- Mechanical: no
- Edits: none

### phantom-063 · Chapter 21 · reconciliation of duplicate glossary deltas
- Question: Where two chapters amended one headword, the owning section's entry was kept. Anything to decide?
- This book now: Reconciliation applied.
- Evidence: `work/phase2a/glossary/21_glossary.md`.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: A record of process. The seven glossary entries this cluster changes are listed under cross-cluster effects.
- Mechanical: no
- Edits: none

---

## Chapter 22 — F.A.Q.

### phantom-064 · Chapter 22 · a new player in the standard game
- Question: May a player join a standard game in progress, as §22.1 answers?
- This book now: Yes, on the campaign's terms: on the bonfire tile, for one spark (§18.4; §22.1).
- Evidence: official 2017: adding and dropping players is a rule of campaign play only (lines 1609–1620). Lead item 11 of `14_open_issues.md` belongs to another cluster.
- Ruling: CONFIRM as written.
- Why: The answer agrees with §18.4 as it stands, which is all an F.A.Q. answer must do. Whether §18.4 keeps the sentence is for the cluster that holds lead item 11; if it is cut, this question and answer are cut with it.
- Mechanical: no
- Edits: none

### phantom-065 · Chapter 22 · the embered reduction and traps
- Question: Does being embered reduce trap damage?
- This book now: No: the reduction applies to an attack that deals three or more damage, and §5.5 states that "trap damage is not an attack" (§7.3; §5.5; §22.3).
- Evidence: this book §5.5, Traps; §7.3; official 2017: a trap is dodged or suffered and "cannot be blocked" (lines 819–822).
- Ruling: CONFIRM as written.
- Why: "Attacks only" is one rule with no list of exceptions, and §5.5 already says in terms that a trap is not an attack. The doubt arose from "dodge it as an attack", which describes the procedure of the dodge and nothing else.
- Mechanical: no
- Edits: none

### phantom-066 · Chapter 22 · ties and choices left to the players
- Question: Should the answer give every unresolved choice to the aggro holder, as the approved draft did?
- This book now: The answer is limited to what the chapters state: players decide together; threat ties are settled at Encounter Start; contested treasure goes to the aggro holder (§22.4; §7.5; §7.7). §13.1 adds the chest decision.
- Evidence: Gate 1 OQ-29 ("tie-break to the aggro holder everywhere", decided for contested treasure); §7.7; §13.1.
- Ruling: CONFIRM as written.
- Why: An F.A.Q. answer cannot make a rule its chapters do not hold. A single fallback in §7.5 ("a choice the players cannot agree on is made by the player whose character holds the aggro token") would be good design and would replace three local tie-breaks, but it is a decision for the cluster that holds chapter 07; see cross-cluster effects.
- Mechanical: no
- Edits: none

### phantom-067 · Chapter 22 · the campaign answers
- Question: Do the answers on campaign sparks and transposition (§22.7) still match chapter 18?
- This book now: They match §18.3, §18.7 and §18.8 as drafted.
- Evidence: §18.3 (maximum one more than the start; one spark per boss), §18.7, §18.8, §18.2.
- Ruling: CONFIRM as written.
- Why: Nothing in this cluster touches them. They must be read again after the campaign cluster rules.
- Mechanical: no
- Edits: none

### phantom-068 · Chapter 22 · every answer against the chapters as they will stand (designer's point)
- Question: Does each answer agree with its chapter after this cluster's rulings, and which answers do other clusters' rulings touch?
- This book now: 50 questions in seven sections.
- Evidence: each answer read against the section it cites.
- Ruling: CHANGE (one answer reworded, one question added; every other answer agrees).
- Why: In §22.6, "Must an invader be killed?" now answers yes or no in the words of §12.2 (phantom-001), and a new question states what the characters recover before a mimic (phantom-026), since players who know the published rule expect a full recovery. The other five answers of §22.6 agree with §12, §13 and §14 after the rulings. Answers outside §22.6 that mention this cluster's rules also agree: "pool souls" (a summon is paid from the caller's own souls), "four characters" (no scaling for a mimic, a phantom or a crystal lizard), and "aggro in a boss encounter" (a summon's damage does not move the token). The answers that depend on other clusters are listed under cross-cluster effects.
- Mechanical: no
- Edits: phantom-E40, phantom-E41

---

## (a) Every CHANGE, ADD and DELETE

| Entry | Ruling | Section | What moves | Mechanical | Edits |
|---|---|---|---|---|---|
| phantom-009 | CHANGE | §12.2, Invasions; Invader Tokens; §2.9; glossary Invader token, Invasion | Invader tokens go only to face-down encounter cards that carry no black cube; the same test applies to the trigger at an embering | yes | E04, E06, E07, E09, E16, E33, E34 |
| phantom-015 | ADD | §12.1, Summoning | If the players cannot agree on the summon, the drawn cards are shuffled and one is drawn | yes | E01 |
| phantom-022 | ADD | §12.1, Summons in Combat | A summon does only what its cards direct: no minor action, no major action, no parry | no | E02 |
| phantom-024 | ADD | §12.2 | Campaign play: standard invaders in tier one, advanced invaders in tier two | yes (campaign) | E03 |
| phantom-026 | CHANGE | §13.1, §13.2, §13.3 example; glossary Mimic encounter; §22.6 | Each character removes every stamina cube before the mimic's first turn; nothing else is recovered (B-035 applied; CH-13-022 reversed) | yes | E18, E19, E23, E38, E41 |
| phantom-028 | CHANGE | §13.3 | A killed mimic's chest token returns to its node open side up, as any opened chest; the node stays blocked | yes | E21, E22 |
| phantom-036 | ADD | §13.2 | Campaign play: Hungry Mimic in tier one, Voracious Mimic in tier two | yes (campaign) | E20 |
| phantom-038 | CHANGE | §14 | A damage cube on the encounter card records a killed crystal lizard | no | E25 |
| phantom-040 | CHANGE | §14; §7.7; glossary Crystal lizard | The Titanite Scale card is awarded to the party, not to the character who made the kill | yes | E24, E13, E12, E37 |
| phantom-048 | ADD | §20.4 | In a PvP encounter "enemy" in a heroic action or on a treasure card means another character | yes | E26 |
| phantom-053 | CHANGE | §20.8; glossary Victory bonus | The victory bonus is marked by a spare token of any kind, not a wound token of value 1 | no | E30, E31, E39 |
| phantom-058 | CHANGE | §20.4 step 4; §20.8; glossary Victory bonus | A character holds no more than one victory bonus (+1, not cumulative) | yes | E27, E30, E39 |
| phantom-059 | DELETE | §20.4 | The option to decline a defence | no | E28 |
| phantom-068 | CHANGE | §22.6 | The invader answer reworded; a question on recovery before a mimic added | no | E40, E41 |

Wording edits attached to CONFIRM rulings (no rule moves): E11 (phantom-001), E29 (phantom-003, table in three rows), E14 and E15 (phantom-010, §6.5 and §6.6), E10 and E12 (phantom-016, §12.2 and §7.7), E17 (phantom-018, §16.4), E35 and E36 (phantom-019, glossary Weak arc and Turn), E05 and E08 (phantom-021, §12.2), E32 (phantom-054, §20.9).

Gate 1 and change-log positions affected: B-035 (approved at Gate 1) is now applied and CH-13-022 is reversed; CH-12-033 (invader counts), CH-12-034 (substitute blanks) and CH-20-018 (dodge values) are confirmed; the cumulative victory bonus of CMP-0009 is revised to the flat +1 of the source manuscript; the "killer takes the card" rule of the source manuscript and CMP-0015 is revised to an award to the party. No Gate 1 OQ answer is revised.

## (b) Not settled, and why

1. Two chests on one encounter card (phantom-031). The encounter cards were not supplied, so it cannot be checked whether any card places two chests. No rule is added; the sentence to use if one does is given in the entry.
2. Cards not supplied (phantom-014, phantom-037). The summon behaviour cards and the crystal lizard data card could not be read. The rulings rest on the booklets' descriptions and do not depend on printed values, but the author should compare one summon card (dice icons, shift and Distract icons) and the crystal lizard card (threat, health, movement away from the nearest character).
3. A Level 4 encounter card in a campaign section. As §12.2 and §18.1 stand, the Level 4 encounter card dealt at a section's setup is an encounter card and can take an invader token, so an advanced invader can join a Level 4 encounter. Nothing in the sources speaks to it and it was not raised as an issue. It is left for the campaign cluster: either accept it or add "No invader token is placed on a Level 4 encounter card" to §12.2.
4. Online discussion. Reddit and BoardGameGeek threads on these rules could not be reached (see Sources). No ruling above depends on an online source; where the community guide was reachable it is quoted.

## (c) Cross-cluster effects for the lead editor

Edits in this cluster's JSON that land in other clusters' chapters:

- §7.7 (chapter 07): E12 names the invader's card and the Titanite Scale card among the cards awarded to the party and words the tie-break as "when the card is awarded"; E13 awards the Titanite Scale to the party. If the chapter 07 cluster rewrites the same paragraph, merge by hand.
- §6.5 step 5 and §6.6 step 15 (chapter 06): E14 and E15 add "and any character is embered".
- §2.9 (chapter 02): E16 adds "that carries no black cube" to the note on invader tokens.
- §16.4 (chapter 16): E17 adds the pointer to the Distract icon.
- Glossary: Invader token (E33), Invasion (E34), Weak arc (E35), Turn (E36), Crystal lizard (E37), Mimic encounter (E38), Victory bonus (E39). The entries Invader, Mimic, Summon, Chest, Cleared, Trap token, Dodge difficulty, PvP encounter and Ultimate victor were checked and need no change.

Places not edited that depend on this cluster's rulings:

- §18.1, Section Setup (chapter 18): the bullet "no more than one invasion is provoked in each section (see §12.2)" stays true. The campaign rule for standard and advanced invaders and for the two mimics now lives in §12.2 and §13.2 (E03, E20) and keys on the current tier of §18.5 and §18.7; if the campaign cluster changes how tier two opens, both sentences follow it.
- §18.1, Player versus Player Encounters (chapter 18): when a boss's defeat does not complete its section, every character who took part is "restored as at the start of the PvP encounter" and the exploration continues. An optional contest therefore hands a co-operating party a full recovery, with estus, luck and heroic action readied, in the middle of a section. Recommended to the campaign cluster: in campaign play a PvP encounter follows only a boss whose defeat completes a section. This needs no record of the characters' earlier state.
- §19.4, The Gauntlet (chapter 19): the official booklet has a listed invader return "every time the party enters that encounter until the invader is defeated" (Phantoms lines 647–652); this book has it appear once, and under §12.2 it vanishes at the first character death. One death therefore removes a Gauntlet invader for good. If the campaigns cluster restores the official rule, §12.2 needs no edit, because a campaign's own rule takes precedence (§18.1).
- §19.8 (chapter 19) names the Voracious Mimic outright and is unaffected by E20.
- §5.5, Chests and §11.5 (chapters 05 and 11): with phantom-028 neither needs an exception for a mimic's chest. With phantom-038 the damage cube on an encounter card stays through a reset; §11.5 step 2 need not mention it, but may.
- §7.5 (chapter 07): no change needed. If that cluster adopts one general tie-break (the aggro holder decides any choice the players cannot agree on), the local tie-breaks in §7.7, §13.1 and the new one in §12.1 (E01) can be cut to a citation, and the answer at §22.4 "Who decides …" shortens.
- §3.5, Luck (lead item 12): §20.4 relies on "own rolls only". If luck is widened for co-operative play, §20.4 should keep own rolls for PvP.
- §9.6 and §3.2, parry slot (chapter 03 and 09 lists): §20.4 defers to §9.6 and follows whatever is ruled.
- §5.5, Traps (lead item 8): §12.1 ("summons neither trigger traps nor suffer them") and §20.6 follow it. If phantoms are made to trigger traps, §12.1 changes with it.
- §7.6 soul table (lead item 1): the invader rewards (3 and 4) sit in the same table as the encounter rewards and are confirmed here at those values.
- §15.6 and the answer at §22.5 on a character pushed off a boss's node: the book limits every push to the character's arc; the official F.A.Q. answers that a push caused by a boss's attack only needs to move the character farther from the boss (F.A.Q. lines 28–37). This is the boss cluster's to settle; the F.A.Q. answer must follow.

F.A.Q. answers that other clusters' rulings would touch (none is edited here):

| F.A.Q. question | Depends on |
|---|---|
| §22.1 left and right weapon slot; §22.2 parry with a two-handed weapon | parry-slot ruling (§3.2, §9.6; A-068) |
| §22.1 pooling souls | shop and bonfire ascetic rulings (§11.4, §18.7; lead item 10); the summon clause is confirmed here |
| §22.1 a new player joins | lead item 11 (§18.4) |
| §22.2 two-handed reroll with luck | lead item 12 (§3.5) |
| §22.3 stagger; frostbite | lead item 16 (§8.5) |
| §22.3 embered reduction; dodging onto a trap; enemies and traps | lead item 8 (§5.5); the embered answer is confirmed here (phantom-065) |
| §22.4 who decides a tie | any general tie-break added to §7.5 |
| §22.4 reduced reward ("campaign play uses the same table") | lead item 1 (§18.5) |
| §22.4 Level 4 encounter reset | lead item 19 (§6.7) |
| §22.4 sold boss treasure | lead item 10 (§11.4) |
| §22.5 Ornstein & Smough; Twin Gargoyles | lead items 4 and 5 (§17) |
| §22.5 order of characters in a boss encounter | lead item 13 (§16.1) |
| §22.5 pushed off a boss's node | §15.6, see above |
| §22.6 summon timing; summon and invader together | none: confirmed here (Gate 1 OQ-32) |
| §22.7 all four answers | campaign rulings (§18.2, §18.3, §18.7, §18.8; lead item 1) |
