# Software Factory Tool-Backed Parallel Dispatch Gate Evidence

Status: completed / pass
Date: 2026-05-06
Run ID: `SF-ORCH-2026-05-06-TOOL-BACKED-PARALLEL-DISPATCH-GATE`
Run folder: `workspaces/software-factory/dry-runs/2026-05-06-tool-backed-parallel-dispatch-gate/`
Parent intake: `control/tde-intake/software-factory-worktree-branch-lock-tooling-2026-05-06.json`

## Objective
Use `tools/software_factory_file_scope_lock_check.py` as an operational pre-dispatch gate in a bounded parallel-builder run, then integrate only declared outputs after clean worker evidence.

## Boundary
No persistent agents, PXS/PXS CRM mutation, deploy/release, credential/access changes, external sends, destructive cleanup, broad repository status sweep, Vega Inquiry Engine intervention, or client/customer data changes.

## Dispatch and integration results
| Role | Result | Evidence |
| --- | --- | --- |
| Architect | pass | `worker-results/ARCHITECT_RESULT.md` |
| Builder A | pass | `worker-results/BUILDER_A_RESULT.md` |
| Builder B | pass | `worker-results/BUILDER_B_RESULT.md` |
| Gatekeeper | pass | `worker-results/GATEKEEPER_RESULT.md` |
| Integrator | pass | `worker-results/INTEGRATOR_RESULT.md` |
| Verifier | pass | `worker-results/VERIFIER_RESULT.md` |

## Lock-gate evidence
- Pre-dispatch lock check: `logs/pre-dispatch-lock-check.log` — pass.
- Gatekeeper caveat: initial pre-dispatch log lacked embedded timestamp.
- Mitigation before root adoption: `logs/pre-integration-lock-check-timestamped.log` — timestamped pass.

## Root artifacts adopted
- `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_DISPATCH_PACKET_TEMPLATE_V0.md` from Builder A isolated copy.
- `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_DISPATCH_GATE_RUNBOOK_V0.md` from Builder B isolated copy.

## Attribution evidence
- Pre-dispatch manifest: `manifests/pre-dispatch-lock-manifest.json`.
- Post-root manifest: `manifests/post-root-allowed-manifest.json`.
- Scoped hash comparison: `SCOPED_DIFF.md`.

## Validation
- `python3 tools/validate_software_factory_orchestration.py workspaces/software-factory/dry-runs/2026-05-06-tool-backed-parallel-dispatch-gate` — pass after integration (`logs/orchestration-validation-after-integration.log`).
- Independent Verifier reran orchestration validation — pass (`logs/verifier-orchestration-validation.log`).
- Independent Verifier reran file-scope lock checker — pass (`logs/verifier-pre-dispatch-lock-check.log`).
- Independent Verifier recomputed post-root root/source hashes — pass (`logs/verifier-post-root-hash-check.log`).

## Verifier closure
Verifier confirmed:
- the file-scope lock checker was used as a required pre-dispatch gate;
- the timestamp caveat was mitigated before root adoption with `logs/pre-integration-lock-check-timestamped.log`;
- Builder A/B scopes are non-overlapping;
- root artifacts match isolated-copy sources by sha256/bytes;
- adoption evidence declares exactly the two intended root artifacts; and
- both required validation commands pass.

## Result
Completed / pass for the tool-backed parallel dispatch gate run.

What was proven:
- a file-scope lock manifest can be used as a required pre-dispatch gate;
- Architect, Builder, Gatekeeper, Integrator, and Verifier can consume the same lock-gate evidence;
- non-overlapping isolated-copy Builder outputs can be exact-copy adopted into root;
- a timestamp/evidence caveat can be caught by Gatekeeper and mitigated before root adoption; and
- independent Verifier can confirm lock-gate use, attribution, and validation.

What was not proven:
- automatic git worktree creation;
- automatic branch creation;
- CI/review feedback routing;
- deploy/release lanes;
- PXS/PXS CRM mutation.

## Exactly one next control object
Decide whether to add automatic worktree creation after this end-to-end tool-backed gate pass.
