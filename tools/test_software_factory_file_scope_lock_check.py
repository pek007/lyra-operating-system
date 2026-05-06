#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "tools/software_factory_file_scope_lock_check.py"
FIXTURE_DIR = ROOT / "tools/fixtures/software_factory_file_scope_locks"

spec = importlib.util.spec_from_file_location("software_factory_file_scope_lock_check", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


def assert_pass(name: str, fixture: str) -> None:
    errors = validator.validate_manifest_path(FIXTURE_DIR / fixture)
    if errors:
        raise AssertionError(f"{name} expected pass, got errors: {errors}")
    print(f"PASS {name}")


def assert_fail_contains(name: str, fixture: str, needle: str) -> None:
    errors = validator.validate_manifest_path(FIXTURE_DIR / fixture)
    joined = "\n".join(errors)
    if needle not in joined:
        raise AssertionError(f"{name} expected error containing {needle!r}, got: {errors}")
    print(f"PASS {name}")


def main() -> int:
    assert_pass("non-overlapping builder scopes", "pass-non-overlap.json")
    assert_fail_contains("overlapping directory/file scopes", "fail-overlap.json", "write scope overlap")
    assert_fail_contains("bad worktree/branch naming", "fail-naming.json", "branch must match")
    assert_fail_contains("changed file outside lock", "fail-changed-file.json", "outside declared write scopes")
    print("[PASS] Software Factory file-scope lock checker tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
