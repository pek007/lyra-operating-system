# PRODUCT_CRON_MODEL_V1.md

Status: Active draft v1  
Owner: Lyra via Control Panel  
Date: 2026-03-10

## Purpose
Define the first bounded cron model for:
- Control Panel (CP-001)
- Task Management (A-001)
- Governance (A-002)

This model clarifies:
- what should remain human-triggered
- what should become cron-driven
- what output/noise rules apply
- where automation should stop

## Core principle
Use cron for **bounded recurring operating loops**, not for ambiguous strategic work.

Cron is appropriate when:
- timing matters
- recurrence adds value
- the work can produce bounded output
- the output can be routed or summarized clearly

Cron is not appropriate when:
- the task is still highly interpretive
- the work needs major judgment or trade-off decisions
- the output is likely to create noise without a clear receiver/action path

## Output/noise rules (apply to all products)
1. A cron loop should have one clear owner.
2. A cron loop should have one bounded purpose.
3. A cron loop should emit either:
   - no message when nothing meaningful changed, or
   - one concise outcome with evidence/path refs.
4. Cron should update durable artifacts when the result matters beyond the run.
5. Cron should escalate, not improvise, when scope becomes ambiguous.
6. Start with the minimum cadence that preserves value.
7. Prefer one good loop over several overlapping loops.

## Product cron model

---

## 1. Control Panel (CP-001)

### Keep human-triggered
- portfolio prioritization
- cross-product trade-offs
- operating-model changes
- major escalation and boundary decisions

### Candidate cron loop
**Control Panel coordination hygiene review**

### Purpose
Surface stale cross-lane coordination items, unresolved handoff dependencies, and watch items that need explicit follow-up.

### Cadence intent
- low-frequency
- likely daily or a few times per week, not high-frequency

### Inputs
- active handoff register
- situational awareness
- selected oversight artifacts
- optionally recent unresolved job/handoff items

### Output
- no output if nothing actionable changed
- otherwise one concise summary containing:
  - stale/blocked coordination items
  - recommended next owner/action
  - artifact refs

### Durable update target
- `SITUATIONAL_AWARENESS.md` only if the issue is material/current
- relevant job/product artifact if a concrete owner/action is identified
- evidence note only if the review itself is important to track

### Guardrails
- do not re-prioritize the portfolio automatically
- do not generate broad worklists from weak signals
- do not spam the central session with low-value hygiene findings

### Recommended status
- **candidate for bounded cron after the coordination skill exists**
- not the first cron to implement

---

## 2. Task Management (A-001)

### Keep human-triggered
- major TDE shape changes
- cutover/deployment judgments
- interface changes with wider system impact
- ambiguous task-policy decisions

### Candidate cron loops
#### A. Task anti-stall review
Purpose:
- detect bounded stalled work or missing recent movement where a simple nudge/escalation is useful

#### B. Task/TDE alignment review
Purpose:
- surface small inconsistencies between current Task Management operating assumptions and the now-documented continuity/handoff model

### Preferred first cron
**Task anti-stall review**

### Cadence intent
- moderate frequency
- enough to prevent drift, not so frequent that it becomes noise

### Inputs
- DB-canonical task/runtime state where applicable
- job bundles for active work
- recent evidence/status artifacts
- explicit anti-stall criteria

### Output
- no output when no bounded anti-stall issue exists
- otherwise one concise result listing:
  - stalled item or missing transition
  - likely next action
  - who should pick it up
  - relevant refs

### Durable update target
- DB/runtime canonical state remains primary
- job `STATE.md` / `HANDOVER.md` when the anti-stall result changes ownership or next action
- evidence note only when repeated/stubborn drift needs tracking

### Guardrails
- do not mutate TDE kernel semantics from cron
- do not invent tasks from weak heuristics
- do not treat transcript silence alone as a stall signal
- do not bypass canonical task-state rules

### Recommended status
- **best first cron candidate** among the three products
- because it has clear recurring value and bounded output potential

---

## 3. Governance (A-002)

### Keep human-triggered
- policy changes
- authority/risk judgments
- exceptions and standard changes
- broader governance interpretation

### Candidate cron loop
**Governance VERIFY reminder/review loop**

### Purpose
Trigger one bounded Governance verification cycle on a known target or cadence and ensure evidence is produced consistently.

### Cadence intent
- low-to-moderate frequency
- only after the manual VERIFY-cycle pattern is clearer

### Inputs
- current governance target list or explicit review slice
- verification procedure/skill
- evidence destination path

### Output
- no output when no scheduled target is due
- otherwise one concise review result:
  - target checked
  - pass/fail/issues-found
  - evidence ref
  - next required action

### Durable update target
- governance evidence artifact
- relevant Governance product artifacts if the result changes status or action
- job state if the review is running under a bounded job

### Guardrails
- do not broaden a bounded VERIFY run into a general governance sweep
- do not auto-change policy from cron output
- do not run until the underlying verification procedure is stable enough

### Recommended status
- **second cron candidate**, after the Governance VERIFY skill/procedure is implemented and trialed manually

---

## Implementation sequence recommendation
1. **Task Management anti-stall review**
2. **Governance VERIFY reminder/review loop**
3. **Control Panel coordination hygiene review**

Rationale:
- Task Management has the clearest bounded recurring need
- Governance should wait until the manual verification capability is stable
- Control Panel should avoid central noise until the skill layer is stronger

## What not to cronify yet
- cross-runtime handoff management
- major product-priority decisions
- broad governance sweeps
- runtime-topology changes
- anything that still depends heavily on implicit agent familiarity

## Review rule
Every cron concept should be re-tested against three questions before implementation:
1. Is the task bounded enough?
2. Is the output/noise ratio good enough?
3. Is there a clear durable artifact or receiver for the result?

## Bottom line
The first bounded cron model should start with:
- **Task Management anti-stall review** as the first implementation candidate
- Governance review loop only after the underlying verification procedure is proven
- Control Panel hygiene loop only after coordination patterns are more stable and low-noise

## Version
- v1.0
- Date: 2026-03-10
