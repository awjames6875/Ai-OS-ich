"""
build_question_bank.py — mines the day's keepers for real questions people asked.
60% DETERMINISTIC. No AI. In-house AnswerThePublic built from actual Redditors.

Run after each pipeline run (keepers.json is overwritten daily — that's why we archive):
    python build_question_bank.py

Reads   2_sort-the-keepers/output/keepers.json
Updates content/question-bank.json  (grows forever; dedupes; times_seen = demand signal)
Writes  content/question-bank.md    (human view, grouped by funnel)
"""

import json
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]          # content/
PROJECT = BASE.parent
KEEPERS = PROJECT / "2_sort-the-keepers" / "output" / "keepers.json"
BANK_JSON = BASE / "question-bank.json"
BANK_MD = BASE / "question-bank.md"

QUESTION_STARTERS = (
    "how ", "what ", "why ", "when ", "where ", "should ", "can ", "is it ",
    "is my ", "does anyone", "has anyone", "am i ", "do i ", "anyone else",
)


def is_question(title: str) -> bool:
    low = title.lower().strip()
    return low.endswith("?") or low.startswith(QUESTION_STARTERS)


def norm(title: str) -> str:
    """Dedup key: lowercase, no trailing punctuation, collapsed spaces."""
    return " ".join(title.lower().strip().rstrip("?!. ").split())


def load_bank() -> dict:
    if not BANK_JSON.exists():
        return {}
    return {norm(e["question"]): e for e in json.loads(BANK_JSON.read_text(encoding="utf-8"))}


def render_md(entries: list) -> str:
    today = date.today().isoformat()
    lines = [
        "# Question Bank — real questions from real Redditors",
        "",
        f"Updated: {today} · {len(entries)} questions · sorted by demand (times_seen)",
        "Use the EXACT phrasing below in blog H2s and FAQs — it's how people ask AI engines too.",
        "",
    ]
    groups = [("BOFU", "BOFU — ready to seek help"), ("MOFU", "MOFU — comparing options"),
              ("TOFU", "TOFU — is this normal?"), (None, "Unsorted — no funnel match yet")]
    for funnel, heading in groups:
        rows = [e for e in entries if e.get("funnel") == funnel]
        if not rows:
            continue
        lines.append(f"## {heading}")
        for e in rows:
            lines.append(f'- "{e["question"]}" (r/{e["subreddit"]}, seen {e["times_seen"]}x)')
        lines.append("")
    return "\n".join(lines)


def main():
    if not KEEPERS.exists():
        print(f"No keepers at {KEEPERS}. Run the pipeline (Rooms 1-2) first.")
        return

    bank = load_bank()
    today = date.today().isoformat()
    added = updated = 0

    for post in json.loads(KEEPERS.read_text(encoding="utf-8")):
        title = (post.get("title") or "").strip()
        if not title or not is_question(title):
            continue
        key = norm(title)
        if key in bank:
            bank[key]["times_seen"] += 1
            bank[key]["last_seen"] = today
            updated += 1
        else:
            bank[key] = {
                "question": title,
                "subreddit": post.get("subreddit", ""),
                "audience": post.get("audience", "general"),
                "funnel": post.get("funnel"),
                "matched_query": post.get("matched_query"),
                "first_seen": today,
                "last_seen": today,
                "times_seen": 1,
            }
            added += 1

    entries = sorted(bank.values(), key=lambda e: -e["times_seen"])
    BANK_JSON.write_text(json.dumps(entries, indent=2), encoding="utf-8")
    BANK_MD.write_text(render_md(entries), encoding="utf-8")
    print(f"Question bank: +{added} new, {updated} repeats bumped, {len(entries)} total.")
    print(f"Wrote {BANK_JSON.name} and {BANK_MD.name} in content/.")


if __name__ == "__main__":
    main()
