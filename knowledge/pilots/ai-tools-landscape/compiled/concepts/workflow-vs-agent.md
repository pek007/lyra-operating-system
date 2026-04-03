# Concept — Workflow vs Agent

Status: initial concept page
Date: 2026-04-03
Confidence: high

## Working definition
The workflow-vs-agent distinction separates:
- **workflows**: predefined orchestration paths for LLM/tool interactions
- **agents**: model-directed systems that decide their own tool use and process path within a task

## Why this concept matters
This is one of the key operating-model decisions for the pilot. A knowledge compiler can be implemented as a bounded workflow, a more flexible agent, or a hybrid of both.

## Practical interpretation
### Workflow pattern
Use when:
- the task is bounded and repeatable
- inputs and outputs are predictable
- auditability and consistency are more important than flexible exploration
- examples: ingest, summarize, update indexes, run lint passes

### Agent pattern
Use when:
- the question is open-ended
- tool choice needs to adapt dynamically
- multi-step exploration is valuable
- examples: exploratory research, deeper synthesis, unresolved comparison work

## Pilot implication
The default posture for the pilot should be:
- **workflow first** for compilation and maintenance
- **agentic flexibility second** for exploratory queries and synthesis where justified

## Risks / cautions
- too much workflow can become rigid and brittle
- too much agentic freedom can create unnecessary cost, drift, and opacity
- complexity should be earned, not assumed

## Related sources
- [Anthropic — Building Effective Agents](../sources/anthropic-building-effective-agents.md)
- [Microsoft Research — VeriTrail](../sources/microsoft-veritrail.md)
