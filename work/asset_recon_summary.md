# Asset reconnaissance — summary

**Scanned:** 12 PDFs (10 official SFG, 2 community) — every page rendered at 80 dpi and inspected; `pdffonts` and `pdfimages -list` run on all; 9 encrypted files re-saved with pypdf.

**Catalogued:** 163 assets in `22_asset_extraction_log.md` (AST-0001–AST-0163). **Extracted in Phase 0:** 114 files in `assets/` (61 icons from the 2022 reference page, 5 logo files incl. vector SVG, 11 ornaments/frames (SVG + PNG), 6 textures incl. the 5174×3378 px print-master page background, 21 anatomy/worked-example diagrams, 8 type specimens, 2 cover items). **Still to extract:** 1 (not designated). **Phase 2B added:** 162 files for 25 catalogue assets (98 component images incl. composites, 5 diagrams, 46 icons, 10 frames and card backs, 3 textures); 1 marked not required, 3 BLOCKED, 12 candidates listed for provenance review (log, Provenance Review F). Hero list for the layout: `layout/hero_assets.json`. **Phase 3 added (provenance confirmed by the author, 2026-11-11):** 220 files for 26 catalogue assets (110 paintings and illustrations, 68 card faces, 40 dashboards, card fans, miniature renders and game boards, 0 special-rule plates, 2 tokens), including the eight mega-boss expansion booklets (AST-0156 to AST-0163). Designer's list: `layout/art_candidates.json`; contact sheets `build/art_contact*.jpg`. **Provenance review:** closed on 2026-11-11 by the author's confirmation; 0 catalogue entries still held.

**Fonts:** display OptimusPrinceps (+SemiBold, freeware); body Adobe Caslon Pro Regular/Italic/Bold/Semibold (commercial); Arimo (open) for utility text; Helvetica in one credits block. None installed locally. Proposed: Cinzel for display, Libre Caslon Text (or EB Garamond) for body, Liberation Sans for utility.

**Palette:** parchment `#f4f2ea`, ink `#231f20`, gold accent `#9c8141`/`#b77e2e`, cover black `#110f0e`; functional colours red `#ce4c4a`, magenta `#b556a7`, blue `#3ca2e0`, orange `#f89a0f`, green `#36b876`.

**Decisions needed from the lead**
1. RESOLVED 2026-11-11: the author confirmed ownership of all source material, painted illustrations and artwork, so the key art is cleared and extracted (Phase 3).
2. Use of the DARK SOULS™ wordmark in the 2E title versus a nominative mention.
3. Whether to request original card/dashboard artwork from the owner — embedded card rasters are ≤372–1000 px, too small for print.
4. Approve the font substitutions (Cinzel / Libre Caslon Text) so they can be installed.

Manifest: `21_asset_manifest.csv` (539 rows). Catalogue data: `work/asset_catalogue_final.json`. Icon label check sheet: `work/icons_contact.png`.
