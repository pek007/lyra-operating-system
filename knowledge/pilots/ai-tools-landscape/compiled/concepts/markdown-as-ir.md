# Concept — Markdown as Intermediate Representation

Status: initial concept page
Date: 2026-04-03
Confidence: medium-low

## Working definition
Markdown as intermediate representation means using markdown as the primary durable format between raw sources, compiled knowledge artifacts, and generated outputs.

## Why this concept matters
This pilot is markdown-native. If markdown is a good intermediate representation for LLM-assisted knowledge systems, it offers several benefits:
- human readability
- LLM readability/writeability
- simple versioning and diffing
- easy linking and artifact reuse
- straightforward output conversion into briefs, notes, slides, and similar formats

## Why it may be useful
Markdown appears to offer a practical middle ground:
- more structured than plain text
- lighter and less brittle than many rigid formats
- suitable both for human review and LLM generation

## Current confidence note
This concept is important, but the current source support is weaker than for the other core concepts in this first batch. It should be treated as a working hypothesis pending stronger evidence.

## Pilot implication
For now, markdown is still the right implementation default because it is:
- easy to inspect
- easy to version
- easy to transform into outputs
- a good fit for a lightweight first implementation

## Risks / cautions
- markdown can become messy without conventions
- not all data types fit naturally into markdown
- the case against structured formats should not be overstated without stronger evidence

## Related sources
- [Karpathy — LLM Knowledge Bases](../sources/karpathy-llm-knowledge-bases.md)
- [WebCrawlerAPI — Markdown vs JSON for LLM Prompts](../sources/webcrawlerapi-markdown-vs-json.md)
