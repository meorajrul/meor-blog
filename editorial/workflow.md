# From a noticed moment to a published entry

## Capture and choose

Use `topics.csv` as an inbox, not a compulsory content calendar. Sources of ideas include supplied personal notes, questions that keep returning, conversations you may ethically describe, projects, books, and public research. Record the origin without exposing private details. Proposed prompts are not claims about Meor's experiences.

Once a week or when ready to write, choose by personal interest, specificity, reader value, evidence availability and effort. Use 0–2 for each criterion if useful; record effort separately. No search-volume target or posting quota is necessary for a personal journal. An authentic small observation can outrank a fashionable topic.

## Brief and genre

Create a packet with `python scripts/blog.py new <slug> --genre reflection|field-note|essay|review`. State one question, intended reader, provisional view, geography/time scope and what would count against it in `brief.md`. Tag sensitive or third-party material for private handling.

A reflection needs truthful author-supplied experience and clear boundaries on generalizations. An essay or review needs inspected evidence for its material external claims. A field note records what was done, when, and under what conditions; distinguish observation from inference. Technical instructions must include actual versions and checks.

## Inner loop: one evidence gap

Select the most consequential unsupported claim. State what evidence would support or challenge it, then search and inspect the original source. Log the actual query, date, platform and selection decision; do not invent screening counts. Register source ID, canonical URL, author/publisher, date, exact locator, inspection status, origin group and appraisal. Cross-check who is behind unfamiliar sources (R06).

Check method, population, comparator, measurement, uncertainty, conflicts and relevance. For recommendations, seek contrary evidence and realistic alternatives. For personal experience, obtain the author's wording; do not outsource memory to research. Narrow, qualify, remove or defer claims the evidence cannot support.

## Outer loop: revise the view

After a few meaningful checks or a surprise, write a short synthesis: what is now supported, what conflicts, how confidence changed, and the best remaining gap. Return to research if that gap could change the central story. Choose deepen, broaden, pivot or conclude. This adapts the requested autoresearch process; it is not an ML experiment or a systematic review.

Stop research when all material external claims have inspected support and locators, counterevidence has been sought, the conclusion fits the evidence, and two targeted passes add no material change. If access or evidence remains inadequate, narrow the article or keep it a draft. Citation counts and a polished draft cannot overrule an unresolved central claim.

## Think, draft, review

Use `docs/frameworks.md` and the corresponding skill. Keep evidence IDs in the packet and ordinary readable source links in the article. Retain raw/derived data and rights metadata when visuals are used. A conceptual diagram must be labeled as the author's explanatory model.

Review the headline, every important external fact, causal language, all numbers and quotations, recommendations, first-person assertions, source relevance, rights, privacy, and uncertainty. Record issues in `review.json`. The source/claim registers are JSON so the structural gate can inspect them; `review.md` holds the actual editorial reasoning.

## Approve and publish

The author approves the final article. After changes, compute `python scripts/blog.py hash <slug>` and record that digest in the review. The hash normalizes line endings and the `draft` flag only. Any substantive article or evidence-packet change invalidates the digest. Record approval honestly; agents do not set it on the author's behalf.

Set `draft = false` only after approval. Run the checks and production preview, then use GitHub Pages publication within the user's authorized scope. The gate checks records, dates and integrity; it cannot evaluate truth, consent, source relevance or voice. A public repository exposes tracked drafts even when Hugo excludes them from the website.

## Correct and maintain

If a published claim is wrong, correct it, explain material changes in the article, update the ledger and review, and append to `corrections.csv`. Re-review changed content and refresh time-sensitive sources before the recorded review-by date. Recheck external source availability near publication; the offline gate does not test remote URLs.
