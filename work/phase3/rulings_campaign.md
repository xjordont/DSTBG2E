# Rulings memo — cluster `campaign`

Scope: lead items 1, 11 and 18; every item in the issue lists for chapters 02, 18 and 19; the chapters themselves and the glossary terms they define. Edits are in `work/phase3/edits_campaign.json` (48 entries, each `old` checked to occur exactly once in its file; E45 to E48 belong to the follow-up section at the end).

## Sources used

Supplied texts are cited by file and line region in `work/text/`. The web was available. The official booklets for the unsupplied mega-boss expansions were found and read in full for their contents pages and campaign pages:

| Booklet | Where found |
|---|---|
| Asylum Demon (campaign Demon Hunting) | third-party mirror of the publisher's PDF, `https://kubix.com.ua/upload/iblock/9ac/t260eqag3859nc6xmgzu56jpf72r0z6e.pdf` |
| Gaping Dragon (Into the Depths) | mirror, `https://kubix.com.ua/upload/iblock/fe8/f29pb8cuh05inxz4uzv57xbt79d1gb60.pdf` |
| The Four Kings (Call of the Abyss) | publisher, `https://steamforged.com/cdn/shop/files/DS-Four-Kings-Rules-web.pdf` |
| Manus, Father of the Abyss (Big Game Hunting) | publisher, `https://steamforged.com/cdn/shop/files/DS-MFA-Rules.pdf` |
| The Last Giant | publisher, `https://steamforged.com/cdn/shop/files/DS-TLG-Rules.pdf` |
| Guardian Dragon | publisher, `https://steamforged.com/cdn/shop/files/DS-GD-Rules-web.pdf` |
| Old Iron King | publisher, `https://steamforged.com/cdn/shop/files/DS-OIK-Rules-web.pdf` |
| Vordt of the Boreal Valley | publisher, `https://steamforged.com/cdn/shop/files/DS-VotBV-Rules-web.pdf` |
| The Sunless City rulebook (2023) | publisher, `https://steamforged.com/cdn/shop/files/DS-TSC-Rulebook-download-min.pdf` |

Text extractions of all nine are in `/tmp/claude-0/-home-user-DSTBG2E/ff710c3a-8948-5673-b38b-8c94b4dc4aee/scratchpad/campaign_dl/` (`a1.txt` Asylum Demon, `a2.txt` Gaping Dragon, the others under their PDF names). Other web sources: the publisher's production updates (`https://darksouls.backerkit.com/hosted_preorders/project_updates?page=7`, `?page=8`, `?page=9`), which repeat the contents lists; the community "Unofficial Guide and Rules FAQ" (`https://docs.google.com/document/d/1DmbTaM68OoosZcSCFW0bTNgBWCaHSP2UE9Um-X4XF54`); a house-rules round-up (`https://gamerant.com/dark-souls-board-game-house-rules/`); retailer and publisher listings for the Painted World of Ariamis. Not obtained: the Painted World of Ariamis rulebook (no copy found), BoardGameGeek pages (searches returned none), one Scribd copy (refused).

---

## Lead items

### campaign-001 · Lead 1: campaign rewards against doubled costs
- Question: Should campaign play keep the standard soul rewards (3/4/5/6) with doubled stat tier costs, or also cut rewards by one as the source manuscript did?
- This book now: standard rewards, reduced 1/2/2/3, and stat tier costs of 4/8/16/20 (§18.5, §18.6; Gate 1 OQ-21).
- Evidence: source manuscript: rewards 2/3/4/5 and costs 4/8/16/20 (`work/phase2a/source/18_campaign_play.md`). Official 2017: campaign keeps the standard reward and doubles the costs to 4/8/16, with tier four at 20 (DS-Core-Rules-lores.txt 1624-1641); a card costs two souls in place of one. Official 2022: no separate campaign mode; costs 2/4/8 (DS-TG 1929-1933). Extended: doubles soul rewards in every game "to greatly reduce play time" (DS-Extended-Rules-V45.txt 21-24). Hollowed: level + 1 souls per character, costs 2/4/6/8 (Hollowed_Edition_v1.3.txt 9-12, 237). Online: the most popular house rule is "Double Souls / Half Sparks", adopted to cut grinding (gamerant round-up).
- Ruling: CONFIRM as written.
- Why: One lever is enough, and it is the official one. Souls per character from first clears, with one repeat of each section's encounters in brackets:

| Game | Rewards 3/4/5/6 | Rewards 2/3/4/5 |
|---|---|---|
| Standard game (two legs) | 44 (+14) | - |
| The First Journey | 65 (+20) | 50 (+15) |
| The Coiled Sword | 77 (+25) | 59 (+19) |
| Facing the Abyss | 67 (+23) | 52 (+19) |
| Demon Hunting | 98 (+26) | 76 (+20) |
| Call of the Abyss, five sections | 107 (+25) | 85 (+20) |
| Into the Depths | 98 (+22) | 78 (+16) |

  One stat to tier three costs 14 souls in the standard game and 28 in a campaign; all four cost 56 and 112. After about 25 souls of other campaign spending (six shop cards, a share of the bonfire ascetic, one transposition), a three-section campaign under the book's rule leaves 60 to 77 souls for stats: two stats at tier three and a step or two elsewhere when the party meets the last boss, and all four at tier three only at the end of a five-section campaign. That is the "more gradual progression" the doubled costs exist for. With the manuscript's second lever the same party has 40 to 53 souls: one stat at tier three and one at tier two against a main-boss, which pushes players back into repeating encounters for one or two souls each, the complaint the community rules were written to cure. With no doubling at all a character reaches tier three in every stat by the end of Section Two and has no choices left to make.
- Mechanical: no
- Edits: none

### campaign-002 · Lead 11: joining or leaving a standard game
- Question: May a player join or leave a standard game under the campaign rule?
- This book now: yes, "under the same rules" (§18.4; F.A.Q. §22.1).
- Evidence: official 2017 gives the rule for campaigns only (DS-Core-Rules-lores.txt 1612-1623); official 2022, Extended, Hollowed, online: silent.
- Ruling: CONFIRM as written, with one clarifying clause.
- Why: A player would guess that the rule for a campaign serves any game, and one rule for both is cheaper than a prohibition. The two steps that set the campaign maximum of the spark dial have nothing to act on in a standard game, and the text should say so.
- Mechanical: no
- Edits: campaign-E29

### campaign-003 · Lead 18: unverified counts and four campaigns
- Question: Do the component counts for unsupplied sets and the four campaigns from unsupplied booklets match the published game?
- This book now: kept as the manuscript gives them (§2, §19).
- Evidence: the official booklets listed under Sources.
- Ruling: CHANGE. The counts are settled in campaign-006 to campaign-008 and the campaigns in campaign-031, campaign-033 and campaign-034. In short: three of the four campaigns contain errors (a missing section, a missing bonfire tile with an invented rest rule, a wrong section name, a named encounter at the wrong level, a missing soul grant); three totals are wrong (boss treasure 63, encounter cards 31 per level, condition tokens seven each).
- Why: Each correction replaces an unverifiable figure or list with the published one.
- Mechanical: yes (through the campaign corrections)
- Edits: those of campaign-006, -007, -008, -031, -033, -034

---

## Chapter 02 — game components

### campaign-004 · Ch. 02: style checker false positives
- Question: Should "Armorer Dennis" and "Plow Scarecrow" be flagged as Americanisms?
- This book now: prints both as on the cards (§2.2, §2.4).
- Evidence: Gate 1 OQ-17 (printed spellings for names on cards); Phantoms and Darkroot booklets print both.
- Ruling: NOT A RULES QUESTION. The checker needs a whitelist of printed names.
- Why: Nothing in the rules changes.
- Mechanical: no
- Edits: none

### campaign-005 · Ch. 02: hollow cubes have no source
- Question: Which set supplies the eight hollow cubes?
- This book now: "8x Hollow cubes", no set named, of a colour distinct from the other cubes (§2.8, §7.2).
- Evidence: official 2017 contents: red, black and white cubes only (DS-Core-Rules-lores.txt 238-264); official 2022: the same (DS-TG 258-264); Extended: asks for "cubes of a different color than what is available in the core set" for its own extra cubes; Hollowed: marks hollowing with two spare black cubes at the right of the bar (Hollowed_Edition_v1.3.txt 284-300); online: silent.
- Ruling: CHANGE (clarification).
- Why: No set contains them, and a components list that names a set for everything else must say so. A distinct colour reads better at the table than a black cube standing beyond the red ones, so the term and the colour rule stay and the list states that the players provide them.
- Mechanical: no
- Edits: campaign-E01, campaign-E02

### campaign-006 · Ch. 02: condition tokens, seven or five
- Question: How many bleed, poison, frostbite and stagger tokens are supplied?
- This book now: seven of each, "Core and expansions", 36 in all (§2.8).
- Evidence: official 2017: five of each (DS-Core-Rules-lores.txt 252-261); no booklet, supplied or downloaded, adds any of the four; Kalameet four calamity (DS-BDK 82); Gaping Dragon four corrosion (booklet contents); official 2022: 21 condition tokens per core set, kinds not listed (DS-TG 264).
- Ruling: CHANGE. Five of each from the core set, 28 in all, and the supply is not a limit.
- Why: Seven cannot be found in any box. Poison stacks without limit, so five tokens can run out; the sentence the book already uses for soul tokens closes that.
- Mechanical: no
- Edits: campaign-E03, campaign-E04

### campaign-007 · Ch. 02: counts for unsupplied sets
- Question: Are the counts for the nine unsupplied sets right?
- This book now: kept from the manuscript; a generic mega-boss set extrapolated from two booklets (§2.2, §2.9).
- Evidence (official booklets, contents pages): every mega-boss expansion has one game board, four Level 4 cards and two mega-boss treasure cards. Asylum Demon: one model, two data cards, 9 + 13 behaviour cards, 2 + 2 treasure cards, four pillar tokens. The Four Kings: four models, four health dials, four identifier tokens, 20 behaviour cards. Gaping Dragon: four corrosion tokens, 14 behaviour cards. Guardian Dragon: four Fiery Breath cards, 11 behaviour cards. Old Iron King: six Fire Beam cards, 12 behaviour cards. Vordt: 17 behaviour cards, nothing else. The Last Giant: 16 behaviour cards, nothing else. Manus: 14 behaviour cards, nothing else. Painted World of Ariamis: 18 miniatures, that is three characters, 13 enemies and two bosses (publisher and retailer listings); the community guide lists "5x Phalanx Hollows" and a Phalanx with no model of its own.
- Ruling: CHANGE. The generic set is confirmed; four expansion-specific lines are added; The Four Kings' four models and dials are noted; the Phalanx entry is corrected.
- Why: The extrapolation was right, and the booklets add four components that the list lacked. The book's five Phalanx and one Phalanx Hollow make 14 enemy models in a box that holds 13.
- Mechanical: no
- Edits: campaign-E05, campaign-E06, campaign-E07, campaign-E08

### campaign-008 · Ch. 02: expansion totals 45/120/63 and 31
- Question: Can the expansion totals be reconciled?
- This book now: starting equipment 45, class-specific 120, common 145, legendary 20, boss treasure 63, 534 in all; 31 encounter cards per level, 169 in all (§2.5, §2.6).
- Evidence, per set:

| Set | Starting | Class-specific | Common | Legendary | Boss | Source |
|---|---|---|---|---|---|---|
| Characters | 23 | 60 | 10 | 10 | 0 | DS-Characters 64-67, 113-115 |
| Darkroot | 0 | 0 | 15 | 0 | 6 | DS-Darkroot 72-85, 141-145 |
| Explorers | 0 | 0 | 15 | 0 | 5 | DS-Explorers 72-95 |
| Iron Keep | 0 | 0 | 15 | 0 | 5 | DS-IronKeep 58-73 |
| ToG | 12 | 30 | 45 | 5 | 5 | DS-TG contents pages |
| PWA | 10 | 30 | 45 | 5 | 5 | by subtraction; community guide gives 95 item cards |
| Asylum Demon | 0 | 0 | 0 | 0 | 4 | booklet |
| Nine other mega-boss expansions | 0 | 0 | 0 | 0 | 18 | booklets, two each |
| Total | 45 | 120 | 145 | 20 | 48 | |

  Encounter cards of each of Levels 1 to 3: Darkroot six, Iron Keep six, Explorers five (booklets), Executioner's Chariot two (ten cards, four of them Level 4), ToG nine and PWA nine (27 each, 9/9/9, in the community guide; the ToG rulebook lists 29 cards, two of which are its boss encounter cards). That is 37. Level 4: ten expansions at four each, 40.
- Ruling: CHANGE. Boss treasure 48 and the total 519, with the invader treasure and Titanite Scale cards named as counted separately; encounter cards 37 per level and 187 in all, with the per-set figures stated.
- Why: Four of the five treasure totals are right. The fifth, 63, is 48 plus the 12 invader treasure cards and the three Titanite Scale cards, which the book lists elsewhere; that also explains 534 (519 + 15). Thirty-one matches no combination of sets. Where a total leans on one set that could not be checked at first hand (PWA), stating the per-set figures beside it lets an owner check it; that is how the encounter total is now worded.
- Mechanical: no
- Edits: campaign-E09, campaign-E10, campaign-E11

### campaign-009 · Ch. 02: Ornstein's printed name
- Question: Is it "Dragonslayer Ornstein" or "Dragon Slayer Ornstein"?
- This book now: one word (§2.3, §17.2, §17.5).
- Evidence: official 2017 prints "Dragon Slayer Ornstein" three times (DS-Core-Rules-lores.txt 170, 177, 1662-1663); the 2023 Sunless City rulebook prints the same; "Old Dragonslayer" is one word in the Explorers booklet.
- Ruling: CHANGE to "Dragon Slayer Ornstein" in the four places. "Old Dragonslayer" is unchanged.
- Why: Gate 1 OQ-17 fixes printed spellings for names. Consistency with §17 was the only reason for the one-word form, and §17 changes with it.
- Mechanical: no
- Edits: campaign-E12, campaign-E13, campaign-E14, campaign-E15

### campaign-010 · Ch. 02: cross-chapter dependencies
- Question: Does §2.4 agree with §12, §2.9 with §17.9, and §2.9 with §6.7?
- This book now: §2.4 gives standard summons before a mini-boss and advanced before a main-boss or mega-boss, standard invaders before the mini-boss's defeat and advanced after.
- Evidence: §12.1 and §12.2 say the same (chapter 12, lines 13, 20, 80, 99); §17.9 defines the setup card; §6.7 step 5 owns the Level 4 reward.
- Ruling: CONFIRM as written.
- Why: The three pairs agree as integrated. The campaign form of the Level 4 reward is settled in campaign-021.
- Mechanical: no
- Edits: none

### campaign-011 · Ch. 02: glossary entries against Gate 1
- Question: Do Mega-boss, Endurance bar, Poison and Stagger still contradict Gate 1?
- This book now: Mega-boss "follow the usual rules"; Endurance bar "10 spaces"; Poison "removes all of its poison tokens"; Stagger "next complete turn" (`12_glossary.md` lines 185, 117, 219, 279).
- Evidence: Gate 1 OQ-14, OQ-08, OQ-13, OQ-16.
- Ruling: NOT A RULES QUESTION. All four were corrected at integration.
- Why: Nothing remains to decide.
- Mechanical: no
- Edits: none

### campaign-012 · Ch. 02: boss treasure cards per boss
- Question: Is "two or more" right, and what is the total?
- This book now: "two or more boss treasure cards" (§2.3, §2.5); totals 18 and 63.
- Evidence: official 2017 "between two and four" for the core bosses (DS-Core-Rules-lores.txt 168-171); booklets: Sif 3, Artorias 3, Pursuer 3, Old Dragonslayer 2, Sir Alonne 2, Smelter Demon 3, Asylum Demon 2, every mega-boss 2; ToG five between two bosses.
- Ruling: CONFIRM "two or more". The total is corrected under campaign-008.
- Why: Every boss checked has two or three cards, so the phrase holds and needs no upper limit.
- Mechanical: no
- Edits: none (see campaign-008)

---

## Chapter 18 — campaign play

### campaign-013 · Ch. 18: campaign soul reward table
- Question: Is the campaign full reward 3/4/5/6 or the manuscript's 2/3/4/5?
- This book now: 3/4/5/6, reduced 1/2/2/3 (§18.5).
- Evidence: as campaign-001.
- Ruling: CONFIRM as written. Gate 1 OQ-21 stands; no revision of Gate 1 is proposed.
- Why: As campaign-001. One reward table for the whole book is also one table fewer to learn.
- Mechanical: no
- Edits: none

### campaign-014 · Ch. 18: bonfire ascetic fee
- Question: Is the fee 16 souls from the party at any rest, or eight per character after the first section (B-034)?
- This book now: 16 souls in all, once, at any rest, from any combination of characters; scaled enemies gain two health for the rest of the campaign (§18.7).
- Evidence: source manuscript: "a communal one time fee ... sixteen souls ... from any combination of character contributions". Official 2017 and 2022: no such mechanic; the official campaigns open the better treasure free after Section 1. Extended and Hollowed: split the treasure deck by stage, with no fee. Online: silent.
- Ruling: CONFIRM as written. B-034 is not adopted.
- Why: The real price of the ascetic is the health increase, which a party that burns it too early pays in every fight; that makes a gate by section unnecessary. A pooled fee keeps a small decision (who gives up a stat tier) that a fixed share per character would remove. The health increase, and the exemptions, are confirmed in campaign-027.
- Mechanical: no
- Edits: none

### campaign-015 · Ch. 18: spark buy-back
- Question: Is one spark per rest the limit, and does a character who cannot pay block the purchase?
- This book now: one spark per rest; every character pays four souls of their own; any character short of four blocks it (§18.3).
- Evidence: official 2017: "2 souls per character in the group", paid from the shared soul cache, up to the starting number (DS-Core-Rules-lores.txt 1601-1606); source manuscript: sparks cannot be bought; Gate 1 OQ-22: "bought back for 4 souls per character"; official 2022, Extended, Hollowed: no purchase. Online: the round-up notes that a purchasable spark can pay for itself by repeating encounters.
- Ruling: CHANGE. The cost stays at four souls for each character, but the party pays it together, as it pays for the bonfire ascetic. One spark per rest, not at the maximum, and allowed during a free rest are confirmed.
- Why: The book had two party purchases with two payment rules. One rule now covers both: a cost charged to the party is paid by any combination of the characters; every other cost is personal. It follows the official shared payment and ends the case in which one character who has just levelled up locks the whole party out. The limit of one per rest keeps the buy-back from paying for itself except in the longest sections, where the return is about six souls a character for an hour's play.
- Mechanical: yes
- Edits: campaign-E18, campaign-E19, campaign-E20, campaign-E21, campaign-E22, campaign-E23

### campaign-016 · Ch. 18: spark dial range
- Question: Can the dial show a lone character's maximum of six?
- This book now: maximum is the starting value plus one, so six for one character (§18.3).
- Evidence: official 2017 and 2022 never set the dial above five (DS-Core-Rules-lores.txt 323-329; DS-TG 1127-1133); Hollowed: "the amount of sparks cannot go above 5" (217-219); Extended, online: silent.
- Ruling: CHANGE. The maximum is the starting value plus one and never more than five.
- Why: A rule that needs a number the component cannot show is a fault. The cap costs a lone character nothing in practice, since the dial is below five after the first rest.
- Mechanical: yes (a lone character only)
- Edits: campaign-E24, campaign-E25, campaign-E26, campaign-E27

### campaign-017 · Ch. 18: PvP encounters in campaign play
- Question: Are PvP encounters played in a campaign, and what follows one after a boss that does not end its section?
- This book now: optional, after each boss; after a boss that does not complete its section the participants are restored and the dead return (§18.1).
- Evidence: all sources silent on campaigns; §20.7: death in a PvP encounter has no cost.
- Ruling: CONFIRM as written.
- Why: The rule only carries §20 into the one case §20 cannot reach, and restoring the participants is what "no cost" requires where no rest follows.
- Mechanical: no
- Edits: none

### campaign-018 · Ch. 18: bosses that do not end a section
- Question: What does a boss grant when its section is not yet completed?
- This book now: its rewards and a spark; no free rest, no restock, no setup (§18.1, §18.3, §18.6); §16.5 defers to §18.
- Evidence: source manuscript: a spark for every boss, a free rest only after the section's final boss; official 2017: no spark and no reset "until the final boss in an area has been defeated" (1602-1606); official campaigns: one published campaign outside this book (Demons and Dragons) has two bosses in a section.
- Ruling: CONFIRM as written.
- Why: This is the author's rule, it is complete, and a spark without a free rest is a fair half-reward. It costs three sentences and is needed for the players' own campaigns.
- Mechanical: no
- Edits: none

### campaign-019 · Ch. 18: a section completed without a boss
- Question: Does clearing the last encounter of such a section grant a spark?
- This book now: a free rest and a restock, no spark (§18.1, §18.3).
- Evidence: official 2017: a spark "each time a mini boss, main boss, or mega boss is defeated" (1597-1599); the booklets say only "The party proceeds to Section 2 when the encounter is defeated" (DS-Darkroot 244-246; DS-IronKeep 200-204).
- Ruling: CONFIRM as written.
- Why: "A spark for a boss" is the rule a player expects, and the free rest already rewards the section.
- Mechanical: no
- Edits: none

### campaign-020 · Ch. 18: section setup details
- Question: Are the inferred setup details sound, and which sets build the encounter decks when a campaign names none?
- This book now: tiles drawn at random from all encounter tiles, either side up; decks "built from the sets the campaign names"; used cards return to the box (§18.1). §19.6, §19.7, §19.8, §19.10, §19.11 and §19.12 name no sets.
- Evidence: official booklets: Call of the Abyss and Into the Depths, "a shared deck of encounters from the core game and the Darkroot expansion"; Go Beyond Death, a shared deck of the core game, Explorers and Iron Keep; The Undead Colosseum, a shared deck (DS-EC 615-623).
- Ruling: CHANGE. Default: the decks are built from every set the campaign requires, shuffled together by level; a campaign that names its sets uses only those. The other details are confirmed.
- Why: One default in §18.1 fills six gaps and matches the published campaigns, where six separate sentences in §19 would say the same thing six times.
- Mechanical: yes (it settles what was undefined)
- Edits: campaign-E30

### campaign-021 · Ch. 18: Level 4 encounters in sections
- Question: Which board and cards does a Level 4 encounter use, how are two fought, what does each award, and is a cleared one crossed free?
- This book now: the board and cards of the section's mega-boss, or of a mega-boss expansion the campaign requires; two are fought in turn on one board; each awards one mega-boss treasure card as in §6.7; a cleared one is not fought again and costs no stamina (§18.1, §18.5).
- Evidence: official booklets: two treasure cards per mega-boss; Call of the Abyss (corrected) and Into the Depths each list three Level 4 encounters before one mega-boss; Level 4 cards "function the same way" as other encounter cards and are drawn from the mega-boss's four (DS-EC 205-262); "the level 4 encounter will not reset" (every booklet); source manuscript: "Boss treasure is only obtained by defeating bosses".
- Ruling: CHANGE the reward: in campaign play a Level 4 encounter is rewarded as any other encounter of its section (Level 4 souls and one current-tier treasure card per character), and mega-boss treasure comes only from the mega-boss. The board, the two-in-turn rule and the free crossing are confirmed.
- Why: Three awards cannot be paid from two cards, so the standard reward breaks in two of the twelve campaigns. The fix deletes a special case, and it removes a contradiction inside §18.5, which says in one sentence that boss treasure comes only from bosses and in the next that a Level 4 encounter awards some. It holds whatever is decided for the standard game under lead item 19.
- Mechanical: yes
- Edits: campaign-E16, campaign-E17

### campaign-022 · Ch. 18: victory
- Question: When is a campaign won?
- This book now: when the last boss of the last section is defeated, or when the last encounter is cleared if the last section has no boss; campaigns may state their own condition (§18.1).
- Evidence: official 2017: "the campaign ends when the party runs out of sparks or the final boss of the scenario is defeated" (1612-1614); Big Game Hunting: sections 2a to 2c in any order.
- Ruling: CONFIRM as written. Big Game Hunting keeps its own statement (§19.12); Demon Hunting needs none once its bonfire tile is restored (campaign-034).
- Why: The general rule and the one exception cover all twelve campaigns.
- Mechanical: no
- Edits: none

### campaign-023 · Ch. 18: adding and dropping players
- Question: Are the join threshold and the unsourced details right?
- This book now: join or leave on the bonfire tile between encounters; joining costs one spark and needs two on the dial; the newcomer has starting equipment, base stats and no souls; treasure on uncleared tiles is topped up or reduced; the leaver's cards pass to the party, which gains a spark; four characters at most (§18.4).
- Evidence: official 2017: "at the cost of 1 spark each ... starting character stats and equipment ... If a player character leaves the party, the party gains 1 spark, the character's equipment is added to the inventory" (1615-1623); source manuscript: the same; A-105 proposed a threshold of one.
- Ruling: CHANGE the threshold to one spark ("cannot join while the dial shows zero"). Everything else is confirmed, including no souls for the newcomer and no grant of six souls when a party is reduced to one character (that grant belongs to setup, §6.1).
- Why: A cost of one spark needs one spark; a second condition is a rule nobody would guess, and a party may already rest itself down to zero. The treasure adjustment is one deal per tile and keeps "one card per character" true. A catch-up grant for a late joiner was considered and not added: the official rule gives none, and the party can pass on its spare cards.
- Mechanical: yes (threshold only)
- Edits: campaign-E28 (and campaign-E29 under campaign-002)

### campaign-024 · Ch. 18: a sold legendary card
- Question: Where does a sold legendary treasure card go?
- This book now: it sells for four souls and goes to the bottom of the legendary treasure deck (§18.6).
- Evidence: source manuscript: sell value four; standard rule: a sold card goes to the bottom of its deck, and boss treasure, which has no deck, to the box (§11.4); A-077 proposed the box.
- Ruling: CONFIRM as written.
- Why: It is the general rule applied to the one deck that exists only in campaign play. No loop arises, because every transposition consumes a boss treasure card.
- Mechanical: no
- Edits: none

### campaign-025 · Ch. 18: when transposition opens
- Question: When does transposition become available, and does any rest qualify?
- This book now: after the last boss of the first section, or after the section is completed if it ends in an encounter; any rest, free or paid (§18.8).
- Evidence: source manuscript: after the final boss of the first section, and only at a rest paid for with a spark; A-051 (approved) removed the paid-rest condition; official campaigns add the legendary cards "after completing Section 1".
- Ruling: CHANGE the wording only: "once the first section of the campaign is completed". Any rest qualifies, as written.
- Why: Section completion already means both cases, so one sentence replaces two and matches the F.A.Q. The rest of §18.8 was reviewed and is sound: a fixed fee, five cards to choose from, and one legendary card for each boss at most. The campaign sale value of four souls for boss treasure (six in the standard game) is a small inconsistency of the author's own table; it is harmless and is left alone.
- Mechanical: no
- Edits: campaign-E31, campaign-E32

### campaign-026 · Ch. 18: invaders in campaign play
- Question: Are standard or advanced invader tokens drawn in a section?
- This book now: one invasion per section; the kind of token is not stated, and §12.2 keys it to the mini-boss's defeat (§18.1).
- Evidence: official Phantoms rules: standard before the mini-boss, advanced after; official campaigns treat "after Section 1" as the standard game's "after the mini boss"; in this book the bonfire ascetic takes that place for treasure and the shop (§18.5 to §18.7).
- Ruling: ADD. Standard invader tokens until the bonfire ascetic is burnt, advanced from then on.
- Why: The hole is real: "before the mini-boss is defeated" has no meaning in a campaign with no mini-boss or with three. The ascetic is already the campaign's line between the early game and the late game, so one event now moves treasure, shop and invaders together, and "stronger enemies" gains a second, visible sense.
- Mechanical: yes
- Edits: campaign-E33

### campaign-027 · Ch. 18: what the bonfire ascetic does not affect
- Question: Which models are exempt, and is a marker needed?
- This book now: every enemy subject to enemy scaling gains two health; a boss, a mimic, a phantom and a crystal lizard are unaffected (§18.7).
- Evidence: source manuscript: exempted invaders and bosses, and raised attack; Gate 1 OQ-07: health, not attack; §8.3: the same four models are never scaled.
- Ruling: CONFIRM as written. No marker is needed.
- Why: "What is not scaled is not affected" is one test in place of two lists. The stocked tier two shop shows that the ascetic has been burnt.
- Mechanical: no
- Edits: none

### campaign-028 · Ch. 18: glossary entry Fog gate
- Question: Should the glossary say "aesthetic only"?
- This book now: glossary, "In campaign play it is aesthetic only"; §18.2, the token marks the doorway, is not moved, gives no shortcut, and is where a summon is called.
- Evidence: source manuscript: "purely aesthetic"; §18.2.
- Ruling: CHANGE the glossary line to match §18.2.
- Why: The token still does two jobs in a campaign, so "aesthetic only" is wrong on its face.
- Mechanical: no
- Edits: campaign-E34

### campaign-029 · Ch. 18: campaign heading titles (C-103)
- Question: Should "Sparks", "Setup" and the other headings be qualified?
- This book now: unqualified; cross-references carry section numbers.
- Evidence: the section map in the drafting brief.
- Ruling: NOT A RULES QUESTION. No change.
- Why: The numbers already make every reference unambiguous.
- Mechanical: no
- Edits: none

### campaign-030 · Ch. 18: the dead after a boss inside a section
- Question: Are characters who died in such a boss encounter revived hollow?
- This book now: revived as after a cleared encounter, without hollow cubes, because the boss's defeat embers every character (§18.1).
- Evidence: §16.5 steps 4 and 5; §7.3 (embering removes hollow).
- Ruling: CONFIRM as written.
- Why: It follows from two standard rules and adds nothing new.
- Mechanical: no
- Edits: none

---

## Chapter 19 — campaigns

### campaign-031 · Ch. 19: the four unverified campaigns
- Question: Do Demon Hunting, Call of the Abyss, Into the Depths and Big Game Hunting match their booklets?
- This book now: kept as the manuscript gives them (§19.6, §19.7, §19.10, §19.12).
- Evidence: the four official booklets, campaign pages (see Sources). Every section and level was compared:

| Campaign | Section | Official | This book | Result |
|---|---|---|---|---|
| Demon Hunting | 1 Undead Asylum | Bonfire, L1, L1, Asylum Demon | no bonfire tile; special rest rule | differs (campaign-034) |
| | 2 Undead Burg | Bonfire, L1, L1, L2, Gargoyle twice | same | matches |
| | 3 Sen's Fortress | Bonfire, L1, L1, L2, L2, Titanite Demon | same | matches |
| | 4 Northern Undead Asylum | Bonfire, L2, L3, L4, Stray Demon | named "Sen's Fortress" | name differs (campaign-034) |
| | 5 Anor Londo | Bonfire, L2, L2, L3, L3, L3, Ornstein & Smough | same | matches |
| Call of the Abyss | 1 Undead Parish | Bonfire, L1, L1, L2, L2, Titanite Demon | same | matches |
| | 2 Darkroot Basin | Bonfire, L1, L2, L2, L3, Sif | same | matches (campaign-033) |
| | 3 Royal Wood | Bonfire, L2, L3, L3, L3, Artorias | same | matches |
| | 4 Penultimate Trial | Bonfire, L3, L3, L4, Ornstein & Smough | absent | missing (campaign-033) |
| | 5 The Abyss | Bonfire, L4, L4, The Four Kings | listed as Section Four | renumbered |
| Into the Depths | 1 Broken Path | Bonfire, L1, L1, L2, L2, Winged Knight | same | matches |
| | 2 Shattered Spire | Bonfire, L2, L2, L2, Titanite Demon | same | matches |
| | 3 Crypt of the Fallen | Bonfire, L2, L3, L3, Artorias | same | matches |
| | 4 Warriors' Revenge | Bonfire, L3, L3, Outskirts of Blighttown (L4), Ornstein & Smough | Outskirts of Blighttown shown as the second Level 3 encounter, with a separate unnamed Level 4 | differs |
| | 5 The Depths | Bonfire, Darkened Chamber (L4), The Depths (L4), Gaping Dragon | same | matches |
| Big Game Hunting | 1 Asylum Hunt | Bonfire, L1, L1, L2, L2, Asylum Demon | same | matches |
| | 2a Forest Hunt | Bonfire, L4, The Last Giant | same | matches |
| | 2b Bridge Hunt | Bonfire, L4, Stray Demon | same | matches |
| | 2c Chasm Hunt | Bonfire, L4, Manus | same | matches |

  Campaign rules in the booklets that the book lacks: Into the Depths may be played without Darkroot, with the Dancer in place of Artorias; Big Game Hunting grants every character 16 souls when Section 1 is defeated, fights every boss on a mega-boss game board, and allows other mega-bosses to be added or substituted.
- Ruling: CHANGE. Into the Depths: Outskirts of Blighttown becomes the Level 4 encounter of Section Four, and the play-without-Darkroot option is added. Big Game Hunting: the 16 souls, the board for the Asylum Demon, the moment each free-order section is set up, and the substitution option are added. Demon Hunting and Call of the Abyss are corrected under campaign-034 and campaign-033.
- Why: These are published lists; where the manuscript differs from them it is a copying error, and the booklets are the only authority. The 16 souls matter: without them a party meets a mega-boss with the income of one short section.
- Mechanical: yes
- Edits: campaign-E39, campaign-E40, campaign-E41

### campaign-032 · Ch. 19: The Gauntlet's invader rule
- Question: Does a listed invader appear once, as in Ambush Lies Ahead, or every time until beaten?
- This book now: once only, the same paragraph as §19.3 (§19.4).
- Evidence: official Phantoms: "Unlike the standard invader rules or other campaign encounters, when an encounter lists an invader, that invader is part of the encounter every time the party enters that encounter until the invader is defeated" (DS-Phantoms 636-640); Ambush Lies Ahead: "Win or lose, the invader will not reappear" (560-565).
- Ruling: CHANGE to the campaign's own rule.
- Why: The copy was an error. The Gauntlet is the campaign about beating every invader; under the copied rule a party could fail once and walk past each of them.
- Mechanical: yes
- Edits: campaign-E35

### campaign-033 · Ch. 19: Call of the Abyss
- Question: Is Section Two (Level 1, 2, 2, 3) right, and is the campaign complete?
- This book now: four sections; Section Two as Level 1, 2, 2, 3 before Sif (§19.7).
- Evidence: official Four Kings booklet: Section 2 is Level 1, 2, 2, 3; the campaign has five sections, the fourth being "Penultimate Trial" (Level 3, Level 3, Level 4, Ornstein & Smough); the publisher's update describes it as played "over five game sessions".
- Ruling: CHANGE. Section Two is confirmed. Section Four: Penultimate Trial is added and The Abyss becomes Section Five.
- Why: Section Two differs from Facing the Abyss in the booklet too, so it was no transcription error. The missing section was.
- Mechanical: yes
- Edits: campaign-E38

### campaign-034 · Ch. 19: Demon Hunting
- Question: Does Section One lack a bonfire tile, and are Sections Three and Four both "Sen's Fortress"?
- This book now: Section One has no bonfire tile and a special rest rule; Section Four is named "Sen's Fortress" (§19.6).
- Evidence: official Asylum Demon booklet: Section 1 begins "Bonfire Tile"; Section 4 is "Northern Undead Asylum"; the Asylum Demon mini-boss is fought "on the Mega Boss game board instead of the Mini Boss tile".
- Ruling: CHANGE (includes one deletion). The bonfire tile is restored to Section One, the special rest rule is deleted, Section Four is renamed, and the board for the Asylum Demon is stated.
- Why: The rest rule was written to repair a list that had lost a line. With the line restored the section is set up like any other and a paragraph of special procedure goes.
- Mechanical: yes
- Edits: campaign-E36, campaign-E37

### campaign-035 · Ch. 19: The First Journey, Section Four heading
- Question: Is the section "Bathed in Flame" or "Royal Wood"?
- This book now: "Section Four: Bathed in Flame" (§19.1).
- Evidence: Kalameet booklet: scenario title "Bathed in Flame", "Section 4 Royal Wood" (DS-BDK 500-530).
- Ruling: CHANGE to "Royal Wood".
- Why: Every other heading in the chapter is the section's printed name; this one alone used the scenario's title.
- Mechanical: no
- Edits: campaign-E42

### campaign-036 · Ch. 19: The Undead Colosseum
- Question: Is Explorers required, is the shared Level 4 deck right, and what is the soul reward?
- This book now: Explorers required; Level 1 to 3 decks from core, Darkroot and Explorers together; Level 4 deck from both mega-boss expansions; cleared encounters never reset; "the campaign soul reward for its level and two further souls" (§19.9).
- Evidence: official: "featuring the Executioner's Chariot and content from the Explorers, Darkroot, and Vordt of the Boreal Valley expansions"; shared decks as the book has them; "players gain 4 souls per player each time they defeat an encounter", against a standard two (DS-EC 615-630). The Vordt booklet carries a different campaign (see the annex).
- Ruling: CONFIRM as written, with one wording correction.
- Why: The Old Dragonslayer and the Pursuer are Explorers bosses, so Explorers is required. The shared Level 4 deck is the published rule and works as written, since Level 4 cards are not tied to one board. The raised reward pays for encounters that cannot be repeated. Only the phrase "campaign soul reward" is wrong, because campaign play has no table of its own.
- Mechanical: no
- Edits: campaign-E43

### campaign-037 · Ch. 19: dependencies on §18.1
- Question: Does §18.1 cover the five cases chapter 19 relies on?
- This book now, and ruling on each:
  - A section that ends in any encounter: covered by §18.1, Section Completion. CONFIRM.
  - Level 4 encounters inside sections: covered by §18.1; reward corrected in campaign-021.
  - A mega-boss that is not the last boss: covered by §18.1 ("does not end the campaign"). CONFIRM.
  - Big Game Hunting, the board for the Asylum Demon and the layout of the three free-order sections: settled in campaign-031 (the Asylum Demon's own board; each section set up when the one before it is completed).
  - The official "add transposed and legendary treasure after Section 1": replaced throughout by the bonfire ascetic and transposition. CONFIRM; one rule for all twelve campaigns is better than a footnote in each.
- Evidence: §18.1; official booklets as cited above.
- Ruling: CONFIRM as written (the two changes are carried by campaign-021 and campaign-031).
- Why: The general rules in §18.1 do the work; §19 needs only lists.
- Mechanical: no
- Edits: none

### campaign-038 · Ch. 19: glossary entry Section
- Question: Does the glossary definition cover sections that end in an encounter or a mimic?
- This book now: "completed when the last boss it lists is defeated or, for a section whose list ends in an encounter, when that encounter is cleared" (`12_glossary.md` line 259).
- Evidence: §18.1; §19.8 states its own exception.
- Ruling: CONFIRM as written.
- Why: The entry already matches §18.1, and a campaign's own rule takes precedence without the glossary listing it.
- Mechanical: no
- Edits: none

### campaign-039 · Ch. 19: the mimic of A Hollow Pursuit
- Question: Is the chest a mimic on every attempt?
- This book now: "When the party opens the chest, a mimic encounter begins as if an ambush card showing Mimic had been revealed" (§19.8).
- Evidence: Explorers booklet: "the chest is automatically a mimic. The party proceeds to Section 3 when the mimic is defeated"; §13.4 returns a mimic to its chest after a failed mimic encounter and uses the face-up ambush card as the record.
- Ruling: CHANGE (clarification): "Each time the party opens the chest", with a pointer to §13.4.
- Why: This chest has no ambush card to act as the record, so the text has to carry it.
- Mechanical: no
- Edits: campaign-E44

### campaign-040 · Ch. 19: listed invaders and the limits of §12.2
- Question: Do the limits of §12.2 (one invasion per leg, standard invaders early) apply to invaders a campaign lists?
- This book now: §12.2, "Some campaigns place named invaders in listed encounters and use no invader tokens"; §19.3 and §19.4 place no tokens.
- Evidence: official Phantoms campaign pages list advanced invaders in early sections and state that no tokens are placed.
- Ruling: CONFIRM as written.
- Why: The limits govern invasions, which are the placing of tokens; a listed invader is not an invasion.
- Mechanical: no
- Edits: none

---

## (a) Every CHANGE, ADD and DELETE

| Item | Ruling | What changes | Mechanical | Edits |
|---|---|---|---|---|
| campaign-003 | CHANGE | Umbrella for lead item 18; carried by the items below | yes | see 006 to 008, 031, 033, 034 |
| campaign-005 | CHANGE | Hollow cubes: supplied by no set, provided by the players | no | E01, E02 |
| campaign-006 | CHANGE | Condition tokens five of each (28); supply is not a limit | no | E03, E04 |
| campaign-007 | CHANGE | Phalanx models; Four Kings models and dials; four expansion-specific component lines; Asylum Demon cards | no | E05 to E08 |
| campaign-008 | CHANGE | Boss treasure 63 to 48, total 534 to 519; encounter cards 31 to 37 per level, total 169 to 187 | no | E09 to E11 |
| campaign-009 | CHANGE | "Dragon Slayer Ornstein" | no | E12 to E15 |
| campaign-015 | CHANGE | Spark buy-back paid by the party together | yes | E18 to E23 |
| campaign-016 | CHANGE | Spark maximum never more than five | yes | E24 to E27 |
| campaign-020 | CHANGE | Default sets for campaign encounter decks | yes | E30 |
| campaign-021 | CHANGE | Campaign Level 4 encounters award ordinary treasure, not mega-boss treasure | yes | E16, E17 |
| campaign-023 | CHANGE | Joining needs one spark on the dial, not two | yes | E28 |
| campaign-025 | CHANGE | Transposition "once the first section is completed" (wording) | no | E31, E32 |
| campaign-026 | ADD | Standard invader tokens until the bonfire ascetic is burnt, advanced after | yes | E33 |
| campaign-028 | CHANGE | Glossary Fog gate follows §18.2 | no | E34 |
| campaign-031 | CHANGE | Into the Depths Section Four and the no-Darkroot option; Big Game Hunting 16 souls, boards, set-up order, substitution | yes | E39 to E41 |
| campaign-032 | CHANGE | The Gauntlet: an invader returns until killed | yes | E35 |
| campaign-033 | CHANGE | Call of the Abyss gains Section Four: Penultimate Trial | yes | E38 |
| campaign-034 | CHANGE, with a DELETE | Demon Hunting: bonfire tile restored, special rest rule deleted, Section Four renamed | yes | E36, E37 |
| campaign-035 | CHANGE | "Section Four: Royal Wood" | no | E42 |
| campaign-039 | CHANGE | A Hollow Pursuit: the chest is a mimic each time it is opened | no | E44 |

Two CONFIRM rulings carry a wording edit: campaign-002 (E29) and campaign-036 (E43). No Gate 1 decision is revised; OQ-21 and OQ-22 are confirmed, and the change to the spark buy-back settles a point OQ-22 left open (who pays).

## (b) Not settled, and why

1. The Painted World of Ariamis contents. No copy of its rulebook was found. Its share of the treasure totals (10/30/45/5/5) is the manuscript's totals less every set that was checked, and it agrees with the community guide's count of 95 item cards; its encounter cards (27, nine per level) and its Phalanx models rest on the community guide and on the publisher's count of 18 miniatures. An owner of the set should check four lines: the starting equipment of the Deprived, Mercenary and Sorcerer, the legendary and boss treasure counts, the encounter cards per level, and the Phalanx models.
2. The split of the 2022 encounter cards by level (nine each) comes from the community guide alone; the rulebook gives only the total of 29 with two boss encounter cards.
3. The highest number on the physical spark dial is inferred to be five (the official game never sets it higher, and one community ruleset says it cannot go above five). If the dial shows six, campaign-016 can be withdrawn without other effect.
4. The printed form of Ornstein's name was checked against two rulebooks, not against the card.
5. Superseded by the follow-up below: the four further official campaigns are now drafted as §19.13 to §19.16 (campaign-041 to campaign-045).
6. A catch-up for a character who joins late in a campaign (campaign-023) was not added. If play shows that a late joiner cannot contribute, the simplest form is a soul grant for each completed section, on the model of Big Game Hunting's 16 souls.

## (c) Cross-cluster effects

- §17 (boss special rules): campaign-E13 to E15 change "Dragonslayer Ornstein" in §17.2 and §17.5; they may collide with edits from the cluster that owns chapter 17. §17.3 should state that the Asylum Demon mini-boss is always fought on the mega-boss side of its expansion's game board (the official booklet says so for every game); §19.6 and §19.12 now cite §17.3 for it. §17.10 should account for the components now listed in §2.9: four identifier tokens and four health dials (The Four Kings), four Fiery Breath cards (Guardian Dragon), six Fire Beam cards (Old Iron King).
- §6.7 and lead item 19 (Level 4 treasure): campaign-021 makes the campaign reward independent of the standard one. The last sentence of §6.7, Level 4 Encounters could add "and is rewarded as that section states (see §18.1)".
- §7.4 (sparks, standard game): the standard game has no ceiling, so a lone character who defeats a boss without resting would need six on the dial. The same cap, "a spark gained while the dial shows five is not added", belongs there (A-047).
- §7.2, §3.4 and the glossary entries Hollow cube and Hollow (lead item 3): §2.8 now says no set supplies the cubes. If the owner of lead item 3 rules otherwise (for example spare black cubes at the right of the bar, as one community ruleset does), campaign-E01 and E02 must follow that ruling.
- §8.3: "The number of characters is fixed at setup" and "in a campaign changes only when a player joins or leaves it" should read for both kinds of game, since §18.4 lets a player join a standard game.
- §8.5: campaign-E04 states that the supply of condition tokens is not a limit; §8.5 is silent and should not contradict it.
- §12.2: Invader Tokens, step 1 needs a pointer for campaign play ("in campaign play, see §18.1"), and End of an Invasion ("An invader appears once") needs "except where a campaign states otherwise (see §19.4)".
- §11.3 and §7.6: both say souls cannot be pooled. They remain true as general rules; the two exceptions are now stated in §18.3 and §18.7, and the F.A.Q. and glossary are edited to match (E22, E23).
- §2.5 and the glossary entry Treasure card differ: the glossary counts an ember card as a treasure card and §2.5 does not. One of the two should follow the other.
- F.A.Q. §22.1: campaign-E23 italicises *spark* one question before the existing italic use in the same section; the later one may be set plain.
- Layout: campaign-E11 lengthens the paragraph after the encounter card table by one sentence, campaign-E07 adds four list lines to §2.9, campaign-E21 adds a row to the Shop Price Table, and campaign-E38 adds a seven-line section to §19.7.

## Annex — official campaigns not in this book

Superseded by the follow-up section at the end of this memo, where these four campaigns are drafted in full. Lists are as printed in the booklets.

- Go Beyond Death (Old Iron King; core, Explorers, Iron Keep; shared deck of the three, Level 4 from Old Iron King). 1 Tower of Flame: Bonfire, L1, L1, L1, L2, Old Dragonslayer. 2 Threshold Bridge: Bonfire, L1, L2, L2, L3, Smelter Demon. 3 Ironhearth Hall: Bonfire, L2, L3, L3, Fortress Gates (L4), Pursuer. 4 Eygil's Idol: Bonfire, L3, Blazing Furnace (L4), Old Iron King.
- Footsteps of Giants (The Last Giant; core, Darkroot; shared deck; a Level 2 or 3 card is redrawn unless it shows a Large Hollow Soldier, Sentinel, Mushroom Parent, Stone Knight or Stone Guardian). 1 Echoes of Giants: Bonfire, L1, L1, L1, Winged Knight. 2 Hall of Remembrance: Bonfire, L2, L2, L2, Titanite Demon. 3 Twisted Wood: Bonfire, L2, L2, L3, Sif. 4 Grove of Giants: Bonfire, L3, L3, Forest of Fallen Giants (L4), Artorias. 5 The Giant's Rest: Bonfire, L3, L3, The Petrified Fallen (L4), The Last Giant.
- Treasures of the Ice Cave (Vordt; core, Phantoms; Level 4 from Vordt). 1 Glacial Entrance: Bonfire, L1, L1, L2, L2 with Melinda the Butcher and Oliver the Collector. 2 Arctic Pass: Bonfire, L2, L2, L2, L3, Boreal Outrider Knight. 3 Frozen Corridor: Bonfire, L2, L3, L3, Guarded Path (L4) with Marvelous Chester and Paladin Leeroy. 4 The Boreal Sanctuary: Bonfire, L3, L3, The Dog's Domain (L4), Vordt. Both invaders of an encounter must be beaten, and they return if the party dies.
- Demons and Dragons (Guardian Dragon; Asylum Demon, Gaping Dragon and Kalameet expansions). Encounters award no souls and one treasure card per player; stat tiers are granted at the start of each section; a Level 4 encounter grants a spark. 1 The Dungeon's Gates: Bonfire, L1, L1, L1, L2, Asylum Demon. 2 The Bloody Road: Bonfire, L2, L2, L2, L2, Titanite Demon. 3 The Peak of Peril: Bonfire, L2, L3, L3, L4, Guardian Dragon. 4 The Maw of Death: Bonfire, L3, L3, L4, Gaping Dragon. 5 The Final Conflict: Bonfire, L4, Stray Demon, L4, Black Dragon Kalameet. This one replaces the soul economy outright and would need the most new text.

---

## Follow-up — the four further campaigns and the local booklets

The eight mega-boss booklets are now in `work/text/` (DS-AD-Rules-web-EN.txt, DS-Four-Kings-Rules-web.txt, DS-GaD-Rules-web.txt, DS-GD-Rules-web.txt, DS-MFA-Rules.txt, DS-OIK-Rules-web.txt, DS-TLG-Rules.txt, DS-VotBV-Rules-web.txt). Line references below are to those files.

### campaign-046 · Re-check against the local booklets
- Question: Do the local booklets differ from the online copies used for campaign-007, -031, -033 and -034?
- This book now: as edited by campaign-E05 to E08 and E36 to E41.
- Evidence: a word-for-word comparison of each local text with the copy used earlier. Seven are identical; the eighth (Asylum Demon) differs only by a stray control character in the extraction. Campaign pages: Demon Hunting, DS-AD 490-551; Call of the Abyss, DS-Four-Kings 513-568; Into the Depths, DS-GaD 507-561; Big Game Hunting, DS-MFA 501-561.
- Ruling: CONFIRM. No earlier edit changes.
- Why: The lists and the contents pages are the same text.
- Mechanical: no
- Edits: none

### campaign-041 · §19.13 Go Beyond Death
- Question: How is the Old Iron King campaign stated in this book's terms?
- This book now: absent.
- Evidence: DS-OIK-Rules-web.txt, campaign pages: four sections; "a shared deck of encounters from the core game, the Explorers expansion, and the Iron Keep expansion"; Level 4 encounters from the Old Iron King expansion; named Level 4 encounters Fortress Gates (Section 3, before the Pursuer) and Blazing Furnace (Section 4).
- Ruling: ADD as §19.13.
- Why: It needs no rule of its own. The general rules of §18.1 already cover a named Level 4 encounter and a Level 4 encounter in a section that ends in a main-boss.
- Mechanical: yes (new content)
- Edits: campaign-E48

### campaign-042 · §19.14 Footsteps of Giants
- Question: How is The Last Giant campaign stated, and how is its redraw rule applied to cards dealt face down?
- This book now: absent.
- Evidence: DS-TLG-Rules.txt, campaign pages: five sections; shared deck of the core game and Darkroot; "When players draw a level 2 or level 3 encounter, discard that encounter and draw again unless it contains one of the following enemies" (Large Hollow Soldier, Sentinel, Mushroom Parent, Stone Knight, Stone Guardian); named Level 4 encounters Forest of Fallen Giants and The Petrified Fallen.
- Ruling: ADD as §19.14. The redraw rule is written as a filter applied when the Level 2 and Level 3 decks are built.
- Why: Filtering the deck first gives exactly the same cards as drawing and redrawing, and it keeps the cards face down, as §18.1 deals them.
- Mechanical: yes (new content)
- Edits: campaign-E48

### campaign-043 · §19.15 Treasures of the Ice Cave
- Question: How is the Vordt campaign stated, and how are two invaders fought in one encounter?
- This book now: absent. §12.2 provides for one invader, one invader health dial, and an invader that vanishes when a character dies.
- Evidence: DS-VotBV-Rules-web.txt, campaign pages: four sections; encounters from the core game, Level 4 from Vordt; "Both invaders must be defeated before obtaining their treasure. If the party dies during this encounter both invaders will respawn. The party proceeds to Section 2 when the encounter is defeated" (Sections 1 and 3); The Dog's Domain named for Section 4. The Phantoms expansion supplies one invader health dial (DS-Phantoms 98-105).
- Ruling: ADD as §19.15, with four short rules for the paired invaders.
- Why: Three of the four rules restate the booklet (both return until both are killed in one visit; treasure only when both are dead; the section ends only then). The fourth fills two real holes the booklet leaves: where the second invader stands and how its health is recorded when the box holds one dial. Requiring both kills for the section also stops a party from ending a section by losing a character and letting the invaders vanish.
- Mechanical: yes (new content)
- Edits: campaign-E48

### campaign-044 · §19.16 Demons and Dragons
- Question: How is the Guardian Dragon campaign's replacement economy stated in this book's terms?
- This book now: absent.
- Evidence: DS-GD-Rules-web.txt, campaign pages: five sections; "Level 4 encounters should be drawn from a shared deck and should use the encounter side of the game board from their original expansion"; "encounters do not reward souls. Instead, each encounter rewards one card from the treasure deck per player. Additionally, level 4 encounters reward the party with 1 spark"; "level 4 encounters and mega boss encounters will not reset"; a list of free stat increases at the start of each section; Section 5 lists two Level 4 encounters and two mega-bosses. The printed title is "Demons & Dragons".
- Ruling: ADD as §19.16: four bulleted rules and one table.
- Why: In this book every encounter already awards a treasure card to each character, so "one card per player in place of souls" becomes one sentence: encounters award no souls. The stat grants are a table. Followed in full they bring all four stats to tier three by Section Five, so no further rule is needed.
- Judgement calls, each one sentence in the draft and easy to strike:
  - Boss and invader soul rewards are kept. The booklet removes souls from "encounters"; read literally that leaves the boss reward, and in this book that small income (six souls a character for each boss) is what pays for the bonfire ascetic, a spark or a transposition. The other reading, no souls at all, would leave the ascetic to be paid for by selling 16 cards.
  - The level 1 to 3 decks are built from the core set, the booklet being silent.
  - The heading is "Demons and Dragons", since headings in this book carry no ampersand.
  - Section Five has a boss that does not end its section; the last line of the draft points to §18.1, which already governs it.
- Mechanical: yes (new content)
- Edits: campaign-E48

### campaign-045 · The count of campaigns
- Question: Where does the book state the number of campaigns?
- This book now: "12" in §18.1; "Twelve" and "twelve" in the introduction to §19; "12" in the glossary entry Campaign. The Introduction, the front matter and the F.A.Q. state no number.
- Evidence: a search of every chapter file and the glossary.
- Ruling: CHANGE to 16 in the three places.
- Why: Consequential on campaign-041 to campaign-044. "A campaign has three to six sections" and "Two of them ... require only the core set" (§18.1) remain true.
- Mechanical: no
- Edits: campaign-E45, campaign-E46, campaign-E47

Additions to the table in (a):

| Item | Ruling | What changes | Mechanical | Edits |
|---|---|---|---|---|
| campaign-041 | ADD | §19.13 Go Beyond Death | yes | E48 |
| campaign-042 | ADD | §19.14 Footsteps of Giants | yes | E48 |
| campaign-043 | ADD | §19.15 Treasures of the Ice Cave, with rules for paired invaders | yes | E48 |
| campaign-044 | ADD | §19.16 Demons and Dragons, with its replacement economy | yes | E48 |
| campaign-045 | CHANGE | Twelve campaigns become 16 in §18.1, §19 and the glossary | no | E45 to E47 |

Notes for the lead editor on the follow-up:

- One edit, E48, carries all four new sections, because the insertion point (the last line of §19.12) can serve as `old` only once.
- §2.9 needs no further component line: the Fire Beam cards, the Fiery Breath cards, the corrosion tokens and the pillar tokens are already listed by campaign-E07, and the other two expansions have no component of their own. The one shortage is the second invader health dial of §19.15, which the draft meets with "any health dial that is not in use".
- The lines "The party may add the Explorers and Characters expansions" in the new sections follow the pattern of the chapter; the booklets do not print them.
- The new sections state their encounter sets in full, so they stand whether or not campaign-E30 (the default in §18.1) is adopted.
- §19.16 depends on two general rules staying as they are: a boss that does not end its section (§18.1, Section Completion) and the Level 4 reward of campaign-E16.
- §12.2 needs the same pointer for §19.15 as for §19.4: "An invader appears once" and "the invader vanishes" hold "except where a campaign states otherwise".
- Totals after the follow-up: CONFIRM 18, CHANGE 20, ADD 5, NOT A QUESTION 3 (46 entries).
