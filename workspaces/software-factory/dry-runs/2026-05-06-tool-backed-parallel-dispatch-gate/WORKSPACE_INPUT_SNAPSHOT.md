# Software Factory Workspace Input Snapshot

Status: ready / scoped
Snapshot ID: `SF-SNAPSHOT-2026-05-06-TOOL-BACKED-PARALLEL-DISPATCH-GATE`
Factory run ID: `SF-ORCH-2026-05-06-TOOL-BACKED-PARALLEL-DISPATCH-GATE`
Target workspace: `/Users/lyra/.openclaw/workspace`
Target product/repo: `products/delivery` / Lyra OS root repository
Captured by: Lyra / Delivery Software Factory
Captured at: 2026-05-06 16:58 CEST

## Workspace operating-package check

Readiness disposition: ready for bounded internal Delivery proof. Process discovery routes this work through Delivery / task execution controls and TDE evidence discipline.

## Product/domain inputs

- `control/execution-evidence/software-factory-worktree-branch-lock-tooling-2026-05-06.md`
- `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_BUILDER_FILE_SCOPE_LOCK_V0.md`
- `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_BUILDER_INTEGRATION_CHECKLIST_V0.md`
- `products/delivery/06-architecture/SOFTWARE_FACTORY_WORKER_RESULT_CONTRACT_V0.md`

## Local validation and run commands

```bash
python3 tools/software_factory_file_scope_lock_check.py workspaces/software-factory/dry-runs/2026-05-06-tool-backed-parallel-dispatch-gate/manifests/pre-dispatch-lock-manifest.json
python3 tools/validate_software_factory_orchestration.py workspaces/software-factory/dry-runs/2026-05-06-tool-backed-parallel-dispatch-gate
python3 tools/validate_repo.py --fix
```

## Authority boundary

No credentials/access changes, external sends, deploy, release, merge, persistent agents, destructive cleanup, PXS/PXS CRM mutation, Vega Inquiry Engine intervention, or client/customer data changes.

## Planning implications

The lock checker must pass before dispatch. If it fails, Builders are not dispatched and the result is blocked/issue with the failed lock evidence preserved.
