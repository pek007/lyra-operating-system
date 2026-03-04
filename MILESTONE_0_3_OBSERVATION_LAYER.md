# Milestone 0.3 — Observation layer bootstrap

Status: delivered (additive)

## Added
- Schemas: observation, observation_capture, observations_index.
- Source/retention policies for observations.
- Observation hashing utility (`sorted_json_v1`) and validator.
- Knowledge index generation now emits `knowledge/indexes/observations_index.json` with deterministic `rootHash`.
- `tools/validate_repo.py` now runs observation checks and evidence-observation link checks.

## TDE compatibility guarantee
- No TDE runtime semantics changed.
- Fail-closed applies only when artifacts explicitly claim `evidence.observations` links and links are invalid.
- Observation ingest/checks are additive governance controls.
