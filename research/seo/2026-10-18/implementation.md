# SEO implementation — 18 October 2026

Status: implemented and verified locally on codex/journal-seo-workflow. No push, PR, merge or deployment. The author retains article approval and main-branch publication.

## Changes

- Added optional search-discovery questions to the brief template, discovery findings to the review template, and SEO steps to the editorial workflow and all seven blog skills. Shared guidance is self-contained in the plugin's references/seo-workflow.md. Reflection remains free of keyword targets, quotas and prescribed length.
- Kept the article approval/digest contract intact. Article files and existing review records were not modified; the sole current article remains draft=true and author_approved=false. New articles still scaffold as drafts.
- Added local Hugo overrides for a single robots directive, development noindex, production noindex on utility/empty taxonomy pages, sitemap filtering, exact pagination canonicals and distinct pagination titles. The sitemap now has three URLs: Home, About and Journal.
- Added Person/WebSite identity, ProfilePage for About, BlogPosting only for actual posts, linked author profiles, safely serialized JSON and conditional real dates. Search has no article schema or year-0001 dates. Added a descriptive homepage title and visible author link to About.
- Strengthened production validation for metadata, exact canonicals, noindex/sitemap conflicts, schema types/dates, genuine inbound navigation links and draft URLs leaking into HTML, RSS or the JSON search index. The existing source-boundary and approval gates remain.
- Moved CI tests after pinned Hugo installation so render integration tests execute there. Deployment conditions still require main and do not deploy pull requests.
- Packaged Meor Journal 1.1.0 and refreshed it through the existing repo marketplace. Installed and enabled status observed; all 27 installed source files match the maintained source byte-for-byte. No duplicate skill copies added.

## Actual verification

- 55 tests pass: 23 existing article approval/evidence cases, 29 output cases and 3 Hugo render integration cases. Rejection cases include unapproved release, changed content/evidence, noindex Home, indexed utility/empty taxonomy pages, wrong same-domain canonicals, duplicate directives, invalid metadata, orphan articles and draft URLs in discovery outputs.
- Render tests use disposable site copies, including ten synthetic public fixtures to exercise pagination and populated taxonomies, JSON escaping, author identity and preview noindex. These are engineering fixtures, not real article approvals or publication.
- python scripts/blog.py check: public=0, draft=1.
- Pinned Hugo 0.167.0 production build succeeds; check-output passes for nine HTML files and three sitemap URLs, local links, source boundaries, draft exclusion, SEO metadata and article discovery.
- All seven skills pass skill-creator validation. Plugin package and archive integrity checks pass. Final archive SHA-256: 5a9badfa61f2ffb816c06b944fe6b384afb52d80379ea1d3f13ace4c950414f2.
- Existing article content, approval packets and vendored theme have no diff against HEAD. Unrelated pre-existing topic inbox changes and topic briefs were preserved.

## Limits and later release

Two pre-existing PaperMod language-property deprecation warnings remain; the pinned build succeeds. No new browser/mobile, PageSpeed, Rich Results Test, Search Console or ranking measurement is claimed. The source has been tested locally; these fixes are not yet on the live website. Search Console account setup and post-publication measurement remain owner-authorized follow-up work.

Current instructions use codex/ branches and PRs to staging. Only origin/main was present in the local remote-ref inventory; no staging branch or PR was created, and main was not changed. Publication remains with the owner. Raw private performance exports belong in private/.
