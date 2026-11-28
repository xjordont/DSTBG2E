# Phase 3A — rulings brief (shared by every rulings researcher)

## The situation

`/home/user/DSTBG2E` holds a finished fan rulebook, "Dark Souls: The Board Game, Second Edition": a community second edition that rebuilds the published game. The manuscript is in `10_manuscript_chapter_NN_*.md` (chapters 00 to 23, chapter 21 being `12_glossary.md`). It is typeset and passes QA. What remains is a list of open rules questions, `14_open_issues.md` (22 lead items in its first table, then one list per chapter; the per-chapter lists are also in `work/phase2a/issues/NN_*.md`).

The author has now delegated every one of them:

> Use your best judgement as a pro boardgame designer to determine the best rulings. Reference the two official rulesets, the two unofficial rulesets, and online discussion of the game's rules and house rules. Ideally we would have clear, intuitive, simple, mechanically consistent, well written, and tactically interesting rules that do not lead to rules bloat or unnecessary complication.

You research and recommend. The lead editor decides and applies. You do NOT edit any manuscript file.

## Sources

| Source | Where | Standing |
|---|---|---|
| This book as drafted | `10_manuscript_chapter_*.md`, `12_glossary.md` | the baseline; its systems (hollowing, sparks, embers, tiers, node rules) are the author's design and are kept unless an item says otherwise |
| The author's source manuscript | `work/phase2a/source/NN_*.md` | what the author originally wrote |
| Gate 1 decisions | `05_gate1_decisions.md` | earlier answers; may be revised where the evidence is clearly against them, and you must say so explicitly when you propose it |
| Official core rules, 2017 | `work/text/DS-Core-Rules-lores.txt` (PDF in `sources/`) | official |
| Official rules, 2022 (Tomb of Giants / Painted World) | `work/text/DS-TG-Rulebook-Compressed_compressed.txt` | official, current |
| Official F.A.Q. | `work/text/Dark_Souls_The_Board_Game_FAQ.txt` | official |
| Official expansion booklets | `work/text/DS-{BDK,Characters,Darkroot,EC,Explorers,IronKeep,Phantoms}-*.txt` | official |
| Community ruleset "Extended Rules" | `work/text/DS-Extended-Rules-V45.txt` | unofficial, well tested |
| Community ruleset "Hollowed Edition" | `work/text/Hollowed_Edition_v1.3.txt` | unofficial |
| Online discussion | web search (BoardGameGeek forums, Reddit r/DarkSoulsTheBoardGame, the publisher's site and downloads, wikis) | evidence of how the rules play and where players struggle |

Web search: use it if the tool is available to you; keep queries generic (the game's name and the rule in question) and never put any personal or project detail in a query. If the web is unavailable or a site refuses, say so in the memo and carry on from the supplied sources. Do not invent sources; quote or paraphrase closely and give the file and line region, or the URL.

## How to judge

1. Simple beats clever. Prefer the ruling a player would guess. One rule that covers three cases beats three rules.
2. Consistent with the rest of this book: same procedure for like cases, same terms, same timing words.
3. Keeps decisions interesting: do not remove a real choice, and do not add book-keeping that carries no choice.
4. No bloat: if a question can be closed by deleting a special case, say so. Do not add a mechanic unless an actual hole needs it.
5. Where the book already answers the question and the answer is sound, the right recommendation is "confirm as written". Most items will be this.
6. Where official rules exist for a component and the book has none (for example a boss with placeholder rules), bring the official rule in, restated in this book's terms and adjusted only where this book's systems differ.

## What to deliver

Two files in `work/phase3/`, named for your cluster (`rulings_<cluster>.md` and `edits_<cluster>.json`). Write both incrementally (after each chapter or each five items) so that nothing is lost if you are interrupted.

### `rulings_<cluster>.md`

For every item in your scope, in order, one entry:

```
### <cluster>-NNN · <lead item number or chapter and a five-word label>
- Question: (one sentence)
- This book now: (what it says, with § reference)
- Evidence: official 2017 … / official 2022 … / Extended … / Hollowed … / online … (short, with file+line region or URL; write "silent" where a source says nothing)
- Ruling: CONFIRM as written | CHANGE | ADD | DELETE | NOT A RULES QUESTION (informational, nothing to decide)
- Why: (two or three sentences, as a designer)
- Mechanical: yes | no   (yes if play changes compared with the book as drafted)
- Edits: ids of the entries in the JSON file, or "none"
```

End the memo with (a) a table of every CHANGE, ADD, and DELETE; (b) anything you could not settle and why; (c) cross-cluster effects (another chapter, the glossary, the F.A.Q.) the lead editor must carry through.

### `edits_<cluster>.json`

A JSON array. One object per text change:

```json
{"id": "<cluster>-E01", "item": "<cluster>-NNN", "file": "10_manuscript_chapter_17_boss_special_rules.md",
 "section": "§17.10", "old": "exact text now in the file", "new": "replacement text",
 "type": "ruling|completion|clarification|correction", "mechanical": true,
 "rationale": "one sentence", "evidence": "short source note"}
```

- `old` must occur exactly once in the file (copy it from the file; include enough words to be unique). To insert, use a nearby sentence as `old` and repeat it inside `new` with the addition.
- Glossary changes: `file` is `12_glossary.md`, `old` the whole current entry line, `new` the whole new entry line. F.A.Q. changes go to `10_manuscript_chapter_22_faq.md` the same way.
- Every rule you change must stay consistent everywhere it is stated: search all chapters, the glossary, and the F.A.Q. for the same rule and include an edit for each place, or list the place under cross-cluster effects.
- Validate before you finish: load the JSON with Python and check that each `old` occurs exactly once in its file.

## The manuscript's style (binding on every `new` text)

Read `work/phase2a/DRAFTING_BRIEF.md` once for the full rules. In short: British English; lawbook voice, present tense, third person ("a character", "the players"), no "you" outside worked examples; no hedge words (may is permission, never possibility); no reference to any other rulebook, edition, publisher, website, or designer; no notes to the reader; defined terms in *italics* exactly as the glossary spells them; cross-references as "(see §N.M)" or "(see §N.M, Sub-heading)"; numbered steps for procedures; icons as `{{icon:ast-NNNN-slug}}` tokens only where the chapter already uses them. A worked example begins "*Example.*" and must compute correctly from the rules as they will stand after your edits.

## Limits

- Do not edit manuscript files, the glossary, or any tool. Write only your two files.
- Do not propose redesigns of systems that are not in question. Stay inside your scope; note anything you notice outside it under cross-cluster effects.
- Keep tool calls efficient (a usage limit applies): read whole files in one call, batch searches.
- Your final message: counts of CONFIRM / CHANGE / ADD / DELETE / NOT A QUESTION, and the five rulings you consider most consequential.
