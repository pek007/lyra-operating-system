# Readiness Scorecard

Status: Draft active
Product: Task Management (`A-007`)
Capability focus: TDE
Date: 2026-03-11
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

Current assessment: **Yellow**

Signals:
- strong conceptual intent and governance posture
- explicit push toward TDE as the system of record
- product review can describe major goals and gaps clearly

Main caution:
- this still needs stronger compact evidence and less directional interpretation

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

Current assessment: **Yellow**

Signals:
- strict production readiness gate exists
- main gap themes are known
- readiness concerns are explicit in the roadmap, risks, and review output

Main caution:
- readiness is still easier to describe than to assess from a compact current-state summary

### 5. Downstream consumability (`pxs`)
Question:
Can `pxs` consume Task Management with minimal custom explanation and without hidden dependencies?

Current assessment: **Yellow**

Signals:
- first formal `pxs` consumption interface now exists
- consumer and provider obligations are explicit
- success conditions for usable consumption are documented

Main caution:
- operational examples and evidence of real downstream use are still thin

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

## Overall assessment
Current overall readiness/health: **Yellow-Green**

Interpretation:
Task Management is structurally strong and increasingly governable, but still not fully compact or proven in operational-readiness terms. The two main readiness gaps remain:
1. compact current-state judgment of TDE readiness
2. stronger evidence of practical downstream consumption in `pxs`

## Highest-leverage next moves
1. keep this scorecard updated during product reviews
2. add clearer evidence links for readiness status
3. produce practical examples or proof points of `pxs` consumption
4. avoid further structural expansion unless it directly improves operability

## Upgrade criteria toward stronger readiness
The scorecard should trend greener when:
- readiness status can be summarized from current evidence without narrative reconstruction
- `pxs` consumption shows real low-friction use
- execution visibility is inspectable in practice, not just in design intent
- governance remains proportionate while proving useful in real work
