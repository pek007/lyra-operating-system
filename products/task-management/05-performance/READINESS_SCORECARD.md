# Readiness Scorecard

Status: Draft active
Product: Task Management (`A-007`)
Capability focus: TDE
Date: 2026-03-22
Owner: Lyra

## Purpose
Provide a compact readiness and health view for Task Management / TDE.

This scorecard exists to make it easier to answer:
- Is the product healthy?
- Is TDE becoming operationally usable?
- What is the main readiness blocker now?
- Is `pxs` consumption becoming real or still mostly conceptual?

It complements:
- `05-performance/METRICS.md` for broader metric logic
- `TDE_PRODUCTION_READINESS_GATE_V1.md` for strict production GO/NO-GO controls
- `06-architecture/PXS_CONSUMPTION_INTERFACE.md` for downstream usability criteria

## How to use
Use this as the compact review surface during product reviews, milestone checks, and readiness discussions.

Traffic-light scale:
- **Green** = healthy / sufficiently clear
- **Yellow** = usable but with material weakness or ambiguity
- **Red** = not ready / materially weak
- **Gray** = not yet assessed

## Scorecard dimensions

### 1. Product model health
Question:
Can the product be understood and steered from its canonical model without reconstructing context from chat?

Current assessment: **Green**

Signals:
- canonical product model exists and is coherent
- strategy, operating model, governance, interfaces, and decisions are explicit
- product review protocol has already been exercised against the model

Main caution:
- plan and scorecard freshness now matter more than further structure-building

### 2. Execution visibility
Question:
Is meaningful work visible enough to inspect what matters, what is blocked, and what is next?

Current assessment: **Yellow-Green**

Signals:
- TDE is clearly the intended system of record and current active work is visible there
- assignment-acceptance behavior is strongly evidenced rather than merely described
- the main visibility weakness is now compact-surface freshness, not lack of core execution structure

Main caution:
- compact steering surfaces still need to reflect current evidence more directly so executive review requires less reconstruction

### 3. Decision traceability
Question:
Are important product and execution decisions explicit enough to support follow-through and later review?

Current assessment: **Green**

Signals:
- major shaping decisions are captured in `DECISIONS.md`
- product review and interface work are being converted into explicit decisions
- decision logic is no longer transcript-only

Main caution:
- downstream execution decisions inside consuming environments still need consistent linkage

### 4. Readiness clarity
Question:
Can we judge TDE readiness for broader operational use quickly and with confidence?

Current assessment: **Yellow-Green**

Signals:
- Phase 1 boundary acceptance is recorded as PASS
- the bounded executable `pxs` interface is real and documented
- assignment-acceptance evidence is strong (21/21 PASS), so the remaining gap is clearer and narrower than older summaries imply

Main caution:
- the remaining readiness weakness is producer/adapter integration, canonical runtime-task formation for proving slices, and explicit DB-cutover decision closure, not absence of a viable substrate

### 5. Downstream consumability (`pxs`)
Question:
Can `pxs` consume Task Management with minimal custom explanation and without hidden dependencies?

Current assessment: **Yellow**

Signals:
- the `pxs` consumption interface is pilot-operational for bounded use
- consumer and provider obligations are explicit
- deterministic bounded processing and worked examples now exist

Main caution:
- broader operational proof, compatibility clarity, and low-friction inspection evidence are still thinner than the current interface maturity warrants

### 6. Governance fitness
Question:
Are controls proportionate enough to support trust without creating process drag?

Current assessment: **Yellow-Green**

Signals:
- governance principles are explicit
- escalation triggers are clear
- readiness and evidence expectations are visible

Main caution:
- the product must now prove that governance helps execution rather than merely documenting it

## Current evidence anchors
- accepted Phase 1 boundary posture: `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md` (**PASS (Phase 1)**)
- bounded-operational downstream interface: `products/task-management/06-architecture/PXS_CONSUMPTION_INTERFACE.md`
- assignment-acceptance substrate proof: `products/task-management/04-execution/TDE_ASSIGNMENT_ACCEPTANCE_TEST_EVIDENCE_2026-03-16.md` (**21/21 PASS**)
- canonical runtime projection / active TDE state: `os/runtime/TASKS_from_db.md`

## Overall assessment
Current overall readiness/health: **Yellow-Green**

Interpretation:
Task Management is materially stronger than several older compact surfaces implied. Phase 1 boundary posture is accepted, the bounded `pxs` interface is real, and the assignment-acceptance substrate is strongly evidenced. The main remaining readiness gaps are now:
1. compact current-state synchronization across plan/risk/readiness surfaces
2. stronger operational proof of downstream `pxs` consumption
3. explicit closure of the producer/adapter path, proving-slice runtime-task formation, and DB-cutover decision chain

## Highest-leverage next moves
1. keep this scorecard and adjacent compact surfaces synchronized to current evidence and accepted scope
2. add clearer evidence links for readiness status
3. produce the next bounded proof point for `pxs` consumption
4. force explicit runtime-path, proving-slice runtime-formation, and DB-cutover readiness decisions rather than leaving them implicit

## Upgrade criteria toward stronger readiness
The scorecard should trend greener when:
- readiness status can be summarized from current evidence without narrative reconstruction
- `pxs` consumption shows real low-friction use beyond the current bounded slice
- producer/adapter wiring and DB-cutover readiness are explicit and evidenced
- governance remains proportionate while proving useful in real work
