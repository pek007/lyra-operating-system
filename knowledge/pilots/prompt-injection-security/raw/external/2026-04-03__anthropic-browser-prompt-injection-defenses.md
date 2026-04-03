# Source Capture — Anthropic: Mitigating the Risk of Prompt Injections in Browser Use

- Source type: research / practical defense note
- Publisher: Anthropic
- Date captured: 2026-04-03
- Source URL: https://www.anthropic.com/research/prompt-injection-defenses
- Capture method: web_fetch markdown extraction
- Trust note: external/public source; design guidance input, not canonical internal policy

## Captured excerpt

Anthropic frames prompt injection as one of the most significant security challenges for browser-based AI agents, because every visited webpage or processed external asset can become an attack vector. It emphasizes that browser use amplifies risk because the attack surface is large and agents can take varied real-world actions.

Key ideas captured include:
- every webpage is a potential prompt injection vector
- untrusted content can hide instructions invisible to users but processed by the model
- browser agents amplify risk because they can navigate, click, fill forms, and download files
- robustness is improving but far from solved
- defenses include reinforcement-learning robustness, classifiers over untrusted content, and human red teaming

## Initial relevance note
This source is directly relevant to Lyra/OpenClaw-style tool and browser use, making it one of the most important practical sources in this pilot.
