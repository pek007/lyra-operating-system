# CRM Core Slice 1 Pilot Kickoff Packet

Date: 2026-04-13
Owner: Lyra
Status: Prepared, pending explicit start conditions
Related intake: `control/tde-intake/crm-core-slice-1-change-to-evidence-pilot-2026-04-13.json`
Related contract: `products/delivery/04-execution/CRM_CORE_SLICE_1_CHANGE_TO_EVIDENCE_PILOT_CONTRACT_V1.md`

## Purpose
Provide the first bounded kickoff packet for the CRM Core Slice 1 change-to-evidence pilot.

This packet is the explicit reviewable start bundle for one real pilot cycle. It does not itself imply that CRM implementation has begun.

## Pilot cycle in scope
**CRM Core Slice 1 — Structured account/contact and post-meeting capture foundation**

This kickoff packet governs the support loop around the slice:
- kickoff preparation
- implementation handoff readiness
- verification capture expectation
- evidence assembly expectation
- completion/abort review expectation

## Preconditions review
### Satisfied now
- bounded slice exists: `CRM_CORE_SLICE_1_DELIVERY_BRIEF_2026-04-03.md`
- architecture note exists: `CRM_CORE_SLICE_1_ARCHITECTURE_NOTE_2026-04-03.md`
- test/evidence expectations exist: `CRM_CORE_SLICE_1_TEST_AND_EVIDENCE_SPEC_2026-04-03.md`
- kickoff acceptance structure exists: `CRM_CORE_SLICE_1_KICKOFF_ACCEPTANCE_NOTE_2026-04-03.md`
- pilot boundary and contract are explicit

### Still required before active implementation start
- explicit confirmation that CRM Core Slice 1 remains the accepted restart slice
- explicit identification of the implementation lane for this cycle
- explicit confirmation that the current implementation split remains: internal/Lyra for scope and architecture judgment, coding-agent-supported implementation for the bounded slice

## Role split for this cycle
### PXS Tools / CRM
Owns:
- product embodiment
- implementation decisions inside the accepted slice
- code and local product changes

### Delivery
Owns:
- pilot delivery envelope
- verification evidence completeness gate
- completion review discipline

### TDE / Task Management
Owns:
- machine-execution support state for this cycle
- visibility of kickoff, verification, evidence, and follow-up progression
- explicit follow-up or abort state if the cycle cannot complete cleanly

## Bounded kickoff contents
### 1. Slice reference
Use the existing bounded slice only:
- account records
- contact records
- structured post-meeting capture
- structured next-step capture
- basic relationship/context continuity

### 2. Out of scope reminder
Do not expand this cycle into:
- opportunity/pipeline logic
- proposal generation
- broad automation/workflow behavior
- dashboards/reporting expansion
- sync/integration concerns
- generalized CRM platform work

### 3. Implementation expectation
Implementation is expected to occur outside TDE primary ownership once the implementation lane is explicitly identified.

TDE is supporting the cycle, not replacing CRM implementation judgment.

### 4. Verification expectation
At minimum, the cycle must produce reviewable verification covering:
- account create/update behavior
- contact create/update behavior
- post-meeting capture behavior
- next-step capture behavior
- one end-to-end integration path through the slice

### 5. Delivery gate expectation
Before the cycle can be treated as verification-captured, the evidence must include at least:
- implementation summary
- test summary with pass/fail or mixed-result status
- explicit out-of-scope confirmation
- explicit unresolved issues / limitations

### 6. Expected next artifacts from the cycle
- one implementation summary artifact
- one verification/test capture artifact
- one evidence pack artifact
- one completion/abort/follow-up judgment artifact

## TDE state target for this packet
This packet supports transition from:
- `ready-for-kickoff-packet`

to:
- `kickoff-packet-prepared`

It should not imply transition to `implementation-in-progress` until the remaining pre-start conditions are explicitly satisfied.

## Recommended next action
Use this kickoff packet as the bounded start bundle, then record the explicit implementation-lane confirmation needed to move the pilot from prepared state into active implementation support.

## Bottom line
The pilot now has a real kickoff packet.
The next move is not more design expansion, but one explicit implementation-start confirmation so the first CRM pilot cycle can begin under the agreed Delivery/TDE boundary.
