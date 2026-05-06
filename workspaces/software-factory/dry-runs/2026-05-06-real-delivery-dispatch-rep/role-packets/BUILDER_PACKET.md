# Builder Packet

Status: ready / bounded
Factory run ID: `SF-ORCH-2026-05-06-REAL-DELIVERY-DISPATCH-REP`
TDE intake: `control/tde-intake/software-factory-real-delivery-dispatch-rep-2026-05-06.json`
Quality gate matrix: `products/delivery/06-architecture/SOFTWARE_FACTORY_PROFESSIONAL_QUALITY_GATE_MATRIX_V0.yaml`
Owning product: `products/delivery`
Owner/reviewer: Peter Eklind / Lyra Operations
GO/HOLD/NO-GO: GO after pre-dispatch lock checker pass

## Objective

Create one useful Delivery operating artifact in the worker's isolated-copy path. Do not edit root final artifacts directly.

## Target repo/worktree

- Root workspace: `/Users/lyra/.openclaw/workspace`
- Run folder: `workspaces/software-factory/dry-runs/2026-05-06-real-delivery-dispatch-rep`

## Allowed paths

- Builder A may write only `workspaces/software-factory/dry-runs/2026-05-06-real-delivery-dispatch-rep/isolated-copy-builder-a/products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_DISPATCH_READINESS_CHECKLIST_V0.md` and `worker-results/BUILDER_A_RESULT.md`.
- Builder B may write only `workspaces/software-factory/dry-runs/2026-05-06-real-delivery-dispatch-rep/isolated-copy-builder-b/products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_DISPATCH_FRICTION_LOG_V0.md` and `worker-results/BUILDER_B_RESULT.md`.
- Read-only inspection is allowed for the dispatch template, gate runbook, Worker Result Contract, role packet, and lock manifest.

## Prohibited paths/actions

- Do not change credentials or access settings.
- Do not push, merge, release, or deploy.
- Do not create persistent agents.
- Do not create git worktrees or branches automatically in this run.
- Do not edit root final artifacts directly.
- Do not perform external sends or client communications.
- Do not mutate PXS, PXS CRM, Vega Inquiry Engine paths, customer data, or unrelated products.
- Do not perform destructive cleanup.

## Non-goals

- No automatic git worktree/branch creation.
- No CI/review feedback routing.
- No production release.
- No owner-bound product decision changes.

## Professional quality gates

- Artifact is concise, operational, and useful for the next Software Factory run.
- Changed files remain within the assigned lock scope.
- Worker result follows `products/delivery/06-architecture/SOFTWARE_FACTORY_WORKER_RESULT_CONTRACT_V0.md`.
- Authority boundary is explicit.

## Validation commands

```bash
python3 tools/software_factory_file_scope_lock_check.py workspaces/software-factory/dry-runs/2026-05-06-real-delivery-dispatch-rep/manifests/pre-dispatch-lock-manifest.json
python3 tools/validate_software_factory_orchestration.py workspaces/software-factory/dry-runs/2026-05-06-real-delivery-dispatch-rep
```

## Expected Builder output

- One assigned Markdown artifact in the isolated-copy path.
- One worker result Markdown file with changed-file list, evidence, validation status, authority boundary, and recommended integration state.

## Evidence target

- `control/execution-evidence/software-factory-real-delivery-dispatch-rep-2026-05-06.md`

## Rollback / abort

Abort if: pre-dispatch lock checker fails, assigned scope overlaps another Builder, automatic worktree/branch creation would be required, a root final artifact would need direct worker edits, validation cannot be run or explained, or any prohibited action is required.
Rollback path: do not integrate isolated-copy output; leave worker result as `blocked`, `issue`, or `decision-needed` with the exact blocker.
