# 01 — Audit Report (Phase 1, Gate 1)

Project: Dark Souls: The Board Game — Second Edition (homebrew) editorial, completion and production pipeline. Branch `claude/lucid-ptolemy-l5w2fk`. Built 2026-11-10 by `tools/build_audit_report.py` from `02_audit_table.csv` (485 findings), `work/audit/E_rows.csv` (23 completions) and `03_coverage_tracker.md`. Agent reports: `work/audit/A_report.md`, `B_report.md`, `C_report.md` (+ `C_glossary_candidates.md`), `D_report.md` (+ `D_delta_table.md`), `E_completion_backlog.md` (= `04_completion_backlog.md`), `F_report.md`.

## 1. Executive summary

The manuscript is a coherent, playable design whose mechanical skeleton is sound and whose text is unfinished. Six parallel audits read all ten reference documents (plus the two supplementary mega-boss booklets) against the 3,006-line body and raised **485 findings**: **24 Blockers, 148 Majors, 245 Minors and 68 Notes**, of which 184 are REQUIRED, 102 OPTIONAL, 155 CLEAN-UP and 44 PROPOSED. Every stub, truncation and missing chapter has a fully drafted completion in `04_completion_backlog.md` (23 entries, about 15,000 words of lift-ready rules text). Coverage of the manuscript's chapters and sections is **100%**.

The design must be preserved, not "corrected": the lineage audit finds 44% of rule topics inherited from the 2017 core, 25% original to the author, 11% from the Hollowed Edition, 11% from the official expansions, 7% from the 2022 edition and 2% from Extended Rules. The deliberate departures (enemies act first in a round; aggro follows damage; block uses the two highest dice; one-stage hollowing with dropped souls; a stocked two-tier shop that restocks only after a boss; stamina-cost skipping; parry and riposte; the campaign ascetic and transposition) are complete and internally consistent. They are recorded in the Preserve list (§5) and are off-limits to later passes.

The book cannot be played from the text as it stands because of a small number of holes rather than any systemic flaw. Four values or procedures that every session needs are missing: the reduced soul reward for repeated encounters, the enemy attack-targeting icons, the end-state when the party is forced to rest with no sparks, and the resolution of character-versus-character attacks in PvP. One listed component (35 event cards) has no rule anywhere and no official source. The numerical audit also shows that three stacking rules are lethal at three and four players (the Repeat 2 scaling, the +1 attack at three players, and the ascetic's +1 stacking on top) and that the encounter-skip cost kills a hollow character outright; these require a mechanical decision, not an edit. The Glossary promised in the Introduction does not exist, the F.A.Q. is an empty heading, the Boss Special Rules chapter covers two of twenty-seven bosses and defers to an external booklet, and the Community Update Pack is a to-do list.

Voice and style are tractable: the manuscript is already British-spelled, carries 44 hedge words and one second-person passage, and has 24 meta-commentary passages and 16 external references, almost all in the Second Edition Notes and the Update Pack. Both the voice audit and the completion audit recommend replacing the Notes with a 165–171-word in-voice Foreword (OQ-01, Option A).

**Gate 1 verdict: ready for approval.** Every Blocker and Major has a proposed fix; every stub has a draft; the clean-up list is complete; asset reconnaissance is complete (155 assets catalogued, 114 extracted) in `22_asset_extraction_log.md`; the open questions in §7 each carry a recommended answer so that approval can be given wholesale or by exception.

## 2. Coverage tracker snapshot

| Measure | Value |
|---|---|
| Chapters + sections tracked (excluding 20 empty headings) | 190 |
| With at least one audit finding or completion | 190 (100%) |
| Findings by agent | see table below |
| Findings needing a user decision | 143 |

| Agent | Findings | Blockers | Majors | Decisions |
|---|---|---|---|---|
| A Rules Integrity | 125 | 5 | 41 | 41 |
| B Numerical Balance | 38 | 4 | 15 | 24 |
| C Style & Consistency | 124 | 1 | 30 | 26 |
| D Homebrew Delta | 41 | 2 | 14 | 19 |
| E Content Completion | 23 | 3 | 15 | 23 |
| F Cross-Reference & Voice | 134 | 9 | 33 | 10 |

Phase 0 status distribution of tracked rows: present 183, MISSING 2, META 1, DUPLICATE 1, STUB 1, SKELETON 1, NOT PRESENT 1. Full per-section detail (Audit IDs and Completion IDs now filled) is in `03_coverage_tracker.md`.

## 3. Top 10 highest-risk issues (lead editor's ranking across agents)

1. **Reduced soul reward is undefined** — A-053, B-008, C-068, CMP-0010 (Blocker). Repeating cleared encounters is a headline mechanic, yet both soul tables have one column. *Recommended:* half the full reward, rounded down (basic 1/2/2/3; campaign 1/1/2/2), as a second column in both tables (B's economy model; E's draft). A's "rounded up" and the "full minus two" alternative are recorded.
2. **Enemy attack targeting is never defined** — A-023 (Blocker), D-008. "Detailed later" points at nothing: aggro/nearest target icons, node attacks, out-of-range misses and push-movement damage are absent. Proposed text is supplied in A-023 (official p.25 as evidence only).
3. **Event cards are a dealt component with no rules** — A-090, A-091, D-001, B-037, CMP-0012 (Blocker; [PROPOSED-SYSTEMIC]). 35 cards are listed, dealt and scried, and no document defines them. *Recommended:* the author supplies the card texts and the one-paragraph rule in CMP-0012 is adopted; otherwise every reference is cut (OQ-06).
4. **Forced rest at zero sparks has no outcome; "lost" is undefined** — A-002, A-001, B-012, C-033, C-088, CMP-0006, CMP-0020 (Blocker). *Recommended:* a forced rest with the dial at zero loses the game; a character who dies while hollow is *lost* until the next rest; the three passages are collapsed into Death & Hollowing.
5. **Enemy scaling is lethal at 3–4 players** — B-003, B-004, B-002, B-031, A-024, A-025 (Blocker, [MECHANICAL CHANGE]). Against a two-highest-dice block cap, Repeat 2 at four players and the ascetic's extra +1 produce expected damage that empties an eight-box bar in two activations. *Recommended:* delete Repeat 2; four players = Base + 4 health and +1 attack; drop the +1 attack at three players; the ascetic adds health, not attack (OQ-07).
6. **Encounter-skip cost kills hollow characters** — B-014, A-008 (Blocker). Three skipped encounters cost six stamina; a hollow character has six boxes. *Recommended:* one stamina per skipped encounter, maximum three (OQ-10).
7. **PvP attack resolution is undefined** — A-032, A-031, A-033, A-035, B-024, CMP-0009 (Blocker). *Recommended:* adopt the CMP-0009 mini-chapter with B's dodge table (3/2/2/1/1/1).
8. **Missing and incomplete chapters** — CMP-0002 Glossary (absent), CMP-0003 F.A.Q. (empty), CMP-0005 Boss Special Rules (2 of 27 bosses; external reference at line 1195: A-115, C-081, F-049), CMP-0004 Community Update Pack (skeleton) (Blocker). Drafts exist for all four; nine bosses remain BLOCKED for want of their booklets (OQ-20).
9. **Treasure is both pre-dealt to tiles and drawn on clearing** — A-057, D-032 (Major). Applied literally the party collects twice. *Recommended:* the pre-dealt card *is* the reward (OQ-11).
10. **Endurance bar: "eight" spaces in the text, ten on every printed dashboard** — B-015, D-022 (Major). Every hollow, skip and overflow number depends on this. *Recommended:* the author confirms whether Second Edition uses the official dashboards (then "ten, reduced to eight when hollow") or a new eight-box dashboard (OQ-08).

Close behind: two-boss encounters and Gargoyle ×2 (A-039, A-040, CMP-0005); the parry's stagger vanishing before it matters (A-078); turn-sequencing gaps (A-073/D-017, A-019, A-020/D-002); the duplicated Tier Four cost (A-067, B-007, C-071, D-005); the "two by six" grid (A-088, C-092); undefined left/right slots that parry depends on (A-068); traps and terrain versus enemies (A-082, A-083, D-009); poison's triangular stacking (B-025).

## 4. Content-Completion Summary

Every entry below is drafted in full in `04_completion_backlog.md` and is `[PROPOSED]` pending approval (OQ-02).

| ID | Section | Severity | Draft |
|---|---|---|---|
| CMP-0001 | Characters › Character Tokens › Estus Flask | Major | `04_completion_backlog.md` › [CMP-0001] |
| CMP-0002 | GLOSSARY | Blocker | `04_completion_backlog.md` › [CMP-0002] |
| CMP-0003 | F.A.Q. | Blocker | `04_completion_backlog.md` › [CMP-0003] |
| CMP-0004 | COMMUNITY UPDATE PACK | Major | `04_completion_backlog.md` › [CMP-0004] |
| CMP-0005 | BOSS SPECIAL RULES | Blocker | `04_completion_backlog.md` › [CMP-0005] |
| CMP-0006 | Gameplay › Death & Hollowing | Major | `04_completion_backlog.md` › [CMP-0006] |
| CMP-0007 | Summons › Phantoms | Major | `04_completion_backlog.md` › [CMP-0007] |
| CMP-0008 | Campaign Play › Setup | Major | `04_completion_backlog.md` › [CMP-0008] |
| CMP-0009 | PLAYER VS PLAYER | Major | `04_completion_backlog.md` › [CMP-0009] |
| CMP-0010 | Gameplay › Souls | Major | `04_completion_backlog.md` › [CMP-0010] |
| CMP-0011 | Gameplay › Encounter Start step 9 | Minor | `04_completion_backlog.md` › [CMP-0011] |
| CMP-0012 | Game Components | Major | `04_completion_backlog.md` › [CMP-0012] |
| CMP-0013 | INTRODUCTION | Major | `04_completion_backlog.md` › [CMP-0013] |
| CMP-0014 | MIMICS | Major | `04_completion_backlog.md` › [CMP-0014] |
| CMP-0015 | CRYSTAL LIZARDS | Minor | `04_completion_backlog.md` › [CMP-0015] |
| CMP-0016 | EQUIPMENT › Spells | Minor | `04_completion_backlog.md` › [CMP-0016] |
| CMP-0017 | BOSS SPECIAL RULES › Wind Up | Minor | `04_completion_backlog.md` › [CMP-0017] |
| CMP-0018 | SUMMONS › Phantoms | Major | `04_completion_backlog.md` › [CMP-0018] |
| CMP-0019 | Returning to the Bonfire › Resuming Exploration | Major | `04_completion_backlog.md` › [CMP-0019] |
| CMP-0020 | Gameplay › Encounter Recovery | Major | `04_completion_backlog.md` › [CMP-0020] |
| CMP-0021 | CAMPAIGNS › The First Journey | Minor | `04_completion_backlog.md` › [CMP-0021] |
| CMP-0022 | CAMPAIGNS › The Undead Colosseum preamble | Major | `04_completion_backlog.md` › [CMP-0022] |
| CMP-0023 | Setup › Setup After the main-boss | Major | `04_completion_backlog.md` › [CMP-0023] |

Flags: CMP-0005 is **partly BLOCKED** (Four Kings, Gaping Dragon, Guardian Dragon, Manus, Old Iron King, Vordt, The Last Giant, Crossbreed Priscilla, Heavy Knight, plus Ornstein & Smough pairing detail and further Asylum Demon rules — booklets not supplied). CMP-0012 is **[PROPOSED-SYSTEMIC]** for the event-card rule paragraph. CMP-0013 offers Option A (Foreword, 171 words) and Option B (expanded Introduction, 119 words); the voice audit's 165-word Foreword is an alternative A text in `work/audit/F_report.md` §9.

## 5. Preserve list — intentional, complete rules to keep untouched

Agreed by audits A and D (full lists in `A_report.md` §5 and `D_report.md` §5). Phase 2A may tighten the prose of these rules but must not alter their mechanics without a `[MECHANICAL CHANGE]` entry and sign-off.

- Round structure: all enemies act first, then every character in descending threat; aggro moves to the round's top damage-dealer (ties keep it). Bosses alternate boss/character; boss aggro moves on any damage.
- Invader acts after each character's turn and never scales; phantoms are drawn at random for two souls per contributing character and act once per character turn in boss fights (cadence clarified by A-020/D-002).
- Character turn: recover one stamina; minor actions Walk, Run, Equip, Heroic Action; one major action Attack, Rest (unless the character ran), Drink Estus, Ember. Stamina overflow becomes stagger and may never be chosen.
- Defence: block/resist = sum of the two highest dice; dodge costs one stamina (+2 for an extra die, max four) and forces a move; failed dodge rolls armour dice only; parry (shield in left hand, same node) staggers the enemy and allows a riposte, fails with full damage and self-stagger.
- Luck rerolls any or all dice; two-handed (or lone one-handed) weapons reroll one attack die; stat scaling +1 when a stat exceeds the highest requirement by the threshold (value under OQ-19).
- Spells: one spell attack option per turn; three spells per catalyst; no scaling or two-handing; upgrade spells cast as a major action.
- Hollowing: death with survivors revives the character hollow (−2 endurance); a hollow's death fails the encounter and forces a spark rest; hollow is removed by rest or ember. Souls are personal; dropped souls return only to the dropper on a surviving clear.
- Partial recovery after a clear (one damage cube — see OQ-12 — all stamina, all conditions; Estus/Luck/Heroic not refreshed).
- Sparks: 6 − N at start; +1 per boss; free rest after a boss; campaign maximum = starting value (buy-back under OQ-22).
- Shop: two tiers stocked by category quota, restocked only after a boss (campaign: after a section); prices 2 / 4, sell 1, boss treasure sells for 6 (campaign 4); embers only in the tier one shop at setup.
- Treasure tiers split at a stat requirement of 25; transposed cards are tier two; five legendaries enter the tier two deck; one treasure per character per first clear; one random boss treasure per boss kill.
- Skipping cleared encounters for a stamina cost; repeating them for souls but not treasure; scrying on clearing a gravestone tile; fog gate becomes a shortcut; failed encounters cannot be skipped once reset.
- Enemy scaling by character count (values under OQ-07); bosses never scale.
- Conditions: bleed = three unblockable damage on the second token; frostbite stops stamina recovery; stagger −1 to attack and defence; Calamity lasts the encounter (OQ-24); Corrosion −1 block until damaged.
- Terrain: gravestones block all movement and grant a scry; barrels break when dodged or pushed into; chests hold one pre-placed card; traps persist through resets.
- Boss deck renewed by flipping the discard unshuffled; weak-arc black die; same-arc movement and pushes; dodge ignores arcs.
- Mimics optional with the forgo-the-chest choice and deferred recovery; mimic kill yields two treasures; crystal lizards award Titanite per kill and never respawn once one has died.
- Campaign: soul rewards one lower; stat costs 4/8/16/20; ascetic (16 souls) unlocks tier two; transposition of boss treasure for 4 souls; fog gate aesthetic only; adding/dropping players for a spark.
- Mega-boss as optional final act after one Level 4 encounter; solo character starts with six souls; *threat* as the single term for the dashboard's taunt value (glossary bridge, D-039).
- Community Update Pack weapon stat revisions (values under B-018…B-021).

## 6. Clean-up list — external references and meta-commentary scheduled for removal

From `F_report.md` §2–3 (all tagged CLEAN-UP in `02_audit_table.csv`).

| Lines | Passage | Disposition |
|---|---|---|
| 1–3 | Byline "Based on related works by Steam Forged Games (SFG), Konami, …" | Move to colophon as acknowledgements (F-001) |
| 371–381 | SECOND EDITION NOTES (publisher history, first person ×8, "google docs", editors' note, WIP statements, the only "you") | CUT; supersession statement and italics convention survive in the Foreword (F-002…F-006, F-055; OQ-01) |
| 845, 1057, 1141 | "Players should include all … expansions …", "DStBG has many expansion sets available …" | Rewrite in voice as inclusion rules (F-009, F-010, F-011) |
| 1109 | "For added challenge the players may forgo choice …" | Rewrite as an option (F-013) |
| 1195 | "special rules described in the mega-boss rule booklet" | Replace with "(see §Boss Special Rules)"; chapter completed by CMP-0005 (F-049, A-115, C-081) |
| 2041, 2053 | Mimics / Crystal Lizards advisory preambles ("Groups with new players should…", "The following rules assume…") | Rewrite as the optional-rule formula (F-023, F-025, F-051) |
| 2069 | "The core game does not come with mega-bosses …" | CUT sentence (F-027, F-050) |
| 2159, 2197 | Strategy advice (memorise the deck); session-logistics advice | CUT (F-033, F-035) |
| 2191 | Reasoning in place of rule ("one can assume …") | Rewrite as the aggro rule (F-034) |
| 2221–2225 | "Campaigns provide a more challenging…", "Players might expect…", "This rule-set includes three campaigns…" | CUT / rewrite; factual error fixed by CMP-0008 (F-036, F-037, F-038) |
| 2297, 2312, 2304 | "essentially unchanged from the basic rules…", "functions similarly…", "They must decide at what point…" | Rewrite as delta statements with §-refs (F-040, F-041, F-042) |
| 2221–3060 (×10) | "the basic game / basic rules" as if a separate book | Define "the standard game" once; §-refs thereafter (F-053) |
| 2352 ff. | Campaign headings tagged with video-game titles ("Dark Souls 3 (Core)") | Optional: keep component tag only (F-052) |
| 3102–3206 | Community Update Pack "Treasure - Official / Errata/Updated" working notes | CUT as notes; rules content becomes the appendix of CMP-0004 (F-047) |
| 3208 | "The first edition of DStBG has many nonsensical weapon stat requirements which this edition aims to remedy…" | CUT; table kept with a one-sentence in-voice lead (F-048) |
| 387–723 | Set codes PWA / ToG undefined | Keep with a one-line key (F-054) |
| Body | 28 prose cross-references ("described later", "as before", "Refer to 'Boss Encounter'") — 4 dangling | Convert all to "(see §N.M)"; add the missing fog-gate placement step (F §6, C-082…C-087) |
| Body | 42 passages copied or closely paraphrased from the official rulebooks (voice carriers, not rights issues) | Rewrite in the book's voice during Phase 2A (F §7) |

Also scheduled: 20 empty headings; the duplicate Spells heading; the duplicate "Facing the Abyss" campaign; "first player token" (CMP-0011); "mastering" (A-112); the gravestone "not flipped" vestige (D-003); the Special Trap cards unless event cards are kept (A-091).

## 7. Open questions for the user (each with the lead's recommended answer)

Approval may be given wholesale ("approve all recommendations") or by exception. Items marked **[MECHANICAL CHANGE]** alter a complete rule and require explicit sign-off.

- **OQ-01 Second Edition Notes.** Rewrite as an in-voice Foreword (Option A) or cut entirely (Option B)? *Recommended:* A — the 165-word Foreword in `F_report.md` §9.1 (or E's 171-word variant), credits to a colophon line.
- **OQ-02 Content completions.** Approve, revise or reject each of CMP-0001…CMP-0023 (§4). *Recommended:* approve all; for CMP-0005 approve the drafted bosses now and leave the nine BLOCKED bosses as "apply the special rules supplied with that expansion" placeholders until booklets arrive (OQ-20).
- **OQ-03 Asset priorities.** Which extracted assets lead the cover, chapter openers and component pages? 155 assets are catalogued and 114 extracted (`22_asset_extraction_log.md`, `21_asset_manifest.csv`, `assets/`). *Recommended:* the vector wordmark (AST-0001/0004) and the lava-scale cover texture for the cover; the complete 2022 symbol key (61 icons) as the book's icon set; the knot, compass-corner and title-rule ornaments for chapter openers and folios; the anatomy diagrams redrawn over the extracted plates; component photography (28 TO EXTRACT items) in Phase 2B.
- **OQ-33 Asset rights and fonts.** (a) Does the rights assertion extend to the FromSoftware / Bandai Namco key art reproduced in the SFG books (both cover paintings and ten character/boss plates, held under Provenance Review)? (b) Is the DARK SOULS wordmark to be used titularly on the cover or only nominatively? (c) Approve the open-font substitutions — Cinzel for OptimusPrinceps (display), Libre Caslon Text or EB Garamond for Adobe Caslon Pro (body), Liberation Sans for utility text — or supply licensed font files. *Recommended:* hold the key art until (a) is confirmed; nominative wordmark use with the book's own title set in the display face; approve Cinzel + Libre Caslon Text.
- **OQ-04 "Combat Cards".** The brief names a truncated Combat Cards section; this DOCX revision has none. Is there a newer manuscript revision? *Recommended:* treat as out of scope unless supplied.
- **OQ-05 Reduced soul reward.** Half rounded down (1/2/2/3; campaign 1/1/2/2) or half rounded up or "full − 2, min 1"? *Recommended:* half rounded down.
- **OQ-06 Event cards.** Supply the 35 card texts and adopt the CMP-0012 rule paragraph, or delete every reference (components, setup, scrying, Special Trap cards)? *Recommended:* delete unless the cards exist as a designed set.
- **OQ-07 Enemy scaling [MECHANICAL CHANGE].** Delete Repeat 2 at four players (→ Base + 4 health, +1 attack), move the +1 attack from three to four players, and make the ascetic add health instead of a second +1 attack? *Recommended:* yes to all three (B §2, §14, §15).
- **OQ-08 Endurance bar.** Does Second Edition use the official ten-box dashboards (text becomes "ten spaces, eight when hollow") or a new eight-box dashboard? *Recommended:* ten-box official dashboards; hollow blocks two.
- **OQ-09 Tier Four [MECHANICAL CHANGE on value].** Basic cost 8 → 10 (B), 12 (D) or 16 (A, C)? Value "+5 over tier three" → 40 (official/HE) or max(40, tier three + 5) (B)? *Recommended:* cost 10; value max(40, tier three + 5).
- **OQ-10 Encounter skip cost [MECHANICAL CHANGE].** Keep two stamina per skipped encounter with A-008's "only if every character can pay" guard, or B-014's one stamina per skipped encounter, maximum three? *Recommended:* B-014.
- **OQ-11 Treasure award.** Pre-dealt card is the reward (delete "draw on clearing") or draw on clearing (delete the pre-deal)? *Recommended:* pre-dealt card is the reward (A-057).
- **OQ-12 Encounter recovery.** Remove one damage cube (Encounter Recovery) or two (Mimics text)? *Recommended:* one; align Mimics (D-035).
- **OQ-13 Poison [MECHANICAL CHANGE].** Keep "one damage per token, remove one" (triangular stacking) or B-025's "n damage, then remove all"? *Recommended:* B-025.
- **OQ-14 Mega-boss permadeath.** Keep sudden death in the final mega-boss fight (text at line 1195) or apply normal hollowing with spark-costed retries? If kept, it applies only when the mega-boss is the campaign's final boss (A-049). *Recommended:* normal hollowing rules (D-007), A-049 either way.
- **OQ-15 PvP frequency.** PvP after every boss with the +1 carry-over, or once after the final boss? *Recommended:* after every boss as written (A-031 text), with CMP-0009's tracking rule.
- **OQ-16 Stagger duration.** Remove at the end of the affected model's *next* complete turn (A-078) so a parry's stagger matters? *Recommended:* yes.
- **OQ-17 Printed card names.** Use the printed American spellings for proper nouns (Armorer Dennis, Marvelous Chester, Plow Scarecrow, "Sword Master") or anglicise? *Recommended:* printed spellings for card names; British English everywhere else (C-010, C-011, D-027).
- **OQ-18 F.A.Q. register.** Keep the 37-entry Q&A (CMP-0003, as the brief requests) or fold rulings into sections (F-046)? *Recommended:* keep the Q&A as a final chapter in lawbook voice.
- **OQ-19 Stat scaling threshold [MECHANICAL CHANGE].** +1 at ten over the requirement (manuscript) or at five over (B-016)? *Recommended:* five.
- **OQ-20 Missing booklets.** Can the Four Kings, Gaping Dragon, Guardian Dragon, Manus, Old Iron King, Vordt, The Last Giant, Painted World of Ariamis and Asylum Demon booklets be supplied to unblock CMP-0005 and verify four campaigns (A-111)? *Recommended:* supply if available; otherwise ship placeholders.
- **OQ-21 Campaign pacing.** Keep both the −1 soul reward and the doubled stat costs, or one lever only (B-011)? *Recommended:* keep rewards at 3/4/5/6 and the doubled costs.
- **OQ-22 Campaign sparks.** Maximum = start + 1 and a 4-souls-per-character buy-back (B-013), or the manuscript's hard cap with no purchase? *Recommended:* B-013.
- **OQ-23 Dice faces.** Confirm the physical faces (Black 0,1,1,1,2,2; Blue 1,1,2,2,2,3; Orange 1,2,2,3,3,4; Green 3 blank / 3 success) so they can be printed (B-001).
- **OQ-24 Calamity.** Keep "lasts the encounter" or adopt removal on damage (B-026, official)? *Recommended:* keep the manuscript's version.
- **OQ-25 Ornstein & Smough / Gargoyle ×2.** Separate decks and dials per boss with alternation A-character-B-character (A-039), or one boss with a shared dial and deck whose cards name the acting model (CMP-0003 F.A.Q. and CMP-0005 as drafted)? Back-to-back Gargoyle fights with the treasure only after both (A-040, CMP-0005 Twin Gargoyles)? *Recommended:* the shared-deck reading (it matches the printed single data card and health dial) and yes to Twin Gargoyles; the F.A.Q. and Boss Special Rules drafts are aligned to whichever is chosen.
- **OQ-26 Minor/major action order.** Any order (D-017/A-073) or move-before-or-after-attack only? *Recommended:* any order, each minor action once.
- **OQ-27 Shop restock.** Sweep unsold cards to the bottom of the deck before restocking (A-046) or top up to quota? *Recommended:* sweep.
- **OQ-28 Invasion limit.** One invasion per leg (before and after the mini-boss) or one per game (A-045)? *Recommended:* one per leg.
- **OQ-29 Contested treasure.** Tie-break to the aggro holder everywhere (C-087, D-037)? *Recommended:* yes.
- **OQ-30 Embering heals?** Keep "remove all damage cubes" on embering (manuscript) or remove hollow only (A-006 alternative)? *Recommended:* keep the manuscript (heal + un-hollow).
- **OQ-32 Phantom (summon) cadence.** In boss encounters the summon acts after each character's turn (A-020, D-002, official Phantoms booklet) or once per round after the last character (manuscript step 6; CMP-0003 F.A.Q. and CMP-0018 as drafted)? *Recommended:* after each character's turn; the F.A.Q. and CMP-0018 drafts are aligned to the decision.
- **OQ-31 Chapter names.** Rename SUMMONS → PHANTOMS and give the Update Pack and weapon table appendix status (C-065, F-047)? *Recommended:* yes.

## 8. Recommended cut / simplify list

| Item | Recommendation | Source |
|---|---|---|
| Second Edition Notes chapter | CUT → Foreword (OQ-01) | F, E |
| Repeat 2 scaling row and +1 attack at three players | CUT / move (OQ-07) | B-003, B-004 |
| Ascetic +1 attack stacking | SIMPLIFY → health | B-031 |
| Event cards and Special Trap cards | CUT unless defined (OQ-06) | A-090, D-001 |
| First player / first activation token | CUT (threat order already fixes the first turn) | CMP-0011, D-040 |
| "mastering" an encounter | CUT | A-112 |
| Gravestone "not flipped" clause | CUT (vestige) | D-003 |
| Duplicate "Facing the Abyss" campaign | CUT one (keep the Darkroot booklet version) | C-102, CMP-0008 |
| 20 empty headings; duplicate Spells heading; "&" in 9 headings | CUT / normalise | C §10 |
| Strategy and session advice (lines 2159, 2197) | CUT | F-033, F-035 |
| Character Turn Order AND/OR blockquote | SIMPLIFY → numbered sequence | C-119, A-073 |
| Mimic procedure stated in three places | SIMPLIFY → Mimics chapter owns it | CMP-0014, C-091 |
| Hollow death stated in three places with three outcomes | SIMPLIFY → Death & Hollowing owns it | C-088, CMP-0006 |
| Terrain movement rules in two places | SIMPLIFY → Terrain owns it | C-088, A-082 |
| Enemy Turn Overview repeats Encounter Turn Order tie-breaks | SIMPLIFY → state once | A, C |
| "the basic game / basic rules" ×10 | SIMPLIFY → "the standard game" + §-refs | F-053 |
| Weapon stat table as plain text | SIMPLIFY → 5-column table with Tier column | C-074, B §8, CMP-0004 |
| PvP dodge list with escaped brackets | SIMPLIFY → table | C-081, B-024 |
| Encounter-skip cost | SIMPLIFY → 1 per skip, max 3 (OQ-10) | B-014 |
| Everything in §5 | KEEP | A, D |

## 9. Gate 1 checklist

| Criterion | Status |
|---|---|
| All inputs audited (11 manifest + 2 supplementary) | ✔ |
| Coverage ≥ 95% | ✔ (100%) |
| Every Blocker/Major has a proposed fix | ✔ (24 Blockers, 148 Majors; all rows carry a Proposed fix) |
| Every stub/truncated section has a [PROPOSED] completion | ✔ (23 CMP entries) |
| Clean-up list complete | ✔ (§6) |
| Asset reconnaissance complete | ✔ (155 catalogued, 114 extracted, 12 under Provenance Review, 3 font substitutions logged) |
| Open questions enumerated | ✔ (OQ-01…OQ-33) |
| Every [PROPOSED] completion has a visible draft | ✔ (`04_completion_backlog.md`) |

**Halt.** Phase 2A begins only on explicit approval of this report and of the completion backlog.
