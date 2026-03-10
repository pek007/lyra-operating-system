# Work Order (WO) — TDE Chaining Pilot v1

## Metadata
- WO-ID: WO-2026-TDE-CHAINING-PILOT-V1
- Title: DB-canonical bounded chaining pilot for objective-linked continuation
- Owner: JOB-PROD-001
- Date opened: 2026-03-10
- Lane: Build
- Work type: Feature
- Risk class: High
- Change class: Normal
- Standard class (if Standard): -
- Auto-promotion requested: No
- Exclusion trigger present: Yes

## Intent
- Objective: Prove that the DB-canonical TDE runtime can carry a bounded multi-step objective forward by deterministically promoting successor work to ready state when predecessor work completes, without approval bypass or uncontrolled fan-out.
- Why now: The TDE frontier has already advanced to DB-canonical runtime state, readiness operations, and chaining design/contract authority. The highest-leverage next step toward the vision is no longer more substrate work; it is bounded autonomous continuation on top of the existing governed runtime.
- Non-goals: Generic autonomous task generation, recursive/unbounded chaining, direct-dispatch event bus behavior, approval bypass, broad rollout expansion beyond named pilot workflow families.

## Acceptance Criteria (Required)
1. Canonical DB task state supports bounded chaining metadata for the pilot (`depends_on`, `activation_rule`, objective/stage context, activation provenance) with fail-closed handling for invalid or ambiguous dependency state.
2. The TDE job tick path can deterministically evaluate successor eligibility and promote newly eligible tasks to `ready` in canonical DB state, while preserving idempotency, WIP bounds, and approval-gate behavior.
3. Automated tests and evidence artifacts cover at least: happy path chaining, missing predecessor fail-closed behavior, partial predecessor completion, idempotent re-run, approval-gated successor handling, and WIP-bound enforcement.
4. At least one bounded real pilot workflow family progresses across multiple ticks in DB-canonical mode with explicit activation evidence and no governance break.
5. A closeout packet states whether chaining is proven for bounded continuation, what constraints remain, and whether pilot scope may expand or must remain held.

## Verification Plan (Required)
- Automated tests: Add/extend chaining-specific tests around canonical DB metadata, promotion logic, idempotent re-run behavior, approval-gated successors, and bounded fan-out/WIP controls.
- Manual checks: Confirm pilot tasks exist in canonical DB state, verify successor promotion evidence matches predecessor completion state, and inspect runtime projection/evidence surfaces for clarity and non-ambiguity.
- Security/privacy checks (if applicable): Confirm no approval route is bypassed, no uncontrolled chain fan-out occurs, and rollback/disable path remains explicit.
- Definition of done reference: `STD-001_DEFINITION_OF_DONE.md`

## Dependencies (Required)
- Models/providers involved: None required beyond the current OpenClaw/TDE runtime path
- Tools/services involved: `tools/tde_state_store.py`, `tools/tde_job_tick_runner.py`, canonical DB runtime store/projection surfaces, chaining contract/planning artifacts
- 3PPs touched: None required for the bounded pilot

## Constraints
- Time/budget constraints: Keep the pilot narrow and objective-linked; prefer one real pilot family with strong evidence over broad partial rollout.
- Policy/security constraints: Fail closed on ambiguous predecessor state, unsupported activation rules, approval-gated successor execution, unclear frontier/canonical-store status, or chain-policy bound violations.

## Prompt/Execution Contract
- Prompt template + version: n/a (repo execution work order)
- Assigned executor agent/lane: JOB-PROD-001 / Lyra Build lane
- Escalation trigger(s): Dependency metadata ambiguity; canonical DB state cannot represent required pilot metadata cleanly; activation evidence is non-deterministic; approval boundaries weaken; fan-out cannot be bounded.

## Delivery Plan
- Planned file/components touched: chaining metadata support in canonical DB path; promotion logic in job tick runtime; chaining tests/evidence; pilot closeout packet; relevant operating/product-owner guidance as needed
- Rollback approach: Disable chaining evaluation path and preserve existing DB-canonical scheduled claim behavior; retain metadata/evidence for diagnosis without continuing automatic promotion.
- Expected output artifacts:
  - chaining metadata/runtime implementation changes
  - chaining verification artifacts under `knowledge/evidence/2026-03/`
  - bounded pilot verification note
  - closeout recommendation for expand / hold / rollback

## Closure
- Outcome summary:
- Accepted by:
- Date closed:
- Linked Change Artifact(s):
