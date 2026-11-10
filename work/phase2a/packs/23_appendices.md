# Drafting pack — chapter 23 (appendices) — manuscript chapter "COMMUNITY UPDATE PACK"

Source text: `work/phase2a/source/23_appendices.md` (manuscript.md lines 3102–3366).

## Tracker rows (section · status · notes)

- **(chapter)** · SKELETON · line 3102. Lists of card names + terse errata notes + weapon stat table; no rules prose. Completion required (CMP).

## Audit findings mapped to this chapter (17)

Columns: ID · Issue type · Severity · Tag · Location · Current text · Proposed fix · Rationale · Gameplay impact · Decision needed (resolved at Gate 1 — apply the recommendation; see 05_gate1_decisions.md).

### F-047 · external-reference · Blocker · CLEAN-UP
- Location: L3102–3206 §Community Update Pack
- Evidence: Working notes and external labels: headings 'Treasure - Official', 'Treasure - Errata/Updated'; bracketed WIP notes '(will keep old one-handed version)', '(will need custom card to state +1 stamina gain per turn)', 'legendary Item instead of Boss Drop'.
- Current text: **Treasure - Official** … **Treasure - Errata/Updated** … Sellsword Twinblade (will keep old one-handed version) … Chloranthy Ring (will need custom card to state +1 stamina gain per turn) …
- Proposed fix: CUT from the rulebook. Card changes that are rules (Titanite Chunk +2, Titanite Slab +3, Tiny Being's Ring, Chloranthy Ring, Wolf Ring, Covetous Silver Serpent Ring, Mon Ring, Blue Titanite) become an in-voice appendix 'Card Text Amendments' stating each card's governing text, e.g. 'Titanite Chunk: +2 attack; may be attached only in place of a Titanite Shard.' The 'Official' / 'Errata' labels and the 'will keep/will need' notes are deleted.
- Rationale: The pack is a to-do list addressed to the editor and cites 'official' material as a source.
- Gameplay impact: none
- Decision needed: Y

### F-048 · meta-commentary · Blocker · CLEAN-UP
- Location: L3208 §Community Update Pack › Weapons - Updated Stat Requirements
- Evidence: 'Changes from prior edition' rationale, external-source references: 'The first edition of DStBG has many nonsensical weapon stat requirements which this edition aims to remedy… from the video game series… in the source material… roughly equal to the first edition.'
- Current text: The first edition of DStBG has many nonsensical weapon stat requirements which this edition aims to remedy. Specifically, many high strength requirement weapons from the video game series where given intelligence and/or Faith requirements… Affected weapons and their changes are summarised below.
- Proposed fix: CUT the paragraph. Keep the table as Appendix A 'Weapon Stat Requirements' with the single in-voice lead: 'The weapons listed below use the stat requirements given here in place of the values printed on their cards.'
- Rationale: Design rationale and comparison with the prior edition are excluded; the table itself is a rule and stays.
- Gameplay impact: none
- Decision needed: Y

### A-096 · contradiction · Major · REQUIRED
- Location: GAMEPLAY › Treasure Rewards (manuscript.md line 1477) vs CRYSTAL LIZARDS (line 2055)
- Evidence: manuscript.md:1477, 2055, 3182; DS-IronKeep-Rules-Web.txt p.3 (3x Titanite Scale Cards), p.5
- Current text: award a Titanite Chunk card to any character who killed a crystal lizard during the encounter. / Whenever a character kills a crystal lizard, they immediately place one Titanite Scale card into their inventory.
- Proposed fix: Whenever a character kills a crystal lizard, that character immediately places one Titanite Scale card in their inventory. (Delete the Titanite Chunk bullet at line 1477.)
- Rationale: Two names and two timings for the same reward. The Iron Keep expansion supplies Titanite Scale cards for exactly this purpose; the Update Pack's Titanite Chunk is a separate common card. Alternative: award a Titanite Chunk and treat the three Scale cards as extra Chunks.
- Gameplay impact: Different cards with different stat requirements and bonuses.
- Decision needed: Y

### B-018 · table-text-mismatch · Major · REQUIRED
- Location: L3246 (Weapons - Updated Stat Requirements: Falchion)
- Evidence: Falchion 37/30: the second-highest STR requirement of the 60 rows (only Dragon Tooth 40 is higher), above Black Knight Greataxe 32 and Vordt's Great Hammer 33, for a basic one-handed curved sword. The stated method (L3210) raised a primary stat 'to ensure overall balance remained roughly equal'; 37 is not roughly equal to any plausible original.
- Current text: Falchion 37 30 0 0
- Proposed fix: Falchion 17 30 0 0
- Rationale: A digit transposition (17 -> 37) is the most economical explanation; 17/30 keeps the weapon tier two on DEX, consistent with Scimitar 18/20 and Shotel 26/29.
- Gameplay impact: Makes the Falchion equippable by a DEX character at Tier Two-Three instead of requiring STR Tier Three/Four.
- Decision needed: Y

### B-019 · table-text-mismatch · Major · REQUIRED
- Location: L3226-3228 (Carthus Curved Greatsword 19/30; Carthus Curved Sword 25/35)
- Evidence: The greatsword requires less of both stats than the one-handed sword; every other paired weapon in the table (Mace/Great Mace, Claws/Manikin Claws, Halberd family) has the heavier weapon higher. STR 25 also pushes the one-handed sword into tier two by one point.
- Current text: Carthus Curved Greatsword 19 30 0 0
Carthus Curved Sword 25 35 0 0
- Proposed fix: Carthus Curved Greatsword 25 35 0 0
Carthus Curved Sword 19 30 0 0
- Rationale: Swapping the two lines restores the heavier-weapon-higher ordering without introducing new values.
- Gameplay impact: Both remain tier two; the one-handed sword becomes reachable at DEX Tier Two-Three.
- Decision needed: Y

### B-022 · undefined-value · Major · REQUIRED
- Location: L1069/L1079/L1085 (Shop Setup) with L823-829 (Equipment Cards), L747-753 (Equipment Slots), L1769 (Parry)
- Evidence: The stock list requires '2 shields' per shop and the parry rule requires 'a shield as their left weapon', but the card-typing rules define only one-handed weapon, two-handed weapon, armour (by icon) and spell (by scroll art). No rule says how a shield is recognised; shields are weapon-typed cards in 1E (East-West Shield appears in the manuscript's own weapons table, L3244).
- Current text: Equipment cards include weapons, spells, shields, armour, and items which the character equips to improve their combat capabilities. ... 3 weapons, 3 armour, 2 shields, 2 upgrades, and 2 spells.
- Proposed fix: Add to Equipment Cards: "A shield is a one-handed weapon card that shows a block or resist value and has no attack option. Shields count as weapons for equipment slots and as shields for shop stocking and parrying."
- Rationale: The shop and parry procedures cannot be executed without a test for 'shield'.
- Gameplay impact: Makes the 12-card stock list and the parry prerequisite determinable.
- Decision needed: Y

### C-056 · terminology · Major · REQUIRED
- Location: L1477; L2055; L3182
- Evidence: 'award a Titanite Chunk card to any character who killed a *crystal lizard*' (1477) vs 'they immediately place one Titanite Scale card into their inventory' (2055). Iron Keep booklet: '3x Titanite Scale Cards', 'add one Titanite Scale card to the inventory'. Community Update Pack (3182) defines Titanite Chunk as a common +2 upgrade replacing Titanite Shard.
- Current text: Titanite Chunk (L1477)
- Proposed fix: Titanite Scale
- Rationale: Two different cards named for the same reward; official component is the Titanite Scale.
- Gameplay impact: Which card a crystal-lizard kill awards
- Decision needed: N

### A-066 · undefined-state · Minor · OPTIONAL
- Location: CHARACTER TURN › Stat Scaling (manuscript.md line 1880)
- Evidence: manuscript.md:1880, 3212–3330 (several weapons with 0/0/0/0 or single requirements)
- Current text: If the character's current stat value exceeds an equipment's highest stat requirement by ten or more points, the character should mark the equipped item...
- Proposed fix: Equipment whose highest stat requirement is zero cannot be scaled.
- Rationale: A card with no requirement has a 'highest requirement' of zero, so every starting character scales it at once. Alternative: allow it (treat zero as a requirement).
- Gameplay impact: Affects throwables and a few low-end weapons.
- Decision needed: Y

### A-074 · contradiction · Minor · CLEAN-UP
- Location: EQUIPMENT › Upgrades (manuscript.md line 853); Shop Rules (line 1943); COMMUNITY UPDATE PACK (line 3182)
- Evidence: manuscript.md:853, 1941, 1943, 3182–3184
- Current text: Titanite upgrades (i.e.: Titanite Shards) attached to sold weapons are returned to the bottom of the tier one treasure deck.
- Proposed fix: Titanite upgrades attached to a sold weapon are returned, with the weapon, to the bottom of the treasure deck of the weapon's tier.
- Rationale: The Update Pack makes Titanite Chunk a 25/25 (tier two) card; the sell rule sends all titanite to tier one.
- Gameplay impact: Cosmetic deck-composition drift.
- Decision needed: N

### B-020 · balance · Minor · OPTIONAL
- Location: L3222 (Butcher Knife 25/0), L3236 (Dark Silver Tracer 0/25), L3324 (Warden Twinblades 17/25)
- Evidence: Three rows sit exactly on the 25 split with their only or highest requirement; one point decides which deck they enter. Twelve rows in total are within two points of the split (see B_report §8.1).
- Current text: Butcher Knife 25 0 0 0 / Dark Silver Tracer 0 25 0 0 / Warden Twinblades 17 25 0 0
- Proposed fix: Decide each boundary row deliberately and move it off the split: Butcher Knife 24 0 0 0 (tier one) or 28 0 0 0 (tier two); Dark Silver Tracer 12 26 0 0; Warden Twinblades 17 26 0 0.
- Rationale: A tier boundary that coincides with a requirement is read differently by every table; the manuscript's own threshold phrase ('equal or greater than 25', L1013) must then be checked card by card during setup.
- Gameplay impact: Deck composition changes by at most three cards.
- Decision needed: Y

### B-021 · table-text-mismatch · Minor · PROPOSED
- Location: L3232 (Claws 0/20), L3270 (Manikin Claws 24/24), L3280/L3290 (Parrying Dagger = Rapier 14/21), L3224 (Caestus 0/15)
- Evidence: Claws and Manikin Claws are the same weapon class 24 STR apart; Parrying Dagger and Rapier are identical; Caestus, Claws, Throwing Knives, Dark Silver Tracer and Priscilla's Dagger keep STR 0 although the rationale (L3210) says zero requirements were replaced. Nine identical stat lines exist in the table (B_report §8.1).
- Current text: Claws 0 20 0 0 / Manikin Claws 24 24 0 0 / Parrying Dagger 14 21 0 0 / Rapier 14 21 0 0 / Caestus 0 15 0 0
- Proposed fix: Claws 12 20 0 0; Manikin Claws 14 24 0 0; Parrying Dagger 10 18 0 0; Caestus 12 10 0 0. Add a sentence under the table: "A requirement of 0 is intentional where shown." for any row left at zero.
- Rationale: Brings the rows into line with the method the section states; distinguishes main-hand from off-hand tools.
- Gameplay impact: All affected rows remain tier one.
- Decision needed: Y

### B-032 · table-text-mismatch · Minor · REQUIRED
- Location: L1477 (Treasure Rewards, crystal lizards) vs L2057 (Crystal Lizards)
- Evidence: L1477 awards 'a Titanite Chunk card' for killing a crystal lizard; L2057 awards 'one Titanite Scale card'. Official Iron Keep rules (text lines 125-131) award a Titanite Scale; the manuscript's own errata list (L3126) redefines Titanite Chunk as a +2 upgrade that must replace a Shard.
- Current text: If playing with the option of *crystal lizards*, award a Titanite Chunk card to any character who killed a *crystal lizard* during the encounter.
- Proposed fix: "If playing with the option of crystal lizards, award one Titanite Scale card to any character who killed a crystal lizard during the encounter."
- Rationale: One reward name across both sections, matching the component list of the Iron Keep expansion (3x Titanite Scale cards).
- Gameplay impact: Prevents the +2 Chunk (a stronger upgrade) being handed out for an optional side-kill.
- Decision needed: N

### C-007 · spelling · Minor · REQUIRED
- Location: L469; L3354
- Evidence: L469 'Skeletal Beast (ToG)'; L3354 'Skeleton Beast'
- Current text: Skeletal Beast
- Proposed fix: Skeleton Beast
- Rationale: Tomb of Giants rulebook prints 'Skeleton Beast' (x3); manuscript uses both.
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

### C-072 · table-text · Minor · REQUIRED
- Location: L3210-L3330
- Evidence: Weapon stat table set as 61 plain-text lines: '**Weapon Name STR DEX INT FTH**' then 'Avelyn 23 30 0 0' etc.
- Current text: Avelyn 23 30 0 0 (plain text)
- Proposed fix: Set as a real 5-column table (Weapon | STR | DEX | INT | FTH), sorted alphabetically, with a caption and a note that all INT/FTH requirements are 0 by design (L3208).
- Rationale: Plain-text columns will not survive typesetting.
- Gameplay impact: None
- Decision needed: N

### C-109 · punctuation · Minor · REQUIRED
- Location: L1033; L1035; L1043; L1045; L1563-1577; L3084-3094; L3182; L3184; L925
- Evidence: '=\>' used for 'greater than or equal to' (1033-1045: 'without a required statistic =\> 25'); '1 -&gt; 2' in the scaling table (1563-1577); '-\>' in the PvP list; escaped '\[25/25/0/0 Common\]' (3182, 3184); 'Range ∞ (inﬁnity)' (925)
- Current text: =\> 25; 1 -&gt; 2; -\>
- Proposed fix: '25 or more' in prose (or '≥ 25' in tables only); '1 → 2' or 'becomes 2'; tables for the PvP list; '[25/25/0/0, common]'; 'Range ∞ (infinity)' with the ligature removed
- Rationale: '=>' is not the symbol for 'greater than or equal'; ASCII arrows and escaped brackets are pandoc artefacts.
- Gameplay impact: L1033-1045 as written literally means 'equals-implies 25'
- Decision needed: N

### C-117 · punctuation · Minor · CLEAN-UP
- Location: L875; L3154; L1806-1834
- Evidence: Pandoc list-separator comments '<!-- -->' (875, 3154) and blockquote '>' markup used for the turn-structure list (1806-1834)
- Current text: <!-- --> / > *Walk*: ...
- Proposed fix: Delete the comments; replace blockquotes with the numbered procedure proposed in the heading row.
- Rationale: Conversion artefacts.
- Gameplay impact: None
- Decision needed: N

## Completion entries that apply (1) — approved at Gate 1

### [CMP-0004] COMMUNITY UPDATE PACK (appendix) — Proposed Completion
- Read `04_completion_backlog.md` lines 411–562 (approved at Gate 1; apply untagged, subject to 05_gate1_decisions.md).

---

