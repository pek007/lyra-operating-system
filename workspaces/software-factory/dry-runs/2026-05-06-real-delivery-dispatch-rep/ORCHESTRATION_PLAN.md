# Software Factory Orchestration Plan

Status: completed / pass
Run ID: `SF-ORCH-2026-05-06-REAL-DELIVERY-DISPATCH-REP`
Parent TDE intake: `control/tde-intake/software-factory-real-delivery-dispatch-rep-2026-05-06.json`
Owning product/workspace: `products/delivery` / `workspaces/software-factory`
Owner/reviewer: Peter Eklind / Lyra Operations
Orchestrator: Lyra / Delivery Software Factory
Created: 2026-05-06 17:11 CEST

## 1. Objective

Run one additional real Delivery-owned tool-backed parallel dispatch rep before adding automatic git worktree creation. The run uses the file-scope lock checker as a required pre-dispatch gate and produces two useful Delivery operating artifacts: a parallel-dispatch readiness checklist and a dispatch friction log template.

## 2. Authority and boundary

This is internal Delivery operating-model/tooling work only. It does not authorize credentials, access changes, external communications, persistent agents, deploy, release, push, merge, destructive cleanup, PXS/PXS CRM mutation, Vega Inquiry Engine intervention, or client/customer data changes. Push is allowed only as final source-control publication after validation within the approved Lyra OS scope.

## 3. Inputs and provenance

- Peter-approved recommendation: hold automatic worktree creation until one more real dispatch rep.
- Predecessor evidence: `control/execution-evidence/software-factory-tool-backed-parallel-dispatch-gate-2026-05-06.md`
- Lock checker: `tools/software_factory_file_scope_lock_check.py`
- Dispatch template: `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_DISPATCH_PACKET_TEMPLATE_V0.md`
- Gate runbook: `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_DISPATCH_GATE_RUNBOOK_V0.md`
- Worker result contract: `products/delivery/06-architecture/SOFTWARE_FACTORY_WORKER_RESULT_CONTRACT_V0.md`

## 4. Situation analysis

The prior run proved the lock checker can gate parallel dispatch end-to-end. The remaining question is whether the manual isolated-copy step is real friction or acceptable discipline. This run produces artifacts that will make future runs easier while capturing friction evidence for the automation decision.

## 5. Work breakdown and TDE task graph

| Task | Role | State | Evidence target |
| --- | --- | --- | --- |
| Prepare real-rep run packet and lock manifest | orchestrator | done | `ORCHESTRATION_PLAN.md` |
| Review real-rep dispatch boundary | architect | done | `worker-results/ARCHITECT_RESULT.md` |
| Draft parallel dispatch readiness checklist | builder | done | `worker-results/BUILDER_A_RESULT.md` |
| Draft parallel dispatch friction log template | builder | done | `worker-results/BUILDER_B_RESULT.md` |
| Check lock-gate and automation-hold boundary | gatekeeper | done | `worker-results/GATEKEEPER_RESULT.md` |
| Adopt exactly two outputs into root | integrator | done | `worker-results/INTEGRATOR_RESULT.md` |
| Verify lock-gate use, attribution, friction capture, and validation | verifier | done | `worker-results/VERIFIER_RESULT.md` |

## 6. Role packets

| Role | Packet | Purpose |
| --- | --- | --- |
| Orchestrator | `role-packets/ORCHESTRATOR_PACKET.md` | Maintain run boundary and state |
| Architect | `role-packets/ARCHITECT_PACKET.md` | Review target split and no-automation decision boundary |
| Builder | `role-packets/BUILDER_PACKET.md` | Generic builder dispatch contract |
| Builder A | `role-packets/BUILDER_A_PACKET.md` | Produce readiness checklist |
| Builder B | `role-packets/BUILDER_B_PACKET.md` | Produce friction log template |
| Gatekeeper | `role-packets/GATEKEEPER_PACKET.md` | Confirm lock gate, hold-automation boundary, and prohibited actions |
| Integrator | `role-packets/INTEGRATOR_PACKET.md` | Exact-copy root adoption |
| Verifier | `role-packets/VERIFIER_PACKET.md` | Final independent verification |

## 7. Quality, security, and compliance gates

| Gate | Required disposition |
| --- | --- |
| Requirements/scope | Lock manifest passes before Builder dispatch; artifacts are useful Delivery operating surfaces |
| Security | No credentials/access changes, external communications, deploy, release, persistent agents, or destructive cleanup |
| Compliance | Internal Delivery docs only; no client/customer data and no public/external sends |
| Tests | File-scope lock checker, orchestration validator, TDE cockpit, and repo validation must pass |
| Release | No deploy/release; final git push only after validation if closure-clean |

## 8. Integration plan

1. Run `python3 tools/software_factory_file_scope_lock_check.py workspaces/software-factory/dry-runs/2026-05-06-real-delivery-dispatch-rep/manifests/pre-dispatch-lock-manifest.json` before Builder dispatch.
2. Dispatch Builder A and Builder B only if the pre-dispatch lock gate passes.
3. Keep Builder outputs in isolated copies.
4. Integrator exact-copies only the two declared artifacts into root after Architect, Builders, and Gatekeeper complete.
5. Record post-root manifest and scoped hash comparison.
6. Verifier confirms lock-gate evidence, friction-capture value, non-overlap, exact-copy attribution, and validation.

## 9. Time and cost budget

Bounded same-day internal rep. Keep artifacts small and operational. Stop on overlap, missing evidence, automation pressure, or prohibited authority request.

## 10. Handoff and acceptance

Acceptance requires: pre-dispatch lock checker pass, two useful Delivery artifacts, non-overlapping Builder outputs, exact-copy root adoption, independent verification pass, orchestration validation pass, repo/TDE validation pass, and evidence closure. Exactly one next control object: decide from captured friction whether automatic worktree creation remains held or moves to a small helper design.

## 11. Final run accounting

Workers used: Architect, two Builders, Gatekeeper, manual Integrator, independent Verifier.
Child tasks completed: seven of seven projected tasks done.
Known limitations: this intentionally does not automate git worktree or branch creation.
Recommendation: keep worktree automation held until the new friction log captures evidence from the next real parallel dispatch.
