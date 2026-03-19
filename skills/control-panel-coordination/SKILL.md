---
name: control-panel-coordination
description: Coordinate bounded same-runtime intra-Lyra handoffs for Control Panel. Use when another Lyra lane/session should take the next action, when Control Panel needs a concise status/result/blocker update, when ownership or next actor needs clarification, or when a lightweight handoff is better than keeping the workflow central.
---

# Control Panel Coordination

Package bounded same-runtime intra-Lyra coordination without relying on copy-paste or thread history alone.

## Do
1. Decide whether a handoff is actually needed.
2. Keep the request bounded: one next action, one blocker, one decision-needed, or one status ask.
3. Build a compact handoff packet using the intra-Lyra protocol.
4. Recommend whether durable write-back is required.
5. Choose the best continuity target:
   - `jobs/<JOB-ID>/STATE.md`
   - `jobs/<JOB-ID>/HANDOVER.md`
   - relevant product artifact
6. Ask for a concise reply form: `status`, `result`, `decision-needed`, or `blocked`.
7. Summarize only the high-signal outcome back into Control Panel artifacts.

## Escalate instead of handing off when
- ownership is materially ambiguous
- the issue crosses runtime or domain boundaries
- the request implies policy, architecture, or authority change
- no adequate continuity target exists
- the target lane still would not have enough context to act safely

## Output
Produce:
- a compact handoff packet
- continuity-target recommendation
- reply-form expectation
- optional concise follow-up summary template

## References
- Read `references/handoff-examples.md` for packet shape and target-selection heuristics.
