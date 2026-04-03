# Selected First Five Sources

Pilot: Prompt Injection Security
Date: 2026-04-03
Status: selected first ingestion set

## Selection principle
This first set is designed to cover five core needs for the prompt injection/security pilot:
1. core concept definition
2. indirect prompt injection
3. practical defense guidance
4. agent/runtime implications
5. evaluation / red-team perspective

---

## 1. OWASP GenAI — LLM01:2025 Prompt Injection
- **URL:** https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- **Theme:** core concept definition
- **Why selected:** strong framing source for prompt injection as a first-class LLM risk, including indirect prompt injection and agent/tool impacts.
- **What we want from it:** baseline taxonomy, risk framing, and broad attack surface definition.

## 2. Anthropic — Mitigating the risk of prompt injections in browser use
- **URL:** https://www.anthropic.com/research/prompt-injection-defenses
- **Theme:** indirect prompt injection / agent/runtime implications
- **Why selected:** directly relevant to Lyra/OpenClaw-style web/tool use and the problem of untrusted retrieved/browser content steering agent behavior.
- **What we want from it:** practical understanding of injection through browsing and what effective mitigations look like in agentic contexts.

## 3. OWASP Cheat Sheet — LLM Prompt Injection Prevention
- **URL:** https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html
- **Theme:** practical defense guidance
- **Why selected:** likely the strongest immediately actionable practical defense source in the first batch.
- **What we want from it:** defense patterns, operational safeguards, and concrete preventive controls.

## 4. Anthropic Docs — Mitigate Jailbreaks and Prompt Injections
- **URL:** https://docs.anthropic.com/en/docs/mitigating-jailbreaks-prompt-injections
- **Theme:** practical runtime guardrails / agent defense layering
- **Why selected:** substituted for the earlier Google source because it fetched cleanly and gives directly useful layered defense guidance for tool-using systems.
- **What we want from it:** practical runtime safeguards, layered defense patterns, and guardrail design guidance.

## 5. OpenAI — Understanding prompt injections: a frontier security challenge
- **URL:** https://openai.com/index/prompt-injections/
- **Theme:** evaluation / red-team perspective
- **Why selected:** useful for current provider-level framing, red-teaming perspective, and the seriousness of the problem in production systems.
- **What we want from it:** higher-level threat framing and practical signals about robustness, testing, and defense posture.

---

## Coverage assessment
This first five gives us:
- OWASP risk framing
- practical defense checklist material
- Anthropic/browser-agent relevance
- Google agent/file/web safety relevance
- OpenAI security/red-team framing

## Likely next source after the first five
A stronger dedicated red-team/evaluation source or attack taxonomy source, depending on how well the first five cover testing methodology.

## Recommended next step
Ingest these five into `raw/external/`, then compile the first source summaries and initial concepts such as:
- prompt injection
n- indirect prompt injection
- instruction/data boundary
- untrusted content channel
- prompt injection defense posture
