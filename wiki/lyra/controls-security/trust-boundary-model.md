# Trust Boundary Model

Status: draft wiki page
Date: 2026-04-03
Domain: Controls & Security

## Summary
The trust boundary model defines where Lyra should treat people, systems, content, credentials, and environments as inside or outside a given trust boundary.

## Why it matters
A great deal of security and control quality depends on whether the system correctly distinguishes:
- trusted instructions vs untrusted content
- same-boundary actions vs cross-boundary actions
- personal-assistant assumptions vs shared/multi-user contexts
- low-consequence actions vs high-consequence actions

## Practical implications
The trust boundary model influences:
- approval requirements
- sandboxing choices
- least privilege design
- prompt injection defense posture
- credential/access handling
- whether a runtime can safely operate with broad authority

## Current relevance
This is especially important in Lyra/OpenClaw because the security audit already warns about potential multi-user/shared-boundary conditions while some runtime surfaces still retain broad power.

## Related pages
- [Prompt Injection](./prompt-injection.md)
- [Least Privilege for Agents](./least-privilege-for-agents.md)
- [Prompt Injection Defense](./prompt-injection-defense.md)
- [Operational Truth vs Compiled Knowledge Boundary](../governance-authority/operational-truth-vs-compiled-knowledge-boundary.md)
