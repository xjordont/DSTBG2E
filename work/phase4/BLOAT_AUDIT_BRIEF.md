# Phase 4 — bloat audit brief (shared by every auditor)

## Situation

`/home/user/DSTBG2E` holds a fan rulebook. The author's ORIGINAL manuscript was 20,700 words of terse bullets (per-chapter copies in `work/phase2a/source/NN_*.md`). After an editorial pipeline the FINAL manuscript is 77,500 words (`10_manuscript_chapter_NN_*.md`; the glossary is `12_glossary.md`). The author now says, in their own words: the book has "so much rules bloat and excessive wordage", and asks for an audit "to avoid redundancy, bloat, unintuitive rules, or introduction of excessive rules bloat", taking "my original manuscript for the baseline starting point" and determining "how we ended up" here.

You audit a group of chapters. You change NO manuscript file. You write one report file.

## What counts as bloat (classify every paragraph, list, table and example of the final text)

- **K keep**: the author's rule (it is in the source), or a rule the game cannot be played without, stated once and tightly.
- **R restated**: a rule owned by another section (or by another paragraph of this one) said again. Say where the owning statement is.
- **X cross-reference clutter**: "(see §…)" parentheticals and pointer sentences that add no rule. Count them per section; do not list each.
- **D defensive**: negative or edge-case sentences that pre-empt a question almost no player would ask ("A … does not …", "even if …", "whether or not …", "A … is not a …"), and sentences that only say that a general rule also applies here.
- **A added rule**: a rule, procedure, step, exception or term that is NOT in the author's source. For each, find what introduced it (search `11_change_log.md` for the section; entries cite an audit finding such as A-073, a completion CMP-00NN, a Gate 1 answer OQ-NN, or a final ruling such as core-E12 / lead-E05 / VA-015) and judge it: A1 needed (the game has a hole without it; say what breaks), A2 could be one sentence instead of a procedure, A3 not needed (delete; play is the same or simpler), A4 makes play less intuitive than the author's version or than what a player would guess.
- **E example**: worked examples. Judge each: earns its place (the rule is hard without it) / could be half the length / not needed.
- **V verbose**: the rule is needed but takes far more words than necessary (legalistic phrasing, definitions repeated inline, lists that could be a table, a table that repeats the text).
- **G glossary-in-chapter**: bold inline definitions that duplicate a glossary entry.

## How to judge

The author's standard: clear, intuitive, simple, mechanically consistent, well written, tactically interesting, no rules bloat. The author's own text is the model of length: one short sentence per rule. Where the final text says in 60 words what the source said in 15 and nothing is gained, that is bloat. Where the source was truly ambiguous or silent and play breaks, a short fix is legitimate. Be concrete and unsentimental: this pipeline's own additions are what is on trial, including rulings that looked careful when written. Do not defend text because a previous pass verified it.

Content the author asked for explicitly and that is NOT on trial as content (only for wordiness): the full boss rules taken from the expansion booklets (chapter 17) and the four added campaigns (§19.13 to §19.16).

## Deliver: `work/phase4/bloat_<group>.md` (write it incrementally, one chapter at a time)

For each chapter:

1. A table, one row per H2 section: `| § | source words | final words | K | R | X count | D | A | E | V | words it needs |`. Word figures by counting (use Python, `len(text.split())`), class columns as approximate words of the final text in that class, and your estimate of the words the section needs.
2. **Added rules** (class A): one line each: `§ · what was added (≤ 20 words) · introduced by (change-log id / finding / ruling) · A1|A2|A3|A4 · recommendation`.
3. **Worst passages**: up to six per chapter. Quote the final passage (trim with … if long), give the source's version if there was one, and write the passage as you would cut it, in the book's voice (British English; third person; "a character", never "you"; no hedging; no reference to other rulebooks). These rewrites are illustrations for the author, not edits.
4. **Unintuitive or over-engineered rules**: anything a new player would trip on or have to look up twice, with the simpler rule you would put in its place and what, if anything, is lost.

End the file with:
- **Totals** for your group: source words, final words, words needed, and the split of the excess by class (R, X, D, A, E, V, G) in words and percent.
- **How it happened**: the five or six mechanisms that produced the growth in your chapters, each with two concrete instances (section and change-log id where there is one).
- **Ten cuts** that would remove the most words with the least loss, in order.

## Practical

- Read the source chapter first, then the final chapter, then search the change log for what you need (`grep -n "CH-NN-" 11_change_log.md`, entries are `### CH-NN-KKK · section` with Type / Before / After / Rationale / Source lines).
- Keep tool calls efficient; a usage limit applies. Read whole files in one call. Save the report after each chapter.
- Final reply to the lead: the totals, the mechanisms in one line each, and the five added rules you would most want removed or simplified.
