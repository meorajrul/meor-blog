# Project plan and decisions

## Intended result

A broad personal journal on GitHub Pages, with meorajrul.com as its canonical domain, an understandable workspace, and a versioned plugin that supports repeatable writing without inventing the author's experience.

## Decisions

- Reuse Hugo 0.167.0 and the existing pinned PaperMod theme; keep old staging intact. Hugo produces static HTML, RSS, sitemap, and a search index.
- Keep web source in `site/`, editorial planning in `editorial/`, evidence in `research/`, and maintained skills in `plugins/meor-journal/`.
- Use genre-aware methods: reflection, field note, researched essay, or review. Evidence burden follows claims, not a word-count or citation quota.
- Prefer a small set of durable tags rather than a fixed subject niche. English is the starting language inherited from the prototype; other languages can be added without changing the workflow.
- Publish via a tested GitHub Actions workflow on main. Only Hugo production output becomes the Pages artifact.
- Use a repo marketplace and a source ZIP for the plugin; record installation separately from packaging.

## Research sufficiency

Before concluding this setup, each requested area must have an inspectable reference and an explicit implementation: topic capture, evidence validation, folder structure, thinking, story, publication, and reusable skills. Framework notes distinguish original guidance from our adaptation. Inspect contrary evidence or limitations. Run concrete good/bad scenarios and production checks. Record unresolved external access honestly.

Two additional targeted search passes should stop changing the core design or leave only clearly bounded gaps. This is a practical stop rule authored for the project, not a validated measure of exhaustive literature coverage. More citations alone are not a reason to continue.

## Completion sequence

1. Source register, synthesis, source cards, workflow, and framework guide.
2. Article templates and repeatable skills; claim validation and release scripts.
3. Synthetic scenario tests and a real example packet kept as a draft.
4. Production build and served-output checks; plugin installation and ZIP verification.
5. Repository push, Pages setup, DNS setup where access permits, and live verification.

## Maintenance

Before a time-sensitive post, recheck relevant official sources and record a review-by date. Monthly, inspect the topic inbox and correction log; quarterly, exercise the publication gate and update pinned dependencies after a fresh successful build. These are suggested routines, not scheduled jobs. Setup heartbeat ends after this project report is complete.
