# Milestone 0.4 — TaskOps backbone

Status: delivered (additive)

## Scope
Implement universal TaskOps control backbone without changing TDE runtime semantics.

## Delivered
- `taskops_work_packet` schema + registry entry.
- Side-effect contract policy (`knowledge/policies/taskops_side_effect_contracts.v1.yaml`).
- Autonomy policy (`knowledge/policies/taskops_autonomy_policy.v1.yaml`).
- Work packet template under `knowledge/taskops/work_packets/`.
- Validator: `tools/taskops/validate_work_packets.py` integrated into `tools/validate_repo.py`.

## Guardrail
- This milestone adds policy/validation controls only.
- TDE execution flow is unchanged.
