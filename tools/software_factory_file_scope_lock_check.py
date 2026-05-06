#!/usr/bin/env python3
"""Validate Software Factory file-scope locks before parallel builder dispatch.

This helper is intentionally small and fail-closed. It accepts a JSON manifest
that declares the factory run, each worker's worktree/branch identity, and the
write scopes each worker is allowed to touch. It rejects ambiguous path syntax,
missing isolation/naming evidence, overlapping write scopes, and changed files
outside a worker's lock.
"""
from __future__ import annotations

import argparse
import json
import posixpath
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

ARTIFACT_TYPE = "software_factory_file_scope_locks"
SCHEMA_VERSION = "0.1.0"
VALID_MODES = {"create", "modify", "delete", "replace"}
VALID_SCOPE_TYPES = {"file", "directory"}
BRANCH_RE = re.compile(r"^sf/[a-z0-9][a-z0-9._-]*/[a-z0-9][a-z0-9._-]*$")
WILDCARD_RE = re.compile(r"[*?\[\]]")


@dataclass(frozen=True)
class Scope:
    worker_id: str
    path: str
    scope_type: str
    mode: str


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def slug(value: str) -> str:
    lowered = value.strip().lower()
    cleaned = re.sub(r"[^a-z0-9._-]+", "-", lowered)
    cleaned = re.sub(r"-+", "-", cleaned).strip("-._")
    return cleaned


def normalize_rel_path(value: Any, label: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label}: path must be a non-empty string")
        return ""
    raw = value.strip().replace("\\", "/")
    if raw.startswith("/"):
        errors.append(f"{label}: absolute paths are not allowed: {value}")
        return ""
    if WILDCARD_RE.search(raw):
        errors.append(f"{label}: wildcard/glob paths are not allowed: {value}")
        return ""
    norm = posixpath.normpath(raw)
    if norm in {".", ""} or norm == ".." or norm.startswith("../"):
        errors.append(f"{label}: path must stay inside the workspace: {value}")
        return ""
    if norm.startswith("./"):
        norm = norm[2:]
    return norm.rstrip("/")


def is_same_or_descendant(parent: str, child: str) -> bool:
    return child == parent or child.startswith(parent + "/")


def scopes_overlap(left: Scope, right: Scope) -> bool:
    if left.path == right.path:
        return True
    # Fail closed on parent/child relationships. Even a nominal file lock on a
    # parent path conflicts with descendants because filesystem type is not
    # known at dispatch time.
    return is_same_or_descendant(left.path, right.path) or is_same_or_descendant(right.path, left.path)


def scope_contains(scope: Scope, path: str) -> bool:
    if scope.scope_type == "file":
        return path == scope.path
    return is_same_or_descendant(scope.path, path)


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"lock manifest not found: {path}") from None
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from None
    if not isinstance(data, dict):
        raise ValueError(f"lock manifest root must be an object: {path}")
    return data


def validate_manifest(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    if data.get("artifactType") != ARTIFACT_TYPE:
        errors.append(f"artifactType must be {ARTIFACT_TYPE}")
    if data.get("schemaVersion") != SCHEMA_VERSION:
        errors.append(f"schemaVersion must be {SCHEMA_VERSION}")

    factory_run_id = data.get("factory_run_id")
    if not isinstance(factory_run_id, str) or not factory_run_id.strip():
        errors.append("factory_run_id must be a non-empty string")
        run_slug = ""
    else:
        run_slug = slug(factory_run_id)
        if not run_slug:
            errors.append("factory_run_id must contain at least one slug-safe character")

    workers = data.get("workers")
    if not isinstance(workers, list) or len(workers) < 1:
        errors.append("workers must be a non-empty list")
        return errors

    worker_ids: set[str] = set()
    branches: set[str] = set()
    worktrees: set[str] = set()
    all_scopes: list[Scope] = []
    scopes_by_worker: dict[str, list[Scope]] = {}

    for idx, worker in enumerate(workers):
        label = f"workers[{idx}]"
        if not isinstance(worker, dict):
            errors.append(f"{label}: worker must be an object")
            continue

        worker_id = worker.get("worker_id")
        if not isinstance(worker_id, str) or not worker_id.strip():
            errors.append(f"{label}.worker_id must be a non-empty string")
            continue
        worker_id = worker_id.strip()
        worker_slug = slug(worker_id)
        if not worker_slug:
            errors.append(f"{label}.worker_id must contain at least one slug-safe character")
        if worker_id in worker_ids:
            errors.append(f"duplicate worker_id: {worker_id}")
        worker_ids.add(worker_id)

        branch = worker.get("branch")
        if not isinstance(branch, str) or not branch.strip():
            errors.append(f"{label}.branch must be a non-empty string")
        else:
            branch = branch.strip()
            expected_prefix = f"sf/{run_slug}/" if run_slug else "sf/"
            if not BRANCH_RE.match(branch):
                errors.append(f"{label}.branch must match sf/<factory-run-slug>/<worker-slug>: {branch}")
            if run_slug and not branch.startswith(expected_prefix):
                errors.append(f"{label}.branch must start with {expected_prefix}: {branch}")
            if worker_slug and not branch.endswith(f"/{worker_slug}"):
                errors.append(f"{label}.branch must end with worker slug /{worker_slug}: {branch}")
            if branch in branches:
                errors.append(f"duplicate branch: {branch}")
            branches.add(branch)

        worktree = normalize_rel_path(worker.get("worktree_path"), f"{label}.worktree_path", errors)
        if worktree:
            lowered_worktree = worktree.lower()
            if run_slug and run_slug not in lowered_worktree:
                errors.append(f"{label}.worktree_path must include factory run slug {run_slug}: {worktree}")
            if worker_slug and worker_slug not in lowered_worktree:
                errors.append(f"{label}.worktree_path must include worker slug {worker_slug}: {worktree}")
            if worktree in worktrees:
                errors.append(f"duplicate worktree_path: {worktree}")
            worktrees.add(worktree)

        result_path = normalize_rel_path(worker.get("assigned_result_path"), f"{label}.assigned_result_path", errors)
        if result_path and not result_path.endswith(".md"):
            errors.append(f"{label}.assigned_result_path should be a markdown worker result path: {result_path}")

        raw_scopes = worker.get("write_scopes")
        if not isinstance(raw_scopes, list) or not raw_scopes:
            errors.append(f"{label}.write_scopes must be a non-empty list")
            continue

        worker_scopes: list[Scope] = []
        for scope_idx, raw_scope in enumerate(raw_scopes):
            scope_label = f"{label}.write_scopes[{scope_idx}]"
            if not isinstance(raw_scope, dict):
                errors.append(f"{scope_label}: scope must be an object")
                continue
            path = normalize_rel_path(raw_scope.get("path"), f"{scope_label}.path", errors)
            scope_type = raw_scope.get("scope_type", raw_scope.get("kind", "file"))
            if scope_type not in VALID_SCOPE_TYPES:
                errors.append(f"{scope_label}.scope_type must be one of {sorted(VALID_SCOPE_TYPES)}")
                scope_type = "file"
            mode = raw_scope.get("mode")
            if mode not in VALID_MODES:
                errors.append(f"{scope_label}.mode must be one of {sorted(VALID_MODES)}")
                mode = "modify"
            if path:
                scope = Scope(worker_id=worker_id, path=path, scope_type=scope_type, mode=mode)
                worker_scopes.append(scope)
                all_scopes.append(scope)

        changed_files = worker.get("changed_files", [])
        if changed_files is None:
            changed_files = []
        if not isinstance(changed_files, list) or not all(isinstance(item, str) and item.strip() for item in changed_files):
            errors.append(f"{label}.changed_files must be a list of strings when present")
        else:
            for changed_idx, changed in enumerate(changed_files):
                changed_path = normalize_rel_path(changed, f"{label}.changed_files[{changed_idx}]", errors)
                if changed_path and not any(scope_contains(scope, changed_path) for scope in worker_scopes):
                    errors.append(f"{label}.changed_files[{changed_idx}] is outside declared write scopes: {changed_path}")

        read_only = worker.get("read_only_paths", [])
        if read_only is None:
            read_only = []
        if not isinstance(read_only, list) or not all(isinstance(item, str) and item.strip() for item in read_only):
            errors.append(f"{label}.read_only_paths must be a list of strings when present")
        else:
            read_only_paths = [normalize_rel_path(item, f"{label}.read_only_paths", errors) for item in read_only]
            for readonly_path in read_only_paths:
                if readonly_path and any(scope_contains(scope, readonly_path) or is_same_or_descendant(readonly_path, scope.path) for scope in worker_scopes):
                    errors.append(f"{label}.read_only_paths overlaps this worker's write scope: {readonly_path}")

        scopes_by_worker[worker_id] = worker_scopes

    for left_idx, left in enumerate(all_scopes):
        for right in all_scopes[left_idx + 1 :]:
            if left.worker_id == right.worker_id:
                continue
            if scopes_overlap(left, right):
                errors.append(
                    "write scope overlap: "
                    f"{left.worker_id}:{left.path} ({left.scope_type}) conflicts with "
                    f"{right.worker_id}:{right.path} ({right.scope_type})"
                )

    # A result path is a worker-owned write surface even if not listed in write_scopes.
    # It must still be unique to avoid cross-worker result overwrites.
    result_paths: set[str] = set()
    for idx, worker in enumerate(workers):
        if not isinstance(worker, dict):
            continue
        result_path = normalize_rel_path(worker.get("assigned_result_path"), f"workers[{idx}].assigned_result_path", [])
        if result_path:
            if result_path in result_paths:
                errors.append(f"duplicate assigned_result_path: {result_path}")
            result_paths.add(result_path)

    return errors


def validate_manifest_path(path: Path) -> list[str]:
    return validate_manifest(load_manifest(path))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a Software Factory file-scope lock JSON manifest")
    parser.add_argument("manifest", nargs="+", help="Path(s) to file-scope lock JSON manifests")
    args = parser.parse_args(argv)

    had_errors = False
    for raw in args.manifest:
        path = Path(raw)
        if not path.is_absolute():
            path = ROOT / path
        try:
            errors = validate_manifest_path(path)
        except ValueError as exc:
            print(f"[FAIL] {exc}")
            had_errors = True
            continue
        if errors:
            print(f"[FAIL] Software Factory file-scope lock check failed: {rel(path)}")
            for error in errors:
                print(f"- {error}")
            had_errors = True
        else:
            print(f"[PASS] Software Factory file-scope lock check passed: {rel(path)}")
    return 1 if had_errors else 0


if __name__ == "__main__":
    sys.exit(main())
