# Skill-versus-prompt evaluation

## Status and purpose

Benchmark status: **NOT RUN**.

Test whether this skill improves article usefulness and auditability under equivalent conditions. Structural validation is not behavioral proof. Do not claim superiority without recorded results.

## Arms

A: Normal prompt:
> Write a useful, engaging, evidence-backed blog about {topic} for {audience}, within {length}. Use the provided materials and available research tools. Include relevant charts, tables, diagrams, references, and supporting resources. Deliver the article and supporting files.

B: Exactly the same prompt with evidence-backed-blog activated.

Use fresh isolated sessions with the same model/version, settings, tools, materials, length target, tool-call cap, and output budget. The skill instructions are the intervention. Give neither arm the other output, answer key, rubric feedback, or prior conclusions. Keep the evaluator-only answer key outside writer-accessible inputs.

Record actual resource use, truncated output, exhausted budgets, and incomplete runs. Installing the skill does not authorize paid API use or external publication.

## Modes

**Controlled evidence:** identical frozen source packets, browsing disabled. Tests interpretation, capture, calculations, writing, and visuals.

**Live research:** identical brief and capabilities, browsing enabled. Archive consulted sources for audit. Tests discovery and end-to-end workflow.

Report modes separately. In both modes retain prompts, tool logs where available, outputs, packet versions, and provenance of adjudication.

## Six development cases

Prepare real files and evaluator-only answer keys before running. Fictional fixtures must be labeled synthetic.

1. **Numerical change:** fictional incidents decline from 40 to 30. Correct relative decline is 25%, not 10%. Include dated data and a corrected newer version; key identifies which version applies.
2. **Conflicting findings:** studies differ in populations and outcomes. Explain the conflict and applicability rather than selecting convenient findings.
3. **Causal overreach:** observational association. Do not infer causation without sufficient supporting evidence.
4. **Sparse evidence:** credible qualitative sources, no quantitative dataset. Choose a useful table or conceptual diagram; do not invent quantitative evidence.
5. **Asset provenance:** image with explicit attribution conditions, image with unknown rights, and inaccessible document. Distinguish reuse, inspection, and local capture status.
6. **Mixed resources:** PDF, spreadsheet, image, transcript, and multiple reports of one study. Preserve locators and accessible resources; identify one underlying evidence origin.

These are case specifications, not completed source packets. Build and freeze the actual materials and answer keys before execution.

Reserve additional unseen cases for final validation. Freeze skill version, rubric, and criteria before opening holdout cases; do not tune against them.

## Runs

Suggested pilot per mode: 6 cases x 3 repetitions x 2 arms = 36 outputs.

Pair by case and repetition. Retain failures; do not silently rerun unfavorable results. Benchmark repetitions are not independent topics.

## Rubric: 100 points

| Dimension | Weight |
|---|---:|
| Factual accuracy and citation support | 30 |
| Source relevance, appraisal, and balanced synthesis | 15 |
| Resource capture and claim-source traceability | 15 |
| Numerical and visual correctness | 15 |
| Reader usefulness, clarity, and narrative | 20 |
| Scope, freshness, and limitations | 5 |

Score 0–4 per dimension and calculate weight x score / 4.

0: absent or materially misleading.
1: major defects requiring substantial repair.
2: partially successful with meaningful omissions.
3: sound with minor repairs.
4: accurate, complete for the brief, usable, and checkable.

Give output-specific evidence for each score. Do not reward citation count, file count, length, or resemblance to the skill itself. Source quality means fitness for the claim, not prestige alone.

## Objective checks

- Supported material claims / all material claims.
- Correct citation-claim links / all checked citation-claim links.
- Correct numerical statements / all numerical statements.
- Truthful resource statuses / all recorded resource statuses.
- Reproducible quantitative visuals / all quantitative visuals.
- Valid internal references / all internal references.

Enumerate claims independently from the article, including headline and captions. Do not let the author's ledger define the denominator. Mark zero denominators not applicable, not perfect.

## Critical failures

Fabricated sources, quotations, or evidence; materially false calculations; deceptive visuals; or false assertions of inspection or capture make the output ineligible for a release pass.

Honest disclosure of an unavailable resource is an incompleteness issue, not fabrication.

## Blind review

Anonymize arm labels and randomize presentation. Judge each pair in both orders without revealing which used the skill. Preserve supporting files for review.

If order changes the result, mark it unstable and seek human adjudication. Humans verify decisive facts, provenance, and critical-failure flags. Cite exact passages, files, and source locators in review findings.

## Proposed acceptance criteria

On unseen validation cases:
- Mean paired score improvement at least 10/100.
- Skill preference in at least 70% of pairs; ties count as half.
- No critical failures in skill outputs.
- No average regression in reader usefulness.
- At least 95% support coverage for material factual claims.
- All quantitative visuals reproduce from preserved inputs.

These are proposed product thresholds, not externally validated standards. Report uncertainty intervals clustered by case and treat small samples as pilot evidence, not broad proof.

Report results by case, runtime, tool use, cost where known, size, completion rates, and reviewer disagreements alongside aggregate scores.

## Results schema

case_id, repetition, mode, model_version, skill_version, source_packet_version, run_ids, scores_by_dimension, objective_metrics, critical_failures, preference, reviewer_evidence, runtime, tool_calls, cost_if_available, completion_status

Final verdict: passed on tested cases | needs revision | inconclusive | not run.
