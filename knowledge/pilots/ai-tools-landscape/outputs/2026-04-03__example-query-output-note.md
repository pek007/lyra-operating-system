# Example Query Output Note

Date: 2026-04-03
Status: example artifact

## Example question
What is the main difference between a knowledge compiler and RAG?

## Example answer
A knowledge compiler and RAG solve related but different problems.

- **RAG** is a runtime retrieval pattern: find relevant source fragments and inject them into the model context for a specific answer.
- **A knowledge compiler** is an architectural layer: it converts raw source material into durable summaries, concepts, indexes, syntheses, and reusable outputs that improve future work.

In short:
- RAG helps answer the current question with retrieved source material.
- A knowledge compiler helps future questions by preserving prior intellectual work in reusable form.

Best current design stance for the pilot:
- compiled knowledge should be primary
- retrieval should support it
- heavier RAG should be introduced only when compiled markdown + lightweight retrieval stop being sufficient

## Why this example exists
This artifact demonstrates the kind of output that may be generated from the pilot. It should be kept only if it improves future reuse; otherwise it is merely illustrative.
