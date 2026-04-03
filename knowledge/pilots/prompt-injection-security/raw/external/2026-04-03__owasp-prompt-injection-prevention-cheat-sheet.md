# Source Capture — OWASP Cheat Sheet: LLM Prompt Injection Prevention

- Source type: practical defense checklist / implementation guidance
- Publisher: OWASP Cheat Sheet Series
- Date captured: 2026-04-03
- Source URL: https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html
- Capture method: web_fetch markdown extraction
- Trust note: external/public source; practical implementation input, not canonical internal policy

## Captured excerpt

This source describes prompt injection as arising from weak separation between instructions and data in LLM applications. It provides a broad attack taxonomy including direct injection, indirect injection, obfuscation, typoglycemia attacks, Best-of-N jailbreaking, HTML/Markdown injection, multi-turn attacks, multimodal injection, RAG poisoning, and agent-specific attacks.

Key defense ideas captured include:
- input validation and sanitization
- structured prompts with clear instruction/data separation
- output validation and monitoring
- human-in-the-loop controls
- least privilege and agent-specific tool controls
- remote content sanitization
- comprehensive monitoring and testing

## Initial relevance note
This is likely the strongest practical defense source in the first batch and should heavily influence any first defense-posture synthesis.
