# Workflow scenario results

The bootstrap commit locked the protocol before execution. This is an engineering check, not a preregistered scientific study or a benchmark of prose quality. Raw output is in test-output.txt and machine-readable results in results.json.

- H1: a complete synthetic reflection with an empty external-claim ledger passes structurally; actual missing author approval is rejected. No real author approval was created.
- H2: unresolved claims, unknown source IDs, uninspected sources, missing source locators, duplicate source IDs, and missing prose citation URLs are rejected.
- H3: changed article/evidence, pending review issues/checks, stale time-sensitive reviews, future review dates, unresolved asset rights, unsafe paths, missing packets, and missing draft flags are rejected. Scaffolding refuses overwrite. Changing only the draft flag preserves the normalized digest.
- H4: production Hugo output passed canonical and internal-link checks across nine HTML pages. The real example draft, local CMS and repository source folders are absent from the served output. Required RSS, sitemap, search, robots and domain files exist.

23 synthetic test cases passed. Separate production and browser checks are recorded in docs/verification.md. Initial visual inspection found a homepage template-context error, encoding damage and theme selector mismatch; these were repaired before deployment. The pinned theme still emits two non-failing Hugo deprecation warnings.

A fabricated fixture with complete declarations can pass this gate. Honest source inspection and actual author approval remain necessary. No evidence here establishes improved reader outcomes or better model writing than a normal prompt.
