# Scheduled-release preparation — 19 October 2026

The owner’s direct instruction, “set this to be release on 20th october 9am”, approves the delivered illustrated essay for 20 October 2026 at 09:00 Asia/Kuala_Lumpur (01:00 UTC). Its body, hero and three charts were unchanged. The date and approval/scheduling records were updated, then a new digest was recorded.

Approved digest: `19ff25e63231984ec5e4e9d0d9b42f6a2f92264b954850b175b93897fa151e4f`.

Release preparation uses a separate managed worktree on `codex/schedule-msme-oct20`, based on origin/staging. Only the selected article, its evidence/assets, supporting upstream research and the T016 topic entry are included. Unrelated local drafts and topic changes are excluded. The selected trees were scanned for common credential/private-key patterns; none matched. This is a limited check, alongside the earlier privacy review.

## Checks actually performed

- In the release worktree, `python scripts/blog.py check` passed with 1 public entry and 3 drafts.
- Hugo 0.167.0 production build passed. Current `check-output` passed across 16 HTML pages: links, source boundary and draft exclusion. This essay is absent from current production output.
- A temporary release rehearsal changed only this article’s draft flag, preserving the approved digest, and ran the full article gate with as_of 20 October 2026. All approval, evidence, citation, asset, date and hash checks passed.
- Hugo’s explicit clock test excluded the article at 08:59 MYT on 20 October and included it at 09:00 MYT. The at-release artifact passed check-output across 23 HTML pages. This is a local clock simulation, not evidence of live publication.
- The temporary flag was restored in a finally block. The committed preparation remains draft=true to prevent early publication.

No validator or deployment workflow was changed. Existing Hugo theme deprecation warnings remain.

## Scheduling boundary

A single thread heartbeat is to run the release check at the requested time. It must verify the approved digest, flip only this article’s draft flag after the time arrives, run current release checks and update or create a PR targeting staging. Actual PR/automation identifiers are recorded in schedule.json once returned by their tools.

The standing repository instructions reserve main and production deployment for the owner. The automation cannot guarantee live publication at 09:00; it prepares the release and reports the remaining manual merge/deployment. It must not touch main, dispatch its deployment or claim publication without checking the live page.
