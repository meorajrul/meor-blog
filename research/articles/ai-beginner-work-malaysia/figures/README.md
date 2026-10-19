# Figure provenance and reuse

Both charts are original visualizations of published numerical summaries. No publisher figure artwork is reproduced, no microdata were used, and no new statistical effect was estimated.

## Malaysian age exposure
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
