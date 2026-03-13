# TDE Decision Policy Runtime Embodiment v1

Status: Draft
Owner: Peter + Lyra
Product: Task Management (`A-007`)
Date: 2026-03-13
Related:
- `products/task-management/07-decisions/TDE_DECISION_TO_ADVANCEMENT_POLICY_V1.md`
- `products/task-management/07-decisions/TDE_PILOT_WORKFLOW_FAMILY_IMPLEMENTATION_VERIFICATION_READINESS_V1.md`
- `products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json`
- `schemas/tde_decision_advancement_record/v1.0.0.schema.json`
- `schemas/tde_decision_policy_envelope/v1.0.0.schema.json`
- `schemas/tde_decision_escalation_package/v1.0.0.schema.json`
- `tools/tde_chaining.py`
- `tools/tde_job_tick_runner.py`
- `tools/tde_state_store.py`

## Purpose
Define the first runtime embodiment decision for the new D-layer:
- what metadata key should bind a task/workflow stage to a decision policy envelope,
- where that key should live in canonical TDE state,
- and what minimum validation rules should run before autonomous progression is allowed.

## Decision
Adopt **`decision_policy_ref`** as the canonical metadata key for v1 runtime embodiment.

## Why this key
`decision_policy_ref` is the right v1 key because it is:
- explicit about purpose,
- artifact-oriented rather than implementation-specific,
- compatible with current metadata patterns,
- narrow enough to validate fail-closed,
- and easy to attach to task metadata without changing the meaning of existing chaining fields.

It separates two concerns cleanly:
- `chain_policy` -> how readiness promotion works
- `decision_policy_ref` -> which delegation envelope authorizes Product Owner decision-making

## Canonical location
For v1, `decision_policy_ref` should live inside each task's canonical metadata object in the DB-backed TDE state.

Example:
```json
{
  "depends_on": ["TDE-PILOT-IMPL-001"],
  "activation_rule": "all_predecessors_done",
  "objective_id": "OBJ-TDE-DECISION-ADVANCEMENT-PILOT",
  "stage_id": "verification",
  "workflow_family": "implementation_verification_readiness",
  "decision_policy_ref": "products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json",
  "chain_policy": {
    "pilot_enabled": true,
    "family": "implementation_verification_readiness"
  }
}
```

## v1 authority model
### Existing chaining fields remain authoritative for readiness mechanics
- `depends_on`
- `activation_rule`
- `objective_id`
- `stage_id`
- `chain_policy`
- `activated_by`
- `activated_at`

### New field for decision authority binding
- `decision_policy_ref`

### Recommended companion field
- `workflow_family`

`workflow_family` is not the authority source by itself.
It is a runtime cross-check and traceability field.
The authority source remains the referenced policy envelope.

## Minimum validation rule set
Before autonomous continuation is allowed for a task/stage, runtime should validate all of the following.

### V1-R1: `decision_policy_ref` presence
If a task is part of an autonomous decision-to-advancement family, `decision_policy_ref` must be present and non-empty.

Fail-closed result if missing:
- successor may still be modeled in state,
- but no Product Owner auto-advance is allowed,
- and the decision path must be blocked or escalated.

### V1-R2: reference resolvability
`decision_policy_ref` must resolve to a readable local artifact.

Fail-closed result if unresolved:
- no auto-advance,
- emit explicit validation reason,
- require manual fix or escalation.

### V1-R3: schema validity
The referenced artifact must validate against:
- `schemas/tde_decision_policy_envelope/v1.0.0.schema.json`

Fail-closed result if invalid:
- no auto-advance,
- validation artifact or error reason emitted.

### V1-R4: workflow family match
If both task metadata and policy envelope specify workflow family, they must match.

Fail-closed result if mismatched:
- no auto-advance,
- mark as policy/task mismatch.

### V1-R5: delegated role match
For v1 pilot flows, the envelope must delegate to:
- `Product Owner`

and escalate to:
- `Ultimate Decision-maker`

Fail-closed result if different:
- no auto-advance under this v1 policy path.

### V1-R6: outcome authorization
The selected decision outcome must be included in the policy envelope's `allowed_outcomes`.

Examples:
- `continue` must be allowed to continue automatically
- `research_further` must be explicitly allowed before a bounded research loop can run
- `retry` must be explicitly allowed before a bounded retry path can run

Fail-closed result if not authorized:
- no auto-advance,
- escalate or block.

### V1-R7: threshold checks
When relevant evidence exists, runtime should verify that the decision record is within the envelope's delegated thresholds:
- confidence at or above `confidence_threshold` for auto-continue/branch
- risk at or below `risk_threshold`
- cost impact at or below `cost_threshold` when present

For v1, if threshold data is unavailable or ambiguous, default fail-closed for autonomous advancement.

### V1-R8: research bound enforcement
If selected outcome is `research_further`, runtime must verify:
- the policy envelope allows `research_further`
- research budget exists
- the research loop count would not exceed `research_budget.max_rounds`

Fail-closed result if exceeded:
- escalate.

### V1-R9: hop bound enforcement
If autonomous progression would exceed `max_autonomous_hops`, runtime must stop auto-advancement and escalate or await review.

### V1-R10: write-scope boundary check
If the next step implies writes outside `write_scope_boundary`, auto-advance is not allowed.

Fail-closed result:
- escalate or block pending decision.

## Where validation should run
### 1. Metadata validation in `tde_state_store`
`tools/tde_state_store.py` should be extended so task metadata validation recognizes:
- `decision_policy_ref`
- `workflow_family`

Minimum checks here:
- type correctness
- non-empty string when present
- preserve/export compatibility

This is structural validation only, not full policy resolution.

### 2. Promotion-time cross-check in `tde_chaining`
`tools/tde_chaining.py` should remain focused on readiness promotion.

For v1, it may optionally record that a successor has:
- missing `decision_policy_ref`, or
- missing `workflow_family`

But chaining should not become the full decision engine.
Its role is to expose eligibility and obvious fail-closed reasons.

### 3. Decision-time enforcement in `tde_job_tick_runner`
`tools/tde_job_tick_runner.py` is the right place for first runtime enforcement of decision policy binding.

Before a claimed successor is auto-progressed under the D-layer, the runner should:
1. load task metadata
2. resolve `decision_policy_ref`
3. validate the envelope
4. verify selected outcome is allowed
5. verify threshold/budget/hop conditions
6. only then record the decision and proceed

If validation fails:
- write fail-closed reason into the tick artifact
- do not auto-advance
- if appropriate, require escalation packaging

## Artifact expectations in v1 runtime
### Decision record
Every autonomous decision under this model should produce a `tde_decision_advancement_record`.

### Escalation package
Every out-of-envelope case that needs Peter should produce a `tde_decision_escalation_package`.

### Tick artifact linkage
`tde_job_tick` artifacts should eventually include refs to:
- decision record path/id
- policy envelope ref
- escalation package ref when applicable

## Minimal fail-closed reasons to standardize
Recommend standard reason strings for v1:
- `decision_policy_ref_missing`
- `decision_policy_ref_unresolved`
- `decision_policy_envelope_invalid`
- `decision_policy_workflow_family_mismatch`
- `decision_outcome_not_authorized`
- `decision_threshold_data_missing`
- `decision_confidence_below_threshold`
- `decision_risk_above_threshold`
- `decision_cost_above_threshold`
- `decision_research_budget_exceeded`
- `decision_autonomous_hop_limit_exceeded`
- `decision_write_scope_boundary_exceeded`

## Recommended implementation sequence
### Slice 1 — metadata acceptance
Extend metadata validation and projection logic to accept:
- `decision_policy_ref`
- `workflow_family`

### Slice 2 — envelope resolver
Add a small resolver/validator helper that:
- reads the referenced policy artifact
- validates it structurally
- returns normalized envelope data or fail-closed reason

### Slice 3 — tick enforcement
Update `tde_job_tick_runner.py` so autonomous continuation for pilot family tasks requires a valid envelope and allowed outcome.

### Slice 4 — artifact linking
Add decision-record and escalation-package refs into tick artifacts.

## Non-goals for v1
- full generic policy engine
- remote policy resolution
- dynamic policy composition
- automatic policy inheritance across unrelated workflow families
- replacing existing chaining logic with decision logic

## Bottom line
For v1 runtime embodiment, the right move is simple:
- adopt `decision_policy_ref` as the canonical task metadata key,
- keep it in canonical DB task metadata,
- validate it fail-closed before autonomous continuation,
- and let the tick runner enforce the delegation envelope.

That gives TDE a concrete first embodiment of the D-layer without overbuilding the runtime.

## Environment / release note
This runtime embodiment should now be governed under the environment-separation model defined in:
- `TDE_ENVIRONMENT_AND_PROMOTION_MODEL_V1.md`