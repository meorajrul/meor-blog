# GPS navigation research figure

Prepared 18 October 2026 using academic-plotting's data-figure workflow. This is a chart of published aggregate results, not an AI-generated illustration or an original experiment.

Source: Laura Miola, Veronica Muffato, Enrico Sella, Chiara Meneghetti and Francesca Pazzaglia (2024), GPS use and navigation ability: A systematic review and meta-analysis, Journal of Environmental Psychology 99, 102417. https://doi.org/10.1016/j.jenvp.2024.102417

Inspected primary PDF: https://www.research.unipd.it/retrieve/c0077d6f-e636-4b6c-946a-dd77579c0949/GPS_use_navigation_ability_systematic%20review_meta-analysis.pdf

## Data and transformations

- Transcribed the three rounded pooled r estimates and confidence limits from section 3.3, printed p. 8, cross-checked against the abstract on p. 1. All three outcome families are shown; the inconclusive result is retained.
- The source combines experimental and cross-sectional research. Its authors convert group differences to the correlation scale and apply random-effects multilevel synthesis. We do not redo that synthesis.
- Plot each reported estimate as a dot and its reported 95% CI as horizontal whiskers. Error distances are estimate minus lower limit and upper limit minus estimate. No raw participant observations, fitted scatter points, percentage conversion, before/after scores or recalculated intervals are invented.
- Display outcomes in a reading-friendly order. Blue marks indicate intervals excluding zero; the gray interval crosses zero and is labeled inconclusive. Labels use plain-language descriptions alongside the source outcome names. The zero line is visible.
- The review contains 23 studies; 18 contribute quantitative data overall. Outcome-specific samples differ. The source reports significant heterogeneity and substantial risk-of-bias concerns. It does not estimate general reasoning decline or separate Google Maps/Waze effects.

Files: gps-navigation-effects.csv is the preserved numeric input; gen_fig_gps_navigation.py creates the web PNG and vector PDF. plot-environment.json records the actual runtime and plotting version. The same CSV is copied into the article bundle for readers to download. Verify the two copies match when changing data.

## Rights and attribution

The paper is labeled CC BY-NC-ND 4.0 on its first page: https://creativecommons.org/licenses/by-nc-nd/4.0/. No publisher image, figure layout or artwork was reused or modified. This project-created chart displays the attributed numerical estimates in a new layout; it does not claim that the paper's license licenses a derivative figure. The article caption and chart identify the original research.

## Evidence selection and limits

Dahmani and Bohbot (2020) was inspected as a longitudinal example, including its small unplanned follow-up and caution about spurious correlations. It is included in Miola et al.'s review, not an independent replication of the meta-analysis. Javadi et al.'s 2017 title was located, but the publisher page could not be retrieved and no brain-activation figure or inference was adopted. A 2025 landmark-instruction result was located only at search/abstract level and not used for a substantive claim. The review supplied a broader comparison and direct counterevidence through the inconclusive wayfinding result.
