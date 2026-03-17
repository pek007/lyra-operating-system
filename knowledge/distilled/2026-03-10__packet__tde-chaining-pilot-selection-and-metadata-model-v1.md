# TDE Chaining Pilot Selection and Metadata Model v1

Date: 2026-03-10
Owner: Lyra
Linked WO: `WO-2026-TDE-CHAINING-PILOT-V1`
Status: Draft execution packet

## Decision summary
Select **Pilot family A — implementation -> verification -> deployment-readiness review** as the first bounded real chaining pilot.

## Why this pilot family
This pilot is the best first proof point because it is:
- familiar and easy to reason about
- naturally bounded
- strongly aligned with existing TDE delivery/governance patterns
- suitable for deterministic predecessor/successor modeling
- rich enough to prove continuation, but not broad enough to create uncontrolled fan-out risk

## Pilot objective
Prove that canonical DB state can carry one staged objective forward through deterministic successor promotion without requiring human prompting between every stage.

## Canonical metadata model for v1 pilot
The pilot should use the canonical chaining fields already defined in `os/sops/TDE_CHAINING_CONTRACT_V1.md`:
- `depends_on`
- `activation_rule`
- `objective_id`
- `stage_id`
- `chain_policy`
- `activated_by`
- `activated_at`

### Required values for pilot v1
#### `depends_on`
- array of predecessor task IDs
- mandatory for successor tasks in the pilot chain

#### `activation_rule`
- `all_predecessors_done`
- mandatory for successor tasks in the pilot chain

#### `objective_id`
- required for pilot tasks in practice, even if optional in generic storage
- rationale: this pilot is explicitly intended to prove objective-linked continuation

#### `stage_id`
Recommended values:
- `implementation`
- `verification`
- `deploy_readiness_review`

#### `chain_policy`
For pilot v1, recommended minimum object:
```json
{
  "family": "pilot_family_a",
  "pilot_enabled": true,
  "promotion_cap_class": "bounded_single_successor"
}
```

#### `activated_by`
- runtime-populated provenance field referencing predecessor completion basis

#### `activated_at`
- runtime-populated ISO-8601 timestamp

## Proposed pilot chain shape

### Task A — implementation
- stage: `implementation`
- role: predecessor root task
- depends_on: none

### Task B — verification
- stage: `verification`
- depends_on: [`Task A`]
- activation_rule: `all_predecessors_done`
- objective_id: same as Task A

### Task C — deployment-readiness review
- stage: `deploy_readiness_review`
- depends_on: [`Task B`]
- activation_rule: `all_predecessors_done`
- objective_id: same as Task A

## Pilot modeling constraints
- only one approved chain family in the first execution pass
- no branching fan-out in v1 pilot
- no automatic successor creation; successors must already exist canonically
- no approval bypass at promotion or claim time
- no free-text or heuristic activation logic

## Immediate next implementation step
Implement canonical DB metadata support and runtime promotion evaluation for the above chain model, then build the happy-path and fail-closed verification cases around it.
