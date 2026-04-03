# Source Summary — Microsoft Research: VeriTrail

- Source file: `../../raw/external/2026-04-03__microsoft-veritrail.md`
- Date compiled: 2026-04-03
- Theme: multi-step provenance / hallucination localization
- Confidence: high

## Summary
VeriTrail addresses hallucination detection in multi-step generative workflows by requiring more than final-output checking. It introduces provenance and error localization across directed acyclic graphs of source material, intermediate outputs, and final outputs. The key contribution is not only saying whether a claim is supported, but tracing how it was derived and where unsupported content likely entered the process.

## Why it matters
This source is highly relevant because our system is inherently multi-step: ingest, compile, synthesize, report, and act. It suggests that trustworthy knowledge systems should preserve evidence trails across stages rather than only validate the final artifact.

## Key ideas
- represent generative flows as traceable structures
- verify claims through intermediate stages, not only at the end
- preserve evidence trails and verdict history
- enable provenance and error localization together
- support user verification without requiring full raw graph inspection

## Relevance to this pilot
Useful for future design of compile logs, synthesis lineage, and integrity/linting workflows.

## Potential limits / cautions
- research-heavy and more complex than the initial pilot likely needs
- may be overkill for the first implementation slice

## Candidate links
- concept: `../concepts/provenance-trail.md`
- concept: `../concepts/error-localization.md`
- topic: `../topics/multi-step-ai-integrity.md`
