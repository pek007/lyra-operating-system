# Builder A Packet

Status: ready
Factory run ID: `SF-ORCH-2026-05-06-PHASE3B-ISOLATED-PARALLEL-BUILDERS`
TDE intake: `control/tde-intake/software-factory-phase3b-isolated-worktree-parallel-builder-proof-2026-05-06.json`
Owning product: Delivery / Software Factory
Owner/reviewer: Peter Eklind / Lyra Operations

## Objective
Create the file-scope lock artifact in isolated copy A.

## Assigned artifact path
`workspaces/software-factory/dry-runs/2026-05-06-phase3b-isolated-worktree-parallel-builder-proof/isolated-copy-builder-a/products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_BUILDER_FILE_SCOPE_LOCK_V0.md`

## Assigned result path
`workspaces/software-factory/dry-runs/2026-05-06-phase3b-isolated-worktree-parallel-builder-proof/worker-results/BUILDER_A_RESULT.md`

## Required content
Define a v0 file-scope lock/check discipline for future Software Factory parallel builders: declared write scopes, overlap detection, lock owner, read-only exceptions, conflict/hold behavior, and evidence fields.

## Boundary
Do not touch Builder B paths or root final artifacts.
