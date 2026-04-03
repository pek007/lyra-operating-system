# Concept — Least Privilege for Agents

Status: initial concept page
Date: 2026-04-03
Confidence: high

## Working definition
Least privilege for agents means restricting model-accessible tools, data, credentials, permissions, and action scopes to the minimum necessary for the task at hand.

## Why this concept matters
Prompt injection risk becomes much more dangerous when the model has broad authority. Limiting the model’s accessible power reduces the blast radius of successful prompt injection and other forms of adversarial steering.

## Current understanding
The current source set suggests:
- tool access and broad permissions are major risk amplifiers
- broad task latitude combined with broad access is particularly dangerous
- many defenses are about reducing consequence, not only reducing attack likelihood
- approval boundaries and sandboxing complement least privilege

## Practical implications
- prefer task-scoped access over general access
- use separate app/service credentials rather than exposing broad user authority where possible
- restrict dangerous tools and data domains by default
- require explicit approval for high-risk actions
- combine least privilege with sandboxing, monitoring, and layered controls

## Related concepts
- approval boundaries
- sandboxing
- high-risk action control
- layered defense

## Related sources
- [OWASP GenAI — LLM01:2025 Prompt Injection](../sources/owasp-llm01-prompt-injection.md)
- [OWASP Cheat Sheet — LLM Prompt Injection Prevention](../sources/owasp-prompt-injection-prevention-cheat-sheet.md)
- [OpenAI — Understanding Prompt Injections](../sources/openai-understanding-prompt-injections.md)
