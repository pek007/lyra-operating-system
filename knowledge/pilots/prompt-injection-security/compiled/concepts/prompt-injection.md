# Concept — Prompt Injection

Status: initial concept page
Date: 2026-04-03
Confidence: high

## Working definition
Prompt injection is a vulnerability class in which malicious or misleading input changes the behavior of an LLM system in ways that conflict with the intended instructions, operating boundaries, or user intent.

## Why this concept matters
This is the umbrella security concept for the pilot. It matters because LLM systems do not cleanly separate instructions from data the way traditional systems separate code from input. As a result, text or other content entering the context window can function as an attack vector.

## Current understanding
The current source set suggests:
- prompt injection is fundamental to current LLM application design, not a niche edge case
- both direct and indirect forms matter
- tool access, browser access, sensitive data access, and broad task latitude increase impact
- mitigation is realistic; perfect prevention is not currently proven

## Main impacts
- safety bypass
- sensitive data disclosure
- system prompt leakage
- unauthorized tool or API actions
- manipulation of outputs or decisions
- contamination of downstream reasoning/workflows

## Related distinctions
### Prompt injection vs jailbreaking
Jailbreaking is often a form or subset of prompt injection focused on bypassing safety constraints. Prompt injection is the broader class.

### Prompt injection vs model hallucination
Hallucination is unsupported generation. Prompt injection is adversarial steering or manipulation of behavior through inputs/context.

## Related sources
- [OWASP GenAI — LLM01:2025 Prompt Injection](../sources/owasp-llm01-prompt-injection.md)
- [OWASP Cheat Sheet — LLM Prompt Injection Prevention](../sources/owasp-prompt-injection-prevention-cheat-sheet.md)
- [OpenAI — Understanding Prompt Injections](../sources/openai-understanding-prompt-injections.md)
