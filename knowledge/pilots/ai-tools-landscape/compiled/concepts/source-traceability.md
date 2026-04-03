# Concept — Source Traceability

Status: initial concept page
Date: 2026-04-03
Confidence: high

## Working definition
Source traceability is the ability to connect a compiled claim, summary, or synthesized output back to the source material from which it was derived.

## Why this concept matters
Without source traceability, compiled knowledge becomes harder to verify, harder to trust, and harder to maintain. In a system that relies on LLM-generated summaries and syntheses, traceability is a core integrity layer.

## Practical requirements
- preserve source references during ingest
- link compiled artifacts to source files
- maintain enough granularity to check support for important claims
- distinguish between directly grounded content and more interpretive synthesis
- avoid fabricated or misleading citation behavior

## In this pilot
Traceability should mean at minimum:
- each compiled summary points to a source file
- concept and synthesis pages point back to relevant compiled source summaries and, where needed, raw sources
- claims that matter can be checked without reconstructing the whole system from memory

## Important distinction
Traceability is not the same as truth.
A system can correctly cite a weak source.
Traceability supports verification; it does not replace judgment about source quality.

## Risks / cautions
- false confidence from shallow citation habits
- broken or stale links over time
- insufficient granularity for meaningful verification
- overclaiming support where the source is only loosely related

## Related sources
- [FINOS — Citations and Source Traceability](../sources/finos-citations-and-source-traceability.md)
- [Microsoft Research — VeriTrail](../sources/microsoft-veritrail.md)
