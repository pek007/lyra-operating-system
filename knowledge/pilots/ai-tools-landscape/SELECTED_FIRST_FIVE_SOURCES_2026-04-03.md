# Selected First Five Sources

Pilot: AI Tools Landscape
Date: 2026-04-03
Status: selected first ingestion set

## Selection principle
This set is chosen to maximize conceptual coverage and practical relevance for the first knowledge-compiler pilot, not to represent the final best corpus.

The set emphasizes:
- one anchor pattern source
- one practical retrieval/architecture tradeoff source
- one provenance/trust source
- one agent/workflow source
- one markdown/output-format source

---

## 1. Karpathy — LLM Knowledge Bases
- **Theme:** knowledge compiler / wiki pattern
- **Why selected:** this is the conceptual anchor for the pilot
- **Status:** already ingested
- **Path:** `raw/external/2026-04-03__karpathy-llm-knowledge-bases.md`

## 2. Anthropic — Building Effective Agents
- **URL:** https://www.anthropic.com/research/building-effective-agents
- **Theme:** agentic research workflow / workflow-vs-agent architecture
- **Why selected:** strong, practical, and high-signal on how to think about workflows vs agents. Useful for deciding how Lyra/Vega should interact with compiled knowledge instead of treating "agentic" work as vague magic.
- **What we want to learn from it:**
  - workflow vs agent boundary
  - when orchestration beats autonomy
  - how tool use should be structured

## 3. FINOS AI Governance Framework — Providing Citations and Source Traceability for AI-Generated Information
- **URL:** https://air-governance-framework.finos.org/mitigations/mi-13_providing-citations-and-source-traceability-for-ai-generated-information.html
- **Theme:** provenance / integrity / source-grounding
- **Why selected:** directly relevant to trust, traceability, and integrity in compiled knowledge systems. Gives us a serious counterweight to "let the LLM write the wiki".
- **What we want to learn from it:**
  - what good source traceability should mean in practice
  - what the integrity layer should look like
  - what should be required for verifiable compiled knowledge

## 4. Microsoft Research — VeriTrail: Detecting hallucination and tracing provenance in multi-step AI workflows
- **URL:** https://www.microsoft.com/en-us/research/blog/veritrail-detecting-hallucination-and-tracing-provenance-in-multi-step-ai-workflows/
- **Theme:** provenance across multi-step AI workflows
- **Why selected:** complements the FINOS source with a more workflow-centric and technical framing. Very relevant because our system is not just a static wiki; it is a multi-step agent/runtime system.
- **What we want to learn from it:**
  - how evidence trails can be preserved across multi-step flows
  - how provenance relates to hallucination control
  - what might transfer into Lyra/Vega runtime design

## 5. WebCrawlerAPI Blog — Markdown vs JSON: Choosing the Right Format for LLM Prompts
- **URL:** https://webcrawlerapi.com/blog/markdown-vs-json-choosing-the-right-format-for-llm-prompts
- **Theme:** markdown as an AI-native intermediate representation / output-friendly knowledge format
- **Why selected:** selected as a practical fallback because the previously chosen Webex source did not yield enough body content via fetch to be useful for the pilot. Still directly relevant to our markdown-native design choice.
- **What we want to learn from it:**
  - what markdown buys us for compilation and querying
  - when markdown is a better intermediate than more complex formats
  - how formatting choices affect downstream answer quality
- **Confidence note:** lower confidence than the other four sources until full-body ingestion and review is completed

---

## Coverage assessment
This set covers:
- **knowledge compiler pattern:** Karpathy
- **workflow/agent architecture:** Anthropic
- **provenance/integrity rule:** FINOS
- **multi-step provenance / hallucination control:** Microsoft Research
- **markdown-native representation:** Webex

### Gap still left open
The weakest remaining area in this first five is the explicit **retrieval-vs-RAG tradeoff** theme.
That should be the first target for source number 6.

---

## Recommended next action
1. Ingest sources 2–5 into `raw/external/`
2. Create compiled summary pages for all five selected sources
3. Build first concept pages from recurring ideas:
   - knowledge compiler
   - workflow vs agent
   - source traceability
   - provenance trail
   - markdown as intermediate representation
4. Add retrieval-vs-RAG tradeoff as the next selected source after this first batch
