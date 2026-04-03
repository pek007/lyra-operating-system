# Minimum Traceability for High-Risk Actions

Status: draft wiki page
Date: 2026-04-03
Domain: Controls & Security

## Summary
Minimum traceability for high-risk actions means keeping enough evidence to distinguish:
- execution success
- routing success
- delivery success
- approval state
- control state

for actions where failure or ambiguity would materially weaken security, auditability, or post-incident learning.

## Why it matters
In Lyra/OpenClaw-style environments, a high-risk action can appear successful at one layer while actually failing or bypassing another. Without explicit traceability, security and control verification become weaker than they should be.

## Practical application
This concept is especially relevant to:
- external messaging and delivery paths
- privileged or destructive actions
- approval-gated actions
- evidence-sensitive automation flows

## Why it belongs in the wiki
This is a reusable control pattern, not just a one-off operational memo.

## Related pages
- [Prompt Injection Defense](./prompt-injection-defense.md)
- [Operational Truth vs Compiled Knowledge Boundary](../governance-authority/operational-truth-vs-compiled-knowledge-boundary.md)
