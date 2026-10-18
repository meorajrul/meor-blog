# Article packet contract

Default workspace: Hugo content at `site/content/posts/<slug>/index.md`; packet at `research/articles/<slug>/`. Use the bundled `scripts/blog.py` with `--root <workspace>` from any installation. It creates a packet and never marks author approval.

The article uses TOML frontmatter with title, description, slug, article_id, genre, date, draft, tags, and time_sensitive. Supported genres: reflection, field-note, essay, review. A packet has brief.md, search-log.csv, sources.json, claims.json, assets.json, review.md and review.json. Templates are under `assets/`.

Sources are objects with id, title, url, publisher, accessed, inspection, locator, origin_group and appraisal. `inspection` must be `inspected` for published evidence; record inaccessible sources without pretending inspection. Claims have id, text, kind, source_ids, locator, status, confidence and limitations. External facts, calculations and source-based inferences require evidence IDs and a URL in the prose. A reflection can have no external claims; a researched essay/review cannot have an empty ledger.

Assets have id, path, alt, rights, attribution, source_url, kind, and input_paths. Paths must stay inside the workspace and resolve to actual files. Give charts their data and transformations, caption and accessible equivalent. Empty assets is valid for text-only entries. Rights and citation meaning require human judgment.

For publication, review.json requires status `approved`, `author_approved: true`, a named reviewer, reviewed_on, no unresolved issues, positive check flags, and the final `content_sha256` from the helper. For time-sensitive entries, review_by must be a current or future ISO date. Record author approval only when supplied. The digest includes the article and evidence records, normalizes newlines and the draft flag, and excludes review.json itself. The helper never certifies truth or actual approval.

Read `scripts/blog.py --help`. `new` is idempotent-by-refusal: it refuses existing paths. `hash` reads without approval changes. `check` checks public posts and structural metadata on drafts. `check-output` checks local production links and boundary files. The release script packages source only. No command pushes or publishes by itself.
