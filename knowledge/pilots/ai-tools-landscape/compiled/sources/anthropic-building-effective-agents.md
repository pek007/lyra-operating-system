# Source Summary — Anthropic: Building Effective Agents

- Source file: `../../raw/external/2026-04-03__anthropic-building-effective-agents.md`
- Date compiled: 2026-04-03
- Theme: workflow vs agent architecture
- Confidence: high

## Summary
Anthropic argues that effective LLM systems are usually built from simple, composable patterns rather than maximal complexity. The source distinguishes between workflows (predefined orchestration paths) and agents (model-directed tool usage with more autonomy), and recommends using the simplest pattern that works. It also emphasizes that many tasks are best handled by retrieval and strong single-call design before adding multi-step agentic complexity.

## Why it matters
This source helps define how Lyra/Vega should interact with compiled knowledge. It gives a practical architectural lens for deciding when the knowledge compiler should run as a bounded workflow and when agentic flexibility is justified.

## Key ideas
- workflows and agents should be distinguished explicitly
- simpler systems are often better than more abstract frameworks
- complexity should be earned, not assumed
- orchestration patterns matter (prompt chaining, routing, orchestrator-workers, evaluator-optimizer)
- tool/interface design quality is critical

## Relevance to this pilot
Supports the operating-model side of the pilot: how compilation, querying, and linting passes should be structured.

## Potential limits / cautions
- broader agent architecture source, not a dedicated knowledge-base design source
- focused on agent systems generally, so knowledge-compiler implications are interpretive

## Candidate links
- concept: `../concepts/workflow-vs-agent.md`
- concept: `../concepts/agent-computer-interface.md`
- topic: `../topics/agentic-research-workflows.md`
