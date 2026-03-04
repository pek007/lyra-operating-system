#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
from typing import Any


def canonical_json_sorted_v1(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha256_tagged(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def compute_record_hash(observation: dict) -> str:
    copy = json.loads(json.dumps(observation))
    integ = dict(copy.get("integrity", {}))
    integ["recordHash"] = None
    copy["integrity"] = integ
    return sha256_tagged(canonical_json_sorted_v1(copy))
