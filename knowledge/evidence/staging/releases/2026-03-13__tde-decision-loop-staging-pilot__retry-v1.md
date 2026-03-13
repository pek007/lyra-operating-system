# TDE Decision Loop Staging Pilot — Retry Path v1

Date: 2026-03-13
Status: Pilot executed successfully in isolated staging-style fixture
Owner: Peter + Lyra
Scope: Staging validation of bounded `research_further -> research activation -> re-entry -> retry`

## Purpose
Validate the newly added `retry` re-entry outcome in a deterministic isolated fixture after the shared staging retry attempt was contaminated by prior state.

## Fixture model
This pilot used an isolated temporary DB fixture with only three tasks:
- `TDE-STAGE-RETRY-ORIGIN-ISO-001`
- `TDE-STAGE-RETRY-RESEARCH-ISO-001`
- `TDE-STAGE-RETRY-TASK-ISO-001`

## Intended flow
1. Origin task selects `research_further`
2. Research task activates
3. Research task executes
4. Origin decision re-enters with outcome `retry`
5. Retry task activates

## Artifacts
- `knowledge/evidence/staging/2026-03/tde-stage-retry-pilot-iso-tick-1.json`
- `knowledge/evidence/staging/2026-03/tde-stage-retry-pilot-iso-tick-2.json`
- `knowledge/evidence/staging/2026-03/tde-decision-advancement-tde-stage-retry-origin-iso-001-20260313-165359.json`
- `knowledge/evidence/staging/2026-03/tde-decision-advancement-tde-stage-retry-research-iso-001-20260313-165359.json`
- `knowledge/evidence/staging/2026-03/tde-stage-retry-research-note.md`

## Result summary
### Tick 1
- claimed: `TDE-STAGE-RETRY-ORIGIN-ISO-001`
- selected outcome: `research_further`
- research successor activated
- origin task parked / non-claimable during active research

### Tick 2
- claimed: `TDE-STAGE-RETRY-RESEARCH-ISO-001`
- research task executed
- origin decision re-entered with outcome `retry`
- retry task `TDE-STAGE-RETRY-TASK-ISO-001` activated successfully

## Evidence-aware re-entry proof
The re-entry decision carried forward:
- confidence score: `0.76`
- evidence ref: `knowledge/evidence/staging/2026-03/tde-stage-retry-research-note.md`
- rationale: `Research indicates a bounded retry is the best next move.`

## Final state snapshot
- origin task: `Active`, unparked, research round recorded
- research task: `Waiting` after execution under current writeback semantics
- retry task: `Active`

## Conclusion
The bounded retry path now works end-to-end in an isolated staging-style environment:
- `research_further`
- research activation
- research completion
- evidence-aware re-entry
- retry-task activation

## Interpretation
This confirms that the expanded re-entry outcome model is working not only for `continue`, but also for `retry`.

It also reinforces the environment lesson from the failed shared staging attempt:
for precise pilot validation, isolated fixtures are the cleaner proving method.
