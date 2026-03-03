# Deep Research Prompting Guideline
Version: 1.0.0
Last updated: 2026-03-03

## Core principle
Use a **hybrid directive**:
1. **Expert-depth directive** (technical rigor, nuance, edge cases)
2. **Decision-structure directive** (clear sections, options, recommendation)

Do not choose one at the expense of the other.

## Why
- Depth-only prompts often produce long but less actionable output.
- Concision-only prompts can become shallow.
- Hybrid prompts improve both analysis quality and usability.

## Required blocks
1. Objective/question and decision to support
2. Audience level (default: expert)
3. Scope boundaries (in/out)
4. Source policy (allowed domains, evidence strength expectations)
5. Output contract (exact sections to return)
6. Style contract (expert-depth + structured concision)
7. Constraints/safety

## Canonical style contract (reuse)
"Assume the audience is domain experts. Prioritize technical depth, edge cases, and trade-offs over basic explanation. Keep the report tightly structured and decision-oriented: explicit assumptions, evidence-backed findings, ranked options, and clear recommendations. Use concise language inside each section and avoid filler."

## Validation checklist
- Is the audience level explicitly set?
- Is depth requested (trade-offs, edge cases, uncertainty)?
- Is output structure explicit and decision-ready?
- Are evidence/citation requirements explicit?
- Are constraints/safety boundaries explicit?
