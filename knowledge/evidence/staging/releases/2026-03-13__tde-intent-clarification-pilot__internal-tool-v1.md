# TDE Intent Clarification Pilot — Internal Tool v1

Date: 2026-03-13
Status: Pilot executed successfully in staging
Owner: Peter + Lyra
Scope: First end-to-end pilot of the clarification branch in the thin TDE intent-intake layer

## Purpose
Prove that TDE can respond to an underspecified request by:
- creating a formation artifact,
- selecting `ask_clarifying_questions`,
- surfacing explicit clarification questions,
- and refusing canonical work creation until the request is sufficiently specified.

## Raw request used
- `Build an internal tool`

## Command executed
- `python3 tools/tde_intent_intake.py --request-text "Build an internal tool" --source-ref "telegram:lyra-operations:internal-tool-vague-request" --formation-out knowledge/evidence/staging/2026-03/tde-intent-formation-internal-tool-vague.json`

## Formation result
Formation artifact:
- `knowledge/evidence/staging/2026-03/tde-intent-formation-internal-tool-vague.json`

Key output values:
- request class: `internal_tool`
- actionability status: `needs_clarification`
- recommended next action: `ask_clarifying_questions`

Clarifications produced:
1. Who is the primary user of the internal tool?
2. What is the main workflow or job the tool should support?
3. What should the first version definitely include or exclude?

## Canonical creation check
A follow-on creation attempt was intentionally made against the resulting formation artifact.

Observed result:
- canonical creation failed as expected with:
  - `formation_not_execution_ready`

## Interpretation
This pilot proves the first thin clarification branch is working correctly.

TDE can now, for at least one request class:
- recognize that the input is too underspecified,
- avoid pretending it can safely form execution-ready work,
- surface a small, high-value clarification set,
- and block canonical creation until clarity improves.

## Why this matters
This is important because it validates the design principle that TDE should:
- not read minds,
- not ask everything,
- but ask when the missing information materially affects professional output quality.

## Bottom line
The thin intake layer now has validated evidence for both major first-branch behaviors:
- proceed with assumptions
- ask clarifying questions

That means the intake layer is beginning to act like a real shaping layer rather than a one-way generator.
