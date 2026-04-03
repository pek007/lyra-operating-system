# Source Capture — OWASP GenAI: LLM01:2025 Prompt Injection

- Source type: risk taxonomy / security guidance
- Publisher: OWASP GenAI Security Project
- Date captured: 2026-04-03
- Source URL: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- Capture method: web_fetch markdown extraction
- Trust note: external/public source; practical security guidance input, not canonical internal policy

## Captured excerpt

OWASP frames prompt injection as a vulnerability where inputs alter LLM behavior or outputs in unintended ways, including both direct and indirect prompt injection. It emphasizes that prompt injection remains possible because of the nature of generative AI, and that defenses are mitigating rather than foolproof. It highlights impacts such as sensitive data disclosure, unauthorized actions, manipulation of decision processes, and tool misuse.

Key mitigation ideas captured include:
- constrain model behavior
- define expected outputs and validate them
- filter inputs and outputs
- enforce least privilege
- require human approval for high-risk actions
- segregate and identify external content
- adversarial testing and attack simulations

## Initial relevance note
This is the baseline framing source for the pilot and should likely anchor the first concept and topic pages.
