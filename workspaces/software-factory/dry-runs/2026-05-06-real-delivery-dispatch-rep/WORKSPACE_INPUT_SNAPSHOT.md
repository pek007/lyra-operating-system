# Software Factory Workspace Input Snapshot

Status: ready / scoped
Snapshot ID: `SF-SNAPSHOT-2026-05-06-REAL-DELIVERY-DISPATCH-REP`
Factory run ID: `SF-ORCH-2026-05-06-REAL-DELIVERY-DISPATCH-REP`
Target workspace: `/Users/lyra/.openclaw/workspace`
Target product/repo: `products/delivery` / Lyra OS root repository
Captured by: Lyra / Delivery Software Factory
Captured at: 2026-05-06 17:11 CEST

## Workspace operating-package check

Readiness disposition: ready for bounded Delivery-owned operational rep. Process discovery routes this work through Delivery / task execution controls and TDE evidence discipline.

## Product/domain inputs

- `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_DISPATCH_PACKET_TEMPLATE_V0.md`
- `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_DISPATCH_GATE_RUNBOOK_V0.md`
- `products/delivery/06-architecture/SOFTWARE_FACTORY_WORKER_RESULT_CONTRACT_V0.md`
- `tools/software_factory_file_scope_lock_check.py`

## Local validation and run commands

```bash
python3 tools/software_factory_file_scope_lock_check.py workspaces/software-factory/dry-runs/2026-05-06-real-delivery-dispatch-rep/manifests/pre-dispatch-lock-manifest.json
python3 tools/validate_software_factory_orchestration.py workspaces/software-factory/dry-runs/2026-05-06-real-delivery-dispatch-rep
python3 tools/validate_repo.py --fix
```

## Authority boundary

No credentials/access changes, external sends, deploy, release, merge, persistent agents, destructive cleanup, PXS/PXS CRM mutation, Vega Inquiry Engine intervention, or client/customer data changes.

## Planning implications

This run should capture whether manual isolated-copy discipline is tolerable after one more real use. Do not add worktree automation inside this run.
