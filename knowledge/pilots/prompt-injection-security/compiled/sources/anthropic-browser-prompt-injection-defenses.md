# Source Summary — Anthropic: Browser Prompt Injection Defenses

- Source file: `../../raw/external/2026-04-03__anthropic-browser-prompt-injection-defenses.md`
- Date compiled: 2026-04-03
- Theme: browser/agent prompt injection risk
- Confidence: high

## Summary
Anthropic describes prompt injection as one of the most serious security problems for browser-based agents because every visited webpage or embedded asset can become an adversarial instruction channel. It emphasizes that browser agents are particularly exposed because they can browse, click, fill forms, and trigger actions. The source highlights improved robustness but explicitly says the problem is far from solved.

## Why it matters
This is one of the most directly relevant sources for Lyra/OpenClaw-like environments, where tools, browser interaction, and untrusted content all intersect.

## Key ideas
- every webpage is a potential injection vector
- hidden or adversarial content can steer agent behavior
- browser use expands attack surface and consequence range
- defenses include model robustness work, classifiers over untrusted content, and human red teaming
- low attack success is still meaningful risk, not "solved"

## Relevance to this pilot
Strong source for indirect prompt injection, agent-specific risk, and security posture around tool/browser use.

## Related concepts
- indirect prompt injection
- untrusted content channel
- browser/tool attack surface
- layered defenses
