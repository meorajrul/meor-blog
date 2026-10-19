# Verification — 19 October 2026

## Research packet

- 22 source records parse; unique source IDs and links resolve within the briefing's reference set.
- 25 claim records parse; source-based facts/inferences have source IDs and all IDs exist.
- 40 actual search queries recorded in search-log.csv. Selection decisions describe evidence screening; no systematic-review counts asserted.
- All 22 registered source URLs appear in Markdown and HTML. This is a cross-reference check, not a new remote-availability test or entailment guarantee.
- Three hypothetical savings scenarios independently recalculated for first-year and later annual results. Inputs remain explicitly hypothetical.
- HTML contains eleven second-level sections and no script dependencies. The initial structural check expected ten sections, overlooking the opening answer section; that assertion was corrected and rerun successfully. No visual screenshot QA was performed. Opening in Codex was queued by the app.
- One topic row T016 registered. No article created; no approval, push, PR or deployment performed.

## Required project checks

- python scripts/blog.py check: exit 0; public 0, drafts 2.
- Hugo version verified: 0.167.0. Production build: exit 0; 14 pages generated, 8 static files and 2 aliases.
- Hugo emitted existing theme deprecation warnings for LanguageDirection and LanguageCode. No vendored theme edited.
- python scripts/blog.py check-output --directory site/public: exit 0; 9 HTML pages and 3 sitemap URLs checked. Internal links, source boundary, draft exclusion, SEO metadata, sitemap consistency and article discovery passed.
- Validator unchanged, so no validator-rejection test suite was required.

These checks establish structural consistency and draft exclusion, not source truth, causal effects, author approval or current agency performance. Unrelated pre-existing draft/topic changes were preserved.

## KRI original provenance

Publisher CDN PDF inspected locally in temporary storage: 64 pages, 1,416,560 bytes.
SHA-256: 3639d44012481e26278b38ec16c3391ddc9d57e08fda825036256c7790978e28.
The temporary original is not a committed research asset. Its publisher URL is recorded in sources.json. Source notes preserve the inspected page locators.
