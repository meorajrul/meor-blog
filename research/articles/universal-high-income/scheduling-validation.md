# Scheduled release validation — 22 October 2026

Requested time: 26 October 2026, 09:00 Asia/Kuala_Lumpur (01:00 UTC). One-time thread heartbeat uhi-release-check-26-october-9am created and confirmed ACTIVE. Its local-time rule is anchored to 26 October at 09:00 with COUNT=1. Host timezone verified +08/+0800. No main/deployment action is scheduled.

Article remains draft=true with date and publishDate 2026-10-26T09:00:00+08:00. Direct owner scheduling request retained in review.json. The hash covers article, cited evidence and hero bytes. Main and deployment remain owner-managed.

Checks completed:
- Current shared checkout: python scripts/blog.py check passed (4 public, 5 drafts); Hugo 0.167.0 production build passed; check-output passed (31 HTML pages, 17 sitemap URLs, metadata/canonical/discovery and draft exclusion). Counts include unrelated existing content.
- Isolated origin/staging checkout: check passed (3 public, 3 drafts); Hugo production build and check-output passed (26 HTML pages). This checkout has the older output checker; current-checkout checks above separately exercise the newer checks. No unrelated validator or website changes were copied into the PR.
- Full article publication gate passed with explicit as_of 26 October in both checkouts after a temporary draft-flag-only change. The original flag was restored in finally blocks. Digest unchanged.
- Hugo production clock rehearsal, with only this flag temporarily false: article absent at 08:59 MYT, present at 09:00 MYT on 26 October. At-release output passed check-output (29 HTML pages in isolated checkout). A clock rehearsal is not evidence of live publication.
- Local preview with localhost baseURL: title, date, byline, AI disclosure and hero visually inspected in browser. The initial production-baseURL preview attempted to load the not-yet-live hero from production; local preview baseURL corrected that preview-only issue. Production hero exists in the generated page bundle output.
- git diff --check passed. No validator changes. Hugo reports existing theme deprecation warnings for LanguageDirection and LanguageCode. Vendored theme unchanged.

Scope limits: selected-source narrative review; no UHI affordability demonstration. Invented fiscal examples and conceptual causal pathway removed from active material; backup retained only under ignored .tools/. Source citations and structural checks cannot certify truth. The decorative hero is AI-generated and does not depict evidence or a predicted economy. LinkedIn copy delivered for owner use after the article is live; no LinkedIn account action.

Isolated release branch: codex/uhi-oct26-release. Main untouched. Source PR targets staging.

## Updated staging verification

Fetched current origin/staging (6d46e1c) and resolved the topics.csv append conflict by retaining both T019 UHI and incoming T025 security essay. No other upstream content changed. Repeated checks passed: 4 public / 3 draft posts; 31 production HTML pages; 34 HTML pages in the at-release clock rehearsal. The full article gate and 08:59/09:00 exclusion/inclusion test passed again. PR #23 targets staging. GitHub reported no check runs at inspection time; local checks are the verified evidence.
