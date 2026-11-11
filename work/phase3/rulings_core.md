# Rulings memo — cluster `core`

Scope: lead items 3, 9, 10, 12, 15, 17, 19, 20 of `14_open_issues.md`; every item of the per-chapter lists for chapters 03, 04, 06, 07, 11 and 23; the designer's review points set for this cluster (hollow marker, soul economy, shop simplicity, token refresh, first-clear treasure wording).

Entries: 70. Edits: 37, in `edits_core.json` (`core-E01` to `core-E37`). Every `old` string was checked to occur exactly once in its file, and the seven chapter files and the glossary pass `tools/style_check.py` with zero violations after all 37 edits are applied to copies.

## Sources and how they are cited

| Short name | File |
|---|---|
| Core17 | `work/text/DS-Core-Rules-lores.txt` (official core rules, 2017) |
| TG22 | `work/text/DS-TG-Rulebook-Compressed_compressed.txt` (official rules, 2022) |
| FAQ17 | `work/text/Dark_Souls_The_Board_Game_FAQ.txt` (official) |
| BDK / EC / Phantoms / Explorers | the official expansion booklets in `work/text/` |
| Ext | `work/text/DS-Extended-Rules-V45.txt` (community, Extended Rules) |
| Holl | `work/text/Hollowed_Edition_v1.3.txt` (community, Hollowed Edition) |
| Src | `work/phase2a/source/NN_*.md` (the author's own manuscript) |

Web: the search tool worked and was used with generic queries. Page fetches were mostly refused: BoardGameGeek returned HTTP 403, the Fextralife board-game wiki host could not be reached from this session, and a Reddit mirror of the house-rules megathread returned 404. One article on community house rules was fetched in full (gamerant.com/dark-souls-board-game-house-rules/). Online evidence below is therefore search-result summaries plus that article; where nothing useful was found the entry says "online: nothing found".

The official F.A.Q. (FAQ17) covers only dodging, pushes and one condition interaction. It is silent on every item in this cluster and is not repeated in each entry.

---

## Part 1 — Lead items

### core-001 · Lead 3 — the component that marks hollowing
- Question: What physical component marks the two blocked spaces of a hollow character's endurance bar, so that it cannot be taken for stamina or damage?
- This book now: "8x Hollow cubes" with no set named, "of a colour distinct from the damage, stamina, and stat cubes" (§2.8; §7.2; glossary Hollow cube).
- Evidence: Core17 l.237-244: the box holds 32 red cubes, 32 black cubes and 16 white cubes, and nothing else cube-shaped. TG22: no hollowing and no white cubes. Ext l.57-59: where a rule needs a colour the box lacks, "you can replace them with a marker of any type that will cover up a spot on the player board". Holl l.56-58 and l.291-301: hollowing is marked with black cubes on the right of the bar, which is the same colour as stamina. Src 03 l.58 and 07 l.20: the author wrote "a marker such as white cubes" and "two white cubes". Online: the Hollowed Edition is the only community ruleset found that blocks bar spaces; no discussion of the marker.
- Ruling: CHANGE
- Why: The book asks for eight cubes that no set supplies. The only cube in the box that is never placed on an endurance bar is the white one, and it is what the author wrote. White on the bar cannot be read as black (stamina) or red (damage), which the Hollowed Edition's black cubes can once a bar fills with stamina. A party of one to three characters has four to twelve white cubes spare. A party of four uses all 16 as stat cubes, so the rule needs one honest sentence of fallback, the same device §2.8 already uses for soul tokens.
- Alternatives weighed and not chosen: (a) black cubes at the right end, as the Hollowed Edition does: fails the "cannot be confused" test when Rest or recovery says "remove every stamina cube"; (b) a stamina cube stacked on a damage cube: in the box and distinct, but fiddly and easily knocked; (c) the character's own ember token laid across the two spaces (an embered character is never hollow, so the token is always free): elegant and never short, but it is a clever answer where a plain one exists, it depends on the size of the token, and it would rename the hollow cube in some thirty places.
- Mechanical: no
- Edits: core-E01, core-E02, core-E03, core-E04 (and the wording of core-E20)

### core-002 · Lead 9 — shop stocking, no twelve-draw cap
- Question: Is a shop stocked by drawing until every category is full, or does stocking stop after twelve draws?
- This book now: draw until every category is full or the deck runs out; set-aside cards are shuffled back; a category is short only if the deck runs out (§6.3).
- Evidence: Core17 l.647-650: no stocked shop, one soul buys a blind draw. TG22 l.2034-2041: four cards are turned up, any may be bought for one soul each, the rest go to the bottom. Ext: two treasure decks split at a requirement of 25, no shop. Holl l.21-28 and l.165-195: three sorted decks (weapons, armour, magic), one soul a card. Src 06: "Draw tier one treasure cards one at a time to stock tier one shop: 3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells ... Reshuffle extra treasures." Audit B-023 itself estimates 22 to 28 draws to fill the twelve places. Online: sorting treasure by kind is one of the most common house rules (gamerant article, "Separate Treasure Decks").
- Ruling: CONFIRM as written
- Why: A cap of twelve draws against a quota of twelve places leaves the shop short almost every time, and a short shop defeats the reason for the quota, which is that every kind of character finds something to buy. The quota is the author's answer to the game's best-known complaint (blind, unsorted treasure) and it costs one extra minute three times a game. Drawing to the quota is the simplest procedure that keeps one deck per tier.
- Mechanical: no
- Edits: none

### core-003 · Lead 10 — shop sales: ember card, Titanite, upgrade service
- Question: Where does a sold ember card go, does attached Titanite add to a sale, and does Andre charge for fitting or removing upgrades?
- This book now: a sold ember card returns face up to the tier one shop; the weapon's sell value is paid once and Titanite adds nothing; attaching and removing are free and unlimited during a rest (§11.4).
- Evidence: Core17 l.671-679: "Upgrading weapons and armor does not have a soul cost"; armour upgrades are freely removed, weapon upgrades never. TG22 l.2062-2089: upgrading is free and any upgrade may be removed at the bonfire. Neither official ruleset has selling. Ext: silent on selling. Holl l.196-206: upgrades free, weapon upgrades "cannot be removed, only replaced". Src 11: sold cards go "to the bottom of their respective treasure deck"; no price for the service. Online: nothing found on selling.
- Ruling: CONFIRM as written
- Why: All three answers are what a player would guess. A sold card goes back where cards of its kind live, and for an ember card that is the shop shelf, which also keeps the count of ember cards fixed. A flat sell value with nothing added for Titanite needs no table. A free service follows both official rulebooks. One refinement to where sold Titanite goes is made in core-048, and the missing destination of a consumed ember card is supplied in core-021.
- Mechanical: no
- Edits: none (see core-021, core-048)

### core-004 · Lead 12 — luck rerolls only the character's own rolls
- Question: May a character spend the luck token on another model's roll?
- This book now: "one of their own attack rolls or defence rolls"; any or all dice, chosen together, new results stand (§3.5, Luck).
- Evidence: Core17 l.526-529: "Any character may flip their Luck token ... to reroll one die in their attack, block, or dodge roll." TG22 l.816-817: "reroll a die in one of their attack or defence rolls." Both officials say "their". Ext l.76-78: an example of a player rerolling her own block die. Holl: token recharged for one soul, no change of scope. Src 03: "reroll any attack or defence roll. Any or all of the dice may be rerolled all at once". Online: no ruling found that allows another player's roll.
- Ruling: CONFIRM as written
- Why: Each character owns one token and one decision. Letting tokens cross the table would pool four rerolls on whichever roll matters most and take the decision away from the owner. The stronger reroll (any or all dice) is the author's and is kept; it is paid for by the token returning only at a rest. One wording gap is closed: §9.6 already lets luck reroll a parry roll, and the list in §3.5 left the parry out.
- Mechanical: no
- Edits: core-E18

### core-005 · Lead 15 — Appendix A: Butcher Knife and the Tier column
- Question: Is the Butcher Knife 24 STR (tier one) or 28 (tier two), and may the Tier column stand when card treasure types are not listed?
- This book now: Butcher Knife 24/0/0/0, tier one; Tier computed from requirements alone, with a section stating that transposed, legendary and boss treasure are placed by type (Appendix A).
- Evidence: Src 23 l.122: the author wrote 25/0/0/0. Audit B-020 (optional) moved it off the boundary and offered 24 or 28. Core17, TG22, Ext, Holl: no card list. Ext l.1107 shows only that the printed card heals on a hit. Online: the card's printed requirement was not found; a search summary of a wiki table for the video game of the same licence lists the Butcher Knife at 24 strength and no dexterity, which is the kind of source the author's appendix says it follows ("nonsensical weapon stat requirements which this edition aims to remedy").
- Ruling: CONFIRM as written
- Why: The appendix exists to make requirements match the weapons' origin, and 24 does. It also takes the card off the one-point boundary, so nobody has to recall whether 25 is "below 25". The Tier column is a convenience and every row was checked against the rule of §6.2 (61 rows, no error); the Treasure Type section already covers the cards whose type overrides the column. If the author prefers the original 25, only that row and its Tier cell change.
- Mechanical: no
- Edits: none

### core-006 · Lead 17 — the dropped Firekeeper luck purchase
- Question: Should a character be able to pay the Firekeeper one soul to ready the luck token?
- This book now: not included; the rest readies the token (§11.2 step 6; §11.3).
- Evidence: Core17 l.711-712: "A character must spend 1 soul to flip their Luck token to the ready side." In Core17 the party visits the bonfire tile freely and resting is a separate choice (l.623, l.690-706), so the purchase readies luck without a spark. TG22: dropped; the luck token is readied by the rest alone (l.1929-1933). Ext: silent. Holl l.236-242: tokens recharged for souls while exploring (luck one soul). Src 11: no purchase. Online: nothing found.
- Ruling: CONFIRM as written
- Why: The purchase only ever made sense where the Firekeeper could be visited without resting. In this book she is visited only during a rest, and the rest has already readied the token, so the purchase would buy nothing. The current official rules dropped it for the same reason. Bringing it back would need a second kind of bonfire visit, which core-050 removes.
- Mechanical: no
- Edits: none

### core-007 · Lead 19 — Level 4 treasure
- Question: Does the Level 4 encounter award one mega-boss treasure card to the party in place of one tier two card per character?
- This book now: one mega-boss treasure card is dealt to the game board and awarded as a chest's card is; no tier two cards are dealt; the soul reward is the Level 4 reward of six (§6.7; §7.6; §7.7).
- Evidence: BDK l.248-253 and EC l.283-288: the official Level 4 encounter pays eight souls per character and no treasure. Core17, TG22: no Level 4. Ext l.26-28: Level 4 souls are not doubled. Holl: silent. Src 06, Setup After the main-boss, step 5: "Shuffle mega-boss Items and deal one face-down to the encounter tile"; no tier two cards are mentioned. Online: nothing found.
- Ruling: CONFIRM as written
- Why: This is the author's own rule, not a reduction made in editing. It is also good design: a mega-boss's treasure would otherwise be won only when the game is over, and here one of its cards is in play for the fight that matters. A ninth random card for each character, with one paid rest left to equip it, would add shuffling and little choice. One card for the party to argue over is the more interesting reward.
- Mechanical: no
- Edits: none

### core-008 · Lead 20 — tile layout for the two legs
- Question: Must the first leg be laid as two rows of three tiles and the second as a straight line?
- This book now: first leg, a grid of two rows of three with the bonfire tile and the mini-boss tile in opposite corners, each encounter tile turned so that "exactly two of its doorways open on to adjacent tiles" (§6.5); second leg, a straight line (§6.6).
- Evidence: Core17 l.295-300: "lay out four of the tiles around the Bonfire tile in any way you wish, aligning their doorways as you go". Core17 l.835-850 shows a tile with doorways on two adjoining walls only, so tiles differ in where their doorways are. TG22: encounters are set up from cards; no route of tiles. Ext l.31-35 and Holl l.254-264: free or procedural layouts. Src 06: "a two by six tile grid ... opposite corners" for the first leg and "a straight line" for the second. Audit A-088 and C-090 corrected the arithmetic to two by three; D-031 read the intent as a line. Online: summaries repeat the official free layout; no discussion of a fixed shape.
- Ruling: CHANGE
- Why: In this book the route is a fixed chain of four encounters, so the shape on the table has no effect on play. Two different shapes for one function is one rule too many. A straight line of seven tile widths does not fit most tables. And "exactly two doorways open on to adjacent tiles" cannot be met by a tile with three or four doorways sitting in a grid, where a third doorway faces a tile that is not next on the route. One rule covers both legs: lay a chain, bend it as the table allows, use the two doorways that join the chain and ignore the rest. The author's grid is kept by name as one permitted chain.
- Mechanical: no
- Edits: core-E05, core-E06, core-E07

---

## Part 2 — Designer's review points

### core-009 · Review — does the soul economy hang together?
- Question: Do the rewards (3/4/5/6), stat tier costs (2/4/8/10), shop prices (2 and 4), sell values (1 and 6) and the summon cost (2) fit one another across a standard game?
- This book now: §7.6 (rewards, reduced reward half rounded down), §11.3 (tiers), §11.4 (prices), §12.1 (summon), §6.1 (a lone character starts with six souls).
- Evidence: Core17 l.867: two souls per character per encounter into a shared cache; l.647: one soul per blind draw; l.697-705: tiers cost 2/4/8. TG22 l.1929-1933 and l.2034-2039: tiers 2/4/8, one soul a card. Ext l.26-28 and l.44-47: encounter souls doubled; a summon costs two souls per player. Holl l.29-33 and l.6-12: level plus one soul per character, tiers 2/4/6/8, one soul a card. Online: the commonest complaint is grinding, and the commonest fix is doubled souls with halved sparks (gamerant article; Reddit megathread summary).
- Estimate, per character, with no encounter fought twice: a first leg of two Level 1 and two Level 2 encounters pays 14 souls; the mini-boss pays 6; a second leg of two Level 2 and two Level 3 encounters pays 18. That is 20 souls in hand at the free rest after the mini-boss and 38 before the main-boss, against about 8 in the official game over the same eight encounters. Each character also receives eight treasure cards free (four tier one, four tier two).
- Needs, per character: one stat to tier three costs 14; a second stat to tier two costs 6; a third to tier one costs 2 (22 in all). Two tier one cards cost 4 and one or two tier two cards cost 4 to 8. A summon costs 2. A focused build therefore costs 30 to 36 of the 38 souls. Tier four (10 more) is out of reach without a mega-boss (which adds 6 for the main-boss and 6 for the Level 4 encounter) or repeated clears. Selling the four or five unusable free cards adds 4 or 5 souls.
- Ruling: CONFIRM as written
- Why: The numbers hang together. A character can afford one complete build and not two, so every purchase is a choice, and nothing has to be ground out. The prices are easy to hold in the head: a tier one card costs what stat tier one costs (2) and a tier two card what stat tier two costs (4). The flat sell value of 1 turns two unwanted tier one cards into one chosen card and four unwanted tier two cards into one chosen card, with no loop to exploit. A boss treasure card sells for the boss reward (6). No price in these chapters is out of line.
- Two observations for the lead editor, neither needing an edit here: (1) the summon (§12.1, another cluster) is the one price with no trade-off, because souls carried to the fog gate cannot be spent on anything else until the next rest; see cross-cluster effects. (2) A lone character's six starting souls cannot be spent until the first rest, which costs a spark; see "Not settled", item 1.
- Mechanical: no
- Edits: none

### core-010 · Review — are the shop rules as simple as they can be?
- Question: Can any shop rule be removed or made parallel without losing the author's design?
- This book now: §6.3 (stocking by category, restock after a boss, legendary handling), §6.6 steps 13 to 16, §11.2 step 7, §11.4 (prices, sales).
- Evidence: as core-002 and core-003. Core17 l.371-381: when the mini-boss falls the transposed and five legendary cards are shuffled into the deck, and every later draw can find them. Src 06: legendary treasure "do not appear in every game and cannot be purchased".
- Ruling: CHANGE
- Why: The rules are already close to minimal: two prices, one sell value, one stocking procedure used every time. Three trims remain. First, §11.2 step 7 restocks "if the shop has not been restocked since a boss was last defeated", which is never true, because the setup after a boss always restocks before the rest; it is deleted in core-052. Second, sold Titanite gets the same destination rule as every other sold card (core-048). Third, the second setup deals the tier two rewards before it stocks the tier two shop and adds the legendary cards, the reverse of the first setup (shop in §6.3, rewards in §6.5). As drafted, no legendary card can ever be dealt as an encounter reward; they could be found only beneath chests. Stocking first makes the two setups run in the same order and lets the five legendary cards turn up among the second leg's rewards, as they can in the official game.
- Mechanical: yes (a legendary card can now be dealt as a second-leg reward)
- Edits: core-E08 (and core-E09 to core-E11 under core-052; core-E31 to core-E33 under core-048)

### core-011 · Review — do embers, estus, luck and the heroic action refresh in parallel?
- Question: Are the refresh rules of the four character tokens clean and stated alike?
- This book now: heroic action, luck and estus flask tokens begin ready, are flipped when used, and are readied only by a rest at the bonfire; clearing an encounter readies none (§3.5; §7.5, Encounter Recovery; §11.2 step 6). The ember token has no ready side: it is gained by an ember card or a boss's defeat and lost only at death (§7.3). The refresh rule is stated in the opening paragraph of §3.5 and again under Heroic Action and Estus Flask, but not under Luck.
- Evidence: Core17 l.500-532 and l.702-706: all three readied by the rest; luck alone could also be bought back (see core-006). TG22 l.705-827 and l.1929-1933: all three readied by the rest; "ember tokens do not have a ready and used side". Ext l.95-97: one variant readies estus and heroic tokens only after a boss. Holl l.170-173 and l.236-242: readied by rest, or bought back for souls. Online: nothing found.
- Ruling: DELETE
- Why: The rule itself is clean and is confirmed: three once-per-rest tokens with one refresh rule, and one status token that a rest does not touch. Only the telling is uneven. Stating the rule once, in the paragraph that covers all three tokens, and removing the two repeats makes the three sub-sections parallel and shorter. The useful consequence ("at most once between rests") moves up to the shared paragraph.
- Mechanical: no
- Edits: core-E12, core-E13, core-E14

### core-012 · Review — is the first-clear treasure reward stated the same way everywhere?
- Question: Do all statements of the treasure reward for a first clear agree?
- This book now: §6.5 Encounter Cards step 3 and §6.6 step 13 (cards dealt to the tile are the reward); §6.7 step 5 and Level 4 Encounters (one mega-boss card for the party); §7.5 Encounter Resolution (a first clear is one made "while the treasure cards dealt to its tile at setup still lie on the tile"; step 3 gives each character one); §7.6; §7.7; §11.5; §18.5; glossary Cleared, Tier one treasure, Tier two treasure; §22.4.
- Evidence: Core17 l.864-868: no treasure for clearing, only souls. TG22 l.1348-1353: rewards are printed on each encounter card. Gate 1 OQ-11: the card dealt to the tile is the reward. Ext, Holl: no dealt rewards. Online: nothing found.
- Ruling: CHANGE
- Why: Ten of the eleven statements agree in substance: the dealt cards are the whole reward, one per character, the dead included, and a repeated clear awards none. One does not fit: §7.5 step 3 says "give each character ... one of the treasure cards dealt to the tile", and a Level 4 encounter has one card for the whole party. The step is reworded to cover both. A wrong cross-reference in §7.7 (the inventory is defined in §3.2, not §4.1) is corrected in passing. The glossary's "encounter rewards and chests draw from tier one" is loose but not wrong and is left.
- Mechanical: no
- Edits: core-E15, core-E17

---

## Part 3 — Chapter 03, characters (7 items)

### core-013 · Ch 03 — parry slot and §3.2
- Question: Must §3.2 change because the parry needs the shield in a particular weapon slot?
- This book now: §3.2 names the left and right weapon slots and says only that "which weapon slot holds a shield matters for the parry and the riposte (see §9.6)"; §9.6 requires the shield in the left weapon slot and the riposte weapon in the right.
- Evidence: Core17 l.565-570: left-hand and right-hand slots, a one-handed card in either; no parry in the official rules. TG22: no parry. Ext, Holl: no parry. Src 03 and audit A-068: the manuscript required the shield "as their left weapon"; A-068 proposed either slot. Online: nothing found.
- Ruling: CONFIRM as written
- Why: The sentence in §3.2 is neutral and correct whichever way §9.6 rules, so nothing in chapter 03 needs to move. The rule itself belongs to §9.6 and to the cluster that owns chapter 09. A view for that owner is under cross-cluster effects: "a shield in one weapon slot, the riposte with the weapon in the other" is the rule a player would guess, and it would let the left and right definitions drop out of §3.2.
- Mechanical: no
- Edits: none

### core-014 · Ch 03 — the red cube that marks stat tier four
- Question: Is the cube that marks stat tier four taken from the red damage cubes?
- This book now: at stat tier four the stat cube in the tier three space is replaced by a red cube and the stat cube returns to the supply (§3.3).
- Evidence: Core17 l.237-244: 32 red cubes, no other marker. Core17 and TG22 have three tiers only. Holl l.196-201: "Indicate tier 4 by replacing the white cube with a red cube." Src 11: "replacing the tier three white cube with a red cube". Ext: silent. Online: nothing found.
- Ruling: CONFIRM as written
- Why: It is the author's rule and the Hollowed Edition's, it needs no new component, and a red cube on the stat track cannot be mistaken for damage on the endurance bar. It also returns a white cube to the supply, which helps core-001. §11.3 and §18.6 already cite §3.3 for the tier four value, as the item asked.
- Mechanical: no
- Edits: none

### core-015 · Ch 03 — luck on another character's roll
- Question: Did the author mean luck to be spent on another character's roll, or on an opponent's roll in PvP?
- This book now: own rolls only (§3.5, Luck).
- Evidence: as core-004.
- Ruling: CONFIRM as written
- Why: Same ruling as core-004. Both official rulebooks say "their" rolls, and one token, one owner, one decision is the simplest rule.
- Mechanical: no
- Edits: none (core-E18 under core-004)

### core-016 · Ch 03 — does the ember token have a ready side?
- Question: Is the ember token a two-sided token or a plain marker?
- This book now: a marker with no ready side; it is never flipped (§2.8; §3.5).
- Evidence: TG22 l.820-822: "Unlike other character tokens, ember tokens do not have a ready and used side, and their effect is always in play." Core17 l.575-586: the token is placed and discarded, never flipped. Ext, Holl: no flipping. Online: nothing found.
- Ruling: CONFIRM as written
- Why: The current official rulebook says so in terms, and nothing in this book flips the token. CMP-0001's "every character token has a ready side and a used side" was a slip of generalisation.
- Mechanical: no
- Edits: none

### core-017 · Ch 03 — the one mention of "Taunt Level"
- Question: Should the single bridge from threat to the printed label "Taunt Level" be kept?
- This book now: "The dashboard prints the character's threat as its Taunt Level" (§3.1; glossary Threat).
- Evidence: Core17 l.493-495 and TG22 l.314: both official rulebooks label the dashboard value "Taunt level" and the enemy value "Threat level"; both icon keys list "Taunt". Ext, Holl: use the official words. Online: nothing found.
- Ruling: CONFIRM as written
- Why: A reader holding the published dashboard knows the value by that name, and one bridge costs one clause. It names a printed label, as the book already does for printed card names, so it breaks no rule of the house style.
- Mechanical: no
- Edits: none

### core-018 · Ch 03 — "10 spaces" or "ten-space"
- Question: Do §3.4 and the glossary write the bar's capacity the same way?
- This book now: §3.4 "a row of 10 spaces"; glossary Endurance bar "the track of 10 spaces".
- Evidence: the two texts as they stand.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: The glossary was aligned at integration; the two already agree.
- Mechanical: no
- Edits: none

### core-019 · Ch 03 — cross-chapter dependencies, and where the ember token starts
- Question: Are the dependencies listed for chapter 03 met, in particular the ember token's starting place?
- This book now: §6.1 step 3 places the stat cubes and step 4 the three ready tokens (met). §7.2 owns hollow cubes and death on a full bar (met). §7.5 states that clearing readies no token (met). §10.1 owns stamina overflow, Equip, Drink Estus and the start-of-turn recovery (met). §4.1 defines the shield and §4.3 the spell's slot (met). Not met: §3.5 and the glossary say the ember token "begins the game beside the dashboard", but §6.1 step 5 puts the ember tokens in the common supply, and §7.2 "discards" the token.
- Evidence: CMP-0001 (approved at Gate 1): "The ember token begins the game beside the dashboard ... Character Setup step 5 stands", where step 5 then read "Place an ember token beside the character's board" (Src 06). Audit A-052 proposed the supply; the chapter 03 issues list records it as superseded. Core17 l.367-372 and TG22: the token is not placed at setup. Ext, Holl: silent. Online: nothing found.
- Ruling: CHANGE
- Why: One token must have one starting place. The owning section and the approved completion both say beside the dashboard, which also shows at a glance who is not embered, so §6.1 is brought into line and §7.2 uses the same verb as §3.5.
- Mechanical: no
- Edits: core-E19, core-E20, core-E21, core-E22

---

## Part 4 — Chapter 04, equipment (8 items)

### core-020 · Ch 04 — the shield test
- Question: Does the definition "a one-handed weapon that shows block or resist dice and has no attack option" hold if a printed shield carries an attack option?
- This book now: that definition, used for stocking the shop and for the parry (§4.1, Card Types; §6.3; glossary Shield).
- Evidence: Core17 l.1178-1182: "shields and even weapons sometimes" show block and resist values, so block dice alone do not mark a shield. TG22 l.840: lists shields as a kind of equipment without defining them. Ext, Holl: no definition. Audit B-022 (the test adopted) and A-069 (a test by "shield icon", which no supplied card text confirms exists). Online: card texts of individual shields were not found.
- Ruling: CONFIRM as written
- Why: The test reads only what is printed on the card, needs no judgement of the artwork, and always gives an answer. If a shield does print an attack option, the rule still works: that card is a weapon, is stocked as a weapon, and does not permit a parry. That outcome is acceptable and needs no extra sentence. A test by name fails on cards such as the Shield Crossbow.
- Mechanical: no
- Edits: none

### core-021 · Ch 04 — where a consumed ember card goes
- Question: Is a consumed ember card removed from the game or returned to the shop?
- This book now: the character "discards" it; no destination is stated (§4.4; §7.3 step 1). A sold or surplus ember card returns to the tier one shop (§11.4; §7.3).
- Evidence: Core17 l.575-586: an ember card is found in the deck and spent at once; a surplus one is shuffled back. TG22 l.868-870: resolve it or keep it. Ext l.86 and l.95: ember cards are split between two decks. Holl l.189-192 and l.288-293: embers are shuffled into the decks and raise the spark dial. None has a card that returns after use. Src 04 (audit A-046): "limited supply". Online: nothing found.
- Ruling: ADD
- Why: The book fixes the supply at one ember card per character and never restocks it; that scarcity is the whole control on embering by card. If a used card went back on the shelf, every rest would sell a second estus flask for two souls. So a used card leaves the game, and the rule says so in the two places that describe the act and in the glossary. A sold or surplus card is unused and rightly goes back to the shelf.
- Mechanical: no (it states what "discard" already implied)
- Edits: core-E23, core-E24, core-E25

### core-022 · Ch 04 — dependency: §6.3 holds the ember stocking rule
- Question: Does §6.3 state in full that ember cards are added at setup only, stay if unsold, and are never restocked?
- This book now: §6.3, Stocking at the Start of the Game step 5 and Restocking After a Boss, first paragraph, state all three.
- Evidence: the text as it stands; audit A-046.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: The dependency is met.
- Mechanical: no
- Edits: none

### core-023 · Ch 04 — dependency: fixed modifiers in §9.4 and §10.3
- Question: Do §9.4 and §10.3 state how a fixed modifier is applied?
- This book now: §9.4 step 5 applies every fixed modifier after the two highest dice are added; §10.3 applies the attack modifier once to the total; the glossary entries Defence total and Attack value agree.
- Evidence: the text as it stands; audit D-033 and A-120.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: The dependency is met; the rules belong to another cluster.
- Mechanical: no
- Edits: none

### core-024 · Ch 04 — dependency: §11.4 cites §4.2 and §4.4
- Question: Does §11.4 cite the upgrade and ember rules and not restate them?
- This book now: §11.4, Upgrades ends by citing §4.2 for slots, requirements, Titanite and upgrade spells; Purchases cites §4.4 for the ember card.
- Evidence: the text as it stands.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: The dependency is met.
- Mechanical: no
- Edits: none

### core-025 · Ch 04 — a stored spell the character cannot equip
- Question: Can a character use a spell stored in a catalyst without meeting the spell's stat requirements?
- This book now: no; "a character who does not meet a stored spell's stat requirements cannot use it" (§4.3, Catalysts).
- Evidence: Core17 l.580-581 and TG22 l.850-851: requirements "must be met ... for a character to use that equipment card". Neither official ruleset stores spells in a catalyst; Ext and Holl likewise. CMP-0016: a stored spell is used "as if equipped". Online: nothing found.
- Ruling: CONFIRM as written
- Why: "As if equipped" brings the requirements with it, and a player would expect that a spell too demanding to equip is too demanding to cast. Any other answer would turn a catalyst into a way round the stat track.
- Mechanical: no
- Edits: none

### core-026 · Ch 04 — a spell card that bears the two-handed icon
- Question: If a spell card bears the two-handed weapon icon, does it still take one weapon slot?
- This book now: "Spells are never two-handed: a spell gains no two-handed reroll, and a spell equipped with the other weapon slot empty is not two-handed" (§4.3). §3.2's slot rule speaks of weapons, and a spell is not a weapon (§4.1).
- Evidence: Core17 l.567-570: a card with the two-handed icon requires the other hand slot to be empty; the rule is about the icon, not the kind of card. TG22 l.846-847: the card shows "the equipment slot the card goes in". Ext, Holl: silent. No supplied text shows whether any spell bears the icon. Online: nothing found.
- Ruling: ADD
- Why: Two different things were sharing one phrase. The slot a card needs is printed on it and is followed as printed; the reroll for two-handed wielding is a bonus that spells never get. One sentence separates them, so that a two-handed spell card, if one exists, has a definite rule. A spell stored in a catalyst takes no slot at all, as §4.3 already says.
- Mechanical: no
- Edits: core-E26

### core-027 · Ch 04 — glossary headword "Attack (major action)"
- Question: Is the headword duplicated by the chapter 10 delta?
- This book now: one entry, "Attack (major action)", in the glossary.
- Evidence: `12_glossary.md` as it stands.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Reconciled at integration.
- Mechanical: no
- Edits: none

---

## Part 5 — Chapter 06, setup (8 items)

### core-028 · Ch 06 — B-023's twelve-draw cap
- Question: Is the cap on stocking draws wanted?
- This book now: no cap (§6.3).
- Evidence: as core-002.
- Ruling: CONFIRM as written
- Why: Same ruling as core-002.
- Mechanical: no
- Edits: none

### core-029 · Ch 06 — when the fog gate goes on the mega-boss game board
- Question: Is the fog gate placed when the board is first laid, or only when it is flipped to its mega-boss side?
- This book now: only when the board is flipped (§6.7, The Mega-Boss Encounter, step 3).
- Evidence: BDK l.289-293 and EC l.324-328: after the Level 4 encounter the board is flipped, its doorway aligned with the bonfire tile, "and place the Fog Gate token on that doorway". Src 06 placed it at the Level 4 entrance. Audit A-095 and D-014 follow the booklets. Core17, TG22, Ext, Holl: no mega-boss setup. Online: nothing found.
- Ruling: CONFIRM as written
- Why: The official booklets place it at the flip, and in this book the token has a second job: the first passage moves it to the bonfire tile as a shortcut (§15.1). On the Level 4 doorway it would mark an encounter that is not a boss and would fire the shortcut early.
- Mechanical: no
- Edits: none

### core-030 · Ch 06 — first-leg tile layout
- Question: Grid or line?
- This book now: grid for the first leg, line for the second (§6.5; §6.6).
- Evidence: as core-008.
- Ruling: CHANGE
- Why: Same ruling as core-008: one chain rule for both legs, with the grid kept as a permitted chain.
- Mechanical: no
- Edits: core-E05, core-E06, core-E07 (under core-008)

### core-031 · Ch 06 — one character per player
- Question: May one player control several characters?
- This book now: "Each player chooses one character" (§6.1); "Each player controls one character" (§1).
- Evidence: Core17 l.367: "Each player should select one character"; a lone player has one character and a larger starting cache (l.632-636). TG22: one character each. Ext, Holl l.111: one class each. Src 06: "character dashboard(s)". Online: playing two characters alone is a common habit, with no rule attached.
- Ruling: CONFIRM as written
- Why: Both official rulebooks say one each, and every rule in this book that scales (enemy health, sparks, the lone character's souls) counts characters, not people. A person who wants to run two characters takes two seats and no rule is strained. Writing a permission would add a sentence to two chapters and make "player" and "character" drift apart in the PvP and joining rules.
- Mechanical: no
- Edits: none

### core-032 · Ch 06 — cross-chapter dependencies
- Question: Are the dependencies listed for chapter 06 met?
- This book now: §4.1 defines the shield by the B-022 test (met; see core-020). §12.2 owns invader token placement and the one invasion per leg (met). §7.7 states that the dealt card is the reward and how a contested card is awarded (met). §18.1 owns campaign Level 4 placement and §18.6 agrees with §4.4 that no ember card enters after setup (met).
- Evidence: the texts as they stand.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: All met.
- Mechanical: no
- Edits: none

### core-033 · Ch 06 — repeated glossary ADD lines
- Question: Do the repeated ADD lines for seven headwords need action?
- This book now: one entry for each headword in `12_glossary.md`.
- Evidence: the glossary as it stands.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: A note about the merge tool; the merge is done.
- Mechanical: no
- Edits: none

### core-034 · Ch 06 — tile side chosen by the party; spare cards to the box
- Question: Does the party choose which side of each encounter tile is face up at the first layout, and do unused ember cards and unselected boss treasure go back to the box?
- This book now: yes to both (§6.5, Encounter Tiles step 2; §6.2; §6.3).
- Evidence: Core17 l.295-300: tiles are shuffled and laid "in any way you wish"; nothing on sides. Src 06: the tiles are flipped "to the opposite side" for the second leg, so the first choice fixes both. TG22, Ext, Holl: silent. Online: nothing found.
- Ruling: CONFIRM as written
- Why: A free choice needs no procedure, and the face of a tile carries little weight once the encounter card decides what stands on it. Sending unused cards to the box is housekeeping that a player would do unprompted.
- Mechanical: no
- Edits: none

### core-035 · Ch 06 — where a sold boss treasure card goes
- Question: Does §11.4 say where a sold boss treasure card goes?
- This book now: "A sold boss treasure card is returned to the game box" (§11.4, Sales; §22.4; glossary Boss treasure).
- Evidence: audit A-077; §6.2 (boss treasure enters neither deck).
- Ruling: CONFIRM as written
- Why: A card that belongs to no deck has no deck to return to, and the box is the only other place. See core-047.
- Mechanical: no
- Edits: none

---

## Part 6 — Chapter 07, gameplay (10 items)

### core-036 · Ch 07 — encounter scry: where the replaced card goes
- Question: When a scry replaces a face-down encounter card, where does the old card go, and are the encounter decks kept for the purpose?
- This book now: the revealed card goes face down to the bottom of the encounter deck of its level, and the top card of that deck takes its place (§7.5, Encounter Resolution). §6.5 builds the decks and deals from them but does not say they stay on the table.
- Evidence: Core17 l.756-759: a gravestone gives information about the boss only. TG22 l.954-960: a gravestone lets the party look at the top card of a deck. Ext, Holl l.353-357: other uses. Src: the scry is the author's own and names no destination. Online: nothing found.
- Ruling: CONFIRM as written
- Why: The bottom of the deck is where the treasure scry and the boss scry already send a rejected card, so one rule serves all three. One clause is added to §6.5 so that the decks the scry draws from are still on the table.
- Mechanical: no
- Edits: core-E29

### core-037 · Ch 07 — boss-behaviour scry: is there a deck to look at?
- Question: Is the next boss's behaviour deck built before a gravestone encounter can scry it?
- This book now: the mini-boss's deck is built at §6.5, Encounter Tiles step 7 and the main-boss's at §6.6 step 10. The mega-boss's deck is not built until the game board is flipped (§6.7, The Mega-Boss Encounter step 4), after the Level 4 encounter has been resolved.
- Evidence: §7.5, Encounter Resolution step 5; BDK and EC: Level 4 cards place terrain, gravestones included. Core17 l.756-759: gravestones reveal boss behaviour at the start of the boss encounter. Ext, Holl: silent. Online: nothing found.
- Ruling: ADD
- Why: The item is settled for the first two bosses. It is still open for the third: a Level 4 encounter with a gravestone grants a scry of a deck that does not yet exist. Building the mega-boss's deck during the setup after the main-boss, as the other two decks are built during their setups, closes the gap with a clause and makes the three setups alike.
- Mechanical: no
- Edits: core-E30

### core-038 · Ch 07 — enemy turn-order tie-breaks are owned by §7.5
- Question: Does §9.1 cite §7.5 for the tie-breaks?
- This book now: §7.5, Encounter Turn Order states them; the dependency is editorial.
- Evidence: Core17 l.1112-1115: players choose the order of enemies with equal threat. The longer chain (nearest, most wounded, players' choice) is the author's (Src 07).
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: A note about which section states the rule. The rule is not in question.
- Mechanical: no
- Edits: none

### core-039 · Ch 07 — the scry procedure lives in §7.5
- Question: Is the scry stated once?
- This book now: in §7.5 only; §5.5 keeps the trigger and a cross-reference (resolved at integration, CH-05-033).
- Evidence: the texts as they stand.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Resolved at integration.
- Mechanical: no
- Edits: none

### core-040 · Ch 07 — an ember card held by a character who becomes embered
- Question: What happens to an ember card held by a character who becomes embered, for example when a boss falls?
- This book now: it must be given at once to a character who is neither embered nor holding one; if there is none, it returns to the tier one shop (§7.3).
- Evidence: Core17 l.584-586: a surplus ember card is shuffled back into the deck and replaced. TG22: silent. Ext, Holl: silent. Audit A-007 (the fix adopted; its alternative was the game box). Online: nothing found.
- Ruling: CONFIRM as written
- Why: The card is unused, so it stays in the game, and the shop is where unused ember cards live. That is the same rule as for a sold ember card. Where a used card goes is settled in core-021.
- Mechanical: no
- Edits: none

### core-041 · Ch 07 — sharing out the cards dealt to a tile
- Question: Do the players choose who takes which of the dealt cards, or are they dealt at random?
- This book now: the players decide; if they cannot agree, the character holding the aggro token decides (§7.7).
- Evidence: Core17 l.647-652 and TG22 l.1353: treasure goes to a shared inventory and any character may take it. Gate 1 OQ-29: contested treasure to the aggro holder everywhere. Ext, Holl: shared inventory. Online: nothing found.
- Ruling: CONFIRM as written
- Why: Characters may already trade cards one for one outside an encounter (§3.2), so a random deal would be undone by a trade a moment later. Choosing together is what a cooperative table does anyway, and one tie-break used everywhere is easier to remember than a second one for this case. One clause is added so that the cards are turned face up before they are shared out.
- Mechanical: no
- Edits: core-E16

### core-042 · Ch 07 — invaders, clearing, and invader treasure
- Question: Must an invader be killed for the encounter to be cleared, and who receives its treasure?
- This book now: §7.5 says an encounter is cleared when every enemy model has been killed; §12.2 owns the invader's part (lead item 2).
- Evidence: Phantoms l.525-533 (the official award); the rest belongs to the cluster that owns chapter 12.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Nothing in chapter 07 depends on the answer: the sentence in §7.5 stands whichever way §12.2 is ruled, and §7.7 already awards an invader's card as §12.2 directs.
- Mechanical: no
- Edits: none

### core-043 · Ch 07 — does a Level 4 encounter reset?
- Question: Does a cleared Level 4 encounter reset when the characters rest?
- This book now: no; once cleared it is not fought again, and a failed one resets as any other (§6.7; §7.5; §11.5; §22.4).
- Evidence: BDK l.216-219 and EC l.249-252: "Once it is defeated, you cannot complete the level 4 encounter again." Core17, TG22, Ext, Holl: no Level 4. Audit A-123 recorded the manuscript's silence; CMP-0023 adopted the official rule. Online: nothing found.
- Ruling: CONFIRM as written
- Why: It matches the official booklets, it keeps the last paid rest before the mega-boss from costing a second run at the hardest encounter, and it removes any reason to fight that encounter again for souls.
- Mechanical: no
- Edits: none

### core-044 · Ch 07 — where a revived character stands
- Question: Must a revived character be placed on a particular node?
- This book now: "upright on the tile beside the surviving characters" (§7.5, Encounter Recovery).
- Evidence: Holl l.381-383: revived characters return to the node they entered from, because a mimic may follow. Core17, TG22: no revival within an encounter. Ext: silent. Online: nothing found.
- Ruling: CONFIRM as written
- Why: Recovery happens only after the tile's fighting is over. If a mimic is to be fought, recovery is put off until afterwards (§7.5; §13), so the revived character's node never matters. The next encounter places every character afresh on entry nodes. A node rule here would decide nothing.
- Mechanical: no
- Edits: none

### core-045 · Ch 07 — hollow cubes: colour and source
- Question: What are the hollow cubes?
- This book now: unsourced cubes of a distinct colour (§7.2).
- Evidence: as core-001.
- Ruling: CHANGE
- Why: Same ruling as core-001: white cubes from the core set, with a stated fallback.
- Mechanical: no
- Edits: core-E01 to core-E04 (under core-001)

---

## Part 7 — Chapter 11, returning to the bonfire (13 items)

### core-046 · Ch 11 — a sold ember card
- Question: May an ember card be sold, and where does it go?
- This book now: it sells as a tier one card (one soul) and returns face up to the tier one shop, where it costs two souls (§11.4).
- Evidence: Neither official ruleset has selling. Ext, Holl: no selling. Src 11: sold cards go "to the bottom of their respective treasure deck", and an ember card has none. Online: nothing found.
- Ruling: CONFIRM as written
- Why: The alternative is a second card that cannot be sold, beside starting equipment. Letting the sale stand and sending the card back to the shelf is the answer a player would guess, costs the seller a soul, and keeps the number of ember cards in the game fixed.
- Mechanical: no
- Edits: none

### core-047 · Ch 11 — sold boss, legendary and transposed treasure
- Question: Where do sold boss, legendary and transposed treasure cards go, and what do they fetch?
- This book now: boss treasure, six souls and the game box; legendary and transposed treasure are tier two cards, one soul and the bottom of the tier two deck; in campaign play a legendary card fetches four (§11.4; §18.6).
- Evidence: no official or community rule on selling. Src 11: boss treasure sells for six. §6.2 shuffles five legendary cards and all transposed cards into the tier two deck. Audit A-077 proposed the game box for sold legendary cards. Online: nothing found.
- Ruling: CONFIRM as written
- Why: Every sold card goes back where cards of its kind live. Legendary and transposed cards live in the tier two deck, so they go to its bottom; boss treasure lives in no deck, so it goes to the box. That is one principle with no special case, and it is the same principle core-048 applies to Titanite.
- Mechanical: no
- Edits: none

### core-048 · Ch 11 — Titanite on a sold weapon
- Question: Does attached Titanite add to the sell value, and where does it go?
- This book now: the weapon's value is paid once and Titanite adds nothing; "the Titanite goes with the weapon to the bottom of the treasure deck of the weapon's tier" (§11.4; §4.2; glossary Titanite).
- Evidence: Src 11: "Titanite upgrades ... attached to sold weapons are returned to the bottom of the tier one treasure deck", that is, to the Titanite's own deck. Appendix B, Titanite Replacement: a replaced Shard returns to the tier one deck and a replaced Chunk to the tier two deck, each to its own. Core17 l.672-679: a weapon upgrade is never removed. No official or community rule on selling. Online: nothing found.
- Ruling: CHANGE
- Why: The value half is confirmed: one price, nothing added. The destination half is changed. As drafted, a Titanite Shard on a tier two weapon is buried in the tier two deck and the two cards sit there fused, while the same Shard replaced by a Chunk goes to the tier one deck. Parting the cards at the sale and sending each to the place of its own kind is what the author wrote, agrees with Appendix B, and needs no rule of its own: it is the general rule for sold cards applied twice.
- Mechanical: yes (which deck a sold Titanite card returns to)
- Edits: core-E31, core-E32, core-E33

### core-049 · Ch 11 — Andre's upgrade service
- Question: Is attaching and removing upgrades free and unlimited during a rest, and must the card be equipped when the upgrade is attached?
- This book now: yes to all three; Titanite is the one upgrade Andre does not remove (§11.4, Upgrades; §4.2).
- Evidence: Core17 l.671-679: "does not have a soul cost"; armour upgrades are freely added and removed, weapon upgrades never removed. TG22 l.2062-2089: upgrades go on "items on their dashboard", cost nothing, and "can be removed ... at any time during this step". Holl l.196-206: free; weapon upgrades replaced, never removed. Ext: silent. Src 11: upgrades go on "equipped" cards. Online: nothing found.
- Ruling: CONFIRM as written
- Why: Free service is the official rule in both editions. Requiring the card to be equipped is the official wording too, and it is the plainest way to make the character meet the upgrade's requirements. The book sits between the two editions on removal (only Titanite is permanent), which keeps one meaningful permanent choice without freezing every gem.
- Mechanical: no
- Edits: none

### core-050 · Ch 11 — returning to the bonfire without resting
- Question: May the party go back to the bonfire tile and not rest?
- This book now: yes. "Returning to the bonfire tile costs nothing ... Until the party rests, no character is restored, the Firekeeper and Andre cannot be visited, and no encounter is reset" (§11.1; glossary Bonfire). §7.5, Encounter Recovery offers only two choices after a clear: advance, or "return to the bonfire tile and rest, spending one spark".
- Evidence: Core17 l.623 and l.690-706: the party returns freely and may shop without resting; resting is a separate choice. TG22 l.1927-1930 and l.2075-2079: "When the party returns to the bonfire ... Turn the spark dial down one number"; "Each time they return to the bonfire, they'll use up a spark." Src 11: "The characters must collectively spend one spark to visit the bonfire". Ext l.31-35: no return without death. Holl l.166-176: return at will, rest included. Online: the gamerant article describes "farming rooms" as a house rule that groups must police by hand.
- Ruling: CHANGE
- Why: A free return did something in the 2017 rules, because the shop was open without a rest. Here nothing can be done at the bonfire without resting, so the state has only one use: a party walks back for nothing, sets out again, and fights encounters it has already cleared for the reduced reward, as often as it likes and without spending a spark. That is the grind this edition was built to remove. The author's text, the current official rules and §7.5 all say the same simpler thing: to go back is to rest. One rule fewer, and the loophole is closed.
- Mechanical: yes (the party can no longer return without resting)
- Edits: core-E35, core-E36, core-E37

### core-051 · Ch 11 — the free rest and PvP
- Question: In what order do a boss's defeat, the PvP encounter, the setup and the free rest fall?
- This book now: boss, PvP encounter, setup, free rest (§11.2; §16.5 steps 6 and 7; §6.6 step 18; §6.7 step 9; §20.9).
- Evidence: Core17 l.707-710: after the mini-boss the tiles are set up and the characters "rest at the bonfire (without using a spark)". TG22 l.2299-2300: the same. No official PvP. Src 11 and Src 20. Online: nothing found.
- Ruling: CONFIRM as written
- Why: The four sections agree, and the order is the natural one: the PvP encounter is fought on the boss's tile before that tile is cleared away, and the rest comes last so that it heals whatever the PvP encounter did.
- Mechanical: no
- Edits: none

### core-052 · Ch 11 — the restock step inside the rest
- Question: Does a rest need a step that restocks the shop "if the shop has not been restocked since a boss was last defeated"?
- This book now: §11.2 step 7, with two sentences in §11.2 and one in §18.6 that explain when it applies.
- Evidence: §6.6 step 16 and §6.7 step 7 restock during the setup after a boss, before the free rest; §18.6 restocks "during the setup of the next section and before the rest that follows". Core17, TG22: no stocked shop. Chapter 11 issues list, item 7: the step "is worded to do nothing once that restock has happened". Online: nothing found.
- Ruling: DELETE
- Why: The condition is never true. Every restock in the book, standard or campaign, happens during a setup that comes before the rest, so the step does nothing and exists only to be explained. Removing it shortens the rest to eight steps and leaves restocking stated once, where it belongs.
- Mechanical: no
- Edits: core-E09, core-E10, core-E11

### core-053 · Ch 11 — souls spent outside a rest
- Question: Is the summon's cost the only payment made outside a rest, and do §7.6, §11.3 and §12.1 agree?
- This book now: yes; all three state the rule and the one exception.
- Evidence: Phantoms l.205-210: the official summon is paid for by giving up the encounter's souls, also at the fog gate. Ext l.44-47: two souls per player, paid during the encounter. Src 11 and audit A-100. Online: nothing found.
- Ruling: CONFIRM as written
- Why: The summon is chosen at the fog gate, when the party knows who is embered, so it has to be paid there. One named exception, stated the same way in three places, is as tidy as this can be.
- Mechanical: no
- Edits: none

### core-054 · Ch 11 — souls cannot be pooled
- Question: Do §11.3 and §7.6 agree, and is the bonfire ascetic stated as the exception?
- This book now: yes; §18.7 states the exception and §22.1 repeats it.
- Evidence: Core17 l.630-636 and TG22 l.1035-1037: the official game has one shared soul cache. Holl l.228-232: individual and shared souls. Src 07: "Souls cannot be transferred between characters." Online: nothing found.
- Ruling: CONFIRM as written
- Why: Personal souls are the author's design and the reason death and dropped souls matter to each player. The one shared payment is in campaign play and is labelled as the exception.
- Mechanical: no
- Edits: none

### core-055 · Ch 11 — resetting a failed boss encounter
- Question: Does §15.2 say how a failed boss encounter is reset?
- This book now: §15.2 states it and §15.5, Deck Reset rebuilds the behaviour deck; §11.5 cites §15.2.
- Evidence: the texts as they stand.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: The dependency is met; the rule belongs to another cluster.
- Mechanical: no
- Edits: none

### core-056 · Ch 11 — invaders and mimics at a reset
- Question: Do §12.2 and §13 say what happens to an invader, an ambush card and a mimic's chest at a reset?
- This book now: §12.2 (an invader that has appeared does not return) and §13.3 and §13.4 (a killed mimic's chest is not placed again; a failed mimic encounter returns the chest) state them; §11.5 cites §12.2.
- Evidence: the texts as they stand.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: The dependency is met. One small gap for the owner of chapter 13 is noted under cross-cluster effects: §11.5 step 4 and §5.5 say terrain stays through a reset without mentioning the mimic's chest.
- Mechanical: no
- Edits: none

### core-057 · Ch 11 — D-011, the Firekeeper's luck purchase
- Question: Is the dropped purchase intended?
- This book now: not included.
- Evidence: as core-006.
- Ruling: CONFIRM as written
- Why: Same ruling as core-006.
- Mechanical: no
- Edits: none

### core-058 · Ch 11 — glossary entries Starting equipment and Fog gate
- Question: Do the two glossary notes need action?
- This book now: Starting equipment reads "cannot be sold (see §11.4)"; Fog gate is owned by §15.1.
- Evidence: `12_glossary.md` as it stands.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: Both were settled at integration.
- Mechanical: no
- Edits: none

---

## Part 8 — Chapter 23, appendices (12 items)

### core-059 · Ch 23 — Butcher Knife
- Question: 24 STR or 28?
- This book now: 24/0/0/0, tier one.
- Evidence: as core-005.
- Ruling: CONFIRM as written
- Why: Same ruling as core-005.
- Mechanical: no
- Edits: none

### core-060 · Ch 23 — the Tier column and unlisted treasure types
- Question: May Appendix A give a tier computed from requirements when no source lists each card's treasure type?
- This book now: the column is computed; the section Treasure Type says that transposed and legendary cards are tier two whatever the column shows and that boss treasure enters neither deck.
- Evidence: TG22 l.2287-2289: Black Knight Halberd, Black Knight Shield and Blue Titanite are the Black Knight's treasure cards. Core17 l.560-562: each card prints its treasure type. Ext, Holl: no list. Online: no card list could be fetched.
- Ruling: CONFIRM as written
- Why: The card in the player's hand prints its type, and the rule of §6.2 sorts by type first. The column is a help for the common case and the section beneath it handles the rest. All 61 rows agree with the rule of 25.
- Mechanical: no
- Edits: none

### core-061 · Ch 23 — the grouping of Additional Treasure
- Question: Should the 34 added cards be grouped by kind, and is the second group boss treasure?
- This book now: one alphabetical table; each card "is sorted during setup by the treasure type marked on it".
- Evidence: TG22 l.2287-2289 confirms three of the ten cards in the source's second group as the Black Knight's treasure. The other seven fit the three remaining bosses of Appendix B by name (Gravelord Sword and Gravelord Sword Dance; Priscilla's Dagger and Lifehunt Scythe; Greatsword, Tower Shield and Steel Armour), but no supplied text confirms them.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: The cards say what they are, and the appendix tells the player to follow the card. A grouping the sources cannot confirm would add a claim without adding a rule.
- Mechanical: no
- Edits: none

### core-062 · Ch 23 — Demon Titanite listed without a change
- Question: Was an amendment to Demon Titanite intended?
- This book now: "Replace the printed card with the revised card. The rules text, stat requirements, and treasure type are unchanged."
- Evidence: Src 23: listed with no note. No official or community text describes the card. Online: nothing found.
- Ruling: CONFIRM as written
- Why: With no note from the author there is nothing to amend, and the row says so plainly. The one thing the book must decide about the card, whether it is Titanite, is settled in core-063.
- Mechanical: no
- Edits: none

### core-063 · Ch 23 — are Demon Titanite and Blue Titanite "Titanite"?
- Question: Do Demon Titanite and Blue Titanite fuse permanently, as the four named Titanite cards do?
- This book now: §4.2 and the glossary name four Titanite cards (Shard, Chunk, Slab, Scale); the appendix does not call the other two Titanite, so as drafted Andre removes them freely.
- Evidence: Core17 l.672-679: no weapon upgrade is ever removed, so both cards were permanent as printed. TG22 l.2088-2089: every upgrade may be removed. CMP-0004 labels both "Weapon upgrade (Titanite)". Holl l.196-200: weapon upgrades "cannot be removed, only replaced". Ext: silent. Online: nothing found.
- Ruling: CHANGE
- Why: A player holding a card called Blue Titanite will read the heading "Titanite" and take it to apply. A test by name ("a weapon upgrade card whose name includes the word Titanite") is the rule that player would guess, needs no list to be kept up to date, and matches how both cards behaved in the first edition. The replacement chain of Shard, Chunk and Slab is untouched.
- Mechanical: yes (Demon Titanite and Blue Titanite can no longer be removed once attached)
- Edits: core-E34 (and the glossary entry in core-E33)

### core-064 · Ch 23 — Mon Ring, "one use per floor"
- Question: Is the Mon Ring used once between rests, or once on each leg of the journey?
- This book now: once between rests; the card is turned face down when used and face up at each rest.
- Evidence: Holl l.484: "Mon Ring can now be used once per floor", and l.58-60: "A floor is the series of encounters leading up to and including a boss." Src 23 took the phrase from there. Core17, TG22, Ext: no such limit. Online: nothing found.
- Ruling: CONFIRM as written
- Why: The source's "floor" is a leg, so once per leg is the literal reading. But this book has no word for a leg in its rules and already has one refresh moment for everything that is used once: the rest. Tying the ring to the rest gives it the same clock as the luck, estus flask and heroic action tokens (core-011), and a turned card is an obvious reminder. If the author wants the stricter reading, the last sentence of the row becomes "each time a boss is defeated".
- Mechanical: no
- Edits: none

### core-065 · Ch 23 — Chloranthy Ring
- Question: Does the ring give one stamina to everyone on the wearer's node at the start of the wearer's turn, or one more to each of them at the start of their own turns?
- This book now: at the start of each of the wearer's turns, the wearer and every other character on the wearer's node each recover one stamina.
- Evidence: Core17 l.660-664 (caption): the ring helps "characters on the same node gain extra stamina every turn". Holl l.475-478: the ring raises the gain "to 2 instead of 1 at the beginning of activation for all players on that node". Src 23: two notes, merged by CMP-0004. Ext: silent. Online: nothing found.
- Ruling: CONFIRM as written
- Why: One trigger at one moment is easier to run than a check at the start of every character's turn, and the wearer still gains two, as both sources say. The frostbite question the item raises is already answered by §8.5 and §22.3: a character with a frostbite token recovers no stamina by any means, the ring included.
- Mechanical: no
- Edits: none

### core-066 · Ch 23 — Black Leather Armour and Eastern Armour
- Question: Which printing's dice and requirements are used?
- This book now: "Where two printings of the card exist, the printing that carries this text is used."
- Evidence: no supplied source gives either printing's values.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: The row is a definite instruction to a player who holds the cards, and nothing more can be said without them.
- Mechanical: no
- Edits: none

### core-067 · Ch 23 — printed names
- Question: Are "Four-Pronged Plough", "Sellsword Twinblades" and "Onikiri and Ubadachi" spelt as the cards print them?
- This book now: those three spellings.
- Evidence: Gate 1 OQ-17: proper nouns on cards keep their printed spelling. §2.2 prints "Plow Scarecrow" for the enemy of the same expansion. Online: the card images could not be reached.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: A proofing check against the cards. See "Not settled", item 2, for the likely answer on the first name.
- Mechanical: no
- Edits: none

### core-068 · Ch 23 — pointers from the chapters to the appendices
- Question: Do the chapters that depend on the appendices cite them?
- This book now: §4.2 cites Appendix B for Titanite replacement, and the glossary entry Stat requirement cites Appendix A. §4.1 (Stat Requirements), §6.2 and §10.5 cite neither.
- Evidence: the texts as they stand; chapter 23 issues list.
- Ruling: ADD
- Why: As drafted, a reader of the rules for equipping a card or building the decks is never told that some printed requirements are replaced and some cards added. One sentence in §4.1 and one in §6.2 repair that. §10.5 belongs to another cluster and is listed under cross-cluster effects.
- Mechanical: no
- Edits: core-E27, core-E28

### core-069 · Ch 23 — treasure totals
- Question: Does the total of 534 treasure cards in §2.5 include the 34 added cards?
- This book now: 534, with no statement either way.
- Evidence: no supplied source lists the cards; chapter 02's own issues list records that the totals cannot be reconciled.
- Ruling: NOT A RULES QUESTION (informational, nothing to decide)
- Why: A count that only the components can settle. No rule depends on it.
- Mechanical: no
- Edits: none

### core-070 · Ch 23 — A-066, weapons with no stat requirement
- Question: Should a weapon whose highest requirement is zero be barred from scaling?
- This book now: §10.5 has no such bar, so a weapon with no requirement is scaled for any character whose stat is five or more. No weapon in Appendix A has a highest requirement of zero.
- Evidence: Core17, TG22: no scaling. Ext, Holl: no scaling. Audit A-066. Online: nothing found.
- Ruling: ADD
- Why: For the appendix there is nothing to do. For §10.5, a view for its owner: scaling rewards a character for growing past a weapon's demand, and a weapon that demands nothing gives every character that reward from the first turn, which turns a bonus into a flat +1 on the weakest cards. One short sentence ("A weapon whose stat requirements are all zero is never scaled") closes it. The edit belongs to the cluster that owns chapter 10.
- Mechanical: yes, if the owner of §10.5 adopts it
- Edits: none (cross-cluster)
