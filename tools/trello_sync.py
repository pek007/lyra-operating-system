#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Dict, List, Tuple

LIST_ORDER = ["Inbox", "Triage", "Active", "Waiting", "Done", "Archived"]
ID_RE = re.compile(r"^([A-Z]+-\d{4}-\d{3})\b")


@dataclass
class TaskItem:
    list_name: str
    title: str
    checked: bool
    key: str


def parse_tasks_md(path: str) -> List[TaskItem]:
    items: List[TaskItem] = []
    current = None
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            h = re.match(r"^##\s+(.+)$", line.strip())
            if h:
                current = h.group(1).strip()
                continue
            m = re.match(r"^- \[( |x|X)\] (.+)$", line.strip())
            if m and current in LIST_ORDER:
                title = m.group(2).strip()
                checked = m.group(1).lower() == "x"
                k = title
                idm = ID_RE.match(title)
                if idm:
                    k = idm.group(1)
                items.append(TaskItem(current, title, checked, k))
    return items


class TrelloClient:
    def __init__(self, key: str, token: str):
        self.key = key
        self.token = token

    def _request(self, method: str, path: str, params=None):
        params = params or {}
        params["key"] = self.key
        params["token"] = self.token
        qs = urllib.parse.urlencode(params)
        url = f"https://api.trello.com/1{path}?{qs}"
        req = urllib.request.Request(url=url, method=method)
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def get_lists(self, board_id: str):
        return self._request("GET", f"/boards/{board_id}/lists", {"cards": "none", "filter": "open"})

    def create_list(self, board_id: str, name: str):
        return self._request("POST", "/lists", {"idBoard": board_id, "name": name})

    def get_cards(self, board_id: str):
        return self._request("GET", f"/boards/{board_id}/cards", {"filter": "open", "fields": "name,idList"})

    def create_card(self, list_id: str, name: str):
        return self._request("POST", "/cards", {"idList": list_id, "name": name})

    def move_card(self, card_id: str, list_id: str):
        return self._request("PUT", f"/cards/{card_id}", {"idList": list_id})

    def get_labels(self, board_id: str):
        return self._request("GET", f"/boards/{board_id}/labels", {"fields": "name,color"})

    def create_label(self, board_id: str, name: str, color: str):
        return self._request("POST", "/labels", {"idBoard": board_id, "name": name, "color": color})


def ensure_lists(client: TrelloClient, board_id: str, apply: bool) -> Dict[str, str]:
    existing = {l["name"]: l["id"] for l in client.get_lists(board_id)}
    for name in LIST_ORDER:
        if name not in existing:
            print(f"[plan] create list: {name}")
            if apply:
                obj = client.create_list(board_id, name)
                existing[name] = obj["id"]
    # refresh to catch position/order after creates
    if apply:
        existing = {l["name"]: l["id"] for l in client.get_lists(board_id)}
    return existing


def index_cards(cards) -> Dict[str, dict]:
    idx = {}
    for c in cards:
        key = c["name"]
        m = ID_RE.match(c["name"])
        if m:
            key = m.group(1)
        idx[key] = c
    return idx


def sync_tasks(client: TrelloClient, board_id: str, tasks: List[TaskItem], list_ids: Dict[str, str], apply: bool):
    cards = client.get_cards(board_id)
    card_idx = index_cards(cards)

    for t in tasks:
        desired_list_id = list_ids[t.list_name]
        card = card_idx.get(t.key)
        if not card:
            print(f"[plan] create card in {t.list_name}: {t.title}")
            if apply:
                client.create_card(desired_list_id, t.title)
            continue
        # optional rename if title changed for same ID key
        if card["idList"] != desired_list_id:
            print(f"[plan] move card {card['name']} -> {t.list_name}")
            if apply:
                client.move_card(card["id"], desired_list_id)


def ensure_labels(client: TrelloClient, board_id: str, apply: bool):
    wanted = [
        ("P1 Critical", "red"),
        ("P2 Important", "orange"),
        ("P3 Normal", "blue"),
        ("P4 Nice-to-have", "green"),
        ("Type 1", "purple"),
        ("Type 2", "sky"),
        ("Blocked", "black"),
    ]
    existing = {(l.get("name") or "").strip().lower() for l in client.get_labels(board_id)}
    for name, color in wanted:
        if name.lower() not in existing:
            print(f"[plan] create label: {name} ({color})")
            if apply:
                client.create_label(board_id, name, color)


def main():
    ap = argparse.ArgumentParser(description="Sync TASKS.md -> Trello board")
    ap.add_argument("--from", dest="from_path", default="TASKS.md", help="Path to TASKS markdown")
    ap.add_argument("--apply", action="store_true", help="Apply changes (default dry-run)")
    ap.add_argument("--ensure-labels", action="store_true", help="Ensure standard labels exist")
    args = ap.parse_args()

    key = os.getenv("TRELLO_KEY")
    token = os.getenv("TRELLO_TOKEN")
    board_id = os.getenv("TRELLO_BOARD_ID")

    if not key or not token or not board_id:
        print("Missing env vars. Required: TRELLO_KEY, TRELLO_TOKEN, TRELLO_BOARD_ID", file=sys.stderr)
        sys.exit(2)

    tasks = parse_tasks_md(args.from_path)
    if not tasks:
        print(f"No syncable tasks found in {args.from_path}.")
        sys.exit(1)

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"Mode: {mode}")
    print(f"Tasks parsed: {len(tasks)}")

    client = TrelloClient(key, token)
    list_ids = ensure_lists(client, board_id, args.apply)

    if args.ensure_labels:
        ensure_labels(client, board_id, args.apply)

    sync_tasks(client, board_id, tasks, list_ids, args.apply)
    print("Done.")


if __name__ == "__main__":
    main()
