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
- Edits: boss-E20 to boss-E28 (entries); boss-E14, boss-E32 to boss-E34 and boss-E38 to boss-E41 (defined terms and glossary); boss-E44 (§2.9)

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
- Ruling: CONFIRM as written (one introductory sentence is added at the head of §17.10, with boss-002)
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
- Ruling: CHANGE: adopt the official structure, and revise Gate 1 OQ-25 for Ornstein & Smough (its Twin Gargoyles half stands).
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
- Ruling: CHANGE: on heat-up the behaviour deck and the discard pile are gathered, one random heat-up card is added, and all are shuffled into a new deck; this is done at the start of the boss's next turn, before it draws.
- Why: Both official rulebooks say what the heat-up is for: the party must learn the boss again. The drafted reading keeps most of the learned order and, timed well, tells the players exactly where the new card lies, so the fight's turning point becomes its most predictable moment. The full reshuffle is also the simpler procedure: three steps, no special case for an empty deck, and the same "gather, change, shuffle" shape that Artorias, the Last Giant and the Guardian Dragon already use. One timing replaces two: the reshuffle is invisible until the boss draws, so doing it at the start of the boss's next turn changes nothing except that the last card's weak arcs stay in force until then, which removes the only awkward question (what are the weak arcs after the discard pile has gone).
- Mechanical: yes
- Edits: boss-E01, boss-E02 (§15.5), boss-E04, boss-E05 (§16.1), boss-E31 (glossary, Heat-up), boss-E48 (F.A.Q. §22.5)

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
- Ruling: CONFIRM as written (the one exception, the Asylum Demon mini-boss fought on its expansion's game board, is made under boss-052)
- Why: The text matches both editions. Whether a boss tile is printed with terrain nodes does not matter, since nothing is placed without an encounter card.
- Mechanical: no
- Edits: none (boss-E03 is listed under boss-052)

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

## Chapter 16 — Boss Turns

### boss-030 · ch. 16, order of character turns (§16.1)
- Question: The same question as boss-015.
- This book now: §16.1; the players choose.
- Evidence: see boss-015.
- Ruling: CONFIRM as written
- Why: See boss-015.
- Mechanical: no
- Edits: none

### boss-031 · ch. 16, repeat on a behaviour card (§16.1)
- Question: Does the repeat icon on a behaviour card repeat the whole row of icons, with targets found again each time?
- This book now: yes to both.
- Evidence: official 2017: "the enemy will perform its entire behaviour multiple times when resolving that behaviour card" (lines 1441–1444). Official 2022: "the boss resolves their entire row of behaviour symbols the number of times shown" (lines 2257–2264). The glossary entry Repeat, as amended by the combat rulings, now says the same for enemies and bosses.
- Ruling: CONFIRM as written
- Why: Official in both editions. Finding the target again at each pass is the only reading that works when the first pass has pushed or killed the first target.
- Mechanical: no
- Edits: none

### boss-032 · ch. 16, push-move against a wall (§16.2, Push-Moves)
- Question: When a boss's push-move cannot push a character directly away, is the character pushed within the arc, with the wall fallback, where §8.4 would leave a character in place?
- This book now: yes, for bosses only.
- Evidence: official 2017 worked example, stage 4: the character "is pushed again, onto the only node within the boss's front arc" (lines 1520–1525), and the arc rule with its wall fallback (lines 1353–1360).
- Ruling: CONFIRM as written
- Why: It reproduces the official example and means a boss's charge always moves the characters in its path, which is what the icon promises. The difference from §8.4 is real but lives in one place and is cited from §8.4.
- Mechanical: no
- Edits: none

### boss-033 · ch. 16, arc of a character on a node the boss enters (§16.2)
- Question: In which arc is a character placed when a boss moves onto their node?
- This book now: the arc in which the node lay immediately before the boss entered it; the player chooses if it lay in two.
- Evidence: official 2017: "the arc that was facing the character before the boss moved" (lines 1434–1437). Official 2022: "the same arc they were in before the movement began" (lines 2252–2257).
- Ruling: CONFIRM as written
- Why: Because the boss turns before each node, "immediately before it entered" is the only wording that gives one answer for a movement of several nodes; the result is the one a player expects (a boss that walks forward onto a character has that character in front of it).
- Mechanical: no
- Edits: none

### boss-034 · ch. 16, leap completions (§16.2, Leap)
- Question: Are the three completions sound: a leap at a target on the boss's own node still pushes; a character with no valid adjacent node stays and chooses an arc; a leap whose push icon carries a damage value attacks as a push-move does?
- This book now: all three, as drafted.
- Evidence: official 2017: the boss is placed on the target's node, keeps its facing, "All leaps also have the Push icon … characters can be pushed onto any adjacent node. They are not considered to be in any particular arc" (lines 1456–1482). Official 2022: characters pushed by this movement go to an adjacent node of their choice, ignoring arcs (lines 2261–2266). Neither covers the three cases. The Four Kings and Old Iron King booklets reuse the leap push for their own placements.
- Ruling: CONFIRM as written
- Why: Each completion applies the nearest existing rule (the leap's own push, §8.4's "no valid node, no push", the push-move's damage) and adds none. The new entries for the Four Kings and the Old Iron King lean on this sub-section, so it must stay as it is.
- Mechanical: no
- Edits: none

### boss-035 · ch. 16, icon tokens for pushes (§16.2, §16.3)
- Question: Are the push icons mapped to the right extracted assets?
- This book now: ast-0058 for a push, ast-0031 for a push with a damage value; no asset for the leap or skull icons.
- Evidence: the icon list in `work/phase2a/DRAFTING_BRIEF.md` §7.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: A layout matter. The new §17.10 text names its new icons in words (Inferno, Bonus Behaviour, Beam, crawl, corrosion), because no extracted asset exists for them, and uses only tokens that chapter 17 already uses.
- Mechanical: no
- Edits: none

### boss-036 · ch. 16, aggro in boss fights (§16.4)
- Question: How does the aggro token move in a boss fight?
- This book now: it starts on the highest threat; at the end of a character's turn it moves to that character if they lowered the boss's health dial; a riposte moves it at the end of that boss turn; an attack reduced to nothing does not move it; a summon never holds it, though a Distract icon makes the boss treat the summon as the holder for one turn.
- Evidence: author's manuscript: "simply move the aggro token to a character's dashboard if they deal any damage to the boss during their turn. If no damage is dealt, the aggro token remains stationary" (`work/phase2a/source/16_boss_turns.md`). Official 2017 and 2022: a character gains the token at the start of each of their own turns, whatever they do (2017 lines 1018–1021; 2022 line 1415); it starts with a character of the players' choice. Phantoms booklet: Distract (lines 293–297). Extended, Hollowed: no boss-specific rule.
- Ruling: CONFIRM as written (the one addition, for other enemy models in a boss encounter, is made under boss-059)
- Why: The author's rule is the better one. Under the official rule the boss attacks whoever acted last, full stop; here a character can act without drawing the boss (heal, reposition, miss) and a damaging blow is also a decision to take the next attack. Combined with free turn order (boss-015) it is the tactical core of the fight, and it costs one sentence.
- Mechanical: no
- Edits: none (boss-E06 and boss-E35 are listed under boss-059)

### boss-037 · ch. 16, dead characters when a boss is defeated (§16.5)
- Question: Does a character who died in the boss encounter receive the soul reward and an ember token, and stay out of play (and out of the PvP encounter) until the free rest?
- This book now: yes.
- Evidence: Hollowed Edition: dead players receive the boss's souls "even if that player died during the boss encounter" (lines 319–322). Official rules: a death fails the encounter, so the case does not arise. §20.1 bars such a character from the PvP encounter.
- Ruling: CONFIRM as written
- Why: The reward belongs to the party, and the free rest that follows restores everyone, so nothing is lost by waiting; a special revival before the PvP encounter would be a rule with one use.
- Mechanical: no
- Edits: none

### boss-038 · ch. 16, the final boss (§16.5)
- Question: Does the defeat of the final boss end the game without rewards?
- This book now: yes; a last PvP encounter may follow.
- Evidence: official 2017: "When the party defeats the main boss, they win the game!" (lines 1411–1413); booklets: the same for a mega-boss.
- Ruling: CONFIRM as written
- Why: Rewards after the game is won have no use. §20.1's phrase "follows the rewards for the boss's defeat" is harmless after the final boss, where there are none; noted for the PvP owner under cross-cluster effects.
- Mechanical: no
- Edits: none

### boss-039 · ch. 16, boss treasure cards not awarded (§16.5 step 3)
- Question: Where do a defeated boss's other treasure cards go?
- This book now: to the game box.
- Evidence: official rules put all of a boss's treasure in the inventory (2017 lines 1406–1409); awarding one at random is the author's rule (§7.7).
- Ruling: CONFIRM as written
- Why: Once only one card is awarded, the box is the only tidy destination; any other would create a second source of boss treasure.
- Mechanical: no
- Edits: none

### boss-040 · ch. 16, where the spark and the free rest are stated (§16.5)
- Question: Is the spark for a defeated boss stated once?
- This book now: §16.5 attributes the spark and the rest to the setup steps of §6.6 and §6.7 and says each is gained once; §7.4 cites §16.5.
- Evidence: the three sections as they stand.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: The statements agree; the cross-references form a chain, not a contradiction. The Ornstein & Smough and Four Kings changes do not disturb it, because Boss Death is still resolved once per boss.
- Mechanical: no
- Edits: none

### boss-041 · ch. 16, cross-chapter dependencies satisfied by chapter 16
- Question: Are the listed dependencies still met?
- This book now: yes, as read.
- Evidence: chapters as they stand.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Checked. §16.5's sentence on bosses with two models is rewritten for boss-012.
- Mechanical: no
- Edits: boss-E07

### boss-042 · ch. 16, dependencies placed on other chapters
- Question: Do §18.1 and §18.3 state how the spark, rest and setup differ in campaign play, and does §17 define every icon found on only one boss's cards?
- This book now: §18.1 (Section Completion) and §18.3 do; §17 defines Wind Up, calamity, strafe and Raise Skeleton.
- Evidence: `10_manuscript_chapter_18_campaign_play.md` lines 46–52 and 93; chapter 17.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Met. The new entries add the crawl, Inferno, Bonus Behaviour and Beam icons and the shaft icon on Manus's cards, each defined where it is used.
- Mechanical: no
- Edits: none

### boss-043 · ch. 16, glossary amendments
- Question: Do the amended entries Aggro token, Round and Turn agree with the chapter?
- This book now: they do, as amended by later rulings (Turn now mentions the summon).
- Evidence: `12_glossary.md`.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Checked; Aggro token gains one clause for boss-036.
- Mechanical: no
- Edits: boss-E35

## Chapter 17 — Boss Special Rules

### boss-044 · ch. 17, dependency from §2.3 (Ornstein & Smough)
- Question: Does §17 state what §2.3 says of the pair?
- This book now: §2.3 repeats the shared-dial version.
- Evidence: see boss-012.
- Ruling: CHANGE (follows boss-012)
- Why: §2.3 must describe the pair as §17.2 now does.
- Mechanical: yes
- Edits: boss-E42

### boss-045 · ch. 17, dependency from §5.3 (one boss model to a node)
- Question: Does §17.1 state the push of one boss model by another?
- This book now: yes, with the consequences for facing and for characters on either node.
- Evidence: official 2017 lines 430–433 and 968–971.
- Ruling: CONFIRM as written
- Why: The paragraph is carried unchanged into the rewritten sub-section; it now also serves the Four Kings, whose arriving king pushes a king standing on the spawn node.
- Mechanical: no
- Edits: boss-E08 (text kept)

### boss-046 · ch. 17, dependency from §5.5 (pillars)
- Question: Do §5.5 and §17.3 agree on when pillars are placed?
- This book now: §5.5 says "a mega-boss encounter"; §17.3 says "every boss encounter fought on the mega-boss side of that game board".
- Evidence: Asylum Demon booklet lines 197–203: both the mini-boss and the mega-boss encounters include the pillars.
- Ruling: CHANGE (§5.5 aligned with §17.3)
- Why: The Asylum Demon mini-boss is fought on the same board (boss-052), so "mega-boss encounter" in §5.5 is too narrow.
- Mechanical: no
- Edits: boss-E45

### boss-047 · ch. 17, dependency from §6.7 step 5 (mega-boss special rules)
- Question: Does §17 give the special rules that §6.7 step 5 applies?
- This book now: for three mega-bosses; the other seven are delegated.
- Evidence: see boss-002 to boss-008.
- Ruling: CHANGE (the seven are now given)
- Why: Every mega-boss now has its rules in §17.
- Mechanical: yes
- Edits: boss-E20 to boss-E26

### boss-048 · ch. 17, dependency from §2.9 (expansion components)
- Question: Are the components that §17 rules on listed in §2.9?
- This book now: yes; §2.9 already lists the Four Kings' models, dials and identifier tokens, the Gaping Dragon's corrosion tokens, the Guardian Dragon's Fiery Breath cards and the Old Iron King's "Fire Beam cards".
- Evidence: `10_manuscript_chapter_02_game_components.md` §2.9 as it stands; booklet contents pages.
- Ruling: CONFIRM as written (one component name is aligned under boss-007)
- Why: Only the Old Iron King's six cards need their name changed to "Beam cards", the name the rules use, so that they are not confused with the three Fire Beam behaviour cards (boss-007).
- Mechanical: no
- Edits: none (boss-E44 is listed under boss-007)

### boss-049 · ch. 17, dependency from §20.1 (PvP after the Twin Gargoyles)
- Question: Does a PvP encounter follow each Gargoyle or only the second?
- This book now: only the second (§17.1, Twin Gargoyles).
- Evidence: the pair is one boss encounter (OQ-25, kept).
- Ruling: CONFIRM as written
- Why: One boss, one Boss Death, one PvP encounter. For the same reason one PvP encounter follows Ornstein & Smough and one follows the Four Kings.
- Mechanical: no
- Edits: none

### boss-050 · ch. 17, Ornstein & Smough (§17.1, §17.2)
- Question: The same question as boss-012, with the three inferences (a) starting nodes, (b) conditions on the shared dial, (c) one heat-up and no model leaving play.
- This book now: as boss-012.
- Evidence: see boss-012.
- Ruling: CHANGE (see boss-012)
- Why: (a) is kept in substance, one model on each boss spawn node, now with Ornstein named for the main-boss node; (b) falls away, since each model holds its own condition tokens; (c) is reversed: the first model to fall leaves play and that is the heat-up.
- Mechanical: yes
- Edits: boss-E08, boss-E10

### boss-051 · ch. 17, Twin Gargoyles (§17.1)
- Question: Are the four settled details and the treatment of a failure against the first Gargoyle sound?
- This book now: one encounter in two parts; the model returns to the spawn node; a character on that node chooses an arc; the second Gargoyle acts after the turn of the character who felled the first; a summon stays; failure against either means both are fought again.
- Evidence: official footnote: "The party receives the Gargoyles' treasure only if they defeat two Gargoyle boss encounters back-to-back. If they are defeated by the second Gargoyle, they must fight both Gargoyles" (`DS-Core-Rules-lores.txt` lines 1680–1685; repeated in the Asylum Demon and Phantoms booklets). Gate 1 OQ-25.
- Ruling: CONFIRM as written
- Why: "Back to back" with nothing between is the simplest complete reading: reset the dial and the deck, carry on. This book gives no recovery after any boss (§16.5), so none between the two parts is consistent. A failure against the first Gargoyle is an ordinary failed boss encounter, so "both again" follows without a rule of its own.
- Mechanical: no
- Edits: none

### boss-052 · ch. 17, Asylum Demon (§17.3)
- Question: On which tile is the Asylum Demon mini-boss fought, and what is the special ability printed on the two data cards?
- This book now: §17.3 does not say where the mini-boss is fought and calls the shared ability Pillar Smasher.
- Evidence: Asylum Demon booklet `DS-AD-Rules-web-EN.txt` lines 183–190: "The Asylum Demon is used just like any other mini boss except that the boss encounter takes place on the Mega Boss game board instead of the Mini Boss tile"; lines 197–212 (Pillar Smasher: both encounters include the pillars); data cards at lines 120 and 159: "Pillars of Woe"; lines 433–445: the Stray Demon "follows the standard rules for behaviour deck creation and heats up like a mini boss or main boss does". The rest of §17.3 (pillar placement, destruction before the attack, one damage and stagger within one node, several pillars at once, restoration at the bonfire, Wind Up) matches the booklet.
- Ruling: CHANGE (tile stated; ability renamed)
- Why: Both open facts are settled by the booklet. Putting the mini-boss on the same board removes the special case "an encounter fought on a tile without pillar nodes", so the section gets shorter as well as complete. §15.3, §5.5, §2.3 and the glossary entry Mini-boss each take one clause.
- Mechanical: yes
- Edits: boss-E11, boss-E12, boss-E03, boss-E45, boss-E47, boss-E36

### boss-053 · ch. 17, pillar damage (§17.3)
- Question: Is the damage of a destroyed pillar unblockable, and does it affect only characters?
- This book now: not an attack; cannot be blocked, resisted or dodged; characters only.
- Evidence: booklet lines 204–208: "any characters within one node of the pillar token immediately suffer 1 damage and the stagger condition".
- Ruling: CONFIRM as written
- Why: "Immediately suffer" with no attack icon is flat damage, and the booklet says characters. A summon is spared, which is consistent with summons ignoring traps (§12.1).
- Mechanical: no
- Edits: none

### boss-054 · ch. 17, Wind Up (§17.3)
- Question: Is the Wind Up movement a Run for every rule, and does it stop the character resting on their own next turn?
- This book now: every rule that applies to a Run applies; nothing is said of the Rest action, so the general rule governs and it does not.
- Evidence: booklet lines 213–225 (and the same text in the Last Giant booklet): "This movement is considered a run for purposes of rules interactions", with the example of armour that forbids running.
- Ruling: CONFIRM as written
- Why: The official text is reproduced. The movement happens in the boss's turn, so limits that count a character's own turn do not see it. Manus's Overextended is written with the same sentence (boss-006).
- Mechanical: no
- Edits: none

### boss-055 · ch. 17, Great Grey Wolf Sif (§17.4)
- Question: When is the cool-down card Limping Strike used?
- This book now: "used only as Sif's data card directs".
- Evidence: Darkroot booklet: the Cool Down "occurs when Sif is edging close to death" (`DS-Darkroot-Rules-web.txt` lines 174–183). Data card, in the community transcription (DSBG-Shuffle card image "Great Grey Wolf Sif – data" and `lib/dsbg_shuffle_behavior_decks.py` line 445): "Mournful Howl: Limping Strike is not a starting behavior card or a Heat Up card. When Sif is reduced to 3 health or less, replace the behavior deck with the Limping Strike card." A BoardGameGeek thread (3023917, search summary) describes the same effect.
- Ruling: CHANGE (the rule is written out)
- Why: The entry was the last "as the data card directs" in a chapter that promises to state each boss's rules. The rule is one sentence and gives Sif the game's only mercy phase, which is worth showing the reader. The threshold of three should be checked against the printed card.
- Mechanical: yes (a rule where the book had a pointer)
- Edits: boss-E13

### boss-056 · ch. 17, Artorias (§17.4)
- Question: Are the two removed cards taken from the deck and the discard pile together?
- This book now: yes: gather both, remove two at random, add all three heat-up cards, shuffle.
- Evidence: Darkroot booklet: "Rather than adding one Heat Up card to his existing behaviour deck, you remove two random behaviour cards and then add all three" (lines 194–200). DSBG-Shuffle does the same over the whole deck.
- Ruling: CONFIRM as written
- Why: "His existing behaviour deck" is all the cards in play. After boss-018 the general heat-up gathers the discard pile too, so Artorias's steps are now the general ones with two cards out and three in, and take the general timing.
- Mechanical: no
- Edits: none

### boss-057 · ch. 17, Old Dragonslayer (§17.6)
- Question: Does the Old Dragonslayer also heat up at a heat-up point?
- This book now: the sentence saying so was left out because the card could not be read.
- Evidence: Explorers booklet data card: "Corrupted Dragonslayer: The first three times the Old Dragonslayer loses 4 or more HP from one attack, add one random heat up card to the top of the behaviour deck", with a dash where the heat-up point is printed (`DS-Explorers-Rules-Web.txt` lines 158–171). DSBG-Shuffle records no heat-up value for this boss.
- Ruling: ADD (one sentence saying that the data card shows no heat-up point; the entry is otherwise confirmed as written)
- Why: The omission was right. Saying so in the entry stops a reader looking for a heat-up that does not exist.
- Mechanical: no
- Edits: boss-E15

### boss-058 · ch. 17, Black Dragon Kalameet (§17.8)
- Question: Does Kalameet keep its facing when placed on the landing node, and is the gravestone reveal rightly dropped?
- This book now: yes to both.
- Evidence: Kalameet booklet: after the strafe "place Kalameet on the landing node … Any characters on the landing node are pushed onto any adjacent node"; no facing given (`DS-BDK-Rules-web.txt` lines 462–481). The reveal for gravestones is the framework step that this book's scry replaces (boss-011).
- Ruling: CONFIRM as written
- Why: Keeping the facing is what a leap does and needs no new rule. The definition of Signature card in §17.8 is widened, because two of the new entries use the term (boss-003, boss-007).
- Mechanical: no
- Edits: boss-E14, boss-E32

### boss-059 · ch. 17, Executioner's Chariot (§17.9)
- Question: Are points (a) to (g) sound: the two models; every enemy acting before each character; aggro before the heat-up; scaling of the Mages and Skeletons; starting facing; no heat-up point and no second heat-up; Crush not applying to a dodge?
- This book now: as listed in the issue; (c) is not ruled on, so before the heat-up the token cannot move unless its holder dies.
- Evidence: Chariot booklet `DS-EC-Rules-Web.txt`: "the skeletal horse and the chariot" (lines 437–441); "other enemies will also activate during the enemy activation using their threat level to determine activation order as usual" (lines 455–462); data card front has no health, block or resist (lines 524–531); heat-up when the Chariot "is the only enemy model remaining" (lines 460–462); "Crush: If a character's armour roll or resistance roll prevents all of a behaviour card's damage, the character suffers 1 damage" (lines 383–387).
- Ruling: ADD for (c): damage to another enemy model in a boss encounter moves the aggro token as damage to the boss does. Points (a), (b), (d), (e), (f) and (g) are confirmed as written
- Why: (b) is official, hard as it is. (c) is a real gap: for the whole first part the Mages and Skeletons would attack one fixed character whatever the party did. The general clause in §16.4 fixes it without a Chariot-only rule and is what players would do unprompted. (g) follows from the card: a dodge is not a block or resist roll.
- Mechanical: yes ((c) only)
- Edits: boss-E06, boss-E35

### boss-060 · ch. 17, Raise Skeleton (§17.9, Unique Icons)
- Question: Is the icon rightly owned by §17.9, and limited to skeletons killed in the current encounter?
- This book now: yes to both.
- Evidence: Chariot booklet introduces the Raise Skeleton behaviour with the Black Hollow Mage (line 185 onward).
- Ruling: CONFIRM as written
- Why: The enemy and its icon come from this expansion, and §17.9 says the icon is resolved the same way in every encounter that holds a Black Hollow Mage. Moving the rule to §9 for the sake of six encounter cards would put an expansion rule in the core chapter; noted for the combat owner in case they prefer a one-line pointer there.
- Mechanical: no
- Edits: none

### boss-061 · ch. 17, dependency placed on §8.4 (boss pushed by a boss)
- Question: Does §8.4 list the displacement of one boss model by another and bar characters from pushing a boss?
- This book now: yes (`10_manuscript_chapter_08_combat_basics.md` lines 93, 122, 124).
- Evidence: as cited.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Met. §8.4 cites "§17.1" without a sub-heading, so the renamed sub-heading breaks no reference.
- Mechanical: no
- Edits: none

### boss-062 · ch. 17, dependency placed on §8.5 (conditions)
- Question: Does §8.5 own calamity, corrosion, frostbite and stagger?
- This book now: yes.
- Evidence: §8.5; the corrosion text agrees with the Gaping Dragon booklet (lines 443–453).
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Met. The new entries cite §8.5 and restate nothing.
- Mechanical: no
- Edits: none

### boss-063 · ch. 17, dependency placed on §9.4 and §9.5 (attacks that target nodes)
- Question: Do the defence rules treat an attack on nodes like any other attack, and does §9.5 state the move after a dodge?
- This book now: yes.
- Evidence: §9.4, §9.5 as they stand.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Met. The Inferno and Beam attacks rely on it exactly as the strafe does.
- Mechanical: no
- Edits: none

### boss-064 · ch. 17, dependency placed on §13 (mimics)
- Question: Does §13 own every mimic rule?
- This book now: yes.
- Evidence: §13; §17.6 only cites it.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Met. A mimic's heat-up cites §15.5 and so takes the new procedure and timing (see cross-cluster effects).
- Mechanical: no
- Edits: none

### boss-065 · ch. 17, dependency placed on §15 (facing, tiles, deck, weak arcs)
- Question: Does §15 state the starting facing, the two spawn nodes of the joined tiles, the allowance for special decks and heat-ups, and the weak-arc bonus?
- This book now: yes.
- Evidence: §15.2, §15.3, §15.5, §15.6.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Met; §15.5's closing sentence now also says that a special heat-up keeps the general timing unless its rule states another.
- Mechanical: no
- Edits: boss-E01

### boss-066 · ch. 17, dependency placed on §16 (deck renewal, arcs, area, Boss Death)
- Question: Does §16 allow renewal whenever a card is due, place a character when a boss enters their node, define the area of an area attack, and withhold rewards after the first Gargoyle?
- This book now: yes; renewal mid-turn is stated by the entries that need it (the Pursuer, and now the Guardian Dragon and Vordt), citing §15.5, Deck Renewal.
- Evidence: §16.1 to §16.5.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Met.
- Mechanical: no
- Edits: none

### boss-067 · ch. 17, dependency placed on §19 (campaign sections)
- Question: Do the campaign sections mark the Twin Gargoyles and hold the sections that §17 cites?
- This book now: the Gargoyle pairs cite §17.1; §19.1 has its optional Section Four with Kalameet; the Chariot's campaign is in §19.
- Evidence: `10_manuscript_chapter_19_campaigns.md` lines 19, 46–48, 102, 215, 362.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Met. The campaigns that include the Four Kings, the Gaping Dragon, Vordt, the Last Giant and Manus now reach bosses with full rules.
- Mechanical: no
- Edits: none

### boss-068 · ch. 17, dependency placed on Appendix B (replacement boss cards)
- Question: Does Appendix B list the replacement cards for the Black Knight, Gravelord Nito, Crossbreed Priscilla and the Heavy Knight?
- This book now: yes, by name; the card texts themselves are not in the book.
- Evidence: `10_manuscript_chapter_23_appendices.md`, Boss Data and Behaviour Cards.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Met as a list. Because the replacement cards were not supplied, the entries for the two Painted World bosses cannot restate their abilities (boss-009, boss-010).
- Mechanical: no
- Edits: none

### boss-069 · ch. 17, glossary entry Heat-up
- Question: Does the entry end with a proper reference and state the current rule?
- This book now: it ends "(see §17)" and states the remaining-deck shuffle.
- Evidence: `12_glossary.md`.
- Ruling: CHANGE (follows boss-018)
- Why: The reference was already fixed; the rule is brought into line with §15.5.
- Mechanical: yes
- Edits: boss-E31

### boss-070 · ch. 17, glossary entry Boss
- Question: Is "a single powerful enemy" still right?
- This book now: "A single powerful enemy …".
- Evidence: Ornstein & Smough and the Four Kings are each one boss with several models.
- Ruling: CHANGE
- Why: One clause removes the contradiction.
- Mechanical: no
- Edits: boss-E30

### boss-071 · ch. 17, glossary entry Calamity
- Question: Does the entry agree with §17.8?
- This book now: yes; calamity lasts the encounter (OQ-24).
- Evidence: Kalameet booklet removes the token when the character next suffers damage (`DS-BDK-Rules-web.txt` lines 452–460); Gate 1 OQ-24 kept the manuscript's version on purpose.
- Ruling: CONFIRM as written
- Why: Owned by §8.5 and settled at Gate 1; nothing in this cluster reopens it.
- Mechanical: no
- Edits: none

## (a) Every CHANGE and ADD (there is no DELETE)

| Item | Ruling | What changes | Mechanical | Edits |
|---|---|---|---|---|
| boss-001 | CHANGE | §17.10: seven placeholders replaced by full entries; one introductory sentence | yes | boss-E20 to boss-E28, boss-E44 |
| boss-002 | CHANGE | The Four Kings: four kings with their own dials, royal summons, the turn with no king in play | yes | boss-E20 |
| boss-003 | CHANGE | Gaping Dragon: six-card deck with two signature cards and a heat-up card, corrosion, Crawling Charge | yes | boss-E21, boss-E14, boss-E32 |
| boss-004 | CHANGE | Guardian Dragon: cage nodes, Fiery Breath deck, Inferno attack, Bonus Behaviour, two heat-up cards | yes | boss-E22, boss-E39, boss-E40 |
| boss-005 | CHANGE | The Last Giant: standard and Arm cards, heat-up swaps Arm cards for heat-up cards and adds Falling Slam, Wind Up | yes | boss-E23, boss-E33 |
| boss-006 | CHANGE | Manus: Overextended, shaft icon on attacks, heat-up that places two cards and does not shuffle | yes | boss-E24, boss-E34 |
| boss-007 | CHANGE | Old Iron King: Iron King nodes, lava, Beam deck and Beam attack, Old Iron Rage | yes | boss-E25, boss-E38, boss-E41, boss-E44 |
| boss-008 | CHANGE | Vordt: movement and attack decks, Icy Blows, two heat-ups, Frostbreath | yes | boss-E26 |
| boss-010 | CHANGE | Heavy Knight: delegation sentence replaced by "no rules beyond its data card" | no | boss-E28 |
| boss-012 | CHANGE | Ornstein & Smough: official structure (two models with their own health, both act, heat-up when the first falls); Gate 1 OQ-25 revised | yes | boss-E08, boss-E10, boss-E07, boss-E42, boss-E46, boss-E30 |
| boss-018 | CHANGE | Heat-up: deck and discard pile reshuffled together with the heat-up card, at the start of the boss's next turn | yes | boss-E01, boss-E02, boss-E04, boss-E05, boss-E31, boss-E48 |
| boss-044 | CHANGE | §2.3 follows boss-012 | yes | boss-E42 |
| boss-046 | CHANGE | §5.5: pillars placed for every boss encounter on that board | no | boss-E45 |
| boss-047 | CHANGE | §6.7 step 5 now finds rules for every mega-boss | yes | boss-E20 to boss-E26 |
| boss-050 | CHANGE | Ornstein & Smough inferences replaced (see boss-012) | yes | boss-E08, boss-E10 |
| boss-052 | CHANGE | Asylum Demon mini-boss fought on the mega-boss game board; ability named Pillars of Woe | yes | boss-E11, boss-E12, boss-E03, boss-E45, boss-E47, boss-E36 |
| boss-055 | CHANGE | Sif: at three health or less the deck is replaced by Limping Strike | yes | boss-E13 |
| boss-057 | ADD | Old Dragonslayer: one sentence, no heat-up point | no | boss-E15 |
| boss-059 | ADD | Aggro: damage to another enemy model in a boss encounter moves the token (Executioner's Chariot, first part) | yes | boss-E06, boss-E35 |
| boss-069 | CHANGE | Glossary, Heat-up follows boss-018 | yes | boss-E31 |
| boss-070 | CHANGE | Glossary, Boss: no longer "a single" enemy | no | boss-E30 |

boss-E27 (Crossbreed Priscilla) changes only the form of a kept placeholder and belongs to a CONFIRM (boss-009).

## (b) What could not be settled, and why

1. Crossbreed Priscilla's invisibility. Her printed ability (Snowblind) was found, but no source read states when she is invisible or how that ends. The Painted World set has no rulebook text for it in the 2022 rulebook supplied, the publisher's errata file for the 2022 sets sits behind a checkout page, and BoardGameGeek, Reddit and the Fextralife wiki could not be read. Her placeholder stays. The fastest fix is a look at her printed behaviour cards and boss encounter card, or at the replacement cards that Appendix B names.
2. The replacement data cards of Appendix B for Crossbreed Priscilla and the Heavy Knight were not supplied. The printed abilities found (Snowblind, Brutal Impact) are therefore reported in this memo and not written into §17.10, because the replacement cards govern.
3. Ornstein & Smough: the cards were read in a community transcription, not from the printed cards. Four points in boss-012 are designer's calls to be checked against the cards: Ornstein acts first; Ornstein on the main-boss spawn node and Smough on the mini-boss spawn node; the health gain (10 and 15) stops at the starting health; five heat-up cards each.
4. Great Grey Wolf Sif: the threshold of three health comes from the same transcription.
5. Vordt's Icy Blows: "blocks or resists 4 or more damage" is read as four or more damage prevented. The other reading (a defence total of four or more) differs only when the attack value is below four. Frostbreath after a blow that crosses both heat-up points is ruled as resolved once.
6. Old Iron King: the booklet says models "can never move into the Old Iron King's back arc". The entry forbids the back arc of his base and treats the lava as a wall; whether a printed node beside him lies on the line of his back arc could not be judged from the Beam card diagram, and such a node, being printed, is treated as open.
7. Guardian Dragon and Old Iron King node cards were read from two page images; the targeted nodes of each individual card were not, and do not need to be, written into the book.

## (c) Cross-cluster effects for the lead editor

- Gate 1: OQ-25 is revised for Ornstein & Smough (not for the Twin Gargoyles). `05_gate1_decisions.md` and `11_change_log.md` need the note; the brief's summary line "Ornstein & Smough one boss, shared dial and deck" no longer holds.
- §2.3, first paragraph: "Each boss has a model, a health dial, a data card" is no longer true of Ornstein & Smough (two of each) or the Four Kings (four models and dials); the components owner may add "or more than one". §2.9 still says "the behaviour cards listed on the data card"; a data card lists a deck size, not cards.
- §6.5 (setup) and §18.1 (campaign play, "A mini-boss is fought on the mini-boss tile"): when the Asylum Demon is the mini-boss its expansion's game board takes the place of the mini-boss tile (boss-052). §17.3 and §15.3 now say so; §6.5 step 3 and §18.1 want a pointer, and §6.5's two-by-three grid does not fit the larger board, so the setup owner may wish to say that the board is placed at the end of the route.
- §12.2 (invader heat-up) and §13 (mimic heat-up) cite §15.5 and so take the new procedure and timing: the unused card is shuffled with the deck and the discard pile at the start of the model's next turn. Their sentences still read correctly; the owners may add "and its discard pile" for clarity.
- §8.5 and the glossary entry Condition: Vordt's Icy Blows places a frostbite token without an attack icon. The Frostbite text may add "or by Vordt's Icy Blows (see §17.10)" as Stagger lists its other sources. §8.5, Corrosion may cite "(see §17.10, Gaping Dragon)".
- §10.3, Shaft: the icon now also appears on Manus's behaviour cards; the glossary is amended here (boss-E34) and §10.3 needs no change.
- §9 (combat owner): Raise Skeleton stays in §17.9 (boss-060); a one-line pointer from §9 is optional.
- §20.1: "follows the rewards for the boss's defeat" has nothing to follow after the final boss (boss-038). One PvP encounter follows Ornstein & Smough and one follows the Four Kings, since each is one boss.
- §19: no change needed. Call of the Abyss, Into the Depths, Big Game Hunting and the Vordt campaign now reach bosses with full rules. The Vordt booklet names particular Level 4 cards for its campaign sections (campaign owner).
- F.A.Q. §22.5: the Ornstein & Smough answer is rewritten (boss-E46) and one question on the heat-up shuffle is added (boss-E48).
- Chapter 15 introduction: "A boss is a single model" is flavour and now loose; a neutral phrase would be safer.
- Layout: §17.10 grows by roughly 3,400 words and nine sub-headings. The new icons (crawl, corrosion, Inferno, Bonus Behaviour, Beam) are named in words because no extracted asset exists; if assets are cut from the newly supplied booklets, tokens can follow the first mention of each.
- Italics: the new §17.10 entries italicise each glossary term at its first use in the section, counted from the Four Kings entry downward; if the lead editor applies only some entries, the first-use italics need a pass.
- Tools: the style checker reports no violation on copies of the seven files with all 40 edits applied. It flags the printed ability name of Smough's data card ("Divided You Fall") as second person, so §17.2 does not print the two ability names.
