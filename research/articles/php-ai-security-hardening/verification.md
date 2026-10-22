# Verification — 22 October 2026

- `python scripts/blog.py check`: passed; 3 public posts and 5 drafts at the time of checking. Draft checks cover structure, not semantic evidence review.
- Production build with Hugo 0.167.0: passed. Existing theme emitted deprecation warnings for LanguageDirection and LanguageCode. Theme was not edited.
- `python scripts/blog.py check-output --directory site/public`: passed; 26 HTML pages, 14 sitemap URLs; internal links, source boundary, draft exclusion, SEO metadata, sitemap consistency and article discovery passed.
- JSON packet consistency: 8 unique sources; all 11 claims have valid references; every material external fact/inference has source IDs; cited sources have inspected status and locators.
- No validator changes, exploitation experiments, live security scan, deployment, publication, or operational hardening performed. No browser visual QA performed for this text-only draft. Existing unrelated working-tree changes were preserved.
- Editorial evidence review and limitations are recorded separately in review.md. Successful structural checks do not establish source truth, citation entailment or author consent.

## Mythos/Node.js revision — 22 October 2026

Required checks rerun after revision: article gate passed (3 public, 5 draft); production Hugo 0.167.0 build passed with the same two theme deprecation warnings; output checks passed (26 HTML pages, 14 sitemap URLs, draft exclusion included). Packet references checked: 11 unique sources, 15 claims with valid source references. Review digest renewed; author approval remains false.

## Hero and CVE timelines — 22 October 2026

Generated hero inspected. Both PNG chart exports visually inspected; margins adjusted after initial inspection. Exact data checks: 10 non-overlapping monthly queries, 21 non-overlapping daily queries; 85,344 YTD and 12,543 October; daily October sum equals monthly query. Raw response checksums verified. Exported CSV copies match preserved inputs. All cited claim source URLs are present in selected-story draft and all asset input paths exist.

Draft build with Hugo 0.167.0 succeeded to isolated .cache/php-security-draft-preview. Rendered HTML checked: selected title, hero plus two charts (3 images), and all linked CSV/PDF/method resources present. PNGs inspected; no browser screenshot of the page performed. The generated image is illustrative. Detailed CVE-record request timed out; no severity breakdown claimed. NVD documentation HTML returned 403; direct API JSON queries succeeded.

Required checks rerun after changes: article structure gate passed (3 public, 5 draft); production Hugo 0.167.0 build passed; output check passed (26 HTML pages, 14 sitemap URLs, internal links, source boundary, draft exclusion, SEO, sitemap consistency and discovery). Existing theme emitted the same two deprecation warnings. No publication or deployment. Structural checks do not establish truth or approval.

## Hero remake verification — 22 October 2026

Generated digital-bug/cell hero visually inspected. Cover references hero-v2.png; alt, caption, provenance and asset checksum updated. Required structural check passed (3 public, 5 draft), production Hugo 0.167.0 build passed with existing theme deprecation warnings, and output checks passed (26 HTML pages, 14 sitemap URLs; draft exclusion included). Original hero retained. No publication.

## Framework perspective verification — 22 October 2026

New advisory claims checked against original passages and all evidence references resolve to cited URLs in the article. Required check passed (3 public, 5 drafts); production Hugo 0.167.0 build passed with existing theme deprecation warnings; output checks passed (26 HTML pages, 14 sitemap URLs, draft exclusion included). Hero and timeline data unchanged. No deployment or publication.

## Approved release verification — 22 October 2026

Release prepared from origin/staging be7c3a7 in isolated codex/php-security-release-2026-10-22 checkout. Source/evidence copied for this article only; unrelated workspace changes excluded. Article draft=false with actual author authorization and date 22 October 2026 +08:00.

- Publication packet check: passed; 4 public, 2 drafts on current staging base.
- Production Hugo 0.167.0 build: passed; existing theme deprecation warnings.
- Output checks: passed; 31 HTML pages, internal links, source boundary and draft exclusion.
- Additional direct inspection: exact canonical, absence of noindex, feed and sitemap inclusion; hero and 2 charts; 3 framework rows; CSV/PDF/method downloads exist.
- 23 release gate tests passed with TMPDIR=/private/tmp. Initial default macOS temp-path run had one error due /var versus /private/var resolution, not article content; no validator change made.
- Five maintainer advisory URLs returned HTTP 200 in same-day release check. Retained chart snapshot intentionally not replaced.

PR targets staging; no main push or live deployment performed. No full browser screenshot of the published page was performed. Tests and structural checks do not validate source truth or establish AI causality.
