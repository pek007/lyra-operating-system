# AI-Native Software Delivery Operating Policy v1 (90-Day Trial)

## Purpose
Run a software process that is reliable, auditable, and continuously improving in an AI-agent-heavy environment.

## Scope
Applies to all software work: feature development, bugfixes, refactors, ops, security, and research-to-build handoffs.

## Non-Negotiable Gates

### Gate A — Before work enters Active
A work item may not move to **Active** unless it has:
1. `WO-ID` (Work Order ID)
2. Objective and explicit non-goals
3. Acceptance criteria (observable/testable)
4. Risk class (Low / Medium / High)
5. Verification plan (tests/checks required)
6. Dependency declaration (models/tools/3PPs touched)

### Gate B — Before merge
A PR/merge may not proceed unless:
1. PR/commit includes `WO-ID`
2. Change Artifact (CA) is attached
3. Required checks pass for risk class

## Decision Rights
- **Peter (Owner):** priorities, scope trade-offs, budget, external commitments, high-risk decisions.
- **Control Tower (Lyra):** enforce gates, route work, maintain audit links, track weekly metrics.
- **Build agents:** execute within WO boundaries; escalate on ambiguity, blocker, security concern, or scope drift.

## Trade-off Policy (Quality / Speed / Cost)
Each WO must declare work type and default trade-off profile:
- **Incident/Security:** quality + speed > cost
- **Feature:** quality + cost balance; speed constrained by verification
- **Refactor:** quality > speed
- **Exploration:** speed + learning > polish (non-production by default)

If uncertainty is high, reduce batch size and increase verification depth.

## Cadence Model (Hybrid)
- **Execution:** flow-based with WIP limits
- **Governance:** weekly review cadence + monthly improvement review

### Initial WIP limits
- Build lane: max 2 active WOs
- Research lane: max 2 active WOs
- High-risk WOs: max 1 active WO

## Product Boundary & Dependency Rule
- Treat initiatives as distinct products with explicit boundaries.
- Default rule: products may depend on platform/shared components, not directly on other products.
- Any direct product-to-product dependency requires an ADR before implementation.

Reference docs:
- `PRODUCT_PORTFOLIO_REGISTRY.md`
- `PRODUCT_BOUNDARY_TEMPLATE.md`
- `REPO_NAMING_STANDARD_V1.md`

## Jobs vs Agents Rule
- Organize responsibilities as jobs first; assign runtime surfaces second; create persistent agents third.
- A job is not equivalent to a persistent agent.
- New persistent agents require lifecycle evaluation per `AGENT_LIFECYCLE_SOP_V1.md` and decision record via `AGENT_DEPLOYMENT_DECISION_TEMPLATE.md`.
- Chief Architect is handled as JOB-ARC-001 in `JOB_MARKET_MODEL_V1.md`, not as a dedicated persistent agent by default.

## System Direction Layering
- Human governance source-of-truth lives under `governance/`:
  - `system-charter.md`
  - `policy-register.md`
  - `agent-catalog.md`
  - `playbook-inventory.md`
  - `task-decision-engine-contract.md`
- Runtime behavior is derived into built-in OpenClaw files/config (`AGENTS.md`, related bootstrap files, and gateway config).

## Audit Trail Standard (Minimum Viable)
Every delivered change must be reconstructable via:
**Intent (WO) → Prompt/version → Agent run/output → PR/commit → Tests/evidence → Release/decision note**

If this chain is broken, the change is non-compliant.

## Decision-First Delivery Rule
- For new dashboard/reporting initiatives, first prove value with a recurring decision artifact (report/materialized summary) before expanding UI scope.
- UI expansion requires explicit decision-use-case coverage and data contract clarity.

Reference docs:
- `CONTROL_PANEL_TERMINATION_ACTION_PLAN_V1.md`
- `DATA_CONTRACT_INVENTORY_TEMPLATE_V1.md`
- `SYSTEM_OWNERSHIP_CONTRACT_TEMPLATE_V1.md`

## Retro-to-Improvement Rule
Every retrospective action must include:
- owner
- due date
- success metric
- review date

No metric = not a valid retro action.

## Starter Metrics (Track Weekly)
1. WIP (by lane)
2. Cycle time (start → done by WO)
3. First-pass acceptance rate
4. Verification debt (merged changes missing required evidence)
5. Retro action completion rate

## R/Y/G Thresholds (Initial)

### Green
- Verification debt = 0
- Retro completion >= 80%
- Cycle time stable or improving (4-week trend)

### Yellow
- Verification debt = 1-2
- Retro completion 50-79%
- Cycle time volatility increasing

### Red
- Verification debt >= 3
- Retro completion < 50%
- Rework spikes / repeated failed acceptance

**Red rule:** pause new feature starts until debt/instability are reduced.

## Weekly Governance Checklist (45 min)
1. Any Active item missing Gate A fields?
2. Any merge missing WO-ID or CA?
3. Metrics status: R/Y/G + trend
4. Top 3 blockers and owners
5. Select max 1-2 improvement experiments

## 90-Day Success Criteria
By day 90:
- >95% WO/PR linkage compliance
- verification debt near zero
- cycle-time stability improved
- retros convert into measured implemented changes

## Versioning
- Version: v1.0
- Date: 2026-02-27
- Owner: Peter/Lyra
