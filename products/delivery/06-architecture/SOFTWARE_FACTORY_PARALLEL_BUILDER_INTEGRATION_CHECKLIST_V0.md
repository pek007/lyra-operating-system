# Software Factory Parallel Builder Integration Checklist v0

Status: draft v0 / isolated-copy builder output
Factory run ID: `SF-ORCH-2026-05-06-PHASE3B-ISOLATED-PARALLEL-BUILDERS`
Owner/reviewer: Peter Eklind / Lyra Operations
Scope: checklist for Integrator intake of outputs from independent isolated-copy builders

## Purpose

This checklist gives the Integrator a repeatable v0 sequence for combining artifacts produced by parallel Software Factory builders without losing isolation, provenance, or authority boundaries.

## Authority Boundary

The Integrator may inspect, compare, and adopt builder outputs into the designated root/final artifact location only when the factory run assigns that responsibility. This checklist does not authorize credentials/access changes, external sends, deploys, releases, pushes, merges, destructive cleanup, persistent agents, or mutation of prohibited products or client/customer data.

## Integration Checklist

### 1. Confirm intake package

- [ ] Confirm each builder has an assigned role packet, assigned artifact path, and assigned worker result path.
- [ ] Confirm a pre-dispatch file-scope lock manifest exists for parallel builder lanes, or record why the run is serial/manual-only.
- [ ] Confirm `python3 tools/software_factory_file_scope_lock_check.py <lock-manifest.json>` passed before dispatch when parallel builders are used.
- [ ] Confirm each worker result follows `products/delivery/06-architecture/SOFTWARE_FACTORY_WORKER_RESULT_CONTRACT_V0.md`.
- [ ] Confirm each changed file is inside that builder's allowed isolated-copy/result scope.
- [ ] Confirm every builder states an authority boundary and recommended integration state.

### 2. Capture pre-integration manifest

Before adopting any builder output, record a pre-integration manifest for the root/final target area:

- target artifact path(s) and current existence state;
- current checksum or `git diff -- <target>` state when available;
- source builder artifact paths;
- source worker result paths;
- validation command(s) expected for the run.

### 3. Review scoped diffs

For each builder output:

- [ ] Compare the builder artifact against the nearest baseline or intended root target.
- [ ] Inspect only the builder's assigned artifact and result paths unless the role packet authorizes more.
- [ ] Check that the output satisfies the builder packet's required content.
- [ ] Note any semantic overlap with other builders before copying or merging text.

### 4. Check for conflicts

Resolve or escalate before integration if any of these appear:

- two builders edit the same final artifact section with incompatible intent;
- one builder's output assumes files, schemas, credentials, deploys, external sends, or product mutations outside the run scope;
- worker results disagree on validation status or authority boundaries;
- generated output is mixed with hand-authored architecture text without provenance;
- a builder recommends `needs-fix`, `blocked`, `reject`, or an unexplained `needs-review` state.

### 5. Contain generated outputs

- [ ] Keep generated or worker-produced artifacts inside the assigned isolated copy until Integrator adoption.
- [ ] Do not overwrite root/final artifacts directly from a worker lane.
- [ ] Preserve source paths and worker result references in integration evidence.
- [ ] If generated material requires cleanup or normalization, document the transformation in handoff evidence.

### 6. Apply validation in order

Recommended v0 order:

1. Validate the file-scope lock manifest with `tools/software_factory_file_scope_lock_check.py` before dispatch or before late integration if the manifest was created retrospectively.
2. Validate each individual worker result for required sections and scoped changed files.
3. Inspect each builder artifact against its packet acceptance criteria.
4. Perform conflict review across all builder artifacts selected for integration.
5. Adopt selected content into the Integrator-owned root/final target.
6. Run the factory validation command supplied by the role packet or owning lane.
7. Re-check final root/final target diff and evidence file before marking the run complete.

### 7. Capture post-integration manifest

After adoption, record:

- integrated root/final artifact path(s);
- source builder artifact path(s) consumed;
- source worker result path(s) consumed;
- final validation command and result;
- any conflicts resolved, deferred, or escalated;
- final authority boundary confirmation.

## Handoff Evidence Minimum

The integration evidence should include:

- pre-integration manifest summary;
- post-integration manifest summary;
- list of consumed builder outputs and worker results;
- exact validation command(s) run and summarized output;
- explicit statement that prohibited actions were not taken;
- final integration recommendation or blocker for the owner/reviewer.

## Recommended v0 Outcome

Use this checklist as an advisory gate before integrating parallel-builder outputs. Final authority remains with the assigned Integrator, human owner/reviewer, and designated quality gate for the factory run.
