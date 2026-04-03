# Source Capture — Anthropic Docs: Mitigate Jailbreaks and Prompt Injections

- Source type: product/security guidance
- Publisher: Anthropic Docs
- Date captured: 2026-04-03
- Source URL: https://docs.anthropic.com/en/docs/mitigating-jailbreaks-prompt-injections
- Final URL fetched: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks
- Capture method: web_fetch markdown extraction
- Trust note: external/public source; practical provider guidance input, not canonical internal policy

## Captured excerpt

Anthropic recommends layered safeguards against jailbreaks and prompt injections, especially for tool-using or policy-sensitive applications. The source emphasizes harmlessness screens, input validation, prompt engineering with explicit value boundaries, continuous monitoring, and chaining multiple safeguards together.

Key ideas captured include:
- pre-screening with lightweight models
- structured outputs for constrained classifications
- prompt engineering with explicit rules and values
- continuous monitoring and iterative refinement
- layered defenses for tool-using systems

## Initial relevance note
This is a better fit for the first batch than the earlier Google source because it fetched cleanly and gives direct, practical runtime defense guidance relevant to our environment.
