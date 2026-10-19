# Validation — illustrated draft, 19 October 2026

## Actual checks
- Journal gate passed: 1 existing public article and 4 drafts including this new draft.
- Production build passed using Hugo0.167.0. Existing theme language-property deprecation warnings remain; no theme files changed.
- Production output gate passed:16HTML pages,8sitemap URLs; internal links, source boundary, draft exclusion, metadata, sitemap consistency and article discovery.
- A separate development build with drafts produced the local review page; production draft exclusion remained intact.
- Hero and both chart exports visually inspected. The World Bank source figure was also rendered locally to verify all10rounded age percentages.
- Rendered article inspected in the in-app browser on a1265px-wide desktop viewport, including heading, hero, both charts and captions. No desktop clipping observed. Mobile viewport was not separately tested.
- Asset/source/claim references and downloaded CSV equality checked separately. Figures preserve original data inputs, generator and vector PDFs.
- Review digest stored in review.json after final draft wording. It records a pending review, not author approval.

## Limitations
The structural gate skips full evidence checks for drafts. S1 remains abstract-level and must not be relabelled as full-text inspected. Source truth and citation entailment require editorial judgment. Malaysian exposure uses2021employment composition and cannot establish present hiring effects. The learning-time comparison is an approximate narrative summary, not an exact effect or confidence interval.

## Output state
New article is draft=true; author_approved=false. No commit, push, PR, publication or deployment performed. Existing work in other article folders was preserved.
