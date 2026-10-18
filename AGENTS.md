# Personal journal project

The owner selected a **broad personal journal**. Preserve their voice and range; do not impose a corporate brand or AI-only topic strategy.

Read `START-HERE.md`, `editorial/workflow.md`, and the relevant `plugins/meor-journal/skills/*/SKILL.md` for editorial work. Read `research/findings.md` and `research/research-state.yaml` to resume this setup.

Website source: `site/`. Plugin source: `plugins/meor-journal/`. Old prototypes are preserved, ignored, and not the source of truth. Build with Hugo 0.167.0. Do not edit the vendored theme for local design changes; use `site/layouts` and `site/assets/css/extended`.

Distinguish memories and opinions from external factual claims. Never manufacture first-person events, feelings, quotes, evidence, numbers, research outcomes, or Meor's approval. A draft is not publication authorization. Existing user authorization remains valid for the work it covers.

Research packets and drafts tracked here are public on GitHub. Put sensitive notes in `private/` and do not stage them. Deploy only `site/public/`, never the repository root. The local CMS from the old prototype must not be deployed.

Run `python scripts/blog.py check`, a production Hugo build, and `python scripts/blog.py check-output --directory site/public` for website/editorial changes. Test gate rejection behavior when changing the validator. Record real results and limitations. A structural checker cannot determine whether a source is true or a citation entails a claim.

Keep plugin files self-contained. Use the repo marketplace for installation; do not scatter duplicate skill copies into `.agents/skills`. Keep source changes versioned and rebuild the package when its version changes.
