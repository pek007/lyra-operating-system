# Software Factory Workspace Input Snapshot

Status: captured
Snapshot ID: `SF-SNAPSHOT-2026-05-06-PHASE3B-ISOLATED-PARALLEL-BUILDERS`
Factory run ID: `SF-ORCH-2026-05-06-PHASE3B-ISOLATED-PARALLEL-BUILDERS`
Target workspace: `/Users/lyra/.openclaw/workspace`
Target product/repo: `products/delivery/` and `workspaces/software-factory/`
Captured by: Lyra
Captured at: 2026-05-06T14:30:00Z

## Workspace operating-package check
- Root workspace `AGENTS.md` and `PROCESS_DISCOVERY_INDEX.md` exist.
- Delivery and Software Factory artifacts provide the owning process and gates.
- Readiness disposition: ready for bounded copy-mode isolated parallel-builder proof.

## Product/domain inputs
| Source | Disposition |
| --- | --- |
| `control/execution-evidence/software-factory-ephemeral-dispatch-mvp-2026-05-06.md` | Phase 3 predecessor proof. |
| `products/delivery/04-execution/SOFTWARE_FACTORY_ISOLATED_WORKTREE_DISCIPLINE_V0_2026-05-04.md` | Isolation/change-attribution rules. |
| `products/delivery/06-architecture/SOFTWARE_FACTORY_WORKER_RESULT_CONTRACT_V0.md` | Worker result contract. |

## Local validation and run commands
```bash
python3 tools/validate_software_factory_orchestration.py workspaces/software-factory/dry-runs/2026-05-06-phase3b-isolated-worktree-parallel-builder-proof
python3 tools/validate_repo.py --fix
```

## Authority boundary
Allowed: run-folder evidence, isolated copy artifacts, final root Delivery architecture artifacts for the two declared files, final evidence. Prohibited: credentials, access changes, external communications, deploy, release, merge, persistent agents, destructive cleanup, PXS/PXS CRM mutation, and Vega Inquiry Engine interference.

## Planning implications
Use copy-mode isolation with two non-overlapping file scopes. Treat this as proof of isolation and integration discipline, not as approval for persistent agents or production release lanes.
