# Validation — first-job article revision, 23 October 2026

Owner requested implementation of the recommended first-job focus. Article date remains24October2026at09:00MYT; source remains draft=true for scheduled release preparation. Review and schedule digest: `0a534852480c428d0718ac332be8a056b234c591ae8ae2dabcb9e82d314449c9` (identical in primary workspace and staging worktree).

- Primary journal check passed:4public,6draft. Hugo0.167.0 production build passed:36pages. Output checks passed:31HTML,17sitemapURLs, links, source boundary, draft exclusion, SEO metadata, sitemap consistency and article discovery.
- Staging worktree check passed:2public,2draft. Production build passed:28pages. Its narrower output checker passed:23HTML, links, source boundary and draft exclusion.
- Full current publication gate passed for an isolated scratch copy with draft=false and as_of24October2026. Actual article remains draft=true. No validator or theme modifications.
- Preview rebuilt in C: output folder served on loopback1338. Browser verified new title,24Octoberdate, all5article images loaded, and no horizontal overflow. Screenshot saved in task visualization folder as first-job-article-preview.png. The Singapore image initially awaited lazy loading; scrolling to its section confirmed it loaded.
- New charts visually compared with source transcription: US approximate -11/+10, Singapore19/14/8/6. CSVs, vector PDFs, code and environment record retained. Missing Singapore fieldwork dates explicitly disclosed.

Existing theme warnings concern LanguageDirection/LanguageCode deprecations. These checks establish structure/rendering, not truth, causal identification, generalisability or policy effectiveness. No main merge or production deployment performed.

## Hero replacement — 23 October 2026

Owner-requested generated hero installed; US chart preserved inline. Current digest8d2e331dfbc9a69e6f6bfd62d34e979ef9400993c3059e49e8f9557dd26d67da. Primary and staging checks/builds/output checks passed with the same counts and existing theme warnings as above. Isolated scheduled-release gate passed as_of24October. Browser confirmed hero loaded, US chart present in body and no horizontal overflow. Screenshot: hero-article-preview.png in task visualization directory. Built-in image tool; prompt and generated asset saved in repository. Publication date unchanged; no deployment.

## Publication setting — 24 October 2026

Owner approved current edited article with “set it to publish and gave me linkedin short story to tell”. Preserved owner wording changes, set draft=false, retained24October09:00MYT. Current digest9045f150d5f6db5fa74f5e3586b97325bc1c9b0201886ea2450242502b5e710c. Review/schedule records updated honestly.

Release worktree: journal check passed(3public,1draft); Hugo0.167.0 production build33pages; output checks28HTML, local links/source boundary/draft exclusion passed. Verified actual article production HTML, hero, canonical https://meorajrul.com/posts/ai-beginner-work-malaysia/ and sitemap entry.

Primary workspace: required journal check failed because separate php-ai-security-hardening time-sensitive review expired. No unrelated article edited. Primary production build42pages and full output checks37HTML/21sitemapURLs passed, including metadata/canonicals/discovery. Existing theme deprecation warnings remain. Structural checks do not establish citation entailment or source truth.

Release branch/PR target staging; main and deployment owner-managed. Source publication setting is enabled; do not represent this as verified live deployment. LinkedIn draft saved, not posted. Live URL could not be verified using web open in this run.
