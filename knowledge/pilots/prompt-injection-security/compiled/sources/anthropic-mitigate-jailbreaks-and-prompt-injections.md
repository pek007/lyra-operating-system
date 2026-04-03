# Source Summary — Anthropic Docs: Mitigate Jailbreaks and Prompt Injections

- Source file: `../../raw/external/2026-04-03__anthropic-mitigate-jailbreaks-and-prompt-injections.md`
- Date compiled: 2026-04-03
- Theme: runtime guardrails and layered defense
- Confidence: medium-high

## Summary
Anthropic’s guidance recommends layered safeguards for jailbreak and prompt-injection risk, especially in tool-using or policy-sensitive applications. It emphasizes lightweight pre-screens, input validation, prompt engineering with explicit value/rule boundaries, continuous monitoring, and chaining multiple safeguards together.

## Why it matters
This source is useful because it translates high-level defense posture into practical runtime control ideas that fit directly with guarded tool use and structured workflows.

## Key ideas
- pre-screen risky inputs
- use constrained/structured outputs where possible
- reinforce explicit values and boundaries in prompts
- monitor and refine continuously
- chain multiple defenses rather than relying on one layer

## Relevance to this pilot
Supports the practical runtime-control side of the pilot and complements the broader OWASP framing.

## Related concepts
- layered defenses
- runtime guardrails
- harmlessness screening
- structured outputs as control aid
