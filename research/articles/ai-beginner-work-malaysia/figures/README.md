# Figure provenance and reuse

The original charts are visualizations of published numerical summaries. No publisher figure artwork is reproduced, no microdata were used, and no new statistical effect was estimated.

## Superseded Malaysian age-exposure chart (removed from current page)
Input: malaysia-ai-exposure-by-age.csv.
Source: Cheng, Calvin, Hanson Chong, Matthew Dornan and Alyssa Farha Jasmin (2025), Novel AI Technologies and the Future of Work in Malaysia, World Bank / ISIS Malaysia.
URL: https://documents1.worldbank.org/curated/en/099092325013010451/pdf/P181093-2e5b89c5-f3be-43b3-868c-8890b74bef21.pdf
Locator: PDF page17 (one-based), Figures6–7. Section3.2 says occupational exposure is mapped onto 2021 LFS employment.
Transcription: highest quartile 26,32,29,24,17; lowest quartile44,37,31,33,36; age groups15–24 to55–64. Rounded published percentages, no transformation. Each percentage uses employment within its age band; middle quartiles omitted. No job-loss interpretation.
Verification: PDF page visually rendered and inspected19 October2026.
Reuse statement: report PDF page2 Rights and Permissions permits non-commercial reproduction with full attribution. This is a new plot of factual values with attribution; no assertion of ownership of the underlying report.

## Learning curve
Input: ai-learning-curve.csv.
Source: Brynjolfsson, Erik, Danielle Li and Lindsey Raymond (2025), Generative AI at Work, Quarterly Journal of Economics140(2),889–942. doi:10.1093/qje/qjae044.
URL: https://doi.org/10.1093/qje/qjae044
Locator: section V.B.3, Moving Down the Experience Curve, FigureV narrative.
Transcription: authors describe about2.5 resolved issues/hour after2months for always-treated agents and after8–10months for never-treated agents. We show only these approximate narrative summaries, not digitized curves, reconstructed observations or exact time-to-target estimates. The8–10range is descriptive, not a confidence interval.
Population: customer-support agents for one US software firm/subcontractors, mostly Philippines-based; staggered rollout, not a Malaysian graduate-hiring study.
Reuse statement: article footer specifies CC BY-NC4.0. Original numerical summary plot with attribution; publisher illustration not reproduced.

## Exports and reproduction
Run gen_fig_experience.py using Python3.12 and matplotlib3.11.2, or a compatible local environment. The script can use the project's ignored .tools/research-figure/python-packages.
Outputs: web PNGs in the Hugo page bundle, vector PDFs here; CSVs also copied into the bundle for accessible download.
Palette: Okabe–Ito blue/orange, pattern distinction and direct value labels. Data ranges start at zero; no invented uncertainty. Captions and alt text identify geography, period and measurement limits.


## China programme decisions — added 22 October 2026
Input: china-programme-changes.csv. Source: China Ministry of Education, 22 April 2025, 2024 undergraduate filing/approval round. Official inspected mirror: https://hudong.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202504/t20250422_1188245.html .
Values: 1839 added, 2220 stopped admissions, 1428 withdrawn, 157 degree-category/duration changes. Unit is an institution-level undergraduate programme offering. No net-change calculation, student count, labour-gap effect or forecast. Original plot of factual counts; no official artwork, logos or prose copied. Attribution is on the chart and in article text.

## Malaysia vacancies — added 22 October 2026
Input: malaysia-vacancies-q2-2026.csv. Source: DOSM, Employment Statistics Q2 2026, released 13 August 2026. Official full overview: https://www.dosm.gov.my/portal-main/release-content/employment-statistics-Q22026 .
Values in thousands: semi-skilled107.3, skilled50.2, low-skilled38.2; published rounded total195.7. Quarterly Employment Survey of covered registered private-sector businesses. No forecast, no inferred TVET/first-job count, and no invented sampling-error interval. Original visualization of factual estimates, not DOSM chart artwork; source attribution included. Manufacturing114.0k is a sector cut of the same total and is not added to the chart.

Reproduce new plots with gen_fig_planning.py using Python3.12 and matplotlib3.11.2; planning-plot-environment.json records the actual runtime. Web PNGs and CSVs are in the bundle; vector PDFs remain here. Both quantitative axes start at zero. New cover is the China data chart; the conceptual staircase hero and prompt were removed from the current version. The age-exposure data/PDF remain only as superseded provenance.

Reference-period recheck22October2026: QJE IV.A says rollout mainly autumn2020 and winter2021. Chart and downloadable inputs now identify this; 2025 is the publication year, not the deployment period. ILO initial scoring uses models available at end2024; May2025 is its publication date, not October2026 capability testing.


## 23 October 2026: graduate outcomes replace China cover
Two new charts transcribe MOHE Higher Education Statistics2025, Chapter7, Tables7.1/7.2 (printed210) and7.7 (printed215). gen_fig_graduates.py stores counts, calculates rounded percentages matching publication, and exports CSV/PNG/PDF. Employment denominator5706 is the employed+unemployed group; position denominator4694 is government+private employees (Table7.6:442+4252). No response rate/CI provided in this chapter; no causal policy/AI effect or long-term outcome asserted. Original factual-data charts, no copied ministry artwork. The source is bilingual with English table labels.
China administrative chart removed from active article/assets on owner English-source instruction. Its old CSV/PDF and gen_fig_planning.py remain historical research artefacts, not support for current claims. Only the Malaysia vacancy output from that historical generator remains active.


## First-job revision — 23 October 2026

US cover chart: S22 printed p3 directly reports approximately -11%/+10% from November2022 to June2026. No interpolation, counterfactual path or forecast. Exposure groupings and age are explicit. Singapore chart: S25 answer paragraph2; shares19/14/8/6 among adopting firms, reported5August2026. The answer does not give fieldwork dates; labels disclose that gap, rather than equating reporting date with collection. Categories are not added. Neither chart supplies invented confidence intervals.

Original matplotlib charts, Okabe-Ito colours, numerical labels and zero baselines, PNG300dpi and vectorPDF. Factual values transcribed with attribution; no publisher artwork reproduced. Code, CSV inputs and software environment retained. Images visually inspected for clipping, labels, scale and source/caveat legibility. Existing graduate employment graphic remains supplementary; first-job chart is now the cover.
