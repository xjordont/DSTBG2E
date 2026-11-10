# Drafting pack — chapter 22 (faq) — manuscript chapter "F.A.Q."

Source text: `work/phase2a/source/22_faq.md` (manuscript.md lines 3098–3101).

## Tracker rows (section · status · notes)

- **(chapter)** · STUB — empty · line 3098. Heading only. Completion required (CMP).
- **(empty heading)** · ORPHAN — delete · line 3100: empty H1 used as page break

## Audit findings mapped to this chapter (4)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### C-030 · italics · Minor · REQUIRED
- Location: Whole body
- Evidence: Inconsistent keyword italicisation (italic/plain in rules text L361-3100): bonfire 39/79; soul 35/33; dodge 27/17; cleared 27/5; spark 25/16; ember 23/10; hollow 19/8; block 17/8; resist 15/6; aggro 14/10; luck 12/4; heroic action 11/5; attack option 10/5; threat 10/14; stamina 8/34; run 12/1; walk 8/0; shift 8/1; parry 7/0; push 2/49; heat-up 2/15; endurance bar 1/16
- Current text: *bonfire* ... the bonfire
- Proposed fix: Adopt one policy (recommended: italicise a glossary keyword at its first use in each H2 section and in headings/tables; plain thereafter) and apply it mechanically from the glossary headword list.
- Rationale: Readers cannot tell which words are defined terms; the Introduction (L381) promises every italicised term is in the glossary.
- Gameplay impact: None
- Decision needed: Y

### C-098 · heading · Minor · REQUIRED
- Location: L893; L983; L1059; L1441; L1842; L1882; L1910; L1925; L1959; L1965; L2049; L2059; L2215; L2308; L2324; L2336; L2400; L3036; L3096; L3100
- Evidence: 20 empty headings ('# ', '## ', '### ') used as page breaks
- Current text: #  (empty)
- Proposed fix: Delete all 20; page breaks belong to layout, not structure.
- Rationale: Empty headings produce blank TOC entries and broken numbering.
- Gameplay impact: None
- Decision needed: N

### C-104 · heading · Minor · CLEAN-UP
- Location: L2350; L1662; L679-2237 (9 headings); L3038; L3098; L1967
- Evidence: '# CAMPAIGNS' (2350) jumps to H3 with no H2; '## Overview' (1662) is generic; '&' in nine headings (679, 895, 1199, 1203, 1710, 1766, 2161, 2201, 2237); '# PLAYER VS PLAYER' (3038) vs 'Target versus Hit' (1483); '# F.A.Q.' (3098); '# SUMMONS' (1967) contains Invaders
- Current text: CAMPAIGNS > ### ; Overview; Tokens & Terrain Elements; PLAYER VS PLAYER; F.A.Q.; SUMMONS
- Proposed fix: Promote campaign headings to H2; 'Enemy Turn Overview'; 'and' for '&' in headings; 'PLAYER VERSUS PLAYER (PvP)'; 'FAQ'; 'PHANTOMS'
- Rationale: Consistent hierarchy and wording.
- Gameplay impact: None
- Decision needed: N

### F-046 · meta-commentary · Note · CLEAN-UP
- Location: L3098 §F.A.Q.
- Evidence: Empty chapter heading 'F.A.Q.'
- Current text: # F.A.Q. (no content)
- Proposed fix: CUT the chapter. If rulings are needed, add them to the relevant section in-voice or as a 'Clarifications' appendix written as rules, not as questions and answers.
- Rationale: A question-and-answer format is a dialogue with the reader and sits outside the lawbook register.
- Gameplay impact: none
- Decision needed: Y

## Completion entries that apply (1) — approved at Gate 1

### [CMP-0003] F.A.Q. (chapter) — Proposed Completion
- Current state: Line 3098 is a bare heading "# F.A.Q." followed by an empty page-break heading (line 3100). No content. STUB.
- Proposed completion (full chapter; each answer applies the manuscript's own rules; where the manuscript is silent the ruling is marked [PROPOSED] and is coordinated with the CMP named):

  > # F.A.Q.
  >
  > **Q.** May a *hollow* character skip previously *cleared* encounters?
  > **A.** Yes, subject to the endurance bar. Skipping costs every character two stamina cubes per encounter skipped. A character may never place a stamina cube when there is no space for it, so a *hollow* character (six spaces) may contribute to skipping at most three encounters and only while their bar is otherwise empty. If any character cannot pay, the characters may not skip that far.
  >
  > **Q.** Who holds the aggro token when its holder dies?
  > **A.** When the character with the aggro token dies, move the token at once to the surviving character with the highest *threat*. Enemy behaviours that target the aggro token target that character from then on. [PROPOSED]
  >
  > **Q.** Does *frostbite* stop the one stamina recovered at the start of a character's turn?
  > **A.** Yes. A frostbitten character recovers no stamina by any means, including the start-of-turn recovery and the *Rest* major action, until the token is removed at the end of their turn.
  >
  > **Q.** May a character *Rest* after *Walking*?
  > **A.** Yes. Only the *Run* minor action prevents *Rest* in the same turn. *Walk*, *Equip*, *Heroic Action* and *Shift* movement do not.
  >
  > **Q.** In a four-character game, does the added *Repeat* apply to push-moves and push-attacks?
  > **A.** No. The scaling *Repeat* is added only to attack icons (crossed swords or white circle). Movement icons, including push-moves that deal damage, are not repeated.
  >
  > **Q.** Does the one-spell-per-turn limit include upgrade spells?
  > **A.** Yes. Attaching an upgrade spell is a main action resolved like casting an attack spell and counts as the character's one spell attack option for the turn.
  >
  > **Q.** May the two-handed reroll be used together with the *luck* token?
  > **A.** Yes. The two-handed reroll rerolls one die; the *luck* token rerolls any or all dice. Each may be used once on the same roll, in either order, and each new result stands.
  >
  > **Q.** Are *Ornstein & Smough* one boss or two?
  > **A.** One boss. They share one data card, one health dial and one behaviour deck, and heat up once. Both models are placed on the main-boss tile and each behaviour card states which model acts. A character attacking either model attacks the boss, and the weak-arc bonus is judged against the model attacked. The boss node limit applies to each model separately. See Boss Special Rules.
  >
  > **Q.** May a character *dodge* into a node containing a barrel?
  > **A.** Yes. The barrel is destroyed and its token removed. A character may not *dodge* into a node containing a gravestone or chest, and a character who has no valid adjacent node may still roll to *dodge* but does not move.
  >
  > **Q.** Who decides ties?
  > **A.** The players decide, collectively. If they cannot agree, the character holding the aggro token decides. Ties in character *threat* are settled this way once at the start of the encounter and the order is kept for the whole encounter.
  >
  > **Q.** Can an invader appear in a boss encounter?
  > **A.** No. Invader tokens are placed only on face-down encounter cards on exploration tiles. Boss tiles never carry an invader token.
  >
  > **Q.** Can a summon and an invader be in the same encounter?
  > **A.** No. Summons are called only at the fog gate for boss encounters; invaders appear only in exploration encounters.
  >
  > **Q.** When does a summon act in a boss encounter?
  > **A.** After the last character in *threat* order has taken their turn and before the boss's next turn. The summon therefore acts once per round, not after each character.
  >
  > **Q.** A chest's ambush card reveals a mimic and every character dies. What happens?
  > **A.** The mimic encounter is *failed*: all *souls* are dropped on the tile, the encounter card is turned face down and the characters must rest at the *bonfire*. The chest stays closed. When the characters next *clear* that tile's encounter, the mimic must be fought again before the chest is opened, until it is killed.
  >
  > **Q.** What is the "reduced *soul* reward" for an encounter *cleared* a second time?
  > **A.** Half the full reward, rounded down. See the Reduced column of the Soul Reward Table and the Campaign Soul Reward Table. [PROPOSED — CMP-0010]
  >
  > **Q.** When may the characters transpose boss treasure in a campaign?
  > **A.** Only while resting at the *bonfire* after spending a *spark*, and only once the final boss of the first section has been defeated. The free rest granted on defeating a section's final boss does not allow transposition.
  >
  > **Q.** May a new player join a game in progress?
  > **A.** In campaign play, yes, at the cost of one *spark*; the new character begins with starting stats and equipment and the maximum number of *sparks* is recalculated. In the basic game a new character joins on the same terms, while the characters are resting at the *bonfire*. [PROPOSED]
  >
  > **Q.** Does *Drink Estus* remove *hollow* markers, condition tokens or stamina cubes?
  > **A.** No. It removes damage cubes only.
  >
  > **Q.** How is *stagger* applied to a roll?
  > **A.** Subtract one from the final total of the attack, block, resist or dodge roll, after the two highest dice are summed and after all rerolls. It is not applied to each die.
  >
  > **Q.** How is a block or resist roll resolved with one die or no dice?
  > **A.** With one die, the defence total is that die's result. With no dice, the defence total is zero and the character suffers the attack's full value.
  >
  > **Q.** May a character with no dodge dice attempt to *dodge*?
  > **A.** Yes. Against dodge difficulty 0 the dodge succeeds automatically for one stamina. Against any higher difficulty the character may pay one stamina and roll nothing (the dodge fails and the character is hit, blocking with armour dice only) or pay three stamina to roll one die.
  >
  > **Q.** After a failed *dodge*, do armour dice modifiers still apply?
  > **A.** Yes. Roll only the armour card's block or resist dice and apply the armour card's own modifiers. Dice and modifiers from weapons, shields and spells are ignored.
  >
  > **Q.** May a character with a two-handed weapon *parry*?
  > **A.** No. A *parry* requires a shield in the left weapon slot; a two-handed weapon occupies both weapon slots. A one-handed weapon wielded two-handed (other slot empty) also prevents a *parry*.
  >
  > **Q.** Which weapon slot is "left" and which is "right"?
  > **A.** The slot printed on the left of the dashboard is the left weapon slot and the slot printed on the right is the right weapon slot. Cards may be moved between them with the *Equip* minor action.
  >
  > **Q.** May an enemy *dodge* or *parry* a *riposte*?
  > **A.** No. Enemies never *dodge* or *parry*. A *riposte* is resolved as a normal character attack against the enemy's block or resist value. Against a boss, the weak-arc bonus applies if the character is in a weak arc.
  >
  > **Q.** Does the *embered* damage reduction apply to *bleed*, *poison* and trap damage?
  > **A.** No. It applies only to damage from a single attack that would deal three or more damage.
  >
  > **Q.** An invader is present and a character dies. Does the encounter continue?
  > **A.** Yes. The invader vanishes at once without reward and the encounter continues against the remaining enemies. The invader does not return.
  >
  > **Q.** After resting at the *bonfire*, may a *cleared* encounter still be skipped?
  > **A.** Yes. Resting resets every encounter (its enemies return), but the black cube marking an encounter *cleared* stays on its card. A reset encounter that was *cleared* may be skipped for two stamina per character or fought again for the reduced *soul* reward. A reset encounter that was *failed*, or never *cleared*, must be fought. See CMP-0019.
  >
  > **Q.** Does a Level 4 encounter reset when the characters rest?
  > **A.** No. Once *cleared*, a Level 4 encounter is not fought again; the mega-boss game board is flipped to its boss side. A *failed* Level 4 encounter resets as any other. [PROPOSED — CMP-0023]
  >
  > **Q.** Do dead and *lost* characters count for enemy scaling?
  > **A.** Yes. Enemy health, movement, attack and *Repeat* scaling use the total number of characters in the game, whether or not they are currently in play.
  >
  > **Q.** May a character pool *souls* with another character?
  > **A.** Only for the *bonfire ascetic*, which is paid communally. Firekeeper upgrades, purchases, phantom summoning and transposition are paid from the acting character's own *souls*.
  >
  > **Q.** Where does a sold boss treasure card go?
  > **A.** To the game box. Boss treasure never enters a treasure deck.
  >
  > **Q.** Do *crystal lizards* prevent an encounter being *cleared*?
  > **A.** No. The encounter is *cleared* when every other enemy model is defeated; surviving *crystal lizards* escape and award nothing.
  >
  > **Q.** Does a character who *dodges* onto a face-down trap token trigger it?
  > **A.** Yes. Any character movement onto the node, including *dodge*, *shift* and pushes, flips the token and resolves it against every model on the node.
  >
  > **Q.** The characters are forced to rest but the *spark* dial shows zero. What happens?
  > **A.** The players lose the game. See Objective & Loss Conditions and CMP-0020. [PROPOSED]
  >
  > **Q.** A character is pushed off a boss's node by a boss attack. Must they stay in the same arc?
  > **A.** Yes. A character pushed off a boss's node moves to the centre-most valid node in the arc they occupied, or to any valid node in that arc, or, if the arc holds no valid node because of a wall, to any adjacent node touching that wall.
  >
  > **Q.** May a *heroic action* be used during another model's turn?
  > **A.** Only if the dashboard says so. Otherwise it is a minor action taken during the character's own turn.

- Design rationale: Each question is one the body leaves open or answers in two places. Answers restate the governing rule and name the chapter so the F.A.Q. never carries a rule of its own; the four rulings the body does not reach (aggro on death, basic-game joining, Level 4 reset, zero-spark forced rest) are tagged and routed to their CMP. The official FAQ's rulings on dodge-with-zero-dice and failed-dodge pushes are compatible with the manuscript and are reflected; its ruling that a push from a boss attack ignores arcs conflicts with the manuscript's Character Arc Movement text and is not adopted. The O&S answer is limited to what the Core rulebook supports (one data card, one dial, one deck).
- Mechanical impact: None beyond the tagged rulings; those are resolved in CMP-0006, CMP-0010, CMP-0019, CMP-0020 and CMP-0023.
- Follow-on changes required: Delete the empty heading at line 3100. Cross-reference section numbers at layout. If any tagged CMP is rejected, delete or amend the corresponding answer.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

