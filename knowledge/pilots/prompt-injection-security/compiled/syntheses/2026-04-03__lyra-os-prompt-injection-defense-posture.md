# Synthesis — Lyra OS Prompt Injection Defense Posture

Date: 2026-04-03
Status: first synthesis note
Confidence: medium-high

## Purpose
Define the current practical defense posture Lyra OS should take toward prompt injection risk, especially in environments involving tool use, browser/web content, external documents, and broad agent tasking.

## Bottom line
Lyra OS should assume that prompt injection is a persistent, non-trivial, and currently unsolved risk in tool-using and content-ingesting agent systems.

Therefore the practical posture should be:
- **assume untrusted external content can contain instructions**
- **treat prompt injection as a consequence-limitation problem as much as a detection problem**
- **use layered controls instead of trusting one mitigation**
- **reduce agent authority by default**
- **require explicit approval for high-risk actions**
- **prefer bounded workflows over broad autonomy where practical**

## 1. Working threat model
Lyra OS should treat the following as plausible injection channels:
- webpages
- fetched articles or documents
- emails and attachments
- retrieved RAG content
- issue text, comments, repo content, and documentation
- hidden or obfuscated instructions inside otherwise legitimate content

The risk increases when the system can:
- browse
- call tools
- access sensitive data
- send messages
- write to files or systems
- act across multiple steps without strong checkpoints

## 2. Core defense principles

### A. Untrusted content must stay untrusted
External content should be treated as data to analyze, not as instructions to follow.

### B. Reduce consequence, not only likelihood
Even if some injection succeeds, the model should have limited ability to cause harm.

### C. Layer defenses
No single safeguard should be treated as sufficient.

### D. Broad autonomy is higher risk
The more open-ended the task and the wider the authority, the easier it is for adversarial content to steer behavior.

## 3. Practical posture for Lyra OS

### 3.1 Default to bounded workflows
For recurring high-risk or semi-structured tasks, prefer workflow-style orchestration over open-ended agents.

Examples:
- fetch -> summarize -> extract -> human review
- classify -> draft -> approval gate
- read-only research flow instead of act-on-behalf flow

### 3.2 Enforce least privilege for tools and data
- give only the minimum tool access needed
- prefer task-scoped access over general access
- keep dangerous actions behind explicit gates
- separate app/service credentials from broad user authority where possible

### 3.3 Require approval for high-risk actions
Require explicit human approval for actions such as:
- sending external messages
- modifying sensitive files/configs
- executing privileged or destructive actions
- accessing or transmitting sensitive data
- actions that cross trust boundaries

### 3.4 Preserve instruction/data separation
- explicitly denote untrusted content as external data
- avoid letting external content silently merge into the instruction layer
- keep critical policy/control logic outside the model where possible

### 3.5 Use layered screening and monitoring
- input screening for suspicious patterns where practical
- output validation for obvious exfiltration or policy breaches
- monitor tool calls, sensitive actions, and anomalous behavior
- review repeated refusal-bypass attempts or suspicious prompt patterns

### 3.6 Sandbox and isolate where possible
When the model uses code execution, browser-like actions, or file/system access, containment matters. Sandboxing and environment isolation should be treated as first-class defenses.

## 4. What not to rely on
Lyra OS should **not** rely on any of the following as sole defenses:
- prompt wording alone
- a single classifier or content filter
- belief that the model is now "robust enough"
- RAG as a safety mechanism
- user trust in apparently benign content

## 5. Specific implications for Lyra/OpenClaw-style environments
The most relevant practical risks are:
- indirect prompt injection through fetched web content
- malicious content in tool-ingested files or documents
- prompt contamination through broad multi-step tasks
- dangerous consequences when agents combine untrusted content with message sending, file writing, browser control, or code execution

Therefore Lyra/OpenClaw-style systems should be especially careful around:
- browser/web-fetch use
- agentic research flows that can also act
- automation with outbound communication
- combined memory/tool/context workflows

## 6. Current posture recommendation
### Recommended current posture
**Cautious, layered, bounded-by-default.**

In practice this means:
- use powerful tools, but with explicit trust boundaries
- use agentic workflows selectively
- keep sensitive actions approval-gated
- avoid broad “handle everything” instructions when safer bounded flows exist
- maintain ongoing red-team and error-learning posture rather than assuming the problem is solved

## 7. Open questions
- What is the best minimal screening layer for Lyra’s real workflows?
- Which current tool paths have the highest prompt injection blast radius?
- Where should stronger trust-boundary labeling be added in current runtime flows?
- What should the first formal prompt injection red-team checklist for Lyra OS be?

## Related sources
- [OWASP GenAI — LLM01:2025 Prompt Injection](../sources/owasp-llm01-prompt-injection.md)
- [OWASP Cheat Sheet — LLM Prompt Injection Prevention](../sources/owasp-prompt-injection-prevention-cheat-sheet.md)
- [Anthropic — Browser Prompt Injection Defenses](../sources/anthropic-browser-prompt-injection-defenses.md)
- [Anthropic Docs — Mitigate Jailbreaks and Prompt Injections](../sources/anthropic-mitigate-jailbreaks-and-prompt-injections.md)
- [OpenAI — Understanding Prompt Injections](../sources/openai-understanding-prompt-injections.md)

## Related concepts
- [Prompt Injection](../concepts/prompt-injection.md)
- [Indirect Prompt Injection](../concepts/indirect-prompt-injection.md)
- [Instruction/Data Boundary](../concepts/instruction-data-boundary.md)
- [Least Privilege for Agents](../concepts/least-privilege-for-agents.md)
