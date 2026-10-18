# Folder and naming guide

Use lowercase descriptive slugs, e.g. `learning-to-notice`. Keep a stable published slug even if the title changes.

```text
site/content/posts/learning-to-notice/index.md    publishable article
site/static/images/learning-to-notice/           cleared public images
research/articles/learning-to-notice/brief.md    question and scope
research/articles/learning-to-notice/search-log.csv
research/articles/learning-to-notice/sources.json
research/articles/learning-to-notice/claims.json
research/articles/learning-to-notice/assets.json
research/articles/learning-to-notice/review.json
research/articles/learning-to-notice/review.md
private/learning-to-notice/                      local-only raw notes
```

Keep raw data and derived data separately in the article packet when used; include the transformation script and units. Cite a source ID in the ledger and a normal URL in article prose. A source can have multiple claim mappings but should keep the same source ID. Sources sharing an underlying study share an origin-group identifier.

`research/literature/` is the shared workflow reference library. `research/articles/` holds the evidence for individual posts. `editorial/topics.csv` tracks ideas; the article's `draft` value and review determine publication readiness.

Use plugin templates and helpers so these paths stay consistent. The previous prototype folders are preserved for recovery; edit the new folders for all future work.
