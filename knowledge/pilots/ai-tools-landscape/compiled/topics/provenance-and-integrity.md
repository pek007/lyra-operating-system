# Topic — Provenance and Integrity

Status: initial topic page
Date: 2026-04-03
Confidence: high

## Topic summary
This topic covers the conditions under which a compiled knowledge system remains trustworthy, verifiable, and maintainable. In the current pilot, provenance and integrity are treated as core design constraints rather than optional polish.

## Why this topic matters
An LLM-maintained compiled layer can become persuasive faster than it becomes trustworthy. Without strong provenance and integrity discipline, the pilot risks becoming an eloquent but weakly grounded markdown corpus.

## Current understanding
The current source set supports several important claims:
- source traceability is a real integrity layer, not just a formatting choice
- multi-step AI workflows need more than final-output checking
- evidence trails and error localization matter where generation is staged
- citation presence does not by itself guarantee source quality or truth

## Major subthemes
- source traceability
- citation/verifiability
- provenance trails
- error localization
- weak-source transparency
- stale-link / versioning concerns
- integrity checks and linting

## Current design stance in this pilot
- every compiled source summary should point to a raw source
- concept and synthesis pages should point back to relevant compiled sources
- lower-confidence sources should remain visibly lower confidence
- the pilot should prefer honest uncertainty over decorative citation behavior

## Key open questions
- how much citation granularity is enough for a useful pilot?
- what is the smallest useful provenance trail for syntheses?
- when should a synthesis be considered too weakly grounded to keep?

## Related sources
- [FINOS — Citations and Source Traceability](../sources/finos-citations-and-source-traceability.md)
- [Microsoft Research — VeriTrail](../sources/microsoft-veritrail.md)
- [Karpathy — LLM Knowledge Bases](../sources/karpathy-llm-knowledge-bases.md)

## Related concepts
- [Source Traceability](../concepts/source-traceability.md)
- [Knowledge Compiler](../concepts/knowledge-compiler.md)
