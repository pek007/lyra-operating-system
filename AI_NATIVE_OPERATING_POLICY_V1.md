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

## Audit Trail Standard (Minimum Viable)
Every delivered change must be reconstructable via:
**Intent (WO) → Prompt/version → Agent run/output → PR/commit → Tests/evidence → Release/decision note**

If this chain is broken, the change is non-compliant.

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
