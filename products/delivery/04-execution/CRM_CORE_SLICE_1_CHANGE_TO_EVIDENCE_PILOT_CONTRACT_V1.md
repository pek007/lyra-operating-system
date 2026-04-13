# CRM Core Slice 1 Change-to-Evidence Pilot Contract v1

Status: Draft active
Owner: Lyra
Date: 2026-04-13
Related pilot note: `2026-04-13_DELIVERY_TDE_PXS_TOOLS_CRM_INTEGRATION_PILOT_NOTE.md`
Related CRM slice artifacts:
- `CRM_CORE_SLICE_1_DELIVERY_BRIEF_2026-04-03.md`
- `CRM_CORE_SLICE_1_TEST_AND_EVIDENCE_SPEC_2026-04-03.md`
- `CRM_RESTART_THIN_SLICE_DECISION_NOTE_2026-04-03.md`

## Purpose
Define the minimum bounded contract for the first Delivery / TDE / PXS Tools integration pilot using CRM Core Slice 1 as the proving case.

This contract governs the **change-to-evidence execution-support loop** around CRM Core Slice 1. It does not make TDE the primary implementation plane for CRM feature work.

## Pilot intent
This pilot should prove that a real PXS Tools development slice can move through a Delivery-governed, TDE-supported support loop with:
1. explicit trigger,
2. explicit machine-work state,
3. at least one real Delivery gate,
4. explicit evidence assembly,
5. explicit completion or abort judgment.

## Trigger for pilot start
The pilot starts only when all of the following are true:
1. CRM Core Slice 1 remains the accepted bounded slice
2. slice scope and out-of-scope conditions are explicit
3. minimum architecture note is available
4. minimum test/evidence expectations are explicit
5. implementation lane for the slice is identified

If those conditions are not met, the pilot remains in `not-ready` state.

## Smallest viable pilot shape
The smallest viable pilot shape is:
- one accepted CRM slice
- one explicit implementation kickoff packet
- one explicit verification/test capture step
- one explicit evidence assembly step
- one explicit status/review output
- one explicit completion or abort judgment

## TDE-owned pilot states
For this pilot, TDE owns the machine-execution support state for the following bounded steps:
1. `not-ready` — preconditions not yet met
2. `ready-for-kickoff-packet` — preconditions met, kickoff packet can be formed
3. `kickoff-packet-prepared` — implementation packet prepared and reviewable
4. `implementation-in-progress` — implementation underway outside TDE primary ownership
5. `verification-pending` — implementation step finished and verification expected
6. `verification-captured` — verification/test result recorded
7. `evidence-pack-pending` — evidence pack still incomplete
8. `evidence-pack-ready` — evidence bundle assembled and reviewable
9. `review-pending` — completion or abort judgment required
10. `completed` — pilot cycle accepted as complete
11. `aborted` — pilot stopped due to failed gate, weak evidence, or boundary violation
12. `follow-up-required` — pilot completed or stopped, but explicit next actions remain

## Delivery gate for this pilot
At minimum, Delivery must provide one enforceable gate before the pilot can move from `verification-pending` to `verification-captured`.

### Minimum gate requirement
The gate must:
- produce explicit pass/fail output
- fail closed on missing or malformed verification input
- generate reviewable evidence rather than only conversational reassurance

### Minimum acceptable first gate
For v1, the most practical first gate is:
- verification evidence completeness gate

This gate checks that the CRM slice run includes at least:
- implementation summary
- test summary with pass/fail status
- explicit out-of-scope statement
- explicit limitations or unresolved issues

If any required evidence component is missing, the pilot must not advance as if verification succeeded.

## Evidence packet contents
The pilot evidence packet must contain:
1. implementation summary
2. test/verification summary
3. pass/fail or mixed-result judgment
4. explicit out-of-scope confirmation
5. unresolved issues / limitations
6. recommended next action

## Completion criteria
The pilot may move to `completed` only if:
- one real CRM Core Slice 1 cycle passed through the bounded support loop
- the Delivery gate produced explicit output
- TDE state progression is explicit and reviewable
- evidence packet is complete
- no material boundary violation occurred (for example, TDE silently taking over feature-implementation judgment)

## Abort criteria
The pilot should move to `aborted` if any of the following occur:
- CRM slice preconditions are not explicit enough to support the loop
- the implementation lane is unclear
- the Delivery gate cannot produce a real pass/fail result
- evidence cannot be assembled to minimum completeness
- the pilot collapses back into chat-memory-only coordination
- the loop requires TDE to take ownership of implementation decisions outside the agreed boundary

## Follow-up rule
If the pilot reaches either `completed` or `aborted`, a short follow-up judgment must still be recorded stating:
- whether this workflow family should be expanded,
- what boundary held or failed,
- what next improvement is most justified.

## Bottom line
This pilot contract is successful if CRM Core Slice 1 becomes the first real proof that Delivery can govern a bounded professional support loop and TDE can hold the machine-execution state for that loop without prematurely absorbing CRM implementation ownership.
