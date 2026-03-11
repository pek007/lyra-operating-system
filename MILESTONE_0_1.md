# Milestone 0.1 — Machine-checkable governance bootstrap

Status: in-progress
Scope: non-invasive bootstrap that does **not** modify TDE execution semantics.

## Delivered
- `schemas/` authority with registry and v1 schemas for TDE artifacts + decision metadata + scorecard.
- `tools/validate_repo.py` single entrypoint.
- Deterministic generators:
  - `tools/gen_inventory.py`
  - `tools/gen_knowledge_indexes.py`
  - `tools/gen_reports_index.py`
- CI workflow: `.github/workflows/governance-machine-check.yml`
- Eval skeleton: `eval/slices/safety_refusal_smoke.v1.yaml` + baseline snapshot.

## Local commands
```bash
python tools/validate_repo.py --fix   # regenerate derivatives
python tools/validate_repo.py         # validate + drift check
```

## Guardrail: TDE compatibility
- Existing TDE artifacts remain valid unless they explicitly claim `artifactType` + `schemaVersion` and fail the corresponding schema.
- Artifacts without `artifactType` are not rejected in this milestone.
- This keeps bootstrap additive and avoids contradiction with active TDE development slices.
