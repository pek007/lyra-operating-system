# Practical Query Workflow

Pilot: AI Tools Landscape
Date: 2026-04-03
Status: draft working workflow

## Purpose
Define how a human or agent should actually use the AI Tools Landscape knowledge-compiler instance in practice.

The goal is to make the pilot operationally useful, not only well organized.

---

## 1. Core query principle
Start with the **highest-value compiled layer that can answer the question**, and only drop down to lower layers when needed.

Default order:
1. synthesis notes
2. topic pages
3. concept pages
4. source summaries
5. raw sources

This preserves efficiency while keeping a path back to evidence.

---

## 2. Query types and how to handle them

### Query type A — Orientation / “what is this?”
Examples:
- What is a knowledge compiler?
- How are we thinking about RAG vs compiled knowledge?

Start with:
- synthesis notes
- concept pages

Escalate to sources only if:
- confidence is low
- evidence needs checking
- the concept page is clearly too thin

### Query type B — Topic understanding / “what is our current view?”
Examples:
- What is our view of provenance in these systems?
- What do we currently think about workflow vs agent design?

Start with:
- topic pages
- related synthesis notes

Escalate to source summaries if:
- the topic page is thin
- the question asks for grounding or disagreement

### Query type C — Source comparison / “how do these sources differ?”
Examples:
- How does Anthropic differ from Karpathy on system design emphasis?
- How does VeriTrail add to FINOS?

Start with:
- relevant source summaries
- then concept/topic pages

Escalate to raw sources if:
- the distinction matters materially
- the summary level feels too interpretive

### Query type D — Evidence check / “what supports this?”
Examples:
- What source basis do we have for markdown-first?
- How well supported is this concept?

Start with:
- concept page or synthesis note
- then inspect linked source summaries
- then drop into raw sources when needed

### Query type E — Output creation / “turn this into something usable”
Examples:
- write me a memo
- prepare an executive note
- produce a comparison brief

Start with:
- synthesis notes if available
- otherwise topic/concept/source-summary chain

Then create:
- a durable output artifact if the result is likely to be reused

---

## 3. Escalation rule
Escalate downward only when one of these is true:
- confidence is weak
- the current layer is too thin
- the user asks for source grounding
- the question is materially sensitive
- cross-source disagreement matters

This avoids unnecessary raw-source traversal while preserving traceability.

---

## 4. File-back rule
A query result should be filed back into the pilot when it is:
- likely to be reused
- more than a one-off answer
- clarifying an important concept or distinction
- improving the pilot’s structure or future navigability

Likely destinations:
- `compiled/syntheses/` for durable cross-source insight
- `outputs/` for briefs, memos, decks, or charts
- `compiled/concepts/` or `compiled/topics/` when the answer materially improves a standing page

Do **not** file back everything.
Only durable, reusable outputs should compound into the system.

---

## 5. Confidence rule
When answering from the pilot:
- use the highest compiled layer available
- but state uncertainty if the supporting source set is weak or uneven
- do not overstate concept maturity just because a page exists

A page existing is not the same as a concept being well established.

---

## 6. Practical examples

### Example 1
Question: “What is the main difference between a knowledge compiler and RAG?”
Path:
1. read synthesis `retrieval-vs-rag-vs-compiled-knowledge`
2. check `knowledge-compiler` concept if needed
3. answer from synthesis unless grounding is requested

### Example 2
Question: “How strong is our case for markdown as the intermediate representation?”
Path:
1. read `markdown-as-ir` concept
2. inspect linked source summary
3. explicitly mention lower confidence and weaker evidence base
4. recommend stronger sourcing before firm conclusions

### Example 3
Question: “Create a short note on provenance requirements for our future knowledge systems.”
Path:
1. read `provenance-and-integrity` topic
2. read relevant synthesis/concepts
3. produce memo artifact
4. file back only if reusable beyond the immediate ask

---

## 7. Current limitation note
At this stage, the pilot is still small.
That means:
- navigability is relatively easy
- manual traversal is still workable
- retrieval helper tooling is not yet necessary for most questions

This workflow should be revisited once corpus size and cross-link density increase.

---

## 8. Bottom line
Use the compiled layer first, verify through lower layers when needed, and only file back outputs that truly strengthen future work.
