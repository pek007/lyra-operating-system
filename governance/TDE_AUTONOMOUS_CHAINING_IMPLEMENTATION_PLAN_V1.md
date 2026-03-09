# TDE Autonomous Chaining Implementation Plan v1

Status: Draft
Owner: Lyra
Date: 2026-03-09
Depends on: `governance/TDE_AUTONOMOUS_CHAINING_DESIGN_NOTE_V1.md`

## Purpose
Translate the autonomous chaining design note into an executable implementation path.

This plan is focused on the recommended near-term target:
**dependency-aware state-driven chaining** on top of the current cron/job-tick architecture.

## Target outcome
Enable TDE to continue moving toward a high-level objective with minimal human intervention by allowing completion of one task to make successor work ready automatically, while preserving:
- bounded execution,
- explicit authority,
- auditability,
- deterministic behavior,
- fail-closed governance.

## Scope decision
### In scope for v1
- dependency-aware readiness promotion
- predecessor/successor metadata model
- deterministic promotion during scheduled ticks
- activation evidence artifacts
- bounded chain progression
- rollout via controlled pilot and verification gates

### Explicitly out of scope for v1
- generic autonomous task generation
- immediate direct-dispatch event bus
- unrestricted recursive task chaining
- autonomous approval bypass for blocked successor routes

## Operating model after implementation
The intended v1 chain model is:

1. Product Owner defines a high-level target and decomposes it into staged tasks.
2. Tasks carry dependency metadata.
3. A scheduled TDE tick runs.
4. If a predecessor has completed, TDE evaluates dependent tasks.
5. Newly eligible tasks are promoted to `ready`.
6. The same or subsequent tick claims the next ready item subject to WIP bounds.
7. Progress continues without human prompting unless an approval or exception gate is hit.

## Delivery phases

## Phase 0 — Design freeze and contract authority
Purpose: lock the core behavior before coding.

### Deliverables
1. **Chaining contract document**
   - New SOP/contract file, e.g. `os/sops/TDE_CHAINING_CONTRACT_V1.md`
   - Defines dependency semantics, promotion rules, evidence expectations, fail-closed conditions

2. **Schema authority decision**
   - Decide where chaining metadata is canonical for v1:
     - DB metadata JSON on tasks, and/or
     - projected markdown-compatible annotations

3. **Pilot workflow selection**
   - Pick 1-2 workflow families for first implementation, such as:
     - implement -> verify -> deploy-ready
     - verify -> closeout -> improvement-log update

### Acceptance criteria
- contract published
- first pilot workflow families named
- promotion semantics frozen for v1

## Phase 1 — Minimal chaining metadata model
Purpose: make dependency structure machine-readable.

### Required schema/runtime additions
Add task metadata fields in canonical DB state:
- `depends_on`: list of predecessor task IDs
- `activation_rule`: enum/string, initial supported value: `all_predecessors_done`
- `objective_id`: optional but recommended link to higher-level target
- `stage_id`: optional grouping for workflow stages
- `chain_policy`: optional boundedness/promotion hints
- `activated_by`: runtime-populated provenance field
- `activated_at`: runtime-populated provenance field

### Design rules
- v1 only supports deterministic predecessor completion checks
- no conditional free-text logic
- no generated subtask trees
- dependency references to unknown task IDs fail validation or remain inactive

### Deliverables
- metadata schema spec in SOP and/or schema registry
- read/write support in `tools/tde_state_store.py`
- minimal parser/serializer behavior for projection surfaces if needed

### Acceptance criteria
- tasks can store dependency metadata in canonical state
- metadata survives read/write/export cycles
- invalid dependency shapes fail closed

## Phase 2 — Readiness promotion engine
Purpose: make completed predecessor tasks promote successors automatically.

### Runtime changes
Implement a deterministic promotion pass in the TDE job tick path.

Preferred runtime sequence:
1. load canonical tasks
2. evaluate successor eligibility for non-ready tasks
3. promote newly eligible tasks to `ready`
4. emit activation evidence
5. apply normal claim-and-execute rules

### Promotion rule for v1
A task may be promoted to `ready` only if:
- all `depends_on` tasks exist,
- all predecessor tasks are complete,
- no required approval gate is pending,
- task is not already done,
- activation rule is valid and supported,
- chain policy bounds are not breached.

### Promotion artifact
Per tick, emit activation block or separate artifact showing:
- predecessor IDs
- promoted successor IDs
- activation rule used
- objective/stage context
- any skipped tasks and reasons

### Files likely to change
- `tools/tde_job_tick_runner.py`
- `tools/tde_state_store.py`
- possibly new helper module such as `tools/tde_chaining.py`

### Acceptance criteria
- successor promotion is deterministic
- repeated tick on same state is idempotent
- promotion does not bypass approval-gated actions
- promotion evidence is emitted reliably

## Phase 3 — Validation, tests, and evidence bundle
Purpose: prove chaining is safe and works as intended.

### Test cases required
1. **Happy path chaining**
   - Task A done -> Task B promoted -> next tick claims B

2. **Missing predecessor**
   - referenced predecessor absent -> fail closed or remain inactive with explicit reason

3. **Partial predecessor completion**
   - one of several predecessors still incomplete -> no promotion

4. **Idempotent re-run**
   - same tick/state repeated -> no duplicate promotion

5. **Approval-gated successor**
   - successor becomes eligible but action remains blocked pending approval

6. **WIP bound honored**
   - multiple successors ready -> claim cap still enforced

7. **Rollback compatibility**
   - chaining feature disabled -> existing job tick behavior preserved

### Verification artifacts
Add evidence under `knowledge/evidence/YYYY-MM/`, for example:
- `tde-chaining-simulation-pass.json`
- `tde-chaining-failclosed-missing-predecessor.json`
- `tde-chaining-wip-bound-pass.json`
- verification note summarizing results

### Acceptance criteria
- automated tests pass
- artifacts prove both happy path and fail-closed behavior
- validator/index surfaces updated if needed

## Phase 4 — Pilot rollout
Purpose: prove the mechanism in a narrow real workflow before broad adoption.

### Pilot design
Use one or two low-risk workflow families with clear stage boundaries.

Recommended first pilot:
- implementation task complete
- verification task auto-promoted to ready
- verification completion auto-promotes deployment-readiness review task

Optional second pilot:
- verification complete
- improvement log/update task promoted automatically

### Rollout controls
- feature flag or config switch for chaining enablement
- limited to named objectives/workflow families
- bounded number of promotions per tick
- explicit rollback path to plain scheduled claim loop

### Pilot success criteria
- at least one real chain progressed without manual prompting
- no duplicate promotions
- no approval bypass
- no ambiguity about why successor was activated

## Phase 5 — Product-owner adoption package
Purpose: make the capability usable, not just implemented.

### Deliverables
1. **Usage guidance for Product Owners**
   - how to model staged chains
   - when to use dependencies
   - when not to use chaining

2. **Example templates**
   - simple 3-stage chain examples
   - example dependency metadata

3. **Governance note**
   - clarify that chaining is for bounded deterministic progression, not autonomous scope expansion

### Acceptance criteria
- at least one documented example available
- PO guidance references the new chaining contract
- operating instruction updated if needed

## Phase 6 — Review gate for v2 candidates
Purpose: decide whether to extend beyond state-driven chaining.

### Questions for later review
- Is successor creation actually needed, or is promotion enough?
- Which workflow families justify automatic generation?
- Are loop-prevention and scope-boundary controls strong enough?
- Is direct dispatch worth the additional complexity?

### Decision options
- remain on v1 promotion model
- add controlled template-based successor generation
- reject broader autonomy and keep bounded chaining only

## Required artifacts and changes by area

### Contracts / governance
- `os/sops/TDE_CHAINING_CONTRACT_V1.md` (new)
- possible update to `os/tde/INDEX.md`
- optional update to `governance/TDE_PRODUCT_OWNER_OPERATING_INSTRUCTION_V1.md`

### Runtime / state
- `tools/tde_state_store.py`
- `tools/tde_job_tick_runner.py`
- optional `tools/tde_chaining.py`
- canonical DB metadata handling

### Tests
- new unit tests for chaining promotion
- regression tests for legacy non-chaining behavior

### Evidence
- chaining verification artifacts
- pilot execution note
- rollout/rollback evidence

## Proposed work breakdown

### Slice 1 — Contract + metadata authority
- publish chaining contract
- freeze metadata fields
- choose pilot workflow family

### Slice 2 — DB metadata persistence
- add metadata support and validation
- prove read/write/export stability

### Slice 3 — Promotion engine
- add deterministic promotion pass
- emit activation evidence

### Slice 4 — Test and fail-closed bundle
- add automated tests
- publish verification artifacts

### Slice 5 — Controlled pilot
- enable for one workflow family
- observe and document results

### Slice 6 — Product-owner packaging
- publish examples and usage note
- update operating instruction references

## Guardrails
The following must remain true throughout implementation:
- No automatic authority expansion
- No automatic external communications
- No approval bypass for gated routes
- No unbounded chain execution per tick
- No hidden task generation in v1
- No ambiguous state transitions without evidence

## Rollback plan
If chaining causes ambiguity or instability:
- disable chaining feature flag / promotion pass
- continue using existing job tick claim model only
- preserve chain metadata in state for later retry
- keep evidence from failed/disabled pilot for diagnosis

## Risks
### 1. Hidden complexity risk
A seemingly simple dependency model can become a workflow engine too quickly.

Mitigation:
- support only one activation rule in v1
- avoid conditional logic and generated tasks

### 2. Product-owner misuse risk
Users may model vague aspirations as dependency chains.

Mitigation:
- guidance and examples
- require explicit staged tasks

### 3. Ambiguous successor activation risk
If successor activation is not transparent, trust drops quickly.

Mitigation:
- explicit activation evidence
- provenance fields (`activated_by`, `activated_at`)

### 4. Runaway chain risk
If too many successors activate at once, execution can become noisy.

Mitigation:
- WIP caps
- promotion caps per tick if needed
- pilot-first rollout

## Recommendation
Approve this plan as the implementation path for the next TDE capability increment.

The most important next move is **not** building a full event bus.
It is implementing **deterministic dependency-aware readiness promotion** on top of the scheduler model we already have.

That gives a practical path from today’s pull-based execution to a much stronger high-level-target operating capability, while staying inside the architecture’s current safety and control model.
