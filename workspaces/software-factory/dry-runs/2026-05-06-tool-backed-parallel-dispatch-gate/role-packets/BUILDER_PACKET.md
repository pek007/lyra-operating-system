# Builder Packet

Status: ready / bounded
Factory run ID: `SF-ORCH-2026-05-06-TOOL-BACKED-PARALLEL-DISPATCH-GATE`
TDE intake: `control/tde-intake/software-factory-worktree-branch-lock-tooling-2026-05-06.json`
Quality gate matrix: `products/delivery/06-architecture/SOFTWARE_FACTORY_PROFESSIONAL_QUALITY_GATE_MATRIX_V0.yaml`
Owning product: `products/delivery`
Owner/reviewer: Peter Eklind / Lyra Operations
GO/HOLD/NO-GO: GO after pre-dispatch lock checker pass

## Objective

Create one assigned Delivery architecture artifact in the worker's isolated-copy path. Do not edit root final artifacts directly.

## Target repo/worktree

- Root workspace: `/Users/lyra/.openclaw/workspace`
- Run folder: `workspaces/software-factory/dry-runs/2026-05-06-tool-backed-parallel-dispatch-gate`

## Allowed paths

- Builder A may write only `workspaces/software-factory/dry-runs/2026-05-06-tool-backed-parallel-dispatch-gate/isolated-copy-builder-a/products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_DISPATCH_PACKET_TEMPLATE_V0.md` and `worker-results/BUILDER_A_RESULT.md`.
- Builder B may write only `workspaces/software-factory/dry-runs/2026-05-06-tool-backed-parallel-dispatch-gate/isolated-copy-builder-b/products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_DISPATCH_GATE_RUNBOOK_V0.md` and `worker-results/BUILDER_B_RESULT.md`.
- Read-only inspection is allowed for the Worker Result Contract, file-scope lock spec, integration checklist, role packet, and lock manifest.

## Prohibited paths/actions

- Do not change credentials or access settings.
- Do not push, merge, release, or deploy.
- Do not create persistent agents.
- Do not edit root final artifacts directly.
- Do not perform external sends or client communications.
- Do not mutate PXS, PXS CRM, Vega Inquiry Engine paths, customer data, or unrelated products.
- Do not perform destructive cleanup.

## Non-goals

- No git worktree automation.
- No CI/review feedback routing.
- No production release.
- No owner-bound product decision changes.

## Professional quality gates

- Artifact is concise, operational, and consistent with the lock checker and Worker Result Contract.
- Changed files remain within the assigned lock scope.
- Worker result follows `products/delivery/06-architecture/SOFTWARE_FACTORY_WORKER_RESULT_CONTRACT_V0.md`.
- Authority boundary is explicit.

## Validation commands

```bash
python3 tools/software_factory_file_scope_lock_check.py workspaces/software-factory/dry-runs/2026-05-06-tool-backed-parallel-dispatch-gate/manifests/pre-dispatch-lock-manifest.json
python3 tools/validate_software_factory_orchestration.py workspaces/software-factory/dry-runs/2026-05-06-tool-backed-parallel-dispatch-gate
```

## Expected Builder output

- One assigned Markdown artifact in the isolated-copy path.
- One worker result Markdown file with changed-file list, evidence, validation status, authority boundary, and recommended integration state.

## Evidence target

- `control/execution-evidence/software-factory-tool-backed-parallel-dispatch-gate-2026-05-06.md`

## Rollback / abort

Abort if: pre-dispatch lock checker fails, assigned scope overlaps another Builder, a root final artifact would need direct worker edits, validation cannot be run or explained, or any prohibited action is required.
Rollback path: do not integrate isolated-copy output; leave worker result as `blocked`, `issue`, or `decision-needed` with the exact blocker.
