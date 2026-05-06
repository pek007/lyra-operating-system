# Software Factory Workspace Input Snapshot

Status: captured
Snapshot ID: `SF-SNAPSHOT-2026-05-06-EPHEMERAL-DISPATCH-MVP`
Factory run ID: `SF-ORCH-2026-05-06-EPHEMERAL-DISPATCH-MVP`
Target workspace: `/Users/lyra/.openclaw/workspace`
Target product/repo: `products/delivery/` and `workspaces/software-factory/`
Captured by: Lyra
Captured at: 2026-05-06T14:00:00Z

## Workspace operating-package check
- Root workspace `AGENTS.md` exists and identifies TDE as execution system of record.
- `PROCESS_DISCOVERY_INDEX.md` exists and routes delivery work to Delivery product artifacts and project routing.
- Readiness disposition: ready for bounded Delivery-owned factory-control mutation.

## Product/domain inputs
| Source | Disposition |
| --- | --- |
| `products/delivery/04-execution/SOFTWARE_FACTORY_ORCHESTRATION_LAYER_PLAN_2026-04-28.md` | Phase 3 dispatch MVP is the active next step. |
| `products/delivery/06-architecture/SOFTWARE_FACTORY_TDE_ORCHESTRATION_CONTRACT_V0.md` | Requires parent/child evidence discipline. |
| `products/delivery/04-execution/SOFTWARE_FACTORY_ISOLATED_WORKTREE_DISCIPLINE_V0_2026-05-04.md` | Supports low-risk scoped mutation with explicit boundaries. |

## Local validation and run commands
```bash
python3 tools/validate_software_factory_orchestration.py workspaces/software-factory/dry-runs/2026-05-06-ephemeral-dispatch-mvp
python3 tools/validate_repo.py --fix
```

## Authority boundary
Allowed: create/update the run folder, dispatch ephemeral subagents, integrate a Delivery-owned worker result contract artifact, and write final evidence. Prohibited: credentials, access changes, external communications, deploy, release, push, merge, persistent agents, destructive cleanup, PXS/PXS CRM mutation, and Vega Inquiry Engine interference.

## Planning implications
Use the lowest-complexity orchestration pattern that proves Phase 3: concurrent read-only Architect/Gatekeeper plus narrow Builder, followed by manual integration and independent Verifier.
