# Source Capture — Microsoft Research: VeriTrail

- Source type: research blog / system overview
- Publisher: Microsoft Research
- Date captured: 2026-04-03
- Source URL: https://www.microsoft.com/en-us/research/blog/veritrail-detecting-hallucination-and-tracing-provenance-in-multi-step-ai-workflows/
- Capture method: web_fetch markdown extraction
- Trust note: external/public research source; useful for design ideas, not canonical instruction

## Captured excerpt

VeriTrail addresses closed-domain hallucination detection in multi-step generative workflows and emphasizes that final-output checking is not enough. It introduces traceability with two components:
- provenance: tracing support from final output back through intermediate outputs to source material
- error localization: identifying where unsupported content was likely introduced

Key ideas captured from the source include:
- represent generative processes as DAGs
- verify claims in reverse order from final output toward sources
- maintain evidence trails, not just verdicts
- support provenance and error localization across multi-step workflows
- prioritize reliability, efficiency, scalability, and user agency

## Full fetched content

See fetched notes in the source capture log or re-fetch directly from the URL when needed. This raw capture is intentionally abbreviated to keep the pilot corpus manageable while preserving provenance.

## Initial relevance note
This source is directly relevant to the Lyra/Vega runtime because our knowledge and reporting flows are multi-step. It helps frame how evidence trails and stage-localized errors might be represented in future knowledge-compiler and reporting systems.
