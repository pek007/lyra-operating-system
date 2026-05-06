# Software Factory Orchestration Plan

Status: completed / pass
Run ID: `SF-ORCH-2026-05-06-PHASE3B-ISOLATED-PARALLEL-BUILDERS`
Parent TDE intake: `control/tde-intake/software-factory-phase3b-isolated-worktree-parallel-builder-proof-2026-05-06.json`
Owning product/workspace: Delivery / Software Factory / Lyra OS root workspace
Owner/reviewer: Peter Eklind / Lyra Operations
Orchestrator: Lyra
Created: 2026-05-06T14:30:00Z

## 1. Objective
Prove Phase 3b / Phase 4-entry isolation discipline by running two independent Builder workers in separate isolated copies with non-overlapping file scopes, then manually integrating their outputs into root Delivery architecture artifacts and verifying scoped attribution.

## 2. Authority and boundary
This run is authorized only for Delivery-owned Software Factory control artifacts and run-folder evidence. It may use ephemeral subagents and isolated copies. Prohibited authority: no push until final owner-reviewable commit, no merge, no deploy, no release, no credentials or access changes, no external communications, no persistent agents, no PXS/PXS CRM mutation, no Vega Inquiry Engine intervention, and no destructive cleanup.

## 3. Inputs and provenance
| Input | Path | Purpose |
| --- | --- | --- |
| Parent intake | `control/tde-intake/software-factory-phase3b-isolated-worktree-parallel-builder-proof-2026-05-06.json` | Phase 3b owner-approved next control object. |
| Predecessor evidence | `control/execution-evidence/software-factory-ephemeral-dispatch-mvp-2026-05-06.md` | Shows Phase 3 dispatch/result contract proof. |
| Isolation discipline | `products/delivery/04-execution/SOFTWARE_FACTORY_ISOLATED_WORKTREE_DISCIPLINE_V0_2026-05-04.md` | Seven minimum isolation/change-attribution rules. |
| Worker result contract | `products/delivery/06-architecture/SOFTWARE_FACTORY_WORKER_RESULT_CONTRACT_V0.md` | Required worker result shape. |
| Pre-run manifest | `manifests/pre-root-allowed-manifest.json` | Initial root state for the two allowed final artifact paths. |

## 4. Situation analysis
Phase 3 proved ephemeral dispatch and result integration, but not parallel Builder isolation or merge discipline. The lowest-risk next proof is two Builders producing separate Delivery-owned architecture artifacts in separate isolated copies, with a manual Integrator copying only declared outputs into root.

## 5. Work breakdown and TDE task graph
| Task | Role | State | Evidence |
| --- | --- | --- | --- |
| Run orchestration and isolation setup | orchestrator | done | `ORCHESTRATION_PLAN.md`; `manifests/pre-root-allowed-manifest.json` |
| Review isolation design and file-scope split | architect | done | `worker-results/ARCHITECT_RESULT.md` |
| Draft file-scope lock artifact in isolated copy A | builder | done | `worker-results/BUILDER_A_RESULT.md` |
| Draft integration checklist artifact in isolated copy B | builder | done | `worker-results/BUILDER_B_RESULT.md` |
| Check boundary and isolation evidence | gatekeeper | done | `worker-results/GATEKEEPER_RESULT.md` |
| Integrate non-overlapping outputs into root | integrator | done | `worker-results/INTEGRATOR_RESULT.md` |
| Verify attribution, validation, and evidence | verifier | done | `worker-results/VERIFIER_RESULT.md` |

## 6. Role packets
| Role | Packet | Dispatch mode |
| --- | --- | --- |
| orchestrator | `role-packets/ORCHESTRATOR_PACKET.md` | Lyra manual orchestration |
| architect | `role-packets/ARCHITECT_PACKET.md` | ephemeral subagent, read-only |
| builder A | `role-packets/BUILDER_A_PACKET.md` | ephemeral subagent, isolated copy A |
| builder B | `role-packets/BUILDER_B_PACKET.md` | ephemeral subagent, isolated copy B |
| gatekeeper | `role-packets/GATEKEEPER_PACKET.md` | ephemeral subagent, read-only |
| integrator | `role-packets/INTEGRATOR_PACKET.md` | Lyra manual integration |
| verifier | `role-packets/VERIFIER_PACKET.md` | ephemeral subagent after integration |

## 7. Quality, security, and compliance gates
| Gate | Requirement | Evidence |
| --- | --- | --- |
| Requirements/scope | Builder A and B write separate isolated-copy files only; root integration copies only those two declared files. | worker results, manifests, scoped diff |
| Security | No credentials, access, deploy, release, external send, persistent agents, or destructive cleanup. | gatekeeper/verifier results |
| Compliance | No client/private/PXS CRM data touched. | boundary statements |
| Tests | Orchestration validator and repo validation pass. | validation logs |
| Release | No release/deploy; final git push only after successful proof closure. | final evidence |

## 8. Integration plan
Architect reviewed and passed the non-overlap design before integration. Builder A and Builder B ran in isolated-copy scopes and produced separate outputs. Gatekeeper noted a sequencing ambiguity between the original concurrency wording and TDE projection dependencies; the orchestrator resolves it by requiring Architect pass before root integration, while treating concurrent Builder execution as acceptable only because integration waited for Architect, both Builder results, and Gatekeeper review. Integrator copies exactly two generated files from isolated copies into root, records post-root manifest, and dispatches Verifier.

## 9. Time and cost budget
Target under 90 minutes. Two Builder workers plus one Gatekeeper, manual integration, one Verifier. No persistent agents and no product-lane mutation.

## 10. Handoff and acceptance
Exactly one next control object: decide whether Phase 4 should formalize worktree/branch naming and file-scope lock checks as reusable tooling, or hold until Control Panel/TDE renders factory child tasks.

## 11. Final run accounting
Workers used: one Architect, two Builders, one Gatekeeper, one manual Integrator, one independent Verifier.
Child tasks completed: six of six projected tasks done.
Known limitations: copy-mode isolation proves non-overlap and exact-copy attribution but is not yet full git-worktree/branch automation or CI/review feedback routing.
Recommendation: next control object should formalize reusable worktree/branch naming and file-scope lock-check tooling before larger scale-up.
