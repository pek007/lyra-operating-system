# AGENT_EXECUTION_SEMANTICS.md

## Purpose
Operational rules for how agents run in the multi-agent model.

## Modes
1. **Persistent:** Control Panel runtime (Lyra main; formerly "Control Tower")
2. **Spawned (default):** specialist subagents for scoped tasks
3. **External workbench:** codex/deep-research/manual runs treated as formal execution lane

## Default Rule
- Use spawned subagents unless long-lived memory/context ownership is explicitly required.

## Spawn Contract
Every spawned run must include:
- Objective
- Scope boundaries
- Allowed tools
- Expected output format
- Timebox/timeout

## Completion Contract
Every completion must return:
1. Outcome summary
2. Artifacts changed
3. Risks/assumptions
4. Next actions + owner

## Escalation
Escalate to the Control Panel runtime when:
- decision becomes Type 1
- security/compliance concerns appear
- cost/risk exceeds planned bounds

## Anti-Drift
- No specialist agent may redefine principles/policies without explicit Control Panel runtime approval.

## Version
- v1.0
- Date: 2026-02-24
