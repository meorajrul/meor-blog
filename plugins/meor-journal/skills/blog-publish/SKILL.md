---
name: blog-publish
description: Validate and publish an author-approved Hugo journal entry through the existing GitHub Pages workflow, or diagnose its deployment and custom-domain status.
---

# Blog Publish


Respect publication authorization already given in the conversation. When only drafting/review is requested, prepare a concrete release candidate without publishing. Confirm actual author approval for the article from trusted user context and the review; never manufacture it.

Read [the packet contract](../../references/editorial-contract.md) and the project's deployment guide. Inspect the final diff and repository status. Ensure private notes and credentials are excluded from staging. A public repository exposes tracked drafts even when the website excludes them.

Run the project `check`, tests if the gate changed, a production Hugo build, and `check-output`. Resolve failures. Verify canonical domain, RSS/sitemap, production draft exclusion and readable links. Preview the actual output when available and state any QA limit honestly.

After approval, set the article draft flag false and record the reviewed final digest. Stage only intended source and evidence cleared for the public repository. Commit and push within authorized scope. Inspect the GitHub Actions result and actual Pages response; an attempted push is not a verified deployment.

For custom domains, set the repository Pages domain as well as DNS. With Actions, CNAME alone is insufficient. Use the official GitHub docs for current records, inspect existing DNS before changes, preserve mail/TXT records, and verify DNS and certificate state separately. Do not claim HTTPS complete while issuance is pending.

Record the published URL, commit, actual checks, and unresolved dependencies. Corrections require updated evidence, a fresh review, and a material correction note where appropriate. Do not schedule a recurring monitor unless requested.

For search and sharing changes, use [the SEO workflow](../../references/seo-workflow.md). Verify canonical share URLs and decoded query parameters, exclude drafts and non-post pages, and report browser/composer verification limits. Use codex/ branches and PRs targeting staging; the owner handles main.
