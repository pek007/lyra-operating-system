# Source Summary — OpenAI: Understanding Prompt Injections

- Source file: `../../raw/external/2026-04-03__openai-understanding-prompt-injections.md`
- Date compiled: 2026-04-03
- Theme: provider security framing and user-control posture
- Confidence: medium-high

## Summary
OpenAI frames prompt injection as a conversational/agentic social engineering problem in which third-party content can enter the model context and attempt to steer behavior. The source emphasizes that risk rises when systems gain tool access, web access, sensitive data access, and broad task latitude. It highlights layered security controls, sandboxing, user confirmation steps, watch/approval modes, and red teaming.

## Why it matters
Useful for user-control posture and for understanding prompt injection not only as a model failure but also as an interaction and deployment-design problem.

## Key ideas
- prompt injection is analogous to phishing for AI systems
- broad instructions increase risk
- explicit confirmations and user awareness matter
- sandboxing and overlapping controls matter
- red teaming and monitoring are ongoing requirements

## Relevance to this pilot
Helpful for building a practical defense posture that combines model-side, runtime-side, and user-control-side mitigations.

## Related concepts
- user-control posture
- approval boundaries
- sandboxing
- broad-task risk
