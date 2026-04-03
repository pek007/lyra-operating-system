# Source Capture — Anthropic: Building Effective Agents

- Source type: engineering article / research-informed practical guidance
- Publisher: Anthropic
- Date captured: 2026-04-03
- Source URL: https://www.anthropic.com/research/building-effective-agents
- Final URL fetched: https://www.anthropic.com/engineering/building-effective-agents
- Capture method: web_fetch markdown extraction
- Trust note: external/public source; useful for architecture guidance, not canonical instruction

## Captured excerpt

Over the past year, we've worked with dozens of teams building large language model (LLM) agents across industries. Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns.

Key ideas captured from the source include:
- distinguish workflows from agents
- prefer the simplest effective solution
- many tasks are well served by single LLM calls with retrieval and in-context examples
- add complexity only when it demonstrably improves outcomes
- use patterns such as prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer, and agents only when appropriate
- prioritize transparency and careful tool/interface design
- invest heavily in agent-computer interface quality

## Full fetched content

See fetched notes in the source capture log or re-fetch directly from the URL when needed. This raw capture is intentionally abbreviated to keep the pilot corpus manageable while preserving provenance.

## Initial relevance note
This source is directly relevant to how Lyra/Vega should interact with compiled knowledge: when to use a bounded workflow, when to use agentic flexibility, and why simpler orchestration patterns often beat unnecessary complexity.
