# Delivery State-Transition Policy v1

Status: Draft
Owner: Lyra
Date: 2026-03-11

## Purpose
Define the governing transition rules for Delivery Units (DUs) under the Delivery-as-Code model.

This policy turns the Delivery Unit schema into an executable control surface by specifying:
- allowed states
- required entry conditions
- approval boundaries
- fail-closed rules
- evidence expectations at each stage
- exception handling rules

## Design posture
This policy is designed to be:
- deterministic where possible
- fail-closed on unclear authority or missing evidence
- compatible with TDE’s scheduler-governed, bounded execution model
- broad enough to govern software and non-software delivery work

## Canonical state set
The authoritative DU states in v1 are:
- `proposed`
- `qualified`
- `planned`
- `in_execution`
- `in_verification`
- `release_recommended`
- `awaiting_approval`
- `approved`
- `released`
- `handed_off`
- `verified_in_use`
- `closed`
- `blocked`
- `retired`

## State semantics
### proposed
Candidate delivery unit exists but is not yet qualified for execution planning.

### qualified
The unit has enough clarity on objective, owner, scope, and risk to enter planning.

### planned
The execution contract is sufficiently defined: acceptance criteria, verification intent, dependencies, and approval profile exist.

### in_execution
Bounded work is being performed against the DU.

### in_verification
Implementation or change activity is complete enough to validate against acceptance and evidence requirements.

### release_recommended
The system has assembled a release or handoff recommendation based on available evidence.
This is a recommendation state, not permission to ship.

### awaiting_approval
The DU is waiting at a human or dual-control boundary before release/handoff.

### approved
A valid approval decision exists for the next release or handoff action.

### released
The DU change has been put into operational use by release.

### handed_off
The DU has been transferred to another operational owner, system, or consumer instead of directly released.

### verified_in_use
There is evidence that the released/handed-off change works in actual use or early operating conditions.

### closed
The DU is complete, with required post-delivery verification and closeout captured.

### blocked
Progress is intentionally halted by an unmet dependency, policy requirement, evidence gap, or authority gap.

### retired
The DU has been intentionally stopped and will not proceed further.

## Transition model
### Primary forward path
`proposed -> qualified -> planned -> in_execution -> in_verification -> release_recommended -> awaiting_approval|approved -> released|handed_off -> verified_in_use -> closed`

### Secondary control transitions
- any active non-terminal state may transition to `blocked`
- `blocked` may transition back to the most recent valid working state once the block is resolved
- non-terminal states may transition to `retired` with explicit rationale
- `release_recommended` may transition back to `planned` or `in_execution` if verification or release readiness fails
- `in_verification` may transition back to `in_execution` if rework is needed
- `approved` may transition back to `planned` or `in_execution` if approval assumptions become invalid before release/handoff

## Transition rules by state
## 1. proposed -> qualified
### Required
- `delivery_unit_id` exists
- `title` exists
- `product_id` exists
- `work_type` exists
- `objective_link` exists and is non-empty
- `owner` exists
- `scope_statement` exists
- initial `risk_class` exists
- initial `delivery_mode` exists

### Decision standard
The DU is clear enough to be governed, even if full planning is not complete.

### Fail closed when
- objective linkage is missing
- owner is missing
- scope is vague enough that acceptance criteria cannot later be derived safely

## 2. qualified -> planned
### Required
- at least one acceptance criterion exists
- verification class exists
- approval profile exists
- dependencies are declared or explicitly empty
- planning evidence exists or a planning artifact reference is attached
- required evidence profile is defined explicitly or derivable by work type

### Decision standard
The DU now has a usable execution contract.

### Fail closed when
- acceptance criteria are missing
- verification expectations are absent
- risk class is incompatible with missing approval profile
- required planning artifacts are not linked

## 3. planned -> in_execution
### Required
- all mandatory planning fields still valid
- no unresolved blocking dependency that prevents safe execution
- execution authority is valid for the route being taken
- for TDE-managed execution: bounded claim/execution conditions pass

### Decision standard
The system may begin work without ambiguity about intended outcome and governance posture.

### Fail closed when
- authority is unclear
- planning data drifted materially after planning
- DU is missing validation-capable acceptance criteria
- a policy binding blocks execution

## 4. in_execution -> in_verification
### Required
- implementation/change activity relevant to the current execution slice is complete
- implementation evidence exists
- changed artifacts are linked when applicable
- deviations from plan are recorded in exceptions or decision log

### Decision standard
The DU has enough completed work to test, review, or otherwise validate.

### Fail closed when
- execution claims completion but no implementation evidence exists
- material deviation occurred with no exception or decision record
- changed artifacts cannot be identified for a change-bearing work type

## 5. in_verification -> release_recommended
### Required
- verification evidence exists
- verification status satisfies the DU’s verification class or approved exception path
- unresolved critical defects or blockers do not remain open
- recommendation packet or equivalent rendered output exists
- known risks are summarized

### Decision standard
The system has enough validated evidence to recommend release or handoff.

### Fail closed when
- required verification evidence is missing
- verification failed or remains ambiguous
- recommendation packet cannot be rendered deterministically
- critical exceptions remain unresolved

## 6. release_recommended -> awaiting_approval
### Use when
- approval profile is `owner_required`, `human_required`, or `dual_control`
- release/handoff crosses a meaningful risk or consequence boundary

### Required
- release/handoff recommendation exists
- approval-required condition is recognized by policy
- DU is not missing mandatory risk or verification evidence

### Fail closed when
- approval is required but recommendation basis is incomplete
- approval profile is ambiguous

## 7. release_recommended -> approved
### Use when
- approval profile is `auto_allowed`
- policy explicitly permits autonomous advancement to approved
- all mandatory evidence gates are satisfied

### Required
- valid policy basis for autonomous approval
- generated or recorded approval decision exists

### Fail closed when
- auto-approval is assumed rather than explicitly permitted
- required evidence pack is incomplete

## 8. awaiting_approval -> approved
### Required
- explicit approval decision record exists
- approver has valid authority under policy
- approval timestamp and rationale exist
- any conditions attached to approval are recorded

### Fail closed when
- no valid decision record exists
- approval comes from an unauthorized actor
- approval is stale because material facts changed after recommendation

## 9. approved -> released
### Use when
- the DU is fulfilled by a release into operational use

### Required
- release route is appropriate for work type
- any release prerequisites are satisfied
- release evidence is produced

### Fail closed when
- approval conditions have not been satisfied
- release route introduces new unreviewed risk
- release evidence cannot be produced

## 10. approved -> handed_off
### Use when
- the DU is fulfilled by transfer to a consumer, operator, product team, or other boundary instead of direct release

### Required
- handoff target is explicit
- handoff packet exists
- receiving boundary or owner is identified
- handoff evidence is produced

### Fail closed when
- handoff target is unclear
- no transfer evidence exists
- handoff is being used to bypass release or verification obligations improperly

## 11. released|handed_off -> verified_in_use
### Required
- post-delivery verification evidence exists
- early-use confirmation or operational signal is captured
- material incidents/issues are logged if present

### Decision standard
The change has moved beyond formal completion and is shown to work in reality.

### Fail closed when
- there is no real-use validation signal
- known serious issues exist with no decision on disposition

## 12. verified_in_use -> closed
### Required
- closeout note or rendered post-delivery review exists
- open exceptions are closed or explicitly carried forward by decision
- key learning or miss capture exists where applicable

### Fail closed when
- post-delivery verification is absent
- closeout evidence is absent
- unresolved exceptions remain with no explicit disposition

## Blocked-state policy
### Any active state -> blocked
Allowed when:
- dependency unresolved
- approval pending
- evidence gap prevents safe progression
- authority unclear
- policy conflict exists
- verification shortfall requires pause

### Required when blocked
- explicit reason recorded
- owner recorded
- unblock condition recorded where possible
- timestamp recorded

### blocked -> prior working state
Allowed when:
- blocking condition resolved
- required evidence or decision now exists
- re-entry conditions for target state still pass

### Fail closed when
- block is marked resolved but underlying evidence or authority is still missing

## Retire-state policy
### Any non-terminal state -> retired
Allowed when:
- objective no longer valid
- DU superseded by another DU
- risk/return no longer justifies continuation
- strategic stop decision made

### Required
- explicit rationale
- decision owner
- timestamp
- successor/superseding reference when relevant

## Approval policy overlay
Approval profile determines whether recommendation can advance autonomously.

### auto_allowed
The DU may transition from `release_recommended` to `approved` only if policy explicitly allows autonomous approval for the current work type, risk class, and delivery mode.

### owner_required
Named owner approval is required.

### human_required
A human with designated authority is required.

### dual_control
Two distinct approvals or approval + independent review are required.

## Risk overlay
### low
Auto-approval may be permitted if work type and policy allow it.

### medium
Auto-approval should be limited; owner approval is preferred unless the work family is explicitly allowlisted.

### high
Human approval is the default.

### critical
Human approval plus enhanced verification or dual-control should be the default.

## Evidence overlay
Required evidence scales by work type and verification class.
The schema’s profile minima are baseline only.
Policy can require more, never less, unless an exception is explicitly approved.

### basic
Minimal but real evidence; useful for low-risk bounded changes.

### standard
Default professional evidence pack.

### enhanced
Adds stronger review, risk articulation, and post-delivery scrutiny.

### strict
Use for high/critical consequences; strongest evidence and approval discipline.

## Exception policy
Exceptions do not bypass policy silently.
They create an explicit governed path.

### Allowed exception uses
- temporary evidence gap with approval
- controlled verification shortfall with compensating control
- dependency-related temporary deviation
- scoped temporary control bypass with explicit expiry

### Required for all exceptions
- exception record
- owner
- reason
- status
- review or expiry point
- approval when the exception affects a mandatory gate

### Prohibited exception use
- bypassing approval for high-consequence changes without formal authorization
- hiding failed verification under narrative language only
- closing a DU without post-delivery verification unless explicitly approved as an exception

## Determinism and idempotency rules
- Re-evaluating a DU on unchanged state must not create contradictory transitions.
- A transition should be attributable to policy, evidence, and decision inputs.
- Automated advancement must emit or update a deterministic transition/evidence record.
- Repeated scheduler evaluation must preserve stable state when no new valid condition exists.

## TDE alignment rules
For TDE-managed execution, this policy should align with existing TDE control principles:
- scheduler-governed progression
- bounded claim/execution
- fail-closed authority checks
- evidence emission for state advancement
- no approval bypass through chaining or automation

Recommended v1 operating pattern:
- scheduler tick evaluates whether a DU can advance
- if conditions pass, DU progresses one controlled step
- if approval boundary is reached, DU pauses in `awaiting_approval`
- if evidence is insufficient, DU remains or moves to `blocked`

## Minimum transition evidence expectation
Each material transition should produce one of:
- state transition record in canonical store
- rendered gate packet
- evidence record tied to the gate
- decision record where human judgment was required

## Decision recommendation
Adopt this as the baseline transition policy for Delivery-as-Code v1, then refine by work-type profile during pilot use.

## Next dependencies
- rendered packet templates v1
- evidence requirement matrix by work type x risk class x verification class
- pilot Delivery Unit mapped to a live TDE slice
