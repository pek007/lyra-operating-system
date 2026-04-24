# Thinking Level Operating Policy V1

Date: 2026-04-24
Owner: Lyra
Status: Draft

## Purpose

Define how Lyra/OpenClaw should use thinking levels in practice so we improve decision quality and hard-task reliability without creating unnecessary workflow drag.

This is an OpenClaw integration artifact.
Canonical system-level doctrine should live in the Lyra OS Model and related operating artifacts, while this file carries tool-specific implementation guidance.

## Core conclusion

Do **not** make thinking level control primarily an agent split.
Do **not** make thinking level control primarily a channel split.

Use a **task- and session-based policy** instead:
- global default: `high`
- escalate to `xhigh` for hard or high-stakes work
- drop to `medium` for routine, low-complexity work when speed matters

## Why

Running everything at `xhigh` is attractive when token budget is not tight, but it still has real costs:
- slower iteration loops
- slower clarification cycles
- more friction in routine operations
- occasional overthinking on simple tasks

At the same time, current experience suggests the system has been under-using thinking on harder tasks, which likely contributes to unresolved issues and weak first-pass reasoning on architecture/debugging work.

So the right answer is not "always xhigh" and not "stay conservative by default".
It is: **raise the default, then escalate deliberately**.

## Recommended operating policy

### Default level
- Set the general default to `high`.

### Use `xhigh` for
- architecture decisions
- root-cause debugging on stubborn issues
- difficult refactors
- production-readiness / release-risk review
- security-sensitive reasoning
- synthesis across many artifacts or competing constraints
- second-pass retries after one or two failed or weak attempts at lower thinking

### Use `high` for
- normal implementation work
- most planning work
- non-trivial operational decisions
- reviews where correctness matters but stakes are not exceptional
- default main-session collaboration

### Use `medium` for
- triage
- routine status work
- straightforward edits
- lightweight document cleanups
- quick follow-ups where responsiveness matters more than deeper reasoning

## Escalation rule

Use a simple operating rule:
1. First serious attempt: `high`
2. If unresolved, ambiguous, or repeatedly wrong: retry at `xhigh`
3. If the task turns out simpler than expected: drop to `medium`

This should be the default mental model unless a session is intentionally dedicated to deep review from the start.

## Implementation options considered

### Option A — separate agents by thinking level
Example: one "routine" agent and one "deep" agent.

Pros:
- simple mental model
- stable persona/role separation is possible

Cons:
- thinking-default behavior per named agent is not the most reliable control surface today
- creates operational sprawl
- easy to route work to the wrong agent for the wrong reason
- mixes cognitive-depth policy with identity/ownership design

Recommendation:
- **Do not use this as the primary mechanism.**
- Consider only later if we want genuinely different roles, not just different thinking levels.

### Option B — separate channels by thinking level
Example: one channel/thread for routine work, another for deep analysis.

Pros:
- visible separation
- easy to preserve session-level `/think` settings per thread

Cons:
- channels should reflect workflow/context boundaries, not just reasoning settings
- forces humans to classify work too early
- creates avoidable routing friction
- many real tasks change depth midstream

Recommendation:
- **Use channel separation only when the workflow itself differs** (for example, an architecture/review lane), not just to control thinking.

### Option C — session/task-based thinking policy
Use one general runtime posture, then apply `/think` at session level or explicit thinking settings on spawned runs/subagents.

Pros:
- matches actual task complexity
- lowest operational overhead
- easiest to adjust in real time
- aligns with current OpenClaw control surfaces

Recommendation:
- **Use this as the primary mechanism.**

## Practical implementation recommendation

### 1. Global default
Set the default thinking level to `high`.

### 2. Session control
Use session-level `/think` changes when a thread clearly becomes:
- deep architecture / decision work -> `/think xhigh`
- routine / speed-sensitive work -> `/think medium`

Important practical note:
- For the **current human-facing session/thread**, the switch is normally made through the chat command itself.
- That means the operator can send `/think xhigh` (or `/think high`, `/think medium`) in that thread.
- Policy docs such as `AGENTS.md` explain **when** to switch, but they do not by themselves change the runtime setting.
- For spawned runs/subagents, the thinking level can be set explicitly at launch time.

### 3. Dedicated deep-work sessions
It is reasonable to keep a small number of sessions/threads intentionally pinned to `xhigh`, but only where the workflow itself is distinct, for example:
- architecture / design review
- release / readiness review
- difficult debugging lane

These are **workflow lanes**, not separate agents created only for thinking control.

### 4. Spawned work
When spawning subagents or isolated runs for hard tasks, explicitly set a higher thinking level there rather than changing the entire environment.

### 5. Review checkpoint
After 1 week of use, review:
- did hard-task quality improve?
- did latency become annoying in normal work?
- which task classes clearly benefited from `xhigh`?
- which tasks should be moved back down to `medium`?

## Recommended default answer to the implementation question

If choosing between agent split and channel split:

- **Primary answer:** neither
- **Best default:** task/session-based control with global `high`
- **If we add structure:** prefer a few dedicated deep-work sessions/threads over separate agents

## Worked example: CRM development

### Example A — normal CRM implementation
Task:
- "Implement the next CRM core-slice endpoint and add the required evidence/test updates."

Recommended thinking level:
- `high`

Why:
- non-trivial implementation work
- real verification needed
- but not automatically a deep-architecture problem

### Example B — CRM architecture ambiguity
Task:
- "We keep circling on the CRM object model, integration boundary, and change-to-evidence lane. Compare the viable options and recommend the best design."

Recommended thinking level:
- `xhigh`

How it works in practice:
1. We are already in a CRM thread running at `high`.
2. The task shifts from implementation to deep design reasoning.
3. At that point, the operator sends `/think xhigh` in that thread, or we move that work into a dedicated CRM architecture/review thread that is intentionally kept at `xhigh`.
4. After the design decision is made, implementation can continue in the same thread or a different implementation thread at `high`.

### Example C — CRM stubborn bug
Task:
- "The CRM pilot evidence gate keeps failing intermittently and prior fixes have not held. Find the real root cause."

Recommended thinking level:
- first pass: `high`
- if still unresolved after a weak or failed pass: `xhigh`

This is the main escalation pattern we want:
- implementation starts at `high`
- repeated failure or ambiguity triggers `xhigh`

## Suggested next operational step

1. Move the global default to `high`
2. Keep the current main session at `high`
3. Use `xhigh` explicitly for hard architecture/debugging/review threads
4. Reassess after a week before introducing more structural separation
