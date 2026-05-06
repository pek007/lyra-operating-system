# Software Factory Phase 3b Isolated Worktree/Copy Parallel-Builder Proof Evidence

Status: completed / pass
Date: 2026-05-06
Run ID: `SF-ORCH-2026-05-06-PHASE3B-ISOLATED-PARALLEL-BUILDERS`
Run folder: `workspaces/software-factory/dry-runs/2026-05-06-phase3b-isolated-worktree-parallel-builder-proof/`
Parent intake: `control/tde-intake/software-factory-phase3b-isolated-worktree-parallel-builder-proof-2026-05-06.json`

## Objective
Prove two independent Builders can work in isolated copies with non-overlapping scopes and that the Integrator can adopt only declared outputs into root with scoped attribution.

## Boundary
No credentials/access changes, external sends, deploy, release, merge, persistent agents, destructive cleanup, PXS/PXS CRM mutation, Vega Inquiry Engine intervention, or client data changes.

## Dispatch and integration results
| Role | Result | Evidence |
| --- | --- | --- |
| Architect | pass | `worker-results/ARCHITECT_RESULT.md` |
| Builder A | pass | `worker-results/BUILDER_A_RESULT.md` |
| Builder B | pass | `worker-results/BUILDER_B_RESULT.md` |
| Gatekeeper | issue / hold before integration | `worker-results/GATEKEEPER_RESULT.md` |
| Integrator | pass | `worker-results/INTEGRATOR_RESULT.md` |
| Verifier | pass | `worker-results/VERIFIER_RESULT.md` |

## Gatekeeper hold resolution
Gatekeeper found no no-go, but held integration until Architect/Builder evidence was complete and sequencing ambiguity was resolved. Orchestrator resolution: root integration waited for Architect pass, Builder A/B completion, and Gatekeeper review. The initial concurrent Builder dispatch is accepted for this proof because the final integration gate enforced the TDE dependency before root adoption.

## Root artifacts adopted
- `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_BUILDER_FILE_SCOPE_LOCK_V0.md` from Builder A isolated copy.
- `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_BUILDER_INTEGRATION_CHECKLIST_V0.md` from Builder B isolated copy.

## Attribution evidence
- Pre-root manifest: `manifests/pre-root-allowed-manifest.json`.
- Post-root manifest: `manifests/post-root-allowed-manifest.json`.
- Scoped diff/hash comparison: `SCOPED_DIFF.md`.

## Validation
- `python3 tools/validate_software_factory_orchestration.py workspaces/software-factory/dry-runs/2026-05-06-phase3b-isolated-worktree-parallel-builder-proof` — pass after integration (`logs/orchestration-validation-after-integration.log`).
- Independent Verifier reran the same orchestration validator — pass (`logs/orchestration-validation-verifier.log`).

## Verifier closure
Verifier confirmed:
- Builder A/B scopes are non-overlapping by exact path and isolated-copy prefix.
- Gatekeeper HOLD was adequately resolved before root adoption: integration waited for Architect pass, Builder A/B completion, and Gatekeeper review.
- The two root artifacts match their isolated-copy sources by sha256/bytes and align with `SCOPED_DIFF.md` and `manifests/post-root-allowed-manifest.json`.
- Only the two declared root Delivery architecture artifacts were adopted from Builder outputs.

## Result
Completed / pass for Phase 3b isolated-copy parallel-builder proof.

What was proven:
- two Builders can operate in separate isolated copies;
- their write scopes can be checked as non-overlapping;
- root adoption can wait for Architect/Gatekeeper/Builder evidence even if Builders were dispatched concurrently;
- exact-copy integration can be verified by post-root manifest and sha256 comparison;
- independent Verifier can confirm attribution and validation.

What was not proven:
- full git worktree/branch automation;
- automated lock checking tooling;
- CI/review feedback routing;
- persistent agents;
- deploy/release lanes;
- PXS/PXS CRM mutation.

## Exactly one next control object
If verifier passes: decide whether to formalize reusable worktree/branch naming and file-scope lock-check tooling, or hold until Control Panel/TDE renders factory child tasks.
