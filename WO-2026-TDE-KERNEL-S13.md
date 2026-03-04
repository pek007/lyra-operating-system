# Work Order (WO) — TDE Kernel Slice S13

## Metadata
- WO-ID: WO-2026-TDE-KERNEL-S13
- Title: Job-tick runtime semantics (operational contract + first isolated job runner)
- Owner: JOB-PROD-001
- Date opened: 2026-03-03
- Lane: Build
- Work type: Feature
- Risk class: Medium

## Intent
- Objective: Make jobs operational at runtime by defining and implementing a deterministic job-tick loop that claims and progresses job-scoped work via isolated cron execution.
- Why now: Jobs are well-defined at policy/spec level, but execution remains opportunistic without a consistent pull-and-claim loop bound to job identity and authority context.
- Non-goals: Full multi-job orchestration rollout, broad external side-effect automation, Trello cutover completion, policy gate relaxation.

## Scope
1. Define a first-class job-tick contract (inputs/outputs, claim semantics, authority metadata, evidence emissions).
2. Implement one isolated cron-driven job runner for a selected active job.
3. Enforce bounded WIP claim/progress behavior in the runner loop.
4. Emit deterministic run-cycle artifacts for observability and audit.

## Acceptance Criteria
1. A formal job-tick contract artifact exists and is linked to existing TDE runtime trigger semantics.
2. At least one isolated cron job runner executes the job-tick loop with internal/no-noise delivery defaults.
3. For ready job-scoped work, at least one item is claimed and progressed without manual prompt in one tick interval.
4. Runner emits cycle evidence including: `job_id`, `binding_id` (or explicit binding status), claimed item IDs, idempotency references, and decision/evidence outputs.
5. Fail-closed behavior is preserved when required authority metadata is missing/invalid.

## Planned Change Artifacts
- `os/sops/TDE_JOB_TICK_CONTRACT_V1.md` (new)
- `tools/tde_job_tick_runner.py` (new) or equivalent extension in existing canary runtime tooling
- Cron wiring/config artifact for isolated job runner execution
- `knowledge/evidence/2026-03/2026-03-03__verification__wo-2026-tde-kernel-s13.md`

## Closure
- Outcome summary: _Pending_
- Accepted by: _Pending_
- Date closed: _Pending_
- Linked Change Artifact(s): _Pending_
