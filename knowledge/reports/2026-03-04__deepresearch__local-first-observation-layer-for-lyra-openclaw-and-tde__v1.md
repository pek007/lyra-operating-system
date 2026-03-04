# Local-first Observation Layer for Lyra OpenClaw and TDE

## Executive summary

- Define a single canonical `observation` artifact (JSON, versioned by `artifactType` + `schemaVersion`) and register it in your existing schema registry to preserve the current governance contract surface. fileciteturn40file6L1-L1  
- Store large/variable payloads as **content-addressed blobs** (SHA-256) and keep the observation record as an **envelope** that carries hashes, provenance, trust, and redaction state. citeturn0search3turn1search0  
- Make hashing deterministic by explicitly specifying canonicalization rules (RFC 8785-style) before you hash; otherwise, “same JSON” can hash differently across serializers. citeturn1search0  
- Treat provenance as a first-class graph: every derived observation references parent observation IDs + parent record hashes, following a minimal subset of the W3C provenance concepts (entity/derivation/agent). citeturn0search5turn0search7  
- Implement ingestion as a **two-step, local-first pipeline**: “capture” into a local inbox (untrusted/raw), then “normalize” into committed observations (trusted/validated). This keeps CI deterministic and avoids network variance.  
- Provide one lightweight normalizer that accepts four sources: chat/message exports, web capture/search snapshots, task board action logs (e.g., entity["company","Trello","task board SaaS"]), and git-based file-change events. citeturn1search1turn2search0  
- Use explicit trust classification tiers and enforce **fail-closed** rules only at the “observation → decision/task input” boundary (not at capture time), mirroring your existing TDE fail-closed design. fileciteturn45file3L1-L1  
- Integrate with TDE by standardizing a single linking convention (`evidence.observations[]`) across evidence artifacts and decision/report frontmatter, and by validating link-resolvability in CI. fileciteturn49file0L1-L1  
- Extend the existing deterministic derivatives model (inventory + indexes) by adding an **observations index + ledger root** generated in `tools/gen_knowledge_indexes.py`, and enforce drift via your current validator entrypoint. fileciteturn44file0L1-L1 fileciteturn33file2L1-L1  
- MVP is feasible in 7–10 days by adding ~6–8 files and making small additive edits to `schemas/_registry.json`, `tools/gen_knowledge_indexes.py`, and `tools/validate_repo.py`, consistent with the current milestone posture of “additive governance checks only.” fileciteturn49file0L1-L1  

## Default architecture and rationale

### Chosen v1 architecture

**Default**: *File-based, schema-validated observation envelopes + content-addressed blobs + deterministic indexes, all inside the repo’s existing governance framework.*

This matches your current direction: one schema authority (`schemas/`), one validation entrypoint (`tools/validate_repo.py`), and deterministic regeneration + drift checks for derived files. fileciteturn49file0L1-L1 fileciteturn40file6L1-L1 fileciteturn33file2L1-L1

Key properties:

- **Local-first**: captures happen locally; normalized observations are durable files; CI never fetches the network.  
- **Deterministic**: hashes are computed over canonicalized representations (RFC 8785 guidance), and indexes omit volatile timestamps. citeturn1search0  
- **Auditable**: record hashes + provenance links make it tractable to verify “what was observed” and “what was derived.” citeturn0search5turn0search7  
- **Additive to TDE**: does not change current job tick/canary/release semantics; it only adds a formal observation model plus validation and linking rules (matching your Milestone 0.1 non-disruption clause). fileciteturn49file0L1-L1  

### Why alternatives are rejected for v1

- **Database event store (SQLite/Postgres)**: adds schema migrations, backup/restore semantics, and a second “source of truth” outside git; you lose the “workspace-as-code” transparency and deterministic diff reviews that your current repo validation relies on.  
- **External policy engines (OPA/Rego, cloud governance)**: introduces a second language/runtime and a heavier deployment surface area, contrary to the “solo operator + agents” constraint and your current approach of Python-based deterministic validators. fileciteturn33file2L1-L1  
- **Merkle transparency log / signed ledger service**: stronger tamper resistance, but requires key management and/or a remote trust anchor. For v1, git history + record-hash validation is sufficient; later you can add optional signatures. citeturn0search3turn1search0  

## Proposed schema set

All schemas follow JSON Schema Draft 2020-12 conventions (`$schema`, `$id`) consistent with your existing schemas. citeturn0search0turn0search2 fileciteturn42file0L1-L1

### Canonical observation schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://lyra.local/schemas/observation/v1.0.0.schema.json",
  "title": "Observation Artifact v1.0.0",
  "type": "object",
  "required": [
    "artifactType",
    "schemaVersion",
    "observation_id",
    "observedAt",
    "source",
    "integrity",
    "trust",
    "redaction",
    "provenance"
  ],
  "properties": {
    "artifactType": { "type": "string", "const": "observation" },
    "schemaVersion": { "type": "string", "pattern": "^1\\.0\\.0$" },

    "observation_id": {
      "type": "string",
      "pattern": "^OBS-[0-9a-f]{16}$",
      "description": "Deterministic ID: derived from source identity (kind/system/instance/eventId)."
    },

    "observedAt": { "type": "string", "format": "date-time" },
    "ingestedAt": { "type": ["string", "null"], "format": "date-time" },

    "source": {
      "type": "object",
      "required": ["kind", "system", "eventId", "captureMethod"],
      "properties": {
        "kind": {
          "type": "string",
          "enum": [
            "chat_message",
            "web_fetch",
            "web_search",
            "task_board_event",
            "local_file_change"
          ]
        },
        "system": {
          "type": "string",
          "pattern": "^[a-z0-9_.-]{2,32}$",
          "description": "Examples: openclaw, trello, web, git"
        },
        "instance": {
          "type": ["string", "null"],
          "maxLength": 256,
          "description": "Workspace/board/repo identity; stable within system."
        },
        "subject": {
          "type": ["string", "null"],
          "maxLength": 2048,
          "description": "Channel ID, URL, file path, etc."
        },
        "eventId": {
          "type": "string",
          "minLength": 1,
          "maxLength": 512,
          "description": "Stable source-provided ID (message ID, Trello action ID, git commit SHA...)."
        },
        "captureMethod": {
          "type": "string",
          "enum": ["export", "api_poll", "webhook", "manual", "git_log"]
        },
        "actor": {
          "type": ["object", "null"],
          "properties": {
            "kind": { "type": "string", "enum": ["human", "agent", "system"] },
            "id": { "type": "string", "minLength": 1, "maxLength": 128 }
          },
          "additionalProperties": false
        }
      },
      "additionalProperties": true
    },

    "content": {
      "type": "object",
      "required": ["contentType", "storage"],
      "properties": {
        "contentType": { "type": "string", "minLength": 3, "maxLength": 128 },
        "preview": { "type": ["string", "null"], "maxLength": 2000 },

        "storage": {
          "type": "object",
          "required": ["mode"],
          "properties": {
            "mode": { "type": "string", "enum": ["inline", "blob_ref"] },
            "inline": {
              "type": ["string", "null"],
              "description": "Only for small, safe payloads (after redaction)."
            },
            "blobPath": {
              "type": ["string", "null"],
              "pattern": "^[a-zA-Z0-9_./-]+$",
              "description": "Repo-relative path to content-addressed blob."
            },
            "encoding": { "type": ["string", "null"], "enum": ["utf-8", "base64", null] },
            "sizeBytes": { "type": ["integer", "null"], "minimum": 0 }
          },
          "additionalProperties": false
        }
      },
      "additionalProperties": true
    },

    "integrity": {
      "type": "object",
      "required": ["hashAlgorithm", "canonicalization", "contentHash", "recordHash"],
      "properties": {
        "hashAlgorithm": { "type": "string", "enum": ["sha256"] },
        "canonicalization": {
          "type": "string",
          "enum": ["sorted_json_v1"],
          "description": "Deterministic serialization used for hashing the observation record."
        },
        "contentHash": {
          "type": "string",
          "pattern": "^sha256:[0-9a-f]{64}$",
          "description": "Hash of raw blob bytes OR hash of canonical inline content."
        },
        "recordHash": {
          "type": "string",
          "pattern": "^sha256:[0-9a-f]{64}$",
          "description": "Hash of canonicalized observation record with recordHash field cleared."
        }
      },
      "additionalProperties": true
    },

    "trust": {
      "type": "object",
      "required": ["level", "sourceClass"],
      "properties": {
        "level": { "type": "string", "enum": ["low", "medium", "high", "authoritative"] },
        "sourceClass": {
          "type": "string",
          "enum": [
            "first_party_logged",
            "third_party_api",
            "web_unpinned",
            "human_asserted",
            "derived"
          ]
        },
        "notes": { "type": ["string", "null"], "maxLength": 2000 }
      },
      "additionalProperties": true
    },

    "redaction": {
      "type": "object",
      "required": ["state"],
      "properties": {
        "state": { "type": "string", "enum": ["none", "partial", "full"] },
        "reason": { "type": ["string", "null"], "maxLength": 512 },
        "redactedFields": { "type": ["array", "null"], "items": { "type": "string" } },
        "policy": { "type": ["string", "null"], "maxLength": 64 }
      },
      "additionalProperties": true
    },

    "provenance": {
      "type": "object",
      "required": ["kind", "parents"],
      "properties": {
        "kind": { "type": "string", "enum": ["direct", "derived", "aggregated"] },
        "capture": {
          "type": ["object", "null"],
          "properties": {
            "capture_id": { "type": "string", "minLength": 1, "maxLength": 128 },
            "capture_path": { "type": ["string", "null"], "maxLength": 512 },
            "capture_tool": { "type": ["string", "null"], "maxLength": 128 }
          },
          "additionalProperties": true
        },
        "parents": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["observation_id", "recordHash"],
            "properties": {
              "observation_id": { "type": "string", "pattern": "^OBS-[0-9a-f]{16}$" },
              "recordHash": { "type": "string", "pattern": "^sha256:[0-9a-f]{64}$" }
            },
            "additionalProperties": true
          }
        },
        "derivation": {
          "type": ["object", "null"],
          "properties": {
            "tool": { "type": ["string", "null"], "maxLength": 128 },
            "toolVersion": { "type": ["string", "null"], "maxLength": 64 },
            "method": { "type": ["string", "null"], "maxLength": 128 }
          },
          "additionalProperties": true
        }
      },
      "additionalProperties": true
    },

    "evidence": {
      "type": ["object", "null"],
      "properties": {
        "links": {
          "type": ["array", "null"],
          "items": {
            "type": "object",
            "required": ["kind", "ref"],
            "properties": {
              "kind": { "type": "string", "enum": ["task", "decision", "report", "artifact"] },
              "ref": { "type": "string", "minLength": 1, "maxLength": 512 }
            },
            "additionalProperties": true
          }
        }
      },
      "additionalProperties": true
    }
  },

  "allOf": [
    {
      "if": { "properties": { "source": { "properties": { "kind": { "const": "web_fetch" } } } } },
      "then": {
        "properties": {
          "source": {
            "required": ["subject"],
            "properties": {
              "subject": { "type": "string", "pattern": "^https?://.+", "maxLength": 2048 }
            }
          }
        }
      }
    },
    {
      "if": { "properties": { "source": { "properties": { "kind": { "const": "local_file_change" } } } } },
      "then": {
        "properties": {
          "source": {
            "properties": {
              "eventId": { "type": "string", "pattern": "^[0-9a-f]{7,64}$" }
            }
          }
        }
      }
    }
  ],

  "additionalProperties": true
}
```

### Observation capture schema

This is for **local inbox captures** (raw, possibly sensitive). It lets you normalize deterministically later without letting ad hoc formats proliferate.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://lyra.local/schemas/observation_capture/v1.0.0.schema.json",
  "title": "Observation Capture v1.0.0",
  "type": "object",
  "required": ["artifactType", "schemaVersion", "capture_id", "capturedAt", "source", "payload"],
  "properties": {
    "artifactType": { "type": "string", "const": "observation_capture" },
    "schemaVersion": { "type": "string", "pattern": "^1\\.0\\.0$" },

    "capture_id": { "type": "string", "minLength": 8, "maxLength": 128 },
    "capturedAt": { "type": "string", "format": "date-time" },

    "source": {
      "type": "object",
      "required": ["kind", "system"],
      "properties": {
        "kind": { "type": "string" },
        "system": { "type": "string" },
        "instance": { "type": ["string", "null"] }
      },
      "additionalProperties": true
    },

    "payload": {
      "type": "object",
      "description": "Raw source payload. Source-specific; normalized later.",
      "additionalProperties": true
    },

    "secretsHint": {
      "type": ["string", "null"],
      "enum": ["none", "possible", "likely", null],
      "description": "Quick triage hint for operators/agents; not authoritative."
    }
  },
  "additionalProperties": true
}
```

### Generated observations index schema

This is optional but makes drift checks and consumer tooling easier.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://lyra.local/schemas/observations_index/v1.0.0.schema.json",
  "title": "Observations Index v1.0.0",
  "type": "object",
  "required": ["artifactType", "schemaVersion", "entries", "rootHash"],
  "properties": {
    "artifactType": { "type": "string", "const": "observations_index" },
    "schemaVersion": { "type": "string", "pattern": "^1\\.0\\.0$" },

    "entries": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["observation_id", "observedAt", "kind", "trust", "redaction", "contentHash", "recordHash", "path"],
        "properties": {
          "observation_id": { "type": "string" },
          "observedAt": { "type": "string", "format": "date-time" },
          "kind": { "type": "string" },
          "trust": { "type": "string" },
          "redaction": { "type": "string" },
          "contentHash": { "type": "string" },
          "recordHash": { "type": "string" },
          "path": { "type": "string" }
        },
        "additionalProperties": true
      }
    },

    "rootHash": {
      "type": "string",
      "pattern": "^sha256:[0-9a-f]{64}$",
      "description": "Hash of canonicalized entries list to detect tampering/drift."
    }
  },
  "additionalProperties": true
}
```

## Repo blueprint

This blueprint is intentionally aligned to your current “machine-checkable governance” layout: schema authority + deterministic tooling + knowledge indexes, without modifying runtime semantics. fileciteturn49file0L1-L1 fileciteturn36file0L1-L1

### Files and folders to add

```text
schemas/
  observation/
    v1.0.0.schema.json
  observation_capture/
    v1.0.0.schema.json
  observations_index/
    v1.0.0.schema.json

knowledge/
  observations/
    2026-03/
      (observation JSON envelopes live here)
    blobs/
      sha256/
        (content-addressed blobs live here)
  indexes/
    observations_index.json
    (indexes_manifest.json updated)

knowledge/policies/
  observation_sources.v1.yaml
  observation_retention.v1.yaml

tools/
  observe/
    README.md
    ingest_observations.py
    capture_web.py
    capture_trello_actions.py
    capture_chat_export.py
    capture_git_events.py
    hash_util.py
    validate_observations.py

.github/workflows/
  governance-machine-check.yml  (edit: ensure pyyaml + jsonschema)
```

### Integration rules with TDE and evidence artifacts

These are the minimum rules that make observations “real” in your system, while remaining additive to TDE:

**Rule: observations are not executable inputs.** They can only influence TDE through *linked evidence* (tasks/decisions/reports must cite observations). This mirrors how your current TDE runners treat binding/objective registries as required authority context and fail closed when that context is missing. fileciteturn45file3L1-L1

**Rule: one canonical linking field.** Standardize the following convention across machine-readable JSON artifacts and Markdown frontmatter:

- `evidence.observations[]`: list of objects `{ observation_id, recordHash }`

This avoids bespoke per-artifact linking fields and enables a single CI validator.

**Rule: fail-closed on invalid provenance only at the boundary.**  
A missing/invalid observation is **not** an ingest failure (captures can be incomplete), but it is a **hard failure** if:

- a decision-impacting report claims a decision impact but references an observation that can’t be resolved/verified (parallel to your decision-impact report mapping rule), fileciteturn49file0L1-L1  
- a release envelope or gate packet relies on observation-derived signals (future-facing),  
- any automation script emits an evidence artifact asserting it consumed observations, but the observations don’t validate.

**Rule: evidence artifacts must link what they consumed.**  
For any evidence JSON artifact that includes `evidence.observations`, validators must ensure:

- each observation exists in `knowledge/observations/`,  
- `recordHash` matches the referenced file,  
- redaction state is compatible with the artifact’s confidentiality (v1: enforce by policy file).  

This is fully consistent with your current pattern of validating evidence artifacts against a schema registry and failing CI on drift/invalid artifacts. fileciteturn40file6L1-L1 fileciteturn33file2L1-L1

## Validation matrix

This mirrors the governance posture in your milestone: hard fail on schema/provenance violations and on drift of generated outputs. fileciteturn49file0L1-L1

| Check | Scope | Hard fail | Warning | Notes |
|---|---|---:|---:|---|
| Observation schema validation | `knowledge/observations/**/*.json` | ✅ |  | Requires `artifactType`, `schemaVersion`, required fields; uses JSON Schema Draft 2020-12. citeturn0search0turn0search2 |
| Record hash verification | observations | ✅ |  | Recompute `integrity.recordHash` using deterministic canonicalization (RFC 8785 motivation). citeturn1search0turn0search3 |
| Content hash verification | blobs referenced by observations | ✅* | ⚠️ | Fail if `blob_ref` + blob exists but hash mismatches; warn if blob missing but retention policy allows local-only. citeturn0search3 |
| Provenance parent resolution | derived observations | ✅ |  | Parent observation must exist and hash-match; provenance modeled after W3C PROV derivation concepts. citeturn0search5turn0search7 |
| Source registration | all observations | ✅ |  | Source must exist in `knowledge/policies/observation_sources.v1.yaml` (prevents “ad hoc new source” drift). |
| Redaction policy compliance | all observations | ✅ |  | Enforce “data minimisation” and “storage limitation” policies; start minimal, but make it machine-checkable. citeturn3search0 |
| Observations index drift | generated index file | ✅ |  | Regenerate deterministically and fail if repo drift is present, consistent with your existing drift check style. fileciteturn44file0L1-L1 |
| Evidence artifact observation links | artifacts that declare `evidence.observations` | ✅ |  | Fail if linked observation missing/invalid (fail-closed boundary). fileciteturn45file3L1-L1 |
| Capture schema validation | local inbox captures |  | ⚠️ | Capture files are optional and often local-only; validate when present to curb format sprawl. |
| Large blob guardrails | blobs/ |  | ⚠️ | Warn if blob exceeds size threshold (operator review); prevents accidental repo bloat. |

## MVP milestone checklist

This is a 9-day plan (fits your 7–10 day window) optimized for a solo operator + AI agents, and consistent with “additive governance checks only” as a default posture. fileciteturn49file0L1-L1

### Day 1: Schemas + registry wiring

- Add `schemas/observation/v1.0.0.schema.json`, `schemas/observation_capture/v1.0.0.schema.json`, `schemas/observations_index/v1.0.0.schema.json`.
- Update `schemas/_registry.json` to include:
  - `"observation": { "1.0.0": "schemas/observation/v1.0.0.schema.json" }`
  - `"observations_index": { "1.0.0": "schemas/observations_index/v1.0.0.schema.json" }` fileciteturn40file6L1-L1  
- Add `knowledge/observations/.gitkeep` and `knowledge/observations/blobs/sha256/.gitkeep`.

### Day 2: Hash utilities and canonicalization

- Add `tools/observe/hash_util.py` implementing:
  - `sha256_bytes(b) -> "sha256:<hex>"`
  - `canonical_json(obj) -> bytes` using stable key sorting and minimal separators, inspired by RFC 8785’s determinism requirements. citeturn1search0  
- Add `tools/observe/README.md` documenting:
  - `sorted_json_v1` canonicalization rules,
  - when to use inline vs blob content.

### Day 3: Normalizer core

- Add `tools/observe/ingest_observations.py`:
  - reads capture files from `.openclaw/inbox/observations/**/*.json` (local-only),
  - writes normalized observations to `knowledge/observations/YYYY-MM/`,
  - writes blobs into `knowledge/observations/blobs/sha256/`,
  - enforces idempotency by deterministic `observation_id` derivation (event identity → stable ID), aligned with the general “retry safely” semantics of idempotency. citeturn4search1turn5view0  

### Day 4: Source-specific capture tools

- Add `tools/observe/capture_trello_actions.py`:
  - polls Trello actions (board/org scope), writes one capture file per action (action `id` is the stable event ID). citeturn1search1turn1search3  
  - do **not** implement webhooks in v1 unless you already have a stable local endpoint; polling is simpler and stays local-first.  
- Add `tools/observe/capture_web.py`:
  - fetches a URL and stores response body + metadata in a capture file (snapshot determinism is achieved by storing the bytes you received).  
- Add `tools/observe/capture_chat_export.py`:
  - converts exported chat JSON/JSONL into capture files, preserving original message IDs if present.  
- Add `tools/observe/capture_git_events.py`:
  - records git commit SHAs and file lists as “local_file_change” captures; git’s hash-based object model provides stable identifiers for content and history. citeturn2search0turn2search3  

### Day 5: Observation validator + repo validator integration

- Add `tools/observe/validate_observations.py`:
  - schema validation (via registry),
  - record hash verification,
  - provenance parent checks,
  - blob hash checks (policy-aware).  
- Update `tools/validate_repo.py` to call:
  - observation validation,
  - regenerated indexes drift check (including the new observations index). fileciteturn33file2L1-L1  

### Day 6: Index generation integration

- Extend `tools/gen_knowledge_indexes.py` to also:
  - scan `knowledge/observations/**/*.json`,
  - write `knowledge/indexes/observations_index.json`,
  - update `knowledge/indexes/indexes_manifest.json` to include this output. fileciteturn44file0L1-L1  
- Ensure the index is deterministic: sorted by `(observedAt, observation_id)` and no “generatedAt” fields.

### Day 7: Policy files for trust + retention

- Add `knowledge/policies/observation_sources.v1.yaml` (allowed sources + default trust class).
- Add `knowledge/policies/observation_retention.v1.yaml` (TTL + blob requirements + redaction defaults).
- Add minimal enforcement in `validate_observations.py`:
  - unknown source → hard fail,
  - forbidden redaction state for a source → hard fail,
  - missing blobs with “repo_required” → hard fail.

Use Swedish data protection phrasing as the baseline intent: data minimisation and storage limitation should be enforceable, not aspirational. citeturn3search0

### Day 8: Seed example observations + link validation

- Generate a small set of real observation artifacts:
  - 1 Trello action capture → 1 observation,
  - 1 web capture → 1 observation,
  - 1 git commit capture → 1 observation,
  - 1 chat export capture → 1 observation.
- Add a tiny “evidence link” example:
  - update or add one evidence artifact to include `evidence.observations[]` and validate link checks.

### Day 9: CI hardening + documentation

- Update `.github/workflows/governance-machine-check.yml` to install `pyyaml` if needed (your tooling already imports YAML), and ensure jsonschema is present. fileciteturn51file0L1-L1  
- Update `MILESTONE_0_1_MACHINE_CHECKABLE_GOVERNANCE.md` with:
  - new derivatives generated (observations index),
  - new validations (observations). fileciteturn49file0L1-L1  

## Top failure modes and mitigations

1. **Non-deterministic hashing due to JSON serialization differences**  
   Mitigation: explicitly define canonicalization (`sorted_json_v1`) and hash that representation; RFC 8785 exists specifically because cryptographic hashing/signing needs invariant formats. citeturn1search0  

2. **“Blob missing” makes observations unverifiable across machines**  
   Mitigation: policy-driven blob requirements: allow local-only blobs for sensitive content, but require repo-stored blobs for any observation that is referenced by decision-impacting evidence. (Validator enforces.)  

3. **Ingestion duplicates due to replay / partial failures**  
   Mitigation: deterministic `observation_id` derived from source identity; “already exists” becomes a safe no-op; treat “same ID but different record hash” as a hard conflict, similar to idempotency conflicts in your kernel approach. fileciteturn35file0L1-L1 citeturn4search1turn5view0  

4. **Provenance drift: derived observations fail to cite parents**  
   Mitigation: require parent observation refs (ID + record hash) for any `provenance.kind = derived`; validate parent resolution in CI using W3C PROV-inspired derivation semantics. citeturn0search5turn0search7  

5. **Trust inflation: low-trust web data silently becomes decision input**  
   Mitigation: enforce boundary rules: evidence artifacts referencing observations must enforce minimum trust level; missing or low-trust inputs cause fail-closed behavior, matching your TDE stance on missing authority context. fileciteturn45file3L1-L1  

6. **Redaction regressions (PII/secrets leak into committed blobs)**  
   Mitigation: default-deny for high-risk sources; enforce “redaction.state != none” for selected sources; align retention/redaction rules with “data minimisation” and “storage limitation” principles. citeturn3search0  

7. **Index drift / CI noise from volatile fields**  
   Mitigation: indexes must not include generation timestamps; sort deterministically; follow the existing “regen must be clean” pattern. fileciteturn44file0L1-L1 fileciteturn49file0L1-L1  

8. **Trello sync loops or ambiguous action coverage**  
   Mitigation: action polling uses Trello action IDs as stable event identities; if you later add webhooks, use Trello’s documented webhook payload structure and the `X-Trello-Client-Identifier` loop-avoidance header strategy. citeturn1search1turn1search3  

## Copy-paste starter templates

### Example observation JSON

```json
{
  "artifactType": "observation",
  "schemaVersion": "1.0.0",

  "observation_id": "OBS-4f3a9c2e1d0b7a11",
  "observedAt": "2026-03-04T10:15:12Z",
  "ingestedAt": "2026-03-04T10:16:03Z",

  "source": {
    "kind": "task_board_event",
    "system": "trello",
    "instance": "board:6a1b2c3d4e5f",
    "subject": "card:51a79e72dbb7e23c7c003778",
    "eventId": "51f9424bcd6e040f3c002412",
    "captureMethod": "api_poll",
    "actor": { "kind": "human", "id": "member:4fc78a59a885233f4b349bd9" }
  },

  "content": {
    "contentType": "application/json",
    "preview": "{\"type\":\"voteOnCard\",\"card\":\"Webhooks\"...}",
    "storage": {
      "mode": "blob_ref",
      "blobPath": "knowledge/observations/blobs/sha256/3a1f...c9.json",
      "encoding": "utf-8",
      "sizeBytes": 1821
    }
  },

  "integrity": {
    "hashAlgorithm": "sha256",
    "canonicalization": "sorted_json_v1",
    "contentHash": "sha256:3a1f0bb2e1f0c52ac4d24f7d5c2b6f8e7d6c4a1b0f2e3d4c5b6a7c8d9e0f1ac9",
    "recordHash": "sha256:6c2b0b9b0c57c7f3b73d6b7dfd9e43d3d5a8e2d5c6f0a7b1d2c3e4f5a6b7c8d9"
  },

  "trust": {
    "level": "high",
    "sourceClass": "third_party_api",
    "notes": "Pulled from Trello actions feed; stable action id."
  },

  "redaction": {
    "state": "none",
    "policy": "obs_redaction_v1"
  },

  "provenance": {
    "kind": "direct",
    "capture": {
      "capture_id": "cap-20260304-101603-trello-51f9424b",
      "capture_path": ".openclaw/inbox/observations/trello/cap-20260304-101603-trello-51f9424b.json",
      "capture_tool": "tools/observe/capture_trello_actions.py"
    },
    "parents": [],
    "derivation": null
  },

  "evidence": {
    "links": [
      { "kind": "task", "ref": "OPS-2026-123 | Investigate Trello webhook loop" }
    ]
  }
}
```

### Source registry YAML

```yaml
version: 1
sources:
  trello:
    allowed_kinds: ["task_board_event"]
    default_trust:
      sourceClass: third_party_api
      level: high
    redaction:
      default_state: partial
      required_for_commit: true
    retention:
      blob_policy: repo_required

  web:
    allowed_kinds: ["web_fetch", "web_search"]
    default_trust:
      sourceClass: web_unpinned
      level: medium
    redaction:
      default_state: none
      required_for_commit: false
    retention:
      blob_policy: repo_optional

  git:
    allowed_kinds: ["local_file_change"]
    default_trust:
      sourceClass: first_party_logged
      level: authoritative
    redaction:
      default_state: none
      required_for_commit: true
    retention:
      blob_policy: repo_optional
```

### Python pseudocode: deterministic hashing and record hash

```python
# tools/observe/hash_util.py (pseudocode)
import hashlib
import json
from typing import Any

def canonical_json_sorted_v1(obj: Any) -> bytes:
    """
    Deterministic JSON serialization:
    - sort object keys
    - no whitespace
    - UTF-8 output
    - avoid floats in canonical fields (store floats as strings upstream)
    Motivated by RFC 8785's requirement for invariant formats.
    """
    return json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")

def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def sha256_tagged(data: bytes) -> str:
    return "sha256:" + sha256_hex(data)

def compute_record_hash(observation: dict) -> str:
    obs_copy = dict(observation)
    integrity = dict(obs_copy.get("integrity", {}))
    integrity["recordHash"] = None
    obs_copy["integrity"] = integrity
    payload = canonical_json_sorted_v1(obs_copy)
    return sha256_tagged(payload)
```

### Python pseudocode: idempotent ingestion loop

```python
# tools/observe/ingest_observations.py (pseudocode)
from pathlib import Path
import json

def deterministic_obs_id(kind: str, system: str, instance: str | None, event_id: str) -> str:
    key = f"{kind}|{system}|{instance or ''}|{event_id}".encode("utf-8")
    h = sha256_hex(key)[:16]
    return f"OBS-{h}"

def ingest_one_capture(capture_path: Path) -> dict:
    cap = json.loads(capture_path.read_text(encoding="utf-8"))

    # Normalize core fields
    src = cap["source"]
    kind = src["kind"]
    system = src["system"]
    instance = src.get("instance")
    event_id = src["eventId"]  # enforce in capture for sources we care about

    obs_id = deterministic_obs_id(kind, system, instance, event_id)

    observed_at = cap.get("payload", {}).get("date") or cap["capturedAt"]

    blob_bytes = extract_blob_bytes(cap)  # source-specific
    content_hash = sha256_tagged(blob_bytes)
    blob_path = Path(f"knowledge/observations/blobs/sha256/{content_hash.split(':',1)[1]}.bin")
    atomic_write(blob_path, blob_bytes)

    obs = {
        "artifactType": "observation",
        "schemaVersion": "1.0.0",
        "observation_id": obs_id,
        "observedAt": observed_at,
        "ingestedAt": cap["capturedAt"],
        "source": {
            "kind": kind,
            "system": system,
            "instance": instance,
            "eventId": event_id,
            "captureMethod": src.get("captureMethod", "export"),
        },
        "content": {
            "contentType": "application/octet-stream",
            "storage": {"mode": "blob_ref", "blobPath": str(blob_path), "encoding": "base64"}
        },
        "integrity": {
            "hashAlgorithm": "sha256",
            "canonicalization": "sorted_json_v1",
            "contentHash": content_hash,
            "recordHash": None,
        },
        "trust": default_trust_for(system),
        "redaction": default_redaction_for(system),
        "provenance": {
            "kind": "direct",
            "capture": {"capture_id": cap["capture_id"], "capture_path": str(capture_path)},
            "parents": [],
        },
    }

    obs["integrity"]["recordHash"] = compute_record_hash(obs)

    out_path = obs_output_path(obs)  # knowledge/observations/YYYY-MM/YYYY-MM-DD__obs__...json
    if out_path.exists():
        existing = json.loads(out_path.read_text(encoding="utf-8"))
        if existing["integrity"]["recordHash"] != obs["integrity"]["recordHash"]:
            raise RuntimeError(f"idempotency_conflict: {out_path}")
        return {"status": "replay", "path": str(out_path)}

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(obs, indent=2) + "\n", encoding="utf-8")
    return {"status": "created", "path": str(out_path)}
```

### Validator hook snippet for `tools/validate_repo.py`

```python
# tools/validate_repo.py (pseudocode, additive)
def main():
    # existing steps: gen_inventory, gen_knowledge_indexes, change policy checks...
    # then:
    validate_observations()        # new
    validate_observation_links()   # new boundary rule (fail-closed)
    check_drift([... add observations_index.json ...])
```

### Evidence artifact linking template

```json
{
  "artifactType": "tde_job_tick",
  "schemaVersion": "1.0.0",
  "tick_id": "job-tick-20260304-101500",
  "timestamp": "2026-03-04T10:15:00Z",

  "evidence": {
    "observations": [
      { "observation_id": "OBS-4f3a9c2e1d0b7a11", "recordHash": "sha256:6c2b0b9b0c57c7f3b..." }
    ]
  }
}
```