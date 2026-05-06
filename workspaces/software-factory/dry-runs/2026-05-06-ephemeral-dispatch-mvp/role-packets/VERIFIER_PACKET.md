# Verifier Packet

Status: ready
Factory run ID: `SF-ORCH-2026-05-06-EPHEMERAL-DISPATCH-MVP`
TDE intake: `control/tde-intake/software-factory-ephemeral-dispatch-mvp-2026-05-06.json`
Owning product: Delivery / Software Factory
Owner/reviewer: Peter Eklind / Lyra Operations

## Objective
After integration, independently verify the worker result contract, run folder, validation logs, and final evidence against Phase 3 success criteria.

## Allowed actions
- Read the integrated artifact and run folder.
- Run local validation commands.
- Write only `workspaces/software-factory/dry-runs/2026-05-06-ephemeral-dispatch-mvp/worker-results/VERIFIER_RESULT.md` and validation logs if needed.

## Expected output
- Pass/hold/no-go.
- Tests/validation run.
- Any missing evidence or boundary breach.
