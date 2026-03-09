# TDE Chained Task Template v1

Use this when modeling a bounded staged workflow for TDE chaining.

## Example workflow family
Implementation -> verification -> deployment-readiness review

## Example task metadata
```json
{
  "depends_on": ["TDE-CHAIN-001"],
  "activation_rule": "all_predecessors_done",
  "objective_id": "OBJ-TDE-FOUNDATION",
  "stage_id": "verification",
  "chain_policy": {
    "pilot_enabled": true,
    "family": "pilot-a"
  }
}
```

## Modeling checklist
- Task has a stable task ID
- Predecessor IDs are explicit and correct
- Successor is a real next step, not a vague future possibility
- Workflow is bounded
- `activation_rule` is `all_predecessors_done`
- `chain_policy.pilot_enabled` is `true`
- `chain_policy.family` matches an approved family
- `objective_id` is added when part of a larger target
- `stage_id` is used for readability

## Example 3-stage chain

### Stage 1 — Implementation
- Task ID: `TDE-CHAIN-001`
- Title: Implement capability X
- Typical initial status: `Active`
- Metadata: optional

### Stage 2 — Verification
- Task ID: `TDE-CHAIN-002`
- Title: Verify capability X
- Typical initial status: `Triage` or `Waiting`
- Metadata:
```json
{
  "depends_on": ["TDE-CHAIN-001"],
  "activation_rule": "all_predecessors_done",
  "objective_id": "OBJ-TDE-FOUNDATION",
  "stage_id": "verification",
  "chain_policy": {
    "pilot_enabled": true,
    "family": "pilot-a"
  }
}
```

### Stage 3 — Deployment-readiness review
- Task ID: `TDE-CHAIN-003`
- Title: Review deployment readiness for capability X
- Typical initial status: `Waiting`
- Metadata:
```json
{
  "depends_on": ["TDE-CHAIN-002"],
  "activation_rule": "all_predecessors_done",
  "objective_id": "OBJ-TDE-FOUNDATION",
  "stage_id": "deployment-readiness-review",
  "chain_policy": {
    "pilot_enabled": true,
    "family": "pilot-a"
  }
}
```

## Notes
- Current chaining support is pilot-gated and intentionally narrow.
- Use only for deterministic staged handoffs.
- If the next step requires real human choice, do not model it as automatic chaining.
