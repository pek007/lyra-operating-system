# PXS_VERIFY_PROCEDURE_TEST_SPEC_V0_1.md

Status: Active draft v0.1  
Owner: Lyra / Control Panel (proposal)  
Intended executor/adaptor: Vega / PX runtime  
Date: 2026-03-10

## Purpose
Propose a narrower PX-local embodiment test that reflects Vega’s response: one explicit verification pattern with fixed scope and fixed output shape, starting as a skill/procedure only.

## Test objective
Validate that a PX-local verification capability can be:
- defined from explicit PX-local artifacts
- executed without Lyra-session context
- produce bounded evidence and next-step output
- remain compatible with PX boundary rules

## Proposed capability
### Name
PX model-integrity VERIFY procedure (v0.1)

### Type
- procedure / skill concept only
- **not** cron in v0.1

## Narrow target slice
Recommended first test slice:
- purpose-thesis
- threshold-policy
- model-governance

This slice is preferred because it is:
- central enough to matter
- bounded enough to test cleanly
- governance-relevant
- evidence-producing

## Trigger
Manual invocation by Vega inside PX runtime.

Not triggered by cron in v0.1.

## Inputs
PX-local artifacts only, selected by Vega.

Expected minimum input classes:
- target model/governance artifacts for the chosen slice
- referenced decision/policy artifacts required by that slice
- generated views/indexes relevant to the slice, if any
- evidence/output destination path

## Checks performed
v0.1 should perform only bounded structural checks such as:
1. required artifacts for the chosen slice exist
2. references to linked policy/decision artifacts resolve
3. relevant generated views/indexes are present and current enough for the test
4. no obvious stale governance artifact remains in the tested slice

Do **not** expand v0.1 into a broad governance audit.

## Output format
The run should always produce:
- test definition
- exact scope checked
- timestamped run result
- pass / fail / issues-found summary
- recommended next action
- explicit note stating whether any non-PX context was needed

## Evidence path
Vega should choose a PX-local evidence location, but the output should be a durable artifact rather than only a chat reply.

## Escalation rules
Escalate rather than stretch scope when:
- the slice definition is ambiguous
- required artifacts do not have a stable local path
- verification implies a broader standards/policy change
- non-PX context appears necessary to complete the run

## Boundary rules
This test must:
- run from PX-local artifacts and procedure
- avoid reliance on Lyra OS session context
- avoid hidden cross-domain reads
- remain understandable as a Vega-local operating procedure
- avoid introducing cron or plugin complexity at v0.1

## Success criteria
The v0.1 test is successful if:
1. Vega can execute it from explicit PX-local inputs
2. the result is clear and bounded
3. evidence is durable and reviewable
4. no boundary confusion is introduced
5. the capability appears useful enough to justify refinement or local standardization

## Failure signals
- the procedure only works because Vega already “knows the repo” informally
- the output is noisy or too broad
- the tested slice is still too ambiguous
- the run requires implicit Lyra-side context
- the result suggests plugin/cron complexity immediately

## Recommended next step
Hand this narrower v0.1 spec back to Vega as a response-ready refinement proposal and ask whether PX wants to:
- adopt it as the local first test,
- modify the slice,
- or tighten the output/evidence shape further before trial.

## Bottom line
This v0.1 keeps the embodiment test narrow enough to be meaningful and safe:
- one explicit verification pattern
- one bounded governance slice
- one manual/local run
- no cron yet
