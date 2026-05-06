# Builder Packet

Status: ready
Factory run ID: `SF-ORCH-2026-05-06-EPHEMERAL-DISPATCH-MVP`
TDE intake: `control/tde-intake/software-factory-ephemeral-dispatch-mvp-2026-05-06.json`
Quality gate matrix: `products/delivery/06-architecture/SOFTWARE_FACTORY_PROFESSIONAL_QUALITY_GATE_MATRIX_V0.yaml`
Owning product: Delivery / Software Factory
Owner/reviewer: Peter Eklind / Lyra Operations
GO/HOLD/NO-GO: GO for narrow draft-only Builder work

## Objective
Draft the Software Factory Worker Result Contract v0 so future ephemeral workers return integration-ready summaries.

## Target repo/worktree
- Root workspace: `/Users/lyra/.openclaw/workspace`
- Draft output path: `workspaces/software-factory/dry-runs/2026-05-06-ephemeral-dispatch-mvp/drafts/SOFTWARE_FACTORY_WORKER_RESULT_CONTRACT_V0_DRAFT.md`

## Allowed paths
- `workspaces/software-factory/dry-runs/2026-05-06-ephemeral-dispatch-mvp/drafts/SOFTWARE_FACTORY_WORKER_RESULT_CONTRACT_V0_DRAFT.md`
- `workspaces/software-factory/dry-runs/2026-05-06-ephemeral-dispatch-mvp/worker-results/BUILDER_RESULT.md`

## Prohibited paths/actions
- Do not change credentials or access settings.
- Do not push, merge, release, or deploy.
- Do not create persistent agents.
- Do not modify PXS, PXS CRM, Vega Inquiry Engine, client data, or external communications.
- Do not perform destructive cleanup.

## Non-goals
- No runtime dispatcher implementation.
- No Control Panel UI changes.
- No TDE kernel schema changes.
- No release or deployment lane.

## Professional quality gates
- Contract is concise and operational, not conceptual prose only.
- Contract includes required fields, output format, evidence expectations, blocker semantics, and integration state recommendation.
- Contract preserves human authority boundaries.
- Contract can be used by Architect, Builder, Verifier, Gatekeeper, and Integrator workers.

## Validation commands
```bash
python3 tools/validate_software_factory_orchestration.py workspaces/software-factory/dry-runs/2026-05-06-ephemeral-dispatch-mvp
```

## Expected Builder output
- Replace the draft contract file with a complete v0 draft.
- Replace `worker-results/BUILDER_RESULT.md` with changed files, rationale, validation, blockers, and recommended next state.

## Evidence target
- Final evidence will be written to `control/execution-evidence/software-factory-ephemeral-dispatch-mvp-2026-05-06.md` by the integrator.

## Rollback / abort
Rollback path: discard the draft file and retain the worker result explaining why.
Abort if: the work requires credentials, push, merge, release, deploy, persistent agents, PXS/PXS CRM mutation, external communications, or paths outside the allowed draft/result files.
