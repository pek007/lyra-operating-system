# Prompt Injection

Status: draft wiki page
Date: 2026-04-03
Domain: Controls & Security

## Summary
Prompt injection is a vulnerability class in which malicious or misleading content changes the behavior of an LLM system in ways that conflict with intended instructions, user intent, or control boundaries.

In Lyra/OpenClaw-style systems, prompt injection matters because untrusted content can be combined with powerful tools, browser access, file/system access, and outbound action channels.

## Why it matters
Prompt injection is not just a model-output issue. It becomes a system-risk issue when the model can:
- browse or fetch external content
- call tools
- access sensitive information
- send messages or write files
- act across multiple steps without strong checkpoints

## Key distinctions
### Prompt injection vs indirect prompt injection
Prompt injection is the broader class.
Indirect prompt injection refers specifically to attacks delivered through external content rather than direct user prompting.

### Prompt injection vs hallucination
Hallucination is unsupported generation.
Prompt injection is adversarial steering through inputs/context.

## Practical posture
Lyra should assume prompt injection is:
- persistent
- non-trivial
- not fully solved
- best addressed through layered controls and consequence limitation

## Related pages
- [Prompt Injection Defense](./prompt-injection-defense.md)
- [Least Privilege for Agents](./least-privilege-for-agents.md)
- [Trust Boundary Model](./trust-boundary-model.md)
