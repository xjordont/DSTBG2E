# Phase 2A Drafting Brief — Dark Souls: The Board Game, Second Edition (Class A working document)

You are drafting ONE chapter of the final Class B manuscript. Everything you need is on disk; read it before writing. Write the chapter file incrementally (skeleton first, then one section at a time, saving after each) so that nothing is lost if your session is interrupted.

## 1. Inputs (read in this order)

1. `work/phase2a/DRAFTING_BRIEF.md` — this file.
2. `work/phase2a/packs/NN_slug.md` — your chapter's pack: tracker rows, every audit finding mapped to the chapter (ID, severity, tag, current text, proposed fix, rationale), and the approved completion (CMP) entries that apply.
3. `work/phase2a/source/NN_slug.md` — the manuscript's current text for the chapter (baseline, not ceiling).
4. `05_gate1_decisions.md` — the binding answers to every open question (OQ-01 … OQ-33). Where a finding, a CMP draft and a Gate 1 answer disagree, **the Gate 1 answer governs**.
5. `12_glossary.md` — the current glossary (headwords in bold). Italicise only terms that have, or that you add, a headword.
6. `01_audit_report.md` §5 (Preserve list), §6 (Clean-up list), §8 (Cut/simplify list).
7. For facts only (never for citation): the official rulebook texts in `work/text/*.txt`; the audit reports in `work/audit/*_report.md` (C §14 style sheet, F §8 voice guide, C §6 terminology table, D §5 lineage).

## 2. What Class B means (hard rules; `tools/style_check.py` enforces most of them)

- **No meta-commentary.** No editorial notes, no "[PROPOSED]", "[MECHANICAL CHANGE]", "[Editor: …]", "TODO", bracketed tags of any kind, no "this edition changes…", no design rationale, no process history. The chapter reads as a finished rulebook.
- **No external references.** Never name the official rulebooks, SFG/Steamforged, first edition, "V2", page numbers, booklets, the Hollowed Edition, Extended Rules, websites, or "the basic rules" as if they were another book. Expansion-specific rules are either reproduced or delegated with the fixed sentence: "Apply the special rules supplied with that expansion."
- **British English** (Oxford -ise is NOT used; use -ise/-yse: randomise, recognise, analyse; armour, behaviour, defence, centre, colour, grey, favour, licence (noun)). Exception (OQ-17): proper nouns printed on cards keep their printed spelling (Armorer Dennis, Marvelous Chester, Plow Scarecrow, Sword Master).
- **No second person** ("you/your") anywhere except inside a worked example paragraph. No first person. No "one must". No "players should".
- **No hedge words:** should, might, could, reasonably, probably, perhaps, maybe, likely, usually, typically, often, generally, essentially, largely, simply, just, roughly, quite.
- **Lawbook voice.** Present tense, third person, active where the actor is known. Preferred shape: "When [trigger], [subject] must/may [action]." One rule per sentence; conditions before consequences. Modals: *must* = obligation; *may* = permission; *cannot* = impossibility/prohibition; *never/always* only when there is no exception in the whole book; *is/are* for states. No *should*, no *can* for permission, no *will/would/could*. Exceptions are their own sentence beginning "If …" or "A … does not …".
- **Actors.** *Players* decide, agree, choose, roll and resolve ties. *Characters* act in the world: move, attack, spend stamina and souls, equip, die, rest, hold tokens. *The party* takes collective decisions and owns collective resources (sparks, boss choice, chests). *Models* occupy nodes, move and are pushed. *Enemies* (non-boss), *bosses*, *phantoms* (umbrella for *summons* and *invaders*). Never "one", never "you".
- **Numerals.** Words for zero to nine in prose; digits from 10; digits always in tables, with signs and symbols (+1, −1, ≥ 25, 90°), beside dice, and in printed labels (Level 1, Tier 2 treasure, 25 STR). Component lists: "2x Hollow Soldier" (lower-case x).
- **Italics = glossary keywords.** A glossary headword is italicised at its first use in each H2 section (and in table labels), plain thereafter. Italicise the whole word including inflections (*staggered*), never the article or punctuation. Every italicised term must be a headword in `12_glossary.md` or in your glossary delta file (§6 below). Do not italicise for emphasis. Do not use bold in running text (bold is for glossary headwords and definition lead-ins only).
- **Headings.** H1 = chapter: `# N. Chapter Title` (Title Case). H2 = numbered section `## N.M Section Title`. H3 = `### Sub-Section Title` (unnumbered). No trailing punctuation, no "&" (write "and"), no empty headings, no heading that is an instruction ("Recover one stamina."). Section titles are nouns.
- **Cross-references.** Always "(see §N.M)" using the section map in §4 of this brief; for a sub-section, "(see §N.M, Sub-Section Title)". Never "later", "earlier", "previously", "above/below" (except within the same H2), "as before", "Refer to", a chapter name in quotation marks, or any reference outside this book. Appendices: "(see Appendix A)". A rule is stated once, in its owning section; every other mention cites it.
- **Procedures** are numbered lists, one action per step, imperative mood with the party as implied actor ("Shuffle the tier one treasure deck."), sub-steps 1.1, 1.2. No advice, motives or examples inside a procedure; options are their own step ("The party may instead …").
- **Standing rules** are short paragraphs (≤ 4 sentences). Bullets only for unordered lists of components, conditions or eligible items (full sentences).
- **Worked examples** are separate paragraphs that begin exactly with `*Example.*` followed by the text, present tense, named characters (the Knight, the Herald, the Assassin, the Warrior), concrete numbers, no conditionals. An example states what happens; it never introduces a rule. Keep the source's examples (corrected) and add one where a finding asks for it.
- **Optional rules** open with the fixed formula: "X are an optional rule. They require the Y expansion. The party decides during setup whether X are in play."
- **Chapter intro.** ≤ 60 words, in-voice flavour permitted, declarative, no rule inside it.
- **Definitions in running text**: "**Entry node.** A basic node adjacent to the doorway through which the characters entered the tile." (same form as the glossary).
- **Punctuation.** Serial (Oxford) comma. Straight quotes. No "etc.", "i.e.", "e.g."; write "for example", "that is". No ampersands except in printed names (Ornstein & Smough). Degree sign for rotation. En dash with spaces for ranges in prose is NOT used; write "one to four"; tables may use "1–4". No em dashes in rules prose; use a full stop or a comma.
- **Markdown.** GitHub-flavoured tables (`| a | b |`), numbered lists `1.`, bullets `-`. Do **not** use blockquotes (`>`) anywhere. Do not use HTML. No footnotes markup; write footnote content as a sentence after the table.
- **Icons.** Refer to printed icons by name in words ("the *repeat* icon", "the skull icon"). Where the extracted icon set has an obvious match, append `{{icon:ast-NNNN-slug}}` immediately after the first mention in each H2 section (slug list in §7). If no obvious match, words only.

## 3. Terminology (canonical; use exactly these)

endurance bar (not stamina bar / endurance tracker) · damage cube (red, characters) · stamina cube (black) · wound token (enemies; never "damage token") · hollow cube (never "white cube"; stat cubes are white) · stat cube · soul token · spark dial · health dial · aggro token · condition token · trap token · fog gate token · invader token · ambush card · data card · behaviour card / behaviour deck · encounter card · treasure card ⊃ equipment card (never bare "item") · attack option (card line) / attack (the major action) · major action (never "main action") · minor action · turn (never "activation") · model (never "miniature") · entry node · heat-up (noun/adj.) / heats up (verb) · fog gate · setup (noun) / set up (verb) · reroll · back-up slot · PvP (after "player versus player (PvP)" once per chapter) · tier one / tier two (treasure) vs stat tier one … four (stats) · Level 1–4 (encounter cards, printed label) · mini-boss / main-boss / mega-boss (lower-case, hyphenated; Title Case only in headings) · the *bonfire* (component: bonfire tile) · Blacksmith Andre at first mention per section, then Andre; Andre's shop / the shop · the Firekeeper · Explorers (expansion; never "Encounters") · Titanite Scale (crystal-lizard reward) · *phantom* ⊃ *summon* + *invader* · threat (the dashboard value; never "taunt") · characters **die**; enemies are **killed**; bosses and encounters are **defeated** / **cleared**; a character out of play is **lost** · characters have damage and stamina; health is for enemies and bosses · tokens have a ready side and a used side; cards and tiles are face up / face down (predicate) or face-up / face-down (attributive) · "the standard game" (never "the basic game/rules") · Anor Londo, Lower Earthen Peak, Xanthous King Jeremiah, Great Grey Wolf Sif, Old Dragonslayer.

Resolved values you must use: endurance bar = ten spaces, hollow blocks two (OQ-08) · reduced soul reward = half rounded down (OQ-05) · four players: Base + 4 health and +1 attack; no Repeat 2; three players: health only (OQ-07) · stat tier costs 2/4/8/10 (campaign 4/8/16/20); tier four value = max(40, tier three + 5) (OQ-09) · skip cost one stamina per skipped encounter, maximum three (OQ-10) · poison: n damage then remove all tokens (OQ-13) · stagger removed at the end of the model's next complete turn (OQ-16) · stat scaling +1 at five over the highest requirement (OQ-19) · campaign sparks max = start + 1, buy-back 4 souls per character (OQ-22) · no event cards anywhere (OQ-06) · no first player token (CMP-0011) · pre-dealt treasure card is the reward (OQ-11) · recovery removes one damage cube (OQ-12) · one invasion per leg (OQ-28) · contested treasure to the aggro holder (OQ-29) · embering heals fully and removes hollow (OQ-30) · summon acts after each character's turn in boss encounters (OQ-32) · Ornstein & Smough one boss, shared dial and deck; Twin Gargoyles back to back, treasure after both (OQ-25) · no mega-boss permadeath (OQ-14) · PvP after every boss (OQ-15) · unsold shop cards swept to the bottom before restock (OQ-27) · any order of minor and major actions, each minor once (OQ-26) · twelve campaigns after the duplicate is removed (CMP-0008 says "thirteen": write twelve).

## 4. Section map (fixed; every "(see §N.M)" in the book targets this list)

Foreword (unnumbered, in `10_manuscript_chapter_00_front_matter.md`)
§1 Introduction (no H2s)
§2 Game Components: 2.1 Characters · 2.2 Enemies · 2.3 Bosses · 2.4 Phantoms · 2.5 Treasure Cards · 2.6 Encounter Cards and Ambush Cards · 2.7 Dice · 2.8 Tokens and Terrain Elements · 2.9 Expansion Components
§3 Characters: 3.1 Character Dashboards · 3.2 Equipment Slots · 3.3 Stat Progression Track · 3.4 Endurance Bar · 3.5 Character Tokens (H3s: Heroic Action, Luck, Estus Flask, Ember)
§4 Equipment: 4.1 Equipment Cards · 4.2 Upgrades · 4.3 Spells · 4.4 Embers
§5 Tiles and Nodes: 5.1 Tiles and Nodes · 5.2 Movement · 5.3 Node Model Limits · 5.4 Range · 5.5 Terrain (H3s: Gravestones, Barrels, Chests, Traps, Pillars)
§6 Setup: 6.1 Character Setup · 6.2 Treasure Deck Setup · 6.3 Shop Setup · 6.4 Bonfire Setup · 6.5 Encounter Setup · 6.6 Setup After the Mini-Boss · 6.7 Setup After the Main-Boss
§7 Gameplay: 7.1 Objective and Loss Conditions · 7.2 Death and Hollowing · 7.3 Embering · 7.4 Sparks · 7.5 Encounters (H3s: Encounter Start, Encounter Turn Order, Encounter Resolution, Encounter Recovery) · 7.6 Souls · 7.7 Treasure Rewards
§8 Combat Basics: 8.1 Target versus Hit · 8.2 Enemy Data Cards · 8.3 Enemy Scaling · 8.4 Pushing · 8.5 Conditions (H3s: Bleed, Poison, Frostbite, Stagger, Calamity, Corrosion)
§9 Enemy Turn: 9.1 Overview · 9.2 Enemy Movement · 9.3 Enemy Attacks · 9.4 Block and Resist · 9.5 Dodge · 9.6 Parry and Riposte
§10 Character Turn: 10.1 Turn Order · 10.2 Character Movement · 10.3 Character Attacks (H3s: Range, Shift, Area-of-Effect, Shaft, Repeat) · 10.4 Two-Handed Attacks · 10.5 Stat Scaling
§11 Returning to the Bonfire: 11.1 The Bonfire · 11.2 Resting · 11.3 The Firekeeper · 11.4 Blacksmith Andre · 11.5 Resuming Exploration
§12 Phantoms: 12.1 Summons · 12.2 Invaders
§13 Mimics (no H2s unless needed: 13.1 …)
§14 Crystal Lizards (no H2s unless needed)
§15 Boss Encounters: 15.1 The Fog Gate · 15.2 Overview · 15.3 Boss Tiles · 15.4 Boss Data Cards · 15.5 Boss Behaviour Cards · 15.6 Arcs and Defence
§16 Boss Turns: 16.1 Overview · 16.2 Boss Movement and Symbols · 16.3 Boss Attacks · 16.4 Boss Aggro · 16.5 Boss Death
§17 Boss Special Rules: 17.1 Rules Common to Several Bosses (incl. Twin Gargoyles, two boss models) · 17.2 Core Set · 17.3 Asylum Demon and Stray Demon · 17.4 Darkroot · 17.5 Iron Keep · 17.6 Explorers · 17.7 Tomb of Giants · 17.8 Black Dragon Kalameet · 17.9 Executioner's Chariot · 17.10 Bosses of Other Expansions
§18 Campaign Play: 18.1 Setup · 18.2 The Fog Gate · 18.3 Sparks · 18.4 Adding and Dropping Players · 18.5 Encounter Rewards · 18.6 The Bonfire (H3s: Stat Tier Costs, Blacksmith Andre's Shop, Shop Price Table) · 18.7 Bonfire Ascetic · 18.8 Transposition
§19 Campaigns: 19.1 The First Journey · 19.2 The Coiled Sword · 19.3 Ambush Lies Ahead · 19.4 The Gauntlet · 19.5 Facing the Abyss · 19.6 Demon Hunting · 19.7 Call of the Abyss · 19.8 A Hollow Pursuit · 19.9 The Undead Colosseum · 19.10 Into the Depths · 19.11 Playing with Fire · 19.12 Big Game Hunting
§20 Player versus Player: 20.1 Setup · 20.2 Turn Order · 20.3 Character Turns · 20.4 Attacking a Character · 20.5 Pushes and Conditions · 20.6 Traps · 20.7 Death · 20.8 Victory · 20.9 After the PvP Encounter
§21 Glossary (`12_glossary.md`)
§22 F.A.Q.: 22.1 … grouped by topic (numbered H2s of your choosing)
Appendix A. Weapon Stat Revisions · Appendix B. Card Amendments (file `10_manuscript_chapter_23_appendices.md`; H1s "Appendix A. Weapon Stat Revisions" and "Appendix B. Card Amendments")

## 5. How to apply the pack

- **REQUIRED** and **CLEAN-UP** findings: apply. **PROPOSED** (approved) findings and CMP entries: apply, untagged. **OPTIONAL** findings: apply when they improve clarity without altering a preserved mechanic; otherwise skip and say so in the change log.
- **Preserve list** (`01_audit_report.md` §5): tighten prose freely, never alter the mechanic. The only mechanical changes permitted are the five signed off at Gate 1 (OQ-07, OQ-09, OQ-10, OQ-13, OQ-19) and the explicit OQ answers; log each with `Type: mechanical change` and `Source: Gate 1 — OQ-NN`.
- A rule belongs to one owning section (see the cut/simplify list for which). If the manuscript states it in your chapter but another chapter owns it, replace the statement with one sentence and a cross-reference. If your chapter owns it, state it in full here even if the manuscript stated it elsewhere.
- Truncated or garbled sentences: complete them from the finding's proposed fix, the CMP draft, or the official text used as a fact source; the result must be a definite rule, never a placeholder. If a fact is genuinely unknown (nine BLOCKED bosses), use the delegation sentence from §2.
- Copied official prose (F §7 list): rewrite in the book's voice; do not paraphrase line by line.
- Delete: empty headings, event-card references, first player token, "mastering", the "not flipped" gravestone clause, strategy and session advice, publisher history, video-game-title tags in campaign headings (keep the component tag only: "The First Journey (Core Set)").

## 6. Deliverables (write all four; do not touch any other file)

1. `10_manuscript_chapter_NN_slug.md` — the chapter (Class B). Begin with the H1. No front matter, no comments.
2. `work/phase2a/changelog/NN_slug.md` — one entry per substantive change, in this exact form (IDs `CH-NN-001`, `CH-NN-002`, … where NN is your chapter number):

   ```
   ### CH-NN-001 · §N.M Section Title
   - Type: clarification | correction | completion | cut | restructure | style | mechanical change
   - Before: "<quote ≤ 40 words from the manuscript>" (or: new text)
   - After: "<quote ≤ 40 words from the chapter>" (or: deleted)
   - Rationale: <one or two sentences>
   - Source: <finding IDs, CMP IDs, Gate 1 OQ numbers>
   ```
   Pure spelling/typography fixes may be grouped in one entry ("style sweep"). OPTIONAL findings you skipped: one grouped entry listing the IDs with a one-line reason each.
3. `work/phase2a/glossary/NN_slug.md` — glossary deltas: `ADD **Headword.** Definition.` for new headwords; `AMEND **Headword.** New definition.` where the chapter's rule differs from the current glossary text; `CONFIRM` is not needed. Definitions in the glossary's own form (bold headword with full stop, one to three sentences, present tense, cross-reference to the owning section as "(see §N.M)").
4. `work/phase2a/issues/NN_slug.md` — anything you could not settle (a fact only the author knows, a conflict between two Gate 1 answers, a cross-chapter dependency). Bullet list; may be empty ("None.").

## 7. Icon slugs available

ast-0006-primary-spawn-node ast-0007-encounter-level-1 ast-0008-skeleton-soldier ast-0009-treasure-chest ast-0010-secondary-spawn-node ast-0011-encounter-level-2 ast-0012-skeleton-archer ast-0013-barrel ast-0014-primary-terrain-node ast-0015-encounter-level-3 ast-0016-giant-skeleton-soldier ast-0017-gravestone ast-0018-secondary-terrain-node ast-0019-giant-skeleton-archer ast-0020-lever ast-0021-trapped-encounter ast-0022-skeleton-beast ast-0023-shrine ast-0024-necromancer ast-0025-torch ast-0026-threat-level ast-0027-behaviour-deck-size ast-0028-block-resist-shield ast-0029-starting-health ast-0030-heat-up-point ast-0031-push-with-damage-satellite-glyph ast-0032-target-nearest-character ast-0033-enemy-movement-composite-symbol ast-0034-turn-90-right ast-0035-turn-90-left ast-0036-turn-around ast-0037-enemy-attack-composite-symbol ast-0038-area-attack-icon ast-0039-neutral-boss-arc ast-0040-attack-boss-arc ast-0041-weak-boss-arc ast-0042-deal-magical-damage ast-0043-one-handed-weapon ast-0044-weapon-upgrade ast-0045-two-handed-weapon ast-0046-armour-upgrade ast-0047-armour ast-0048-block ast-0049-upgrade-slots ast-0050-resist ast-0051-black-dice ast-0053-blue-dice ast-0054-node-attack ast-0055-orange-dice ast-0056-shaft ast-0057-shift ast-0058-push-affected-enemies ast-0059-taunt ast-0060-attack-range ast-0061-repeat-behaviour-or-attack ast-0062-dodge ast-0063-bleed ast-0064-frostbite ast-0065-poison ast-0066-stagger

## 8. Verification before you finish

Run the style check against a merged glossary (your deltas appended) and fix every violation; the chapter must report **Total violations: 0**:

```
mkdir -p /tmp/gl_NN && { cat 12_glossary.md; sed -n 's/^ADD \(.*\)$/\1/p; s/^AMEND \(.*\)$/\1/p' work/phase2a/glossary/NN_slug.md; } > /tmp/gl_NN/12_glossary.md
python3 tools/style_check.py 10_manuscript_chapter_NN_slug.md /tmp/gl_NN/12_glossary.md
```

Then re-read the chapter once as a player would: every rule has a trigger, an actor and an outcome; every "(see §…)" targets the map in §4; nothing is left half-written. Report back in under 150 words: sections written, findings applied / skipped (counts), number of change-log entries, glossary adds/amends, open issues. Do not paste the chapter into your report.

## 9. Working method

Make few, large tool calls. Write the skeleton (H1, intro, all H2 headings) first, then fill the sections in order, appending as you go. Do not spawn sub-agents. Do not modify `12_glossary.md`, `03_coverage_tracker.md`, `11_change_log.md`, other chapters, or anything under `tools/`. Do not commit. Draft in British English from the first word; do not plan to "fix spelling later".
