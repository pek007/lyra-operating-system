# Prompt Injection Security Pilot

Status: active pilot
Date created: 2026-04-03
Owner: Lyra / security research domain

## Purpose
This pilot tests the Knowledge Compilation capability in a security domain focused on prompt injection, indirect prompt injection, and practical defense posture for Lyra OS.

## Scope
The pilot should:
- ingest raw source material on prompt injection risks and defenses
- compile reusable markdown knowledge artifacts
- support stronger security synthesis and policy/design thinking
- create reusable outputs for Lyra OS defense posture

The pilot should not:
- silently replace canonical security policy or governance artifacts
- claim operational closure without proper governed follow-through
- become a dumping ground for generic AI security material unrelated to prompt injection risk

## Key references
- `/Users/lyra/.openclaw/workspace/repos/control-panel/docs/capabilities/knowledge-compilation/README.md`
- `/Users/lyra/.openclaw/workspace/repos/control-panel/docs/capabilities/knowledge-compilation/INSTANCE_MODEL.md`

## Folder model
- `raw/` — minimally transformed source material
- `compiled/` — LLM-maintained summaries, topics, concepts, syntheses, indexes
- `outputs/` — durable briefs/memos/policy notes from the pilot
- `logs/` — compile/lint run traces and notes
