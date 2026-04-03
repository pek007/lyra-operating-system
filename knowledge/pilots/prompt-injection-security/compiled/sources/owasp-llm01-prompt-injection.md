# Source Summary — OWASP GenAI: LLM01:2025 Prompt Injection

- Source file: `../../raw/external/2026-04-03__owasp-llm01-prompt-injection.md`
- Date compiled: 2026-04-03
- Theme: core prompt injection definition and risk framing
- Confidence: high

## Summary
OWASP frames prompt injection as a vulnerability where inputs alter LLM behavior or output in unintended ways. It distinguishes direct and indirect prompt injection and emphasizes that prompt injection is deeply tied to the nature of generative AI, meaning mitigation rather than perfect prevention is the realistic stance. It highlights real impacts such as data disclosure, tool misuse, unauthorized actions, content manipulation, and critical decision interference.

## Why it matters
This is the anchor risk-framing source for the pilot. It gives a practical baseline taxonomy and a broad enough mitigation frame to structure the first concepts and defense posture.

## Key ideas
- prompt injection can be direct or indirect
- RAG and fine-tuning do not eliminate the risk
- agency/tool access amplifies impact
- defenses include constrained behavior, validation, filtering, least privilege, human approval, external-content segregation, and adversarial testing

## Relevance to this pilot
Foundational source for concept and topic formation.

## Related concepts
- prompt injection
- indirect prompt injection
- least privilege for agents
- human approval for high-risk actions
