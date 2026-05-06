# Builder Packet

Status: ready
Factory run ID: `SF-ORCH-2026-05-06-PHASE3B-ISOLATED-PARALLEL-BUILDERS`
TDE intake: `control/tde-intake/software-factory-phase3b-isolated-worktree-parallel-builder-proof-2026-05-06.json`
Quality gate matrix: `products/delivery/06-architecture/SOFTWARE_FACTORY_PROFESSIONAL_QUALITY_GATE_MATRIX_V0.yaml`
Owning product: Delivery / Software Factory
Owner/reviewer: Peter Eklind / Lyra Operations
GO/HOLD/NO-GO: GO for narrow isolated-copy builder work only

## Objective
Create one assigned Delivery-owned architecture artifact in the assigned isolated copy and write a Worker Result Contract-conformant result.

## Target repo/worktree
- Root workspace: `/Users/lyra/.openclaw/workspace`
- Isolated copies: `/Users/lyra/.openclaw/workspace/workspaces/software-factory/dry-runs/2026-05-06-phase3b-isolated-worktree-parallel-builder-proof/isolated-copy-builder-a` and `/Users/lyra/.openclaw/workspace/workspaces/software-factory/dry-runs/2026-05-06-phase3b-isolated-worktree-parallel-builder-proof/isolated-copy-builder-b`

## Allowed paths
- Builder-specific isolated-copy artifact path from the assigned Builder A or Builder B packet.
- Builder-specific worker result path from the assigned Builder A or Builder B packet.

## Prohibited paths/actions
- Do not change credentials or access settings.
- Do not push, merge, release, or deploy.
- Do not create persistent agents.
- Do not modify PXS, PXS CRM, Vega Inquiry Engine, client data, or external communications.
- Do not modify root final artifacts directly; Integrator owns root adoption.
- Do not perform destructive cleanup.

## Non-goals
- No runtime dispatcher implementation.
- No Control Panel UI changes.
- No TDE kernel schema changes.
- No release or deployment lane.

## Professional quality gates
- Artifact is concise and operational.
- Artifact supports future Software Factory isolation or integration discipline.
- Result follows `products/delivery/06-architecture/SOFTWARE_FACTORY_WORKER_RESULT_CONTRACT_V0.md`.
- Authority boundary is explicit.

## Validation commands
```bash
python3 tools/validate_software_factory_orchestration.py workspaces/software-factory/dry-runs/2026-05-06-phase3b-isolated-worktree-parallel-builder-proof
```

## Expected Builder output
- Write assigned isolated-copy artifact.
- Write assigned worker result with changed files, evidence, validation, blockers/risks, authority boundary, and recommended integration state.

## Evidence target
- Final evidence will be written to `control/execution-evidence/software-factory-phase3b-isolated-worktree-parallel-builder-proof-2026-05-06.md` by the integrator.

## Rollback / abort
Rollback path: discard the assigned isolated copy output and retain the worker result explaining why.
Abort if: the work requires credentials, push, merge, release, deploy, persistent agents, PXS/PXS CRM mutation, external communications, destructive cleanup, or paths outside the assigned isolated-copy/result files.
