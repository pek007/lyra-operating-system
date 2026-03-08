# Deep Research Prompting Guideline
Version: 1.1.0
Last updated: 2026-03-08

## Core principle
Use a **hybrid directive**:
1. **Expert-depth directive** (technical rigor, nuance, edge cases)
2. **Decision-structure directive** (clear sections, options, recommendation)

Do not choose one at the expense of the other.

## GPT-5.4 update
For GPT-5.4, the main gains come from being more explicit about:
- output contract
- evidence vs inference separation
- completion criteria
- dependency checks before recommendation
- stopping rules for research expansion

In short: less implicit craft, more explicit operating contract.

## Why
- Depth-only prompts often produce long but less actionable output.
- Concision-only prompts can become shallow.
- Hybrid prompts improve both analysis quality and usability.
- GPT-5.4 responds especially well when “done” and “how to decide” are explicit.

## Required blocks
1. Objective/question and decision to support
2. Audience level (default: expert)
3. Scope boundaries (in/out)
4. Source policy (allowed domains, evidence strength expectations)
5. Output contract (exact sections to return)
6. Style contract (expert-depth + structured concision)
7. Research discipline / stopping rule
8. Completeness contract
9. Constraints/safety

## Canonical style contract (reuse)
"Assume the audience is domain experts. Prioritize technical depth, edge cases, and trade-offs over basic explanation. Keep the report tightly structured and decision-oriented: explicit assumptions, evidence-backed findings, ranked options, and clear recommendations. Use concise language inside each section and avoid filler."

## Recommended GPT-5.4 research additions
### Output contract
- Return exactly the requested sections, in order.
- Separate evidence, interpretation, and recommendation.
- Keep prose compact, but do not omit caveats.

### Research discipline
- Gather enough evidence to support the decision; do not over-search by default.
- If evidence materially conflicts, run one additional focused retrieval pass.
- Distinguish confirmed facts, inference, and uncertainty.

### Completeness contract
- Treat the report as incomplete until all requested sections are covered.
- Cite non-trivial claims or mark them as uncertainty.
- Mark unanswered questions as `[unresolved]`.

## Validation checklist
- Is the audience level explicitly set?
- Is depth requested (trade-offs, edge cases, uncertainty)?
- Is output structure explicit and decision-ready?
- Are evidence/citation requirements explicit?
- Is a stopping rule included?
- Is completeness defined?
- Are constraints/safety boundaries explicit?
