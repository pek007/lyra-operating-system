# Thinking Level Lane Patterns V1

Date: 2026-04-24
Owner: Lyra
Status: Draft

## Purpose

Define the first three official OpenClaw lane patterns for reasoning-depth control so thinking-level policy becomes executable operating structure rather than ad hoc switching.

## Design rule

These are **workflow lanes**, not separate named agents created only to hold different thinking defaults.

A lane should exist only when:
- the workflow is genuinely distinct
- the reasoning posture is repeatedly different from normal work
- the lane improves control and repeatability more than it adds routing friction

## Applicability by runtime

### Shared doctrine
The underlying doctrine is shared across work-performing runtimes:
- reasoning depth is an operating control
- there should be a default posture
- escalation should be explicit
- lane usage should be reviewed against real outcomes

This shared doctrine is intended to apply across Lyra and Vega.

### Runtime-local bindings
Lyra and Vega should not be forced into permanently identical local bindings.

They may diverge over time on:
- default thinking posture
- exact lane definitions
- benchmark sets
- escalation triggers

The default rule is:
- share the doctrine
- localize the operating bindings where the runtime boundary or work pattern is genuinely different

### Thin system/control runtimes
Thin system/control runtimes should generally not operate as their own deep-work lanes.

Their role is to:
- route
- wake
- preserve control state
- dispatch bounded work

If deeper reasoning is needed, they should wake or dispatch Lyra, Vega, or a bounded worker/run with an explicit thinking setting rather than accumulate doctrine-heavy reasoning themselves.

## Lane 1 — Delivery Implementation Lane

### Purpose
Advance normal implementation work with solid reasoning and acceptable responsiveness.

### Default thinking
- `high`

### Typical work
- implementation of bounded features
- routine refactors
- evidence/test updates
- normal execution follow-through
- planning that is concrete but not deeply ambiguous

### Entry rule
Use this lane by default unless the task is clearly architecture-heavy, debugging-heavy, or review-heavy.

### Escalation triggers
Escalate out of this lane (or temporarily escalate the lane posture) when:
- repeated failed or weak attempts occur
- architecture ambiguity blocks clean implementation
- hidden boundary decisions start appearing
- root cause is unclear after the first serious pass

### Exit / de-escalation rule
Return to this lane after the deep decision/debug/review work is complete and execution becomes straightforward again.

---

## Lane 2 — Architecture and Decision Review Lane

### Purpose
Resolve design ambiguity, tradeoffs, boundaries, and structural choices where judgment quality matters more than speed.

### Default thinking
- `xhigh`

### Typical work
- architecture tradeoffs
- entity/boundary design
- operating-model choices
- cross-artifact synthesis with competing constraints
- decisions where overbuilding or wrong abstraction is costly

### Entry rule
Use this lane when the task is primarily:
- deciding between viable designs
- clarifying boundaries
- preventing premature architecture or hidden drift
- synthesizing across several artifacts before coding proceeds

### Guardrails
- stay decision-oriented, not academic
- produce explicit rationale and constraints
- hand back a bounded implementation consequence when possible

### Exit rule
Once the design decision is made, move implementation back to the Delivery Implementation Lane.

---

## Lane 3 — Root-Cause Debug and Readiness Review Lane

### Purpose
Handle stubborn debugging, recovery diagnosis, release/readiness review, and other work where weak first-pass reasoning is expensive.

### Default thinking
- start `high`
- escalate to `xhigh` when the first serious pass is weak, ambiguous, or repeatedly unsuccessful

### Typical work
- intermittent or repeated failures
- debugging where prior fixes did not hold
- release-readiness / risk review
- post-recovery verification
- security-sensitive debugging/review tasks

### Entry rule
Use this lane when the task is mainly about finding the real cause, validating safety/readiness, or deciding whether something is trustworthy enough to proceed.

### Escalation rule
Escalate to `xhigh` when:
- the first pass did not isolate the cause
- multiple plausible causes remain
- the review requires synthesis across several logs/artifacts/control surfaces
- a wrong conclusion would create material risk

### Exit rule
Once the root cause or readiness decision is clear, move corrective implementation back to the Delivery Implementation Lane unless the follow-up remains deeply diagnostic.

---

## Runtime control mapping

These lane patterns should be expressed through available OpenClaw controls such as:
- global default reasoning posture in config
- session/thread `/think` changes
- explicit thinking settings on spawned runs/subagents
- dedicated sessions/threads when the workflow itself is distinct enough to justify it

## Default operating posture
- global default: `high`
- architecture/decision lane: `xhigh`
- debug/readiness lane: `high`, with deliberate escalation to `xhigh`

## Operating rule

When in doubt:
1. start in Delivery Implementation Lane at `high`
2. escalate into Architecture/Decision Review Lane or Root-Cause Debug and Readiness Review Lane only when the task shape truly changes
3. return to the implementation lane once the deeper reasoning phase is complete

## Review rule

These lane patterns should be reviewed against real benchmark tasks and real work outcomes.
If they create routing friction without decision-quality gain, simplify them.
If they materially improve judgment quality and reduce repeated errors, keep and formalize them further.
