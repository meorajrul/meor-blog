---
name: blog-review
description: Review a journal draft for evidence fit, unsupported claims, numbers, first-person authenticity, voice, rights, privacy and publication readiness. Use before approving or publishing an entry.
---

# Blog Review


Read [the packet contract](../../references/editorial-contract.md). Review the actual article, evidence packet and any supplied author notes. Start with the headline, conclusion, all numbers and quotes, causal claims, recommendations and first-person assertions; then inspect other material factual claims.

For each consequential claim, verify that the cited source entails the actual wording and scope. Check origin groups, source inspection and locators, dates, sample, comparator, units, uncertainty and competing explanations. A working link is not evidence of relevance. A structural gate is not a substitute for this reading.

Check voice and narrative against the brief. Personal reflection may remain unresolved. Flag invented or unsupported biography; do not rewrite it as if confirmed. Verify permissions/rights and privacy for published material. For visuals, compare exports to inputs and inspect accessibility.

Write concrete findings in review.md: issue, implication, required change and actual evidence. Update review.json with real check outcomes and unresolved issues. Status remains pending until issues are resolved and actual author approval exists for the final version. Never infer author approval from a request to review.

After final wording and evidence are stable, print the digest with `python scripts/blog.py hash <slug>`. Record it only with the actual review. Use current official sources and a review_by date for time-sensitive entries. Run the structural gate and report its results separately from editorial judgment. If content or evidence changes, re-review the affected material and update the digest.

Return publish-ready, revise or hold with reasons. This assesses readiness, not truth certification or formal peer review.

For requested SEO, AI search or ranking reviews, read [the SEO workflow](../../references/seo-workflow.md). Separate crawl eligibility, documented platform practices and observed performance; leave unsupported ranking effects open.
