# Concept — Instruction/Data Boundary

Status: initial concept page
Date: 2026-04-03
Confidence: high

## Working definition
The instruction/data boundary is the distinction between trusted instructions that should control model behavior and untrusted content that should be treated as data to analyze rather than commands to follow.

## Why this concept matters
A weak instruction/data boundary is one of the central reasons prompt injection works. If the system does not reliably preserve this distinction, malicious content can influence model behavior by crossing from the data role into the instruction role.

## Current understanding
The current source set suggests:
- prompt injection often exploits weak or blurred instruction/data separation
- structured prompts and explicit segregation help, but do not fully solve the problem
- systems should clearly denote untrusted external content
- control logic should remain in code/policy layers where possible rather than being delegated entirely to the model

## Practical implications
- treat user and external content as data, not authoritative instructions
- use explicit wrappers/segregation for untrusted content
- validate outputs and sensitive actions independently
- keep privileged control logic outside the model where possible

## Caution
A declared instruction/data boundary is not enough by itself. The model may still be influenced by adversarial content, so additional layers such as least privilege, HITL, filtering, monitoring, and sandboxing remain necessary.

## Related sources
- [OWASP Cheat Sheet — LLM Prompt Injection Prevention](../sources/owasp-prompt-injection-prevention-cheat-sheet.md)
- [OWASP GenAI — LLM01:2025 Prompt Injection](../sources/owasp-llm01-prompt-injection.md)
- [Anthropic Docs — Mitigate Jailbreaks and Prompt Injections](../sources/anthropic-mitigate-jailbreaks-and-prompt-injections.md)
