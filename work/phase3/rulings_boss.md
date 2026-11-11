# Rulings memo — cluster `boss`

Scope: lead items 4, 5 and 13 of `14_open_issues.md`; every item of the per-chapter lists for chapters 15, 16 and 17; chapters 15 to 17 and the glossary terms they define. Edits are in `work/phase3/edits_boss.json` (ids `boss-E..`).

## Sources reached, and sources that refused

- Supplied texts in `work/text/` (2017 core rules, 2022 rules, F.A.Q., six expansion booklets, Extended Rules, Hollowed Edition): read for every item.
- Official booklets for the eight mega-boss expansions, supplied by the author during this task and treated as the primary source for those bosses: `work/text/DS-Four-Kings-Rules-web.txt` (The Four Kings), `DS-GaD-Rules-web.txt` (Gaping Dragon), `DS-GD-Rules-web.txt` (Guardian Dragon), `DS-TLG-Rules.txt` (The Last Giant), `DS-MFA-Rules.txt` (Manus, Father of the Abyss), `DS-OIK-Rules-web.txt` (Old Iron King), `DS-VotBV-Rules-web.txt` (Vordt of the Boreal Valley), `DS-AD-Rules-web-EN.txt` (Asylum Demon). Line references below are to these extracts. Before they were supplied the same booklets had been found on the publisher's file server (`steamforged.com/cdn/shop/files/DS-Four-Kings-Rules-web.pdf`, `DS-GD-Rules-web.pdf`, `DS-OIK-Rules-web.pdf`, `DS-VotBV-Rules-web.pdf`) and on a rules-archive site (`cdn.1j1ju.com`, Last Giant, Manus, Gaping Dragon, Asylum Demon); the texts are the same. Two card diagrams that the text extract garbles (the Guardian Dragon's Fiery Breath card and the Old Iron King's Beam card) were read from the page images.
  Each booklet is 16 pages; the first eleven repeat a shared mega-boss framework (setup after the main boss, Level 4 encounters, data card and behaviour card anatomy), which this book already states once in §6.7 and §15 (see boss-011). Only the "Starting the … Mega Boss Encounter" page and the "Custom Game Elements" page differ from boss to boss.
- The 2024 re-issue rulebook of the core set (`https://steamforged.com/cdn/shop/files/DS-TSC-Rulebook-download-min.pdf`): read for Ornstein & Smough. It lists "2x Main Boss Miniature, 2x Main Boss Data card, 15x Main Boss Behaviour cards" and gives no further rule for the pair.
- Community rules guide "DSBG – Unofficial Guide & Rules FAQ" (`https://docs.google.com/document/d/1DmbTaM68OoosZcSCFW0bTNgBWCaHSP2UE9Um-X4XF54`): read; it summarises each mega-boss's mechanic and agrees with the booklets.
- Community companion program DSBG-Shuffle (`https://github.com/DanDuhon/DSBG-Shuffle`, files `lib/dsbg_shuffle_behaviors.py` and `lib/dsbg_shuffle_behavior_decks.py`): a transcription of every printed boss card and of each boss's heat-up handling. Used as evidence of card text for Ornstein & Smough, Great Grey Wolf Sif, and the Painted World bosses.
- BoardGameGeek and the publisher's old forum: pages refuse automated reading (HTTP 403 and 503). Only the search-result summaries of threads were available; they are cited as such. Reddit is closed to the search tool. The Fextralife wiki host is outside this session's network. Nothing is quoted from a page that was not read.
- The Painted World of Ariamis has no rulebook of its own on the publisher's site: the 2022 rulebook supplied (`DS-TG-Rulebook-Compressed_compressed.txt`) is the rulebook for both 2022 sets and names only the Black Knight and Gravelord Nito. Its bosses' rules are printed on their cards alone.

## Lead items

### boss-001 · lead item 4, nine bosses with placeholders
- Question: Can the nine placeholder entries of §17.10 be replaced by full rules?
- This book now: §17.10 gives each of the nine bosses one paragraph: "played from its data card and the general boss rules … Apply the special rules supplied with that expansion."
- Evidence: official booklets found for all seven mega-bosses (see list above); the two Painted World bosses have no booklet (their rules are their cards); Extended Rules names the bosses only in campaign text (lines 812 to 1029); Hollowed Edition mentions only corrosion (line 511).
- Ruling: CHANGE (seven full entries, boss-002 to boss-008); the two Painted World bosses are handled in boss-009 and boss-010.
- Why: The book promised a definite rule for every boss and delegated nine. The official rules exist, are short, and fit the book's existing forms (deck built by procedure, node-targeting attack decks, special heat-ups), so they are brought in, restated in this book's terms.
- Mechanical: yes (rules where there were none)
- Edits: boss-E20 to boss-E28 (entries), boss-E30 to boss-E36 (glossary), boss-E37 (§2.9 components)

### boss-002 · lead item 4, The Four Kings
- Question: What are the special rules of the Four Kings?
- This book now: §17.10 placeholder, with one true sentence ("fought with several boss models").
- Evidence: official booklet `DS-Four-Kings-Rules-web.txt`: contents lines 56–80 (four models, four numbered health dials, four identifier tokens, 20 behaviour cards); encounter start lines 368–395 (king one on the mega-boss spawn node; deck of four of the eight standard cards; "The Four Kings do not heat up like other bosses"); "One through Four" lines 445–456 (all four must be defeated; one data card and one deck; "any kings in play perform the listed behaviours", in numerical order; no threat value); "Royal Summons" lines 458–474 (first three times the deck is empty: place the next king, push other models as for a leap, remove one random card, add two of the new king's cards, shuffle); "Take a Breather" lines 475–481 (no king in play: draw a card, each character gains 1 health). Extended, Hollowed: silent. Community guide: same summary.
- Ruling: CHANGE (full entry replaces the placeholder)
- Why: The fight is a clock: a new king arrives every time the deck runs out, whether or not the last one is dead, so the party is racing the deck. The official rule is short and needs only the several-models framework that Ornstein & Smough now shares (boss-012). "Gains 1 health" is restated as "removes one damage cube"; the arriving king faces as a boss faces at the start (§15.2), which the booklet leaves unsaid.
- Mechanical: yes
- Edits: boss-E20; boss-E08 (framework)

### boss-003 · lead item 4, Gaping Dragon
- Question: What are the special rules of the Gaping Dragon?
- This book now: §17.10 placeholder plus "attacks inflict the corrosion condition".
- Evidence: official booklet `DS-GaD-Rules-web.txt`: contents lines 57–80 (14 behaviour cards, 4 corrosion tokens); encounter start lines 367–400 (three of seven standard cards, one random heat-up card, both Stomach Slam signature cards: a six-card deck; Crawling Charge face up beside the data card; ordinary heat-up adds "a second Heat Up card"); data card "Devouring Maw"; "Corrosion Condition" lines 443–453; "Crawling Charge" lines 454–466 (the Crawl icon makes the dragon perform the Crawling Charge card at once, and its activation then ends; the card is never in the deck). §8.5 already owns corrosion and agrees with the booklet.
- Ruling: CHANGE (full entry replaces the placeholder)
- Why: Official rule brought in. One point the booklet leaves open is settled the way the general rule already points: after a Crawling Charge the drawn card, not the Crawling Charge card, stays the current behaviour card for weak arcs, because the Crawling Charge card never enters the discard pile. The booklet's "reveal a card for each gravestone" step is dropped, as it was for Kalameet, because this book's scry replaces it.
- Mechanical: yes
- Edits: boss-E21, boss-E14, boss-E32

### boss-004 · lead item 4, Guardian Dragon
- Question: What are the special rules of the Guardian Dragon?
- This book now: §17.10 placeholder.
- Evidence: official booklet `DS-GD-Rules-web.txt`: contents lines 54–75 (11 behaviour cards, 4 Fiery Breath cards); encounter start lines 359–395 (five of nine standard cards; "Take both Cage Grasp Inferno Heat Up behaviour cards and shuffle them into the behaviour deck"); data card "Caged Beast"; "Cage Nodes" lines 438–444 (four corner nodes block movement except during Cage Grasp Inferno); "Cage Grasp Inferno" lines 446–470 (Inferno icon: remove the dragon, reveal a Fiery Breath card, place the dragon on the indicated cage node facing the centre node, attack the targeted nodes; Bonus Behaviour icon: perform another behaviour card at once). The Fiery Breath card diagram on booklet p. 13 prints the attack value and dodge difficulty on the Fiery Breath card itself.
- Ruling: CHANGE (full entry replaces the placeholder)
- Why: Official rule brought in, written as the Kalameet strafe procedure is written (§17.8) so that like attacks read alike. The Bonus Behaviour draw renews an empty deck first, the same answer the Pursuer's second card already has (§17.6).
- Mechanical: yes
- Edits: boss-E22, boss-E39, boss-E40

### boss-005 · lead item 4, The Last Giant
- Question: What are the special rules of the Last Giant?
- This book now: §17.10 placeholder.
- Evidence: official booklet `DS-TLG-Rules.txt`: contents lines 53–70 (16 behaviour cards); encounter start lines 369–400 (three of five standard cards and three of five Arm cards; at heat-up "Add the Slam behaviour card to the behaviour deck, remove all three Arm behaviour cards, add three random Heat Up cards, and shuffle the new behaviour deck"); data card "Armed and Dangerous"; "Wind Up" lines 452–462 (same text as the Asylum Demon booklet).
- Ruling: CHANGE (full entry replaces the placeholder)
- Why: Official rule brought in. The Wind Up icon is not restated; the entry cites §17.3, which already owns it, and the glossary entry is widened to name the Last Giant.
- Mechanical: yes
- Edits: boss-E23, boss-E33

### boss-006 · lead item 4, Manus, Father of the Abyss
- Question: What are the special rules of Manus?
- This book now: §17.10 placeholder.
- Evidence: official booklet `DS-MFA-Rules.txt`: contents lines 58–75 (14 behaviour cards: nine standard, five heat-up); encounter start lines 370–400 (ordinary five-card deck; model faces "the board edge where the entry nodes are located"; heat-up: one random heat-up card on top of the deck, a second "face up on the bottom of the discard pile. Do not shuffle the behaviour deck!"); "Shaft" lines 446–466 (attacks with the shaft icon never hit range 0); "Overextended" lines 467–480 (at the end of every boss activation any character may spend 1 stamina to move one node, counted as a run).
- Ruling: CHANGE (full entry replaces the placeholder)
- Why: Official rule brought in. Manus is the one boss whose heat-up keeps the learned order and inserts two known-position cards; the entry spells out what the placement means (the first is drawn at once, the second leads the next cycle). Overextended reuses the wording of Wind Up so that the two "pay one stamina to step" rules read the same.
- Mechanical: yes
- Edits: boss-E24, boss-E34

### boss-007 · lead item 4, Old Iron King
- Question: What are the special rules of the Old Iron King?
- This book now: §17.10 placeholder.
- Evidence: official booklet `DS-OIK-Rules-web.txt`: contents lines 54–75 (12 behaviour cards, 6 "Fire Beam Cards"); encounter start lines 349–385 (model on "the Iron King node … opposite the doorway"; three of six standard cards plus the three Fire Beam signature cards; ordinary heat-up plus "+1" to the damage and dodge difficulty of Fire Beam); data card "Old Iron Rage"; "Molten Iron Dweller" lines 424–433 (three Iron King nodes; lava behind them treated as a wall; no model in his back arc); "Beam Attacks" lines 435–460 (reveal a Beam card, move the king to the node shown facing the centre, push models there as for a leap, attack the targeted nodes).
- Ruling: CHANGE (full entry replaces the placeholder)
- Why: Official rule brought in. The booklet calls the six node cards both "Fire Beam cards" and "Beam cards" while the three signature behaviour cards are also named Fire Beam; the entry uses "Beam card" for the six and "Fire Beam" for the three so that the two cannot be confused, and §2.9 is aligned.
- Mechanical: yes
- Edits: boss-E25, boss-E38, boss-E41, boss-E44

### boss-008 · lead item 4, Vordt of the Boreal Valley
- Question: What are the special rules of Vordt?
- This book now: §17.10 placeholder plus "attacks inflict the frostbite condition".
- Evidence: official booklet `DS-VotBV-Rules-web.txt`: contents lines 57–85 (17 behaviour cards in five kinds); encounter start lines 378–420 (four-card movement deck, three-card attack deck, Frostbreath card set aside; "Vordt heats up twice", the first adding an attack heat-up card to the attack deck only, the second a movement heat-up card to the movement deck only); "Movement and Attack Behaviour Decks" lines 463–474 (movement card, then attack card, each turn); "Frostbreath" lines 475–490 (performed at the start of the first activation after each heat-up, then turned face down); data card "Icy Blows: If a player Blocks or Resists 4 or more damage they suffer Frostbite."
- Ruling: CHANGE (full entry replaces the placeholder)
- Why: Official rule brought in. Two designer's readings are needed. "Blocks or resists 4 or more damage" is read as damage prevented (the lower of the attack value and the defence total), which punishes the heavy blocker and leaves dodging as the answer, the tactical point of the fight. If one blow crosses both heat-up points, both heat-ups are carried out and Frostbreath is resolved once, since the booklet ties it to the activation, not to the count of heat-ups.
- Mechanical: yes
- Edits: boss-E26

### boss-009 · lead item 4, Crossbreed Priscilla
- Question: What are the special rules of Crossbreed Priscilla?
- This book now: §17.10 placeholder; her data card and behaviour cards are the replacement cards of Appendix B.
- Evidence: no rules booklet exists for the Painted World set beyond the shared 2022 rulebook, which names only the Black Knight and Gravelord Nito (`DS-TG-Rulebook-Compressed_compressed.txt` lines 2099–2290). The printed data card, in a community transcription (DSBG-Shuffle, card image "Crossbreed Priscilla – data"), reads "Snowblind: While Crossbreed Priscilla is invisible, characters do not gain an additional black die when attacking her weak arc" (threat 10, health 40, deck size 5, block 2, resist 1, heat-up 25). Nothing found states when she is invisible or how she becomes visible. Searched: the publisher's resource pages and file server (no Painted World rulebook or errata file reachable), three web searches for the invisibility rule, the community guide, the DSBG-Shuffle code, two reviews of the 2022 sets, an online copy of the "Painted World" rulebook (it is the Tomb of Giants text). BoardGameGeek, Reddit and the Fextralife wiki could not be read.
- Ruling: CONFIRM as written (placeholder kept; form only aligned with the other entries)
- Why: The one rule found depends on a state whose rule was not found, and this book plays Priscilla from replacement cards that were not supplied either. Writing an invisibility rule would be invention.
- Mechanical: no
- Edits: boss-E27

### boss-010 · lead item 4, Heavy Knight
- Question: What are the special rules of the Heavy Knight?
- This book now: §17.10 placeholder; its data card and behaviour cards are the replacement cards of Appendix B.
- Evidence: as boss-009 for the absence of a booklet. Printed data card (same community transcription): "Brutal Impact: If a character with a Stagger token is hit by an attack that inflicts the Stagger condition, place a stamina token on their endurance bar" (threat 10, health 25, deck size 4, block 2, resist 2, heat-up 15). The ability is complete on the card and needs no chapter rule.
- Ruling: CHANGE (placeholder replaced by the form §17.7 uses for the Black Knight: replacement cards, no rules beyond the data card)
- Why: "Apply the special rules supplied with that expansion" pointed at rules that do not exist; the expansion supplies only the cards. Saying so closes the entry. The printed ability is not restated because Appendix B replaces the printed data card.
- Mechanical: no
- Edits: boss-E28

### boss-011 · lead item 4, the shared mega-boss framework
- Question: Do §6.7, §15 and §16 agree with the framework that every mega-boss booklet repeats, and are mega-boss game board rules stated once?
- This book now: §6.7 owns the setup after the main-boss, the Level 4 encounter and the flip to the mega-boss side; §15 owns the encounter; §17.8 and §17.9 each open by citing §6.7.
- Evidence: the framework pages are the same in all eight booklets (for example `DS-Four-Kings-Rules-web.txt` lines 135–330): game board beside the bonfire tile, encounter side up; one random Level 4 card, replaced if its sets are missing; four entry nodes; a cleared Level 4 encounter is not fought again; no free rest after it, a spark to rest; flip the board, fog gate on its doorway; boss on the mega-boss spawn node; data and behaviour cards as for any boss; the mega-boss's defeat wins the game. No booklet states a Level 4 rule peculiar to its boss.
- Ruling: CONFIRM as written, and ADD one sentence at the head of §17.10
- Why: The book agrees with the framework and states it once, in §6.7 and §15. Where it differs it does so on purpose, through the author's systems, and none of these is reopened here: one spark is added after the main-boss where the booklets reset the dial (§6.7 step 8, §7.4); the Level 4 soul reward follows the book's table, not "8 souls per character" (§7.6); the Level 4 encounter awards one mega-boss treasure card (lead item 19); the aggro token starts on the highest threat where the booklets let the players choose (§15.2); the behaviour deck is built at setup and the scry takes the place of "reveal a card for each gravestone" (§15.5); the model faces the entry nodes (boss-014). The new sentence at the head of §17.10 says once, for all seven new entries, that the board and the Level 4 encounter are §6.7's and that an entry's deck procedure replaces the general one.
- Mechanical: no
- Edits: boss-E20 (opening paragraph)

### boss-012 · lead item 5, Ornstein & Smough
- Question: Is the pair one boss with a shared health dial and a deck whose cards each name one acting model (Gate 1 OQ-25), or two models with their own health that both act each turn, as published?
- This book now: §17.1 (Two Boss Models in One Encounter) and §17.2: one data card, one health dial, one deck; each card names the model that acts and the other does nothing; one ordinary heat-up; both models stay until the boss is defeated. §2.3 and F.A.Q. §22.5 repeat it. The author's own manuscript listed the two as separate main-bosses (`work/phase2a/source/02_game_components.md` lines 128–130); OQ-25 chose the shared reading because it "matches the printed single data card and health dial".
- Evidence:
  - Official 2017 core rules: the rulebook lists "Dragon Slayer Ornstein & Executioner Smough" as one main boss (`DS-Core-Rules-lores.txt` lines 167–177, 1709) and gives the only multi-boss rules in the text: one boss model to a node, a boss moving onto another boss's node pushes it (lines 430–433), and that push is the only push of a boss (lines 968–971). It leaves the rest to the cards: "Some bosses have special rules on their boss data card which alter how the heat up functions" (lines 1398–1400).
  - The cards (community transcription in DSBG-Shuffle, card images "Ornstein – data" and "Smough – data", `lib/dsbg_shuffle_behaviors.py` lines 32 and 1703–1835, `lib/dsbg_shuffle_behavior_decks.py` lines 718–737): there are two data cards. Ornstein, "United We Stand: Ornstein and Smough both activate each turn. When Smough dies, Ornstein gains [10] Health, and Ornstein's heat up cards become the new behavior deck. Ornstein spawns on the Main Boss node." Smough, "Divided You Fall", the mirror image with 15 health. Ornstein has health 20, block 3, resist 3; Smough health 30, block 2, resist 2; neither has a heat-up point; deck size 5. The 15 behaviour cards are five paired cards (for example "Gliding Stab & Hammer Smash"), each with one behaviour and one dodge difficulty per model, five Ornstein heat-up cards and five Smough heat-up cards.
  - Official 2024 re-issue of the core set: "2x Main Boss Miniature, 2x Main Boss Data card, 15x Main Boss Behaviour cards" (rulebook component page). The 2017 box lists eight dials, which is one spark dial and seven health dials: four mini-bosses, the Dancer, Ornstein, and Smough (retail listing; inference).
  - Explorers booklet: the Old Dragonslayer "uses the miniature for Ornstein, half of the Ornstein & Smough main boss … alongside this new boss's health dial" (`DS-Explorers-Rules-Web.txt` lines 352–357).
  - Extended Rules, Hollowed Edition: silent on how the pair is fought.
  - Online: publisher forum thread 37344 and BoardGameGeek threads 2350492 and 1789313 (search summaries only): the pair share a five-card deck showing both bosses; when one dies the survivor's heat-up cards become the deck and the survivor gains health; one starts on the main-boss node and one on the mini-boss node; players debate which to kill first.
- Ruling: CHANGE. Adopt the official structure, and revise Gate 1 OQ-25 for Ornstein & Smough (its Twin Gargoyles half stands).
- Why: OQ-25 rested on a premise that the evidence contradicts: the pair has two data cards and two health dials, and every paired card gives both models a behaviour, so "each card names the model that acts" cannot be played with the printed cards. The official fight is also the better design. It asks one clear question, which of the two to bring down first, and answers it with a second phase that differs by the choice (five different heat-up cards, a different survivor, a different heal); the shared-dial version has no such decision and no second act. It costs no extra rules, because the Four Kings need the same several-models framework (own dial per model, every model acts on each card), so one sub-section of §17.1 now serves both.
- Designer's calls inside the ruling, each to be checked against the printed cards: (a) Ornstein acts before Smough on each card, the order in which every card names them; (b) Ornstein starts on the main-boss spawn node and Smough on the mini-boss spawn node (the transcription of Smough's card also says "Main Boss node", which cannot be right with one boss model to a node; the forum summary gives one on each); (c) the survivor's health gain stops at its starting health, which the card leaves open and a BoardGameGeek thread asks without a visible answer; the cap rewards concentrating on one target and matches the meaning of healing everywhere else in this book; (d) the heat-up (deck change and heal) is carried out at the start of the next boss turn, the one timing this book now uses for every heat-up (boss-018).
- Mechanical: yes
- Edits: boss-E08 (§17.1), boss-E10 (§17.2), boss-E07 (§16.5), boss-E42 (§2.3), boss-E46 (F.A.Q. §22.5), boss-E30 (glossary, Boss)

### boss-013 · lead item 13, fog gate shortcut
- Question: Does the fog gate shortcut on the bonfire tile cost skip stamina, and is it open when encounters on the route are not cleared?
- This book now: §15.1: the shortcut begins the boss encounter at once; the route's encounters are neither fought nor skipped and no stamina cube is placed; an uncleared encounter does not bar it; not available in campaign play.
- Evidence: author's manuscript: "travel directly to the boss encounter from the bonfire tile to try again without having to fight any encounters" (`work/phase2a/source/15_boss_encounters.md`, The Fog Gate). Official 2017: no shortcut; after a rest "they will need to fight their way back to the Fog Gate" (`DS-Core-Rules-lores.txt` lines 728–733). Official 2022: defeating the mini-boss lets later rests start from its space, "allowing the players to avoid the earlier encounters" (lines 2294–2297). Extended, Hollowed: silent on a fog gate shortcut.
- Ruling: CONFIRM as written
- Why: The shortcut is the author's reward for reaching the boss, and it removes the published game's most criticised chore, re-clearing the route before every boss attempt. Charging the skip cost would tax exactly the retry the shortcut exists to speed up, and would add book-keeping with no decision in it. The choice that matters is kept: walk the route again for souls and treasure, or go straight in.
- Mechanical: no
- Edits: none

### boss-014 · lead item 13, starting facing
- Question: Which way does a boss face when it is placed at the start of its encounter?
- This book now: §15.2 step 6: the centre of the front arc faces the adjacent node closest to the entry nodes; the players choose on a tie; a boss's special rules may replace the step.
- Evidence: official 2017 and 2022: the model is placed on its spawn node and no facing is given (`DS-Core-Rules-lores.txt` lines 1370–1373; 2022 lines 2177–2178 say only that a boss always faces an adjacent node). Mega-boss booklets: "front arc facing the centre of the Mega Boss game board" in seven booklets and Kalameet's (for example `DS-Four-Kings-Rules-web.txt` lines 373–377); Manus alone: "facing the board edge where the entry nodes are located" (`DS-MFA-Rules.txt` lines 380–383). The Four Kings board diagram (booklet p. 5) shows the mega-boss spawn node on the centre line near the far edge, so facing the centre and facing the entry nodes are the same direction. No data card shows a facing.
- Ruling: CONFIRM as written, for every boss
- Why: One rule that a player would guess (the boss faces the party as it comes through the fog) covers the mini-boss and main-boss, where the official rules say nothing, and reproduces the booklets' result for the mega-bosses; Manus's wording is this rule exactly. A separate "faces the centre" clause for mega-bosses would be a second rule with the same outcome. The new §17.10 entries therefore state no starting facing; the Old Iron King's entry names his starting node, and placements made during a fight (Inferno, Beam) state their own facing as the booklets do.
- Mechanical: no
- Edits: none

### boss-015 · lead item 13, order of character turns
- Question: In a boss encounter do the players choose which character acts next, or do characters act in descending threat order as in other encounters?
- This book now: §16.1: the players choose; no character acts twice in a round until every living character has acted.
- Evidence: author's manuscript: "one character may take their turn … characters must take an equal number of turns" (`work/phase2a/source/16_boss_turns.md`). Official 2017: the first character is the players' choice, then clockwise (`DS-Core-Rules-lores.txt` lines 886–893); 2022: the same alternation. Extended, Hollowed: no boss-specific order.
- Ruling: CONFIRM as written
- Why: This is the best decision in a boss fight and it is the author's. Because the boss's next card is often known from the last cycle, and because the aggro token follows the character who last wounded the boss (§16.4), choosing who acts before each boss turn is choosing who is attacked and who gets the weak arc. Fixed threat order would script the fight; free choice within a round keeps the turn count fair.
- Mechanical: no
- Edits: none

## Chapter 15 — Boss Encounters

### boss-016 · ch. 15, starting facing (§15.2 step 6)
- Question: The same question as boss-014.
- This book now: §15.2 step 6.
- Evidence: see boss-014.
- Ruling: CONFIRM as written
- Why: See boss-014.
- Mechanical: no
- Edits: none

### boss-017 · ch. 15, fog gate shortcut (§15.1)
- Question: The same question as boss-013.
- This book now: §15.1.
- Evidence: see boss-013.
- Ruling: CONFIRM as written
- Why: See boss-013. The skip cost (OQ-10) is not charged.
- Mechanical: no
- Edits: none

### boss-018 · ch. 15, heat-up shuffle and timing (§15.5)
- Question: When a boss heats up, is the heat-up card shuffled into the remaining draw pile only, or are the deck and the discard pile reshuffled together; and when exactly is it done?
- This book now: §15.5: the card is shuffled into the cards that remain in the deck; the discard pile keeps its order; if no cards remain the heat-up card alone is the deck. Timing has two cases: after the attack that caused it (character's turn), or after the current card is resolved and discarded (boss's own turn).
- Evidence: official 2017: "Take one random Heat Up behaviour card and shuffle it into the behaviour deck. Note that players will now need to relearn the boss's attack pattern as well as having to face a powerful Heat Up card" (`DS-Core-Rules-lores.txt` lines 1392–1396). Official 2022: the same sentence, "relearn the boss's attack pattern" (lines 2146–2153). Booklets: the Last Giant's heat-up removes Arm cards from the whole deck and "shuffle[s] the new behaviour deck" (`DS-TLG-Rules.txt` lines 384–395); Manus's is marked as the exception, "Do not shuffle the behaviour deck!" (`DS-MFA-Rules.txt` lines 384–396); Vordt's Frostbreath is timed "at the start of his activation" after the heat-up (`DS-VotBV-Rules-web.txt` lines 475–490). Extended, Hollowed: silent. Online: BoardGameGeek thread 1819893 (search summary): consensus is to shuffle deck and discard pile together with the heat-up card; one poster notes that otherwise "you can 100% predict where the Heat Up card will go by getting the boss to Heat Up when the deck is empty"; a suggested fix for mid-turn cases is to shuffle "before the boss's next draw". The DSBG-Shuffle program reshuffles the whole deck.
- Ruling: CHANGE. On heat-up the behaviour deck and the discard pile are gathered, one random heat-up card is added, and all are shuffled into a new deck; this is done at the start of the boss's next turn, before it draws.
- Why: Both official rulebooks say what the heat-up is for: the party must learn the boss again. The drafted reading keeps most of the learned order and, timed well, tells the players exactly where the new card lies, so the fight's turning point becomes its most predictable moment. The full reshuffle is also the simpler procedure: three steps, no special case for an empty deck, and the same "gather, change, shuffle" shape that Artorias, the Last Giant and the Guardian Dragon already use. One timing replaces two: the reshuffle is invisible until the boss draws, so doing it at the start of the boss's next turn changes nothing except that the last card's weak arcs stay in force until then, which removes the only awkward question (what are the weak arcs after the discard pile has gone).
- Mechanical: yes
- Edits: boss-E01, boss-E02 (§15.5), boss-E04, boss-E05 (§16.1), boss-E31 (glossary, Heat-up)

### boss-019 · ch. 15, deck reset between attempts (§15.5, Deck Reset)
- Question: Is a boss's behaviour deck rebuilt from all its cards before each new attempt?
- This book now: yes; undealt standard cards are set aside rather than boxed, and a card revealed by a scry is lost when the deck is rebuilt.
- Evidence: official 2017: the deck is created each time a boss encounter starts, from random cards, "This allows boss encounters to be new each time you face them!" (lines 1375–1390). Official 2022: the deck is drawn "after setting up a boss encounter" (lines 2138–2143). Extended, Hollowed: silent. Online: BoardGameGeek thread 1824467 exists on the point (title only).
- Ruling: CONFIRM as written
- Why: It matches both official editions and keeps a failed attempt from handing the party the answer sheet. Losing a scried card on reset is the fair price of a failed attempt and needs no extra rule.
- Mechanical: no
- Edits: none

### boss-020 · ch. 15, weak arcs on a card with several arc diagrams (§15.6)
- Question: Which diagram shows the weak arcs when a card has more than one, and are the arc-state names right?
- This book now: the diagram beneath the last attack icon; states neutral, attack, weak (black, green, red).
- Evidence: official 2017: "look at the last attack icon on the behaviour card on the top of the discard pile" (lines 1397–1400); the 2022 symbol key names the states "Neutral boss arc, Attack boss arc, Weak boss arc" (line 2360).
- Ruling: CONFIRM as written
- Why: It is the official rule, and "neutral" is the official name in the icon set this book uses.
- Mechanical: no
- Edits: none

### boss-021 · ch. 15, parry of boss attacks (§15.6, Defence)
- Question: Which boss attacks may be parried?
- This book now: an attack that targets one character and is not an area attack, a node attack, or a push-attack.
- Evidence: official rules have no parry; the mechanic is the author's (§9.6). The exclusion list is the manuscript's.
- Ruling: CONFIRM as written
- Why: The list follows from what a parry is, one character turning one blow aside. It is the author's system and is consistent with §9.6 and the glossary as they now stand.
- Mechanical: no
- Edits: none

### boss-022 · ch. 15, push off a boss's node (§15.6, Characters and Arcs)
- Question: Does the same-arc limit apply to every push off a boss's node, including a push-attack and the node model limit?
- This book now: yes, whatever causes the push; wall fallback as the official rule; the push after a leap is free.
- Evidence: official 2017: a character "pushed off of a boss's node … must remain in the same arc", with the wall fallback (lines 1353–1360). Official F.A.Q.: a push from a boss's attack need not stay in the arc, "it simply needs to be moved farther from the attacking model" (`Dark_Souls_The_Board_Game_FAQ.txt`, third question). 2022: same-arc for any push off the node (lines 2175–2179).
- Ruling: CONFIRM as written
- Why: One rule for every push off the node is simpler than the 2017 F.A.Q.'s exception and agrees with the 2022 text. "Directly away from the boss" has no meaning for a character standing on the boss's base, and "out through the arc you stand in" is the natural completion. This is a deliberate difference from the 2017 F.A.Q.
- Mechanical: no
- Edits: none

### boss-023 · ch. 15, dodge on a boss's node (§15.6, Defence)
- Question: Where may a character go after a successful dodge on, or onto, a boss's node?
- This book now: to any valid adjacent node or any other arc of the base; a character who dodges onto the boss's node chooses the arc.
- Evidence: official 2017: "ignore the normal rules for boss arcs and instead move to any arc or onto any adjacent node" (lines 1367–1371); 2022 the same (lines 2180–2183).
- Ruling: CONFIRM as written
- Why: Official rule, with "any other arc" because this book's dodge movement is compulsory. Choosing the arc on arrival is the only answer that needs no further rule.
- Mechanical: no
- Edits: none

### boss-024 · ch. 15, boss tiles (§15.3)
- Question: How are the two boss tiles joined, and is terrain ever placed on a boss tile?
- This book now: joined along one edge into one rectangular tile; no encounter card, traps, or terrain unless a boss's special rules place some.
- Evidence: official 2017: "place both the mini boss and main boss tiles down to create one large rectangular room" (lines 1361–1364); 2022: "as though they were a single large tile" (lines 2100–2103).
- Ruling: CONFIRM as written; ADD the one exception that the Asylum Demon mini-boss is fought on its expansion's game board (see boss-052)
- Why: The text matches both editions. Whether a boss tile is printed with terrain nodes does not matter, since nothing is placed without an encounter card.
- Mechanical: yes (the exception only)
- Edits: boss-E03

### boss-025 · ch. 15, worked examples use an unnamed boss
- Question: May the examples keep illustrative values?
- This book now: unnamed mini-boss, health 24, heat-up 12, block 2, resist 1.
- Evidence: none needed.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: An example states what happens under the rules and does not need a real card. The heat-up example is rewritten for boss-018 with the same values.
- Mechanical: no
- Edits: boss-E02

### boss-026 · ch. 15, the sentence after the chapter introduction
- Question: May "Bosses follow the enemy rules of §8 and §9 except as stated in this chapter and §16" stand as its own paragraph?
- This book now: it does.
- Evidence: both official editions open their boss chapter with the same statement (2017 lines 1244–1248; 2022 lines 2109–2111).
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Editorial placement; the sentence is correct. The introduction's "a boss is a single model" is flavour; the glossary entry Boss is corrected in boss-070.
- Mechanical: no
- Edits: none

### boss-027 · ch. 15, repeated glossary additions
- Question: Do the repeated ADD lines for Node attack, Push-attack, Push-move and Leap cause a conflict?
- This book now: one entry for each in `12_glossary.md`.
- Evidence: glossary as it stands.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Integration is done and each headword appears once.
- Mechanical: no
- Edits: none

### boss-028 · ch. 15, cross-chapter dependencies satisfied by chapter 15
- Question: Are the listed dependencies (§5.1, §6.5 to §6.7, §7.5, §8.4, §9.6, §10.3, §11.5, §12.1, §12.2, §13, §17.1) still met?
- This book now: each is met in the chapter as read.
- Evidence: chapters as they stand after the lead editor's applied rulings.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Checked while reading; boss-018 changes the heat-up steps that §12.2 and §13 cite, and both still read correctly (see cross-cluster effects).
- Mechanical: no
- Edits: none

### boss-029 · ch. 15, dependencies placed on other chapters
- Question: Do §18.2 and §17 carry what §15 defers to them?
- This book now: §18.2 states that the fog gate token gives no shortcut in campaign play; §17 states every special placement, deck procedure and heat-up.
- Evidence: `10_manuscript_chapter_18_campaign_play.md` §18.2; chapter 17 with the edits of this memo.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Both are met; the nine placeholders were the last gap, and seven are now filled.
- Mechanical: no
- Edits: none

