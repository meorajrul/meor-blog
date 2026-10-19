# Scheduled release validation - 19 October 2026

Isolated staging checkout: gate passed (1 existing public article, 2 drafts). Hugo 0.167.0 production build and output boundary/link checks passed. Existing theme language deprecation warnings remain. Scheduled article excluded from current production output.

A separate scratch copy set draft=false and validated the release packet with as_of=2026-10-23: passed, including sources, claims, assets, approval and digest. This was a simulated date for preflight, not early publication. No validator code was changed.

Actual state: date=2026-10-23T09:00:00+08:00, draft=true, author_approved=true. A scheduled run can prepare release on a codex branch/staging PR; main and deployment remain owner-managed.
