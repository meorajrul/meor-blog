# Malaysia functional-integration sensitivity model

Prepared 19 October 2026. These are illustrative planning cases, not observed savings, forecasts or probability ranges. They do not estimate the causal effect of AI or any specific legal closure. Figures are nominal RM million, without inflation or discounting.

## Budget anchors

Source D01 is the proposed 2027 KUSKOP federal expenditure estimate, B.26: https://belanjawan.mof.gov.my/pdf/belanjawan2027/perbelanjaan/BP.26.pdf

| Anchor | Proposed 2027 RM million |
|---|---:|
| SME Corp operating grant | 42.7564 |
| INSKEN operating grant | 12.0009 |
| Ministry P1 management supplies and services | 29.8360 |

The RM84.5933m combined anchor is not a verified pool of overhead, cash expenditure or duplicate spending. Agency grants may contain pass-through programme funding. The P1 aggregate is used once; its own subcomponents are not added again. Development financing, guarantee volumes and entity-wide mandates are not added to these operating anchors.

## Assumptions and formula

For each anchor, assumed addressable share multiplied by assumed retirement share determines the cost retired. Each share is an analyst assumption. Retirement requires actual removal or avoidance of cost; a staff or contract transfer alone is insufficient. Full input rows are in savings-assumptions.csv.

| Scenario | SME Corp shares | INSKEN shares | Ministry shares | New annual recurring cost | One-time transition |
|---|---|---|---|---:|---:|
| Low | 10% × 15% | 20% × 20% | 10% × 10% | 2.00 | 6.00 |
| Central | 15% × 20% | 27.5% × 25% | 15% × 15% | 1.50 | 4.50 |
| High | 20% × 25% | 35% × 30% | 20% × 20% | 1.00 | 3.00 |

Mature gross annual retirement = sum(anchor × addressable share × retirement share).

Annual net saving = mature gross retirement × rollout share − new recurring cost − transition cost in that year.

Rollout shares are 25%, 75% and 100% in years 1, 2 and 3. Full recurring cost starts in year 1; the transition cost is charged entirely in year 1. The cumulative chart starts at zero before rollout and sums annual net flows. It shows three scenario paths, not statistical confidence bands.

| Scenario | Mature gross | Mature annual net | Year 1 net | Year 2 net | Year 3 net | Three-year cumulative |
|---|---:|---:|---:|---:|---:|---:|
| Low | 1.419742 | -0.580258 | -7.645065 | -0.935194 | -0.580258 | -9.160516 |
| Central | 2.779064 | 1.279064 | -5.305234 | 0.584298 | 1.279064 | -3.441872 |
| High | 4.591355 | 3.591355 | -2.852161 | 2.443516 | 3.591355 | 3.182709 |

The central case would permit only RM1.058128m in transition spending for three-year break-even under the other assumptions: two mature years' equivalent gross benefits minus three years of recurring costs. This is a mathematical ceiling, not a priced implementation offer.

## Evidence limits

No verified baseline administrative ledger, workforce transfer plan, retired contract schedule or system quotation establishes these assumptions. Existing BPMB-group bank integration is not counted as a new federal saving. The separate SME Bank expense-pool sensitivity in the earlier research is excluded from this chart. Company cost savings, agency funding and public net savings remain separate categories.

Programme performance and the institutional quadrant use a different evidence base: reported 2024 IAFSP scores in SMEIPA 2025. The threshold is 70 points. These are neither percentages nor whole-organisation KPI attainment. Institutional categories are analyst judgments. Missing SKM and TERAJU scores remain unplaced.

Reproducibility: src/build_charts.py recalculates all nine annual net flows from the preserved assumptions and reconciles the results to savings-model.json before exporting the figures. The article provides annual/cumulative CSV data, assumptions and vector charts. No inference about measured overseas fiscal savings is used to calibrate this model.
