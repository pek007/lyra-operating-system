# TDE Pilot Chain Example v1

Status: Reference
Workflow family: `implementation_verification_readiness`
Policy envelope:
- `products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json`
Pilot workflow mapping:
- `products/task-management/07-decisions/TDE_PILOT_WORKFLOW_FAMILY_IMPLEMENTATION_VERIFICATION_READINESS_V1.md`

## Purpose
Show a concrete chained-task shape for the first pilot family, including where the policy reference attaches.

## Example chain

### Stage 1 — Implementation
- Task ID: `TDE-PILOT-IMPL-001`
- Title: Implement decision-advancement pilot runtime note
- Status: `Active`
- Metadata:
```json
{
  "objective_id": "OBJ-TDE-DECISION-ADVANCEMENT-PILOT",
  "stage_id": "implementation",
  "workflow_family": "implementation_verification_readiness",
  "decision_policy_ref": "products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json"
}
```

### Stage 2 — Verification
- Task ID: `TDE-PILOT-VERIFY-001`
- Title: Verify decision-advancement pilot runtime note
- Status: `Waiting`
- Metadata:
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

### Stage 2b — Research loop (optional)
- Task ID: `TDE-PILOT-RESEARCH-001`
- Title: Investigate mixed verification signals for decision-advancement pilot
- Status: `Waiting`
- Metadata:
```json
{
  "depends_on": ["TDE-PILOT-VERIFY-001"],
  "activation_rule": "all_predecessors_done",
  "objective_id": "OBJ-TDE-DECISION-ADVANCEMENT-PILOT",
  "stage_id": "verification-research",
  "workflow_family": "implementation_verification_readiness",
  "decision_policy_ref": "products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json",
  "chain_policy": {
    "pilot_enabled": true,
    "family": "implementation_verification_readiness"
  }
}
```

### Stage 3 — Readiness review
- Task ID: `TDE-PILOT-READY-001`
- Title: Review readiness for decision-advancement pilot
- Status: `Waiting`
- Metadata:
```json
{
  "depends_on": ["TDE-PILOT-VERIFY-001"],
  "activation_rule": "all_predecessors_done",
  "objective_id": "OBJ-TDE-DECISION-ADVANCEMENT-PILOT",
  "stage_id": "readiness-review",
  "workflow_family": "implementation_verification_readiness",
  "decision_policy_ref": "products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json",
  "chain_policy": {
    "pilot_enabled": true,
    "family": "implementation_verification_readiness"
  }
}
```

### Stage 4 — Closeout / improvement capture (optional)
- Task ID: `TDE-PILOT-CLOSE-001`
- Title: Capture closeout and improvement follow-up for decision-advancement pilot
- Status: `Waiting`
- Metadata:
```json
{
  "depends_on": ["TDE-PILOT-READY-001"],
  "activation_rule": "all_predecessors_done",
  "objective_id": "OBJ-TDE-DECISION-ADVANCEMENT-PILOT",
  "stage_id": "closeout",
  "workflow_family": "implementation_verification_readiness",
  "decision_policy_ref": "products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json",
  "chain_policy": {
    "pilot_enabled": true,
    "family": "implementation_verification_readiness"
  }
}
```

## Notes
- `decision_policy_ref` is the new key addition in this example pack; it shows where decision-to-advancement delegation attaches.
- `chain_policy` continues to govern readiness promotion behavior.
- In runtime terms, chaining determines whether the successor can become ready, while the decision artifacts determine whether the Product Owner is authorized to select that path.
