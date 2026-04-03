# Concept — Indirect Prompt Injection

Status: initial concept page
Date: 2026-04-03
Confidence: high

## Working definition
Indirect prompt injection occurs when malicious or misleading instructions are delivered through external content that an LLM system processes, rather than directly through the user’s explicit prompt.

## Why this concept matters
Indirect prompt injection is especially important for agents and tool-using systems because it turns apparently ordinary content — webpages, emails, documents, code comments, issue descriptions, retrieved RAG content — into a possible instruction channel.

## Current understanding
The current source set suggests:
- indirect prompt injection is one of the most operationally important prompt injection forms for agentic systems
- browser use and external-content ingestion amplify exposure dramatically
- users may not see the malicious content even when the model processes it
- hidden or embedded instructions can steer actions, outputs, or exfiltration behavior

## High-risk channels
- webpages
- emails and attachments
- PDFs/documents
- repository comments or issue text
- retrieved RAG content
- multimodal inputs

## Why it is dangerous
Indirect prompt injection attacks exploit the fact that the model may treat untrusted external content as instruction-bearing material. This is especially dangerous when the model can browse, click, call tools, send messages, or access sensitive data.

## Related sources
- [OWASP GenAI — LLM01:2025 Prompt Injection](../sources/owasp-llm01-prompt-injection.md)
- [Anthropic — Browser Prompt Injection Defenses](../sources/anthropic-browser-prompt-injection-defenses.md)
- [OpenAI — Understanding Prompt Injections](../sources/openai-understanding-prompt-injections.md)
