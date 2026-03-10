# Control Panel Coordination Skill

## Purpose
Help Control Panel coordinate bounded same-runtime intra-Lyra work without relying on copy-paste or thread history alone.

## Use when
- another Lyra lane/session should take the next bounded action
- Control Panel needs a concise status/result/blocker update
- ownership or next actor needs clarification
- a lightweight handoff is better than keeping the workflow central

## Core behavior
1. Decide whether a handoff is actually needed.
2. Keep the request bounded: one next action, one blocker, one decision-needed, or one status ask.
3. Build a compact handoff packet using the intra-Lyra protocol.
4. Recommend whether durable write-back is required.
5. Choose the best continuity target (`jobs/<JOB-ID>/STATE.md`, `HANDOVER.md`, or relevant product artifact).
6. Ask for a concise reply form: `status`, `result`, `decision-needed`, or `blocked`.
7. Summarize only the high-signal outcome back into Control Panel artifacts.

## Guardrails
- Do not use for cross-runtime or cross-domain transfers.
- Do not overstep into portfolio strategy or major product decisions.
- Do not create broad work from vague prompts.
- Escalate when ownership is ambiguous, boundary/risk is material, or no adequate continuity target exists.

## Output standard
Produce:
- a compact handoff packet
- continuity-target recommendation
- reply-form expectation
- optional concise follow-up summary template

See `references/handoff-examples.md` for packet shape and target-selection heuristics.
