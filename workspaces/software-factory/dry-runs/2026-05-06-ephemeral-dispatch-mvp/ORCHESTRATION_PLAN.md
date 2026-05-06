# Software Factory Orchestration Plan

Status: completed / pass
Run ID: `SF-ORCH-2026-05-06-EPHEMERAL-DISPATCH-MVP`
Parent TDE intake: `control/tde-intake/software-factory-ephemeral-dispatch-mvp-2026-05-06.json`
Owning product/workspace: Delivery / Software Factory / Lyra OS root workspace
Owner/reviewer: Peter Eklind / Lyra Operations
Orchestrator: Lyra
Created: 2026-05-06T14:00:00Z

## 1. Objective
Prove Phase 3 of the Software Factory orchestration layer by dispatching bounded ephemeral role agents from this run packet, collecting their result summaries, manually integrating one low-risk Delivery-owned control artifact, and producing owner-reviewable evidence.

The concrete control artifact target is `products/delivery/06-architecture/SOFTWARE_FACTORY_WORKER_RESULT_CONTRACT_V0.md`, which defines the minimum result shape for future Software Factory workers.

## 2. Authority and boundary
This run may create and update only the declared run folder, the Delivery-owned worker result contract artifact, and the final evidence note. It may use ephemeral OpenClaw subagents only.

Prohibited authority: no push, no merge, no deploy, no release, no credentials or access changes, no external communications, no persistent agents, no PXS/PXS CRM mutation, no Vega Inquiry Engine thread intervention, and no destructive cleanup.

## 3. Inputs and provenance
| Input | Path | Purpose |
| --- | --- | --- |
| Owner approval | Lyra Operations message 6233 | Peter approved doing the Phase 3 dispatch MVP. |
| Orchestration plan | `products/delivery/04-execution/SOFTWARE_FACTORY_ORCHESTRATION_LAYER_PLAN_2026-04-28.md` | Phase 3 target and success criteria. |
| TDE contract | `products/delivery/06-architecture/SOFTWARE_FACTORY_TDE_ORCHESTRATION_CONTRACT_V0.md` | Parent/child and evidence discipline. |
| Isolation discipline | `products/delivery/04-execution/SOFTWARE_FACTORY_ISOLATED_WORKTREE_DISCIPLINE_V0_2026-05-04.md` | Boundary and attribution discipline. |
| Prior proof | `control/execution-evidence/software-factory-control-panel-owner-reviewed-scoped-mutation-proof-2026-05-05-2016-cest.md` | Passed owner-reviewed scoped mutation proof. |

## 4. Situation analysis
The factory has proven plan-before-code, validation, isolated-copy attribution, and one owner-reviewed scoped mutation. The next bottleneck is proving that orchestration can dispatch bounded role workers, collect structured results, and integrate without noisy status spam, persistent agents, or uncontrolled authority.

A worker result contract is the smallest Delivery-owned artifact that directly supports Phase 3. It improves future dispatch reliability while avoiding PXS/Vega product mutation.

## 5. Work breakdown and TDE task graph
| Task | Role | State | Evidence |
| --- | --- | --- | --- |
| Confirm run design and result contract needs | architect | done | `worker-results/ARCHITECT_RESULT.md` |
| Draft worker result contract | builder | done | `worker-results/BUILDER_RESULT.md` |
| Check authority/security/compliance boundaries | gatekeeper | done | `worker-results/GATEKEEPER_RESULT.md` |
| Verify integrated artifact and run evidence | verifier | done | `worker-results/VERIFIER_RESULT.md` |
| Integrate worker outputs and close evidence | integrator | done | `worker-results/INTEGRATOR_RESULT.md` |

## 6. Role packets
| Role | Packet | Dispatch mode |
| --- | --- | --- |
| orchestrator | `role-packets/ORCHESTRATOR_PACKET.md` | Lyra manual orchestration |
| architect | `role-packets/ARCHITECT_PACKET.md` | ephemeral subagent, read-only |
| builder | `role-packets/BUILDER_PACKET.md` | ephemeral subagent, narrow draft write scope |
| gatekeeper | `role-packets/GATEKEEPER_PACKET.md` | ephemeral subagent, read-only |
| verifier | `role-packets/VERIFIER_PACKET.md` | ephemeral subagent after integration |
| integrator | `role-packets/INTEGRATOR_PACKET.md` | Lyra manual integration |

## 7. Quality, security, and compliance gates
| Gate | Requirement | Planned evidence |
| --- | --- | --- |
| Requirements/scope | Only declared Delivery/factory-control paths may change. | scoped git diff and worker results |
| Security | No credentials, access, deployment, external send, or persistent agent action. | gatekeeper result |
| Compliance | No client/private/PXS CRM data mutation or export. | gatekeeper result |
| Tests | Orchestration validator and repo validator pass. | validation logs |
| Release | No push, merge, deploy, release, or production adoption authority. | final evidence boundary statement |

## 8. Integration plan
Architect, Builder, and Gatekeeper may run concurrently because their write scopes do not conflict: Architect and Gatekeeper are read-only; Builder writes only the draft contract and its result file. Lyra integrates their outputs into the root Delivery contract artifact, then dispatches Verifier for independent review. If any role reports a blocker, stop and record the blocker instead of expanding scope.

## 9. Time and cost budget
Target under 90 minutes. Use three ephemeral workers plus manual integration and one verifier. No persistent agents, no ACP harnesses, no parallel builders, and no external services beyond existing local tooling.

## 10. Handoff and acceptance
Exactly one next control object: decide whether Phase 3 should proceed to a second dispatch proof with two independent builders in isolated worktrees, or hold until Control Panel/TDE rendering of child factory tasks is improved.

## 11. Final run accounting
Workers used: three initial ephemeral workers completed (Architect, Builder, Gatekeeper), one manual Integrator completed, one independent Verifier completed and rechecked after closure fixes.
Child tasks completed: six of six projected tasks done.
Known limitations: this MVP proves result collection and manual integration, not multi-builder worktree merge discipline, persistent agents, CI feedback routing, release lanes, or PXS/PXS CRM mutation.
Recommendation: create the next control object for Phase 3b isolated-worktree parallel-builder proof, with no persistent agents or PXS/PXS CRM mutation until separately approved.
