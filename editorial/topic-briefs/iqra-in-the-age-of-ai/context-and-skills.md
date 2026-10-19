# Current context, skills and the duty to read

Added 18 October 2026 from the owner's follow-up, using blog-topics and blog-research. This is a proposed section for a future reflection, not a standalone article or a report of an experiment. The organizational recommendation and Iqra connection are the author's developing argument.

## Proposed passage

In a company built around AI, current context matters whether the next action comes from a person or an agent. What are we trying to achieve now? Which requirement changed? Which decision still stands? A fluent answer is useful only if it addresses the work actually in front of us.

An agent's active context is a working selection of instructions and task material. A platform may also keep documents and memory elsewhere, retrieving them when needed. We should distinguish information being stored from evidence being available for a particular response. [Context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) describes this boundary.

AI skills offer one technique: package procedures, references and tools into reusable resources, then load relevant details as needed. They can tell an agent how to approach a task; the current brief still supplies what matters for this task. That separation is my proposed working discipline. [Skills design](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) supports loading expertise on demand.

A long interaction can accumulate irrelevant material. Compaction helps manage it, but an overly aggressive summary can discard an important detail. [The engineering guidance](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) discusses both the benefit and the risk. What feels like “laziness” needs closer inspection: did the agent skip a check, reuse an outdated assumption, or miss a constraint?

This brings me back to Iqra as a personal reflection: keep returning to the evidence that gives the work its meaning. Before acting, check the relevant source and its current version, reconcile it with the latest instructions, and explain how it supports the decision. Skills can organize that practice; they cannot replace the practice of reading.

## Technical boundaries

- **Context is not all knowledge.** Files, retrieved memory and model training are different from the material supplied for one response. Do not claim that most platforms store all organizational knowledge in a context window; adoption prevalence was not researched here.
- **Skills have a defined scope.** The [open format](https://agentskills.io/specification) separates discovery metadata, task instructions and supporting resources. Loading a skill is not model retraining or proof of compliance. Keeping changing facts at a current source is an editorial recommendation.
- **Availability is not reliable use.** [Liu et al.](https://aclanthology.org/2024.tacl-1.9/) found position-sensitive performance in document QA and key-value retrieval. Their tested model generations and tasks do not establish how a particular present-day platform behaves.
- **Length is not a diagnosis.** [Laban et al.'s author summary](https://www.microsoft.com/en-us/research/publication/llms-get-lost-in-multi-turn-conversation/) also describes early assumptions and poor recovery in simulated conversations. Only the publication summary was inspected here; it is not evidence that compaction caused those results. Missing retrieval, outdated documents and tool failures are further possibilities to investigate, not findings from a run in this project.
- **“Always read” means a dependable source check.** Retrieve the decision-relevant passages when requirements change, evidence is missing after compaction, or a consequential action needs confirmation. A verified unchanged copy can suffice. Repeatedly loading every file would work against relevance; reopening a file still does not guarantee a correct interpretation.

## A possible practice to test later

1. Identify the current objective and latest user decisions.
2. Select the relevant skill and supporting references.
3. Consult the authoritative task document and record its version or date.
4. Extract the constraint and passage that determine the action; resolve conflicting instructions or flag the gap.
5. Before the action, check that the proposed output follows that evidence. After compaction, recover any missing decisive detail from the source.

This is a proposed practice, not a validated method. A future field note could use a non-sensitive document with a revision and compare whether an agent identifies the current requirement before and after a long interaction. No such test has been run, and a single run would not establish a general effect.

## Research decision

The initial technical pass established the retrieval and skills distinction. A second pass checked the open format and a controlled long-context study. A final check of the multi-turn author summary reinforced the need to distinguish failure mechanisms. No later check changed the recommended scope: explain the techniques, retain uncertainty about a particular failure, and propose source verification. This is sufficient for the added idea; it does not meet the evidence needed to assert a market-wide tendency to become lazy.

Sources S7–S11 and technical claims TC01–TC09 are recorded alongside this note. Existing sources S1–S6 remain intact; their original inspection limits still apply. The ledger covers this extension, not every possible claim in a future article.
