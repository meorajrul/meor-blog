# Start here

This is your personal journal. A reflection can be short and unfinished in thought; a researched essay needs evidence for the factual promises it makes.

1. Put an idea in `editorial/topics.csv`. Capture what made you notice it and what you want to explore.
2. Create a draft: `python scripts/blog.py new my-topic --genre reflection` (or `essay`, `field-note`, `review`).
3. Write in `site/content/posts/my-topic/index.md`. Keep private raw notes in `private/`, not in a tracked draft.
4. For external claims, use `research/articles/my-topic/`: brief, search log, inspected sources, and claim ledger. A reflection with no external factual claims can leave its source and claim arrays empty.
5. Choose a framework from `docs/frameworks.md`; it is a thinking aid, not a mandatory voice. When discovery matters, add the optional reader-search question, intent and original contribution to the brief; follow the SEO steps in `editorial/workflow.md`.
6. Use the blog review skill. Resolve gaps, record the actual review and author approval in `review.json`, then set `draft = false`. Agents must never invent author approval.
7. Run `python scripts/blog.py check`, build Hugo in production, and run `python scripts/blog.py check-output --directory site/public`. Use a `codex/` branch and a PR targeting `staging`; the owner handles `main` and deployment. Keep articles as drafts until the author explicitly approves them. After authorized publication, review indexing and search data when available.

Ask Codex naturally:

- “Use blog-topics to turn these notes into a few journal ideas.”
- “Use blog-research for this question, including evidence that challenges it.”
- “Use blog-think to compare a reflective opening with a clear argument.”
- “Use blog-write to draft from my notes without inventing my experiences.”
- “Use blog-review to tell me what must change before this can publish.”
- “Use blog-publish to check and publish the article I have approved.”

For the first launch, home and About can go live without pretending sample articles are finished. The included example article stays a draft.

## Local preview

On this Windows computer, run `./scripts/Preview.ps1`. The helper installs the pinned Hugo tool if missing and serves only on localhost. Use `-IncludeDrafts` when intentionally reviewing drafts; stop with Ctrl+C. No files are published.
