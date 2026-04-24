# Proposed Wording — Thinking-Level Operating Design

Date: 2026-04-24
Owner: Lyra
Status: Draft support artifact for model-change candidate `2026-04-24-thinking-level-operating-design.md`

## Purpose

Provide draft wording that can be promoted into canonical Lyra OS Model artifacts if the model-change candidate is accepted.

---

## A. Proposed addition to `LYRA_OS_RUNTIME_AND_OPERATING_MODEL_V1.md`

### New subsection: Reasoning-depth control

Lyra OS runtime operation should treat **reasoning depth / thinking level** as an explicit operating-control dimension.

Reasoning depth is not only a prompt-writing preference or model-quality setting.
It is part of how the runtime balances:
- decision quality
- latency
- control
- throughput
- risk of under-reasoning on hard tasks
- risk of over-reasoning on routine work

The operating model should therefore prefer:
- a clear default reasoning posture for general work
- explicit escalation on tasks where stronger judgment materially improves outcomes
- lower reasoning posture where responsiveness is the more important operating constraint

### New subsection: Reasoning escalation rule

Lyra OS should use an explicit reasoning-escalation pattern rather than rely only on operator instinct.

A default pattern is:
1. use the standard runtime reasoning posture for normal work
2. escalate to stronger reasoning for architecture, root-cause debugging, difficult tradeoff decisions, security-sensitive review, or repeated weak/failed first passes
3. return to the standard posture when the task returns to bounded execution or routine follow-through

This escalation may be expressed through:
- session/thread control
- dedicated workflow lanes
- spawned runs with explicit reasoning settings
- other runtime controls supported by the execution substrate

The key design rule is that reasoning escalation should be **explicit, bounded, and purposeful**.
It should not remain an undocumented habit.

### New subsection: Deep-work lanes

When certain work repeatedly benefits from stronger reasoning posture, Lyra OS may define dedicated **deep-work lanes** for that workflow class.

Examples may include:
- architecture / design review
- root-cause debugging
- release/readiness or risk review

These lanes exist to stabilize execution quality for work with distinct reasoning needs.
They should not be introduced casually, and they should reflect workflow differences rather than create unnecessary runtime sprawl.

### New subsection: Runtime review rule for reasoning posture

Reasoning-depth policy should be reviewed using evidence from real representative tasks.

Lyra OS should not harden a reasoning policy solely from intuition, vendor guidance, or isolated anecdotes.
Where useful, benchmark tasks or recurring work samples should be used to assess:
- whether stronger reasoning improved judgment quality
- which task classes benefited materially
- where higher reasoning created latency without enough quality gain

This keeps reasoning-depth policy inside the inspectable runtime-improvement loop.

---

## B. Proposed addition to `LYRA_OS_LEARNING_AND_EVOLUTION_MODEL_V1.md`

### New subsection: Promotion rule for reasoning-level learning

Learning about reasoning depth should be treated like other operating learning.

If local experiments repeatedly show that different reasoning postures materially change:
- decision quality
- error rate
- architecture judgment
- debugging reliability
- review quality
- workflow speed/drag tradeoffs

then that learning should be considered for promotion beyond local prompt habits.

Possible promotion targets include:
- runtime operating model updates
- workspace operating guidance
- product-local lane conventions
- execution-profile defaults
- review and benchmark protocols

### New subsection: Anti-drift rule for reasoning posture

Reasoning-depth behavior should not drift silently into de facto system design.

Unhealthy drift exists when:
- stronger reasoning is repeatedly used in practice but not reflected in operating guidance
- defaults remain weak while operators compensate informally
- deep-work threads emerge repeatedly without explicit lane design
- speed/quality tradeoffs are argued from intuition without benchmark evidence

When that happens, the appropriate response is explicit review and promotion or constraint, not continued informal adaptation.

---

## C. Optional short doctrine addition to `LYRA_OS_MODEL_V1.md`

A short cross-model doctrine statement could be:

**Lyra OS treats reasoning depth as part of runtime operating design. Default posture, escalation posture, and any deep-work lanes should be explicit, evidence-informed, and governed rather than left to silent habit.**
