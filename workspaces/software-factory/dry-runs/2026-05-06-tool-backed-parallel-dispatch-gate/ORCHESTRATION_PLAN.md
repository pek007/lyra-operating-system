# Software Factory Orchestration Plan

Status: completed / pass
Run ID: `SF-ORCH-2026-05-06-TOOL-BACKED-PARALLEL-DISPATCH-GATE`
Parent TDE intake: `control/tde-intake/software-factory-worktree-branch-lock-tooling-2026-05-06.json`
Owning product/workspace: `products/delivery` / `workspaces/software-factory`
Owner/reviewer: Peter Eklind / Lyra Operations
Orchestrator: Lyra / Delivery Software Factory
Created: 2026-05-06 16:58 CEST

## 1. Objective

Use the newly implemented Software Factory file-scope lock checker as a required pre-dispatch gate in a real bounded parallel-builder run. The run will create two small Delivery architecture artifacts in separate isolated copies, then Integrator will adopt only declared outputs into root if the pre-dispatch lock gate, worker evidence, and verification pass.

## 2. Authority and boundary

This run is Delivery-owned internal tooling/procedure work only. It does not authorize credentials, access changes, external communications, persistent agents, deploy, release, push, merge, destructive cleanup, PXS/PXS CRM mutation, Vega Inquiry Engine intervention, or client/customer data changes. Push is allowed only as the final Lyra OS source-control publication step after local validation and owner-approved scope from chat.

## 3. Inputs and provenance

- Predecessor evidence: `control/execution-evidence/software-factory-worktree-branch-lock-tooling-2026-05-06.md`
- Lock checker: `tools/software_factory_file_scope_lock_check.py`
- File-scope lock spec: `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_BUILDER_FILE_SCOPE_LOCK_V0.md`
- Integration checklist: `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_BUILDER_INTEGRATION_CHECKLIST_V0.md`
- Worker result contract: `products/delivery/06-architecture/SOFTWARE_FACTORY_WORKER_RESULT_CONTRACT_V0.md`

## 4. Situation analysis

Phase 3b proved isolated-copy parallel builders and exact-copy integration. The follow-up tooling cycle implemented the lock checker and expected-fail fixtures. This run is the first operational use of that checker as a pre-dispatch gate rather than only a standalone tool validation.

## 5. Work breakdown and TDE task graph

| Task | Role | State | Evidence target |
| --- | --- | --- | --- |
| Prepare tool-backed run packet and lock manifest | orchestrator | done | `ORCHESTRATION_PLAN.md` |
| Review lock-manifest dispatch boundary | architect | done | `worker-results/ARCHITECT_RESULT.md` |
| Draft parallel dispatch packet template in isolated copy A | builder | done | `worker-results/BUILDER_A_RESULT.md` |
| Draft lock-gate runbook in isolated copy B | builder | done | `worker-results/BUILDER_B_RESULT.md` |
| Check lock gate and boundary evidence | gatekeeper | done | `worker-results/GATEKEEPER_RESULT.md` |
| Adopt exactly two outputs into root | integrator | done | `worker-results/INTEGRATOR_RESULT.md` |
| Verify lock-gate use, attribution, and validation | verifier | done | `worker-results/VERIFIER_RESULT.md` |

## 6. Role packets

| Role | Packet | Purpose |
| --- | --- | --- |
| Orchestrator | `role-packets/ORCHESTRATOR_PACKET.md` | Maintain run boundary and state |
| Architect | `role-packets/ARCHITECT_PACKET.md` | Review lock-manifest and target split |
| Builder | `role-packets/BUILDER_PACKET.md` | Generic builder dispatch contract |
| Builder A | `role-packets/BUILDER_A_PACKET.md` | Produce dispatch packet template |
| Builder B | `role-packets/BUILDER_B_PACKET.md` | Produce lock-gate runbook |
| Gatekeeper | `role-packets/GATEKEEPER_PACKET.md` | Check fail-closed gate use and prohibited actions |
| Integrator | `role-packets/INTEGRATOR_PACKET.md` | Exact-copy root adoption |
| Verifier | `role-packets/VERIFIER_PACKET.md` | Final independent verification |

## 7. Quality, security, and compliance gates

| Gate | Required disposition |
| --- | --- |
| Requirements/scope | Lock manifest passes before Builder dispatch and root adoption remains exactly two artifacts |
| Security | No credentials/access changes, external communications, deploy, release, persistent agents, or destructive cleanup |
| Compliance | Internal Delivery docs only; no client/customer data and no public/external sends |
| Tests | `tools/software_factory_file_scope_lock_check.py` and orchestration validator must pass |
| Release | No deploy/release; final git push only after validation if closure-clean |

## 8. Integration plan

1. Run `python3 tools/software_factory_file_scope_lock_check.py workspaces/software-factory/dry-runs/2026-05-06-tool-backed-parallel-dispatch-gate/manifests/pre-dispatch-lock-manifest.json` before Builder dispatch.
2. Dispatch Builder A and Builder B only if the pre-dispatch lock gate passes.
3. Keep Builder outputs in isolated copies.
4. Integrator exact-copies only the two declared artifacts into root after Architect, Builders, and Gatekeeper complete.
5. Record post-root manifest and scoped hash comparison.
6. Verifier confirms pre-dispatch gate evidence, non-overlap, exact-copy attribution, and final validation.

## 9. Time and cost budget

Bounded same-day internal proof. Prefer small artifacts, one pre-dispatch lock manifest, two isolated Builder outputs, one Integrator pass, one Verifier pass. Stop on any overlap, missing evidence, or prohibited authority request.

## 10. Handoff and acceptance

Acceptance requires: pre-dispatch lock checker pass, two non-overlapping Builder outputs, exact-copy root adoption, independent verification pass, orchestration validation pass, and evidence closure. Exactly one next control object: decide whether to add automatic worktree creation after this tool-backed run passes.

## 11. Final run accounting

Workers used: Architect, two Builders, Gatekeeper, manual Integrator, independent Verifier.
Child tasks completed: seven of seven projected tasks done.
Known limitations: this uses isolated-copy paths and lock-manifest validation; it still does not automatically create git worktrees or branches.
Recommendation: next control object should decide whether to add automatic worktree creation after this tool-backed run passed end-to-end.
