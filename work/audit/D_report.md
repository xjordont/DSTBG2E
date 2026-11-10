# Audit D — Homebrew Delta Report

Outputs: `work/audit/D_delta_table.md` (132 rows), `work/audit/D_rows.csv` (41 rows, D-001…D-041), this report. All manuscript references are line numbers in `work/docx/manuscript.md`; official and homebrew references are file name and page (pdftotext page split) in `work/text/`.

## 1. Method

1. Read the full manuscript body (lines 361–3366) and built a topic checklist (components; dashboards and slots; stats; endurance bar; tokens; equipment, upgrades, spells; tiles, nodes, range, terrain; setup; objective; death and hollowing; embers; sparks; encounter start, turn order, resolution, recovery; souls; combat basics, scaling, pushing, conditions; enemy turn; character turn; attacks; bonfire, Firekeeper, Andre; summons; invaders; mimics; crystal lizards; boss encounters and turns; boss special rules; campaign play; campaigns; PvP; Community Update Pack).
2. Read the 2017 core rulebook (41 pp.), the 2022 Tomb of Giants rulebook (33 pp.), the FAQ, all seven expansion booklets, Hollowed Edition v1.3 and Extended Rules V45 in full (the Extended "Revised Rules", "Rule Variations", scenarios and Combat Cards sections; its encounter and weapon-art lists were scanned by keyword only).
3. For each topic recorded the manuscript rule, the 1E rule, the V2 rule, the nearest homebrew source, and whether the manuscript combines halves from different sources (hybrid). Where a manuscript sentence reproduces official wording, the row says "verbatim" or "near-verbatim" for Agent F.
4. Component lists were reconciled arithmetically against Core p.4–7, V2 p.4–6 and each expansion's Contents page. Sets not supplied (Painted World of Ariamis, Asylum Demon, Four Kings, Gaping Dragon, Guardian Dragon, Manus, Old Iron King, Vordt) are marked unverifiable.
5. CSV rows were raised only for incompatible or unreconciled hybrids, silently dropped official rules that leave a hole, component discrepancies, and deviations that are incompletely specified relative to the rule they replace. Deliberate, coherent deviations are listed in the Preserve list and are not CSV rows.

## 2. Lineage proportions

Counted by primary lineage of the 132 delta-table rows (one row = one rule topic; rows are not weighted by prose length):

| Lineage | Rows | Share | What it covers |
|---|---|---|---|
| Official 1E core (incl. campaign rules and FAQ) | 58 | 44% | Tiles, nodes, range, pushing, enemy movement icons, attack icons, boss data/behaviour/arcs/movement, campaign framework, stat costs, most structural prose |
| Original to manuscript | 33 | 25% | Round-based turn order, damage-based aggro, enemy scaling, parry/riposte, two-handed reroll, stat scaling, spells/catalysts, shop stocking and restock timing, treasure pre-deal, event cards, bonfire ascetic, transposition, PvP, invader cadence, mega-boss death |
| Hollowed Edition | 14 | 11% | Block = two highest dice, failed dodge → armour-only block, bleed, hollowing, individual souls, soul-reward scale, solo 6 souls, rest major action, forgo-the-chest mimic choice, push priority, CUP errata items |
| Official expansions (Phantoms, Explorers, Iron Keep, Darkroot, BDK/EC) | 14 | 11% | Invader tokens and setup, mimic procedure, crystal lizards, level 4 / mega-boss setup, Calamity, 0-difficulty dodge, campaign lists |
| Official V2 (Tomb of Giants) | 9 | 7% | Backup slot of two any-type cards, equipment card anatomy, four token types, ember discard on death, frostbite wording, scrying, fog-gate shortcut, +1 spark and ember on boss death |
| Extended Rules | 3 | 2% | Treasure split at stat 25 into two decks, 2 souls per player summon cost, skipping cleared tiles |
| None (hole) | 1 | 1% | Enemy attack targeting (dropped) |

Reading: the skeleton and most explanatory prose are 1E; the combat feel (defence, death, souls, action economy) is Hollowed; the component conveniences (backup slot, card anatomy, shortcut, boss-death rewards) are V2; the economy (shop, treasure tiers, scaling, scrying trigger, event cards) is the author's own. Extended Rules contributed only the two-deck treasure split and the summon price. 38 rows are hybrids.

## 3. Hybrids and compatibility verdicts

Incompatible or unreconciled (CSV rows raised):
1. **Event cards** (rows 10, 52; D-001) — V2-style levelled event cards dealt to 1E tiles with no rule anywhere stating their effect. Incompatible: nothing to resolve. Blocker.
2. **Summon turn cadence** (row 100; D-002) — Extended's 2-souls-per-player price and the official random draw, but the phantom acts "after all character turns and before the first enemy turn", a phase that exists only in the manuscript's round-based standard encounters; summons appear only in boss fights, which keep 1E alternation. Incompatible as written; adopting the official Phantoms cadence (after each character) resolves it.
3. **Gravestone "not flipped"** (row 38; D-003) — V2 two-sided gravestone vestige on 1E single-sided tokens. Harmless but incoherent; delete.
4. **Mega-boss permanent death** (row 56; D-007) — original sudden-death rule bolted onto the official mega-boss setup, contradicting the manuscript's own loss condition. Needs a decision.
5. **Stat tier four** (row 99; D-005) — HE red-cube marker, 1E cost column with a duplicated "8", and an original "+5" value that matches neither 1E (40) nor HE (40) and that the manuscript's own campaign table (20 souls, from Core p.33) implicitly contradicts. Needs a decision.
6. **Boss push-off-arc** (row 111; D-004) — pre-FAQ Core p.28 text plus an original "centre-most node" clause, where the FAQ ruled that attack pushes ignore arcs. Minor; author's choice.
7. **Shop composition on official card types** (row 45; D-006, filed as underspecified) — original fixed-composition shop uses categories (shield, spell) that are not official card types; needs a classification rule.
8. **Traps** (row 42; D-009, filed as dropped rule) — 1E placement kept, resolution dropped, "all models on that node" contradicts 1E's "no effect on enemies".

Compatible hybrids (no CSV row; noted for the author):
- Block = two highest dice (HE) with 1E dodge dice and original paid extra dice, plus HE armour-only block on a failed dodge (rows 86–87). Coherent: the HE cap makes heavy shields less dominant, which the manuscript wants. Only gap: fixed modifiers on defence (D-034, optional).
- Upgrades: V2 removability plus 1E permanence restricted to Titanite (row 29).
- Ember: 1E damage reduction + V2 discard-on-death + Phantoms invader trigger + original heal/un-hollow/summon gate (row 27).
- Death and hollowing: HE hollowing (capped at one stage) + 1E forced rest when a hollow dies (row 58).
- Souls: HE individual souls + 1E lost-if-you-die-again (row 67; "mastering" undefined, D-030).
- Treasure decks: Extended stat-25 split + 1E five legendaries + original inclusion of all class cards (row 44).
- Setup after mini-boss: 1E procedure with V2/1E-campaign "+1 spark" and HE "return dropped souls" (row 54).
- Node push priority: 1E limit + HE priority + original "boss does not count" (row 34).
- Poison: HE stacking + 1E one-token removal — harsher than either source but coherent (row 77).
- Stagger: HE attack penalty extended to defence rolls; doubles as overflow and parry penalty (row 79).
- Calamity: BDK −1 to defence rolls, HE persistence; BDK "removed on damage" dropped (row 80).
- Dodge: 1E stamina cost, expansion 0-difficulty auto-success, HE armour fallback, original paid dice and mandatory post-success move (row 87).
- Character turn: HE major/minor economy with original Rest-unless-run (rows 89–90). Ordering of minor vs major unstated (D-018).
- Mimics: Explorers procedure + HE "forgo the chest" + original "must be fought again" (row 105).
- Invaders: Phantoms tokens and setup + original after-each-character cadence + per-character souls (rows 101–104).
- Crystal lizards: Iron Keep + original per-kill award (row 106; supply gap D-029).
- Campaign shop: 1E prices + original restock-per-section, ascetic gate and transposition (row 126).
- Round-based standard encounters (original) alongside 1E alternation for bosses (rows 61, 112): deliberate asymmetry, compatible provided summon/invader cadence is stated for each (D-002).

## 4. Dropped official rules

| Official rule | Source | Manuscript status | Verdict |
|---|---|---|---|
| Enemy attack targeting (aggro/nearest icons, out-of-range miss, node attack) | Core p.25; V2 p.25 | Absent; 1706 defers to a section that does not exist | **Omission — hole** (D-008) |
| Trap resolution: suffer or dodge; unblockable; no effect on enemies; triggers once | Core p.18; V2 p.12 | Absent; replaced by "resolve its effect on all models" | **Omission — hole** (D-009) |
| Summon taunt level, Distract icon, special ability, death has no effect on party | PH p.6, p.9 | Absent | **Omission — hole** (D-010) |
| Initial fog gate placement | Core p.8 | Absent; later step says "as before" | **Omission — hole** (D-015) |
| Move-before-or-after-attack restriction | Core p.22; V2 p.20 | Replaced by minor/major list with no ordering rule | **Omission** (D-018; HE's free ordering is the likely intent) |
| Gargoyle double-fight footnote | Core p.35; PH p.17 | Absent | Omission (D-012) |
| Undead Colosseum special rules and section-6 level 4 | EC p.18–19 | Absent | Omission (D-013) |
| Level 4: four entry nodes; fog gate placed after L4 | BDK/EC p.8–9 | Absent / re-timed | Omission, minor (D-014) |
| Push-move: starting node not damaged | FAQ p.1 | Implicit only | Omission, minor (D-016) |
| Firekeeper restores luck for 1 soul | Core p.15 | Absent | Probably intentional, unacknowledged (D-011) |
| FAQ: attack push off a boss node ignores arcs | FAQ p.1 | Pre-FAQ text kept | Unacknowledged (D-004) |
| 1E activation order (First Activation token, clockwise) | Core p.19 | Replaced by threat order; token still placed | Intentional; vestige (D-019, D-040) |
| Any death = party defeated | Core p.19 | Replaced by hollowing | Intentional |
| Communal soul cache; 16 souls for solo | Core p.13 | Replaced by personal souls; 6 for solo (HE) | Intentional |
| Sparks reset after mini-boss | Core p.9 | Replaced by +1 spark | Intentional |
| Boss souls = 1 per character per spark | Core p.19 | Replaced by flat 6 | Intentional |
| Level 4 clear = 8 souls per character | BDK/EC p.8 | Replaced by 6 | Intentional |
| Treasure bought blind for 1 soul; drawn in pairs from chests | Core p.14, p.17 | Replaced by shop and single pre-dealt card | Intentional |
| Weapon upgrades permanent | Core p.14 | Replaced by V2 removability (Titanite excepted) | Intentional |
| Equipment changed only at Andre; backup holds weapons only | Core p.12, p.14 | Replaced by V2 backup and between-encounter swapping | Intentional |
| Luck rerolls one die | Core p.11; V2 p.9 | Replaced by any/all dice | Intentional |
| Estus removes stamina cubes as well | Core p.11; V2 p.9 | Replaced by damage only, major action | Intentional (text lives only in the DOCX footer — see intake §3.1) |
| Stamina recovery 2 (1E) / 3 (V2) | Core p.22; V2 p.20 | Replaced by 1 + Rest action (HE) | Intentional |
| Barrel: walk/run/dodge in for +1 stamina; souls per surviving barrel | Core p.17; V2 p.12 | Replaced by dodge/push only | Intentional |
| Gravestone: reveal boss cards at boss start | Core p.28 | Replaced by scrying on clear | Intentional |
| Campaign "Dashing Through" | Core p.33 | Replaced by stamina-cost skip | Intentional |
| Campaign spark purchase (2 souls per character) | Core p.33 | Explicitly removed (2236) | Intentional |
| Campaign sold treasure discarded | Core p.33 | Replaced by bottom of deck | Intentional |
| V2: upkeep "each other character can move one node"; combined dodge+block roll; objectives, keywords, timer, encounter track, levers/torch/shrine | V2 p.12, p.17–20, p.25 | Not adopted | Intentional (the Second Edition Notes reject V2's out-of-turn actions) |

Counts: 9 omissions leaving holes or needing text (D-008, D-009, D-010, D-012, D-013, D-014, D-015, D-016, D-018), 2 unacknowledged drops that may be intentional (D-004, D-011), 19 clearly intentional replacements.

## 5. Preserve list — deliberate, coherent homebrew design (do not "correct" towards official)

- Enemies act first; each round every enemy acts once, then every character once in descending threat; aggro moves to the round's top damage-dealer (1281–1295).
- Bosses alternate with each character, 1E-style; boss aggro moves to whoever damages it (2158, 2192).
- Invader acts after each character's turn and does not scale (2026–2028, 2020).
- Block/resist = sum of the two highest dice; failed dodge falls back to armour dice only (1722, 1759).
- Dodge: 1 stamina, +2 stamina buys one extra die to a maximum of four; success forces a move; difficulty 0 auto-succeeds (1736–1755).
- Parry and riposte (1768–1797).
- Character turn: recover 1 stamina; minor walk/run/equip/heroic; major attack/rest/estus/ember; Rest restores all stamina unless the character ran (1802–1834).
- Luck rerolls any or all dice (801).
- Two-handed (or lone one-handed) weapon rerolls one attack die (1877); stat scaling +1 at +10 over requirement (1881).
- Spells: one spell attack per turn; catalysts hold three spells; no scaling or two-handing (859–887).
- Enemy scaling by character count (health +1 each; move 1→2; +1 damage at 3+; repeat at 4) (1521–1584).
- Hollowing: one stage of two cubes; a hollow's death fails the encounter; removed by spark or ember (1205–1223).
- Partial recovery after a clear (one damage cube; all stamina; conditions); tokens not refreshed (1345–1355).
- Personal souls; rewards 3/4/5/6 per character (2/3/4/5 in campaigns); dropped souls reclaimed by clearing the tile (1385–1435, 2244).
- Shop: two tiers, fixed composition, buy 2/4, sell 1, boss treasure sells for 6 and is never bought; restock only after a boss; embers sold only in tier one (1065–1089, 1935–1957).
- Treasure split at stat requirement 25 into two tier decks; five legendaries in tier two; one treasure per character per first clear, pre-dealt to tiles (1013–1053, 1135).
- Skip a cleared encounter for 2 stamina per character; failed encounters cannot be skipped once reset (1261, 1339).
- Scrying on clearing an encounter with a gravestone (933–943); fog gate moves to the bonfire as a shortcut (2066).
- Boss death: +1 spark, ember token each, free rest; one random boss treasure (2196, 1479).
- Mimics optional with the forgo-the-chest choice and deferred recovery; crystal lizards award Titanite per kill (2042–2057).
- Campaign: sparks capped at the starting number, no purchase; soul rewards −1; tier two gated behind a 16-soul bonfire ascetic that also gives non-boss enemies +1 damage; transposition of boss treasure into legendaries; shop restock per section (2232–2348).
- PvP module (3040–3094).
- Community Update Pack weapon stat revisions (3206–3330).

## 6. Component discrepancy table

| Item | Manuscript | Official | Source | CSV |
|---|---|---|---|---|
| Mimic miniatures / data cards | "1x HungryVoracious Mimic" (443) | 2 miniatures, 2 data cards | EXP p.4 | D-020 |
| Mushroom Child & Parent | "1x Mushroom Child & Parent" (449) | 2 enemies, separate data cards (14 minis, 7 cards) | DR p.4 | D-027 |
| Ornstein & Smough | two main-boss entries (509–511) | one main boss | Core p.5 | D-023 |
| The Last Giant | absent from mega-boss list; used at 3018 | — | — | D-024 |
| First Activation token | absent (679–723); used at 1277, 3056 | 1x | Core p.7 | D-019 |
| Condition tokens | 7 each of four; "35x" (36 by arithmetic) | 5 each (20) + 4 Calamity | Core p.7; BDK p.4 | D-021 |
| Endurance bar | eight spaces (781) | ten boxes | Core p.20 | D-022 |
| Invader tokens, ambush cards, Titanite Scale cards, pillar tokens, health dials, mega-boss boards | absent | 6+6+3 tokens; 5 cards; 3 cards; dials; boards | PH p.5; EXP p.4; IK p.3; BDK/EC p.4 | D-025 |
| Event cards | 10/10/10 + 5 Special Trap cards | none in 1E; 30 un-levelled in V2 | Core p.6; V2 p.6 | D-001 |
| Encounter cards (expansions) | 31/31/31; level 4 = 40 | not reconcilable from supplied booklets; 9 megas × 4 = 36 | DR/IK/EXP/EC/BDK/V2 | D-026 |
| Phantom names | Jeramiah/Jeremiah, Armourer Dennis, Marvellous Chester | Jeremiah, Armorer Dennis, Marvelous Chester | PH p.5 | D-028 |
| Core enemies, bosses, treasure (13/40/60/10/18), dice, wound/soul tokens, cubes, terrain, tiles | as listed | match | Core p.4–7 | — |
| Expansion treasure totals (45/120/145/20/63 = 534) | as listed | commons and legendaries reconcile; starting/boss totals plausible but PWA and mega-boss sets unverifiable | CH p.4–5; V2 p.5; DR/IK/EXP p.3–4; BDK/EC p.4 | — |

## 7. Passages identical or near-identical to official text (for Agent F)

Core p.10 → 899–925 (tiles, nodes, adjacency, node limits, range); Core p.11 → 733–753 (dashboard list); V2 p.10 → 813–833 (equipment card list); Core p.17–18 → 931, 969–981 (gravestone, trap placement); Core p.19 → 1840 last sentence; Core p.20 → 1485–1517 (target vs hit, enemy data card list); Core p.21 → 1589–1594 (pushing, boss push); Core p.22–23 → 1838–1873 (movement, attacks, Range/Shift/AoE/Shaft/Repeat — Shift and Repeat paragraphs verbatim); Core p.24 → 1670–1702 (enemy movement, towards/away nearest paragraphs verbatim with taunt→threat); Core p.26–29 → 2079–2188 (boss data cards, behaviour cards, heat-up, arcs — "Bosses always directly face an adjacent node…" and "Remember that a character can be in more than one arc…" verbatim; deck renewal; movement; leap; area; repeat); Core p.33 → 2222–2240 (campaign setup, adding and dropping players verbatim), 2301–2306 (stat costs); Core p.35/37, PH p.17/19, DR p.11, EXP p.15, IK p.7, EC p.18–19 → campaign section lists; PH p.11–15 → 1999–2022 (invader tokens and setup); EXP p.10–13 → 2045–2047 (mimic procedure); IK p.5 → 2055 (crystal lizards); V2 p.31 → 2196 (boss death rewards).

## 8. Deviations traced to Hollowed Edition or Extended Rules (with source quotes)

Hollowed Edition v1.3:
- p.9 "When blocking, roll all dice available according to your equipment. Choose any two rolled dice." → 1722.
- p.9 "on a failed dodge roll a player may block damage from the attack using only the dice listed on their armor, and not weapons and shields." → 1759.
- p.9 "Enemies always activate first" / "Rest – Major action: Recover all of your stamina" / "passively recover 1 stamina" → 1664, 1802, 1826.
- p.9 "If the push originates on the same node, such as a leap or expel, the player may choose freely." → 1593; "it must push another monster. If no monsters are on the node, the player… is pushed" → 919.
- p.10 "Bleed stacks up to 2 times… the stack is consumed and the model takes 3 damage unaffected by armor." → 1605–1613; "Poison can stack indefinitely" → 1617; Corrosion "removed upon taking damage" → 1659; Calamity persistence → 1647.
- p.7 "After the first death, place 2 black cubes on the right side of the bar… Hollowing can be reversed by becoming embered." → 1215–1221, 805; "Dead players do get souls from the encounter" → 1449; "All dropped souls are recovered if a boss is defeated" → 1145.
- p.4 "Solo players begin with 6 souls." → 1003.
- p.2/p.6 "X+1 individual souls to each player, where X is the level of the encounter" → campaign table 2/3/4/5 (2256–2280); basic table is X+2.
- p.5 tier 4 "replacing the white cube with a red cube" → 1915; 2/4/6/8 cost ladder partly echoed (2/4/8/8).
- p.8 "choose whether to open or forgo the chest… do not have the opportunity to change equipment, recharge tokens, or move before opening" → 2043–2045; "Invaders… does not come back, even when re-entering that encounter or becoming embered again" → 1999, 2037.
- p.10 errata (Titanite Chunk +2, Titanite Slab +3, Tiny Being's Ring, Chloranthy Ring, Covetous Silver Serpent Ring, Mon Ring once per floor) → Community Update Pack 3178–3204.

Extended Rules V45:
- p.3 "Deck 1… All non-gem, non-Ember cards that have stat requirements of less than 25. Deck 2… Character Transposed treasure cards. 5 random Legendary treasure cards… at least one stat requirement of greater than or equal to 25." → 1013–1053.
- p.2 "the cost of a summon is two souls per player" → 1973.
- p.2 "When the party dies, they may take a shortcut to skip tiles that have face up encounter cards." → 1261 (with the original stamina price).
- The "Enemy Scaling" table, two-handed reroll, stat scaling, parry, round-based turn order and PvP have no source in either homebrew; they are original to the manuscript (or to the author's unpublished ruleset referred to at 377).

## 9. Totals

- Delta rows: 132 (incl. 27a). Hybrids: 38 rows; incompatible/unreconciled: 4 (event cards, summon cadence, gravestone vestige, mega-boss death) plus 4 needing a decision or classification (tier four, boss push arcs, shop categories, traps); the remaining 30 are compatible.
- Dropped official rules: 30 identified; 9 holes, 2 unacknowledged, 19 intentional replacements.
- CSV: 41 rows — 6 hybrid, 10 dropped-rule, 10 component-count, 15 underspecified-deviation; 2 Blocker, 14 Major, 23 Minor, 2 Note; 19 need a user decision.
