# Observation tooling

- `hash_util.py`: deterministic canonicalization + record hashing (`sorted_json_v1`).
- `validate_observations.py`: schema, hash, source-policy, blob, and provenance checks.

These checks are additive and do not alter TDE execution semantics.
