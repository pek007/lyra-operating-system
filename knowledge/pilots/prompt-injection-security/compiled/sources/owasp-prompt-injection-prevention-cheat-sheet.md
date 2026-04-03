# Source Summary — OWASP Cheat Sheet: LLM Prompt Injection Prevention

- Source file: `../../raw/external/2026-04-03__owasp-prompt-injection-prevention-cheat-sheet.md`
- Date compiled: 2026-04-03
- Theme: practical defense patterns
- Confidence: high

## Summary
The OWASP cheat sheet treats prompt injection as arising from weak separation between instructions and data, then lays out a broad taxonomy of attacks and a layered defense model. It covers direct and indirect attacks, obfuscation, Best-of-N jailbreaks, multimodal injection, RAG poisoning, multi-turn attacks, and agent-specific attacks. It also proposes concrete defense patterns including structured prompts, input sanitization, output validation, HITL controls, least privilege, monitoring, and dedicated testing.

## Why it matters
This is likely the strongest first-batch source for actionable defense posture. It is especially useful because it moves from threat taxonomy into practical implementation layers.

## Key ideas
- instruction/data separation is central
- layered defenses matter more than single tricks
- least privilege and HITL are important in agentic systems
- remote content sanitization and monitoring matter
- current defenses have real limitations against persistent attackers

## Relevance to this pilot
Core source for moving from general prompt injection concern to a practical Lyra OS defense posture.

## Related concepts
- instruction/data boundary
- layered defense
- least privilege for agents
- HITL for high-risk actions
