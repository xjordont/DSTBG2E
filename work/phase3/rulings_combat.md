# Phase 3A rulings memo — cluster `combat`

Scope: lead items 8 and 16 of `14_open_issues.md`; every item of the per-chapter lists for chapters 05, 08, 09 and 10; the designer points set for this cluster (entries combat-072 to combat-079). Edits are in `work/phase3/edits_combat.json` (44 objects, `combat-E01` to `combat-E44`); every `old` was checked to occur exactly once, the 44 edits were applied in order to a scratch copy of the book, and `tools/style_check.py` reports 0 violations on the result. No manuscript file was touched.

Source shorthand used in the Evidence lines (all under `work/text/`):

| Short | File |
|---|---|
| Core | `DS-Core-Rules-lores.txt` (official, 2017) |
| TG | `DS-TG-Rulebook-Compressed_compressed.txt` (official, 2022) |
| FAQ | `Dark_Souls_The_Board_Game_FAQ.txt` (official, 11 April 2017) |
| Ext | `DS-Extended-Rules-V45.txt` (community) |
| Hol | `Hollowed_Edition_v1.3.txt` (community) |
| Src | `work/phase2a/source/NN_*.md` (the author's manuscript) |

Online: web search worked; several sites did not. Opened and read: the community "DSBG - Unofficial Guide & Rules FAQ" (https://docs.google.com/document/d/1DmbTaM68OoosZcSCFW0bTNgBWCaHSP2UE9Um-X4XF54/mobilebasic), cited below as "Guide". Seen only as search-result summaries: the publisher's backer update on trap tokens (https://darksouls.backerkit.com/hosted_preorders/project_updates?page=22), the GamesRadar review (https://www.gamesradar.com/dark-souls-the-board-game-review), the Tabletop Gaming review (https://tabletopgaming.co.uk/reviews/dark-souls-the-board-game-review), and a fan rules summary (https://lehi-innovation.github.io/boardgame-rules/rules/dark-souls-the-board-game/). Refused: both Reddit house-rule megathread mirrors (HTTP 503 and 404), so r/DarkSoulsTheBoardGame is represented only by search snippets; no BoardGameGeek thread could be opened. Where "online: silent" appears, it means nothing was found in what could be read.

One structural fact governs most of this cluster. In both official rulebooks every enemy acts before each character's turn (Core 875–894). This book has one enemy phase and one character phase per round (§7.5) and replaces the lost pressure with the enemy scaling table (§8.3). Every timing question below was judged against this book's round, not the official one.

## Lead items

### combat-001 · Lead 8 · traps and other models
- Question: Do enemies, bosses and phantoms trigger traps or suffer them?
- This book now: Only characters trigger traps and only characters are affected; enemies, bosses and phantoms neither trigger nor suffer them (§5.5, Traps; glossary Trap token; §9.2; §12.1; §22.3).
- Evidence: official 2017: "Trap tokens have no effect on enemies and cannot be triggered by them" (Core 811–826) / official 2022: "Traps do not affect enemies and are not flipped if an enemy moves onto the same node" (TG 958–983) / Extended: keeps the official rule and makes "Enemies can also trigger traps and are affected by them" a special rule of single encounters (Ext 223–230, 1013–1015), which shows the default / Hollowed: "Resolve traps when a player moves onto that node" (Hol 370–375) / online: the publisher's backer update describes traps as a memory test for the players, 11 of the 20 tokens blank, turned face down again so that the party must remember them (search summary); Guide: silent on enemies. Src 05 said "resolve its effect on all models on that node", the only text anywhere that reaches enemies.
- Ruling: CONFIRM as written
- Why: Every ruleset agrees, and the trap is a knowledge game for the party: if enemies revealed tokens, their movement would hand the party the information for nothing, and if they suffered damage the party would herd them onto unknown nodes, which is clever but adds an enemy dodge rule the game does not have. One sentence, no exception, is the simple rule.
- Mechanical: no
- Edits: none

### combat-002 · Lead 16 · frostbite duration
- Question: Is frostbite removed at the end of the model's turn, or, as stagger is after Gate 1 OQ-16, at the end of its next complete turn?
- This book now: Frostbite and stagger are both removed at the end of the affected model's next complete turn; a token placed during the model's own turn stays until the end of its following turn (§8.5).
- Evidence: official 2017: poison, frostbite and stagger are all removed "when a model ends its activation" (Core 968–971) / official 2022: frostbite and stagger carry the identical sentence, "At the end of a model's turn ... the token is discarded" (TG 1489–1512) / Extended: silent / Hollowed: stagger and frostbite both "removed at the end of an activation" (Hol 488–498) / Src 08: both "removed at the end of the model's turn" / online: Guide repeats the official sentence. Audit finding A-078 (REQUIRED) named "a stagger or frostbite token" together.
- Ruling: CONFIRM as written
- Why: In every source the two conditions share one duration; Gate 1 moved stagger, and leaving frostbite behind would make this the only ruleset in which they differ. The two rules differ in play only when frostbite is placed during the affected model's own turn (a riposte with a frostbite weapon against an enemy, an invader, a boss, or in PvP the attacker), and there the aligned rule is the only one under which the token does anything at all. One duration for both is also one fewer thing to remember.
- Mechanical: no
- Edits: none (see combat-072 for the one sentence that states the shared clock)

## Chapter 05 — tiles and nodes

### combat-003 · Ch 05 · traps and enemies
- Question: Which of the two approved findings governs: enemies suffer trap damage without rolling (A-083), or enemies neither trigger nor suffer traps (D-009)?
- This book now: D-009: enemies neither trigger nor suffer traps (§5.5, Traps).
- Evidence: as combat-001.
- Ruling: CONFIRM as written
- Why: As combat-001. A-083's own alternative was this rule.
- Mechanical: no
- Edits: none

### combat-004 · Ch 05 · summons, invaders and traps
- Question: Does a summon or an invader trigger or suffer a trap?
- This book now: No; only characters do (§5.5, Traps; §12.1).
- Evidence: official 2017 and 2022: traps name characters and enemies only (Core 818–826; TG 965–983); the Phantoms booklet is silent on traps / Extended: silent / Hollowed: "when a player moves onto that node" (Hol 373–375) / online: silent.
- Ruling: CONFIRM as written
- Why: "Only characters" needs no list of exceptions. An invader is hostile and behaves as an enemy. A summon is called only for a boss encounter (§12.1), and no trap tokens are dealt to a boss tile (§15.3), so the summon half of the question never arises unless a boss rule places traps; the general sentence already answers it.
- Mechanical: no
- Edits: none

### combat-005 · Ch 05 · scry count per encounter
- Question: Do two gravestones on one tile grant one scry or two when the encounter is cleared?
- This book now: One scry per cleared encounter, "however many gravestones the tile holds" (§5.5, Gravestones; §7.5, Encounter Resolution step 5; glossary Gravestone).
- Evidence: official 2017: "the party gains information about the boss for each gravestone"; "Reveal one random card from the behaviour deck for each gravestone on a tile with a face-up encounter card" (Core 755–759, 1385–1386) / official 2022: each gravestone is used once by a character and then flipped (TG 952–960) / Extended: silent on the count / Hollowed: one summon charge "for each tombstone" (Hol 353–356) / online: silent. Src 05: "an encounter containing a gravestone ... may scry one card" (singular, written for the usual one-gravestone tile).
- Ruling: CHANGE
- Why: All three other rulesets pay out per gravestone, and a player who sees two tokens on the tile will guess two scries. Counting the tokens is the rule a table would assume, and it lets the "however many" clause be deleted rather than explained. The gain is small (a second look at a deck top or a second encounter card) and arises only on tiles with two gravestones.
- Mechanical: yes
- Edits: combat-E01, combat-E02, combat-E03, combat-E04

### combat-006 · Ch 05 · scried encounter card destination
- Question: Where does an encounter card go when a scry replaces it?
- This book now: Face down to the bottom of the encounter deck of its level (§7.5, Encounter Resolution).
- Evidence: official 2017: no encounter scry / official 2022: the card looked at is returned "to either the top or bottom of the deck" (TG 954–960) / Extended, Hollowed, online: silent. Src 05 names no destination.
- Ruling: CONFIRM as written
- Why: The treasure scry and the boss behaviour scry already send a rejected card to the bottom of its deck; the encounter scry now does the same. One destination for all three is the consistent answer, and the bottom keeps the rejected card from coming straight back.
- Mechanical: no
- Edits: none

### combat-007 · Ch 05 · boss behaviour deck for the scry
- Question: Is there a boss behaviour deck to scry before the boss encounter begins?
- This book now: Yes. The deck is built at setup and kept face down until the encounter; a scry may reveal its top card (§15.5; glossary Behaviour deck).
- Evidence: official 2017 builds the deck at the start of the boss encounter and reveals cards per gravestone then (Core 1380–1388) / official 2022: the gravestone looks at a deck top (TG 954–960) / others: silent.
- Ruling: CONFIRM as written
- Why: The dependency the issue names is met in §15.5 and the glossary. Building the deck early is what makes the scry possible, and a deck rebuilt after a failed attempt discards what the party learned, which is the right price for failing.
- Mechanical: no
- Edits: none

### combat-008 · Ch 05 · trap dealing exclusion
- Question: Are trap tokens kept off the basic nodes along a tile edge that adjoins another tile (the manuscript), or off those along any wall with a doorway (official)?
- This book now: Off the basic nodes along a tile edge that adjoins another tile (§5.5, Traps, step 2).
- Evidence: official 2017: "excluding any basic nodes that are along a wall that has a doorway" (Core 812–817, example 847–851) / official 2022: excludes character start, enemy spawn, terrain and doorway nodes (TG 958–963) / Hollowed: "excluding edges with a connected doorway" (Hol 371–374), the manuscript's meaning / Extended, online: silent.
- Ruling: CONFIRM as written
- Why: In this book no model crosses a doorway during an encounter (§5.2), so the only nodes that must be free of traps are those on which characters are placed. Every edge that adjoins another tile is a possible entry edge; a doorway that leads nowhere is not, and a few more traps there cost nothing. The manuscript's wording is the functionally exact one and matches the Hollowed lineage.
- Mechanical: no
- Edits: none

### combat-009 · Ch 05 · trap token faces in §2.8
- Question: Does §2.8 describe a trap token as §5.5 does (blank, or a dodge difficulty and a damage value)?
- This book now: §5.5 and the glossary describe the faces; §2.8 says only where the tokens are dealt and cites §5.5.
- Evidence: official 2017: blank, or damage with a dodge (Core 818–822) / official 2022: "a dodge and damage value" (TG 968–981) / online: backer update, 11 blank and 9 with values (search summary, not verified against the components).
- Ruling: NOT A RULES QUESTION
- Why: Nothing in §2.8 contradicts §5.5. The mix of tokens is a component fact and is listed under (b) at the end of this memo.
- Mechanical: no
- Edits: none

### combat-010 · Ch 05 · entry node definition
- Question: Which nodes are entry nodes, and do §5.1, §6.7, §7.5, §15.3 and the glossary agree?
- This book now: §5.1: "A basic node adjacent to a doorway" (any doorway). Glossary: "A basic node beside the doorway through which the characters entered". Glossary Basic node and Doorway each give a third and fourth wording. §6.7 and §15.3 speak of nodes "along the wall beside the doorway" and "adjacent to the doorway".
- Evidence: official 2017: "All basic nodes that are adjacent to doorways are entry nodes"; the example places the characters "on any node along the bottom edge of the tile" (Core 415–422, 853–855) / official 2022: character start nodes are printed on the encounter card (TG 905–907) / Src 07: "the basic nodes along the wall adjacent to the previous encounter tile" / others: silent.
- Ruling: CHANGE
- Why: A node cannot be adjacent to a doorway, because a doorway is not a node (§5.1), so the present wording does not say which nodes are meant. The official example and the author's own Encounter Start both mean every basic node along the edge the party came in by. One definition, tied to the doorway actually used, serves every rule that needs the term (placement, the order of trap dealing, the boss's starting facing). No play changes.
- Mechanical: no
- Edits: combat-E05, combat-E06, combat-E07, combat-E08

### combat-011 · Ch 05 · main-boss tile adjacency
- Question: Are nodes across the join of the two boss tiles adjacent?
- This book now: Yes; the joined tiles are one tile, with no wall along the join (§5.1; §15.3).
- Evidence: official 2017 treats the main boss tile as one tile (Core 284–289) / others: silent.
- Ruling: CONFIRM as written
- Why: §15.3 states the join in the same words as §5.1, so the dependency is met. See combat-075 for range across the join.
- Mechanical: no
- Edits: none

### combat-012 · Ch 05 · tile boundary during an encounter
- Question: May any model leave the tile or pass through a doorway during an encounter, and is the rule stated once?
- This book now: No model may; §5.2 owns the rule, and §9.2, §10.2, §12.2 and §20.3 each give one sentence with a citation.
- Evidence: official 2017: the party "cannot leave the encounter until either the party or the encounter is defeated" (Core 878–880) / official 2022: models move between tiles through doorway nodes, and attacks cannot cross tiles (TG 889–893, 918–919) / Hollowed, Extended: as 2017 / online: the Guide records the 2022 multi-tile rule as a known source of exploits (enemies chasing across tiles "not attacking").
- Ruling: CONFIRM as written
- Why: One tile per encounter is the simpler game and avoids the multi-tile exploits the community documents for the 2022 rules. The one-sentence reminders in §9.2 and §10.2 cite §5.2 and do not restate it. §12.2 already places the invader "directly on its node".
- Mechanical: no
- Edits: none

### combat-013 · Ch 05 · overcrowding push in the glossary
- Question: Does the push rule list the node model limit as a cause of a push?
- This book now: Yes: §8.4 and glossary Push both list it, with the two-boss displacement.
- Evidence: official 2017: "the players must push one of the three models already on the node" (Core 427–433) / official 2022: "place it on an adjacent node" (TG 928–930) / Hollowed: monsters push monsters, otherwise the lowest-threat player (Hol 446–451).
- Ruling: CONFIRM as written
- Why: The dependency is met. The list of causes is still one short (a leap also pushes); that is corrected under combat-074.
- Mechanical: no
- Edits: none (see combat-074)

### combat-014 · Ch 05 · enemy pathing around terrain
- Question: What does an enemy or boss do when the node its icon points to is not a valid node?
- This book now: It follows the shortest path of valid nodes; if no path exists it does not move (§9.2, Paths; §16.2).
- Evidence: official 2017: "When two different nodes would take an enemy closer ... the players can choose" and nothing on blocked nodes (Core 1118–1125) / official 2022: the same (TG 1636–1638) / others: silent.
- Ruling: CONFIRM as written
- Why: The dependency is met, and the path rule is better than the official step-by-step "closer" rule, under which an enemy directly behind a gravestone has no closer node and stalls. See combat-045 for the unreachable target.
- Mechanical: no
- Edits: none

### combat-015 · Ch 05 · chest opening step
- Question: Does §7.7 state the opening of a chest, the tie-break and the pre-dealt card?
- This book now: Yes (§7.5, Encounter Resolution step 4; §7.7).
- Evidence: official 2017: open on defeating the encounter, draw two cards (Core 780–801) / official 2022: an adjacent character spends an action (TG 943–954) / Gate 1 OQ-11 and OQ-29.
- Ruling: CONFIRM as written
- Why: The dependency is met; nothing in §5.5 needs to change.
- Mechanical: no
- Edits: none

### combat-016 · Ch 05 · primary and secondary node icons
- Question: Do the rules need to mention that spawn nodes and terrain nodes come in a primary and a secondary kind?
- This book now: §5.1 attaches the primary icons to "spawn node" and "terrain node" and does not mention the secondary kind.
- Evidence: official 2017 symbol key: "Primary spawn node", "Secondary spawn node", "Primary terrain node", "Secondary terrain node" (Core 1830–1842); the setup example reads the card node by node (Core 836–845) / others: silent.
- Ruling: ADD
- Why: No rule treats the two kinds differently, but an encounter card cannot be read without knowing that the two icons name two different nodes of the tile. Two sentences close the gap and say outright that the difference has no other effect. Layout must still confirm the two extra icon tokens.
- Mechanical: no
- Edits: combat-E09

## Chapter 08 — combat basics

### combat-017 · Ch 08 · frostbite duration
- Question: Is the frostbite half of the "next complete turn" rule confirmed?
- This book now: As combat-002.
- Evidence: as combat-002.
- Ruling: CONFIRM as written
- Why: As combat-002.
- Mechanical: no
- Edits: none

### combat-018 · Ch 08 · conditions on bosses
- Question: May a boss hold condition tokens, so that a second bleed token deals three damage to it?
- This book now: Any model may hold condition tokens: a character, an enemy, a boss or a phantom (§8.5; §16.1).
- Evidence: official 2017: the token goes on "the model (or models) hit by that attack", with no boss exception (Core 963–971) / official 2022: the same (TG 1463–1471) / Extended: no boss immunity stated; its weapon arts place conditions on "the target enemy" without distinction (Ext 1114–1202) / Hollowed: no boss exception (Hol 464–515) / online: Guide lists no boss immunity.
- Ruling: CONFIRM as written
- Why: No source exempts bosses, and an exemption would be a special case to remember. This book's bleed is also the weaker of the two against a boss: three damage for every two bleed hits, where the official rule adds two for every bleed hit that is followed by any damage. Stagger, frostbite and poison all have defined effects on a boss through §8.5.
- Mechanical: no
- Edits: none

### combat-019 · Ch 08 · staggered enemy values floor
- Question: Do the values that stagger reduces on an enemy stop at zero?
- This book now: Yes: "A value reduced by a condition cannot fall below zero" (§8.5).
- Evidence: official 2017 and 2022: an enemy's attack values are reduced by one, no floor stated (Core 1005–1009; TG 1504–1509) / Hollowed: "damage values lowered by one" (Hol 488–491) / Src 08: "subtract one from attack, block, resist, and dodge".
- Ruling: CONFIRM as written
- Why: A negative block would add damage and a negative dodge difficulty means nothing; zero is the reading every table would reach. A dodge difficulty reduced to zero still costs the one stamina of the dodge (§9.5), so the floor creates no free defence.
- Mechanical: no
- Edits: none

### combat-020 · Ch 08 · condition damage, embers and aggro
- Question: Does the embered reduction apply to bleed and poison damage, and does condition damage count when the aggro token is assigned?
- This book now: Bleed and poison damage are "not an attack", so the embered reduction (three or more damage "from a single attack", §7.3) does not apply (§8.5; §22.3). Nothing says whether condition damage counts towards the aggro token (§7.5; §16.4).
- Evidence: official 2017 and 2022: no ember reduction exists; aggro passes to each character as their turn starts (Core 1017–1020; TG 1412–1416) / Hollowed: embered reduces "3 or more damage in a single hit"; bleed is "3 damage unaffected by armor" (Hol 303–306, 476–480) / Extended, online: silent.
- Ruling: ADD
- Why: The first half is confirmed: "condition damage is never reduced by anything" is one rule, and it keeps bleed worth its two hits. The second half is a real hole, closed by when the damage is recorded: bleed is triggered by a character's attack and is recorded during that attack, so it counts for that character; poison is recorded at the end of the enemy's own turn, when no character is acting, so it counts for nobody. No new tracking is needed.
- Mechanical: no
- Edits: combat-E17

### combat-021 · Ch 08 · push direction
- Question: Is a pushed model sent to the node most directly opposite the attacker (the manuscript), or to any farther node the players choose (official)?
- This book now: To the valid node most directly opposite the attacker, taken from the adjacent nodes farther from the attacker by range; the players choose only among nodes equally opposite; no farther valid node, no push; attacker on the same node, any valid node (§8.4).
- Evidence: official 2017: "an adjacent node that is farther from the attacking model. If there are multiple nodes ... the players choose" (Core 973–978) / official 2022: "further away from the source of the push. If there are multiple equidistant nodes, the players choose" (TG 1489–1494) / FAQ: a pushed character "simply needs to be moved farther from the attacking model" (FAQ 22–37) / Hollowed: "it must move in a logical direction away from the source of the push. If the push originates on the same node ... the player may choose freely" (Hol 452–456) / Src 08: "most directly opposite" / online: Guide and the fan summary restate the official rule; nothing found on corners.
- Ruling: CONFIRM as written
- Why: A push that goes straight back is what a player expects a push to be, and it makes position matter before the blow lands: a character can be driven onto a trap or off a target, and a character can aim an enemy. The official free choice turns every push into a small gift to the players. The cost is one judgement of "most opposite", and the rule already hands ties to the players. The corner case is the same under either rule, since both require a farther node.
- Mechanical: no
- Edits: none

### combat-022 · Ch 08 · push-move damage ownership
- Question: Does §8.4 own the damage of a push-move, with §9.2 and §9.3 citing it?
- This book now: Yes. §8.4 holds the four steps; §9.2 describes the icon and cites §8.4; §9.3 owns the target icons, the tie-breaks and the out-of-range miss.
- Evidence: official 2017: push rule in Combat Basics, movement attack in Enemy Attacks (Core 981–989, 1196–1210) / official 2022: Pushes, then "Enemy Attacks During Movement" (TG 1480–1498, 1884–1892).
- Ruling: CONFIRM as written
- Why: The split is the one the issue asked for and the two sections agree. See combat-037 for the one clause tightened in §8.4.
- Mechanical: no
- Edits: none

### combat-023 · Ch 08 · repeat icon on enemy data cards
- Question: What does a repeat icon printed on an enemy data card repeat: the attack beside it, or the whole row of icons?
- This book now: The attack beside it only, "not a movement icon" (§8.2; §9.3). A boss's behaviour card repeats the whole row (§16.1 step 4), and the glossary says a repeat icon repeats "an entire attack option or behaviour card".
- Evidence: official 2017: with the repeat icon "the enemy will perform its entire behaviour multiple times" (Core 1441–1444); symbol key "Repeat behaviour or attack" (Core 1898) / official 2022: "resolves their entire row of behaviour symbols the number of times shown" (TG 2256–2264) / Extended, Hollowed: silent / online: Guide: each repetition "is a separate action, and its targets are resolved from scratch". The attack-only wording came from finding B-005, written for the manuscript's rule that added Repeat 2 to every enemy at four players, which Gate 1 OQ-07 deleted.
- Ruling: CHANGE
- Why: The special case outlived its purpose: no rule of this book now adds a repeat icon to an enemy, so the only repeat icons left are printed ones, and both official rulebooks and this book's own §16.1 and glossary read a printed icon as the whole row. One meaning for the icon wherever it is printed on a data card or behaviour card is the consistent rule. No enemy data card in the supplied sets is known to print the icon, so the change is one of principle.
- Mechanical: yes
- Edits: combat-E12, combat-E18, combat-E19, combat-E36

### combat-024 · Ch 08 · dodge and push
- Question: Does the movement of a dodge happen before or after the roll, and from which node is a failed dodger pushed?
- This book now: Only a successful dodge moves the character, after the roll and compulsorily; a failed dodge moves nobody, so a push is resolved from the node the character occupies (§9.5; §8.4).
- Evidence: official 2017: the character "must spend 1 Stamina and can move 1 node" before rolling (Core 1217–1226); FAQ: after a failed dodge the push starts "from the node they occupied after their dodge move" (FAQ 12–34) / official 2022: only after a successful dodge may the target "spend 1 stamina to move one node" (TG 1680–1683) / Hollowed: "Dodging works as normal" (Hol 440–443) / Src 09: on success "The character must move to an adjacent node" / online: Guide: 2017 chooses the node before rolling, 2022 after rolling and only on success.
- Ruling: CONFIRM as written
- Why: The book follows the current official timing and the author's "must". Moving only on success is the cleaner story (the roll decides whether the character got clear) and removes the official FAQ's failed-dodge-then-push case entirely. The compulsory move is a real cost that keeps the dodge from being a free block.
- Mechanical: no
- Edits: none

### combat-025 · Ch 08 · summons and push-moves
- Question: Is a summon on the path of a push-move pushed and attacked as a character?
- This book now: A boss's behaviours treat a summon as a character; a summon that is hit is pushed and receives conditions as a character does (§12.1). Enemies outside boss encounters never meet a summon.
- Evidence: official Phantoms booklet: silent on push-moves / others: silent.
- Ruling: CONFIRM as written
- Why: "Treat a summon as a character" covers the push-move without a line of its own, and summons exist only in boss encounters, where §16.2 owns the push-move.
- Mechanical: no
- Edits: none

### combat-026 · Ch 08 · scaling exemptions
- Question: Are bosses, mimics, phantoms and crystal lizards exempt from enemy scaling and from the bonfire ascetic?
- This book now: Yes, in §8.3, §12.1, §12.2, §13, §14, §15.4, §16.2, §16.3 and §18.7, all in agreement; §18.4 states from when a new number of characters counts.
- Evidence: official: no enemy scaling exists / Src 08: "Boss enemies ... do NOT modify their base health or receive scaling benefits" / finding A-028.
- Ruling: CONFIRM as written
- Why: The four exempt models each have a health dial or a deck of their own and were costed without scaling; a scaled crystal lizard would move two nodes and end the chase. Every chapter the issue names already agrees. See combat-078 for the table itself.
- Mechanical: no
- Edits: none

### combat-027 · Ch 08 · cross-chapter dependencies
- Question: Are the rules that §8 hands to other sections stated there?
- This book now: Checked and present: stamina overflow and the second stagger token (§3.4; §10.1; §8.5 general rule); frostbite and Rest (§10.1); the parry's stagger (§9.6); the damage calculation (§10.3); the boss data card (§15.4); the arc limit on pushes and boss push-moves (§15.6; §16.2); the two-boss push (§17.1); pushes and conditions between characters (§20.5).
- Evidence: this book only.
- Ruling: NOT A RULES QUESTION
- Why: A list of hand-offs, all met. The attacks that place calamity and corrosion (§17.8; §17.10) belong to the boss cluster and were not checked here.
- Mechanical: no
- Edits: none

### combat-028 · Ch 08 · wound token values in §7.5
- Question: Do the two rules in §7.5 that count wound tokens mean their number or their total value?
- This book now: §8.2 and §10.3 count total value. §7.5 breaks an enemy tie by "the most wound tokens" and moves the aggro token "counting wound tokens placed".
- Evidence: official 2017: one wound token per point of damage (Core 952–957) / this book §2.8: tokens of value 1, 3 and 5.
- Ruling: CHANGE
- Why: With tokens of three values, a count of tokens is not a measure of damage: an enemy with one token of value 5 would rank below one with two tokens of value 1. Both sentences must say total value, as §8.2 does.
- Mechanical: no
- Edits: combat-E31, combat-E32

### combat-029 · Ch 08 · glossary entry Attack value
- Question: Does the glossary cover the damage value of a push-move and the stagger reduction as parts of an enemy's attack value?
- This book now: The entry gives "the fixed number printed in the attack icon, scaled for the number of characters" and no more.
- Evidence: this book §8.3 ("the damage value of a push-move"), §8.4 step 3 ("with that attack value"), §8.5, Stagger.
- Ruling: CHANGE
- Why: Three sections treat the push-move's damage value as an attack value and the glossary did not; the entry is brought into line.
- Mechanical: no
- Edits: combat-E42

### combat-030 · Ch 08 · example values
- Question: Are the Hollow Soldier values used in the examples (base health 1, movement 1, attack value 4, block 1) the printed ones?
- This book now: The examples use those values; other examples say "an enemy".
- Evidence: the supplied texts carry the rulebook pages but not the data card images, so the values cannot be read from them.
- Ruling: NOT A RULES QUESTION
- Why: A proof check against the physical cards; listed under (b). No example needs changing as a result of any ruling in this memo.
- Mechanical: no
- Edits: none

### combat-031 · Ch 08 · icon slugs
- Question: Are the icon tokens for the push icon, the skull icon, the node icon and the two expansion conditions right?
- This book now: As the issue describes.
- Evidence: the icon list of the drafting brief.
- Ruling: NOT A RULES QUESTION
- Why: A layout matter.
- Mechanical: no
- Edits: none

### combat-032 · Ch 08 · poison token supply
- Question: Is the number of poison tokens a model may hold limited by the tokens supplied?
- This book now: No limit (§8.5, Poison); finding A-081 (OPTIONAL) was not applied.
- Evidence: official 2017 and 2022: one poison token per model (Core 965–968; TG 1469–1470) / Hollowed: "Poison can stack indefinitely" (Hol 482–486) / Gate 1 OQ-13.
- Ruling: CONFIRM as written
- Why: A rule that depends on how many pieces are in the box is a rule nobody remembers. Gate 1 already made poison clear itself every turn, so stacks stay small, and any marker stands in if the tokens run short.
- Mechanical: no
- Edits: none

## Chapter 09 — enemy turn

### combat-033 · Ch 09 · nearest-character tie-break
- Question: When characters are tied for nearest, is the tie broken by rule or by the players' free choice?
- This book now: The tied character who holds the aggro token; otherwise the tied character with the highest threat; otherwise the players choose (§9.2; §9.3; glossary Nearest character).
- Evidence: official 2017: aggro token, then "the higher Taunt level" (Core 1136–1144, 1173–1179) / official 2022: the same (TG 1613–1617) / Hollowed: enemy behaviour as official / Src 09: the same two steps / online: Guide: the aggro token "acts as a tie-breaker".
- Ruling: CONFIRM as written
- Why: Both official editions and the manuscript use the same deterministic order, and a rule that tells the players whom the enemy attacks is what makes the aggro token and the threat value worth holding. The free choice is right only as the last step, where nothing else separates the characters.
- Mechanical: no
- Edits: none

### combat-034 · Ch 09 · B-002 and B-033 left unapplied
- Question: Does a shield raise the block limit to the three highest dice (B-002), and does the extra dodge die cost one stamina in place of two (B-033)?
- This book now: Neither. The defence total is the two highest dice (§9.4); the extra green die costs two further stamina (§9.5).
- Evidence: official 2017 and 2022: every block die is added, and no stamina buys a dodge die (Core 1182–1193; TG 1671–1693) / Hollowed: "Choose any two rolled dice" (Hol 433–438) / Extended: a block total above the attack costs stamina (Ext 62–67) / Src 09: two highest dice; two additional stamina for one die / online: silent.
- Ruling: CONFIRM as written
- Why: B-002 was a remedy for the manuscript's +1 attack at three players and Repeat 2 at four; Gate 1 removed both, so the pressure it answered is gone, and "three dice with a shield" is a special case. At one stamina the extra die would be bought by every dodging character every time, which is a tax, not a decision; at two it is dear enough to be weighed against the one stamina a turn the character recovers.
- Mechanical: no
- Edits: none

### combat-035 · Ch 09 · parry slot
- Question: Must the shield be in the left weapon slot and the riposte weapon in the right, or may the shield be in either slot?
- This book now: Left slot only; "A shield in the right weapon slot does not permit a parry"; the riposte uses the weapon in the right slot (§9.6; §3.2; glossary Parry, Riposte; §22.1; §22.2).
- Evidence: official 2017 and 2022: no parry; the dashboard has a left-hand and a right-hand slot with no rule attached (Core 1017–1022; TG 1417–1419) / Extended: no parry rule; a "Parrying Dagger" weapon art only (Ext 1273) / Hollowed: no parry / Src 09: "a shield as their left weapon"; "the weapon equipped to the right weapon slot" / online: house-rule threads let other weapons parry (search snippet); none found with a left-hand rule. Finding A-068 (approved, REQUIRED) proposed a shield in one slot and the riposte weapon in the other.
- Ruling: CHANGE
- Why: The parry is the only rule in the whole book that depends on which of the two weapon slots holds a card (a search of every chapter confirms it). The player loses nothing by putting the shield on the left, so the requirement is not a decision, only a way to be caught out, and it already costs the book a negative clause and an F.A.Q. entry. A shield in either slot, the riposte from the other, is the same parry with nothing to remember. The examples, which have the shield on the left, stay correct.
- Mechanical: yes
- Edits: combat-E22, combat-E23, combat-E24, combat-E25, combat-E30, combat-E34, combat-E39, combat-E40

### combat-036 · Ch 09 · riposte with a spell
- Question: May a riposte be made with a spell equipped in the weapon slot, or with a spell stored in a catalyst there?
- This book now: The riposte uses "one attack option of the weapon" in the slot; a spell is not a weapon (§4.1), so by implication it cannot (§9.6).
- Evidence: official, Extended, Hollowed: no riposte / Src 09: "the weapon equipped to the right weapon slot" / online: silent.
- Ruling: CONFIRM as written
- Why: A riposte is a quick counter with the weapon in hand. Letting spells riposte would raise three further questions (the one-spell-per-turn limit on another model's turn, upgrade spells, the choice among stored spells) for no gain in play. The exclusion was only implied by the word "weapon", so combat-E24 states it in one sentence; a catalyst's own printed attack option remains a weapon's attack option and may be used.
- Mechanical: no
- Edits: none (the sentence is part of combat-E24, under combat-035)

### combat-037 · Ch 09 · push steps in §8.4 and §9.2
- Question: Which section owns the push-move, and do the two agree?
- This book now: §8.4 owns the steps; §9.2 defines the icon, fixes the target before any push, and cites §8.4. Two statements are made only in §9.2: the attack of a push-move cannot be parried, and a character pushed onto a node the enemy enters next is attacked again. §8.4 says that attack "is defended as any other enemy attack".
- Evidence: official 2017: movement attacks are opposed "with a block or dodge roll"; the same character may be attacked several times; the start node is not attacked (Core 1196–1210; FAQ 36–48) / official 2022: characters pushed at the start are attacked too (TG 1627–1631, 1884–1892) / online: Guide notes the 2017 and 2022 rules disagree on the first push.
- Ruling: CHANGE
- Why: Ownership is confirmed as it stands: one procedure in §8.4, cited from §9.2. The book rightly follows the 2017 rule and the official F.A.Q. (no attack on the node the enemy starts from), which is the fairer of the two. The only fault is the phrase "as any other enemy attack", which invites a parry that §9.2 and §9.6 forbid; one clause is tightened.
- Mechanical: no
- Edits: combat-E15

### combat-038 · Ch 09 · push-move damage and scaling
- Question: Is the damage value of a push-move scaled as an attack value is?
- This book now: Yes: +1 with four characters (§8.3; §9.2; §22.2).
- Evidence: official: no scaling / finding A-025.
- Ruling: CONFIRM as written
- Why: The damage value is an attack value in every other respect (§8.4 step 3), so it scales with the rest. Three places agree.
- Mechanical: no
- Edits: none

### combat-039 · Ch 09 · repeat icon in §9.3
- Question: Do §8.2 and §9.3 agree on the repeat icon, and is "the target is determined afresh each time" sound?
- This book now: Both limit it to the attack beside it; §9.3 redetermines the target each time.
- Evidence: as combat-023.
- Ruling: CHANGE
- Why: As combat-023: the icon repeats the whole row, as on a boss's behaviour card. Redetermining the target is kept, and needs no rule of its own, because every icon's target is determined when that icon is resolved.
- Mechanical: yes
- Edits: combat-E12, combat-E18, combat-E19, combat-E36 (the same four edits as combat-023)

### combat-040 · Ch 09 · stagger citations
- Question: Do §9.3 and §9.6 agree with §8.5 on the effect and duration of stagger?
- This book now: Yes; both cite §8.5, and the first parry example (block 1 reduced to 0) computes correctly.
- Evidence: this book only.
- Ruling: NOT A RULES QUESTION
- Why: A consistency note, checked.
- Mechanical: no
- Edits: none

### combat-041 · Ch 09 · fixed defence modifiers
- Question: Are fixed modifiers applied after the two highest dice whether or not their card's die is among the two, and is a negative defence total zero?
- This book now: Yes to both (§9.4 steps 4 and 5; glossary Defence total).
- Evidence: official 2022: modifiers "add or subtract a value from the damage total" of an attack (TG 1459–1462); nothing on defence / official 2017: equipment modifiers named, no order (Core contents, "Equipment Modifiers" p. 12) / Hollowed: two dice chosen, modifiers not mentioned (Hol 433–438) / findings D-033, A-120.
- Ruling: CONFIRM as written
- Why: The alternative, a modifier that counts only when its own card's die is kept, would make players remember which die came from which card. "Two highest dice, then every modifier" is one sentence and matches how §10.3 treats an attack's modifier. The floor of zero mirrors the floor on the attack value.
- Mechanical: no
- Edits: none

### combat-042 · Ch 09 · failed dodge and armour upgrades
- Question: After a failed dodge, are the dice of upgrade cards attached to the armour rolled with it?
- This book now: Yes (§9.5, Failed Dodge; §22.2).
- Evidence: Hollowed: "using only the dice listed on their armor, and not weapons and shields" (Hol 440–443) / Src 09: "provided by the character's currently equipped armour" / official: no such roll.
- Ruling: CONFIRM as written
- Why: §3.2 makes an attached upgrade part of its card. Treating it as part of the armour here needs no new rule, and excluding it would need one.
- Mechanical: no
- Edits: none

### combat-043 · Ch 09 · dodge and parry with a full bar
- Question: May a character with no empty space for the stamina cube dodge or parry, and what happens at a trap?
- This book now: No; such a character cannot choose either defence, and at a trap suffers the damage (§9.5; §9.6; §3.4; §10.1). In PvP the character dies at a trap (§20.6).
- Evidence: official 2017: a full bar of any cubes kills (Core 935–936) / Hollowed: "Players cannot use moves that require more stamina than they have empty slots" (Hol 313–317) / Src 03: "A character may never elect to spend excess stamina".
- Ruling: CONFIRM as written
- Why: It is the stamina rule applied without exception: stamina is spent only into empty spaces. A character who has spent everything has chosen to stand and block.
- Mechanical: no
- Edits: none

### combat-044 · Ch 09 · "do nothing" as a defence
- Question: Is doing nothing a fourth defence?
- This book now: §9.3 lists three defences and omits it. §20.4 keeps "The defender may decline to defend."
- Evidence: Src 09: "block, resist, dodge, parry, or do nothing" / official 2017: block or dodge (Core 1203–1209) / Extended: players "may decline to roll any number of dice" because over-blocking costs stamina there (Ext 62–67), a reason this book does not have.
- Ruling: DELETE
- Why: A block or resist costs nothing and, with or without dice, is never worse than no defence, so the fourth option is never taken; listing it only invites the question of what it is for. §9.3's omission is confirmed, and the leftover sentence in §20.4 is deleted so that the two lists match.
- Mechanical: no
- Edits: combat-E33

### combat-045 · Ch 09 · unreachable target
- Question: Does an enemy with no path of valid nodes to its target stay where it is, or move as near as it is able?
- This book now: It does not move (§9.2, Paths).
- Evidence: official 2017 and 2022: silent on blocked paths (Core 1118–1125; TG 1619–1638) / others: silent.
- Ruling: CONFIRM as written
- Why: On a standard tile the case all but cannot occur: the least connected node, a corner, has three neighbours, the symbol key gives a tile only a primary and a secondary terrain node, and a full node is still a valid node. It can arise only on the larger boards. "As near as it is able" would need a second measure of nearness for a case that is almost never met; standing still is definite and is what the players would do with the model.
- Mechanical: no
- Edits: none

### combat-046 · Ch 09 · summons as enemy targets
- Question: May an enemy target a summon?
- This book now: Enemies target only characters (§9.1); a boss's behaviours treat a summon as a character (§12.1; §16.2; §16.3); no invader and no summon share an encounter (§22.6).
- Evidence: official Phantoms booklet: summons join boss encounters / others: silent.
- Ruling: CONFIRM as written
- Why: Summons appear only where bosses do, and the boss chapters already say how a summon is targeted. §9.1 needs no exception.
- Mechanical: no
- Edits: none

### combat-047 · Ch 09 · hand-offs to the boss chapters
- Question: Do §15.6 and §16 state which boss attacks may be parried and what a riposte does to the aggro token and the heat-up?
- This book now: §15.6, Defence: a boss attack on one character may be parried; area attacks, node attacks and push-attacks cannot. §16.4: a riposte that damages the boss moves the aggro token at the end of that boss turn. §16.1: a heat-up or a defeat during the boss's own turn.
- Evidence: this book only.
- Ruling: NOT A RULES QUESTION
- Why: The hand-offs are met.
- Mechanical: no
- Edits: none

### combat-048 · Ch 09 · riposte in player versus player
- Question: How is a riposte against a character defended?
- This book now: The target may block, resist or dodge it but cannot parry it (§20.4); §9.6 states the rule for enemies and cites §20.4.
- Evidence: no source has PvP parries.
- Ruling: CONFIRM as written
- Why: "A riposte cannot be parried" holds in both settings and stops a chain of parries; everything else follows the ordinary PvP defence.
- Mechanical: no
- Edits: none

### combat-049 · Ch 09 · icon names
- Question: Are the damage icons named the same way in the chapters and the glossary?
- This book now: §4.3, §8.2, §9.3 and §10.3 say "the magical damage icon"; the glossary says "the white circle icon". The glossary also ties physical damage to "the crossed swords icon", which a character's attack option does not show.
- Evidence: official 2017 and 2022 symbol keys name the icon by its function (Core 1066–1067; TG 1533–1535).
- Ruling: CHANGE
- Why: A wording matter with one rules consequence: under the glossary's sentence a weapon attack, which shows no crossed swords, has no stated damage type. Both entries are brought into line with §10.3. The icon tokens themselves are for layout.
- Mechanical: no
- Edits: combat-E43, combat-E44

### combat-050 · Ch 09 · where dodge difficulty is defined
- Question: Is §9.5 the right owner of the term?
- This book now: Defined in §9.5; listed on the data card in §8.2 with a citation.
- Evidence: this book only.
- Ruling: NOT A RULES QUESTION
- Why: The dodge, the parry and the trap all use the value, and §9.5 is the first of them. No change.
- Mechanical: no
- Edits: none

### combat-051 · Ch 09 · glossary lines for push-attack and push-move
- Question: Do the two glossary entries match §8.4?
- This book now: They do.
- Evidence: this book only.
- Ruling: NOT A RULES QUESTION
- Why: A merge note from drafting; the merged glossary is consistent.
- Mechanical: no
- Edits: none

### combat-052 · Ch 09 · named enemies in examples
- Question: Are the examples safe from being read as printed card data?
- This book now: Named enemies appear only with the Hollow Soldier values of §8.3; the rest say "an enemy".
- Evidence: as combat-030.
- Ruling: NOT A RULES QUESTION
- Why: A proof matter, listed under (b).
- Mechanical: no
- Edits: none

## Chapter 10 — character turn

### combat-053 · Ch 10 · scaling requirement
- Question: Is a weapon's scaling judged against the highest of the four requirements printed on the card, with upgrade cards left out?
- This book now: Yes (§10.5; glossary Relevant stat, Scaled (weapon)); Appendix A values replace the printed ones (glossary Stat requirement).
- Evidence: official, Extended, Hollowed: no stat scaling (Extended's "gear match" is a different mechanic, Ext 54–67) / Src 10: "exceeds an equipment's highest stat requirement" / Gate 1 OQ-19 (five or more).
- Ruling: CONFIRM as written
- Why: Requirements are printed per card, so the card is the only thing the rule can read. Counting upgrade requirements would make a weapon gain or lose its bonus when a gem is fitted, which is book-keeping with no decision in it.
- Mechanical: no
- Edits: none

### combat-054 · Ch 10 · weapons with no requirement
- Question: Is a weapon whose highest requirement is zero scaled for every character with a stat of five or more?
- This book now: Yes, by the letter of §10.5; finding A-066 (OPTIONAL) was not applied.
- Evidence: no other ruleset has stat scaling / Src 10: silent on the case / finding A-066: "Equipment whose highest stat requirement is zero cannot be scaled."
- Ruling: ADD
- Why: Scaling pays a character for raising a stat past what a weapon asks. A weapon that asks nothing is scaled by every character from the first turn: a permanent +1 that rewards no choice, plus a red cube to place on it. One sentence removes both, and it is the answer a player would guess (a weapon with no requirement scales with nothing).
- Mechanical: yes
- Edits: combat-E29, combat-E35, combat-E41

### combat-055 · Ch 10 · tied requirements
- Question: When two requirements are tied for the highest, which stat is compared?
- This book now: The character chooses one of the tied stats (§10.5).
- Evidence: Src 10: "If two requirements are tied, use either."
- Ruling: CONFIRM as written
- Why: It is the author's rule in the book's words, and it favours the character without any further test.
- Mechanical: no
- Edits: none

### combat-056 · Ch 10 · scaling marker
- Question: Is the red cube that marks a scaled weapon taken from the damage cubes?
- This book now: Yes; §2.8 lists no separate marker (§10.5; §3.3 uses the same cube for stat tier four).
- Evidence: Src 10: "mark the equipped item with a red damage cube" / Hollowed marks tier four with "a red cube" (Hol 196–200).
- Ruling: CONFIRM as written
- Why: The author named the damage cube, and the supply is ample. The cube is a reminder, not a state: the weapon is scaled whether or not it is marked.
- Mechanical: no
- Edits: none

### combat-057 · Ch 10 · two rerolls on one roll
- Question: May the two-handed reroll and the luck token both be used on one attack roll, and may one die be rerolled twice?
- This book now: Yes to both, in either order (§10.3; §10.4; §22.2).
- Evidence: official 2017: the luck token rerolls "one die in their attack, block, or dodge roll" (Core 525–531); no two-handed reroll / Src 10: "any re-rolls available to them by their luck token or otherwise" / others: silent.
- Ruling: CONFIRM as written
- Why: Each reroll is used once per roll, and nothing more needs saying. A ban on rerolling the same die twice would make players track which die had been touched, for the sake of a token that is spent once per rest.
- Mechanical: no
- Edits: none

### combat-058 · Ch 10 · actions resolved in full
- Question: May a character take a minor action between the two attacks of one Attack major action?
- This book now: No; each action is resolved in full before another begins (§10.1).
- Evidence: official 2017: move "before attacking or after attacking (but not both)" (Core 1030–1031) / official 2022: the second weapon attacks "as part of the same action", with the move before or after it (TG 1427–1431, 1440–1442) / Hollowed: "Actions can be done in any order" (Hol 400–404) / Gate 1 OQ-26.
- Ruling: CONFIRM as written
- Why: Both official editions keep the two attacks together. An undivided action is the simple rule, it leaves the shift icon as the one way to move inside an attack (which is what the icon is for), and it shuts out attacking with one weapon, taking Equip, and attacking with a third.
- Mechanical: no
- Edits: none

### combat-059 · Ch 10 · repeat on attack options
- Question: Does each resolution of a repeated attack option have its own shift, target and roll for one payment, and must every resolution be made?
- This book now: The stamina is paid once and steps 3 to 12 are resolved once "for each time shown", each with its own target (§10.3, Repeat).
- Evidence: official 2017: "use that entire weapon option the number of times indicated" (Core 1098–1103) / official 2022: "perform the attack up to the number of times shown ... The extra attacks do not have to target the same enemy, do not cost additional stamina" (TG 1566–1572) / online: Guide: stamina once; different targets allowed.
- Ruling: CHANGE
- Why: Everything in the drafted reading is confirmed by the current official text except one word: the repeats are a permission ("up to"), not a duty. That matters in this book, where damage dealt decides who takes the aggro token and a second push may send an enemy the wrong way. It also matches §10.3's own "up to one attack with each weapon".
- Mechanical: yes
- Edits: combat-E27, combat-E36

### combat-060 · Ch 10 · attack with no target
- Question: May a character pay for an attack that has no target, and what happens if none is in range when the target is to be chosen?
- This book now: The stamina is paid, then the target is chosen; "A character cannot make an attack that has no permitted target within its range" (§10.3, Range). No outcome is given if a shift before the dice ends out of range.
- Evidence: official 2017: target first, then option and payment (Core 1017–1022) / official 2022: pay, shift, then choose the target (TG 1421–1423, 1546–1549) / online: Guide: a shift may be used to move, including between tiles in the 2022 game; no ruling on a missing target.
- Ruling: ADD
- Why: The ban is confirmed: every attack has a target, which stops a free attack option with a shift from becoming a second Walk. The gap is step 4 after a shift printed before the dice: a trap entered during the shift, or the player's own choice of node, can leave nobody in range, and the procedure then has no next step. The added sentence gives the only fair outcome (the attack ends, the stamina is spent), and since it also costs that weapon its attack for the turn, it opens no exploit.
- Mechanical: no
- Edits: combat-E26

### combat-061 · Ch 10 · fixed modifiers and the floor
- Question: Is a fixed modifier applied once to the total after rerolls, and does an attack value below zero count as zero?
- This book now: Yes to both (§10.3 step 8).
- Evidence: official 2022: modifiers are applied to the damage total at step 4; "if 2 and 1 were rolled, the damage total would be 4" with +1 (TG 1459–1475) / others: silent.
- Ruling: CONFIRM as written
- Why: It is the official reading, and the floor matches the defence total in §9.4.
- Mechanical: no
- Edits: none

### combat-062 · Ch 10 · what a character may target
- Question: Do §8.1 and §10.3 give the same list of targets?
- This book now: §10.3: an enemy, a boss, an invader, a mimic or a crystal lizard. §8.1: "enemies, bosses, and invaders".
- Evidence: official 2017: characters target enemies (Core 904–912); the Explorers and Iron Keep booklets add mimics and crystal lizards as models that are attacked / this book §13 and §14.
- Ruling: CHANGE
- Why: Two lists for one rule; §8.1 is brought up to §10.3. Nothing in play changes.
- Mechanical: no
- Edits: combat-E11

### combat-063 · Ch 10 · dependencies already met
- Question: If §8.5, §9.6 or §20 change, must §10 follow?
- This book now: §10.1 step 1, §10.3 step 8 and its riposte paragraph, and the parry sentence of §10.4 rest on those sections.
- Evidence: this memo.
- Ruling: NOT A RULES QUESTION
- Why: Checked against the rulings here. The either-slot parry (combat-035) touches no sentence of chapter 10: §10.4 says only that a character wielding two-handed "has no shield equipped", which stays true.
- Mechanical: no
- Edits: none

### combat-064 · Ch 10 · dependencies then still open
- Question: Does §8.5 state every effect that step 3 of the character turn resolves, and do §12.1, §15.4 and §15.6 own what §10 cites?
- This book now: §8.5 states the poison damage and the removal of frostbite and stagger under their headings; §12.1 has the summon's turn; §15.4 and §15.6 own the health dial, the arcs and the weak-arc die.
- Evidence: this book only.
- Ruling: NOT A RULES QUESTION
- Why: All met. Combat-E16 adds the one sentence that gathers the end-of-turn effects in §8.5 (see combat-072).
- Mechanical: no
- Edits: none

### combat-065 · Ch 10 · wound tokens by total value
- Question: Is "total value of wound tokens" the right measure in §10.3?
- This book now: Yes, in §8.2 and §10.3.
- Evidence: as combat-028.
- Ruling: CONFIRM as written
- Why: As combat-028, which carries the same wording into §7.5.
- Mechanical: no
- Edits: none (see combat-028)

### combat-066 · Ch 10 · glossary Attack value merge
- Question: Is there one merged glossary entry?
- This book now: Yes.
- Evidence: this book only.
- Ruling: NOT A RULES QUESTION
- Why: The merge was done; combat-029 adds the push-move clause to it.
- Mechanical: no
- Edits: none (see combat-029)

### combat-067 · Ch 10 · other glossary entries
- Question: Are Frostbite, Stagger, Attack (major action), Drink Estus, Relevant stat and Turn in order?
- This book now: All present and consistent with their sections.
- Evidence: this book only.
- Ruling: NOT A RULES QUESTION
- Why: A drafting note.
- Mechanical: no
- Edits: none

### combat-068 · Ch 10 · italics after action names
- Question: Are "major action" and "minor action" left plain after an italicised action name?
- This book now: Yes, as in chapters 04 and 07.
- Evidence: the drafting brief.
- Ruling: NOT A RULES QUESTION
- Why: A style matter.
- Mechanical: no
- Edits: none

### combat-069 · Ch 10 · example values
- Question: Are the block, resist and requirement values in the examples the printed ones?
- This book now: Illustrative (Silver Knight Swordsman block 2 and resist 4, Hollow Soldier resist 1, great axe 14 STR, sword 18 STR and 18 DEX; the Rapier's 14 STR and 21 DEX are from Appendix A).
- Evidence: not readable from the supplied texts.
- Ruling: NOT A RULES QUESTION
- Why: A proof check, listed under (b). Every example still computes correctly after the edits in this memo.
- Mechanical: no
- Edits: none

### combat-070 · Ch 10 · catalysts wielded two-handed
- Question: Does a catalyst that prints an attack option of its own gain the two-handed reroll when the other weapon slot is empty?
- This book now: Spells never gain the reroll, stored or equipped; the catalyst's own attack option is not mentioned (§10.4).
- Evidence: no source addresses it. This book §4.1 and the glossary make a catalyst a weapon card.
- Ruling: ADD
- Why: The general rule already answers: a catalyst is a weapon, and a one-handed weapon alone in the hands is wielded two-handed. Saying so in one sentence stops the spell exclusion beside it from being read too widely. It follows from the rules as written, so no play changes.
- Mechanical: no
- Edits: combat-E28

### combat-071 · Ch 10 · forced stamina and overflow
- Question: What does stamina overflow do, given that no rule of the book forces a character to place a stamina cube?
- This book now: A character cannot choose to spend stamina the bar cannot hold; a cube that a rule forces onto a full bar is not placed and the character is staggered instead; a second stagger token is not placed (§3.4; §10.1; §8.5).
- Evidence: Src 03: forced with no space, "the character is instead marked staggered ... may never elect to spend excess stamina" / Hollowed: "Players cannot use moves that require more stamina than they have empty slots" (Hol 316–317) / official 2017: a full bar kills (Core 935–936).
- Ruling: CONFIRM as written
- Why: It is the author's safety valve and costs one sentence. Every stamina cost now in the book is a choice gated by free space (the skip cost included), so the valve is idle in the standard game, but printed card text and expansion rules can force a cost, and a book that says what happens then is better than one that does not.
- Mechanical: no
- Edits: none

## Designer points

### combat-072 · Conditions · one timing pattern
- Question: Do the conditions share one pattern for when they are applied and when they are removed, and what is the simplest consistent one?
- This book now: Applied: all six alike, when an attack bearing the icon hits, after damage and push, whether or not damage was dealt (§8.5). Removed: bleed by its second token; poison resolved and cleared at the end of each of the model's turns; frostbite and stagger at the end of the model's next complete turn; corrosion when the model next suffers damage; calamity only when the encounter ends; all at the end of the encounter.
- Evidence: official 2017: one token of each; poison, frostbite and stagger removed at the end of the model's activation; bleed on the next damage (Core 963–1009) / official 2022: placed "after the attack is resolved, even if the attack doesn't cause damage"; poison, frostbite, stagger discarded at the end of the model's turn (TG 1463–1512) / Hollowed: bleed at two stacks; poison all at the end of the activation; stagger and frostbite at the end of an activation; calamity not removable; corrosion on taking damage (Hol 464–515) / FAQ: poison damage triggers official bleed (FAQ 55–63), which this book's bleed no longer does / online: Guide recommends the 2022 placement timing.
- Ruling: ADD
- Why: The pattern is sound and is confirmed; it only needed saying once. There is one way on (the attack sequence) and one clock off: the end of the affected model's own turn is the only moment at which a turn touches a condition, never the start of a turn, the end of the round, or another model's turn. Poison keeps no grace turn because it is a trigger that needs no memory (count, suffer, clear); frostbite and stagger are durations and need the "next complete turn" clause to mean anything when placed during the model's own turn. The other three are ended by events. One sentence in §8.5 states the clock.
- Mechanical: no
- Edits: combat-E16

| Condition | Tokens held | Placed | Ended by |
|---|---|---|---|
| Bleed | 1 | attack hits; after damage and push | a second bleed token (three damage, token removed) |
| Poison | any number | the same | the end of each of the model's turns (one damage per token, all removed) |
| Frostbite | 1 | the same | the end of the model's next complete turn |
| Stagger | 1 | the same; also a parry and stamina overflow | the end of the model's next complete turn |
| Calamity | 1 | the same | the end of the encounter |
| Corrosion | 1 | the same | the model next suffering damage |

### combat-073 · Attacks · one sequence, stated once
- Question: Is the order of an enemy attack (target, range, defence, damage, push, condition) and of a character attack stated once and matched everywhere?
- This book now: The character attack is one numbered procedure (§10.3, steps 1 to 12) and puts the push before the condition. The enemy attack has no single statement: target and range are in §9.3, the defences in §9.4 to §9.6. §8.4 and §8.5 give damage, then push, then condition; §9.4 step 7 gives the condition first and the push second; the glossary says the token is placed "after the attack is resolved".
- Evidence: official 2022: nine numbered steps, ending "Apply any conditions or push effects from the attack, even if the attack caused 0 damage" (TG 1667–1763) / official 2017: the push comes "after the roll is resolved" (Core 1182–1184) / Src 09: damage, conditions, push / Hollowed, Extended: silent / online: Guide follows the 2022 steps.
- Ruling: CHANGE
- Why: The order matters in one real case: a push-attack that carries stagger and drives the character onto a trap. If the token comes first, the trap's dodge is rolled at −1. The owning sections (§8.4, §8.5) and §10.3 already say push, then condition, which is also the natural reading (the blow lands, throws the target back, and only then leaves its mark), so §9.4 step 7 is corrected to match. A seven-step sequence is added to §9.3, the counterpart of the list in §10.3, so that every other section has one statement to cite; it also fixes the order among the characters struck by a node attack (the players choose).
- Mechanical: no
- Edits: combat-E20, combat-E21, combat-E38

### combat-074 · Pushes · displacement and other edge cases
- Question: Are the push and the node-limit displacement complete at their edges?
- This book now: §5.3 and §8.4, with §15.6 for a boss's node. §8.4 says a model is pushed "for one of four reasons".
- Evidence: official 2017: three models to a node, the players push one already there; a boss is pushed only by another boss (Core 427–438, 968–971) / official 2022: "place it on an adjacent node" (TG 928–930) / Hollowed: an entering monster pushes a monster, otherwise the lowest-threat player (Hol 446–451) / Src 05: friendly pushes friendly, hostile pushes hostile / online: fan summary: "the active player chooses which model to push".
- Ruling: CHANGE
- Why: The cases were walked through and all but one are already answered. A displaced model always has a valid node, because the node the entering model came from is one. A displacement into another full node chains under the same rule. Off a boss's node the arc limit applies (§15.6). A displaced character triggers a trap and breaks a barrel as in any push. A model with no farther valid node is not pushed, and the rest of the attack stands. The one fault is the count: a leap (§16.2), Kalameet's landing (§17.8) and the Chariot's track cards (§17.9) also push, so "four reasons" was wrong; the list is opened and the glossary follows. No play changes.
- Mechanical: no
- Edits: combat-E13, combat-E14, combat-E37

### combat-075 · Range · doorways and joined tiles
- Question: How is range counted through a doorway and across joined tiles?
- This book now: Range is the shortest chain of adjacent nodes; nodes on different tiles are not adjacent; no model leaves the encounter's tile; the two joined boss tiles are one tile; a wall lengthens range only by breaking adjacency; range ∞ reaches every model in the encounter (§5.1; §5.2; §5.4; §15.3).
- Evidence: official 2017: range between models, ∞ reaches "any model in the encounter" (Core 407–414) / official 2022: range "measured between nodes in the same way as adjacency"; "Actions and attacks cannot target a model on a different tile" (TG 908–919) / online: Guide confirms no targeting across tiles in the 2022 game.
- Ruling: CONFIRM as written
- Why: The question cannot arise in this book: an encounter is fought on one tile, so nothing stands beyond a doorway to be measured to, and the non-adjacency of tiles says so in rule form. One definition of range (the chain of adjacent nodes) covers walls, the join and the mega-boss boards without a special case. §15.3 should keep its words "the nodes that face it across the join", meaning the one node directly opposite.
- Mechanical: no
- Edits: none

### combat-076 · Movement · one definition of a valid node
- Question: Do Walk, Run, shift, the dodge and the push use one definition of a valid node?
- This book now: One definition in §5.2, with the terrain of §5.5 deciding by form of entry: gravestones, chests and pillars block everything; an intact barrel blocks a move but is broken by a dodge or a push; traps block nothing; a full node is valid. §10.2, §10.3 (Shift), §9.2, §9.5, §8.4 and §16.2 all cite it. §5.5, Traps calls the movement after a dodge "the move".
- Evidence: official 2017: barrels block movement and pushes and are broken by a character for one stamina (Core 765–776) / official 2022: any model entering removes the barrel (TG 970–979) / Hollowed: barrels break "while dodge-rolling or getting pushed into them" (Hol 345–350) / Src 05 and 10: the rule as the book has it.
- Ruling: CHANGE
- Why: The single definition is confirmed. The only difference between the forms of movement is the barrel, and that one difference earns its place: a deliberate step is stopped, a roll or a blow smashes through. The three-way wording (move; movement after a dodge; push) exists to carry it and is used consistently, with one slip in §5.5, which is corrected.
- Mechanical: no
- Edits: combat-E10

### combat-077 · Character turn · action economy
- Question: What is once per turn, what repeats, and what does stamina overflow do?
- This book now: See the table (§10.1; §10.2; §3.4; §9.5; §9.6).
- Evidence: official 2017: gain 2 stamina; walk once; run any number; attack with each weapon; swap at the start (Core 1017–1040) / official 2022: recover 3; one move and one action in either order (TG 1408–1444) / Hollowed: recover 1; Attack and Rest are major actions, Run and Estus minor, Walk and Swap free (Hol 400–432) / Gate 1 OQ-26 / online: reviews single out the official game's length and repetition, which the Rest-or-Attack choice answers (search summaries).
- Ruling: CONFIRM as written
- Why: The economy is tight and legible: one stamina a turn comes back unasked, and everything more must be bought with the major action. Rest against Attack is the turn's central decision, and the Run exclusion stops a character from sprinting and resting in one turn. Each limit is stated once in §10.1. The only loose ends were inside the Attack action and are settled in combat-058 to combat-060.
- Mechanical: no
- Edits: none

| Element | Limit | Cost |
|---|---|---|
| Recovery at the start of the turn | automatic; none with frostbite | recovers one stamina |
| Walk | once per turn | none |
| Run | any number of times; not in a turn with Rest | one stamina per node |
| Equip | once per turn | none |
| Heroic Action | once per turn, and the token is readied only at the bonfire | the token |
| Major action | one per turn: Attack, Rest, Drink Estus or Ember | as stated for each |
| Attack | up to one attack with each weapon slot; one spell attack option per turn; a repeat icon allows up to the number shown | the stamina of each option, once |
| Dodge or parry (in other models' turns) | one defence per attack | one stamina; two more for one dodge die |
| Stamina overflow | never by choice | a forced cube with no space is not placed and staggers the character; nothing more if already staggered |

### combat-078 · Enemy scaling · by number of characters
- Question: Is the enemy scaling table a sound and simple answer to party size?
- This book now: One character: base. Two: +1 health, movement of 1 becomes 2. Three: +2 health, the same movement. Four: +4 health, the same movement, +1 to attack values. Fixed at setup; dead characters still count; bosses, mimics, phantoms and crystal lizards are exempt (§8.3; Gate 1 OQ-07).
- Evidence: official 2017 and 2022: no stat scaling; every enemy acts before each character's turn, so pressure grows with the party by itself (Core 875–894; TG 1638–1653) / Extended: scales the soul rewards by party size, not the enemies (Ext 99–107) / Hollowed: keeps the official alternation (Hol 400–425) / Src 08: +1 health per character beyond the first, 1 becomes 2 at two, +1 attack at three, Repeat 2 at four / online: reviews: more players means "more activations between each character's turn" and a longer, harder game (GamesRadar, Tabletop Gaming, search summaries).
- Ruling: CONFIRM as written
- Why: The single enemy phase is this book's best structural change (it removes the official game's worst downtime), and it needs an explicit table to replace the pressure it removes. The table does that with three levers, each read straight off the data card, and the Gate 1 numbers are defensible: health rises roughly with the party's damage for the one-health enemies that fill most encounters, movement keeps enemies in reach of a larger party, and attack rises only where four characters share the blows. Two limits are worth knowing but do not justify more rules: a flat health increase does little for enemies with high base health, and the step from three to four characters is the steepest. Fixing the number at setup avoids rescaling in the middle of a fight.
- Mechanical: no
- Edits: none

### combat-079 · Duplicates · where two rules did one job
- Question: Where do two rules do the same job, and which one stays?
- This book now: Eight pairs were found in this cluster.
- Evidence: this memo.
- Ruling: NOT A RULES QUESTION
- Why: An index; each pair is ruled on in its own entry. (1) Repeat icon: whole row for a boss, one attack for an enemy; the whole row stays (combat-023). (2) Push before condition in §8.5 and §10.3, condition before push in §9.4; push first stays (combat-073). (3) Three defences in §9.3, four in §20.4; three stay (combat-044). (4) Four wordings of "entry node"; one stays (combat-010). (5) Two lists of what a character may target; the longer stays (combat-062). (6) Wound tokens counted by number in §7.5 and by value in §8.2; value stays (combat-028). (7) "Move" and "the movement that follows a dodge" for the same thing in §5.5; the second stays (combat-076). (8) Left slot and right slot as a condition of the parry beside the general rule that a one-handed card goes in either slot; the general rule stays (combat-035). Two overlaps were looked at and left: §8.4 and §9.2 both describe the push-move, but one owns the steps and the other cites it; and Heroic Action is limited both "once per turn" and by a token readied only at the bonfire, which is harmless.
- Mechanical: no
- Edits: none

## (a) Every CHANGE, ADD and DELETE

| Entry | Ruling | What changes | Mechanical | Edits |
|---|---|---|---|---|
| combat-005 | CHANGE | One scry for each gravestone on a cleared tile, in place of one per encounter | yes | E01, E02, E03, E04 |
| combat-010 | CHANGE | Entry node defined once: a basic node along the edge of the doorway the characters entered by | no | E05, E06, E07, E08 |
| combat-016 | ADD | Primary and secondary spawn and terrain nodes named; the difference has no rules effect | no | E09 |
| combat-020 | ADD | For the aggro token, bleed damage counts for the character who triggered it; poison damage counts for nobody | no | E17 |
| combat-023, combat-039 | CHANGE | A repeat icon on an enemy data card repeats the whole row of icons, as on a boss's behaviour card | yes | E12, E18, E19, E36 |
| combat-028 | CHANGE | §7.5 counts the total value of wound tokens, not their number | no | E31, E32 |
| combat-029 | CHANGE | Glossary Attack value covers the push-move damage value and stagger | no | E42 |
| combat-035 | CHANGE | A shield in either weapon slot permits a parry; the riposte uses the weapon in the other slot, never a spell | yes | E22, E23, E24, E25, E30, E34, E39, E40 |
| combat-037 | CHANGE | §8.4 says outright that the attack of a push-move cannot be parried | no | E15 |
| combat-044 | DELETE | "The defender may decline to defend" removed from §20.4 | no | E33 |
| combat-049 | CHANGE | Glossary names the magical damage icon as the chapters do; physical damage is the default of a character's attack | no | E43, E44 |
| combat-054 | ADD | A weapon whose four requirements are all zero is never scaled | yes | E29, E35, E41 |
| combat-059 | CHANGE | A repeated attack option is resolved up to the number of times shown; the character may stop | yes | E27, E36 |
| combat-060 | ADD | An attack whose shift leaves no target in range ends without a roll; the stamina is spent | no | E26 |
| combat-062 | CHANGE | §8.1 lists the same targets as §10.3 | no | E11 |
| combat-070 | ADD | A catalyst's own printed attack option gains the two-handed reroll | no | E28 |
| combat-072 | ADD | One sentence in §8.5: the end of the model's own turn is the only moment a turn acts on a condition | no | E16 |
| combat-073 | CHANGE | §9.4 step 7 resolves the push before the condition; a seven-step Attack Sequence is added to §9.3; glossary Condition follows | no | E20, E21, E38 |
| combat-074 | CHANGE | §8.4's list of the causes of a push is opened to include a leap and other boss rules | no | E13, E14, E37 |
| combat-076 | CHANGE | "the move that follows a successful dodge" becomes "the movement" in §5.5 | no | E10 |

Five rulings change play: combat-005, combat-023 (with combat-039), combat-035, combat-054 and combat-059. All five are small and each is reversible by dropping its edits. None revises a Gate 1 decision; combat-023 removes a special case that Gate 1 OQ-07 left without a purpose.

## (b) Not settled, and why

- Printed card values. The examples in §8.2, §8.3, §8.5, §9.4 to §9.6 and §10.3 use values for the Hollow Soldier and the Silver Knight Swordsman, and requirement values for three weapons, that cannot be read from the supplied texts (the data cards are images). They must be checked against the cards at proof (combat-030, combat-052, combat-069). A resist of 4 for the Silver Knight Swordsman in the §10.3 area-of-effect example looks high and deserves the first look.
- Trap token mix. The publisher's backer update gives 11 blank tokens and 9 with values out of 20, but it was seen only as a search summary and not against the components (combat-009).
- Whether any enemy data card in any set prints a repeat icon, and whether any catalyst prints an attack option of its own. Neither could be checked without the cards. Both rulings (combat-023, combat-070) are written so that they are right whichever is true.
- How many encounter cards place two gravestones. This fixes how often combat-005 matters, not whether it is right.
- A shift that is taken away from every target on purpose. Combat-E26 gives it the same outcome as a shift cut short by a trap (the attack ends, the stamina and that weapon's attack are spent). If the lead editor prefers to forbid it, the sentence needs the words "if a trap moved the character" in place of the general condition; the cost is a special case.
- Online discussion was thinner than the brief hoped: the Reddit mirrors refused and no BoardGameGeek thread could be opened, so house-rule evidence rests on the two community rulesets, the community Guide, and search summaries.

## (c) Cross-cluster effects for the lead editor

1. Chapter 07 (§7.5) is edited four times from this cluster: the scry step and the scry paragraph (E02, E03) and the two wound-token sentences (E31, E32). If another cluster rewrites the same sentences, the rulings to carry over are "one scry for each gravestone" and "total value of wound tokens".
2. Chapter 03 (§3.2), chapter 20 (§20.4) and the F.A.Q. (§22.2, two answers) each take one edit that follows a ruling here (E30, E33, E34, E35).
3. F.A.Q. §22.1, first question ("Which weapon slot is the left weapon slot, and which is the right?"): after combat-035 no rule depends on the answer. It is harmless and may stay; deleting it is tidier.
4. §16.4 defines damage to a boss as "an attack lowers the boss's health dial". With combat-E17, bleed triggered by a character's attack counts for the aggro token, and bleed is not an attack (§8.5). §16.4 needs the words "or a bleed that the attack triggers" in that sentence. No edit is supplied, because the sentence belongs to the boss cluster.
5. §6.7 ("All four basic nodes along the wall beside the doorway are entry nodes") and §15.3 ("the basic nodes adjacent to the doorway on which the fog gate token is placed") still use the older wordings of an entry node. Both agree in substance with the new definition (combat-010); §15.3 should say "along the edge that holds the doorway", and the §6.7 sentence becomes a statement of number, not an exception.
6. §16.3, Damage, Pushes, and Conditions already gives push after damage and then the condition; it may cite "(see §9.3, Attack Sequence)". §15.5's card anatomy and §16.1 step 4 already state the whole-row repeat that §9.1 now shares.
7. Glossary entries edited here that another cluster may also touch: Gravestone, Entry node, Basic node, Doorway, Repeat, Push, Condition, Parry, Riposte, Scaled (weapon), Attack value, Magical damage, Physical damage. Each `new` is the whole line; merge by hand if two clusters meet on one entry. The entries Dodge, Frostbite, Stagger, Poison, Bleed, Trap token, Valid node, Move, Node model limit, Nearest character and Enemy scaling were checked against the rulings and need no change.
8. Two F.A.Q. entries would now be worth adding, each restating a rule this cluster owns: the order of damage, push and condition (§9.3, Attack Sequence), and that a boss holds condition tokens as any model does (§8.5; §16.1). No edit is supplied; the F.A.Q. belongs to another cluster.
9. `14_open_issues.md`: lead items 8 and 16 are confirmed as written. Finding A-068 moves from "not adopted" to adopted (combat-035); findings B-002 and B-033 stay unapplied by decision (combat-034); A-066 is applied (combat-054); A-081 stays unapplied by decision (combat-032). The change log needs entries for the five mechanical rulings.
10. Layout: combat-E09 uses two icon tokens new to chapter 05 (`ast-0010-secondary-spawn-node`, `ast-0018-secondary-terrain-node`), and combat-E18 adds the repeat icon token to §9.1. The new H3 "Attack Sequence" in §9.3 is a citable sub-heading.
