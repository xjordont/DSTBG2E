# Drafting pack — chapter 07 (gameplay) — manuscript chapter "GAMEPLAY"

Source text: `work/phase2a/source/07_gameplay.md` (manuscript.md lines 1197–1480).

## Tracker rows (section · status · notes)

- **(chapter)** · present — to audit · line 1197.
- **Objective & Loss Conditions** · present — to audit · line 1199.
- **Death & Hollowing** · present — to audit · line 1203.
- **Embering** · present — to audit · line 1225.
- **Sparks** · present — to audit · line 1245.
- **Encounters** · present — to audit · line 1255.
- **Encounter Start** · present — to audit · line 1257.
- **Encounter Turn Order** · present — to audit · line 1279.
- **Encounter Resolution** · present — to audit · line 1297.
- **Encounter Recovery** · present — to audit · line 1343.
- **Souls** · present — TOC mismatch · line 1383. TOC calls it "Soul Rewards".
- **Soul Reward Table** · present — defect · line 1401. Stray "i" in header cell ("per characteri").
- **(empty heading)** · ORPHAN — delete · line 1441: empty H2 used as page break
- **Treasure Rewards** · present — to audit · line 1443.

## Audit findings mapped to this chapter (110)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### A-002 · undefined-state · Blocker · REQUIRED
- Location: GAMEPLAY › Objective & Loss Conditions (manuscript.md line 1201); Death & Hollowing (line 1223)
- Evidence: manuscript.md:1201, 1223, 1253, 1341; DS-Core-Rules-lores.txt p.8 ('Once the dial reads 0 ... the next time a character is killed, the game is lost')
- Current text: The players lose collectively if at any point, all characters are dead and there are no remaining sparks to revive them.
- Proposed fix: When the characters are forced to rest at the bonfire and the spark dial shows zero, the players lose the game. The characters may not choose to rest at the bonfire while the spark dial shows zero.
- Rationale: A hollow character's death fails the encounter while other characters are still alive (1305); the forced rest then costs a spark that does not exist, and the stated loss condition (all characters dead) never triggers. The official rule ties the loss to a death at zero sparks; the manuscript's forced-rest model needs the equivalent.
- Gameplay impact: The game's only end-state for defeat has no rule that applies in the commonest defeat sequence.
- Decision needed: N

### A-053 · undefined-state · Blocker · REQUIRED
- Location: GAMEPLAY › Souls (manuscript.md line 1391); Soul Reward Table (lines 1401–1439); Encounter Resolution (line 1327); Campaign Soul Reward Table (lines 2247–2285)
- Evidence: manuscript.md:1321–1327, 1389–1391, 1401–1439, 2245, 2247–2285
- Current text: Upon successfully clearing an encounter that has been previously cleared, reward the reduced soul reward to each character.
- Proposed fix: The reduced soul reward is half of the full soul reward, rounded up. Add a 'Reduced reward' column to both soul reward tables: basic 2 / 2 / 3 / 3 (Level 1–4), campaign 1 / 2 / 2 / 3.
- Rationale: The tables have a single column; 'reduced' is never quantified, so repeated encounters (a core loop the manuscript explicitly allows at 1321 and 2245) have no payout. Alternative: full reward minus two, minimum one (basic 1/2/3/4, campaign 1/1/2/3).
- Gameplay impact: Every repeated encounter is unresolvable.
- Decision needed: Y

### A-090 · omission · Blocker · REQUIRED
- Location: GAME COMPONENTS › Event cards (manuscript.md lines 659–667); SETUP steps (lines 1133, 1161, 1181); Encounter Start step 5 (line 1269); Gravestones (line 939)
- Evidence: manuscript.md:659–667, 939, 1133, 1147, 1161, 1181, 1269; no official 1E source; DS-TG-Rulebook p.19 (V2 event cards are a different, unlevelled mechanic drawn after encounters)
- Current text: Deal one face-down event card of the encounter card's level to each tile. ... Reveal the tile's event card, if not already revealed.
- Proposed fix: Either delete every reference to event cards and the Special Trap cards (components, setup steps, Encounter Start step 5, Event scrying), or add a chapter 'Event Cards': When an encounter's event card is revealed, resolve its text immediately; its effect lasts for that encounter only. When the encounter is reset, the event card is returned face-down to its tile and is resolved again the next time the encounter is fought. Event cards are not used in boss, mimic or Level 4 encounters.
- Rationale: Thirty-five cards are listed, dealt and scried, but nothing says what an event card is, what it does, or where it comes from; no supplied official or community source defines levelled event cards. The rulebook cannot stand alone until the component is defined or removed.
- Gameplay impact: A dealt component with no rules blocks every encounter setup.
- Decision needed: Y

### B-008 · undefined-value · Blocker · REQUIRED
- Location: L1391 (Souls) and Soul Reward Table L1401-1434
- Evidence: "reward the reduced soul reward" is used but no reduced value appears anywhere in the manuscript. Candidate values: half rounded down 1/2/2/3 (re-clear of four tiles = 6-8 souls), half rounded up 2/2/3/3, reward-2 1/2/3/4 (campaign L1 would be 0), flat 1.
- Current text: Upon successfully *clearing* an encounter that has been previously *cleared*, reward the reduced *soul* reward to each character.
- Proposed fix: "Upon clearing an encounter that has previously been cleared, each character gains half the listed soul reward, rounded down." Add a third column to both Soul Reward Tables headed "Reduced reward": basic 1 / 2 / 2 / 3; campaign 1 / 1 / 2 / 2.
- Rationale: Half-rounded-down is the strongest anti-grind value that still pays; a full four-tile re-clear (6-8 souls) is worth less than one Tier Three step (8), which matches the stated design goal of removing grinding.
- Gameplay impact: Defines a rule that currently cannot be played; caps repeat income at about +14 souls per game.
- Decision needed: Y

### B-014 · balance · Blocker · REQUIRED
- Location: L1261-1263 (Encounter Start step 2) with L781 and L791-795
- Evidence: Three skipped encounters = 6 stamina (the manuscript's own example). Hollow bar = 6 spaces, so a hollow character starts with zero free boxes: any damage kills (L795) and any stamina cost is forbidden (L791-793), leaving Rest as the only legal major action. A healthy character with three skips has 2 free boxes: P(death) from one Hollow Soldier hit (attack 4, 2 black block dice) = 0.556; at 3 players (attack 5) 0.889. Any hollow death fails the encounter and costs a spark (L1223).
- Current text: Characters may skip previously *cleared* encounters at the cost of two stamina cubes placed in the endurance bar of each character. For example, if the first three encounters are marked *cleared* then the characters could skip to the fourth encounter but would all start with 6 stamina expended.
- Proposed fix: "Characters may skip previously cleared encounters. Each character places one stamina cube in their endurance bar for each encounter skipped, to a maximum of three. For example, if the first three encounters are marked cleared, the characters may skip to the fourth encounter and each starts it with three stamina spent."
- Rationale: The skip is a time-saving device; the tax must leave a hollow character at least three free boxes (6 - 3 = 3) so that the first enemy phase is survivable.
- Gameplay impact: Hollow three-skip death chance per Hollow Soldier hit falls from 100% to 19% (3 free boxes, attack 4); healthy from 56% to 3%.
- Decision needed: Y

### C-068 · table-text · Blocker · REQUIRED
- Location: L1389; L1391; L1401-1439; L2243
- Evidence: Souls: 'reward the full *soul* reward' for a first clear (1389) and 'the reduced *soul* reward' for a repeat clear (1391); the Soul Reward Table has a single column (3/4/5/6) and no reduced value; Campaign table is simply basic minus one (2/3/4/5) and L2245 says repeats reward souls 'just as in the basic game'
- Current text: the reduced *soul* reward
- Proposed fix: Either add a 'Repeat clear' column to both tables (author decision on values) or delete 'reduced' and pay the full reward on repeats; then rewrite L1391 and L2245 to match.
- Rationale: A rule references a value that exists nowhere.
- Gameplay impact: Soul income on every repeated encounter is undefined
- Decision needed: Y

### D-001 · hybrid · Blocker · REQUIRED
- Location: manuscript.md 661–667 (components), 1133, 1161 (setup), 1269 (encounter start), 939 (scrying)
- Evidence: No 1E event cards exist (Core p.6–7 lists none). V2 p.6/p.19 has 30 un-levelled event cards of three kinds (Immediate, Consumable, Rendezvous) drawn after completing an encounter. The manuscript lists levelled event cards plus 'Special Trap cards', deals one per tile, reveals it at encounter start and allows scrying it, but contains no rule stating what an event card does.
- Current text: 10x Level 1 event cards / 10x Level 2 event cards / 10x Level 3 event cards / 5x Special Trap cards … Deal one face-down event card of the encounter card's level to each tile … Reveal the tile's event card, if not already revealed.
- Proposed fix: Either (a) add a section 'Event Cards' defining the card anatomy, when the card's text applies, and how it is discarded or reset when the characters rest; or (b) delete every reference to event cards (components, setup steps 3 and 7, encounter start step 5, event scrying).
- Rationale: A V2-style component has been grafted onto 1E tiles with no mechanic attached; the halves are not reconciled because the V2 event mechanic (drawn after an encounter, tied to the encounter track) cannot operate in the manuscript's tile dungeon.
- Gameplay impact: Players cannot resolve setup or encounter start as written.
- Decision needed: Y

### A-001 · undefined-state · Major · REQUIRED
- Location: RETURNING TO THE BONFIRE › Resting at The Bonfire (manuscript.md line 1906)
- Evidence: manuscript.md:1890, 1906, 1223, 1305, 2235
- Current text: Resting at the bonfire also revives lost characters who have been removed from play due to dying while hollow.
- Proposed fix: A character who dies while hollow is lost. A lost character's model is placed on its side beside the bonfire tile and takes no further part in the encounter. When a character is lost, the encounter is failed immediately and the characters must rest at the bonfire. Resting at the bonfire revives all dead and lost characters.
- Rationale: The term 'lost' appears at lines 1890, 1906 and 2235 but is never defined. Death & Hollowing (1223) already forces an immediate rest when a hollow character dies, so 'lost' is a transient state that must be named once and added to the glossary.
- Gameplay impact: Players cannot tell whether a lost character differs from a dead one or whether lost characters return after a free (post-boss) rest.
- Decision needed: N

### A-003 · undefined-state · Major · REQUIRED
- Location: GAMEPLAY › Souls (manuscript.md lines 1395–1399); Encounter Resolution (line 1331)
- Evidence: manuscript.md:1207, 1309, 1323, 1331, 1395–1399, 1145
- Current text: Dropped souls are lost forever if the character who dropped them dies before reclaiming the souls.
- Proposed fix: Souls dropped by a character remain on the encounter tile where they were dropped. Souls dropped at the moment of death are not forfeited by that death; they are returned to the supply only if the same character dies again before reclaiming them. When an encounter is failed, every living character drops their souls on that tile in addition to any souls already there. A character reclaims their own dropped souls only by surviving to clear the encounter on the tile where the souls lie.
- Rationale: A hollow character's death simultaneously drops souls (1207) and fails the encounter (1305), so the literal text ('dies before reclaiming') forfeits the souls dropped by that very death. Line 1331 also makes all characters drop souls, including characters whose souls already lie on the tile. Hollowed Edition keeps dropped souls until a second death.
- Gameplay impact: Whether a hollow character's death wipes their souls is the single largest soul swing in the game and is currently ambiguous.
- Decision needed: N

### A-006 · contradiction · Major · REQUIRED
- Location: GAMEPLAY › Embering (manuscript.md line 1229) vs CHARACTERS › Ember (line 805) and CHARACTER TURN › Major Action › Ember (line 1834)
- Evidence: manuscript.md:805, 891, 1227–1233, 1834
- Current text: Ember: Place ember token on dashboard; discard equipped ember card.
- Proposed fix: Ember (major action, or at any time outside an encounter): Discard an ember card from the back-up slot. Remove all damage cubes and all hollow markers from the endurance bar and place an ember token on the dashboard. The character is now embered.
- Rationale: Three passages define embering; only Embering (1229) says it removes all damage cubes. A full heal as a major action is a major tactical resource and must be stated identically everywhere. Alternative: delete 'Remove all damage cubes' at 1229 so that embering only removes hollow markers (Hollowed Edition precedent, p.5).
- Gameplay impact: Groups will disagree on whether embering heals; the difference is up to eight health in combat.
- Decision needed: Y

### A-008 · contradiction · Major · REQUIRED
- Location: GAMEPLAY › Encounters › Encounter Start step 2 (manuscript.md lines 1261–1263) vs CHARACTERS › Endurance Bar (line 787)
- Evidence: manuscript.md:781, 787, 1261–1263
- Current text: A character may never elect to spend excess stamina at the cost of receiving a staggered condition marker.
- Proposed fix: The characters may skip cleared encounters only if every character can place all of the required stamina cubes without exceeding their endurance bar. A hollow character has six spaces. The stamina cubes for skipped encounters are placed at the start of the next encounter the characters fight.
- Rationale: Skipping is elective, costs two stamina per skipped encounter per character, and a hollow character has six spaces; skipping four encounters (eight stamina) is therefore impossible under line 787, yet campaign sections list up to five encounters. Alternative: allow the skip and place a single stagger token for the overflow.
- Gameplay impact: Determines whether hollow characters can use the skip mechanic at all in long sections.
- Decision needed: Y

### A-013 · undefined-state · Major · REQUIRED
- Location: GAMEPLAY › Encounters › Encounter Turn Order step 3 (manuscript.md line 1291); ENEMY TURN › Enemy Movement (line 1672)
- Evidence: manuscript.md:1275, 1291–1293, 1672, 1682; DS-Core-Rules-lores.txt p.22 (aggro passes on activation)
- Current text: After all characters have taken their turn, place the aggro token on the character who placed the most damage tokens on enemy models.
- Proposed fix: When the character holding the aggro token dies, immediately place the aggro token on the living character with the highest threat value; if several are tied, the players choose. The aggro token is never held by a dead character.
- Rationale: Enemy movement and attacks target the aggro holder; nothing says what happens when that character is removed from play mid-round. In the official game the token moves every character activation, so the state never arises.
- Gameplay impact: Enemy behaviours become unresolvable for the rest of the round after a death.
- Decision needed: N

### A-019 · undefined-state · Major · REQUIRED
- Location: BOSS TURNS › Boss Turn Overview (manuscript.md line 2157)
- Evidence: manuscript.md:2157, 1205, 1211
- Current text: characters must take an equal number of turns and cannot take a turn until every other character has taken an equal number of turns.
- Proposed fix: Dead characters are ignored when counting turns. Within each round the living characters choose the order in which they take their turns, and no living character takes a second turn in a round until every other living character has taken one.
- Rationale: A dead character can take no turns, so the literal equal-turns rule blocks every living character once anyone dies in a boss fight.
- Gameplay impact: Boss fights after a death become unplayable as written.
- Decision needed: N

### A-031 · contradiction · Major · REQUIRED
- Location: GAMEPLAY › Objective & Loss Conditions (manuscript.md line 1201) vs PLAYER VS PLAYER (line 3042)
- Evidence: manuscript.md:1201, 3042, 3078–3080
- Current text: Players may also choose to add a player versus player (PvP) encounter after the final boss is defeated ... / After each boss (mini, main, and mega) a PvP encounter will occur.
- Proposed fix: If the players chose PvP during setup, a PvP encounter is played after each boss encounter (mini, main and mega) is cleared and before the characters rest at the bonfire.
- Rationale: The objective text says PvP happens once, after the final boss; the PvP chapter says after every boss and its '+1 attack damage in future PvP' rule only makes sense with several PvP rounds. Alternative: a single PvP encounter after the final boss and deletion of the +1 rule.
- Gameplay impact: Decides how many PvP rounds a game contains.
- Decision needed: Y

### A-050 · contradiction · Major · REQUIRED
- Location: SETUP › Setup After the main-boss step 11 (manuscript.md line 1195) vs Death & Hollowing (line 1223) and Objective & Loss Conditions (line 1201)
- Evidence: manuscript.md:1191, 1195, 1201, 1223, 1305; DS-EC-Rules-Web.txt p.9 and DS-BDK-Rules-web.txt p.9 (official: no free rest after the level 4 encounter; retries cost a spark)
- Current text: If a character dies they are permanently removed from play. If all characters die, the players lose the game.
- Proposed fix: During the final mega-boss encounter the Death & Hollowing rules are replaced: a character who dies is removed from play for the rest of the game, the encounter is not failed, and the players lose only when every character is dead. Sparks cannot be spent during or after the final mega-boss encounter.
- Rationale: A hollow character's death normally fails the encounter and forces a rest (1223); the mega-boss text instead removes the character permanently without saying that the failure rule is suspended. Alternative: delete the permanent-death sentence and let the mega-boss follow normal boss rules with spark-costed retries, as the official mega-boss booklets do.
- Gameplay impact: The climactic fight has two incompatible death rules.
- Decision needed: Y

### A-054 · contradiction · Major · REQUIRED
- Location: RETURNING TO THE BONFIRE › Resuming Exploration (manuscript.md line 1963) vs Encounter Start step 2 (line 1261), Encounter Resolution (line 1319) and The Fog Gate (line 2065)
- Evidence: manuscript.md:1261, 1317–1319, 1339, 1963, 2065
- Current text: If the encounter card on the tile is face-down (cleared or failed), they must flip the card face-up and proceed with fighting the enemies of that encounter.
- Proposed fix: After the characters rest, every encounter card is face-down. When the characters enter a tile whose card is face-down, they reveal it. If the encounter is marked cleared, the characters may skip it for the stamina cost; otherwise they must fight it. The fog gate shortcut is unaffected.
- Rationale: 'Must ... proceed with fighting' contradicts the skip rule for cleared encounters (1261, 1319) and the fog gate shortcut (2065), both of which assume the party can bypass reset tiles.
- Gameplay impact: Decides whether the skip mechanic exists after the first rest.
- Decision needed: N

### A-057 · contradiction · Major · REQUIRED
- Location: SETUP › Encounter cards step 4 (manuscript.md line 1135) and Setup After the mini-boss step 8 (line 1163) vs Treasure Rewards (line 1451)
- Evidence: manuscript.md:1135, 1163, 1313, 1445–1451, 2291–2293, 2340
- Current text: Deal one tier one treasure per character face-down to each encounter tile. / Draw cards from the Tier one treasure deck before defeating the mini-boss, and Tier two treasure deck thereafter.
- Proposed fix: The treasure cards dealt face-down to an encounter tile during setup are that encounter's treasure reward. When the encounter is cleared for the first time, each character takes one of those cards; the cards are not drawn from the deck at that time. In campaign play, treasure cards already dealt to tiles are not replaced when the bonfire ascetic is burnt.
- Rationale: Setup pre-deals one card per character to every tile, yet Treasure Rewards says to draw from the deck on clearing; a party would collect both. The pre-deal is the only reading under which 'Characters receive their treasure card reward even if they died' and the campaign tier rules (2291) are mechanical. Alternative: delete the pre-deal steps and draw on clearing.
- Gameplay impact: Doubles treasure income if both are applied.
- Decision needed: Y

### A-060 · undefined-state · Major · REQUIRED
- Location: GAMEPLAY › Treasure Rewards (manuscript.md lines 1463–1475); MIMICS (lines 2043–2047)
- Evidence: manuscript.md:1313, 1357, 1467–1475, 2043–2047; DS-Explorers-Rules-Web.txt p.12–13 (official: recover and gain souls first, then flip the ambush card)
- Current text: The characters do not recover stamina, remove damage, draw treasure, or collect souls until a decision is made.
- Proposed fix: Until the ambush card is revealed, dead characters remain dead and no character recovers stamina or damage. If the mimic is slain, resolve the cleared encounter's soul and treasure rewards and Encounter Recovery (reviving dead characters), then award the mimic's treasure. If the mimic encounter is failed, the cleared encounter's soul and treasure rewards are forfeited, the encounter card is reset and the cleared marker remains.
- Rationale: The deferred-reward rule leaves open whether the dead fight the mimic, whether the original rewards survive a mimic wipe, and when recovery happens after a mimic kill. Alternative: adopt the official order (recover and collect rewards before the ambush card).
- Gameplay impact: A mimic wipe can cost or not cost an entire encounter's rewards depending on reading.
- Decision needed: Y

### A-061 · contradiction · Major · REQUIRED
- Location: GAMEPLAY › Encounter Recovery (manuscript.md line 1347) vs MIMICS (line 2043)
- Evidence: manuscript.md:1347, 2043
- Current text: Remove one damage cube from each character. / they proceed to recover all stamina and two damage normally.
- Proposed fix: Encounter Recovery: Remove two damage cubes from each surviving character. (Align line 2043 to the same number.)
- Rationale: The two passages give different healing amounts for the same event. Alternative: one damage cube, with the mimic chapter corrected.
- Gameplay impact: Changes attrition across every encounter chain.
- Decision needed: Y

### A-096 · contradiction · Major · REQUIRED
- Location: GAMEPLAY › Treasure Rewards (manuscript.md line 1477) vs CRYSTAL LIZARDS (line 2055)
- Evidence: manuscript.md:1477, 2055, 3182; DS-IronKeep-Rules-Web.txt p.3 (3x Titanite Scale Cards), p.5
- Current text: award a Titanite Chunk card to any character who killed a crystal lizard during the encounter. / Whenever a character kills a crystal lizard, they immediately place one Titanite Scale card into their inventory.
- Proposed fix: Whenever a character kills a crystal lizard, that character immediately places one Titanite Scale card in their inventory. (Delete the Titanite Chunk bullet at line 1477.)
- Rationale: Two names and two timings for the same reward. The Iron Keep expansion supplies Titanite Scale cards for exactly this purpose; the Update Pack's Titanite Chunk is a separate common card. Alternative: award a Titanite Chunk and treat the three Scale cards as extra Chunks.
- Gameplay impact: Different cards with different stat requirements and bonuses.
- Decision needed: Y

### A-104 · undefined-state · Major · PROPOSED
- Location: CAMPAIGNS › Demon Hunting Section One (manuscript.md lines 2598–2608)
- Evidence: manuscript.md:1223, 1341, 1894, 2598–2608
- Current text: Section One - Undead Asylum: Level 1 Encounter, Level 1 Encounter, Asylum Demon (Mini-Boss) ... Bonfire Tile (characters revive here if they die in Section One)
- Proposed fix: Demon Hunting, Section One: there is no bonfire tile. If the characters are forced to rest during Section One, they spend a spark, revive and restore their characters as if resting, and restart Section One from its first encounter tile; the Firekeeper, Andre and the shop are not available until Section Two.
- Rationale: Every forced rest in the manuscript sends the party to the bonfire tile; Section One has none, and the parenthetical only says where characters revive, not what happens to the section. Alternative: the party is moved to Section Two's bonfire and Section One is abandoned.
- Gameplay impact: The opening section of the campaign has no defeat procedure.
- Decision needed: Y

### A-122 · omission · Major · REQUIRED
- Location: BOSS ENCOUNTERS (manuscript.md lines 2061–2151) — boss encounter start
- Evidence: manuscript.md:909–911, 1265, 2131, 2165; DS-Core-Rules-lores.txt p.28 ('Then place the Aggro token on one of the characters, and place the boss model on the Mini Boss Spawn node'); DS-BDK-Rules-web.txt p.12 ('front arc facing the centre')
- Current text: Bosses always directly face an adjacent node.
- Proposed fix: At the start of a boss encounter, place the characters on the entry nodes beside the fog gate doorway and the boss on its spawn node with the centre of its front arc facing the adjacent node closest to the entry nodes.
- Rationale: The boss's initial facing determines which arcs are weak and which characters are in range; no rule sets it, and the chapter never states the placement step at all.
- Gameplay impact: First boss turn of every boss fight.
- Decision needed: N

### B-004 · scaling · Major · PROPOSED
- Location: L1527 and table row 3 (Enemy Scaling)
- Evidence: +1 attack at 3 characters raises Hollow Soldier expected damage from 1.67 to 2.67 (+60%) and removes the zero-damage block outcome (P(0) 0.111 -> 0). The health step (+1) is a +33% change at the same player count. Three characters also absorb three times the enemy activations of one character because all enemies act between every character turn (L1297-1311).
- Current text: If playing with three or more characters, increase all non-boss attack values by one. [table: 3 | Base + 2 | 1 -> 2 | +1 | -]
- Proposed fix: "If playing with four characters, increase all non-boss enemy attack values by one." Table: row 3 "3 | Base + 2 | 1 -> 2 | - | -"; row 4 "4 | Base + 3 | 1 -> 2 | +1 | -".
- Rationale: Moves the attack step to the player count where the party has the most defensive redundancy and keeps each step of the table roughly equal in expected-damage terms.
- Gameplay impact: 3-player encounters return to 1-2 player per-hit lethality while keeping +2 health per enemy.
- Decision needed: Y

### B-012 · undefined-value · Major · REQUIRED
- Location: L1197 (Objective & Loss Conditions) with L1223 and L1341 (forced rest)
- Evidence: A failed encounter 'forces' the party to spend one spark and rest. The loss condition only triggers when all characters are dead and no sparks remain. The state 'hollow character dies, survivors standing, spark dial at 0' is undefined: the forced rest cannot be paid. Spark budgets: 4 players have three paid rests in the whole basic game.
- Current text: The players lose collectively if at any point, all characters are dead and there are no remaining sparks to revive them.
- Proposed fix: "The players lose the game when an encounter is failed and the spark dial shows zero."
- Rationale: A failed encounter always demands a spark; defining the loss at that moment closes the gap and matches official 1E (Core p.8: once the dial reads 0, the next time a character is killed the game is lost).
- Gameplay impact: Makes the end state deterministic; no numeric change.
- Decision needed: N

### B-015 · table-text-mismatch · Major · REQUIRED
- Location: L781 (Endurance Bar) and L1215-1219 (Death & Hollowing)
- Evidence: Manuscript: endurance bar 'total of eight stamina/damage cubes', hollow reduces to six. Official 1E boards have ten boxes (Core p.20: 'If all ten of a character's endurance bar boxes have cubes'; Herald board image p.11). Hollowed Edition p.5 applies the same two cubes to the official ten-box bar. Every survivability figure in B_report assumes eight.
- Current text: The effect of these *hollow* markers is to reduce the functional capacity of the endurance bar from a total of eight stamina/damage cubes to only six.
- Proposed fix: Either (a) "from a total of ten stamina and damage cubes to eight" if official dashboards are used, or (b) state in Game Components that Second Edition dashboards have an eight-space endurance bar.
- Rationale: The number must match the physical component the players own; nothing in the manuscript announces new dashboards.
- Gameplay impact: Two boxes = 25% of capacity; with ten boxes the 4-player Repeat Hollow Soldier one-activation kill chance drops from 5.8% to 0.1%.
- Decision needed: Y

### C-019 · hedge · Major · REQUIRED
- Location: L765; L793; L979; L1131; L1159; L1201; L1880; L1963; L2065; L2169
- Evidence: 10 'should' in procedural rules, e.g. L1131 'Encounter levels should increase from the tile adjacent to The Bonfire tile'; L2065 'the fog gate tile should be removed... and placed on the bonfire tile'; L1880 'the character should mark the equipped item with a red damage cube'; L765 'players should not interact with their character's inventory cards'
- Current text: should
- Proposed fix: must / imperative: 'Encounter levels must increase from the tile adjacent to the bonfire tile towards the mini-boss tile.' / 'Move the fog gate token from the boss tile's entrance to the bonfire tile.' / 'Mark the equipped card with a red damage cube.' / 'During an encounter a character may not access their inventory.' Full list in C_report.md Task 2.
- Rationale: These are mandatory steps; 'should' makes them optional.
- Gameplay impact: Setup order, fog-gate shortcut, inventory access and scaling marker become mandatory as intended
- Decision needed: N

### C-033 · italics · Major · REQUIRED
- Location: L1399; L1890; L1906; L2235; L1397; L1277; L3056; L2175; L2017; L1985
- Evidence: Undefined keywords: '*lost*' used at 1890/1906/2235 ('lost to the hollow', 'revives lost characters who have been removed from play due to dying while hollow') but never defined and conflicts with L1223 (hollow death forces a rest, no removal) and L1195 (mega-boss death = permanent removal); 'mastering the encounter' (1397) undefined; '*first player* token' (1277) placed but never used and not a component; 'First turn token' (3056) different name for same thing; boss '*leaps*' (2175) icon undefined; 'Heat Up value' for invaders (2017) undefined on invader cards; 'entrance node' (1985)
- Current text: lost / mastering / first player token / leaps
- Proposed fix: Define *lost* once (proposed: 'A character who dies while *hollow* is *lost*: remove the model from play until the party next rests at the *bonfire*'), then make L1223, L1906 and L1195 agree; delete 'mastering'; either define the first player token's effect or delete L1277 and use 'first player' in PvP only; define *leap*; use 'entry node'.
- Rationale: A term used as a keyword must be defined once.
- Gameplay impact: Whether a hollow character's death removes it from play or ends the encounter
- Decision needed: Y

### C-035 · terminology · Major · REQUIRED
- Location: L775; L1215; L1205
- Evidence: 'A character's stamina bar tracks their stamina and damage' (775); 'Place two white cubes on the right side of the stamina bar' (1215); 'cannot add a damage cube to their endurance tracker' (1205); 'endurance bar' x14 elsewhere incl. heading L773
- Current text: stamina bar / endurance tracker
- Proposed fix: endurance bar
- Rationale: The bar tracks both stamina and damage; 'stamina bar' misdescribes it. Official term is 'endurance bar' (Core/TG x21).
- Gameplay impact: None once standardised
- Decision needed: N

### C-036 · terminology · Major · REQUIRED
- Location: L1285; L1291; L1293; L1850
- Evidence: 'the model with the most damage tokens' (1285); 'the character who placed the most damage tokens on enemy models' (1291, 1293); 'place a number of damage tokens onto the target enemy model's base' (1850) vs 'wound token' (681, 1517, 1664, 2099) and 'damage cubes' for characters (x16)
- Current text: damage tokens
- Proposed fix: wound tokens (enemies); damage cubes (characters)
- Rationale: Two components, two names: enemies take wound tokens (L1517), characters take red damage cubes (L779). 'Damage token' is neither.
- Gameplay impact: Avoids confusion between the two damage-tracking components
- Decision needed: N

### C-048 · terminology · Major · REQUIRED
- Location: L1393; L805; L891; L919; L2239; L989; L1095
- Evidence: 'Successfully defeated invaders provide additional *souls* per player' (1393) vs Soul Reward Table 'per character' (1411); 'when that player discards an ember card' (805); 'stored in a player's inventory' (891); 'characters must choose a friendly model to push' (919 - a decision); 'If a player character leaves the characters' (2239). Note L989 'character dashboard(s)' and L1095 'character model(s)' allow one player to control several characters.
- Current text: per player / that player / player's inventory / characters must choose
- Proposed fix: Rule of use: PLAYERS decide, agree, choose and roll; CHARACTERS act, hold tokens, own cards and inventories, gain souls and die; MODELS occupy nodes, move and are pushed. L1393 -> 'per character'; L805 -> 'when that character discards'; L891 -> 'a character's inventory'; L919 -> 'the players must choose a friendly model to push'; L2239 -> 'If a player leaves, remove their character...'
- Rationale: When one player controls two characters, 'per player' and 'per character' pay different soul rewards.
- Gameplay impact: Soul rewards for invaders in 1-2 player games
- Decision needed: N

### C-050 · terminology · Major · REQUIRED
- Location: L781; L805; L1215; L1231; L1367; L1379; L1898; L3074; L771; L993; L1914; L689
- Evidence: 'block off the two furthest right spaces... with a marker such as white cubes. The effect of these *hollow* markers' (781); 'discard any *hollow* tokens' (805, 1379); 'Place two white cubes' (1215, 1367); 'Remove all *hollow* cubes' (1231, 1898, 3074). 'White cubes' are also the stat cubes (771, 993, 1914) and the component list has exactly 16 stat tier cubes (689) = 4 characters x 4 stats, none spare.
- Current text: hollow markers / hollow tokens / hollow cubes / white cubes
- Proposed fix: 'hollow cube' throughout; add a component line '8x Hollow cubes (white)' or specify the colour and source of the marker once in §Death & Hollowing
- Rationale: One component, four names; and the marker is not in the component list.
- Gameplay impact: Players may be short of markers; 'white cube' is ambiguous with stat cubes
- Decision needed: Y

### C-056 · terminology · Major · REQUIRED
- Location: L1477; L2055; L3182
- Evidence: 'award a Titanite Chunk card to any character who killed a *crystal lizard*' (1477) vs 'they immediately place one Titanite Scale card into their inventory' (2055). Iron Keep booklet: '3x Titanite Scale Cards', 'add one Titanite Scale card to the inventory'. Community Update Pack (3182) defines Titanite Chunk as a common +2 upgrade replacing Titanite Shard.
- Current text: Titanite Chunk (L1477)
- Proposed fix: Titanite Scale
- Rationale: Two different cards named for the same reward; official component is the Titanite Scale.
- Gameplay impact: Which card a crystal-lizard kill awards
- Decision needed: N

### C-064 · terminology · Major · REQUIRED
- Location: L543; L1967; L1969; L1971; L3052; L805; L1239
- Evidence: 'Phantoms' heading (543) covers Invaders and Summons; chapter 'SUMMONS' (1967) contains both 'Phantoms' (= summons only, 1969-1993) and 'Invaders' (1995); 'summon a random friendly phantom' (1971); 'Phantoms (Summons and Invaders)' (3052); 'enable the character to summon phantoms, but also attract malicious invaders' (805)
- Current text: Phantoms (two senses); chapter SUMMONS
- Proposed fix: *phantom* = umbrella (summons and invaders); *summon* = friendly phantom; *invader* = hostile phantom. Rename chapter 'PHANTOMS' with sections 'Summons' and 'Invaders'; L1969 heading -> 'Summons'.
- Rationale: The same word names the superset and one subset within two pages.
- Gameplay impact: Reader confusion over which rules apply to invaders
- Decision needed: N

### C-087 · cross-ref · Major · REQUIRED
- Location: L963; L1461; L1479; L2043
- Evidence: Chest treasure tie-break: 'If they cannot decide, the treasure should be awarded to a randomly selected character' (963) vs 'If the players cannot decide, the treasure will be awarded to the character who ended the encounter with the *aggro* token' (1461, 1479); mimic chest decision deadlock 'the character with the *aggro* token makes the final decision' (2043)
- Current text: randomly selected character (963)
- Proposed fix: State the tie-break once (recommended: aggro-token holder) in §Treasure Rewards and have §Chests cite it.
- Rationale: Two sections give different resolutions for the same deadlock.
- Gameplay impact: Who receives contested treasure
- Decision needed: Y

### C-088 · cross-ref · Major · REQUIRED
- Location: L1223; L1906; L1195; L1341
- Evidence: Hollow death: 'any character with *hollow* status dies, then the characters are forced to immediately spend one *spark* and rest' (1223, 1341) vs 'revives *lost* characters who have been removed from play due to dying while *hollow*' (1906) vs mega-boss 'If a character dies they are permanently removed from play' (1195)
- Current text: (three statements)
- Proposed fix: Make §Death & Hollowing the single source: define *lost*, state the forced rest, and have §Resting at the Bonfire and §Setup After the main-boss cite it (with the mega-boss exception stated as an exception).
- Rationale: Three sections describe the same event with different consequences.
- Gameplay impact: Whether the encounter ends immediately when a hollow character dies
- Decision needed: Y

### C-119 · voice · Major · REQUIRED
- Location: L1205-1253; L1299-1399; L1445-1479; L1935-1949; L859-887; L931-981; L1604-1658; L2243-2293; L2314-2322; L3040-3094
- Evidence: Rules stated as bullet fragments: Death & Hollowing, Embering, Sparks (1205-1253); Encounter Resolution/Recovery, Souls (1299-1399); Treasure Rewards (1445-1479); Shop Rules (1935-1949); Spells (859-887); Terrain (931-981); Conditions (1604-1658); campaign Soul/Treasure Rewards and Shop (2243-2322); the whole PLAYER VS PLAYER chapter (3040-3094) is 27 bullets with no sentence structure
- Current text: - Encounters are *failed* if either all characters die.
- Proposed fix: Policy: PROCEDURES (setup, turn sequence, defence rolls, encounter start, resting, transposition) = numbered steps; DEFINITIONS and component anatomies (dashboard parts, data-card fields, condition effects, terrain) = bulleted lists of complete sentences; RULES (everything else) = short declarative paragraphs in 'When [trigger], [subject] must/may [action].' form. Rewrite PvP as prose plus a dodge table.
- Rationale: Fragments omit the trigger and subject that lawbook syntax requires ('Encounters are failed if either all characters die' has a dangling 'either').
- Gameplay impact: None
- Decision needed: Y

### D-007 · hybrid · Major · REQUIRED
- Location: manuscript.md 1195 vs 1201 (Objective & Loss Conditions)
- Evidence: BDK/EC p.10 apply the standard boss rules (party defeated → rest at the bonfire, spark spent). The manuscript's Objective says the players lose only when all characters are dead and no sparks remain, but the mega-boss step says a character who dies is permanently removed and all dead = loss regardless of sparks.
- Current text: If a character dies they are permanently removed from play. If all characters die, the players lose the game.
- Proposed fix: A character who dies in the mega-boss encounter is removed from play for the remainder of that encounter. If every character dies, the encounter is failed and the characters rest at the bonfire at the cost of one spark; the mega-boss encounter is then set up again.
- Rationale: Reconciles the mega-boss rule with the manuscript's own loss condition and with the official mega-boss booklets; the alternative is to keep sudden death and amend the Objective.
- Gameplay impact: Decides whether sparks matter in the final fight.
- Decision needed: Y

### D-028 · underspecified-deviation · Major · REQUIRED
- Location: manuscript.md 1477 (Treasure Rewards) vs 2055 (Crystal Lizards)
- Evidence: IK p.3: 3x Titanite Scale cards; IK p.5: one Titanite Scale is added to the inventory only when every lizard in an encounter is killed before the encounter is cleared, and the icon is ignored once the three cards are gone. The manuscript awards a card per lizard killed, names it 'Titanite Chunk' at 1477 and 'Titanite Scale' at 2055, and does not say what happens when the three cards are exhausted.
- Current text: award a Titanite Chunk card to any character who killed a crystal lizard during the encounter … they immediately place one Titanite Scale card into their inventory
- Proposed fix: Whenever a character kills a crystal lizard, that character takes one Titanite Scale card from the supply. When no Titanite Scale cards remain, crystal lizards are no longer placed during encounter setup.
- Rationale: Unifies the name with the printed card and closes the supply gap created by the per-kill award.
- Gameplay impact: Upgrade economy with Iron Keep.
- Decision needed: Y

### D-035 · underspecified-deviation · Major · REQUIRED
- Location: manuscript.md 1347 (Encounter Recovery) vs 2043 (Mimics)
- Evidence: Core p.19 and HE p.6 both restore all health after a victory; the manuscript's partial heal is original and is stated as one damage cube at 1347 but 'two damage' at 2043.
- Current text: Remove one damage cube from each character. … they proceed to recover all stamina and two damage normally.
- Proposed fix: Characters who survive to clear an encounter remove one damage cube and all stamina cubes.
- Rationale: One value must be chosen; the author decides which was playtested.
- Gameplay impact: Attrition pacing across a dungeon.
- Decision needed: Y

### F-014 · tone · Major · CLEAN-UP
- Location: L1201 §Gameplay › Objective & Loss Conditions
- Evidence: Tone slip: 'to determine a single intimate victor'; advisory 'Players should agree'
- Current text: Players may also choose to add a player versus player (PvP) encounter after the final boss is defeated to determine a single intimate victor. Players should agree on whether they will include a mega-boss and/or PvP encounter during set-up.
- Proposed fix: REWRITE-IN-VOICE: 'The party may add a player-versus-player encounter after the final boss to determine a single champion (see §20). Both options are chosen during setup.'
- Rationale: 'intimate victor' is an error for 'ultimate victor' and in any case a tone slip; 'should agree' is advice where a setup rule is meant.
- Gameplay impact: none
- Decision needed: N

### F-086 · register-shift · Major · CLEAN-UP
- Location: L919, L1461, L1479, L2043, L1245 vs L2233, L1201, L1107
- Evidence: Actor shifts between 'players' and 'characters' for the same kind of decision: 'the players must push one of the three models… characters must choose a friendly model' (L919); 'Players decide which character should receive' (L1461) vs 'Characters must collectively decide' (L2043); 'Players begin sparks equal to' (L1245) vs 'The characters start a campaign with the same number of sparks' (L2233).
- Current text: Multiple models can share the same node… the players must push one of the three models already on the node. characters must choose a friendly model to push…
- Proposed fix: Apply the actor policy (Voice Guide §3): characters act in the game world (move, attack, spend, die); players make rules decisions where the game asks for a human choice; 'the party' for a collective decision. E.g. L919: 'If a fourth model enters a node, the party chooses a friendly model to push; an enemy pushes another enemy if able.'
- Rationale: Clarity of who acts; also removes the lower-case sentence starts ('characters must…' L919, L1931, L2069, L2155, L2185, L2207).
- Gameplay impact: none
- Decision needed: N

### F-089 · tone · Major · CLEAN-UP
- Location: L765, L979, L1131, L1159, L1201, L1461, L1479, L1666, L1880, L2065, L2169, L2596 ff.
- Evidence: 'should' used as a rule modal: 'players should not interact with their character's inventory cards' (L765); 'Players should fill the basic nodes furthest from the tiles entry' (L979); 'Encounter levels should increase' (L1131); 'the character should mark the equipped item' (L1880); 'the fog gate tile should be removed' (L2065); 'The target character model should remain static' (L2169); 'players should add the Explorers and Characters expansions if available' (campaign headers ×9).
- Current text: Once the encounter has started players should not interact with their character's inventory cards.
- Proposed fix: Modal policy (Voice Guide §2): 'must' for obligations, 'may' for permissions, 'cannot' for prohibitions, 'is/are' for states. E.g. 'During an encounter the inventory cannot be accessed.'; 'Trap tokens are placed first on the basic nodes furthest from the entry.'; 'Encounter levels increase from the tile adjacent to the *bonfire* tile towards the boss tile.'; 'Mark the item with a red cube.'; campaign headers: 'Recommended additions: Explorers, Characters.'
- Rationale: 'should' is advisory and leaves the rule optional.
- Gameplay impact: none
- Decision needed: N

### A-004 · undefined-state · Minor · OPTIONAL
- Location: GAMEPLAY › Death & Hollowing (manuscript.md line 1213)
- Evidence: manuscript.md:1213, 1223, 1003
- Current text: If any character survives to clear an encounter, then the characters who died in that encounter are revived in a hollow state.
- Proposed fix: A character adventuring alone never becomes hollow: when that character dies, the encounter is failed and the character must spend a spark to rest at the bonfire.
- Rationale: The revival branch requires a surviving character; a solo death therefore always falls to the failed-encounter branch, which costs a spark. Stating this explicitly removes the question of whether a solo character ever hollows.
- Gameplay impact: Solo players need to know that every death costs a spark (the official 1E outcome).
- Decision needed: N

### A-005 · contradiction · Minor · REQUIRED
- Location: GAMEPLAY › Death & Hollowing (manuscript.md line 1221) vs Resting at The Bonfire (line 1898), Boss Death (line 2195), PvP (line 3046)
- Evidence: manuscript.md:1221, 1898, 1908, 2195, 3046
- Current text: Hollow status is only removed by using a spark or an ember token.
- Proposed fix: Hollow status is removed only by resting at the bonfire or by becoming embered.
- Rationale: Resting after a boss (2195) and before PvP (3046) costs no spark yet removes hollow cubes (1898). The restriction must name the rest, not the spark.
- Gameplay impact: Literal reading leaves characters hollow after the free post-boss rest.
- Decision needed: N

### A-007 · undefined-state · Minor · PROPOSED
- Location: GAMEPLAY › Embering (manuscript.md line 1243); Shop Rules (line 1949); Boss Death (line 2195)
- Evidence: manuscript.md:1243, 1949, 2195
- Current text: Characters cannot carry an ember card while embered.
- Proposed fix: When a character becomes embered while holding an ember card, that character must immediately give the ember card to another character who is neither embered nor holding an ember card. If no such character exists, the ember card is returned to the tier one shop.
- Rationale: Boss Death embers every character at once (2195), so a character holding an ember card is placed in an illegal state with no resolution. Alternative: return the card to the game box.
- Gameplay impact: Rare but guaranteed to arise after the first boss when a character has bought an ember.
- Decision needed: Y

### A-010 · procedural · Minor · REQUIRED
- Location: COMBAT BASICS › Conditions › Frostbite (manuscript.md line 1626) vs CHARACTER TURN › Recover one stamina (line 1802), Rest (line 1826), Encounter Recovery (lines 1349–1351)
- Evidence: manuscript.md:1626, 1630, 1802, 1826, 1349–1351; DS-TG-Rulebook p.21 (frostbitten characters recover one less stamina)
- Current text: Frostbite affected characters cannot recover stamina.
- Proposed fix: A frostbitten character does not recover stamina at the start of their turn and may not take the Rest major action. At the end of an encounter, condition tokens are removed before stamina cubes are removed.
- Rationale: The mandatory 'Recover one stamina' step and the Rest action are both stamina recovery; the text must say that both are blocked. Encounter Recovery lists stamina removal before condition removal, so a frostbitten survivor is blocked from the end-of-encounter recovery by the literal order.
- Gameplay impact: Clarifies a condition that otherwise silently disables a whole turn step.
- Decision needed: N

### A-014 · undefined-state · Minor · OPTIONAL
- Location: SETUP › Character Setup step 7 (manuscript.md line 1001); Encounter Start step 8 (line 1275); Encounter Turn Order step 2 (line 1289)
- Evidence: manuscript.md:1001, 1275, 1289, 3056–3058
- Current text: Each character takes their turn one-by-one in descending threat value.
- Proposed fix: If two or more characters share a threat value, the players choose which of them receives the aggro token and the order in which the tied characters take their turns.
- Rationale: Several character dashboards share threat values; no tie-break is given for either the aggro assignment or the turn order.
- Gameplay impact: Common with two characters of the same class family; cheap to fix.
- Decision needed: N

### A-015 · undefined-state · Minor · OPTIONAL
- Location: GAMEPLAY › Encounters › Encounter Turn Order step 3 (manuscript.md line 1291)
- Evidence: manuscript.md:1291–1293, 2019, 2035
- Current text: ...the character who placed the most damage tokens on enemy models.
- Proposed fix: After all characters have taken their turns, place the aggro token on the character who inflicted the most damage on enemy models during that round, counting damage recorded on an invader's or boss's health dial as well as damage tokens.
- Rationale: Invaders track damage on a dial, not with tokens; the literal measure excludes damage to invaders. The phrase 'that round' is also needed so that cumulative damage is not counted.
- Gameplay impact: Prevents the aggro token ignoring the character fighting the invader.
- Decision needed: N

### A-017 · omission · Minor · REQUIRED
- Location: GAMEPLAY › Encounters › Encounter Start step 9 (manuscript.md line 1277); PLAYER VS PLAYER (line 3056)
- Evidence: manuscript.md:679–723 (no such component), 1277, 1289, 3056; DS-Core-Rules-lores.txt p.7 (1x First Activation Token exists officially)
- Current text: Place the first player token on the character with the highest threat value.
- Proposed fix: Delete Encounter Start step 9. In PLAYER VS PLAYER replace the first turn token bullet with: Characters take their turns in descending threat order; ties are broken by the players' choice.
- Rationale: The first player token is not in the component list and is never used: character order is fixed by threat value (1289), so the token has no function. PvP calls the same object a 'First turn token'.
- Gameplay impact: Removes a phantom component and a contradiction between two names.
- Decision needed: N

### A-022 · undefined-state · Minor · OPTIONAL
- Location: BOSS TURNS › Boss Turn Overview (manuscript.md line 2157) vs Encounter Turn Order step 2 (line 1289)
- Evidence: manuscript.md:1289, 2157
- Current text: After each boss turn, one character may take their turn, then the boss takes another turn, a second character, and so-on.
- Proposed fix: In boss encounters the players choose which living character takes each character turn, subject to the equal-turns rule. The descending threat order of ordinary encounters does not apply.
- Rationale: Ordinary encounters fix character order by threat (1289); boss encounters say 'one character may take their turn', which implies free choice without saying so. Alternative: apply threat order in boss encounters as well.
- Gameplay impact: Determines whether players can sequence the healer after the tank in boss fights.
- Decision needed: Y

### A-034 · undefined-state · Minor · OPTIONAL
- Location: PLAYER VS PLAYER (manuscript.md lines 3050, 3076–3078)
- Evidence: manuscript.md:1213, 1357, 3046, 3050, 3076–3078
- Current text: Dead characters are excluded from PvP. ... Victory on non-final bosses provides +1 attack damage in future PvP only.
- Proposed fix: The PvP encounter is played after dead characters have been revived and every character has been restored as if rested. A PvP encounter with fewer than two living characters is not played. Record a PvP victory by placing a 1-soul token from the supply on the champion's dashboard; in later PvP encounters the champion adds one to the attack value of every attack against a character.
- Rationale: Clearing a boss revives the dead as hollow (1213) and PvP restores everyone (3046), so 'dead characters are excluded' is unreachable; and no marker is defined for the +1 bonus.
- Gameplay impact: Removes an unreachable rule and gives the bonus a physical tracker.
- Decision needed: N

### A-047 · undefined-state · Minor · OPTIONAL
- Location: GAMEPLAY › Sparks (manuscript.md lines 1247–1253); Boss Death (line 2195)
- Evidence: manuscript.md:715, 1093, 1249, 2195, 2233; DS-Core-Rules-lores.txt p.33 (campaign maximum = starting sparks)
- Current text: Defeating a mini-boss or main-boss provides one additional spark.
- Proposed fix: The spark dial never shows more sparks than the characters' starting number; a spark gained beyond that maximum is lost.
- Rationale: The campaign chapter sets this maximum (2233) but the basic game does not; a solo character would reach six or seven, beyond the physical dial. Alternative: no maximum, track overflow with a token.
- Gameplay impact: Solo and two-character basic games only.
- Decision needed: Y

### A-055 · undefined-state · Minor · REQUIRED
- Location: GAMEPLAY › Encounter Resolution (manuscript.md lines 1335–1339)
- Evidence: manuscript.md:1315, 1335–1339
- Current text: Failed encounters flip their encounter card face-down. ... Failed encounters may not be skipped once reset.
- Proposed fix: When an encounter marked cleared is subsequently failed, remove the cleared marker; the encounter is treated as never having been cleared.
- Rationale: A cleared encounter that is later repeated and failed keeps its black cube under the literal text, so 'may not be skipped once reset' and 'cleared encounters may be skipped' both apply. Alternative: the marker remains and the encounter stays skippable.
- Gameplay impact: Occurs whenever a party farms a cleared tile and wipes.
- Decision needed: Y

### A-056 · terminology · Minor · CLEAN-UP
- Location: RETURNING TO THE BONFIRE › Resuming Exploration (manuscript.md line 1963); Terrain › Traps (line 977)
- Evidence: manuscript.md:977, 1317, 1337, 1963
- Current text: flip all cleared and failed encounter tiles face-down to reset them.
- Proposed fix: Reset: an encounter is reset by turning its encounter card face-down and setting aside any enemy models; terrain, trap and chest tokens remain in place. Replace 'encounter tiles' with 'encounter cards' at line 1963.
- Rationale: Tiles are double-sided boards; flipping them would change the map. 'Reset' is used four times without a definition.
- Gameplay impact: Cosmetic but a literal reading flips the map.
- Decision needed: N

### A-058 · contradiction · Minor · REQUIRED
- Location: GAMEPLAY › Treasure Rewards (manuscript.md line 1471) vs Terrain › Chests (line 961) and Encounter Start step 7 (line 1273)
- Evidence: manuscript.md:961, 1273, 1459, 1471, 2045
- Current text: If the ambush card shows treasure, they collect one treasure card from the appropriate tier treasure deck.
- Proposed fix: If the ambush card shows treasure, reveal the treasure card placed beneath the chest token and award it as for an ordinary chest.
- Rationale: Chests carry a pre-placed card (961, 1273, 1459); the mimic branch draws a fresh one instead, leaving the pre-placed card unresolved.
- Gameplay impact: Small duplication of treasure when mimics are used.
- Decision needed: N

### A-059 · contradiction · Minor · REQUIRED
- Location: Terrain › Chests (manuscript.md line 963) vs Treasure Rewards (lines 1465–1469) and MIMICS (line 2043)
- Evidence: manuscript.md:963, 1465, 1469, 2043
- Current text: the players must flip the chest permanently to its open side / If any surviving character wishes to open a chest after an encounter ends, they must reveal the ambush card / If the characters cannot agree, the character with the aggro token makes the final decision.
- Proposed fix: Without mimics, a chest is opened automatically when the encounter is cleared. With mimics, the surviving characters decide collectively whether to open the chest; if they cannot agree, the character holding the aggro token decides.
- Rationale: Three passages give three decision rules (automatic; any single character; collective with aggro tie-break).
- Gameplay impact: Table disputes about who may force a mimic check.
- Decision needed: N

### A-062 · loop/exploit · Minor · OPTIONAL
- Location: GAMEPLAY › Encounter Resolution (manuscript.md lines 1321–1327)
- Evidence: manuscript.md:1267, 1321–1327, 1391, 2057
- Current text: Encounters cleared that have already been cleared resolve as follows: ... Characters gain soul rewards but not treasure.
- Proposed fix: A cleared encounter may be repeated at most once between two rests at the bonfire.
- Rationale: Nothing limits re-fighting a cleared tile; with only one damage healed per clear the loop is self-limiting but still permits indefinite soul farming of a weak encounter. Alternative: no limit (risk-based self-limiting).
- Gameplay impact: Prevents grinding, which the Second Edition Notes name as a design goal.
- Decision needed: Y

### A-063 · omission · Minor · REQUIRED
- Location: GAMEPLAY › Encounters (manuscript.md lines 1255–1341); MIMICS (line 2043)
- Evidence: manuscript.md:1255–1341, 1890, 2043
- Current text: The then are faced with the typical option of continuing onto the next encounter or returning to rest at the bonfire for the cost of one spark.
- Proposed fix: After an encounter is cleared, the characters choose either to continue to an adjacent tile or to return to the bonfire tile and rest, spending one spark.
- Rationale: The 'typical option' is referred to only inside the Mimics chapter; the Encounters chapter never states that a voluntary return is possible between encounters.
- Gameplay impact: The core exploration decision is undocumented in the chapter that owns it.
- Decision needed: N

### A-105 · undefined-state · Minor · OPTIONAL
- Location: CAMPAIGN PLAY › Adding & Dropping Players (manuscript.md line 2239)
- Evidence: manuscript.md:765, 1385–1387, 2239; DS-Core-Rules-lores.txt p.33
- Current text: New players can join a campaign that is in progress at the cost of one spark each. ... the character's equipment is added to the inventory
- Proposed fix: A new player may join only while the spark dial shows at least one spark. When a character leaves, their equipment cards are distributed among the remaining characters' inventories as the players choose, and their souls are returned to the supply.
- Rationale: The manuscript has personal inventories and personal souls (765, 1387), so the official communal-inventory sentence no longer resolves; joining at zero sparks is unaddressed.
- Gameplay impact: Rare.
- Decision needed: N

### A-112 · terminology · Minor · CLEAN-UP
- Location: GAMEPLAY › Souls (manuscript.md line 1397)
- Evidence: manuscript.md:1301, 1397
- Current text: The character who dropped them by successfully clearing or mastering the encounter on which they were dropped can reclaim dropped souls.
- Proposed fix: A character reclaims their dropped souls by surviving to clear the encounter on the tile where they were dropped.
- Rationale: 'Mastering' is used once and never defined; only 'cleared' and 'failed' outcomes exist.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-113 · terminology · Minor · CLEAN-UP
- Location: GAME COMPONENTS › Tokens (manuscript.md line 681); Encounter Turn Order (line 1285); Character Attacks (line 1850); Enemy Turn Overview (line 1664)
- Evidence: manuscript.md:681, 1285, 1291, 1517, 1664, 1850
- Current text: Wound tokens / damage tokens / wounds
- Proposed fix: Use 'wound token' throughout for the tokens placed on enemies and 'damage cube' for the red cubes on endurance bars.
- Rationale: Three terms for one component.
- Gameplay impact: Cosmetic.
- Decision needed: N

### A-121 · undefined-state · Minor · OPTIONAL
- Location: GAMEPLAY › Souls (manuscript.md line 1389); Encounter Resolution (line 1313)
- Evidence: manuscript.md:1313, 1389, 1449
- Current text: reward the full soul reward to each character.
- Proposed fix: Every character, including characters who died during the encounter, receives the soul reward.
- Rationale: Treasure says 'even if they died' (1449); souls do not. Alternative: dead characters receive no souls.
- Gameplay impact: Small but frequent.
- Decision needed: Y

### A-125 · terminology · Minor · CLEAN-UP
- Location: CHARACTERS › Character Dashboards item 7 (manuscript.md line 745)
- Evidence: manuscript.md:745, 1289, 1515; DS-Core-Rules-lores.txt p.11 ('Taunt Level'); DS-Phantoms-Rules-lores.txt p.6
- Current text: Threat Level
- Proposed fix: Glossary: Threat – the value printed as 'Taunt' on official character dashboards and summon cards; the manuscript uses 'threat' for characters, phantoms and enemies alike.
- Rationale: Physical dashboards say Taunt; without the glossary note readers cannot find the character's threat value.
- Gameplay impact: Cosmetic.
- Decision needed: N

### B-009 · table-text-mismatch · Minor · REQUIRED
- Location: L1393 and L1415-1424 (Souls; Soul Reward Table row labels)
- Evidence: L1393 says invaders give 'additional souls per player' without a number; the only figures are the row labels 'Standard Invaders 3' and 'Advanced Invaders 4' inside the encounter table. Official 1E gives 3 souls to the shared cache for any invader (Phantoms p.15), i.e. 0.75 per character at 4 players; the manuscript gives 3-4 per character, 4-5x the official reward.
- Current text: Successfully defeated invaders provide additional *souls* per player.
- Proposed fix: "A defeated standard invader provides three souls to each character; a defeated advanced invader provides four souls to each character, in addition to the encounter reward."
- Rationale: States the figure in prose where the rule lives; the table alone is not a rule.
- Gameplay impact: Confirms an invader is worth a whole extra encounter per character; acceptable given invaders act after every character turn (L2027).
- Decision needed: N

### B-028 · economy · Minor · REQUIRED
- Location: L683 (Soul tokens) with L1383 (Souls are individual)
- Evidence: Supply 10x1 + 5x3 + 3x5 + 1x8 = 19 tokens, total face value 48 (the Core set's shared-cache supply, Core p.7). The manuscript makes souls individual and non-transferable; four characters each holding 15-20 souls (B_report §4.2) need 60-80 in face value.
- Current text: - 10x1, 5x3, 3x5, and 1x8 Soul tokens
- Proposed fix: Add after the token list: "Soul tokens are not limited. If the supply runs out, use any convenient counters or record souls on paper."
- Rationale: Individual soul tracking exceeds the printed supply in ordinary play.
- Gameplay impact: Avoids an artificial cap of 48 souls across the party.
- Decision needed: N

### B-029 · table-text-mismatch · Minor · REQUIRED
- Location: L689 (Stat tier cubes) with L781, L1215, L1367 (hollow markers 'white cubes')
- Evidence: 16 white cubes = 4 characters x 4 stats, all placed on dashboards at setup (L771). Hollow status is marked with two white cubes per hollow character; in a four-character game none are spare.
- Current text: When a character dies and is revived *hollow*, they block off the two furthest right spaces of the endurance bar with a marker such as white cubes.
- Proposed fix: "...block off the two furthest right spaces of the endurance bar with two hollow markers (use the Tier Four red cube from a stat track that has not reached tier four, or any two counters)." and add "8x Hollow markers" to the component list.
- Rationale: A marker must exist in the component list; white cubes are fully committed at four players.
- Gameplay impact: None.
- Decision needed: N

### B-030 · table-text-mismatch · Minor · REQUIRED
- Location: L1277 (Encounter Start step 9) and L3058 (PvP 'First turn token') vs component list L681-716
- Evidence: A 'first player' token (and in PvP a 'First turn token') is used but not listed among components. Core p.7 lists '1x First Activation Token'.
- Current text: 9.  Place the *first player* token on the character with the highest threat value.
- Proposed fix: Add "1x First player token" to Tokens & Terrain Elements; use the term "first player token" in both the Encounter Start and Player vs Player sections.
- Rationale: Component used in play must be listed; one term throughout.
- Gameplay impact: None.
- Decision needed: N

### B-032 · table-text-mismatch · Minor · REQUIRED
- Location: L1477 (Treasure Rewards, crystal lizards) vs L2057 (Crystal Lizards)
- Evidence: L1477 awards 'a Titanite Chunk card' for killing a crystal lizard; L2057 awards 'one Titanite Scale card'. Official Iron Keep rules (text lines 125-131) award a Titanite Scale; the manuscript's own errata list (L3126) redefines Titanite Chunk as a +2 upgrade that must replace a Shard.
- Current text: If playing with the option of *crystal lizards*, award a Titanite Chunk card to any character who killed a *crystal lizard* during the encounter.
- Proposed fix: "If playing with the option of crystal lizards, award one Titanite Scale card to any character who killed a crystal lizard during the encounter."
- Rationale: One reward name across both sections, matching the component list of the Iron Keep expansion (3x Titanite Scale cards).
- Gameplay impact: Prevents the +2 Chunk (a stronger upgrade) being handed out for an optional side-kill.
- Decision needed: N

### B-035 · balance · Minor · PROPOSED
- Location: L2047-2049 (Mimics) with L1455-1463 (Treasure Rewards, mimic ambush)
- Evidence: Characters 'do not recover stamina, remove damage ... until a decision is made' and then fight the mimic (Hungry Mimic health 18, heat-up 8, deck 4; Explorers text) from their end-of-encounter nodes with the stamina and damage they carry. After a 4-character scaled encounter this is typically 4-6 stamina and 2-4 damage already on an 8-box bar; the mimic acts first and needs about six activations to kill with starting weapons.
- Current text: Characters remain on the nodes they occupied at the end of the encounter containing the chest. The mimic will take its turn first.
- Proposed fix: "Characters remain on the nodes they occupied at the end of the encounter containing the chest and remove all stamina cubes, but no damage cubes, before the mimic takes its first turn."
- Rationale: Keeps the ambush dangerous (damage carries over) without starting the fight with characters unable to act.
- Gameplay impact: Mimic fights begin with full stamina; expected character deaths in the first mimic activation fall sharply at 3-4 players.
- Decision needed: N

### C-016 · spelling · Minor · CLEAN-UP
- Location: L1201
- Evidence: 'to determine a single intimate victor'
- Current text: intimate victor
- Proposed fix: ultimate victor
- Rationale: Wrong word.
- Gameplay impact: None
- Decision needed: N

### C-020 · hedge · Minor · REQUIRED
- Location: L963; L1461; L1479; L1664
- Evidence: 'the treasure should be awarded to a randomly selected character' (L963); 'Players decide which character should receive this treasure' (L1461, L1479); 'the players decide which model should go first' (L1664)
- Current text: should be awarded / should receive / should go first
- Proposed fix: is awarded / receives / takes its turn first (present indicative)
- Rationale: Decision outcomes are stated as facts, not advice.
- Gameplay impact: None (but see tie-break conflict row C-089)
- Decision needed: N

### C-022 · hedge · Minor · REQUIRED
- Location: L375; L377; L849; L1263
- Evidence: 'could' x4: L375 'that new players could use'; L377 'any sort of improvement that could be made'; L849 'a character could attach up to two weapon upgrade cards'; L1263 'the characters could skip to the fourth encounter but would all start with 6 stamina expended'
- Current text: could
- Proposed fix: L849: 'a character may attach up to two weapon upgrade cards to a weapon with an upgrade limit of two.' L1263: 'the characters may skip to the fourth encounter; each character begins it with six stamina cubes on their endurance bar.' L375/L377: front matter - cut or move to Foreword.
- Rationale: Permissions use 'may'; examples use the indicative.
- Gameplay impact: None
- Decision needed: N

### C-027 · italics · Minor · REQUIRED
- Location: L793; L1369; L1445; L1776; L1840; L1890; L1906; L1963; L2043; L2047; L2099; L2185; L2195
- Evidence: Punctuation inside italics: '*heroic actions, luck, and estus flask.*' (793); '*failed:*' (1369); '*cleared.*' (1445); '*Push, area-of-effect,*' (1776); '*dodge,*' and '*walk, run,*' (1840); '*hollow.*' (1890, 1906); '*failed),*' (1963); '*spark.*' (2043); '*cleared.*.' (2047); '*threat, block,*' (2099); '*, resist,*' (2185); '*embered.*' (2195)
- Current text: *cleared.* etc.
- Proposed fix: Italicise the term only; punctuation outside: '*cleared*.' - and italicise each term separately in lists: '*walk*, *run*,'
- Rationale: Keyword italics must not include punctuation or spaces; it breaks glossary linking and search.
- Gameplay impact: None
- Decision needed: N

### C-028 · italics · Minor · REQUIRED
- Location: L787; L1341; L1794; L1880; L2145; L3082
- Evidence: Split or partial italics: 'stagger*ed*' x2 (787); '*C*haracters' (1341); 'block*/*resist' (1794); 'attack option*s*' (1880); 'dodge*s*' (2145); 'attack option*'s*' (3082)
- Current text: stagger*ed*
- Proposed fix: *staggered*; Characters; *block*/*resist*; *attack options*; *dodges*; *attack option*'s
- Rationale: Italicise the whole inflected word or none.
- Gameplay impact: None
- Decision needed: N

### C-029 · italics · Minor · REQUIRED
- Location: L705; L1529; L1890; L1345; L3056; L1640; L1650; L1808-L1832
- Evidence: Italicised fragments/non-terms: '*4x Corrosion*' (705, repeats quantity); '*repeat to*' (1529); '*spark to*' (1890); '*clear an*' (1345); '*First* *turn*' (3056); headings '*Calamity (*Kalameet Expansion*)*' and '*Corrosion (*Gaping Dragon Expansion*)*' (1640, 1650); bold **AND**/**OR** connectors (1808-1832)
- Current text: *4x Corrosion*
- Proposed fix: '4x each of *calamity* and *corrosion* tokens'; '*repeat* to'; '*spark* to'; '*clear* an'; '*first player* token'; '*Calamity* (Kalameet expansion)'; replace AND/OR connectors with a numbered procedure
- Rationale: Italics mark glossary keywords only.
- Gameplay impact: None
- Decision needed: N

### C-030 · italics · Minor · REQUIRED
- Location: Whole body
- Evidence: Inconsistent keyword italicisation (italic/plain in rules text L361-3100): bonfire 39/79; soul 35/33; dodge 27/17; cleared 27/5; spark 25/16; ember 23/10; hollow 19/8; block 17/8; resist 15/6; aggro 14/10; luck 12/4; heroic action 11/5; attack option 10/5; threat 10/14; stamina 8/34; run 12/1; walk 8/0; shift 8/1; parry 7/0; push 2/49; heat-up 2/15; endurance bar 1/16
- Current text: *bonfire* ... the bonfire
- Proposed fix: Adopt one policy (recommended: italicise a glossary keyword at its first use in each H2 section and in headings/tables; plain thereafter) and apply it mechanically from the glossary headword list.
- Rationale: Readers cannot tell which words are defined terms; the Introduction (L381) promises every italicised term is in the glossary.
- Gameplay impact: None
- Decision needed: Y

### C-045 · terminology · Minor · REQUIRED
- Location: L771; L1451; L2314; L2316; L1920-1923; L1955-1956; L2303-2306; L2330-2331; L689; L1914; L2299
- Evidence: 'tier one/two' lower-case x60 in prose; 'Tier One/Two' x10 in table and heading labels; 'Tier one/two' mid-sentence (1451, 2314, 2316). Separately, 'tier' has two senses: stat tier (771 'from base tier to tier two', 1914) and treasure tier (1013 'tier two treasure deck').
- Current text: Tier one treasure deck (mid-sentence); 'tier two' (stat sense) unqualified
- Proposed fix: Lower-case 'tier one/two' in prose; Title Case only in headings and table row labels. Always qualify the stat sense as 'stat tier' ('stat tier two') and the treasure sense as 'tier two' ('tier two treasure', 'tier two shop').
- Rationale: Ambiguity: L771 'tier two' means a stat tier while L1013 'tier two' means a treasure deck.
- Gameplay impact: Misreading stat tiers as treasure tiers
- Decision needed: Y

### C-059 · terminology · Minor · CLEAN-UP
- Location: L969; L1017; L1021; L1025; L1029; L1201; L2055; L2748; L1473
- Evidence: 'set-up' x8 (noun), 'setup' x21 (noun), 'set up' (1473, verb)
- Current text: set-up
- Proposed fix: Noun 'setup' (and 'Setup' in headings); verb 'set up'
- Rationale: Standard British usage distinguishes noun and phrasal verb.
- Gameplay impact: None
- Decision needed: N

### C-060 · terminology · Minor · CLEAN-UP
- Location: L801; L1720; L1744; L1780; L1876; L1846; L3194; L763; L805; L1814; L891; L1201; L1908; L373-379; L2225
- Evidence: 'reroll' x8 vs 're-roll' x2 (1846, 3194); 'back-up slot' x2 vs 'backup slot' (891); 'PvP' x10 vs 'player versus player (PvP)' (1201) vs 'player-versus-player (PvP)' (1908); 'rule set'/'ruleset'/'rule-set'; 'rule book'/'rulebook'/'rule-book'
- Current text: (variants)
- Proposed fix: reroll; back-up slot; define 'player versus player (PvP)' once (L1201) then 'PvP'; ruleset; rulebook
- Rationale: One spelling per compound.
- Gameplay impact: None
- Decision needed: N

### C-061 · terminology · Minor · REQUIRED
- Location: L1517; L1850; L1295; L1301; L2053; L2195; L1223; L1305
- Evidence: Enemy death verbs vary: 'considered killed and removed from the tile' (1517); 'that enemy dies and is removed from play' (1850); 'all enemy models are defeated' (1295, 1301); 'the lizard is slain' (2053); 'the boss is slain' (2195). Characters 'die' (1223, 1305).
- Current text: killed / dies / defeated / slain
- Proposed fix: Characters 'die'; non-boss enemy models are 'killed' (and removed); bosses and encounters are 'defeated'/'cleared'. Replace 'slain' and enemy 'dies'.
- Rationale: Distinct verbs let rules refer unambiguously to character death (which has consequences) versus enemy removal.
- Gameplay impact: None
- Decision needed: Y

### C-062 · terminology · Minor · CLEAN-UP
- Location: L1985; L2065; L1179; L903; L1265
- Evidence: 'the boss tile's entrance node' (1985); 'the boss-tile entryway' (2065); 'placed at the entrance' (1179) vs 'entry node' (903, 1265)
- Current text: entrance node / entryway / entrance
- Proposed fix: entry node
- Rationale: Defined term at L903.
- Gameplay impact: None
- Decision needed: N

### C-063 · terminology · Minor · CLEAN-UP
- Location: L787; L701; L793; L1351; L1600
- Evidence: 'the appropriate condition marker' / 'a staggered condition marker' (787) vs 'condition token' x10
- Current text: condition marker
- Proposed fix: condition token
- Rationale: Component name.
- Gameplay impact: None
- Decision needed: N

### C-077 · table-text · Minor · CLEAN-UP
- Location: L679-723; L1277; L2205; L2055; L1997; L1137; L1975; L1315
- Evidence: Items used in rules but absent from Tokens & Terrain Elements: first player token (1277), pillar tokens (2205), Titanite Scale cards (2055), invader tokens and blank invader tokens (1997-2007), ambush cards (1137), phantom cards (1975), hollow cubes (781). L1315 'Mark the encounter card *cleared* with a black cube' uses a stamina cube as a marker.
- Current text: (absent)
- Proposed fix: Decide the scope of the component list (core only vs all supported content) and either add the expansion components under their expansion name or state that expansion components are listed in their own booklets; state that the cleared marker is a black stamina cube.
- Rationale: Component list is the reader's inventory check.
- Gameplay impact: None
- Decision needed: Y

### C-084 · cross-ref · Minor · CLEAN-UP
- Location: L837; L839; L841; L891; L1057; L1165; L1475; L1485; L1760; L1852; L2045; L2069; L2077; L2099; L2105; L2163; L2195; L2197; L2289; L2297; L2312
- Evidence: 21 prose cross-references resolved correctly but informally: 'explained in detail later on in the section title "Character Attacks"' (837, 'title' for 'titled'); 'section titled "Enemy Attacks"' (839); 'described later in more detail' (841); 'aforementioned effects' (891); 'as above' (1057, 1760); 'as previously described' (1165, 2195); 'later in these rules' (1475); 'detailed later' (1485); 'explained above/previously' (1852); 'per normal treasure chest rules' (2045); 'as described previously' (2069); 'will follow' (2077); 'previously described' (2099, 2163); 'as detailed during the setup chapter' (2105); 'as described earlier' (2197); 'as in the basic rules' (2289, 2297, 2312)
- Current text: (see Evidence)
- Proposed fix: Convert every one to the form '(see §N.N Heading)' once section numbers exist; drop 'later/earlier/previously/aforementioned'. Resolution table in C_report.md Task 6.
- Rationale: Positional words break when sections move; numbered references do not.
- Gameplay impact: None
- Decision needed: N

### C-091 · example · Minor · CLEAN-UP
- Location: L1261-1263
- Evidence: Rule: skip costs 'two stamina cubes... each character'. Example: 'if the first three encounters are marked *cleared* then the characters could skip to the fourth encounter but would all start with 6 stamina expended.' 3 x 2 = 6: arithmetic correct; wording hedged and numeral style mixed.
- Current text: could skip ... would all start with 6 stamina expended
- Proposed fix: 'Example: the first three encounters are *cleared*. The characters may skip to the fourth encounter; each character begins it with six stamina cubes on their endurance bar.'
- Rationale: Example verified; voice and numeral policy only.
- Gameplay impact: None
- Decision needed: N

### C-098 · heading · Minor · REQUIRED
- Location: L893; L983; L1059; L1441; L1842; L1882; L1910; L1925; L1959; L1965; L2049; L2059; L2215; L2308; L2324; L2336; L2400; L3036; L3096; L3100
- Evidence: 20 empty headings ('# ', '## ', '### ') used as page breaks
- Current text: #  (empty)
- Proposed fix: Delete all 20; page breaks belong to layout, not structure.
- Rationale: Empty headings produce blank TOC entries and broken numbering.
- Gameplay impact: None
- Decision needed: N

### C-103 · heading · Minor · CLEAN-UP
- Location: L1916/L2299; L1951/L2326; L2063/L2227; L1245/L2231; L633/L1119; L543/L1969; L385/L725; L985/L2219
- Evidence: Identical heading titles in different chapters: 'Stat Tier Costs' x2, 'Shop Price Table' x2, 'The Fog Gate' x2, 'Sparks' x2, 'Encounter cards' x2, 'Phantoms' x2, 'Characters' x2, 'Setup' x2
- Current text: Stat Tier Costs (x2)
- Proposed fix: Qualify the campaign versions: 'Stat Tier Costs (Campaign)', 'Shop Price Table (Campaign)', 'The Fog Gate in Campaigns', 'Sparks in Campaigns'; rename L633 'Encounter and Event Cards', L1969 'Summons', L385 'Character Classes'
- Rationale: Duplicate titles defeat '(see §Heading)' cross-references and index entries.
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

### C-107 · punctuation · Minor · REQUIRED
- Location: L1412; L1989
- Evidence: Stray 'i': 'per characteri' (1412, Soul Reward Table header); 'phantom behaviour deck.i' (1989)
- Current text: characteri / deck.i
- Proposed fix: character / deck.
- Rationale: Conversion or typing artefact.
- Gameplay impact: None
- Decision needed: N

### C-112 · punctuation · Minor · CLEAN-UP
- Location: L679; L895; L1199; L1203; L1710; L1766; L2161; L2201; L2237; L449; L2398
- Evidence: '&' in nine headings and in list items 'Mushroom Child & Parent' (449), 'Ornstein & Smough' (2398, 2500, 2660, 2934)
- Current text: &
- Proposed fix: 'and' in headings and prose; '&' only inside an official product or card name
- Rationale: Ampersand is a logo/label device, not prose.
- Gameplay impact: None
- Decision needed: N

### C-116 · punctuation · Minor · CLEAN-UP
- Location: L925; L1069; L1079; L1085; L1093; L1263; L1860; L1880; L1914; L2177; L2179; L2293; L2316; L2340; L1261
- Evidence: Numerals vs words mixed in prose: 'Range 0 / Range 1 / Range 2' (925); '3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells' (1069, 1079, 1085) vs 'two stamina cubes' (1261) and '6 stamina' (1263); 'six minus the number of characters' (1093); 'costs 0 Stamina' (1860); '5 greater' (1914); '90 degrees', '180 degrees' (2177-2179); '16 *souls*' (2293, 2316) vs 'sixteen souls' (2340). Number words in body: one x155, two x79, four x30, three x27, six x6, five x5, ten x3.
- Current text: 3 weapons ... 6 stamina ... sixteen souls ... 5 greater
- Proposed fix: Policy: words for zero to nine in running prose ('two stamina', 'three weapons'); numerals for 10 and above ('16 souls'), for every value in a table, for values with a sign or symbol ('+1', '≥ 25', '90°'), for dice counts beside icons, and for printed labels ('Level 1', 'Range 0'). Violations under this policy: 1069/1079/1085 (3, 3, 2, 2, 2 -> words), 1263 (6 -> six), 1860 (0 -> no), 1914 (5 -> five), 2340 (sixteen -> 16).
- Rationale: One policy; approximately 8 prose lines currently violate it.
- Gameplay impact: None
- Decision needed: Y

### C-122 · voice · Minor · CLEAN-UP
- Location: L1115; L1141; L1241; L1461; L1479; L2027; L2047; L2055; L2057; L1171; L2996
- Evidence: Future tense for rules: 'This will create a linear route' (1115); 'they would use only the encounters' (1141); 'Invaders will attempt to kill the characters' (1241); 'the treasure will be awarded' (1461, 1479); 'the invader will take many more turns' (2027); 'The mimic will take its turn first' (2047); 'the crystal lizards will respawn' (2055); 'no further crystal lizards will spawn' (2057); 'When all three section two options are complete, the players win' (2996, ok)
- Current text: will be awarded / will take / will respawn
- Proposed fix: Present indicative: 'is awarded', 'takes its turn first', 'respawn'.
- Rationale: Rules are timeless statements.
- Gameplay impact: None
- Decision needed: N

### C-124 · voice · Minor · REQUIRED
- Location: L1107; L1109; L1137; L1141; L2041; L2053; L1201; L3040
- Evidence: Optional rules are introduced inconsistently: 'if they wish... if they like' (1107); 'For added challenge the players may forgo choice' (1109); 'If playing with optional mimics for increased challenge' (1137); 'if they prefer more variety' (1141); 'may choose whether they wish to include mimics' (2041); 'as an optional game component' (2053); 'Players should agree on whether they will include a mega-boss and/or PvP' (1201); 'Decide during setup if PvP rules will be used' (3040)
- Current text: (eight phrasings)
- Proposed fix: One pattern: a boxed 'Optional rule: <name>' heading, then 'If the players choose this option during setup, ...'. List all options (random bosses, all-expansion decks, mimics, crystal lizards, mega-boss, PvP) once in §Setup.
- Rationale: Options are rules too; they need a fixed form.
- Gameplay impact: None
- Decision needed: N

### D-018 · component-count · Minor · REQUIRED
- Location: manuscript.md 679–723 (Tokens & Terrain Elements) vs 1277, 3056
- Evidence: Core p.7 lists 1x First Activation Token. The manuscript's component list omits it but uses a 'first player token' (1277) and a 'first turn token' (3056).
- Current text: (absent from list)
- Proposed fix: 1x First Activation token
- Rationale: Either list the token or delete the two references (characters act in threat order, so the token has no function outside PvP).
- Gameplay impact: None if removed.
- Decision needed: Y

### D-029 · underspecified-deviation · Minor · REQUIRED
- Location: manuscript.md 1397 (Souls)
- Evidence: 'Mastering' an encounter is used once and never defined; the resolution rules (1307–1341) know only 'cleared' and 'failed'.
- Current text: The character who dropped them by successfully clearing or mastering the encounter on which they were dropped can reclaim dropped souls.
- Proposed fix: A character reclaims dropped souls by surviving a clear of the encounter on whose tile the souls lie.
- Rationale: Removes an undefined term; the intended rule is already stated at 1311.
- Gameplay impact: None.
- Decision needed: N

### D-037 · underspecified-deviation · Minor · REQUIRED
- Location: manuscript.md 964 (Chests) vs 1461 (Treasure Rewards)
- Evidence: Two tie-break rules for an undecided chest treasure: random character (964) and the aggro holder (1461).
- Current text: If they cannot decide, the treasure should be awarded to a randomly selected character. … the treasure will be awarded to the character who ended the encounter with the aggro token.
- Proposed fix: If the players cannot agree, the treasure is awarded to the character holding the aggro token.
- Rationale: One rule; the aggro version is used twice (1461, 1479).
- Gameplay impact: None.
- Decision needed: Y

### D-038 · underspecified-deviation · Minor · REQUIRED
- Location: manuscript.md 1906 (Resting at The Bonfire) vs 1224 (Death & Hollowing)
- Evidence: 'Lost' characters 'removed from play due to dying while hollow' are revived by resting, but 1224 says a hollow death forces an immediate rest, so no character is ever 'lost' between encounters; the term is undefined.
- Current text: Resting at the bonfire also revives lost characters who have been removed from play due to dying while hollow.
- Proposed fix: Resting at the bonfire revives every dead character.
- Rationale: Removes an undefined status; the forced rest already covers the case.
- Gameplay impact: None.
- Decision needed: N

### D-039 · underspecified-deviation · Minor · OPTIONAL
- Location: manuscript.md 745, 1690, 1282 (Threat Level)
- Evidence: Core p.11 and V2 p.8 call the character value 'taunt level' and the enemy value 'threat level'. The manuscript uses 'threat' for both, so 'higher threat level' at 1690 (copied from Core p.24 'higher Taunt level') now reads as an enemy statistic.
- Current text: 7. Threat Level … the enemy moves towards the character with the higher threat level.
- Proposed fix: Characters have a taunt level; enemies have a threat level. (Restore 'taunt' at 745, 1003, 1275, 1277, 1289, 1690, 1694, 2192, 3056, 3058.)
- Rationale: Avoids one word meaning two different statistics; optional if the author prefers a single term and defines it.
- Gameplay impact: Clarity of targeting rules.
- Decision needed: Y

### D-040 · underspecified-deviation · Minor · REQUIRED
- Location: manuscript.md 1277 (Encounter Start, step 9)
- Evidence: Core p.19 uses the First Activation token to fix character order; the manuscript orders characters by threat (1289) so the token placed at 1277 is never consulted.
- Current text: Place the first player token on the character with the highest threat value.
- Proposed fix: (delete step 9; see D-019)
- Rationale: Vestige of the 1E activation system.
- Gameplay impact: None.
- Decision needed: Y

### D-041 · underspecified-deviation · Minor · OPTIONAL
- Location: manuscript.md 1135, 1163 (setup) vs 1313, 1447 (rewards)
- Evidence: Treasure cards are dealt face down to each tile at setup, but the reward rules say characters 'draw' from the tier deck and never refer back to the dealt cards.
- Current text: Deal one tier one treasure per character face-down to each encounter tile. … Draw cards from the Tier one treasure deck before defeating the mini-boss
- Proposed fix: On the first clear of an encounter each character takes one of the treasure cards dealt to that tile at setup.
- Rationale: Links the setup step to the reward it exists for.
- Gameplay impact: None.
- Decision needed: N

### F-056 · second-person · Minor · CLEAN-UP
- Location: L1475 §Gameplay › Treasure Rewards; L2047 §Mimics
- Evidence: Imperatives addressed to the reader: 'See the detailed rules on mimics later in these rules for details.'; 'Refer to "Boss Encounter" rules for more details…'
- Current text: See the detailed rules on mimics later in these rules for details. / Refer to “**Boss Encounter**” rules for more details on how to manage the mimic's behaviour cards.
- Proposed fix: Replace with parenthetical references: '(see §13)' and '(see §15.5 and §16)'.
- Rationale: 'See'/'Refer to' are reader imperatives; the convention is a parenthetical § reference.
- Gameplay impact: none
- Decision needed: N

### F-067 · prose-crossref · Minor · CLEAN-UP
- Location: L1475 §Gameplay › Treasure Rewards
- Evidence: Prose cross-reference: 'See the detailed rules on mimics later in these rules for details.'
- Current text: See the detailed rules on mimics later in these rules for details.
- Proposed fix: '(see §13)' — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: §13 Mimics. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-083 · prose-crossref · Minor · CLEAN-UP
- Location: L1263, L1141, L849, L1914, L2141 (inline 'For example…')
- Evidence: Prose cross-reference: 'For example, if the first three encounters are marked cleared…'
- Current text: For example, if the first three encounters are marked cleared…
- Proposed fix: Set each as a separate *Example.* paragraph per the Voice Guide §7; examples are not rules. — Phase 2A convention: parenthetical '(see §N.M)' after the clause; never 'later', 'previously', 'earlier', 'aforementioned', 'as described'.
- Rationale: Resolves to: n/a — worked examples embedded in rule sentences. Numbering per F_report.md §6 provisional map.
- Gameplay impact: none
- Decision needed: N

### F-085 · register-shift · Minor · CLEAN-UP
- Location: L1203–1479 §Gameplay; L1598–1658 §Combat Basics › Conditions; L3038–3094 §PvP
- Evidence: Bullet-fragment register ('- Remove all damage cubes.', '- Souls cannot be transferred between characters.', '- Aggro token is not used.') alongside declarative-prose chapters (§3, §4, §8–§10) and numbered-procedure chapters (§6).
- Current text: - Drop all *souls* from the dashboard onto the current encounter tile. / - *Aggro* token is not used. / - Dying in PvP does not cause any penalty.
- Proposed fix: Normalise per the Voice Guide: sequences → numbered steps; standing rules → full declarative sentences with a subject ('The *aggro* token is not used in PvP.'); keep bullets only for unordered lists of conditions or components.
- Rationale: Three registers for the same kind of content; readers cannot tell a procedure from a standing rule.
- Gameplay impact: none
- Decision needed: N

### F-088 · register-shift · Minor · CLEAN-UP
- Location: L1241, L1461, L1479, L1670, L1848, L2047, L2057, L2151, L3040, L3042, L1115, L1109
- Evidence: Future tense in rules: 'Invaders will attempt to kill the characters'; 'the treasure will be awarded'; 'how an enemy model will move'; 'will instead do magical damage'; 'The mimic will take its turn first'; 'no further crystal lizards will spawn'; 'a PvP encounter will occur'; 'This will create a linear route'.
- Current text: - Invaders will attempt to kill the characters. … After each boss (mini, main, and mega) a PvP encounter will occur.
- Proposed fix: Present tense throughout: 'Invaders attack the characters.'; 'the treasure is awarded to…'; 'The mimic takes the first turn.'; 'a PvP encounter follows each boss'.
- Rationale: Tense policy: present.
- Gameplay impact: none
- Decision needed: N

### F-092 · register-shift · Minor · CLEAN-UP
- Location: L1263 §Gameplay › Encounter Start step 2.1
- Evidence: Worked example in conditional mood inside a numbered procedure: 'For example, if the first three encounters are marked cleared then the characters could skip to the fourth encounter but would all start with 6 stamina expended.'
- Current text: 1.  For example, if the first three encounters are marked *cleared* then the characters could skip to the fourth encounter but would all start with 6 stamina expended.
- Proposed fix: Set apart as '*Example.* The first three encounters are *cleared*. The party skips to the fourth encounter. Each character places six stamina cubes on their endurance bar.'
- Rationale: Examples are present-tense, labelled and separate from the procedure.
- Gameplay impact: none
- Decision needed: N

### A-123 · inherits-official-silently · Note · CLEAN-UP
- Location: SETUP › Setup After the main-boss step 4 (manuscript.md line 1181); CAMPAIGN PLAY
- Evidence: manuscript.md:1181, 1317; DS-EC-Rules-Web.txt p.8 and p.19 ('If the party rests at the bonfire, the level 4 encounter will not reset like level 1–3 encounters do')
- Current text: Characters then attempt to clear the Level 4 encounter as they have with previous encounters.
- Proposed fix: Level 4 encounters reset when the characters rest, like any other encounter. (Record as a deliberate departure; alternative: adopt the official no-reset rule.)
- Rationale: The official booklets exempt Level 4 encounters from resetting; the manuscript does not, and the generic reset rule therefore applies. Recording the choice prevents accidental 'correction'.
- Gameplay impact: Mega-boss approach is repeatable in the manuscript.
- Decision needed: Y

### A-124 · inherits-official-silently · Note · CLEAN-UP
- Location: ENEMY TURN › Overview (manuscript.md line 1664); Encounter Turn Order (lines 1281–1295) — turn structure
- Evidence: manuscript.md:1281–1295, 1664, 2025–2027; DS-Core-Rules-lores.txt p.19; Hollowed_Edition_v1.3.txt p.7 ('Enemies always activate first')
- Current text: Each encounter begins with each enemy model taking their turn before proceeding to the character's turns.
- Proposed fix: No change.
- Rationale: The manuscript's round structure (all enemies, then every character in threat order, then aggro reassignment) is complete and internally consistent and differs from both official editions by design. Recorded for the preserve list together with the invader-after-each-character rule.
- Gameplay impact: None.
- Decision needed: N

### C-069 · table-text · Note · CLEAN-UP
- Location: L1401-1439; L2247-2285; L1411-1412; L2257-2258
- Evidence: Campaign Soul Reward Table (2/3/4/5) equals basic table (3/4/5/6) minus one, matching L2243 'reduced by one compared to the basic game'. Header text differs: 'per characteri' (1412, stray i) vs 'per character' (2258).
- Current text: per characteri
- Proposed fix: per character
- Rationale: Arithmetic verified consistent; header defect only.
- Gameplay impact: None
- Decision needed: N

### C-089 · cross-ref · Note · CLEAN-UP
- Location: L1471; L1473-1475; L2045; L2047
- Evidence: Mimic rules split between §Treasure Rewards (1463-1475) and §MIMICS (2041-2047); the two are consistent (one treasure on a treasure ambush; two treasures for killing the mimic) but §Treasure Rewards repeats five sentences of §MIMICS
- Current text: (duplicate)
- Proposed fix: Keep the full procedure in §MIMICS; reduce §Treasure Rewards to one sentence with '(see §Mimics)'.
- Rationale: Duplicated rules drift apart in later edits.
- Gameplay impact: None
- Decision needed: N

## Completion entries that apply (10) — approved at Gate 1

### [CMP-0006] Gameplay › Death & Hollowing — "Lost" state — Proposed Completion
- Current state: "Lost" is used but never defined: "keeping them from being *lost* to the *hollow*" (line 1890); "Resting at the *bonfire* also revives *lost* characters who have been removed from play due to dying while *hollow*" (line 1906); "The players lose the campaign if all characters are lost to the hollow without a *spark* to revive them" (line 2235). Death & Hollowing (line 1223) and Encounter Resolution (line 1305) say that when a *hollow* character dies the encounter is *failed* and the characters must spend a *spark* and rest. Setup After the main-boss step 11 (line 1195) says that in the mega-boss encounter "If a character dies they are permanently removed from play." Objective & Loss Conditions (line 1201) defines loss only as "all characters are dead and there are no remaining sparks".
- Proposed completion:

  New bullet group appended to Death & Hollowing (after line 1223):

  > - A *hollow* character who dies is *lost*.
  >
  >   - A *lost* character is removed from play: place the model on its side beside the *bonfire* tile, drop its *souls* on the encounter tile and discard its *ember* token as for any death.
  >
  >   - A *lost* character is not revived by *clearing* an encounter. A *lost* character is revived only when the characters rest at the *bonfire*; resting removes the *hollow* markers as usual.
  >
  >   - When a character becomes *lost*, the current encounter is *failed* at once and the characters must rest at the *bonfire* (see Encounter Resolution). If the *spark* dial shows zero, the players lose the game (see Objective & Loss Conditions).
  >
  >   - In a mega-boss encounter no rest follows: a character who dies or is *lost* in a mega-boss encounter is removed from play for the rest of the game.

  Replacement for the Encounter Resolution bullet at line 1305: "Encounters are *failed* if any *hollow* character dies; that character is *lost*."

  Replacement sentence for Returning to the Bonfire line 1906: "Resting at the *bonfire* also revives *lost* characters: characters who died while *hollow* and were removed from play."

  Addition to Objective & Loss Conditions (line 1201), as a second paragraph: "The players also lose if the characters are required to rest at the *bonfire* when the *spark* dial shows zero, and if every character is removed from play during a mega-boss encounter."
- Design rationale: The definition takes the three uses of "lost" as given and makes them one state. It keeps the manuscript's rule that a *hollow* death fails the encounter, so "lost" is a label for the interval between that death and the forced rest, and for permanent removal in the mega-boss fight. The zero-spark case is the one gap the body leaves (the forced rest cannot be paid); the ruling follows the manuscript's own loss condition rather than letting survivors continue without the lost character.
- Mechanical impact: None where sparks remain. With zero sparks, a hollow death now ends the game explicitly; previously the outcome was undefined.
- Follow-on changes required: Glossary entry "Lost" (CMP-0002) loses its [PROPOSED] tag on approval. F.A.Q. entries on forced rest and mega-boss death (CMP-0003) align. CMP-0020 carries the zero-spark rule into Encounter Recovery.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

### [CMP-0007] Truncated and defective sentences (several chapters) — Proposed Completion
- Current state: Six sentences are cut short or carry a wrong word.
  1. Summons › Phantoms, line 1993: "Phantoms are removed from play if their health dial is reduced to or the encounter ends."
  2. Setup › Setup After the mini-boss step 11, line 1169: "Place all character models on the *bonfire* tile where they may now without spending a spark."
  3. Setup › Shop Setup › After Boss is Defeated step 2.3, line 1089: "Shuffle five random legendary treasure cards."
  4. Summons › Invader Encounter Setup step 2, line 2017: "deal a number equal to their starting decks deck size".
  5. Summons › Invader Encounter Setup step 4, line 2021: "If the central node is blocked by train".
  6. Mimics, line 2045: "they must reveal one an *ambush* card".
  Also: Summons › Phantoms step 7, line 1989, stray "i" after "behaviour deck."; steps 8 (line 1991) and Invader Combat step 4 (line 2031) say "each icon on the encounter card" where the behaviour card is meant; Soul Reward Table header, line 1412, "per characteri"; Mimics line 2047 "*cleared.*."; Game Components line 443 "1x HungryVoracious Mimic".
- Proposed completion (completed sentences, to be substituted in place):

  > 1. Phantoms are removed from play when their health dial is reduced to zero or when the encounter ends.
  >
  > 2. Place all character models on the *bonfire* tile, where they may now rest without spending a *spark*. They may visit the Firekeeper and Andre's Shop as usual after resting at the *bonfire*.
  >
  > 3. Shuffle five random legendary treasure cards into the tier two treasure deck. Return the remaining legendary treasure cards to the game box.
  >
  > 4. Shuffle the invader's behaviour cards and deal a number of them equal to the behaviour deck size on the invader's data card, face down, to create the invader behaviour deck. When the invader's health is reduced to or below its heat-up point, shuffle one unused invader behaviour card into the behaviour deck.
  >
  > 5. After the encounter card setup is complete, place the invader model on the encounter tile's central node. If the central node is blocked by terrain, place the invader model on a node adjacent to the central node, chosen by the players.
  >
  > 6. If the characters wish to open the chest, they must reveal the *ambush* card beside that encounter tile to determine whether the chest is a lurking mimic.
  >
  > Step 7 (line 1989): Each phantom turn, draw and resolve the top card of the phantom behaviour deck.
  >
  > Step 8 (line 1991) and Invader Combat step 4 (line 2031): After each icon on the behaviour card is resolved in left-to-right order, the phantom's [invader's] turn ends.
  >
  > Soul Reward Table header: "*Soul* reward per character".
  >
  > Mimics line 2047: "…and may mark the encounter *cleared*."
  >
  > Game Components line 443: "1x Hungry Mimic and 1x Voracious Mimic (Explorers)" — two data cards sharing two miniatures and one health dial.
- Design rationale: Each completion supplies the word the sentence's structure demands and that the surrounding rules confirm (zero health; rest; the tier two deck, as Legendary Treasure line 1025 already states; deck size; terrain; one ambush card). "Encounter card" in the phantom and invader turn steps is corrected to "behaviour card" because the phantom and invader rules draw from behaviour decks, not encounter cards.
- Mechanical impact: None; restores intended text.
- Follow-on changes required: None beyond substitution. Glossary (CMP-0002) and CMP-0018 reference the corrected phantom steps.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

### [CMP-0009] PLAYER VS PLAYER (chapter) — Proposed Completion
- Current state: Lines 3038–3094: twenty-seven bullets and a six-line dodge-difficulty list. No prose. Gaps: how a character attacks a character (which defence rolls, which dodge difficulty, how damage is placed); parry and riposte; pushes; conditions; what "outermost available node" means; what a trap token does in PvP; simultaneous death; how the "+1 attack damage" carry-over is tracked; ties in threat; what the champion is; "intimate victor" (line 1201) for "ultimate". The bullet "First turn token is given to the character with the highest threat value" (line 3056) duplicates the turn-order bullet (see CMP-0011).
- Proposed completion (full chapter; the manuscript's bullets are the skeleton):

  > # PLAYER VS PLAYER
  >
  > Player versus player (PvP) is an optional contest fought between the characters after each boss is defeated. The players must agree during setup whether PvP encounters will be played. If they are, a PvP encounter is fought after every mini-boss, main-boss and mega-boss encounter that is won.
  >
  > ## Setup
  >
  > 1. Remove every enemy model, wound token and trap token from the boss encounter tile(s). Terrain tokens remain.
  > 2. Restore every surviving character as if they had rested at the *bonfire*: remove all damage cubes, stamina cubes, *hollow* markers and condition tokens, and flip *luck*, *estus flask* and *heroic action* tokens to the ready side. *Ember* tokens are kept.
  > 3. Characters who died in the boss encounter take no part in the PvP encounter. Summons and invaders take no part.
  > 4. Place each character on a different corner node of the boss encounter tile(s). The character with the highest *threat* chooses first, then the next highest, and so on.
  > 5. The *aggro* token is not used.
  > 6. Set the trap tokens face down beside the tile, shuffled.
  >
  > ## Turn Order
  >
  > Characters take turns one at a time in descending *threat* order. If two characters share a *threat* value, the players decide their order before the first turn; if they cannot agree, decide at random. The order is kept for the whole PvP encounter. After the last character has taken a turn, the first takes the next, and so on until one character remains.
  >
  > ## Character Turns
  >
  > A character's turn is unchanged from the basic rules: recover one stamina; take any minor actions (*Walk*, *Run*, *Equip*, *Heroic Action*); take one major action (*Attack*, *Rest*, *Drink Estus* or *Ember*). A character may not leave the tile(s). The limit of one spell attack option per turn applies.
  >
  > After a character's major action, that character's player draws one trap token and places it face down on an outermost available node. The outermost available nodes are the nodes along the tile's edges that contain no model, no terrain token and no trap token; when every edge node is occupied, the next ring of nodes inward is the outermost. If no trap token remains, none is placed.
  >
  > ## Attacking a Character
  >
  > A character attacks another character exactly as they would attack an enemy: choose an attack option, pay its stamina cost, nominate a character within the attack's range as the target, roll the dice, apply modifiers, and use any rerolls (two-handed, *luck*, equipment). The result is the attack value. Attack options with the *shaft* icon may not target a character on the attacker's node. An *AoE* attack option targets every other character on the chosen node; roll once and resolve each defence separately. A *scaled* weapon's +1 and any PvP victory bonus (below) apply.
  >
  > The target then defends as against an enemy attack, choosing one of the following before any dice are rolled.
  >
  > - *Block* or *resist*: roll the block dice (against a physical attack option) or resist dice (against a magical attack option) of every equipped card; the defence total is the sum of the two highest dice. The defender suffers damage equal to the attack value minus the defence total, to a minimum of zero. The defender is hit.
  > - *Dodge*: pay one stamina (or three stamina for one additional die) and roll dodge dice against the dodge difficulty given by the table below. On a success the attack misses entirely and the defender must move to an adjacent node. On a failure the defender is hit and rolls only their armour card's block or resist dice.
  > - *Parry*: pay one stamina. A *parry* is allowed only if the defender has a shield in the left weapon slot, shares a node with the attacker, and the attack option has no push icon and is not *AoE*. Roll dodge dice against the table below. On a success the attack misses, the attacker receives a *stagger* token and the defender may at once make one *riposte* with any attack option of the weapon in their right weapon slot, paying its stamina cost; the attacker defends against the *riposte* by blocking, resisting or dodging but may not *parry* it. On a failure the defender suffers the full attack value, with no defence roll, and receives a *stagger* token.
  > - Do nothing: the defender suffers the full attack value and is hit.
  >
  > Damage suffered is placed as damage cubes on the defender's endurance bar. An *embered* defender reduces damage of three or more from a single attack by one, as usual.
  >
  > **Dodge difficulty in PvP.** The dodge difficulty of a character's attack option is set by its stamina cost:
  >
  > | Stamina cost of the attack option | Dodge difficulty |
  > |---|---|
  > | 0 | 4 |
  > | 1 | 3 |
  > | 2 | 2 |
  > | 3 | 1 |
  > | 4 | 1 |
  > | 5 or more | 0 |
  >
  > A *riposte* uses the dodge difficulty of the attack option chosen for it.
  >
  > ## Pushes and Conditions
  >
  > An attack option with the push icon pushes each character it hits one node directly away from the attacker, as Pushing describes; a character is not pushed into a node containing a gravestone or chest, and a barrel in the destination node is destroyed. Condition icons on attack options place the matching condition token on each character hit. Conditions on characters are resolved as Combat Basics › Conditions describes: *bleed* deals three damage when a second token would be placed; *poison* deals damage at the end of the character's turn; *frostbite* stops stamina recovery; *stagger* subtracts one from every roll total.
  >
  > ## Traps
  >
  > When a character moves onto, dodges onto, shifts onto or is pushed onto a node containing a face-down trap token, flip the token. If it shows a trap, the character must attempt to *dodge* against the trap's printed dodge difficulty, paying one stamina as usual; a character who fails, or who cannot pay, dies. A trap token showing nothing has no effect. A flipped trap token stays on its node and does not trigger again.
  >
  > ## Death
  >
  > A character whose endurance bar is full of damage cubes, or who fails to dodge a trap, dies and is removed from the tile. Death in PvP has no cost: *souls* are not dropped, the *ember* token is not removed, and no *hollow* markers are placed. The character is restored with the others at the end of the PvP encounter.
  >
  > ## Victory
  >
  > The last character on the tile wins the PvP encounter. If the last two or more characters die at the same time, no character wins.
  >
  > The winner of a PvP encounter fought after a mini-boss or a non-final main-boss gains a PvP victory bonus: place one wound token beside the winner's dashboard. In every later PvP encounter the character adds one to the attack value of each attack option per wound token beside their dashboard. The bonus has no effect outside PvP and is cumulative.
  >
  > The winner of the PvP encounter fought after the final boss is the champion of the game. The players still share the victory over the final boss.
  >
  > ## After the PvP Encounter
  >
  > Return all trap tokens to the supply. Place every character, including those who died, on the *bonfire* tile and rest there without spending a *spark*, as after a boss. Remove the wound tokens used to mark PvP victory bonuses only when the game ends.

  Consequential edit to Gameplay › Objective & Loss Conditions (line 1201): "…to determine a single ultimate victor." Delete the bullet "*First* *turn* token is given to the character with the highest threat value" (line 3056; see CMP-0011).
- Design rationale: Every mechanic is the manuscript's own, applied symmetrically: the defender rolls exactly as against an enemy (two highest dice; armour-only after a failed dodge; parry conditions and stagger results from Enemy Turn › Parry & Riposte), and the attacker's fixed enemy-style dodge difficulty is replaced by the manuscript's stamina-cost table. The outermost-node ring rule gives the trap bullet a definite meaning that shrinks the arena and ends stalemates. Simultaneous death yields no winner so the carry-over bonus cannot be awarded twice. The bonus is tracked with a wound token because wound tokens are otherwise unused on characters and no new component is needed. "A riposte may not be parried" prevents an endless chain of parries between two shield-bearers.
- Mechanical impact: PvP becomes fully playable. The only numeric additions are the trap death rule (already in the bullets) and the cumulative +1 bonus tracking. Terrain is kept on the tile (the bullets remove only enemies and traps), which keeps gravestones and chests as cover.
- Follow-on changes required: Delete the empty heading at line 3096. Add "Resting at the *bonfire*" after PvP to Returning to the Bonfire line 1908 (already states it). Glossary entries Dodge difficulty and Riposte (CMP-0002) reference this chapter. If the editor prefers a dedicated marker to the wound token, add "4x PvP victory tokens" to Game Components.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

### [CMP-0010] Gameplay › Souls / Campaign Play › Encounter Soul Rewards — Reduced soul reward — Proposed Completion
- Current state: Souls (line 1391): "Upon successfully *clearing* an encounter that has been previously *cleared*, reward the reduced *soul* reward to each character." Encounter Resolution (line 1327): "Characters gain *soul* rewards but not treasure." Campaign Play (line 2245): "repeated for *souls* rewards but not treasure rewards, just as in the basic game." Neither Soul Reward Table (lines 1401–1439) nor the Campaign Soul Reward Table (lines 2247–2285) has a reduced column; no value is ever given.
- Proposed completion:

  Replacement for line 1391: "Upon successfully *clearing* an encounter that has been previously *cleared*, reward the reduced *soul* reward to each character. The reduced reward is half the full reward, rounded down."

  Replacement for the Soul Reward Table:

  > ### Soul Reward Table
  >
  > | Encounter | Full reward per character | Reduced reward per character (already *cleared*) |
  > |---|---|---|
  > | Level 1 Encounter and Standard Invaders | 3 | 1 |
  > | Level 2 Encounter and Advanced Invaders | 4 | 2 |
  > | Level 3 Encounter | 5 | 2 |
  > | Level 4 Encounter and Bosses | 6 | 3 |
  >
  > Invaders and bosses are never *cleared* twice; their reduced reward is never used.

  Replacement for the Campaign Soul Reward Table:

  > ### Campaign Soul Reward Table
  >
  > | Encounter | Full reward per character | Reduced reward per character (already *cleared*) |
  > |---|---|---|
  > | Level 1 Encounter and Standard Invaders | 2 | 1 |
  > | Level 2 Encounter and Advanced Invaders | 3 | 1 |
  > | Level 3 Encounter | 4 | 2 |
  > | Level 4 Encounter and Bosses | 5 | 2 |

  Replacement for Encounter Resolution line 1327: "Characters gain the reduced *soul* reward but no treasure."
- Design rationale: Half rounded down is chosen over "one fewer" because the manuscript's stated aim is to remove grinding: at one fewer, repeating a Level 3 encounter would pay 4 souls per character, barely less than clearing it. Half makes repeats worth taking only when a character must retrieve dropped souls or wants a safe route to the boss. Rounding down keeps every value a whole number and never reduces a reward to zero. The alternative (one fewer: 2/3/4/5 and 1/2/3/4) is recorded here for the editor's decision.
- Mechanical impact: Repeat clears pay 1–3 souls (basic) or 1–2 souls (campaign) per character. Dropped-soul recovery is unaffected.
- Follow-on changes required: F.A.Q. answer on reduced rewards (CMP-0003) matches. Line 2243 ("reduced by one compared to the basic game") stands and refers to the full reward only; add "The reduced reward is half the campaign full reward, rounded down" after it.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

### [CMP-0011] Gameplay › Encounter Start step 9 and Player vs Player — "First player token" — Proposed Completion
- Current state: Encounter Start step 9 (line 1277): "Place the *first player* token on the character with the highest threat value." Player vs Player (line 3056): "*First* *turn* token is given to the character with the highest threat value." No such token is listed in Game Components › Tokens & Terrain Elements (lines 679–723). Turn order is fixed by *threat* in both places (lines 1289, 3058), so the token has no function.
- Proposed completion: Remove the token. Delete Encounter Start step 9 and the PvP bullet at line 3056, and replace Encounter Start step 8 (line 1275) with:

  > 8. Place the *aggro* token on the character with the highest *threat* value. That character takes the first character turn of the encounter; ties in *threat* are settled by the players before the first turn and the order is kept for the encounter.

  Replacement for PvP turn-order bullet (line 3058), as drafted in CMP-0009: "Characters take turns one at a time in descending *threat* order. If two characters share a *threat* value, the players decide their order before the first turn; if they cannot agree, decide at random."
- Design rationale: Removal is recommended over definition. Threat order already fixes the first character, so a first-player token would duplicate information the dashboards carry; the Core rulebook's First Activation token existed only because its turn order went clockwise, which this edition has abandoned. Defining the token would also require adding a component. The tie rule supplies the one thing the token's position would have recorded.
- Mechanical impact: None.
- Follow-on changes required: Remove "first player" from the italicised-term inventory; no Glossary entry. Renumber Encounter Start.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

### [CMP-0012] Game Components and owning chapters — Undefined components (event cards, ambush cards, mega-boss items, Level 4 tiles, pillar tokens, strafe and track cards) — Proposed Completion [PROPOSED-SYSTEMIC for event cards]
- Current state: Game Components lists "Event cards" (lines 659–667: 10 per level and 5 Special Trap cards) and "Level 4 encounter cards" (line 653) but no ambush cards, pillar tokens, mega-boss items, strafe cards, track behaviour cards, mega-boss setup card, phantom or invader components, or mega-boss game boards. Event cards are used at Setup (lines 1133, 1161), Encounter Start (line 1269), Gravestones (line 939) and Setup After the main-boss (line 1181, "No event card is used"), but no rule says what an event card does; the Tomb of Giants set's event cards (immediate/consumable/rendezvous, drawn as rewards) are a different component and its rules do not match the manuscript's levelled, tile-dealt deck. "Ambush card" is used (lines 1137, 1469–1473, 2045) and defined only by use. "Mega-boss Items" (line 1183) are never defined. "Level 4 encounter tile associated with the chosen mega-boss" (line 1179) is the double-sided mega-boss game board. "Pillar token" (line 2205) and "pillar nodes" are used only in Boss Special Rules.
- Proposed completion:

  (a) Additions to Game Components (insert after line 667 and within Tokens & Terrain Elements as marked):

  > ### Phantom cards and tokens (Phantoms)
  >
  > - 10x Summon data cards (5 standard, 5 advanced), 40x Summon behaviour cards, 1x Summon health dial
  > - 12x Invader data cards (6 standard, 6 advanced), 64x Invader behaviour cards, 12x Invader treasure cards, 1x Invader health dial
  > - 6x Standard invader tokens, 6x Advanced invader tokens, 3x Blank invader tokens
  >
  > ### Mimic cards (Explorers)
  >
  > - 2x Mimic data cards (Hungry, Voracious), 14x Mimic behaviour cards, 1x Mimic health dial, 5x Ambush cards
  >
  > ### Mega-boss components (one set per mega-boss expansion)
  >
  > - 1x Mega-boss game board (double-sided: Level 4 encounter side and mega-boss side)
  > - 4x Level 4 encounter cards
  > - 1x Mega-boss data card, 1x Health dial, behaviour cards as listed on the data card, 2x Mega-boss treasure cards
  > - Black Dragon Kalameet only: 8x Strafe cards, 4x *Calamity* tokens
  > - Executioner's Chariot only: 4x Track behaviour cards, 1x Mega-boss setup card
  > - Asylum Demon only: 4x Pillar tokens
  >
  > (Tokens & Terrain Elements, after line 713) - 4x Pillar tokens (Asylum Demon)

  (b) New sub-section in Game Components › Cards, after Event cards (line 667):

  > ### Ambush cards
  >
  > Five cards from the Explorers expansion, each showing Treasure or Mimic on its face. One is dealt face down beside each encounter tile when mimics are in play and is revealed only when the characters choose to open that tile's chest. See Mimics.

  (c) Rule paragraph for event cards, as a new sub-section Gameplay › Encounters › Event Cards (insert after Encounter Start, line 1277) [PROPOSED-SYSTEMIC]:

  > ### Event Cards
  >
  > Each encounter tile carries one face-down event card of the same level as its encounter card, dealt at setup. When the characters enter the tile, reveal the event card after the encounter card and before enemies and terrain are placed. The event card's text modifies that encounter and applies until the encounter ends, unless the card states otherwise. An event card that cannot be applied to its encounter (for example, one that refers to a terrain type the encounter does not place) has no effect. Event cards stay on their tiles, face up, after the encounter; when the characters rest at the *bonfire*, event cards are turned face down with their encounter cards and apply again when the encounter is next fought. Special Trap cards are event cards that replace the standard trap tokens of a trapped encounter with the trap layout printed on the card; if the encounter is not trapped, the Special Trap card has no effect. Level 4 encounters and boss encounters use no event card.

  (d) Definition of mega-boss items, replacing Setup After the main-boss step 5 (line 1183):

  > 5. Shuffle the mega-boss's treasure cards (its *mega-boss items*) and deal one face down to the Level 4 encounter tile. This card is the Level 4 encounter's treasure reward and is awarded, when the encounter is *cleared*, as a chest treasure is: the players decide which character receives it. No tier two treasure cards are dealt to the Level 4 tile. [PROPOSED]

  (e) Definition of the Level 4 tile, replacing Setup After the main-boss step 3 (line 1179):

  > 3. Place the mega-boss game board supplied with the chosen mega-boss adjacent to the *bonfire* tile, with its Level 4 encounter side (enemy spawn and terrain nodes) face up and a doorway aligned with the *bonfire* tile. Place the fog gate on that doorway. The game board's other side shows the mega-boss spawn node and is used for the mega-boss encounter.

  (f) Pillar tokens: the definition in Boss Special Rules › Pillar Smasher (line 2205) stands; add to Tiles & Nodes › Terrain, after Traps (line 981): "**Pillars.** Pillar tokens are placed only on the pillar nodes of the Asylum Demon mega-boss game board. Pillars block movement, dodging and pushes until destroyed; see Boss Special Rules."
- Design rationale: Items (a), (b), (e) and (f) are inventories and descriptions drawn from the supplied booklets, matched to the manuscript's existing lists. Item (d) resolves "mega-boss Items" as the mega-boss's own treasure cards, the only cards an expansion supplies that fit the phrase, and gives the Level 4 tile a reward in place of the per-character tier two cards the generic setup would otherwise deal. Item (c) is a new subsystem: the manuscript dealt, revealed and scried event cards without ever stating their effect, and the only published event cards (Tomb of Giants) work differently; the paragraph is the minimum needed for the component to function (when revealed, duration, reset, what a Special Trap card is, where no event is used) and does not design any card.
- Mechanical impact: Event cards gain a definite timing and reset. Level 4 encounters award one mega-boss treasure card instead of one tier two card per character (a reduction of up to three cards). Component counts allow the Game Components chapter to be checked against the boxes.
- Follow-on changes required: Decision needed on (c): confirm that the author's event deck exists (print-and-play in the Community Update Pack?) and supply card texts, or delete every event-card reference (lines 659–667, 939, 1133, 1161, 1181, 1269). Confirm (d) with the author. Glossary entries Event card and Ambush card (CMP-0002). Campaign Play: state whether campaign Level 4 encounters also receive a mega-boss item.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

### [CMP-0014] MIMICS / Gameplay › Treasure Rewards / Tiles & Nodes › Chests — Mimic and chest procedure reconciliation — Proposed Completion
- Current state: Three passages state the chest-and-mimic procedure with differences. Chests (line 963): undecided treasure goes to "a randomly selected character". Treasure Rewards (lines 1453–1475): undecided treasure goes to the character who ended the encounter with the aggro token; no recovery "until a decision is made"; one treasure if the ambush card shows treasure; mimic encounter set up immediately. Mimics (lines 2041–2047): the expansion is called "Encounters" then "Explorers"; the aggro holder makes the open/leave decision; after leaving the chest the characters "recover all stamina and two damage" (Encounter Recovery, line 1347, removes one damage cube); "min-boss"; killing the mimic gives two treasures and marks the encounter *cleared*; a mimic that defeats the characters is fought again "next time they complete the normal encounter"; "once the mimic has been fought once, it must be fought again at the end of the encounter until it is killed".
- Proposed completion: The Mimics chapter owns the procedure. Treasure Rewards and Chests keep one pointer each.

  Replacement for Tiles & Nodes › Chests bullet at line 963: "Upon *clearing* an encounter containing a chest, the players flip the chest to its open side and decide which character takes the revealed treasure. If they cannot decide, the character who ended the encounter with the *aggro* token takes it. When playing with mimics, see Mimics before opening a chest."

  Replacement for Treasure Rewards lines 1463–1475 (the five mimic bullets): "- If playing with mimics, a chest is opened only as the Mimics chapter describes; the encounter is not resolved until the characters have decided whether to open it."

  Replacement for the MIMICS chapter (lines 2039–2047):

  > # MIMICS
  >
  > Mimics are an optional challenge from the Explorers expansion. The players decide during setup whether to include them. Groups with new players are advised to leave mimics out; experienced groups are advised to include them. When mimics are in play, one face-down *ambush* card is dealt beside each encounter tile at setup.
  >
  > When an encounter containing an unopened chest is *cleared*, the characters do not recover at once. They remain on their nodes and decide collectively whether to open the chest. If they cannot agree, the character holding the *aggro* token decides.
  >
  > If the characters leave the chest closed, they recover as Encounter Recovery describes and collect their *soul* and treasure rewards. The chest stays closed and may be opened after a later clearing of the same encounter.
  >
  > If the characters open the chest, reveal the *ambush* card beside the tile. If it shows Treasure, the characters receive the treasure card beneath the chest and assign it as the Chests rules describe; then they recover and collect their rewards. If it shows Mimic, a mimic encounter begins at once, before any recovery or reward.
  >
  > The mimic encounter is a mini-boss encounter fought on the same tile. Use the Hungry Mimic's data and behaviour cards if the mini-boss has not yet been defeated, and the Voracious Mimic's if it has. Replace the chest token with the mimic model on the chest's node. The characters keep their damage cubes, stamina cubes and condition tokens and remain on the nodes they occupied. Build the mimic's behaviour deck from random behaviour cards equal to its deck size. The mimic takes the first turn, then the characters and the mimic alternate as in any boss encounter. Mimics have no arcs and no heat-up cards; see Boss Special Rules › Explorers Expansion.
  >
  > If the mimic is slain, the characters receive two treasure cards of the current tier in place of the chest's one, assign them as the Chests rules describe, recover as Encounter Recovery describes, and collect the rewards of the encounter that contained the chest. Mark that encounter *cleared*. The mimic does not return; the chest's node is a basic node for the rest of the game.
  >
  > If every character dies, the mimic encounter is *failed*: the characters drop their *souls*, the encounter card is turned face down and the characters must rest at the *bonfire*. The mimic returns to its chest. Each later time the characters *clear* that encounter, they may again choose to open the chest, and the mimic must be fought again until it is slain.

- Design rationale: One procedure, in one chapter, with the other two passages reduced to pointers so no second version can drift. The aggro holder is chosen as tie-breaker in every case because Treasure Rewards and Mimics both already use it and a random draw adds a step. Recovery after leaving the chest follows Encounter Recovery (one damage cube) rather than the Mimics chapter's "two damage". The mimic replacing the chest token on its node follows the Explorers booklet ("the mimic returns to its terrain node") and gives the mimic a defined starting node, which the manuscript never states. "Each later time… they may again choose" resolves the manuscript's two incompatible sentences (fought "next time they complete the encounter" versus "must be fought again until it is killed") in favour of choice, since the characters can always decline to open the chest.
- Mechanical impact: Recovery after declining a chest is one damage cube, not two. The mimic starts on the chest node (previously undefined). Everything else is unchanged.
- Follow-on changes required: Delete the empty heading at line 2049. Glossary entries Chest, Mimic, Ambush card (CMP-0002) align. CMP-0005 holds the mimic's special rules.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

### [CMP-0015] CRYSTAL LIZARDS / Treasure Rewards — Reward card name — Proposed Completion
- Current state: Treasure Rewards (line 1477) awards "a Titanite Chunk card" for killing a *crystal lizard*; Crystal Lizards (line 2055) awards "one Titanite Scale card". The Iron Keep expansion contains three Titanite Scale cards; Titanite Chunk is a Community Update Pack card with STR 25 / DEX 25 requirements (CMP-0004).
- Proposed completion: Titanite Scale is the reward. Replacement for line 1477: "If playing with the option of *crystal lizards*, award a Titanite Scale card to each character who killed a *crystal lizard* during the encounter, as the Crystal Lizards chapter describes." Addition to the Crystal Lizards chapter after line 2055: "The Iron Keep expansion supplies three Titanite Scale cards. When none remains, ignore the crystal lizard symbol on encounter cards; no further *crystal lizards* are placed."
- Design rationale: Titanite Scale is the physical card in the Iron Keep box and the name the chapter that owns the rule uses. Titanite Chunk carries tier two requirements that a low-stat character who killed the lizard does not necessarily meet, and the Community Update Pack defines it as a shop-sorted upgrade, not a reward. The three-card limit follows the Iron Keep booklet and prevents an undefined state when the supply runs out.
- Mechanical impact: Lizard rewards are capped at three per game.
- Follow-on changes required: Glossary entry Crystal lizard and Titanite (CMP-0002) name Titanite Scale. Delete the empty heading at line 2059.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

### [CMP-0019] Gameplay › Encounter Resolution / Returning to the Bonfire › Resuming Exploration — Reset and skip reconciliation — Proposed Completion
- Current state: Encounter Resolution (lines 1315–1319) marks a *cleared* encounter card with a black cube, says *cleared* encounters "are reset when characters rest at the *bonfire*" and "may be skipped thereafter"; *failed* encounters "flip their encounter card face-down", "are reset when characters rest" and "may not be skipped once reset" (lines 1335–1339). Resuming Exploration (line 1963) says "flip all cleared and failed encounter tiles face-down to reset them… If the encounter card on the tile is face-down (*cleared* or *failed*), they must flip the card face-up and proceed with fighting the enemies of that encounter." Read together, a *cleared* encounter after a rest both may be skipped and must be fought. Encounter Start step 2 (line 1261) allows skipping *cleared* encounters for two stamina each.
- Proposed completion (replacement for Resuming Exploration, line 1963):

  > ## Resuming Exploration
  >
  > When the characters have finished resting at the *bonfire*, reset the encounter tiles before setting out: turn every face-up encounter card face down; leave the black cube on each card that was marked *cleared*; remove any enemy models left on the tiles; do not move terrain tokens (chests, gravestones, barrels, pillars, traps), but turn trap tokens face down and restore barrels.
  >
  > The characters then move to the encounter tile nearest the *bonfire* tile and advance one tile at a time. On entering a tile, turn its encounter card face up. If the card carries a black cube, the encounter was *cleared* earlier: the characters may either skip it, paying two stamina each as Encounter Start describes, or fight it again for the reduced *soul* reward and no treasure. If the card carries no black cube, the encounter was *failed* or never fought and must be fought. After each tile is resolved the characters continue towards the boss tile, or use the fog gate shortcut if it has been placed on the *bonfire* tile.

  Replacement for Encounter Resolution bullet at line 1335: "*Failed* encounters have their encounter card turned face down and any black cube removed."
- Design rationale: The two passages are made to say one thing: resting resets every encounter's enemies, but the *cleared* mark survives and keeps the skip option open; failing an encounter strips the mark. This is the reading under which both Encounter Resolution bullets and the Encounter Start skip rule remain true, and it matches the manuscript's anti-grinding design (a cleared tile is a toll, not a wall).
- Mechanical impact: *Failed* encounters lose their *cleared* status (previously undefined). Otherwise none.
- Follow-on changes required: F.A.Q. entry on skipping after a rest (CMP-0003) matches. Delete the empty heading at line 1959.
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

### [CMP-0020] Gameplay › Encounter Recovery / Objective & Loss Conditions — Forced rest with no sparks — Proposed Completion
- Current state: Encounter Recovery (lines 1369–1381) requires every *failed* encounter to end with "Spend one *spark*" and a rest. Sparks (line 1253) and The Bonfire (line 1890) require a *spark* to rest. Objective & Loss Conditions (line 1201) defines loss only as "all characters are dead and there are no remaining sparks". No rule covers a forced rest when the *spark* dial shows zero while some characters live (a *hollow* death).
- Proposed completion: Insert as the first bullet under "All characters must rest at the bonfire if an encounter is *failed*" (before line 1371): "If the *spark* dial shows zero, the characters cannot rest: the players lose the game." Add to Objective & Loss Conditions, as drafted in CMP-0006: "The players also lose if the characters are required to rest at the *bonfire* when the *spark* dial shows zero."
- Design rationale: The manuscript's loss condition and its forced-rest rule otherwise contradict each other in the *hollow*-death case. The Core rulebook resolves the same case by ending the game when a character dies at zero sparks; this edition's version is narrower (only a forced rest triggers it), which preserves the manuscript's rule that surviving characters may still win if no rest is forced.
- Mechanical impact: Defines a previously undefined end state. With the voluntary rest already impossible at zero sparks, play is otherwise unchanged.
- Follow-on changes required: Coordinated with CMP-0006 (Lost) and the F.A.Q. (CMP-0003).
- Status: approved (Gate 1, 2026-11-10 — see 05_gate1_decisions.md)

---

---

