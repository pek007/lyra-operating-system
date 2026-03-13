# TDE Pilot Workflow Family — Implementation -> Verification -> Readiness v1

Status: Draft
Owner: Peter + Lyra
Product: Task Management (`A-007`)
Date: 2026-03-13
Related:
- `products/task-management/07-decisions/TDE_DECISION_TO_ADVANCEMENT_POLICY_V1.md`
- `products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json`
- `os/sops/TDE_CHAINING_CONTRACT_V1.md`
- `governance/TDE_CHAINING_OPERATING_NOTE_V1.md`
- `templates/TDE_CHAINED_TASK_TEMPLATE_V1.md`

## Purpose
Define the first real pilot workflow family for the new decision-to-advancement layer.

This artifact turns the policy and schemas into one bounded operational family that can be piloted in TDE with explicit:
- stages,
- successor rules,
- Product Owner decision rights,
- escalation points,
- and `research_further` behavior.

## Workflow family ID
`implementation_verification_readiness`

## Why this family first
This is the best first pilot because it is already close to current TDE chaining practice:
- naturally staged,
- deterministic in its happy path,
- evidence-bearing,
- low ambiguity in normal continuation,
- but rich enough to test retry, research, and escalation.

It also aligns with the already proven chaining pattern:
- implementation -> verification -> deployment-readiness review

## Scope
### In scope
- internal staged work in TDE
- bounded successor activation
- Product Owner delegated decisions inside the approved envelope
- escalation to Ultimate Decision-maker for out-of-policy cases
- one bounded `research_further` loop where needed

### Out of scope
- automatic creation of broad new task families
- external communications
- autonomous approval bypass
- open-ended research loops
- strategic reprioritization across unrelated objectives

## Role model for this family
### Product Owner
Responsible for:
- evaluating execution evidence at each stage boundary
- selecting the next outcome within policy
- triggering at most the allowed bounded research loop
- escalating to Peter when authority bounds are exceeded

### Ultimate Decision-maker
Peter decides when:
- the next move crosses policy limits
- evidence remains insufficient after bounded research
- a meaningful architecture, scope, cost, or strategic trade-off appears

## Canonical stages
### Stage 1 — Implementation
Purpose:
- deliver the intended capability change or artifact change

Typical evidence:
- execution receipt
- implementation note
- diff / artifact update
- local verification signal if available

Nominal next decision:
- `continue` to Stage 2 (Verification)

### Stage 2 — Verification
Purpose:
- verify whether implementation outcome is valid enough to proceed

Typical evidence:
- test result
- validation note
- runtime or artifact verification output
- defect note if applicable

Nominal next decisions:
- `continue` to Stage 3 (Readiness review) if verification passes
- `retry` back to bounded implementation correction if verification fails in a known way
- `research_further` if verification is mixed/ambiguous and more evaluation could resolve the uncertainty
- `escalate` if the implications exceed Product Owner authority

### Stage 3 — Readiness review
Purpose:
- decide whether the verified change is ready for the next operational step in its lane

Typical evidence:
- verification evidence bundle
- readiness review note
- outstanding risk / issue list

Nominal next decisions:
- `complete_stop` if the chain target has been achieved
- `branch` to closeout or improvement capture
- `escalate` if readiness involves a higher-order trade-off

### Optional Stage 4 — Closeout / improvement capture
Purpose:
- capture learning, follow-up friction, or residual improvement work

Typical evidence:
- closeout note
- improvement item
- error / friction artifact

Nominal next decisions:
- `complete_stop`
- `branch` into bounded improvement work if already authorized

## Stage transitions
### Transition A — Implementation -> Verification
Allowed when:
- implementation evidence exists
- no hard blocker is open
- next step remains within approved workflow family
- authority check is `within_policy`

Default outcome:
- `continue`

Successor handling:
- verification task becomes ready under existing chaining rules

### Transition B — Verification -> Readiness review
Allowed when:
- verification evidence meets threshold
- confidence is at or above policy threshold
- risk remains at or below the policy threshold
- no mandatory escalation trigger is hit

Default outcome:
- `continue`

Alternative outcomes:
- `retry`
- `research_further`
- `escalate`

### Transition C — Readiness review -> Closeout / improvement capture
Allowed when:
- the main delivery intent is satisfied
- remaining work is bounded and inside the policy envelope

Default outcome:
- `branch` or `complete_stop`

## Decision gates by stage
### Gate G1 — Post-implementation gate
Question:
- Was the implementation completed successfully enough to justify verification?

Product Owner may:
- continue to verification
- block
- defer
- research further

Escalate if:
- implementation result materially changes scope or architecture
- expected next step crosses write-scope or risk boundary

### Gate G2 — Post-verification gate
Question:
- Is the result sufficiently verified to proceed to readiness review?

Product Owner may:
- continue
- retry
- block
- defer
- research further

Escalate if:
- verification reveals a material trade-off
- evidence remains insufficient after one bounded research loop
- risk exceeds `medium`
- required next step would cross policy boundary

### Gate G3 — Post-readiness gate
Question:
- Is the workflow family complete, or should it branch into bounded closeout/improvement work?

Product Owner may:
- complete_stop
- branch
- block
- defer

Escalate if:
- branch would create a new workflow family
- the next step materially affects product strategy, architecture, or external exposure

## `research_further` behavior in this family
This family explicitly allows one bounded research loop, primarily at verification.

### Typical triggers
- mixed verification signals
- inconsistent evidence
- uncertainty over whether a defect is real or incidental
- unclear readiness implications that may be resolved by deeper evaluation

### Bounds
- maximum rounds: 1
- maximum minutes: 30
- no authority expansion during research
- reevaluation must return to the same decision gate

### After research returns
The Product Owner must re-run the gate and choose one of:
- `continue`
- `retry`
- `block`
- `defer`
- `escalate`

If evidence is still insufficient after the bounded research loop, default to `escalate`.

## Policy envelope for this family
Canonical reference artifact:
- `products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json`

Current reference settings:
- confidence threshold: `0.75`
- risk threshold: `medium`
- cost threshold: `low`
- max autonomous hops: `2`
- retry limit: `1`
- research rounds: `1`

## Example decision patterns
### Happy path
1. Implementation finishes.
2. Product Owner records `continue`.
3. Verification becomes ready.
4. Verification passes.
5. Product Owner records `continue`.
6. Readiness review becomes ready.
7. Readiness review passes.
8. Product Owner records `complete_stop` or `branch` to closeout.

### Controlled retry path
1. Verification finds a known bounded defect.
2. Product Owner records `retry`.
3. Correction step is executed within the same family boundary.
4. Verification is re-run once.

### Research path
1. Verification results are mixed.
2. Product Owner records `research_further`.
3. Bounded evaluation step runs.
4. Gate G2 is rerun.
5. If uncertainty remains, escalate.

### Escalation path
1. Verification or readiness reveals a non-trivial architecture or scope trade-off.
2. Product Owner prepares escalation package.
3. Peter decides.

## Runtime embodiment target
For this pilot family, the runtime should eventually support:
- chained successor activation using existing TDE chaining semantics
- decision recording via `tde_decision_advancement_record`
- policy validation against `tde_decision_policy_envelope`
- escalation packaging via `tde_decision_escalation_package`

## Acceptance criteria for pilot use
This family is ready for first practical pilot use when:
- all stages are representable in canonical TDE state
- successor relationships are explicit
- the policy envelope is attached or referenced
- a Product Owner can record all decision outcomes cleanly
- one `research_further` path is modeled explicitly
- one escalation path is modeled explicitly
- no step relies on transcript memory alone to determine what happens next

## Recommended immediate next implementation slice
1. Decide whether `decision_policy_ref` should become the canonical metadata key in task/runtime state.
2. Wire runtime validation so a chain cannot auto-advance without a valid policy envelope reference.
3. Add schema-validated example artifacts to automated tests.
4. Bind one real pilot chain in canonical TDE state.

## Reference example pack added
The first example pack for this workflow family now includes:
- `products/task-management/07-decisions/examples/TDE_DECISION_ADVANCEMENT_RECORD_CONTINUE_V1.json`
- `products/task-management/07-decisions/examples/TDE_DECISION_ADVANCEMENT_RECORD_RESEARCH_FURTHER_V1.json`
- `products/task-management/07-decisions/examples/TDE_DECISION_ESCALATION_PACKAGE_V1.json`
- `products/task-management/07-decisions/examples/TDE_PILOT_CHAIN_EXAMPLE_V1.md`

## Bottom line
This pilot family is the first practical embodiment of the new D-layer.

It is simple enough to pilot safely, but rich enough to test the important mechanics:
- automatic continuation,
- bounded retry,
- bounded deeper research,
- and clean escalation from Product Owner to Ultimate Decision-maker.
