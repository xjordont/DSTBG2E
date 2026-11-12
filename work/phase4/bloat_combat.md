# Bloat audit — combat group (chapters 08, 09, 10, 11, 20)

Baseline: the author's source chapters in `work/phase2a/source/`. On trial: the final chapters `10_manuscript_chapter_NN_*.md`. Word figures are counted (`len(text.split())`, HTML tags stripped from the source tables). "Words it needs" is my estimate of the section written at the author's density, keeping every rule the game cannot be played without and every change the author approved at Gate 1.

Changes the author approved at Gate 1 (OQ-07 scaling table, OQ-13 poison, OQ-16 stagger timing, OQ-24 calamity) are treated as the author's rules and judged for wordiness only.

---

## Chapter 08 — Combat Basics

### Section table

| § | source words | final words | words it needs | main excess |
|---|---|---|---|---|
| 8 intro | 0 | 62 | 0 | flavour paragraph with no rule (CH-08-001 says so itself) |
| 8.1 Target versus Hit | 129 | 325 | 110 | R: the hit rule is stated four times in five paragraphs; 11 cross-references; one example |
| 8.2 Enemy Data Cards | 266 | 604 | 220 | R + X: a seven-bullet icon legend that §9.2 and §9.3 own; 22 cross-references |
| 8.3 Enemy Scaling | 149 | 402 | 120 | R + E: three paragraphs repeat the table; a 112-word example repeats it again |
| 8.4 Pushing | 353 | 1,077 | 380 | E + A + R: three examples (278 words); a list of every cause of a push; terrain rules restated |
| 8.5 Conditions | 340 | 1,183 | 430 | E + V + A: four examples (309 words); general paragraphs that pre-state each condition; summon and aggro riders |
| **Chapter** | **1,240** | **3,653** | **1,260** | 72 cross-references; 10 examples (846 words) against none in the source |

### Added rules

- §8.1 · List of what a character may target (enemies, bosses, invaders, mimics, crystal lizards) · combat-E11 (CH-08-043) · **A3** · delete; "a character targets enemies" is enough, and the list was added only to make §8.1 agree with a second list in §10.3.
- §8.2 · Legend of seven satellite icons, the physical/magical icon, and pointers to boss, phantom and mimic cards · CH-08-008, CH-08-009 (A-023, D-008) · **A3 here** · delete; each icon is resolved in §9.2 or §9.3. A labelled picture of one card does this job.
- §8.2 · "Wound tokens stay on the model until the enemy is killed or the encounter ends"; "Damage beyond the enemy's scaled health has no further effect" · CH-08-011 · **A3** · delete both.
- §8.3 · The character count "changes only when a player joins or leaves"; each enemy "is scaled when its model is placed" · lead-E05, lead-E06 (CH-08-050, -051), CH-08-015 · **A2** · keep "dead characters still count" (the author's rule); leave joining and leaving to §18.4.
- §8.3 · Exemption widened from bosses to bosses, mimics, phantoms and crystal lizards · CH-08-017 (A-028, A-029) · **A1** · keep as the one sentence it is; drop the four cross-references.
- §8.3 · A push-move scales as movement; its damage value scales as an attack value · CH-08-016 (A-025) · **A2** · one clause in the table's footnote.
- §8.4 · Five-item list of every cause of a push (push-attack, push-move, node model limit, boss onto boss, boss rules such as a leap) · CH-08-020, then patched by combat-E13, combat-E14 (CH-08-045, -046) · **A3** · delete. The list had to be corrected twice because it was incomplete; a rule that says "an effect that pushes a model…" needs no list.
- §8.4 · What a pushed model does on meeting a gravestone, chest, pillar, barrel, trap or full node · CH-08-021 (A-085) · **A2** · one sentence: a pushed model enters a node as though it had moved there.
- §8.4 · Fallback direction: "farther" defined by range; choice among adjacent nodes farther than the model's own; no farther node, no push · CH-08-022 (A-085) · **A1 in substance, A2 as written** · the source covered only the corner. Two sentences (see worst passage 2).
- §8.4 · A push-move's damage value is a physical attack, blocked or dodged, never parried; characters on the enemy's starting node are pushed but not attacked · CH-08-024 (A-023, D-016), combat-E15 (CH-08-047) · **A1, but stated five times** (§8.4 steps, §8.4 paragraph, §9.2 twice, §9.6) · state once in §8.4.
- §8.4 · A boss is also pushed by a boss "placed on" its node (the Four Kings) · VB-006 (CH-08-053) · **A3 here** · it belongs to §17.10 alone.
- §8.5 · "Next complete turn": a stagger or frostbite token placed during a model's own turn lasts to the end of its following turn · Gate 1 OQ-16 (CH-08-029, -035, -037) · **A1, A2 as worded** · the author approved the fix; it is explained in the general paragraph, under Frostbite, under Stagger and in an example. One sentence serves.
- §8.5 · Bleed damage counts towards the aggro token for the character who triggered it; poison damage counts for nobody · combat-E17 (CH-08-049; "No source addresses it") · **A3** · delete. Nobody asks; the source counts "damage tokens placed" and the table can do the same.
- §8.5 · Summons: stagger reduces a summon's rolls; frostbite reduces its shift icons · lead-E20 (CH-08-052), VA-024a (CH-08-056) · **A3 in this chapter** · a rule for an optional expansion model inside the core definition of two conditions. If wanted, one sentence in §12.1.
- §8.5 · Condition damage "is recorded as any other damage" (cubes, wound tokens, dial); "any model may hold condition tokens"; "some rules place a condition token without an attack; the token then has the same effect"; a second token of a condition "is not placed and has no effect" · CH-08-030, CH-08-031 (F-112, B-038, A-009) · **A3** · delete all four. Keep only "a value cannot be reduced below zero".

### Worst passages

**1. §8.1, the hit (about 150 words, plus a 69-word example)**

Final:
> **Hit.** An attack hits its target when the target is within the attack's *range* (see §5.4) and does not avoid the attack by a successful *dodge* (see §9.5) or a successful *parry* (see §9.6).
> A hit does not depend on damage. An attack whose damage is reduced to zero by *block* or *resist* still *hits* its target (see §9.4; §10.3).
> A target that is out of range, or that dodges or parries the attack, is not hit. An attack has no effect on a target it does not hit: it deals no damage, does not *push* the target, and places no *condition* token on it.
> A push (see §8.4) and a condition (see §8.5) carried by an attack apply only to a model that the attack hits. They apply to every model the attack hits, whether or not the attack dealt damage to it.
> *Example.* An enemy attack with an *attack value* of 4 bears the node icon and the push icon … The Herald dodges successfully, is not hit, and is not pushed.

Source (64 words):
> A model is considered hit by an attack even if the attack deals zero damage so long as the attack was in range and the target model did not successfully dodge the attack. Therefore, targets who successfully *dodge* an attack are not considered hit and therefore are not pushed or afflicted with conditions…

Cut version (47 words):
> An attack hits its target unless the target is out of range or dodges or parries the attack. A hit does not depend on damage: an attack blocked to zero still hits. Only a model that is hit is pushed or receives a condition token.

**2. §8.4, where a push-attack sends its target (about 210 words with the two examples that explain it)**

Final:
> A push-attack pushes the model directly away from the attacker. A node is farther from the attacker when its *range* from the attacker's node is greater (see §5.4). The model is pushed into the valid node most directly opposite the attacker's node, chosen from the adjacent nodes that are farther from the attacker than the model's own node. If two or more such nodes are equally opposite the attacker, the players choose one of them.
> If no valid node is farther from the attacker than the model's own node, the model is not pushed. If the attacker shares the model's node, every adjacent node is farther from the attacker, and the players choose any valid node.

Source (about 70 words):
> The pushed model(s) must move to the adjacent node most directly opposite of the attacking model. If there are multiple adjacent nodes equally opposite to the attacking model the players choose the node. A model being pushed directly into a corner remains on the corner node. If the attacker is on the same node as the model hit by the push attack, the players choose any adjacent node…

Cut version (62 words):
> A model hit by a push-attack is pushed one node directly away from the attacker. If that node cannot be entered, or two nodes are equally far from the attacker, the players choose among the adjacent nodes that are farther from the attacker. If there is none, the model stays where it is. If the attacker shares the model's node, the players choose any adjacent node.

**3. §8.5, the three general paragraphs before the conditions (about 240 words)**

Final:
> A model holds at most one token of each condition, and it may hold tokens of different conditions at the same time. When a token of a condition is to be placed on a model that already holds a token of that condition, the token is not placed and has no effect. Bleed and poison are exceptions, each stated under its own heading below.
> Damage dealt by a condition is recorded as any other damage is: with *damage cubes* for a character (see §3.4), with *wound tokens* for an enemy (see §8.2), and on the *health dial* for a boss, a phantom, or a *mimic* (see §15.4). A value reduced by a condition cannot fall below zero. When the *aggro token* is assigned, bleed damage counts as damage inflicted by the character whose attack triggered it, and poison damage counts for no character…
> Each condition lasts until the rule under its heading removes it. The end of the affected model's own *turn* is the only moment at which a turn acts on a condition: poison is then resolved, and frostbite and stagger tokens are then removed. Where a token is removed at the end of a model's next complete turn, a token placed during that model's own turn is not removed at the end of that turn; it is removed at the end of the model's following turn. Every condition token still in play is removed when the *encounter* ends…

Source (24 words, with a one-line limit under each condition):
> When an attack has a condition icon, place the corresponding condition token on the model(s) hit by that attack.

Cut version (58 words):
> When an attack with a condition icon hits a model, place the matching token on it. A model holds one token of each condition, except poison. Condition damage is not reduced by block or resist, and a condition never reduces a value below zero. A token placed during a model's own turn is not removed at the end of that turn. All condition tokens are removed when the encounter ends.

With that paragraph in place each condition is two or three of the author's bullets, as in the source, and the four examples (bleed 95 words, poison 45, frostbite 60, stagger 80) can go; only the stagger-from-parry timing is hard, and the sentence above covers it.

### Unintuitive or over-engineered rules

- **"Next complete turn."** A coined term the reader must decode before reading Frostbite and Stagger. Put the plain sentence in its place: "A token placed during a model's own turn is not removed at the end of that turn." Nothing is lost.
- **A push-move with a damage value hits the same character once for every node.** §9.2 rules that a character pushed along the enemy's path "is attacked again on that node", and its example has the Assassin attacked twice by one icon. With two or more characters every 1-node push-move becomes two nodes, so this happens constantly. A player expects one icon to hurt once. Simpler rule: "A character suffers a push-move's damage once, the first time the enemy enters their node." What is lost: the literal reading of "repeated for each node moved"; what is gained is that the awkward VA-023 example ("its path turns at that node, so the second node it enters is not the node to which the Knight was pushed") is no longer needed.
- **Two push directions in one procedure.** Step 1 of a push-move pushes characters "to a valid node chosen by the players"; step 4 pushes them "directly away from the node the enemy has left, as for a push-attack made from that node". This is the author's rule and stays, but it reads far more easily as two sentences than as four numbered steps plus three explanatory paragraphs.
- **Bleed and poison bookkeeping for the aggro token** (combat-E17). A ruling for a question no table asks. Delete.
- **Frostbite on a summon reduces "the number of nodes of each shift icon on its behaviour cards".** A reader of the core conditions meets a term (shift) from an optional expansion. Move to §12.1 or delete.
- **§8.2 defines the repeat icon as modifying "no single icon"** in a list headed "Smaller icons printed around a behaviour icon modify it". The legend contradicts its own heading; it is the product of two successive rulings (CH-08-042, then combat-E12). Delete the legend; §9.1 states the rule.

---

## Chapter 09 — Enemy Turn

### Section table

The source has three sections; its defences are sub-headings of Enemy Attacks, counted separately here.

| § | source words | final words | words it needs | main excess |
|---|---|---|---|---|
| 9 intro | 0 | 53 | 0 | flavour paragraph with no rule |
| 9.1 Overview | 200 (of which 105 is the turn-order tie-break, now in §7.5) | 293 | 90 | X + R: two closing paragraphs (100 words) are nothing but pointers to §8.1, §8.3, §8.5, §12, §13, §16 |
| 9.2 Enemy Movement | 462 | 1,149 | 380 | E + R + A: three examples (290 words); four sub-sections that now say the same sentence; push-move restated from §8.4; a path-finding sub-section |
| 9.3 Enemy Attacks | 151 | 874 | 250 | A + R: a seven-step attack sequence that the three defence procedures then point back to; icon list repeated from §8.2; two examples |
| 9.4 Block and Resist | 162 | 502 | 170 | D + E: edge cases (no dice, one die, negative total, back-up slot, stored spell); a paragraph explaining where the procedure ends; two examples |
| 9.5 Dodge | 218 | 805 | 260 | D + R: stamina-space paragraph, "not a move" paragraph, a Traps sub-section owned by §5.5, two examples |
| 9.6 Parry and Riposte | 190 | 868 | 300 | A + D: the riposte grew from one sentence (30 words) to four paragraphs (230 words); two examples (207 words) |
| **Chapter** | **1,386** | **4,544** | **1,450** | 86 cross-references (218 words inside the brackets alone); 11 examples (945 words) against none in the source |

### Added rules

- §9.1 · A repeat icon on a data card repeats the enemy's whole row of icons, re-targeting each time · combat-E12, combat-E18, combat-E19 (CH-08-044, CH-09-039, -040), replacing CH-09-018, which said the opposite · **A1** · one sentence, stated once (it now appears in §8.2, §9.1 and §9.3).
- §9.1 · "The enemy's turn ends … when the enemy is killed" · CH-09-004 (A-119) · **A3** · delete; a removed model does nothing.
- §9.2 · "Nearest character" as a defined term: living character at shortest range; tie to aggro holder, then highest threat, then players' choice · CH-09-008 (D-008, A-023) · **A1** · the author's tie-break, said once instead of twice. Keep; it is shorter than the source.
- §9.2 Paths · Shortest path of valid nodes around terrain; stop on the target's node; no path, no move; away-movement tested node by node; "the rest of its movement is lost" · CH-09-009, CH-09-010 (A-082) · **A1 in substance, A2 as written** (210 words) · two sentences: "An enemy moves by the shortest route of nodes it can enter. If it cannot get closer (or farther), it stops."
- §9.2 Paths · An enemy never leaves the tile or passes a doorway; displaces at the node model limit; neither triggers nor suffers traps · CH-09-012 · **A3 here** · all three are owned by §5.2, §5.3, §5.5.
- §9.2 · A push-move pushes characters only; an enemy model on the node entered stays · CH-09-014 · **A3** · the source says "pushes characters out of its way".
- §9.2 · A push-move's damage value is a physical attack against every character on each node entered; a character pushed along the path "is attacked again on that node" · CH-09-015 (A-023, D-016) · **A4** for the repeat hit · see Unintuitive rules.
- §9.3 · Out-of-range target: "the attack misses … No other character is attacked in the target's place" · CH-09-016 (A-023, D-008) · **A1** · keep, one sentence.
- §9.3 · Node attack as a defined term; each character defends separately against the full value · CH-09-016 · **A1** · the source promised "special rules detailed later" and never gave them. Keep, two sentences.
- §9.3 · Seven-step Attack Sequence, with "a character who dies in step 5 is not pushed and receives no token" · combat-E20 (CH-09-041), then RV-001 to RV-004 (CH-09-048 to -051) · **A2** · one sentence: "After the defence, place the damage, then resolve any push, then place any condition token." The four RV patches exist only because the sequence and the three defence procedures each claimed the same steps.
- §9.3 · The defence is chosen before any dice are rolled and cannot be changed · CH-09-019 (F-071) · **A1** · keep, one sentence.
- §9.4 · A fixed modifier on block or resist dice is added after the two highest dice, "whether or not a die of its card is among the two highest" · CH-09-022 (D-033, A-120) · **A1 / A2** · keep the first half as a clause in step 4.
- §9.4 · One die: its result is the sum; no dice: zero; a total below zero is zero; back-up slot, inventory and a stored spell give no dice · CH-09-021, CH-09-023, CH-09-024 · **A3** · delete all; "equipped cards" already excludes the back-up slot.
- §9.5 · A dodge needs an empty space for its stamina cube; a character with no dodge dice may still attempt one · CH-09-026 · **A3** · the stamina rule is §3.4's; delete.
- §9.5 · Dodge movement: must be a valid node; none, stay; "not a move"; destroys a barrel; reveals a trap; displaces at the node limit · CH-09-027 (A-087) · **A2** · "The character then moves to an adjacent node of the player's choice, if one can be entered."
- §9.5 · Failed dodge: upgrade cards attached to the armour count; no armour, full damage; stamina not returned · CH-09-028 · **A3** · delete the last two; the first is one clause.
- §9.5 Traps · A trap is dodged under this section; trap damage cannot be blocked · CH-09-029 · **A3 here** · §5.5 owns it; delete the sub-section.
- §9.6 · A shield in either weapon slot permits a parry; the riposte uses "the other weapon slot, the slot that does not hold the shield used for the parry" · combat-E22 to combat-E25 (CH-09-043 to -046), reversing CH-09-031 and the author's "shield as their left weapon … weapon equipped to the right weapon slot" · **A4 as worded** · either restore the author's left/right rule or say "a shield equipped" and "the character's other weapon". The generalisation needed four rulings and then VA-025a.
- §9.6 · "A character who wields a weapon other than a shield two-handed has no shield equipped and cannot parry" · VA-025a (CH-09-047), VA-025b in §10.4 · **A3** · a tautology produced by the either-slot ruling. Delete in both places.
- §9.6 · A spell cannot be used for a riposte, "whether equipped in that slot or stored in a catalyst there" · combat-E24 (CH-09-045) · **A3** · "weapon" already says it.
- §9.6 · Riposte riders: the stagger token is in place first; an enemy cannot dodge or parry a riposte; it is not the Attack major action; it is optional and cannot be made without a weapon, the stamina, or a legal option (the shaft case); a kill ends the attacker's turn; PvP pointer · CH-09-034 (A-119, A-078) · **A2** · keep "the riposte is extra and does not use the character's Attack"; delete the rest.
- §9.6 · A parry needs an empty space for its cube; "no further die may be added"; the push-move attack named as unparryable · CH-09-032, CH-09-033 · **A2** · "A parry is rolled as a dodge, without the extra die."

### Worst passages

**1. §9.6, Riposte (four paragraphs, about 230 words)**

Final:
> A riposte is one attack against the attacker, made with one *attack option* of the *weapon* equipped in the character's other weapon slot, the slot that does not hold the shield used for the parry. A *spell* cannot be used for a riposte, whether it is equipped in that slot or stored in a *catalyst* there (see §4.3). The character pays the stamina cost of the attack option and resolves the attack as §10.3 describes. The attacker's stagger token is in place before the riposte is resolved. An enemy cannot dodge or parry a riposte.
> A riposte is made during the attacker's *turn*. It is not the character's *Attack* major action, and it does not count against the attacks the character makes in their own turn (see §10.3). In every other respect a riposte is an attack: the character may flip the luck token to reroll its dice, and the icons of the attack option apply. A riposte against a character in a PvP encounter is defended as §20.4 describes.
> A riposte is optional. No riposte is made if the other weapon slot holds no weapon with an attack option, if the character cannot pay the stamina cost, or if no attack option of that weapon may target the character's own node, as with the *shaft* icon (see §10.3, Shaft). The parry succeeds all the same, and the attacker is staggered.
> If the riposte kills the attacker, the attacker's turn ends at once, and its remaining icons are not resolved (see §9.1).

Source (30 words):
> The character may make one *riposte* attack out of turn against the attacker using any *attack option* on the weapon equipped to the right weapon slot after paying the associated stamina cost.

Cut version (43 words):
> The character may then riposte: one attack against the staggered attacker with any attack option of the character's other weapon, at its usual stamina cost. A riposte is extra. It does not use the character's Attack action or that weapon's attack for the turn.

**2. §9.3 Attack Sequence and the hand-backs in §9.4, §9.5 and §9.6 (about 330 words in four places)**

Final (§9.3):
> 4. Resolve the defence, which fixes how much of the damage it prevents (see §9.4; §9.5; §9.6). If a dodge or a parry succeeds, the character is not hit, and the attack on that character ends. 5. Place the damage that the defence has not prevented (see §3.4). 6. If the attack is a push-attack, push the character (see §8.4). 7. Place any condition token the attack carries (see §8.5).
> Steps 6 and 7 are resolved even if the character suffered no damage. A character who dies in step 5 is not pushed and receives no token. A node attack resolves steps 3 to 7 for one character at a time… The attack of a push-move with a damage value follows the same steps from step 3 (see §8.4).

Final (§9.4):
> The procedure ends with step 6. The damage is placed, and any *push* and any *condition* token the attack carries are resolved, in steps 5 to 7 of the attack sequence, which follow whether or not the character suffered damage (see §9.3, Attack Sequence).

Final (§9.6, Failed Parry):
> When a parry fails, the character is hit and no block or resist dice are rolled: the defence prevents nothing, and the damage placed in step 5 of the attack sequence equals the full *attack value* (see §9.3, Attack Sequence). Any condition token the attack carries is placed in step 7 of that sequence (see §8.5).

Source (in the block procedure):
> 5. Determine damage to the defending character… 6. Place any condition tokens indicated, even if no damage was dealt. 7. Resolve any push effects.
> (failed parry) The character takes full damage without the option to block/resist. Place a *stagger* token on the defending character's dashboard.

Cut version (§9.3, 46 words, with no sequence and no hand-backs):
> The targeted character chooses one defence before rolling: block or resist, dodge, or parry. Unless the dodge or parry succeeds, the character is hit: place the damage the defence did not prevent, then resolve the attack's push, then place its condition token, even if no damage was dealt.

Cut version (failed parry, 22 words):
> If the parry fails, the character is hit for the full attack value, rolls no block or resist dice, and is staggered.

**3. §9.2, Paths and the four direction sub-sections (about 330 words before the examples)**

Final:
> When the icon moves the enemy towards its target, the enemy follows the shortest path of valid nodes from its own node to the target's node. It stops when it has moved the number of nodes shown or when it stands on the target's node. If two or more such paths are equally short, the players choose which path the enemy follows. If the enemy already stands on the target's node, or if no path of valid nodes leads to that node, the enemy does not move.
> When the icon moves the enemy away from its target, each node the enemy enters must be a valid node at a greater range from the target than the node it leaves. If two or more such nodes are open to the enemy, the players choose which node it enters. If no such node is open to the enemy, it stops, and the rest of its movement is lost. …
> ### Towards Aggro
> The enemy moves the number of nodes shown towards the character who holds the aggro token. An enemy on that character's node does not move.
> ### Away from Aggro … ### Towards Nearest … ### Away from Nearest … (the same two sentences three more times)

Source (three sentences, 68 words):
> If an enemy movement icon instructs an enemy to move towards a character it already shares a node with, then it simply does not move. If an enemy movement icon instructs an enemy to move away from a character that is already at maximum distance, then it simply does not move. When two different nodes would take an enemy closer to where it is trying to go, the players can choose which node the enemy enters.

Cut version (73 words, no sub-sections):
> An enemy moves one node at a time, towards its target by the shortest route it can take, or away from it to a node that is farther from the target. Where two nodes serve equally, the players choose. An enemy that reaches its target's node, or that has no node to move to, stops. The skull icon makes the target the character with the aggro token; the ring icon makes it the nearest character.

### Unintuitive or over-engineered rules

- **Procedures that call each other by step number.** To block an attack a player now holds §9.3's seven steps and §9.4's six, and is told "the procedure ends with step 6 … steps 5 to 7 of the attack sequence … follow". A failed dodge "is resolved from step 2 of the block and resist procedure" and "then continues with its steps 5 to 7". The source's defence lists simply ended with "place any condition tokens … resolve any push effects". Put that one sentence in §9.3 and delete every step-number reference. Nothing is lost.
- **A push-move with a damage value attacks the same character again on each node** (§9.2, last paragraph and example). One icon, two attacks, two defences. Replace with "once per push-move". Lost: nothing a player would miss.
- **Which slot holds the shield.** The author's rule (shield left, riposte with the right-hand weapon) is concrete. The final's "one of the weapon slots … the other weapon slot, the slot that does not hold the shield used for the parry", with the rider about wielding "a weapon other than a shield two-handed", is harder to read than either the author's rule or the plain "a shield" and "the other weapon".
- **The riposte's list of reasons it cannot be made** (no weapon, no stamina, shaft icon). These are the ordinary conditions of any attack. Delete.
- **Dodge step order.** Step 3 sells the extra die before step 4 says that a difficulty of zero needs no roll. Put the zero case first, as the source does ("the character does not need to roll dice").
- **"A push-move pushes characters only. An enemy model on a node the enemy enters stays there, unless the node model limit displaces it."** A sentence that sets up a rule and then its exception about a case the source never raises. Delete.
- **§9.1's last two paragraphs** list everything the chapter is not about (scaling, conditions, invaders, summons, bosses, mimics). A new player reads five cross-references before the first rule of movement. Delete both.

---

## Chapter 10 — Character Turn

### Section table

| § | source words | final words | words it needs | main excess |
|---|---|---|---|---|
| 10 intro | 0 | 63 | 0 | flavour paragraph with no rule |
| 10.1 Turn Order | 141 | 848 | 260 | R + E: two opening paragraphs of pointers (§7.5, §12, §16, §20); four closing paragraphs restating §3.2, §3.4 and the bullets above them; three examples (171 words) |
| 10.2 Character Movement | 271 | 314 | 80 | R: Walk and Run defined a second time (first in §10.1), terrain from §5.5, tile edge from §5.2; the source section was itself the author's wordiest |
| 10.3 Character Attacks | 514 | 1,831 | 620 | E + V + R: six examples (483 words); a 12-step procedure followed by six paragraphs re-explaining its steps; 36 cross-references; Range grew from 30 words to 200 |
| 10.4 Two-Handed Attacks | 57 | 328 | 80 | D + A + E: spell, catalyst and parry riders; an 89-word example of a one-die reroll |
| 10.5 Stat Scaling | 107 | 329 | 90 | E + G: three examples (158 words) for a +1 rule; a coined term, "relevant stat" |
| **Chapter** | **1,094** | **3,713** | **1,130** | 78 cross-references; 14 examples (950 words) against none in the source |

Gate 1 changes treated as the author's: free order of minor and major actions and once-per-turn limits (OQ-26), ember from the back-up slot (OQ-30), scaling threshold of five (OQ-19).

### Added rules

- §10.1 · Step 3 of the turn, "Resolve every condition that takes effect at the end of the character's turn" · CH-10-003, combat-E16 · **A1** · keep; it is the author's poison rule given a place in the turn.
- §10.1 · "Each action is resolved in full before another is begun … cannot take a minor action in the middle of an attack" · CH-10-014 (A-073, D-017) · **A2** · one clause on the Attack bullet: "both attacks are made together".
- §10.1 · A character who has rested cannot run for the rest of the turn · CH-10-010 (A-011) · **A1** · keep; closes a real loophole in six words.
- §10.1 · Frostbite stated at step 1 and again at Rest; "Rest removes stamina cubes only. Damage cubes, hollow cubes, and condition tokens stay" · CH-10-006, CH-10-010 · **A3** · §8.5 owns frostbite; the Rest sentence pre-empts a question nobody asks.
- §10.1 · Stamina cannot be spent beyond the empty spaces; an obliged cube with no space staggers the character · CH-10-013 ("preserve list; dependency from §3.4") · **A3 here** · §3.4 owns it. Delete the paragraph and its example.
- §10.1 · Equip: "each card must go to a slot that accepts it, and the character must meet its stat requirements"; "the only way to change equipped cards during an encounter" · CH-10-007 · **A3 here** · §3.2 and §4.1 own it.
- §10.3 · "In this section the word enemy covers all of these" (bosses, invaders, mimics, crystal lizards) · CH-10-021, combat-E11 · **A4** · a local redefinition of a core word. Delete the list and the redefinition.
- §10.3 · The two-handed reroll and the luck reroll as separate steps, in either order, both allowed on one roll · CH-10-023 (C-060, "see issues") · **A2** · one step: "Reroll as the luck token or a two-handed weapon allows."
- §10.3 · A fixed modifier is applied once to the total after rerolls, not to each die; an attack value below zero counts as zero · CH-10-022 (D-033, A-120) · **A2** · the first is a clause in the attack-value step; delete the second.
- §10.3 · Granted attacks (a riposte) follow the same steps and do not count towards the limit · CH-10-026 (A-119) · **A3 here** · §9.6 says it.
- §10.3 Range · Range is a maximum and includes the attacker's own node; it is checked after a shift; an attack cannot begin unless a target is in range or a shift could bring one in range; otherwise it "ends without a roll, and the stamina paid is not returned" · CH-10-028, combat-E26 (CH-10-042) · **A2** · "If no target is in range when the target is chosen, the attack is lost." The clause about a shift "able to bring one within range" asks the player to prove reachability before attacking.
- §10.3 Area-of-Effect · May target the attacker's own node unless it has the shaft icon; "Outside a PvP encounter, characters on the targeted node are not affected" · CH-10-030 · **A3** · delete both; an attack that "targets every enemy on a node" does not target characters.
- §10.3 Repeat · Stamina paid once; "steps 3 to 12" for each resolution; may stop early ("up to"); each resolution has its own target; two-handed reroll each time; luck for one roll only; all resolutions are one attack · CH-10-032, combat-E27 (CH-10-043) · **A1 for "pay once, roll again each time, choose a target each time"; the rest A3** · two sentences.
- §10.4 · Whether a weapon is two-handed "is judged when each attack is made"; any card in the other slot, including a spell or catalyst, prevents it · CH-10-033 (A-069) · **A2** · the author's sentence ("without equipment to their other hand") already says the second; delete the first.
- §10.4 · A spell is never two-handed, equipped or stored; a catalyst's own printed attack option does gain the reroll · CH-10-034, combat-E28 (CH-10-044) · **A3** · §4.3 says spells are never two-handed. The catalyst rider is hair-splitting.
- §10.4 · "A character who wields a weapon other than a shield two-handed has no shield equipped and therefore cannot parry" · CH-10-034, VA-025b (CH-10-046) · **A3** · a tautology.
- §10.5 · "Relevant stat" as a defined term; "only the relevant stat is compared; the weapon's other stat requirements play no part" · CH-10-036 · **A2** · the author's "exceeds the weapon's highest stat requirement" needs no term.
- §10.5 · The red cube "is removed when the weapon is no longer equipped" · CH-10-036 · **A3** · delete.
- §10.5 · A weapon whose requirements are all zero is never scaled · combat-E29 (CH-10-045), earlier skipped as optional (CH-10-040, A-066) · **author's call** · one sentence; with the threshold at five it stops every starting-grade weapon being scaled by everyone. Keep if the author agrees, otherwise delete; either way no more than the 17 words it has.

### Worst passages

**1. §10.2, Character Movement (the whole section, 314 words)**

Final (opening and definitions):
> During an *encounter* a character changes *node* in five ways: by either of two *minor actions*, *Walk* and *Run*; by a *shift* icon on an *attack option* (see §10.3, Shift); by the movement that follows a successful *dodge* (see §9.5); and by a *push* (see §8.4). Walk, Run, and shift are *moves*. The movement that follows a dodge and the movement of a push are not moves (see §5.2).
> **Walk.** A minor action. The character moves to one *adjacent node* without spending stamina. A character may walk once per *turn*.
> **Run.** A minor action. The character spends one stamina and moves to one adjacent node. A character may run any number of times in a turn, spending one stamina for each node. A character who has run cannot *Rest* in that turn (see §10.1).
> A character may walk and run before the *major action*, after it, or both (see §10.1). A character may run without having walked. …

Every sentence is already in §10.1 (the Walk and Run bullets, the Rest bullet, "in any order"), §5.2, §5.3 or §5.5. Cut version (41 words), as the last paragraph of §10.1, with §10.2 deleted:
> A character also moves when an attack option shifts them, when they dodge, and when they are pushed. However a character moves, they stay on the encounter's tile and enter only nodes that the terrain allows.

**2. §10.3, Range (200 words and a 55-word example)**

Final:
> Every weapon card and spell card prints a base range beside the range icon (see §4.1, Card Anatomy). An attack option that prints a range of its own uses that range in place of the card's base range. The attack option's range applies to that attack option alone; the card's other attack options keep the base range.
> Range is counted in *nodes* (see §5.4). The range of an attack is a maximum: a target at any shorter distance, including a target on the attacker's own node, is within range unless an icon on the attack option forbids it (see §10.3, Shaft). Range is checked when the target is chosen, after any shift resolved before the dice. A character cannot begin an attack unless a permitted target is within its range or a shift printed before its dice is able to bring one within range. If no permitted target is within range when the target is to be chosen, the attack ends without a roll, and the stamina paid is not returned.

Source (30 words):
> Some *attack options* specify a range that is different from the weapon's default range listed on its equipment card. An *attack option* specific range replaces the weapon's range for that attack action.

Cut version (34 words, no example):
> An attack option that prints its own range uses it in place of the weapon's range. The target may be at that range or nearer. If no target is in range when the target is chosen, the attack is lost.

**3. §10.4, Two-Handed Attacks (328 words)**

Final (after the two-case list):
> Any card in the other weapon slot is equipment in the other hand. A one-handed weapon equipped beside a *shield*, a *catalyst*, a *spell*, or a second weapon is not two-handed (see §4.1, Card Types). Whether a weapon is wielded two-handed is judged when each attack is made.
> When a character attacks with a weapon wielded two-handed, the character may reroll one die of the attack roll after rolling (see §10.3). The new result stands. The reroll is available on every attack roll made with that weapon, including each resolution of an *attack option* that bears the *repeat* icon…
> A spell is never two-handed (see §4.3). A spell card equipped while the other weapon slot is empty gains no reroll, and the attack options of a spell stored in a catalyst gain none. A catalyst is a weapon: an attack option printed on the catalyst card itself gains the reroll while the catalyst is wielded two-handed.
> A character who wields a weapon other than a shield two-handed has no shield equipped and therefore cannot *parry* (see §9.6).
> *Example.* The Knight has a one-handed sword in the right weapon slot and no card in the left weapon slot … (89 words)

Source (57 words, 37 of them rule):
> Attack actions with two-handed weapons may reroll any single die after rolling to attack. Additionally, if a character equips a one-handed weapon without equipment to their other hand, that weapon is considered to be wielded as two-handed and gains the same reroll option.

Cut version (45 words):
> A weapon is wielded two-handed if it bears the two-handed icon, or if it is a one-handed weapon and the character's other weapon slot is empty. On each attack roll with such a weapon the character may reroll one die. Spells gain no reroll.

### Unintuitive or over-engineered rules

- **The 12-step attack.** Steps 3 and 12 are the two shift positions, 6 and 7 are two rerolls, 9 and 10 are subtract and place. Repeat then tells the player to "resolve steps 3 to 12 of the attack for each resolution". The author's paragraph has six beats: choose and pay, choose a target in range, roll, reroll, subtract block or resist, place wounds and effects. Six steps, with shift handled in the Shift entry, lose nothing.
- **"Relevant stat."** A term invented to carry a tie-break the author gave in four words ("if two requirements are tied, use either"). Say "the weapon's highest stat requirement" and delete the term and two of the three examples.
- **The reachability test for attacks** (combat-E26). Before paying, a player must establish that "a shift printed before its dice is able to bring one within range". Players will simply not start attacks they cannot finish. Replace with the one-line outcome in the cut version above.
- **"In this section the word enemy covers all of these."** The book defines enemy elsewhere and then changes it for one section. Either the definition of enemy includes bosses for targeting purposes everywhere, or §10.3 says "a hostile model" throughout. Simplest: delete the sentence; the boss, invader and mimic chapters each say that characters attack them.
- **Two-handed catalysts.** "A spell is never two-handed" but "a catalyst is a weapon" whose own printed attack option does get the reroll, while the spell stored in it does not. Three sentences for a case that the author's rule ("spells gain no reroll") settles.
- **§10.1's stamina paragraph** ("A character cannot choose to spend stamina that the bar has no empty space to hold … If a rule obliges a character to place a stamina cube and no empty space remains…"). The reader meets the overflow rule in the middle of the turn order with an example about a dagger. It is §3.4's rule; a reader of §10.1 needs only "pay its stamina cost".

---

## Chapter 11 — Returning to the Bonfire

### Section table

| § | source words | final words | words it needs | main excess |
|---|---|---|---|---|
| 11 intro | (flavour, inside The Bonfire) | 44 | 40 | none; the author's own flavour, already halved |
| 11.1 The Bonfire | 159 (about 75 of rule) | 242 | 60 | R + A: a list of the three occasions for returning, each owned by §7.5 or §16.5; a ruling that returning and resting "are one act" |
| 11.2 Resting | 105 | 618 | 170 | E + D: one 211-word example; three paragraphs on what resting does not do (ember, shop, inventory); spark costs restated from §7.4 |
| 11.3 The Firekeeper | 154 | 299 | 110 | V + R: tier sequence spelt out tier by tier; souls rules from §7.6; campaign pointer |
| 11.4 Blacksmith Andre | 248 | 710 | 300 | V + A: every price stated three times (Purchases, Sales, Prices table); a three-way list of where sold cards go, by provenance; shop tiers restated from §6.3 |
| 11.5 Resuming Exploration | 135 | 413 | 150 | R + E: the skip rule and black cubes of §7.5 restated; three exception pointers (Level 4, boss, invader); an 80-word example |
| **Chapter** | **809** | **2,326** | **830** | 61 cross-references; 3 examples (346 words) against one inline example in the source |

Gate 1 changes treated as the author's: stat tier four at 10 souls (OQ-09), skipping cleared encounters (OQ-10), free rest after the boss or after PvP (OQ-15), tier two shop (OQ-27).

### Added rules

- §11.1 · "The bonfire tile has no nodes … A model on the bonfire tile stands anywhere on the tile" · CH-11-004 · **A3** · delete.
- §11.1 · "Returning to the bonfire tile and resting there are one act"; the party cannot choose to return at zero sparks · core-E35, core-E36 (CH-11-044, -045), reversing the pipeline's own CH-11-006 ("Returning to the bonfire tile costs nothing") · **A2** · the author's sentence says it: "The characters must collectively spend one spark to visit the bonfire."
- §11.2 · A failed encounter forces a rest; with no spark the game is lost · CH-11-008 (CMP-0006) · **A1, owned by §7.1 and §7.5** · one clause here at most.
- §11.2 · Rest step 5, "Remove every condition token from each character" · CH-11-012 · **A3** · §8.5 already removes every condition token when the encounter ends, and no encounter is in progress at a rest.
- §11.2 · Visits "in either order and any number of times" · CH-11-015, core-E09 (CH-11-041) · **A3** · delete the tail.
- §11.2 · "Resting neither places nor removes an ember token…" · CH-11-013 · **A3** · delete.
- §11.2 · "Resting does not restock the shop…" (55 words) · core-E10 (CH-11-042), reversing CH-11-014, which had made restocking a step of the rest · **A3 here** · the author's bullet, "Shops are only restocked after a boss is defeated", is in §11.4 already.
- §11.2 · Characters may rearrange inventory and trade during a rest "as at any time outside an encounter" · CH-11-015 · **A3** · §3.2 owns it and the sentence admits it adds nothing.
- §11.2 · "A rest restores every character in the same way, whether the character was living, dead, or lost … After a rest no character is hollow, and every endurance bar is empty" · CH-11-010 · **A3** · restates steps 2 to 4.
- §11.3 · Any number of purchases in one rest, each paid separately; souls cannot be pooled; "Outside a rest, souls are spent only to call a summon" · CH-11-017, CH-11-020 (A-100) · **A3 here** · §7.6 owns souls.
- §11.4 · A card may be sold from an equipped slot, the back-up slot or the inventory · CH-11-028 · **A3** · delete.
- §11.4 · An ember card is a tier one shop card, cannot be bought by a character not permitted to carry one, and when sold "is returned face up to the tier one shop" · CH-11-024, CH-11-025 (A-007) · **A2 / A4 for the special return** · keep the author's "each character may carry only one ember card"; a sold ember goes where any tier one card goes.
- §11.4 · Invader treasure and Titanite Scale cards sell for one soul and go back to the box; boss treasure goes back to the box; other cards go to the deck only if they "came from a treasure deck or from the shop" · lead-E09 (CH-11-046), VA-026a to VA-026c (CH-11-048 to -050) · **A2** · one table row and one sentence: "A sold card goes to the bottom of its deck, or to the box if it has none."
- §11.4 · Titanite "is sold with" the weapon; "the sell value of the weapon is paid once; attached Titanite adds nothing to it. The weapon and the Titanite are separated, and each goes to the place stated for a sold card of its kind" · CH-11-026, core-E32 (CH-11-043) · **A2** · the author's two bullets suffice (Titanite to the bottom of the tier one deck; other upgrades back to the character).
- §11.4 · Andre removes non-Titanite upgrades; both services are free; any number per rest · CH-11-031 · **A2** · one sentence, or leave to §4.2, which the next paragraph cites for everything else.
- §11.5 · Reset steps "Leave the black cube…", "Leave every terrain token…", "Leave all dropped souls…" · CH-11-033, CH-11-035 (CMP-0019) · **A2** · three steps that instruct the players to do nothing. One sentence: "Nothing else on the tiles is moved."
- §11.5 · A cleared Level 4 encounter is not reset; a failed boss encounter resets under §15.2; an invader that has appeared does not return · CH-11-036 · **A3 here** · each is owned by the section cited.
- §11.5 · The fog gate on the bonfire tile lets the party go straight to the boss · CH-11-037 · **A3 here** · §15.1 owns it.

### Worst passages

**1. §11.2, the paragraphs after the rest procedure and the example (about 380 words)**

Final:
> A rest restores every character in the same way, whether the character was living, dead, or lost when the rest began. After a rest no character is *hollow*, and every endurance bar is empty.
> Resting neither places nor removes an *ember token*. An *embered* character stays embered through the rest, and a character who is not embered does not become embered by resting (see §7.3).
> Resting does not restock the *shop*. Cards bought from the shop are not replaced, and unsold cards stay in the shop, until the shop is next restocked during the setup that follows a boss's defeat (see §6.3, Restocking After a Boss). In campaign play the shop is restocked during the setup that follows the completion of a section (see §18.6, Blacksmith Andre's Shop).
> While the party rests, each character may rearrange their *inventory* and equipment slots and may trade cards with other characters, as at any time outside an encounter (see §3.2).
> *Example.* The Knight, the Herald, and the Assassin clear the second encounter … (211 words covering the spark dial, cubes, tokens, the Firekeeper, a purchase, a sale and the reset)

Source: nothing; the rest is seven bullets (105 words).

Cut version: delete all five paragraphs. The rest procedure above them is complete without them. If one example is wanted for the chapter, keep the Firekeeper's (55 words), which is the author's own.

**2. §11.4, Sales (about 240 words) and Prices**

Final:
> … Andre pays one soul for a tier one or tier two treasure card, one soul for an *invader*'s treasure card or a Titanite Scale card, and six souls for a boss treasure card, and the character takes the souls from the supply. Legendary treasure and *transposed treasure* are *tier two treasure* cards (see §6.2).
> A sold card goes to one of the following places.
> - A sold tier one or tier two treasure card that came from a treasure deck or from the shop is placed face down at the bottom of the treasure deck of its tier (see §6.2).
> - A sold boss treasure card is returned to the game box, and so is any other sold card that came from no treasure deck: an *invader*'s treasure card or a Titanite Scale card.
> - A sold ember card is returned face up to the tier one shop.
> When a *weapon* with *Titanite* attached is sold, the Titanite is sold with it, and every other *upgrade card* attached to a sold card returns to the character's inventory (see §4.2, Titanite). The sell value of the weapon is paid once; attached Titanite adds nothing to it. The weapon and the Titanite are separated, and each goes to the place stated for a sold card of its kind.

Source (five bullets, 62 words):
> Starting equipment cannot be sold. Sold items are placed at the bottom of their respective treasure deck. Titanite upgrades … attached to sold weapons are returned to the bottom of the tier one treasure deck. Weapon upgrades aside from Titanite upgrades … are returned to the character. Armour upgrades attached to sold armour are returned to the character.

Cut version (58 words, with the price table as the only statement of prices):
> A character may sell any treasure card except starting equipment, for the value in the table. A sold card goes to the bottom of its treasure deck, or back to the box if it has no deck. Titanite attached to a sold weapon goes to the bottom of the tier one deck. Every other attached upgrade returns to the character.

**3. §11.1, The Bonfire (242 words)**

Final:
> The *bonfire* is represented by the bonfire tile, which is placed at setup (see §6.4). The bonfire tile has no nodes, and no *encounter* is fought on it. A model on the bonfire tile stands anywhere on the tile. … The party returns to it in the following cases. (three bullets, each a pointer) … When the party returns, the characters' models are placed on the bonfire tile. The characters do not pass back through the encounter tiles, and no encounter is fought on the way.
> Returning to the bonfire tile and resting there are one act. The party returns only to rest, and the rest begins when the models are placed on the tile (see §11.2). The party cannot choose to return while the *spark* dial shows zero (see §7.4).

Source (the rule in it, 40 words):
> The characters must collectively spend one *spark* to visit the *bonfire* to rest, improve stats, upgrade equipment, and shop. … Characters cannot spend their hard-earned *souls* without resting at the *bonfire*.

Cut version (48 words; §11.1 then merges into §11.2):
> After any encounter the party may return to the bonfire and rest, and after a failed encounter it must. Place the characters' models on the bonfire tile; no encounter is fought on the way back. A rest costs one spark, except after a boss is defeated.

### Unintuitive or over-engineered rules

- **Where a sold card goes depends on where it came from** ("came from a treasure deck or from the shop" against "came from no treasure deck"). Nobody remembers a card's provenance. Rule by the card itself: it has a deck or it does not.
- **A sold ember card returns face up to the shop**, the one card that does. Treat it as the tier one card it is. Lost: an ember can no longer be bought back at once, which costs the players nothing they would notice.
- **Prices in three places.** Purchases states 2 and 4 in prose; Sales states 1, 1 and 6 in prose; the Prices table states all of them; "An ember card is priced as a tier one card" appears twice. Keep the author's table and nothing else.
- **Reset steps that say "Leave".** Three of the five numbered steps of the reset instruct the players not to touch something. The reset is two actions: turn the encounter cards face down and remove the enemy models.
- **Returning versus resting.** The pipeline first separated the two (CH-11-006), then ruled that they "are one act" (core-E36), and the text still carries both ideas across §11.1 and §11.2. The author had one idea: spend a spark to visit the bonfire.
- **The rest's condition step.** Step 5 removes tokens that §8.5 says cannot be there. A reader who trusts step 5 will wonder when conditions outlast an encounter.

---

## Chapter 20 — Player versus Player

The source is 27 bullets (247 words) under one heading; the final has nine sections. The source was truly incomplete here: it never says how a character defends against another character. Some growth is legitimate, so the "needs" figure is three times the source.

### Section table

| § | source words (bullets that map to it) | final words | words it needs | main excess |
|---|---|---|---|---|
| 20 intro | 0 | 50 | 0 | flavour paragraph with no rule |
| 20.1 Setup | 70 | 462 | 150 | R + D: a paragraph previewing §20.7, §20.8 and §20.9; "Steps 2 and 3 restore the characters but are not a rest…"; a definition of a corner |
| 20.2 Turn Order | 25 | 137 | 40 | D: a definition of a round for PvP; the aggro token set aside twice (here and setup step 6) |
| 20.3 Character Turns | 10 | 103 | 20 | R: the author's one bullet ("turn structure is unchanged") expanded into a list of what is unchanged |
| 20.4 Attacking a Character | 40 | 789 | 250 | E + R: two examples (211 words); a four-step attacker procedure and an icon paragraph that restate §10.3 |
| 20.5 Pushes and Conditions | 0 | 146 | 35 | D: two paragraphs saying that the general rules apply; one needed sentence at the end |
| 20.6 Traps | 30 | 354 | 110 | A + E: "available" and "outermost" defined by rings; five riders on triggering; one example |
| 20.7 Death | 25 | 158 | 45 | R + D: death causes restated; "neither cleared nor failed" |
| 20.8 Victory | 30 | 360 | 90 | G + R: victory bonus stated three times and ultimate victor twice; a stalemate rule; one example |
| 20.9 After the PvP Encounter | 0 | 147 | 40 | R: the one free rest explained three ways |
| **Chapter** | **247** | **2,706** | **780** | 53 cross-references; 4 examples (371 words) |

Gate 1 changes treated as the author's: PvP after every boss and its place before the free rest (OQ-15); the compressed dodge-difficulty table (B-024).

### Added rules

- §20.1 · No PvP encounter with fewer than two eligible characters · CH-20-006 (A-034) · **A1** · keep; one sentence.
- §20.1 · Corner chosen by each player in turn order; "a corner node is the node nearest to one of the four corners of the tile, among the nodes that hold no terrain"; terrain stays · CH-20-007, CH-20-009 (CMP-0009) · **A1 / A2** · "Each player in turn order places their model on an empty corner node. Terrain stays."
- §20.1 · "Steps 2 and 3 restore the characters but are not a rest … No spark is spent, no encounter is reset, and the characters cannot visit the Firekeeper or Blacksmith Andre. An embered character keeps the ember token" · CH-20-008 · **A3** · the steps say what is restored; nothing suggests a shop visit.
- §20.1 · Campaign: only after a boss that completes a section · VB-013 (CH-20-042) · **A3 here** · §18.1 owns it.
- §20.2 · Ties in threat: "the players decide … If the players cannot agree, … at random"; the order is fixed for the encounter · CH-20-012 (A-014) · **A4** · the tied players are opponents. "Ties are settled by a die roll."
- §20.2 · A round defined for PvP · CH-20-012 · **A3** · needed only by the stalemate rule below.
- §20.3 · "Every limit of the standard game applies, including the limit of one spell attack option per turn. No model leaves the tile" · CH-20-014 · **A3** · delete.
- §20.4 · The defender blocks or resists by rolling (two highest dice), dodges against the table, or parries · CH-20-015 (A-032, CMP-0009), combat-E33 · **A1** · the hole the source left. Keep, in about 60 words.
- §20.4 · "Attacker" and "defender"; a four-step attacker procedure; the list of modifiers that still apply (scaled, two-handed, luck) · CH-20-015, phantom-E27 (CH-20-037) · **A2** · "A character attacks another character as an enemy is attacked."
- §20.4 · "The word enemy in a heroic action or on a treasure card means another character" · phantom-E26 (CH-20-036) · **A1** · keep; one sentence.
- §20.4 · Shaft, AoE and repeat restated for characters · CH-20-016 · **A3** · follows from the sentence above; keep only "an area attack does not hit the attacker".
- §20.4 · The riposte "is an attack under this section with the roles reversed, and its dodge difficulty is set by the stamina cost…"; it cannot be parried · CH-20-017 · **A2** · "A riposte cannot be parried."
- §20.5 · Pushes and conditions work as in the standard game; a push onto a trap triggers it · CH-20-021 · **A3** · two paragraphs that add no rule.
- §20.5 · A choice the rules leave to "the players" belongs to the player whose character attacks or moves · CH-20-022 ("none (drafting completion)") · **A1** · keep; it is the one PvP-specific sentence in the section.
- §20.6 · Trap token drawn unseen and placed face down; "may occupy a node of any type"; "available" defined; "outermost" defined by rings working inward; none placed if no node or no token · CH-20-023 (A-033) · **A2** · "…on an empty node at the edge of the tile, or as near the edge as there is one."
- §20.6 · Blank tokens do nothing; the damage value is not used; a character "cannot choose to suffer a trap's damage"; a character with no space for the dodge's stamina cube dies; a face-up token stays and has no further effect · CH-20-024 (A-033, A-083) · **A2** · "A character who enters a trap must dodge it and dies if the dodge fails or cannot be paid for."
- §20.7 · "A PvP encounter is neither cleared nor failed … the party spends no spark for it and is not required to rest" · CH-20-026 · **A3** · delete.
- §20.8 · If the last characters die together nobody wins · CH-20-027 · **A1** · keep; one sentence.
- §20.8 · Stalemate: after three rounds with no damage and no death, every character suffers one undefendable damage each round · CH-20-028 (A-035; listed among the optional findings in CH-20-033) · **A3 / A4** · the author already built the clock: a trap is laid on the outer ring after every turn and a failed dodge is death. The new rule adds a counter to watch and a second clock.
- §20.8 · The victory bonus is marked by "a spare token of any kind", is capped at one, lasts to the end of the game, and has no effect outside PvP · CH-20-029, phantom-E30 (CH-20-039) · **A2** · the cap is a ruling on the author's "+1 attack damage in future PvP only"; keep it as four words ("once only") and drop the token.
- §20.8 · "Ultimate victor" as a defined term; no bonus from the last PvP; no victor if nobody wins; "Victory over the final boss is shared by every player, whatever the outcome" · CH-20-030 · **A3** · the author's bullet is enough.
- §20.9 · Trap tokens returned; the rest "is the one rest that follows the boss's defeat … a PvP encounter grants no second rest"; campaign pointer; no rest after the last PvP · CH-20-031, phantom-E32 (CH-20-041) · **A2** · one sentence.

### Worst passages

**1. §20.8, the victory bonus and the ultimate victor (about 215 words with the example)**

Final:
> **Victory bonus.** The reward for winning a PvP encounter that follows the defeat of a boss other than the *final boss*: +1 to the attack value of each of the winner's attacks in every subsequent PvP encounter.
> When a character wins a PvP encounter that follows the defeat of a boss other than the final boss, the character gains the *victory bonus*. A spare token of any kind is placed beside the winner's dashboard to mark it. In every subsequent PvP encounter, the character adds one to the *attack value* of each of their attacks (see §20.4). A character holds no more than one victory bonus, however many PvP encounters the character wins. The victory bonus has no effect outside PvP encounters and is kept until the game ends.
> **Ultimate victor.** The character who wins the PvP encounter that follows the defeat of the final boss.
> The winner of the PvP encounter that follows the defeat of the final boss is the *ultimate victor*. That PvP encounter awards no victory bonus. If no character wins it, the game has no ultimate victor. Victory over the final boss is shared by every player, whatever the outcome of the PvP encounter (see §7.1).

Source (17 words):
> Victory on non-final bosses provides +1 attack damage in future PvP only. Victory on the final boss determines the ultimate champion.

Cut version (39 words):
> The winner of a PvP encounter adds one to the attack value of their attacks in every later PvP encounter. The bonus is gained once only. The winner of the PvP encounter after the final boss is the ultimate champion.

**2. §20.6, placing a trap (about 135 words)**

Final:
> At the end of each character's *turn*, that character's player draws one *trap token* from the supply without looking at its face and places it face down on an outermost available *node* of that player's choice. A trap token placed in a *PvP encounter* may occupy a node of any type.
> A node is available when it holds no model, no trap token, and no other *terrain*. The outermost available nodes are the available nodes along the edges of the tile. When no node along the edges is available, the outermost available nodes are the available nodes of the next ring inward, and so on towards the centre of the tile. If no node is available, or if no trap token remains in the supply, no trap token is placed.

Source (12 words):
> Players place a trap token on an outermost available node after each turn.

Cut version (47 words):
> At the end of their turn, each player places one trap token face down, unseen, on an empty node at the edge of the tile. When the edge is full, the token goes on an empty node as near the edge as possible. A character who enters it must dodge it or die.

**3. §20.4, the attack before the defences (about 250 words)**

Final:
> In a *PvP encounter* the *target* of a character's attack is another character. The character who makes the attack is the attacker, and the targeted character is the defender. The attacker resolves the attack as an attack against an enemy (see §10.3), and the defender defends as against an enemy's attack (see §9.3), except as this section states.
> The attacker makes the attack as follows. 1. Choose an *attack option* of an *equipped* card and pay its stamina cost. 2. Name one other character within the attack option's *range* as the target (see §5.4). 3. Roll the attack option's dice, apply every modifier, and use any rerolls. 4. Add one to the result if the attacker holds the *victory bonus* (see §20.8).
> The final result is the *attack value*. The modifiers and rerolls of the standard game apply to the roll: the +1 of a *scaled* weapon (see §10.5), the reroll of a *two-handed* weapon (see §10.4), and the *luck* token (see §3.5, Luck).
> The icons and text of an attack option apply to a defender as they apply to an enemy (see §10.3). … (shaft, AoE and repeat restated)

Source: nothing but the dodge table.

Cut version (68 words):
> A character attacks another character as an enemy is attacked, and wherever a card says "enemy" it means another character. The attacked character defends as against an enemy's attack: by blocking or resisting with dice, by dodging, or by parrying. The dodge difficulty of the attack is set by its stamina cost, as the table shows. A riposte cannot be parried. Where the rules leave a choice to the players, the attacking player makes it.

### Unintuitive or over-engineered rules

- **The stalemate rule** (§20.8). Players must count rounds in which "no character suffers damage and no character dies" and then apply damage that "a character cannot defend against". The author's closing ring of lethal traps already ends a stand-off. Delete; nothing is lost while trap tokens last.
- **Ties settled by agreement between opponents** (§20.2). Roll for it.
- **A trap token that shows a damage value which "is not used"**, with an example that reads the damage value aloud and then ignores it. The author's rule is simply "fail the dodge and die". Say that, and do not mention the printed damage.
- **"Steps 2 and 3 restore the characters but are not a rest."** The author wrote "Restore each character as if they rested at the bonfire." The final replaces that with two steps and then a paragraph listing what a rest would have included. The author's sentence is clearer than both.
- **Three statements of one bonus.** A bold definition, a paragraph and step 4 of the attack all give the +1. A player checking it finds three slightly different wordings.
- **§20.9's "the one rest that follows the boss's defeat … grants no second rest".** A worry created by §20.1 restoring the characters before the fight; if setup says "restore each character", §20.9 needs only "then carry on with the setup that follows the boss".

---

## Totals — combat group

| Chapter | source words | final words | words needed | growth | excess |
|---|---|---|---|---|---|
| 08 Combat Basics | 1,240 | 3,653 | 1,260 | ×2.9 | 2,393 |
| 09 Enemy Turn | 1,386 | 4,544 | 1,450 | ×3.3 | 3,094 |
| 10 Character Turn | 1,094 | 3,713 | 1,130 | ×3.4 | 2,583 |
| 11 Returning to the Bonfire | 809 | 2,326 | 830 | ×2.9 | 1,496 |
| 20 Player versus Player | 247 | 2,706 | 780 | ×11.0 | 1,926 |
| **Group** | **4,776** | **16,942** | **5,450** | **×3.5** | **11,492** |

The group needs about 5,450 words: the source's length plus about 700 words of legitimate fixes, most of them in PvP. The other 11,500 words are excess.

Split of the excess by class. Example words and the words inside "(see …)" brackets are counted; the other classes are estimated paragraph by paragraph.

| Class | words | share of excess | note |
|---|---|---|---|
| E examples | 3,110 | 27% | 42 examples, 3,458 words in all; about 350 words (six short examples) are worth keeping |
| R restated | 2,290 | 20% | rules owned elsewhere, or by the paragraph above |
| A added rules | 1,770 | 15% | after allowing for the short fixes that are needed |
| X cross-reference clutter | 1,730 | 15% | 350 bracketed references (869 words) and about 860 words of sentences that only point |
| D defensive | 1,180 | 10% | "is not a move", "whether or not", "stays where it is", "is not returned" |
| V verbose | 1,190 | 10% | includes four chapter intros with no rule (228 words) |
| G glossary-in-chapter | 225 | 2% | 19 bold inline definitions |

## How it happened

1. **A worked example for every rule, by instruction.** The drafting brief required examples ("brief §2 (worked examples)"), and the chapter instructions asked for each procedure "succeeding once and failing once". CH-09-036 added 11 examples to chapter 09 in one entry; CH-10-038 added 11 to chapter 10, where the source had none. Result: 42 examples, a fifth of the final text, including three for a +1 scaling bonus (§10.5) and one of 211 words for a rest (§11.2, CH-11-016).

2. **One owner per rule, and a pointer everywhere else.** The policy was meant to stop repetition. In practice each section gained sentences announcing what it does not own. CH-09-006 added to §9.1 "Enemies target only characters … (see §8.1) … scaled for the number of characters (see §8.3) … (see §8.5)"; CH-10-026 added six one-sentence pointers to §10.3 (hits, bosses, health dials, weak arc, PvP, riposte); CH-08-009 added pointers to boss, phantom and mimic cards. Result: 350 bracketed cross-references and whole paragraphs with no rule (§9.1 paragraphs 4 and 5; §11.5 paragraph 3).

3. **Every audit finding became a paragraph.** Findings of the form "the manuscript does not say what happens when…" were closed by writing the answer out, however rare the case. A-085 (push into terrain) became CH-08-021 and CH-08-022 and two examples; A-082 (blocked enemy path) became the Paths sub-section, CH-09-009; A-087 became the dodge-movement paragraph, CH-09-027; A-033 became the ring-by-ring trap placement of §20.6, CH-20-023. Most of these needed one sentence.

4. **Rulings that bred rulings.** A late ruling changed one sentence and then needed consequential rulings and verification patches. The either-slot parry: combat-E22, then E23, E24, E25, then VA-025a and VA-025b. The Attack Sequence: combat-E20 (CH-09-041), then RV-001 to RV-004 because the sequence and the defence procedures now claimed the same steps. The repeat icon: CH-09-018 said one thing, CH-08-042 followed it, combat-E12, E18 and E19 reversed both. The list of "four reasons" for a push (CH-08-020) was found incomplete and patched by combat-E13 and E14. In chapter 11, CH-11-006 was reversed by core-E36 and CH-11-014 by core-E10, and each reversal left a paragraph explaining what is not the case.

5. **Prose turned into numbered procedures, then explained.** The house style wanted "one action per step". CH-10-020 made the author's attack paragraph a 12-step procedure, which then needed six paragraphs to explain interactions between steps, and Repeat now cites "steps 3 to 12". CH-08-023 made the push-move four steps plus three paragraphs. CH-11-032 made the reset five steps, three of which begin "Leave". Step numbers then became cross-reference targets (mechanism 4).

6. **Glossary-form definitions and coined terms inside the chapters.** CH-08-002 and CH-08-004 set Target and Hit as bold definitions and then restated each in prose; CH-10-036 coined "relevant stat"; CH-08-029 coined "next complete turn"; CH-20-004 and CH-20-030 made "PvP encounter", "victory bonus" and "ultimate victor" defined terms, each stated again in the paragraph below its definition.

7. **Optional modules written into core rules.** Each core section was made to answer for PvP, summons, bosses and campaigns. lead-E20 and VA-024a put summons into Stagger and Frostbite (CH-08-052, -056); VB-006 put the Four Kings into §8.4 (CH-08-053); §8.1, §8.4, §8.5, §9.3, §9.6, §10.1 and §10.3 each end with "In a PvP encounter…".

## Ten cuts, in order of words saved for least loss

1. **Delete 36 of the 42 examples and halve the rest** (about 3,100 words). Keep one each for a failed dodge (§9.5), a parry and riposte (§9.6), a full character attack (§10.3), a push-move (§8.4), the Firekeeper (§11.3, the author's own) and a PvP attack (§20.4).
2. **Strip the cross-reference apparatus** (about 1,700 words): remove bracketed references to the neighbouring section and to glossary terms, and delete sentences and paragraphs that only point (§9.1 paragraphs 4 and 5; §10.1 paragraphs 1 and 2; §10.3's boss, PvP and riposte paragraphs; §11.5's exceptions paragraph; §8.2's other-card pointers).
3. **Delete what restates a neighbour** (about 1,100 words): §10.2 entire (40 words move to §10.1); the icon legend of §8.2; the three paragraphs of §8.3 that repeat its table; the four direction sub-sections of §9.2; the chapter intros of 08, 09, 10 and 20; the bold inline definitions.
4. **Chapter 20 to the author's shape plus the defence rule** (about 900 words): cut §20.1's preview and "not a rest" paragraphs, §20.2's round, §20.3, both general paragraphs of §20.5, §20.7's last paragraph, the duplicated bonus and victor text, the stalemate rule, and the ring definitions.
5. **§10.3 back to six steps** (about 700 words): merge the two rerolls and the subtract-and-place steps, delete the six explanatory paragraphs, and return Range, Area-of-Effect, Shaft and Repeat to two sentences each.
6. **One statement of how an enemy attack ends** (about 750 words): delete the Attack Sequence and every "steps 5 to 7" hand-back; put "place the damage, then the push, then the condition" in §9.3; delete the edge-case paragraphs of §9.4 and §9.5 (no dice, one die, negative totals, back-up slot, stamina space, stamina not returned) and the Traps sub-section.
7. **Chapter 11 housekeeping** (about 700 words): merge §11.1 into §11.2; delete the "does not" paragraphs of §11.2; prices in the table only; sold cards "to the bottom of the deck, or to the box"; reset as two actions.
8. **§8.4 Pushing to the author's four paragraphs** (about 550 words): delete the list of causes, the terrain paragraph, the node-limit paragraph and the boss and PvP pointers; state the push-move once here and delete its restatement in §9.2.
9. **§8.5 general rules in one paragraph** (about 400 words): one token per condition, no reduction below zero, the own-turn timing sentence, removal at the end of the encounter; delete the aggro and summon riders and every "is not an attack" sentence.
10. **§9.6 riposte to one sentence and the shield rule to one clause** (about 350 words): "the character may riposte with their other weapon; it is extra"; delete the spell, shaft, two-handed-shield and turn-ends riders.

Together these remove about 10,250 of the 11,500 excess words and no rule of the author's.
