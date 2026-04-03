# Source Capture — OpenAI: Understanding Prompt Injections

- Source type: security framing / provider guidance
- Publisher: OpenAI
- Date captured: 2026-04-03
- Source URL: https://openai.com/index/prompt-injections/
- Capture method: web_fetch markdown extraction
- Trust note: external/public source; provider framing input, not canonical internal policy

## Captured excerpt

OpenAI frames prompt injection as a social engineering attack specific to conversational and agentic AI, especially where third-party content can enter the context window. It stresses that as AI systems gain tool use, web access, and access to sensitive data, prompt injection risk grows.

Key ideas captured include:
- prompt injection is analogous to phishing/scam patterns for AI systems
- broad task instructions increase risk
- explicit user confirmation and watch/approval modes are important for sensitive actions
- sandboxing and layered security controls matter
- automated monitors and red teaming are core defenses
- users should stay aware of connected-app and data-access risk

## Initial relevance note
Useful for user-control posture, red-teaming perspective, and framing prompt injection as a practical deployment challenge rather than just a model-level bug.
