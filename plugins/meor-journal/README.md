# Meor Journal plugin — 1.1.0

The maintained source for a broad personal journal workflow. Skills: **blog-topics**, **blog-research**, **blog-think**, **blog-write**, **blog-review**, **blog-publish**, and the retained **evidence-backed-blog** advanced resource/visual workflow.

## Install

From the workspace root:

```powershell
codex plugin marketplace add . --json
codex plugin add meor-journal@meor-blog --json
codex plugin list --json
```

You can also add the public repository as a marketplace after it has been pushed: `codex plugin marketplace add meorajrul/meor-blog`.

Refresh or restart Codex if the new skills are not visible in the current chat. Do not copy duplicate skills into another discovery folder. Source lives here; Codex installs a cached copy. After source changes, bump the manifest version, package again, and reinstall/refresh through the supported plugin commands.

The repo marketplace and CLI commands follow [official packaging guidance](https://developers.openai.com/plugins/build/plugins). Packaging alone is not installation; actual observed status is recorded in the project verification report.

## Run without a plugin client

Python 3.11+ is enough for the deterministic helpers:

```powershell
python plugins/meor-journal/scripts/blog.py --root . new my-topic --genre reflection
python plugins/meor-journal/scripts/blog.py --root . check
```

The helper never approves an article, changes DNS, pushes Git or publishes. Review records are declarations that still require honest human/agent practice; a complete fixture can pass structurally while containing false claims.

## Package and improve

Run `python scripts/package-plugin.py` from the repository root. It validates the manifest, skills and relative resource links, then creates a ZIP and SHA-256 file under `plugins/packages/`. The archive contains plugin source, not personal articles, credentials, caches or the reference library.

Use the actual workflow on several author-approved entries before claiming benefit. Track consequential corrections and time spent if useful; optional controlled benchmarking remains **not run**. No reader study or model-quality improvement is asserted. The inherited evaluation reference is available only for an explicit future evaluation request.

SEO steps now connect briefs, writing, review, output validation and manual post-publication measurement; articles remain drafts until explicit author approval. See [SEO workflow](references/seo-workflow.md).

Support details: [editorial contract](references/editorial-contract.md), [frameworks](references/frameworks.md), templates in `assets/`, implementation in `scripts/`, and source research in the repository's `research/` folder. This package provides source and local installation; it is not submitted to the universal plugin directory.
