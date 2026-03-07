# Activation — Governance Policy Assembly v0.1

## Preferred (target) lane
Use git-pinned dependency (submodule/subtree/release artifact).

## Interim (allowed) lane
Controlled copy-sync into PXS with explicit provenance and removal marker.

## Activation Steps (PXS)
1. Register assembly in `PXS_ASSEMBLY_LOCK.md`.
2. Add policy pack files (pinned or interim copy).
3. Link checklist in PXS operating flow for:
   - authority changes
   - new external tool/service usage
   - OpenClaw config-impacting changes
4. Require evidence reference for gated changes.

## Daily Use
- Treat this pack as mandatory guardrail for high-risk operational changes.
- Do not modify copied policy files directly in PXS; update at Lyra OS source and resync.
