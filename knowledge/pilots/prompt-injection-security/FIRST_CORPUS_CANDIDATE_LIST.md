# First Corpus Candidate List

Pilot: Prompt Injection Security
Date: 2026-04-03
Status: draft ingestion queue

## Purpose
Define the first bounded source corpus for prompt injection and practical defense posture research.

## Recommended first-corpus target size
- Minimum viable corpus: 8 sources
- Good first pilot corpus: 10–15 sources

## Bucket A — Core prompt injection concepts
- direct prompt injection
- indirect prompt injection
- tool-mediated prompt injection
- retrieval/content poisoning as instruction channel

## Bucket B — Practical defenses
- instruction/data separation patterns
- tool permission and capability boundaries
- sanitization / filtering / content isolation
- provenance and trust boundaries for retrieved content
- human approval / high-risk action guardrails

## Bucket C — Agent/runtime implications
- prompt injection in tool-using agents
- multi-step prompt contamination
- memory/context contamination risks
- browser/web-fetch/content-ingest attack paths

## Bucket D — Evaluation / red teaming
- testing prompt injection robustness
- red-team patterns
- failure-mode taxonomies
- practical security checklists

## Immediate next step
Select the first 5 concrete sources across:
1. core concept definition
2. indirect prompt injection
3. practical defense guidance
4. agent/runtime implications
5. evaluation/red-team perspective
