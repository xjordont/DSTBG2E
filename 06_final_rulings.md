# 06 — Final Rulings (Class A)

Date: 2026-11-11. Authority: the author delegated every open rules question to the lead editor ("use your best judgement as a pro boardgame designer"), asked that the official rulesets, the two community rulesets, and online discussion inform each ruling, and set the standard: clear, intuitive, simple, mechanically consistent, well written, tactically interesting, and free of bloat. On the same date the author confirmed ownership of the rights in all source artwork and supplied eight further expansion booklets. This file records what was decided. It supersedes `05_gate1_decisions.md` wherever the two differ, and each such place is named below.

## 1. Method

1. Every item in `14_open_issues.md` (22 lead items and the per-chapter lists) was assigned to one of five rules areas.
2. For each area a researcher read the chapters, the author's source manuscript, the official 2017 and 2022 rulebooks, the official F.A.Q., the official expansion booklets, the two community rulesets (Extended Rules, Hollowed Edition), and what online discussion could be reached, and wrote one entry per question with the evidence and a recommendation. The memos are `work/phase3/rulings_<area>.md`; the proposed text changes are `work/phase3/edits_<area>.json`.
3. The lead editor read every ruling that changes play, settled the places where two areas met, withdrew what the evidence did not support, and added the follow-up changes the researchers flagged for other areas (`work/phase3/lead_overrides.json`, `work/phase3/edits_lead.json`).
4. `tools/apply_rulings.py` applied the accepted changes; each is an entry in `11_change_log.md` that cites its ruling, marked `[MECHANICAL CHANGE]` where play changes.
5. Online evidence was thin: several forums refuse automated reading. No ruling rests on an online source alone; the memos say which sources were reached.

Totals: 334 questions answered (add 22, change 71, confirm 177, delete 4, not a rules question 60); 225 text changes applied, 98 of them changes to play.

## 2. The 22 lead questions

| # | Question | Ruling | Entry |
|---|---|---|---|
| 1 | Campaign soul rewards against doubled stat costs | Confirm: One lever is enough, and it is the official one. Souls per character from first clears, with one repeat of each section's encounters in brackets:  | campaign-001 |
| 2 | When an invader's encounter is cleared | Confirm: The general rule of §7.5 (every enemy model killed) already gives this answer with no special case, and every source that speaks treats the invader as one of the enemies. The alternative turns the invader into a second crystal lizard: the party kills the weak enemies and the hunter walks away, which removes the fight … | phantom-001 |
| 3 | What marks hollowing | Change: The book asks for eight cubes that no set supplies. The only cube in the box that is never placed on an endurance bar is the white one, and it is what the author wrote. White on the bar cannot be read as black (stamina) or red (damage), which the Hollowed Edition's black cubes can once a bar fills with stamina. A party … | core-001 |
| 4 | Bosses whose rules were placeholders | Change: The book promised a definite rule for every boss and delegated nine. The official rules exist, are short, and fit the book's existing forms (deck built by procedure, node-targeting attack decks, special heat-ups), so they are brought in, restated in this book's terms. | boss-001, boss-002, boss-003 |
| 5 | Ornstein & Smough | Change: OQ-25 rested on a premise that the evidence contradicts: the pair has two data cards and two health dials, and every paired card gives both models a behaviour, so "each card names the model that acts" cannot be played with the printed cards. The official fight is also the better design. It asks one clear question, which … | boss-012 |
| 6 | Player-versus-player stalemate | Confirm: The hole is real. A block costs nothing and an attack costs stamina that fills the same bar as damage, so the defender is favoured and two careful players can stop hurting each other; the trap supply is only what is left after trapped encounters have taken their share of the 20 tokens, and may be nil. The rule is two … | phantom-002 |
| 7 | Player-versus-player dodge difficulty | Confirm: The author's idea is sound and worth its place: a cheap attack is quick and hard to dodge, a heavy one is slow and easy to dodge, so attacker and defender each have a real choice between force and certainty. The manuscript's end values break it: a free attack that cannot be dodged and a heavy attack that is dodged … | phantom-003 |
| 8 | Traps and models other than characters | Confirm: Every ruleset agrees, and the trap is a knowledge game for the party: if enemies revealed tokens, their movement would hand the party the information for nothing, and if they suffered damage the party would herd them onto unknown nodes, which is clever but adds an enemy dodge rule the game does not have. One sentence, … | combat-001 |
| 9 | Shop stocking | Confirm: A cap of twelve draws against a quota of twelve places leaves the shop short almost every time, and a short shop defeats the reason for the quota, which is that every kind of character finds something to buy. The quota is the author's answer to the game's best-known complaint (blind, unsorted treasure) and it costs one … | core-002 |
| 10 | Shop sales | Confirm: All three answers are what a player would guess. A sold card goes back where cards of its kind live, and for an ember card that is the shop shelf, which also keeps the count of ember cards fixed. A flat sell value with nothing added for Titanite needs no table. A free service follows both official rulebooks. One … | core-003 |
| 11 | Joining or leaving a game | Confirm: A player would guess that the rule for a campaign serves any game, and one rule for both is cheaper than a prohibition. The two steps that set the campaign maximum of the spark dial have nothing to act on in a standard game, and the text should say so. | campaign-002 |
| 12 | Luck | Confirm: Each character owns one token and one decision. Letting tokens cross the table would pool four rerolls on whichever roll matters most and take the decision away from the owner. The stronger reroll (any or all dice) is the author's and is kept; it is paid for by the token returning only at a rest. One wording gap is … | core-004 |
| 13 | Boss encounter details (shortcut, facing, turn order) | Confirm: The shortcut is the author's reward for reaching the boss, and it removes the published game's most criticised chore, re-clearing the route before every boss attempt. Charging the skip cost would tax exactly the retry the shortcut exists to speed up, and would add book-keeping with no decision in it. The choice that … | boss-013, boss-014, boss-015 |
| 14 | The mimic's reward | Confirm: Four sources agree and none gives a soul value; inventing one adds a row to the soul table for no gain. Double treasure is the right prize for a chest that bites: it is what the party came to the chest for, and it needs no arithmetic. The risk side of the bargain is dealt with at phantom-026. | phantom-004 |
| 15 | Appendix A and the Butcher Knife | Confirm: The appendix exists to make requirements match the weapons' origin, and 24 does. It also takes the card off the one-point boundary, so nobody has to recall whether 25 is "below 25". The Tier column is a convenience and every row was checked against the rule of §6.2 (61 rows, no error); the Treasure Type section already … | core-005 |
| 16 | Frostbite duration | Confirm: In every source the two conditions share one duration; Gate 1 moved stagger, and leaving frostbite behind would make this the only ruleset in which they differ. The two rules differ in play only when frostbite is placed during the affected model's own turn (a riposte with a frostbite weapon against an enemy, an … | combat-002 |
| 17 | The dropped Firekeeper luck purchase | Confirm: The purchase only ever made sense where the Firekeeper could be visited without resting. In this book she is visited only during a rest, and the rest has already readied the token, so the purchase would buy nothing. The current official rules dropped it for the same reason. Bringing it back would need a second kind of … | core-006 |
| 18 | Component counts and campaigns from booklets not first supplied | Change: Each correction replaces an unverifiable figure or list with the published one. | campaign-003 |
| 19 | Level 4 treasure | Confirm: This is the author's own rule, not a reduction made in editing. It is also good design: a mega-boss's treasure would otherwise be won only when the game is over, and here one of its cards is in play for the fight that matters. A ninth random card for each character, with one paid rest left to equip it, would add … | core-007 |
| 20 | Layout of the first leg | Change: In this book the route is a fixed chain of four encounters, so the shape on the table has no effect on play. Two different shapes for one function is one rule too many. A straight line of seven tile widths does not fit most tables. And "exactly two doorways open on to adjacent tiles" cannot be met by a tile with three … | core-008 |
| 21 | Painted illustrations | Closed by the author: the rights in all source artwork are confirmed, so the paintings are placed and the anatomy plates are shown whole. | author, 2026-11-11 |
| 22 | Shortage of blank invader tokens | Confirm: Substitution is what a table would do unprompted, costs one sentence, needs no notion of which tiles go without, and keeps the invader hidden among every eligible card. The alternative (tokens only on the four nearest cards) tells the party that the far encounter is safe. With the ruling at phantom-009 a cleared … | phantom-005 |

## 3. Rulings that change play

| Edit | Where | What changes |
|---|---|---|
| core-E08 | §6.6 | The shop is stocked before the treasure rewards are dealt, as in the first setup (§6.3 before §6.5), so the five legendary cards are in the tier two deck when the second leg's rewards are dealt. |
| core-E31 | §4.2, Titanite | One destination rule for every sold card: each card returns to the place of its own kind, as a replaced Titanite card already does (Appendix B). |
| core-E32 | §11.4, Sales | As core-E31. |
| core-E33 | Glossary | Carries both Titanite rulings: Titanite is recognised by name (core-063) and a sold Titanite card goes to the place of its own kind (core-048). |
| core-E34 | §4.2, Titanite | A test by name settles Demon Titanite and Blue Titanite without a second list: every card called Titanite behaves as Titanite. |
| core-E35 | §11.1 | Returning and resting are one act, as §7.5 already states. |
| core-E36 | §11.1 | Removes the state of standing at the bonfire without resting, which had no use except to fight cleared encounters again without spending a spark. |
| core-E37 | Glossary | Glossary follows §11.1. |
| combat-E01 | §5.5, Gravestones | One scry for each gravestone: the token count is the rule, and the "however many" clause is deleted. |
| combat-E02 | §7.5, Encounter Resolution | Keeps the resolution step in line with §5.5. |
| combat-E03 | §7.5, Encounter Resolution | Keeps the scry rule in line with §5.5 and fixes the order of several scries. |
| combat-E04 | Glossary, Gravestone | Glossary follows §5.5. |
| combat-E12 | §8.2 | One meaning for the repeat icon on every data card and behaviour card: the whole row is repeated. |
| combat-E18 | §9.1 | States the repeat rule for an enemy data card where the row of icons is described, in the words §16.1 uses for a boss. |
| combat-E19 | §9.3 | Deletes the attack-only special case, which was written for the scaling rule that Gate 1 removed. |
| combat-E22 | §9.6 | The parry was the only rule in the book that depended on which weapon slot held a card; the choice of slot carried no decision. |
| combat-E23 | §9.6 | As combat-E22. |
| combat-E24 | §9.6, Riposte | Follows the either-slot parry and states the spell exclusion that the word "weapon" only implied. |
| combat-E27 | §10.3, Repeat | A repeated attack is a permission, as every other attack of the Attack major action is ("up to one attack with each weapon"). |
| combat-E29 | §10.5 | Without it every character scales such a weapon at once, a +1 that rewards nothing and a red cube that records no choice. |
| combat-E30 | §3.2 | Follows §9.6 as changed by combat-E22. |
| combat-E35 | §22.2 | Follows §10.5 as changed by combat-E29. |
| combat-E36 | Glossary, Repeat | Glossary follows §9.1, §10.3 and §16.1. |
| combat-E39 | Glossary, Parry | Glossary follows §9.6. |
| combat-E41 | Glossary, Scaled (weapon) | Glossary follows §10.5. |
| boss-E01 | §15.5, Heat-Up | The whole deck is reshuffled with the heat-up card, so the learned order is lost as both official rulebooks intend, and one timing (the start of the boss's next turn) replaces two. |
| boss-E02 | §15.5, Heat-Up | The example must compute from the heat-up rule as changed by boss-E01. |
| boss-E03 | §15.3 | The Asylum Demon mini-boss is fought on its expansion's mega-boss game board; §15.3 must allow the exception that §17.3 now states. |
| boss-E04 | §16.1 | States in the boss turn where the heat-up of boss-E01 is carried out, without renumbering the steps. |
| boss-E06 | §16.4 | Without this the token cannot move during the first part of the Executioner's Chariot encounter, when the boss cannot be damaged; one general clause closes the gap for every boss that brings other enemies. |
| boss-E07 | §16.5 | Boss Death must not be resolved when one of several boss models falls (Ornstein & Smough, the Four Kings). |
| boss-E08 | §17.1, Two Boss Models in One Encounter | One framework for every boss with several models: each model has its own health dial and all models act on each card, as the official cards for Ornstein & Smough and the booklet for the Four Kings both direct. Revises Gate 1 OQ-25 for Ornstein & Smough. |
| boss-E10 | §17.2 | Restores the official structure: two models with their own health, both acting each turn, and a heat-up when the first falls. It matches the printed cards and keeps the fight's one real decision, which of the two to defeat first. Revises Gate 1 OQ-25. |
| boss-E11 | §17.3, Setup | Settles the open fact: the Asylum Demon mini-boss is fought on the mega-boss game board, so both demons meet the pillars. The sentence about tiles without pillar nodes is no longer needed. |
| boss-E13 | §17.4, Great Grey Wolf Sif | Replaces 'as the data card directs' with the data card's rule, so the entry is complete. |
| boss-E20 | §17.10, The Four Kings | Replaces the placeholder with the official rules of the Four Kings, restated in this book's terms. |
| boss-E21 | §17.10, Gaping Dragon | Replaces the placeholder with the official rules of the Gaping Dragon, restated in this book's terms. |
| boss-E22 | §17.10, Guardian Dragon | Replaces the placeholder with the official rules of the Guardian Dragon, restated in this book's terms. |
| boss-E23 | §17.10, The Last Giant | Replaces the placeholder with the official rules of the Last Giant, restated in this book's terms. |
| boss-E24 | §17.10, Manus, Father of the Abyss | Replaces the placeholder with the official rules of Manus, restated in this book's terms. |
| boss-E25 | §17.10, Old Iron King | Replaces the placeholder with the official rules of the Old Iron King, restated in this book's terms. |
| boss-E26 | §17.10, Vordt of the Boreal Valley | Replaces the placeholder with the official rules of Vordt, restated in this book's terms. |
| boss-E31 | Glossary, Heat-up | Keeps the glossary in step with the heat-up rule of boss-E01. |
| boss-E35 | Glossary, Aggro token | Keeps the glossary in step with boss-E06. |
| boss-E42 | §2.3, Main-Bosses | Keeps §2.3 in step with boss-E10. |
| boss-E46 | §22.5 | Keeps the F.A.Q. in step with boss-E10. |
| campaign-E16 | §18.1, Level 4 Encounters and Mega-Bosses | A mega-boss has two treasure cards, and Call of the Abyss and Into the Depths each list three Level 4 encounters before one mega-boss, so the standard reward cannot be paid; the campaign's own rule is that boss treasure comes only from bosses. |
| campaign-E17 | §18.5 | Keeps §18.5 in step with §18.1 and removes the contradiction with the sentence before it. |
| campaign-E18 | §18.3 | A party purchase is paid by the party, as the bonfire ascetic already is, so that one character without souls cannot block it. |
| campaign-E19 | §18.3 | The example must compute from the pooled payment. |
| campaign-E20 | §18.7 | Two party purchases now share one payment rule. |
| campaign-E22 | Bonfire ascetic | Glossary follows §18.3 and §18.7. |
| campaign-E23 | §22.1 | F.A.Q. follows §18.3 and §18.7. |
| campaign-E28 | §18.4 | The cost of joining is one spark, so one spark is enough; a second condition is not needed. |
| campaign-E30 | §18.1, Section Setup | Six of the twelve campaigns name no sets for their decks; one default closes the gap for all of them. |
| campaign-E33 | §18.1, Section Setup | §12.2 chooses the token by whether the mini-boss has been defeated, which has no meaning in a campaign; the bonfire ascetic already takes the mini-boss's place for treasure and the shop. |
| campaign-E35 | §19.4 | The Gauntlet's own rule differs from Ambush Lies Ahead: each invader must be beaten, which is the point of the campaign. |
| campaign-E36 | §19.6 | The official list gives Section One a bonfire tile, so the special rest rule answers a problem that does not exist and is deleted. |
| campaign-E38 | §19.7 | The official campaign has five sections; the manuscript omitted the fourth. |
| campaign-E39 | §19.10 | Outskirts of Blighttown is the Level 4 encounter of the section, not a Level 3 encounter. |
| campaign-E40 | §19.10 | The official campaign gives this substitution, which opens the campaign to a party without Darkroot. |
| campaign-E41 | §19.12 | Restores the campaign's own soul grant, names the board for the mini-boss, and says when each of the three free-order sections is set up. |
| campaign-E48 | §19.12 (insert §19.13 to §19.16 after it) | Adds the four published campaigns the book lacked (items campaign-041 to campaign-044), restated in this book's terms. |
| phantom-E01 | §12.1, Summoning | Gives the one joint choice in the chapter that had no tie-break a tie-break that needs no token and no new term. |
| phantom-E03 | §12.2 (opening paragraph) | A campaign has several mini-bosses or none, so 'the mini-boss' names no moment there; the current tier is the one switch every campaign has, and it keeps the stronger invaders in step with the stronger treasure. |
| phantom-E04 | §12.2, Invasions | A reset turns every encounter card face down, cleared ones included; without the qualifier an invader token can land on an encounter the party skips and the invasion is wasted. |
| phantom-E06 | §12.2, Invader Tokens, step 2 | Same qualifier as the trigger: a cleared encounter receives no token. The substitution rule for a shortage of blank tokens is kept unchanged. |
| phantom-E07 | §12.2, Invader Tokens, step 4 | Keeps step 4 in line with step 2. |
| phantom-E13 | §7.7 | Keeps §7.7 in step with §14: the Titanite Scale card is awarded to the party, whatever killed the crystal lizard. |
| phantom-E16 | §2.9, Phantoms | Keeps the component note in step with §12.2. |
| phantom-E19 | §13.2 | The ambush stays dangerous because damage carries over, but the fight no longer opens with characters who cannot act, and the party has no reason to stall on the last enemy to shed stamina before opening a chest. |
| phantom-E20 | §13.2 | Same anchor as for invaders: a campaign has no single mini-boss, and the mimic's extra card is drawn from the treasure deck of the current tier, so the stronger mimic guards the stronger treasure. |
| phantom-E21 | §13.3, step 4 | An opened chest already stays on its node for the rest of the game; treating the looted mimic's chest the same way removes an exception from §5.5, §7.5 and §11.5. |
| phantom-E22 | §13.3 | Follows the change to step 4: no special terrain state is left behind by a killed mimic. |
| phantom-E23 | §13.3 (example) | The example now computes from §13.2 as amended: stamina cubes are removed before the mimic's first turn, damage cubes are kept. |
| phantom-E24 | §14 | An award to the party needs no rule for a crystal lizard killed by a condition or by an attack that hits several models, and it treats this card as every other card won from a kill is treated. |
| phantom-E26 | §20.4 | The setup readies every heroic action token, so the chapter must say whether a heroic action that names an enemy works; one sentence extends the rule already stated for attack options. |
| phantom-E27 | §20.4, step 4 | The victory bonus is no longer cumulative. |
| phantom-E30 | §20.8 | A flat +1 gives the earlier contests a stake without deciding the last one in advance; a cumulative bonus reaches +4 or +5 in a campaign of five or six bosses. A spare token replaces the value 1 wound token, of which the core set has six and enemies need all. |
| phantom-E33 | Invader token | Keeps the entry in step with §12.2, Invader Tokens. |
| phantom-E34 | Invasion | Keeps the entry in step with §12.2, Invasions. |
| phantom-E37 | Crystal lizard | Keeps the entry in step with §14: the card is awarded to the party. |
| phantom-E38 | Mimic encounter | Keeps the entry in step with §13.2 as amended. |
| phantom-E39 | Victory bonus | Keeps the entry in step with §20.8: one bonus, not cumulative, marked by a spare token. |
| phantom-E41 | §22.6 | Players who know the published rule expect a full recovery before the mimic; the answer states this book's rule as amended. |
| lead-E01 | §5.5, Traps | The number of traps must not depend on which tiles happen to touch; the exclusion is keyed to the doorways the party uses. |
| lead-E02 | §18.1, Player versus Player Encounters | A contest in the middle of a section handed a co-operating party a full restoration; tying the contest to the end of a section removes that and the rule that restored characters to an earlier state. |
| lead-E03 | §18.1, Player versus Player Encounters | Follows lead-E02. |
| lead-E09 | §11.4, Sales | A card that came from outside the decks no longer enters a treasure deck when it is sold, from which it could have been dealt as an ordinary reward. |
| lead-E10 | §6.1 | The six souls exist to help a lone character through the first encounters, and could not be spent before a rest that costs a spark. |
| lead-E17 | §12.2 | The invader follows the one heat-up procedure and timing of boss-E01: deck and discard pile reshuffled with the added card at the start of its next turn. |
| lead-E18 | §13.2 | As lead-E17, for the mimic. |
| lead-E20 | §8.5, Stagger | A summon rolls dice to attack and to defend, as a character does (§12.1), and has no fixed block, resist, or dodge value for the token to reduce. |
| lead-E21 | Glossary, Stagger | Glossary follows §8.5 (lead-E20). |
| lead-E22 | §6.1 | lead-E10 is withdrawn. Letting a lone character spend before setting out made an exception to the one rule that souls are spent at a rest (§7.6, §11.3, §11.4, and three glossary entries); the author's rule stands as written, and the six souls are spent at the … |

## 4. Where a Gate 1 answer is revised

- boss-012 (lead item 5, Ornstein & Smough): OQ-25 rested on a premise that the evidence contradicts: the pair has two data cards and two health dials, and every paired card gives both models a behaviour, so "each card names the model that acts" cannot be played with the printed cards. The official fight is also the better design. It asks one …
- phantom-026 (Chapter 13 · B-035, stamina before the mimic's first turn): The author's idea is that the chest is opened in the state the fight left the party in, and that idea is kept: wounds, conditions, spent estus and the dead all carry over, so a battered party still thinks twice. Stamina is different. It is the one part of that state the party can clear by rote: …

## 5. The lead editor's own decisions

Recommendations not adopted, or adjusted:

- campaign-E01: not applied. Hollow cubes follow the core ruling (core-E01 to E04, E20): the white cubes of the core set.
- campaign-E02: not applied. As campaign-E01.
- campaign-E24: not applied. Withdrawn by the lead editor: the spark dial shows 1 to 20, so no ceiling of five is needed; the campaign maximum stays the starting value plus one.
- campaign-E25: not applied. As campaign-E24.
- campaign-E26: not applied. As campaign-E24.
- campaign-E27: not applied. As campaign-E24.
- phantom-E28: not applied. Same deletion as combat-E33, applied once.
- phantom-E15: applied with adjusted text. Step renumbered by core-E08.

Follow-up changes across areas:

- lead-E01 (§5.5, Traps): The number of traps must not depend on which tiles happen to touch; the exclusion is keyed to the doorways the party uses.
- lead-E02 (§18.1, Player versus Player Encounters): A contest in the middle of a section handed a co-operating party a full restoration; tying the contest to the end of a section removes that and the rule that restored characters to an earlier state.
- lead-E03 (§18.1, Player versus Player Encounters): Follows lead-E02.
- lead-E04 (§12.2, End of an Invasion): Two campaigns bring a listed invader back until it is killed; the general rule now points to them.
- lead-E05 (§8.3): A player may join or leave a standard game as well as a campaign (§18.4), so the count is not fixed at setup.
- lead-E06 (§8.3): Now stated once, for both kinds of game (lead-E05).
- lead-E07 (§6.7, Level 4 Encounters): Points to the campaign rule made by campaign-E16.
- lead-E08 (§2.5): §4.4 and the glossary count an ember card as a treasure card; §2.5 did not.
- lead-E09 (§11.4, Sales): A card that came from outside the decks no longer enters a treasure deck when it is sold, from which it could have been dealt as an ordinary reward.
- lead-E10 (§6.1): The six souls exist to help a lone character through the first encounters, and could not be spent before a rest that costs a spark.
- lead-E11 (§22.1): After the parry ruling (combat-E22) no rule depends on which weapon slot is which, so the question is withdrawn.
- lead-E12 (§22.4): States the consequence of core-E36 where players will look for it.
- lead-E13 (§16.4): Bleed triggered by a character's attack counts for the aggro token (combat-E17), and bleed is not itself an attack.
- lead-E14 (§2.3): Ornstein & Smough and the Four Kings have a health dial for each model (boss-E08, boss-E10, boss-E20).
- lead-E15 (§6.5): The Asylum Demon mini-boss is fought on its expansion's game board (boss-E11); the setup now points to it.
- lead-E16 (§18.1, Section Setup): As lead-E15, for campaign play.
- lead-E17 (§12.2): The invader follows the one heat-up procedure and timing of boss-E01: deck and discard pile reshuffled with the added card at the start of its next turn.
- lead-E18 (§13.2): As lead-E17, for the mimic.
- lead-E19 (§15 (introduction)): Two bosses are fought with more than one model.
- lead-E20 (§8.5, Stagger): A summon rolls dice to attack and to defend, as a character does (§12.1), and has no fixed block, resist, or dodge value for the token to reduce.
- lead-E21 (Glossary, Stagger): Glossary follows §8.5 (lead-E20).
- lead-E22 (§6.1): lead-E10 is withdrawn. Letting a lone character spend before setting out made an exception to the one rule that souls are spent at a rest (§7.6, §11.3, §11.4, and three glossary entries); the author's rule stands as written, and the six souls are spent at the first rest, which leaves the lone character a real choice between resting early and pressing on.

## 6. Every question, by area

The full entry for each row (question, what the book said, evidence from each source, reasoning) is in the area's memo.

### Core loop and economy (chapters 3, 4, 6, 7, 11, appendices)

Memo: `work/phase3/rulings_core.md`. 70 questions.

| Entry | Question | Ruling | Changes play |
|---|---|---|---|
| core-001 | Lead 3 — the component that marks hollowing | CHANGE | no |
| core-002 | Lead 9 — shop stocking, no twelve-draw cap | CONFIRM as written | no |
| core-003 | Lead 10 — shop sales: ember card, Titanite, upgrade service | CONFIRM as written | no |
| core-004 | Lead 12 — luck rerolls only the character's own rolls | CONFIRM as written | no |
| core-005 | Lead 15 — Appendix A: Butcher Knife and the Tier column | CONFIRM as written | no |
| core-006 | Lead 17 — the dropped Firekeeper luck purchase | CONFIRM as written | no |
| core-007 | Lead 19 — Level 4 treasure | CONFIRM as written | no |
| core-008 | Lead 20 — tile layout for the two legs | CHANGE | no |
| core-009 | Review — does the soul economy hang together? | CONFIRM as written | no |
| core-010 | Review — are the shop rules as simple as they can be? | CHANGE | yes |
| core-011 | Review — do embers, estus, luck and the heroic action refresh in parallel? | DELETE | no |
| core-012 | Review — is the first-clear treasure reward stated the same way everywhere? | CHANGE | no |
| core-013 | Ch 03 — parry slot and §3.2 | CONFIRM as written | no |
| core-014 | Ch 03 — the red cube that marks stat tier four | CONFIRM as written | no |
| core-015 | Ch 03 — luck on another character's roll | CONFIRM as written | no |
| core-016 | Ch 03 — does the ember token have a ready side? | CONFIRM as written | no |
| core-017 | Ch 03 — the one mention of "Taunt Level" | CONFIRM as written | no |
| core-018 | Ch 03 — "10 spaces" or "ten-space" | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-019 | Ch 03 — cross-chapter dependencies, and where the ember token starts | CHANGE | no |
| core-020 | Ch 04 — the shield test | CONFIRM as written | no |
| core-021 | Ch 04 — where a consumed ember card goes | ADD | no |
| core-022 | Ch 04 — dependency: §6.3 holds the ember stocking rule | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-023 | Ch 04 — dependency: fixed modifiers in §9.4 and §10.3 | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-024 | Ch 04 — dependency: §11.4 cites §4.2 and §4.4 | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-025 | Ch 04 — a stored spell the character cannot equip | CONFIRM as written | no |
| core-026 | Ch 04 — a spell card that bears the two-handed icon | ADD | no |
| core-027 | Ch 04 — glossary headword "Attack (major action)" | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-028 | Ch 06 — B-023's twelve-draw cap | CONFIRM as written | no |
| core-029 | Ch 06 — when the fog gate goes on the mega-boss game board | CONFIRM as written | no |
| core-030 | Ch 06 — first-leg tile layout | CHANGE | no |
| core-031 | Ch 06 — one character per player | CONFIRM as written | no |
| core-032 | Ch 06 — cross-chapter dependencies | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-033 | Ch 06 — repeated glossary ADD lines | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-034 | Ch 06 — tile side chosen by the party; spare cards to the box | CONFIRM as written | no |
| core-035 | Ch 06 — where a sold boss treasure card goes | CONFIRM as written | no |
| core-036 | Ch 07 — encounter scry: where the replaced card goes | CONFIRM as written | no |
| core-037 | Ch 07 — boss-behaviour scry: is there a deck to look at? | ADD | no |
| core-038 | Ch 07 — enemy turn-order tie-breaks are owned by §7.5 | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-039 | Ch 07 — the scry procedure lives in §7.5 | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-040 | Ch 07 — an ember card held by a character who becomes embered | CONFIRM as written | no |
| core-041 | Ch 07 — sharing out the cards dealt to a tile | CONFIRM as written | no |
| core-042 | Ch 07 — invaders, clearing, and invader treasure | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-043 | Ch 07 — does a Level 4 encounter reset? | CONFIRM as written | no |
| core-044 | Ch 07 — where a revived character stands | CONFIRM as written | no |
| core-045 | Ch 07 — hollow cubes: colour and source | CHANGE | no |
| core-046 | Ch 11 — a sold ember card | CONFIRM as written | no |
| core-047 | Ch 11 — sold boss, legendary and transposed treasure | CONFIRM as written | no |
| core-048 | Ch 11 — Titanite on a sold weapon | CHANGE | yes |
| core-049 | Ch 11 — Andre's upgrade service | CONFIRM as written | no |
| core-050 | Ch 11 — returning to the bonfire without resting | CHANGE | yes |
| core-051 | Ch 11 — the free rest and PvP | CONFIRM as written | no |
| core-052 | Ch 11 — the restock step inside the rest | DELETE | no |
| core-053 | Ch 11 — souls spent outside a rest | CONFIRM as written | no |
| core-054 | Ch 11 — souls cannot be pooled | CONFIRM as written | no |
| core-055 | Ch 11 — resetting a failed boss encounter | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-056 | Ch 11 — invaders and mimics at a reset | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-057 | Ch 11 — D-011, the Firekeeper's luck purchase | CONFIRM as written | no |
| core-058 | Ch 11 — glossary entries Starting equipment and Fog gate | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-059 | Ch 23 — Butcher Knife | CONFIRM as written | no |
| core-060 | Ch 23 — the Tier column and unlisted treasure types | CONFIRM as written | no |
| core-061 | Ch 23 — the grouping of Additional Treasure | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-062 | Ch 23 — Demon Titanite listed without a change | CONFIRM as written | no |
| core-063 | Ch 23 — are Demon Titanite and Blue Titanite "Titanite"? | CHANGE | yes |
| core-064 | Ch 23 — Mon Ring, "one use per floor" | CONFIRM as written | no |
| core-065 | Ch 23 — Chloranthy Ring | CONFIRM as written | no |
| core-066 | Ch 23 — Black Leather Armour and Eastern Armour | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-067 | Ch 23 — printed names | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-068 | Ch 23 — pointers from the chapters to the appendices | ADD | no |
| core-069 | Ch 23 — treasure totals | NOT A RULES QUESTION (informational, nothing to decide) | no |
| core-070 | Ch 23 — A-066, weapons with no stat requirement | CONFIRM as written | no |

### Movement and combat (chapters 5, 8, 9, 10)

Memo: `work/phase3/rulings_combat.md`. 79 questions.

| Entry | Question | Ruling | Changes play |
|---|---|---|---|
| combat-001 | Lead 8 · traps and other models | CONFIRM as written | no |
| combat-002 | Lead 16 · frostbite duration | CONFIRM as written | no |
| combat-003 | Ch 05 · traps and enemies | CONFIRM as written | no |
| combat-004 | Ch 05 · summons, invaders and traps | CONFIRM as written | no |
| combat-005 | Ch 05 · scry count per encounter | CHANGE | yes |
| combat-006 | Ch 05 · scried encounter card destination | CONFIRM as written | no |
| combat-007 | Ch 05 · boss behaviour deck for the scry | CONFIRM as written | no |
| combat-008 | Ch 05 · trap dealing exclusion | CONFIRM as written | no |
| combat-009 | Ch 05 · trap token faces in §2.8 | NOT A RULES QUESTION | no |
| combat-010 | Ch 05 · entry node definition | CHANGE | no |
| combat-011 | Ch 05 · main-boss tile adjacency | CONFIRM as written | no |
| combat-012 | Ch 05 · tile boundary during an encounter | CONFIRM as written | no |
| combat-013 | Ch 05 · overcrowding push in the glossary | CONFIRM as written | no |
| combat-014 | Ch 05 · enemy pathing around terrain | CONFIRM as written | no |
| combat-015 | Ch 05 · chest opening step | CONFIRM as written | no |
| combat-016 | Ch 05 · primary and secondary node icons | ADD | no |
| combat-017 | Ch 08 · frostbite duration | CONFIRM as written | no |
| combat-018 | Ch 08 · conditions on bosses | CONFIRM as written | no |
| combat-019 | Ch 08 · staggered enemy values floor | CONFIRM as written | no |
| combat-020 | Ch 08 · condition damage, embers and aggro | ADD | no |
| combat-021 | Ch 08 · push direction | CONFIRM as written | no |
| combat-022 | Ch 08 · push-move damage ownership | CONFIRM as written | no |
| combat-023 | Ch 08 · repeat icon on enemy data cards | CHANGE | yes |
| combat-024 | Ch 08 · dodge and push | CONFIRM as written | no |
| combat-025 | Ch 08 · summons and push-moves | CONFIRM as written | no |
| combat-026 | Ch 08 · scaling exemptions | CONFIRM as written | no |
| combat-027 | Ch 08 · cross-chapter dependencies | NOT A RULES QUESTION | no |
| combat-028 | Ch 08 · wound token values in §7.5 | CHANGE | no |
| combat-029 | Ch 08 · glossary entry Attack value | CHANGE | no |
| combat-030 | Ch 08 · example values | NOT A RULES QUESTION | no |
| combat-031 | Ch 08 · icon slugs | NOT A RULES QUESTION | no |
| combat-032 | Ch 08 · poison token supply | CONFIRM as written | no |
| combat-033 | Ch 09 · nearest-character tie-break | CONFIRM as written | no |
| combat-034 | Ch 09 · B-002 and B-033 left unapplied | CONFIRM as written | no |
| combat-035 | Ch 09 · parry slot | CHANGE | yes |
| combat-036 | Ch 09 · riposte with a spell | CONFIRM as written | no |
| combat-037 | Ch 09 · push steps in §8.4 and §9.2 | CHANGE | no |
| combat-038 | Ch 09 · push-move damage and scaling | CONFIRM as written | no |
| combat-039 | Ch 09 · repeat icon in §9.3 | CHANGE | yes |
| combat-040 | Ch 09 · stagger citations | NOT A RULES QUESTION | no |
| combat-041 | Ch 09 · fixed defence modifiers | CONFIRM as written | no |
| combat-042 | Ch 09 · failed dodge and armour upgrades | CONFIRM as written | no |
| combat-043 | Ch 09 · dodge and parry with a full bar | CONFIRM as written | no |
| combat-044 | Ch 09 · "do nothing" as a defence | DELETE | no |
| combat-045 | Ch 09 · unreachable target | CONFIRM as written | no |
| combat-046 | Ch 09 · summons as enemy targets | CONFIRM as written | no |
| combat-047 | Ch 09 · hand-offs to the boss chapters | NOT A RULES QUESTION | no |
| combat-048 | Ch 09 · riposte in player versus player | CONFIRM as written | no |
| combat-049 | Ch 09 · icon names | CHANGE | no |
| combat-050 | Ch 09 · where dodge difficulty is defined | NOT A RULES QUESTION | no |
| combat-051 | Ch 09 · glossary lines for push-attack and push-move | NOT A RULES QUESTION | no |
| combat-052 | Ch 09 · named enemies in examples | NOT A RULES QUESTION | no |
| combat-053 | Ch 10 · scaling requirement | CONFIRM as written | no |
| combat-054 | Ch 10 · weapons with no requirement | ADD | yes |
| combat-055 | Ch 10 · tied requirements | CONFIRM as written | no |
| combat-056 | Ch 10 · scaling marker | CONFIRM as written | no |
| combat-057 | Ch 10 · two rerolls on one roll | CONFIRM as written | no |
| combat-058 | Ch 10 · actions resolved in full | CONFIRM as written | no |
| combat-059 | Ch 10 · repeat on attack options | CHANGE | yes |
| combat-060 | Ch 10 · attack with no target | ADD | no |
| combat-061 | Ch 10 · fixed modifiers and the floor | CONFIRM as written | no |
| combat-062 | Ch 10 · what a character may target | CHANGE | no |
| combat-063 | Ch 10 · dependencies already met | NOT A RULES QUESTION | no |
| combat-064 | Ch 10 · dependencies then still open | NOT A RULES QUESTION | no |
| combat-065 | Ch 10 · wound tokens by total value | CONFIRM as written | no |
| combat-066 | Ch 10 · glossary Attack value merge | NOT A RULES QUESTION | no |
| combat-067 | Ch 10 · other glossary entries | NOT A RULES QUESTION | no |
| combat-068 | Ch 10 · italics after action names | NOT A RULES QUESTION | no |
| combat-069 | Ch 10 · example values | NOT A RULES QUESTION | no |
| combat-070 | Ch 10 · catalysts wielded two-handed | ADD | no |
| combat-071 | Ch 10 · forced stamina and overflow | CONFIRM as written | no |
| combat-072 | Conditions · one timing pattern | ADD | no |
| combat-073 | Attacks · one sequence, stated once | CHANGE | no |
| combat-074 | Pushes · displacement and other edge cases | CHANGE | no |
| combat-075 | Range · doorways and joined tiles | CONFIRM as written | no |
| combat-076 | Movement · one definition of a valid node | CHANGE | no |
| combat-077 | Character turn · action economy | CONFIRM as written | no |
| combat-078 | Enemy scaling · by number of characters | CONFIRM as written | no |
| combat-079 | Duplicates · where two rules did one job | NOT A RULES QUESTION | no |

### Bosses (chapters 15, 16, 17)

Memo: `work/phase3/rulings_boss.md`. 71 questions.

| Entry | Question | Ruling | Changes play |
|---|---|---|---|
| boss-001 | lead item 4, nine bosses with placeholders | CHANGE (seven full entries, boss-002 to boss-008); the two Painted World bosses are handled in boss-009 and boss-010. | yes |
| boss-002 | lead item 4, The Four Kings | CHANGE (full entry replaces the placeholder) | yes |
| boss-003 | lead item 4, Gaping Dragon | CHANGE (full entry replaces the placeholder) | yes |
| boss-004 | lead item 4, Guardian Dragon | CHANGE (full entry replaces the placeholder) | yes |
| boss-005 | lead item 4, The Last Giant | CHANGE (full entry replaces the placeholder) | yes |
| boss-006 | lead item 4, Manus, Father of the Abyss | CHANGE (full entry replaces the placeholder) | yes |
| boss-007 | lead item 4, Old Iron King | CHANGE (full entry replaces the placeholder) | yes |
| boss-008 | lead item 4, Vordt of the Boreal Valley | CHANGE (full entry replaces the placeholder) | yes |
| boss-009 | lead item 4, Crossbreed Priscilla | CONFIRM as written (placeholder kept; form only aligned with the other entries) | no |
| boss-010 | lead item 4, Heavy Knight | CHANGE (placeholder replaced by the form §17.7 uses for the Black Knight: replacement cards, no rules beyond the data … | no |
| boss-011 | lead item 4, the shared mega-boss framework | CONFIRM as written (one introductory sentence is added at the head of §17.10, with boss-002) | no |
| boss-012 | lead item 5, Ornstein & Smough | CHANGE: adopt the official structure, and revise Gate 1 OQ-25 for Ornstein & Smough (its Twin Gargoyles half stands). | yes |
| boss-013 | lead item 13, fog gate shortcut | CONFIRM as written | no |
| boss-014 | lead item 13, starting facing | CONFIRM as written, for every boss | no |
| boss-015 | lead item 13, order of character turns | CONFIRM as written | no |
| boss-016 | ch. 15, starting facing (§15.2 step 6) | CONFIRM as written | no |
| boss-017 | ch. 15, fog gate shortcut (§15.1) | CONFIRM as written | no |
| boss-018 | ch. 15, heat-up shuffle and timing (§15.5) | CHANGE: on heat-up the behaviour deck and the discard pile are gathered, one random heat-up card is added, and all are … | yes |
| boss-019 | ch. 15, deck reset between attempts (§15.5, Deck Reset) | CONFIRM as written | no |
| boss-020 | ch. 15, weak arcs on a card with several arc diagrams (§15.6) | CONFIRM as written | no |
| boss-021 | ch. 15, parry of boss attacks (§15.6, Defence) | CONFIRM as written | no |
| boss-022 | ch. 15, push off a boss's node (§15.6, Characters and Arcs) | CONFIRM as written | no |
| boss-023 | ch. 15, dodge on a boss's node (§15.6, Defence) | CONFIRM as written | no |
| boss-024 | ch. 15, boss tiles (§15.3) | CONFIRM as written (the one exception, the Asylum Demon mini-boss fought on its expansion's game board, is made under … | no |
| boss-025 | ch. 15, worked examples use an unnamed boss | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-026 | ch. 15, the sentence after the chapter introduction | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-027 | ch. 15, repeated glossary additions | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-028 | ch. 15, cross-chapter dependencies satisfied by chapter 15 | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-029 | ch. 15, dependencies placed on other chapters | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-030 | ch. 16, order of character turns (§16.1) | CONFIRM as written | no |
| boss-031 | ch. 16, repeat on a behaviour card (§16.1) | CONFIRM as written | no |
| boss-032 | ch. 16, push-move against a wall (§16.2, Push-Moves) | CONFIRM as written | no |
| boss-033 | ch. 16, arc of a character on a node the boss enters (§16.2) | CONFIRM as written | no |
| boss-034 | ch. 16, leap completions (§16.2, Leap) | CONFIRM as written | no |
| boss-035 | ch. 16, icon tokens for pushes (§16.2, §16.3) | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-036 | ch. 16, aggro in boss fights (§16.4) | CONFIRM as written (the one addition, for other enemy models in a boss encounter, is made under boss-059) | no |
| boss-037 | ch. 16, dead characters when a boss is defeated (§16.5) | CONFIRM as written | no |
| boss-038 | ch. 16, the final boss (§16.5) | CONFIRM as written | no |
| boss-039 | ch. 16, boss treasure cards not awarded (§16.5 step 3) | CONFIRM as written | no |
| boss-040 | ch. 16, where the spark and the free rest are stated (§16.5) | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-041 | ch. 16, cross-chapter dependencies satisfied by chapter 16 | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-042 | ch. 16, dependencies placed on other chapters | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-043 | ch. 16, glossary amendments | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-044 | ch. 17, dependency from §2.3 (Ornstein & Smough) | CHANGE (follows boss-012) | yes |
| boss-045 | ch. 17, dependency from §5.3 (one boss model to a node) | CONFIRM as written | no |
| boss-046 | ch. 17, dependency from §5.5 (pillars) | CHANGE (§5.5 aligned with §17.3) | no |
| boss-047 | ch. 17, dependency from §6.7 step 5 (mega-boss special rules) | CHANGE (the seven are now given) | yes |
| boss-048 | ch. 17, dependency from §2.9 (expansion components) | CONFIRM as written (one component name is aligned under boss-007) | no |
| boss-049 | ch. 17, dependency from §20.1 (PvP after the Twin Gargoyles) | CONFIRM as written | no |
| boss-050 | ch. 17, Ornstein & Smough (§17.1, §17.2) | CHANGE (see boss-012) | yes |
| boss-051 | ch. 17, Twin Gargoyles (§17.1) | CONFIRM as written | no |
| boss-052 | ch. 17, Asylum Demon (§17.3) | CHANGE (tile stated; ability renamed) | yes |
| boss-053 | ch. 17, pillar damage (§17.3) | CONFIRM as written | no |
| boss-054 | ch. 17, Wind Up (§17.3) | CONFIRM as written | no |
| boss-055 | ch. 17, Great Grey Wolf Sif (§17.4) | CHANGE (the rule is written out) | yes |
| boss-056 | ch. 17, Artorias (§17.4) | CONFIRM as written | no |
| boss-057 | ch. 17, Old Dragonslayer (§17.6) | ADD (one sentence saying that the data card shows no heat-up point; the entry is otherwise confirmed as written) | no |
| boss-058 | ch. 17, Black Dragon Kalameet (§17.8) | CONFIRM as written | no |
| boss-059 | ch. 17, Executioner's Chariot (§17.9) | ADD for (c): damage to another enemy model in a boss encounter moves the aggro token as damage to the boss does. Points … | yes |
| boss-060 | ch. 17, Raise Skeleton (§17.9, Unique Icons) | CONFIRM as written | no |
| boss-061 | ch. 17, dependency placed on §8.4 (boss pushed by a boss) | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-062 | ch. 17, dependency placed on §8.5 (conditions) | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-063 | ch. 17, dependency placed on §9.4 and §9.5 (attacks that target nodes) | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-064 | ch. 17, dependency placed on §13 (mimics) | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-065 | ch. 17, dependency placed on §15 (facing, tiles, deck, weak arcs) | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-066 | ch. 17, dependency placed on §16 (deck renewal, arcs, area, Boss Death) | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-067 | ch. 17, dependency placed on §19 (campaign sections) | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-068 | ch. 17, dependency placed on Appendix B (replacement boss cards) | NOT A RULES QUESTION (informational, nothing to decide) | no |
| boss-069 | ch. 17, glossary entry Heat-up | CHANGE (follows boss-018) | yes |
| boss-070 | ch. 17, glossary entry Boss | CHANGE | no |
| boss-071 | ch. 17, glossary entry Calamity | CONFIRM as written | no |

### Campaign play and components (chapters 2, 18, 19)

Memo: `work/phase3/rulings_campaign.md`. 46 questions.

| Entry | Question | Ruling | Changes play |
|---|---|---|---|
| campaign-001 | Lead 1: campaign rewards against doubled costs | CONFIRM as written. | no |
| campaign-002 | Lead 11: joining or leaving a standard game | CONFIRM as written, with one clarifying clause. | no |
| campaign-003 | Lead 18: unverified counts and four campaigns | CHANGE. The counts are settled in campaign-006 to campaign-008 and the campaigns in campaign-031, campaign-033 and … | yes |
| campaign-004 | Ch. 02: style checker false positives | NOT A RULES QUESTION. The checker needs a whitelist of printed names. | no |
| campaign-005 | Ch. 02: hollow cubes have no source | CHANGE (clarification). | no |
| campaign-006 | Ch. 02: condition tokens, seven or five | CHANGE. Five of each from the core set, 28 in all, and the supply is not a limit. | no |
| campaign-007 | Ch. 02: counts for unsupplied sets | CHANGE. The generic set is confirmed; four expansion-specific lines are added; The Four Kings' four models and dials … | no |
| campaign-008 | Ch. 02: expansion totals 45/120/63 and 31 | CHANGE. Boss treasure 48 and the total 519, with the invader treasure and Titanite Scale cards named as counted … | no |
| campaign-009 | Ch. 02: Ornstein's printed name | CHANGE to "Dragon Slayer Ornstein" in the four places. "Old Dragonslayer" is unchanged. | no |
| campaign-010 | Ch. 02: cross-chapter dependencies | CONFIRM as written. | no |
| campaign-011 | Ch. 02: glossary entries against Gate 1 | NOT A RULES QUESTION. All four were corrected at integration. | no |
| campaign-012 | Ch. 02: boss treasure cards per boss | CONFIRM "two or more". The total is corrected under campaign-008. | no |
| campaign-013 | Ch. 18: campaign soul reward table | CONFIRM as written. Gate 1 OQ-21 stands; no revision of Gate 1 is proposed. | no |
| campaign-014 | Ch. 18: bonfire ascetic fee | CONFIRM as written. B-034 is not adopted. | no |
| campaign-015 | Ch. 18: spark buy-back | CHANGE. The cost stays at four souls for each character, but the party pays it together, as it pays for the bonfire … | yes |
| campaign-016 | Ch. 18: spark dial range | CHANGE. The maximum is the starting value plus one and never more than five. | yes |
| campaign-017 | Ch. 18: PvP encounters in campaign play | CONFIRM as written. | no |
| campaign-018 | Ch. 18: bosses that do not end a section | CONFIRM as written. | no |
| campaign-019 | Ch. 18: a section completed without a boss | CONFIRM as written. | no |
| campaign-020 | Ch. 18: section setup details | CHANGE. Default: the decks are built from every set the campaign requires, shuffled together by level; a campaign that … | yes |
| campaign-021 | Ch. 18: Level 4 encounters in sections | CHANGE the reward: in campaign play a Level 4 encounter is rewarded as any other encounter of its section (Level 4 … | yes |
| campaign-022 | Ch. 18: victory | CONFIRM as written. Big Game Hunting keeps its own statement (§19.12); Demon Hunting needs none once its bonfire tile … | no |
| campaign-023 | Ch. 18: adding and dropping players | CHANGE the threshold to one spark ("cannot join while the dial shows zero"). Everything else is confirmed, including no … | yes |
| campaign-024 | Ch. 18: a sold legendary card | CONFIRM as written. | no |
| campaign-025 | Ch. 18: when transposition opens | CHANGE the wording only: "once the first section of the campaign is completed". Any rest qualifies, as written. | no |
| campaign-026 | Ch. 18: invaders in campaign play | ADD. Standard invader tokens until the bonfire ascetic is burnt, advanced from then on. | yes |
| campaign-027 | Ch. 18: what the bonfire ascetic does not affect | CONFIRM as written. No marker is needed. | no |
| campaign-028 | Ch. 18: glossary entry Fog gate | CHANGE the glossary line to match §18.2. | no |
| campaign-029 | Ch. 18: campaign heading titles (C-103) | NOT A RULES QUESTION. No change. | no |
| campaign-030 | Ch. 18: the dead after a boss inside a section | CONFIRM as written. | no |
| campaign-031 | Ch. 19: the four unverified campaigns | CHANGE. Into the Depths: Outskirts of Blighttown becomes the Level 4 encounter of Section Four, and the … | yes |
| campaign-032 | Ch. 19: The Gauntlet's invader rule | CHANGE to the campaign's own rule. | yes |
| campaign-033 | Ch. 19: Call of the Abyss | CHANGE. Section Two is confirmed. Section Four: Penultimate Trial is added and The Abyss becomes Section Five. | yes |
| campaign-034 | Ch. 19: Demon Hunting | CHANGE (includes one deletion). The bonfire tile is restored to Section One, the special rest rule is deleted, Section … | yes |
| campaign-035 | Ch. 19: The First Journey, Section Four heading | CHANGE to "Royal Wood". | no |
| campaign-036 | Ch. 19: The Undead Colosseum | CONFIRM as written, with one wording correction. | no |
| campaign-037 | Ch. 19: dependencies on §18.1 | CONFIRM as written (the two changes are carried by campaign-021 and campaign-031). | no |
| campaign-038 | Ch. 19: glossary entry Section | CONFIRM as written. | no |
| campaign-039 | Ch. 19: the mimic of A Hollow Pursuit | CHANGE (clarification): "Each time the party opens the chest", with a pointer to §13.4. | no |
| campaign-040 | Ch. 19: listed invaders and the limits of §12.2 | CONFIRM as written. | no |
| campaign-046 | Re-check against the local booklets | CONFIRM. No earlier edit changes. | no |
| campaign-041 | §19.13 Go Beyond Death | ADD as §19.13. | yes |
| campaign-042 | §19.14 Footsteps of Giants | ADD as §19.14. The redraw rule is written as a filter applied when the Level 2 and Level 3 decks are built. | yes |
| campaign-043 | §19.15 Treasures of the Ice Cave | ADD as §19.15, with four short rules for the paired invaders. | yes |
| campaign-044 | §19.16 Demons and Dragons | ADD as §19.16: four bulleted rules and one table. | yes |
| campaign-045 | The count of campaigns | CHANGE to 16 in the three places. | no |

### Phantoms, mimics, crystal lizards, player versus player, F.A.Q. (chapters 12, 13, 14, 20, 22)

Memo: `work/phase3/rulings_phantom.md`. 68 questions.

| Entry | Question | Ruling | Changes play |
|---|---|---|---|
| phantom-001 | Lead 2 · invader and clearing an encounter | CONFIRM as written. | no |
| phantom-002 | Lead 6 · PvP stalemate rule | CONFIRM as written. | no |
| phantom-003 | Lead 7 · PvP dodge table | CONFIRM as written (values); the table is condensed to three rows. | no |
| phantom-004 | Lead 14 · the mimic's reward | CONFIRM as written. | no |
| phantom-005 | Lead 22 · shortage of blank invader tokens | CONFIRM as written. | no |
| phantom-006 | Chapter 00 · no open items | NOT A RULES QUESTION (informational, nothing to decide) | no |
| phantom-007 | Chapter 01 · no open items | NOT A RULES QUESTION (informational, nothing to decide) | no |
| phantom-008 | Chapter 12 · invader and clearing (duplicate) | CONFIRM as written. | no |
| phantom-009 | Chapter 12 · invasion trigger and eligible cards | CHANGE (the two moments are confirmed; tokens go only to face-down encounter cards that carry no black cube). | yes |
| phantom-010 | Chapter 12 · first setup, step 5 of §6.5 | CONFIRM as written (rule); both steps gain the condition in words. | no |
| phantom-011 | Chapter 12 · souls spent away from the bonfire | CONFIRM as written. | no |
| phantom-012 | Chapter 12 · blank invader tokens (duplicate) | CONFIRM as written. | no |
| phantom-013 | Chapter 12 · summon defence, pushes and conditions | CONFIRM as written. | no |
| phantom-014 | Chapter 12 · summon attacks | CONFIRM as written. | no |
| phantom-015 | Chapter 12 · choice of summon, no tie-break | ADD (if the players cannot agree, the drawn cards are shuffled and one is drawn). | yes |
| phantom-016 | Chapter 12 · invader treasure tie-break wording | CONFIRM as written (rule); the tie-break is stated once, in §7.7, as "when the card is awarded". | no |
| phantom-017 | Chapter 12 · invader as an enemy model | CONFIRM as written. | no |
| phantom-018 | Chapter 12 · cross-chapter dependencies | CONFIRM as written. | no |
| phantom-019 | Chapter 12 · glossary entries owned elsewhere | CONFIRM as written (rules); two glossary entries are corrected to say what the chapters say. | no |
| phantom-020 | Chapter 12 · notes "resolved at integration" | CONFIRM as written. | no |
| phantom-021 | Chapter 12 · the invasion procedure at its shortest (designer's point) | CONFIRM as written (procedure), with two trims. | no |
| phantom-022 | Chapter 12 · summons: cost, timing, limits (designer's point) | ADD (one sentence on what a summon cannot do); cost and timing CONFIRMED. | no |
| phantom-023 | Chapter 12 · what an invader awards, and when it vanishes (designer's point) | CONFIRM as written. | no |
| phantom-024 | Chapter 12 · standard and advanced invaders in campaign play (designer's point) | ADD (in campaign play: standard while the current tier is tier one, advanced once it is tier two). | yes |
| phantom-025 | Chapter 13 · "the mimic's souls" (duplicate) | CONFIRM as written. | no |
| phantom-026 | Chapter 13 · B-035, stamina before the mimic's first turn | CHANGE (each character removes every stamina cube before the mimic's first turn; damage cubes, condition tokens, used … | yes |
| phantom-027 | Chapter 13 · failed mimic encounter and the cleared marker | CONFIRM as written. | no |
| phantom-028 | Chapter 13 · the chest token after the mimic is killed | CHANGE (the chest token goes back on its node, open side up). | yes |
| phantom-029 | Chapter 13 · deferred resolution and §7.5 | CONFIRM as written. | no |
| phantom-030 | Chapter 13 · the closed mimic model as a marker | CONFIRM as written. | no |
| phantom-031 | Chapter 13 · several chests on one tile | CONFIRM as written (no rule added). | no |
| phantom-032 | Chapter 13 · mimic values not restated | NOT A RULES QUESTION (informational, nothing to decide) | no |
| phantom-033 | Chapter 13 · cross-chapter dependencies | CONFIRM as written. | no |
| phantom-034 | Chapter 13 · glossary entry Chest | CONFIRM as written. | no |
| phantom-035 | Chapter 13 · is the chest worth opening? (designer's point) | CONFIRM as written (with the change at phantom-026). | no |
| phantom-036 | Chapter 13 · Hungry and Voracious Mimic in campaign play (designer's point) | ADD (in campaign play: Hungry Mimic while the current tier is tier one, Voracious Mimic once it is tier two). | yes |
| phantom-037 | Chapter 14 · the data card | CONFIRM as written. | no |
| phantom-038 | Chapter 14 · marker for a tile where a crystal lizard was killed | CHANGE (one damage cube is placed on the encounter card). | no |
| phantom-039 | Chapter 14 · supply of Titanite Scale cards | CONFIRM as written. | no |
| phantom-040 | Chapter 14 · who receives the card | CHANGE (the card is awarded to the party). | yes |
| phantom-041 | Chapter 14 · cross-chapter dependencies | CONFIRM as written. | no |
| phantom-042 | Chapter 14 · is the chase worth it? (designer's point) | CONFIRM as written. | no |
| phantom-043 | Chapter 20 · stalemate rule (duplicate) | CONFIRM as written. | no |
| phantom-044 | Chapter 20 · dodge-difficulty table (duplicate) | CONFIRM as written (values). | no |
| phantom-045 | Chapter 20 · characters who died in the boss encounter | CONFIRM as written. | no |
| phantom-046 | Chapter 20 · order of events after a boss | CONFIRM as written. | no |
| phantom-047 | Chapter 20 · choices the standard rules leave to the players | CONFIRM as written. | no |
| phantom-048 | Chapter 20 · heroic actions and card text that name enemies | ADD (in a PvP encounter the word enemy in a heroic action or on a treasure card means another character). | yes |
| phantom-049 | Chapter 20 · luck | CONFIRM as written. | no |
| phantom-050 | Chapter 20 · parry | CONFIRM as written. | no |
| phantom-051 | Chapter 20 · trap tokens | CONFIRM as written. | no |
| phantom-052 | Chapter 20 · corner node | CONFIRM as written. | no |
| phantom-053 | Chapter 20 · victory marker | CHANGE (a spare token of any kind). | no |
| phantom-054 | Chapter 20 · PvP in campaign play | CONFIRM as written; a pointer is added to §20.9. | no |
| phantom-055 | Chapter 20 · threat ties | CONFIRM as written. | no |
| phantom-056 | Chapter 20 · glossary entries owned elsewhere | CONFIRM as written. | no |
| phantom-057 | Chapter 20 · icon slugs | NOT A RULES QUESTION (informational, nothing to decide) | no |
| phantom-058 | Chapter 20 · victory bonuses (designer's point) | CHANGE (kept, but a character holds no more than one victory bonus). | yes |
| phantom-059 | Chapter 20 · the option to decline a defence (designer's point) | DELETE. | no |
| phantom-060 | Chapter 20 · pushes and conditions between characters (designer's point) | CONFIRM as written. | no |
| phantom-061 | Chapter 20 · the chapter as a design (designer's point) | CONFIRM as written, with the cuts at phantom-003, phantom-058 and phantom-059. | no |
| phantom-062 | Chapter 21 · headwords defined in bold but never italicised | NOT A RULES QUESTION (informational, nothing to decide) | no |
| phantom-063 | Chapter 21 · reconciliation of duplicate glossary deltas | NOT A RULES QUESTION (informational, nothing to decide) | no |
| phantom-064 | Chapter 22 · a new player in the standard game | CONFIRM as written. | no |
| phantom-065 | Chapter 22 · the embered reduction and traps | CONFIRM as written. | no |
| phantom-066 | Chapter 22 · ties and choices left to the players | CONFIRM as written. | no |
| phantom-067 | Chapter 22 · the campaign answers | CONFIRM as written. | no |
| phantom-068 | Chapter 22 · every answer against the chapters as they will stand (designer's point) | CHANGE (one answer reworded, one question added; every other answer agrees). | no |

## 7. What could not be settled from the materials

These are facts about printed components, not rules decisions. Each is stated in the book in the safest form the evidence allows.

**Core loop and economy.**

1. A lone character's six starting souls. They sit on the dashboard at setup (§6.1 step 7) but can be spent only during a rest, and the first rest costs one of the five sparks. In the official game the lone player's larger cache is meant to be spent before setting out (Core17 l.632-636: "purchase some treasure and level up your character a bit before facing the dangers that await"). The rules here are definite, so this is not a hole, and no edit is filed. If the author wants the head start to be usable, the clean way is to end the first setup as the two later setups end, with a rest that costs no spark; for a party of two or more that rest does nothing. It would touch §6.4, §7.4, §11.2 and the glossary entry Resting at the bonfire.
2. Printed card names (core-067). "Four-Pronged Plough" is very probably printed "Four-Pronged Plow": the same expansion's enemy is printed "Plow Scarecrow" (§2.2), and Gate 1 OQ-17 keeps printed spellings. It was not changed because the card could not be seen, and `tools/style_check.py` needs the name on its whitelist first. "Sellsword Twinblades" and "Onikiri and Ubadachi" also need a look at the cards.
3. The Butcher Knife's printed requirement, and whether the card is an invader's treasure. Neither could be found. The ruling (24, tier one) rests on the appendix's stated purpose and on a search summary of the video game's value, not on the card.
4. Card facts that would test two rulings: whether any shield card prints an attack option (core-020) and whether any spell card bears the two-handed icon (core-026). Both rulings give a definite answer either way, so play is not held up.
5. The number of doorways on each tile face and the size of the tiles. Core17 shows that tiles differ, but no component list gives the detail. The chain rule (core-008) is safe whatever the tiles are; the claim that the drafted "exactly two doorways" step can be impossible depends on tiles with three or four doorways existing.
6. The treasure types of seven of the ten cards that look like boss treasure in Appendix B (core-061), the 534-card total (core-069), and the dice of the two armour printings (core-066): all need the components.
7. The white-cube shortfall with four characters (core-001). The box holds no fifth colour of cube, so the book must either accept a stated fallback, as proposed, or tell players to supply eight cubes of their own, as it does now. No in-box answer that is both plain and always sufficient was found; the ember-token alternative is described in the entry in case the author prefers it.

**Movement and combat.**

- Printed card values. The examples in §8.2, §8.3, §8.5, §9.4 to §9.6 and §10.3 use values for the Hollow Soldier and the Silver Knight Swordsman, and requirement values for three weapons, that cannot be read from the supplied texts (the data cards are images). They must be checked against the cards at proof (combat-030, combat-052, combat-069). A resist of 4 for the Silver Knight Swordsman in the §10.3 area-of-effect example looks high and deserves the first look.
- Trap token mix. The publisher's backer update gives 11 blank tokens and 9 with values out of 20, but it was seen only as a search summary and not against the components (combat-009).
- Whether any enemy data card in any set prints a repeat icon, and whether any catalyst prints an attack option of its own. Neither could be checked without the cards. Both rulings (combat-023, combat-070) are written so that they are right whichever is true.
- How many encounter cards place two gravestones. This fixes how often combat-005 matters, not whether it is right.
- A shift that is taken away from every target on purpose. Combat-E26 gives it the same outcome as a shift cut short by a trap (the attack ends, the stamina and that weapon's attack are spent). If the lead editor prefers to forbid it, the sentence needs the words "if a trap moved the character" in place of the general condition; the cost is a special case.
- Online discussion was thinner than the brief hoped: the Reddit mirrors refused and no BoardGameGeek thread could be opened, so house-rule evidence rests on the two community rulesets, the community Guide, and search summaries.

**Bosses.**

1. Crossbreed Priscilla's invisibility. Her printed ability (Snowblind) was found, but no source read states when she is invisible or how that ends. The Painted World set has no rulebook text for it in the 2022 rulebook supplied, the publisher's errata file for the 2022 sets sits behind a checkout page, and BoardGameGeek, Reddit and the Fextralife wiki could not be read. Her placeholder stays. The fastest fix is a look at her printed behaviour cards and boss encounter card, or at the replacement cards that Appendix B names.
2. The replacement data cards of Appendix B for Crossbreed Priscilla and the Heavy Knight were not supplied. The printed abilities found (Snowblind, Brutal Impact) are therefore reported in this memo and not written into §17.10, because the replacement cards govern.
3. Ornstein & Smough: the cards were read in a community transcription, not from the printed cards. Four points in boss-012 are designer's calls to be checked against the cards: Ornstein acts first; Ornstein on the main-boss spawn node and Smough on the mini-boss spawn node; the health gain (10 and 15) stops at the starting health; five heat-up cards each.
4. Great Grey Wolf Sif: the threshold of three health comes from the same transcription.
5. Vordt's Icy Blows: "blocks or resists 4 or more damage" is read as four or more damage prevented. The other reading (a defence total of four or more) differs only when the attack value is below four. Frostbreath after a blow that crosses both heat-up points is ruled as resolved once.
6. Old Iron King: the booklet says models "can never move into the Old Iron King's back arc". The entry forbids the back arc of his base and treats the lava as a wall; whether a printed node beside him lies on the line of his back arc could not be judged from the Beam card diagram, and such a node, being printed, is treated as open.
7. Guardian Dragon and Old Iron King node cards were read from two page images; the targeted nodes of each individual card were not, and do not need to be, written into the book.

**Campaign play and components.**

1. The Painted World of Ariamis contents. No copy of its rulebook was found. Its share of the treasure totals (10/30/45/5/5) is the manuscript's totals less every set that was checked, and it agrees with the community guide's count of 95 item cards; its encounter cards (27, nine per level) and its Phalanx models rest on the community guide and on the publisher's count of 18 miniatures. An owner of the set should check four lines: the starting equipment of the Deprived, Mercenary and Sorcerer, the legendary and boss treasure counts, the encounter cards per level, and the Phalanx models.
2. The split of the 2022 encounter cards by level (nine each) comes from the community guide alone; the rulebook gives only the total of 29 with two boss encounter cards.
3. The highest number on the physical spark dial is inferred to be five (the official game never sets it higher, and one community ruleset says it cannot go above five). If the dial shows six, campaign-016 can be withdrawn without other effect.
4. The printed form of Ornstein's name was checked against two rulebooks, not against the card.
5. Superseded by the follow-up below: the four further official campaigns are now drafted as §19.13 to §19.16 (campaign-041 to campaign-045).
6. A catch-up for a character who joins late in a campaign (campaign-023) was not added. If play shows that a late joiner cannot contribute, the simplest form is a soul grant for each completed section, on the model of Big Game Hunting's 16 souls.

**Phantoms, mimics, crystal lizards, player versus player, F.A.Q..**

1. Two chests on one encounter card (phantom-031). The encounter cards were not supplied, so it cannot be checked whether any card places two chests. No rule is added; the sentence to use if one does is given in the entry.
2. Cards not supplied (phantom-014, phantom-037). The summon behaviour cards and the crystal lizard data card could not be read. The rulings rest on the booklets' descriptions and do not depend on printed values, but the author should compare one summon card (dice icons, shift and Distract icons) and the crystal lizard card (threat, health, movement away from the nearest character).
3. A Level 4 encounter card in a campaign section. As §12.2 and §18.1 stand, the Level 4 encounter card dealt at a section's setup is an encounter card and can take an invader token, so an advanced invader can join a Level 4 encounter. Nothing in the sources speaks to it and it was not raised as an issue. It is left for the campaign cluster: either accept it or add "No invader token is placed on a Level 4 encounter card" to §12.2.
4. Online discussion. Reddit and BoardGameGeek threads on these rules could not be reached (see Sources). No ruling above depends on an online source; where the community guide was reachable it is quoted.
