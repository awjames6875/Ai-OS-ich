"""
sort_posts.py — Room 2: Sort The Keepers
60% DETERMINISTIC. No AI. Applies keep/skip rules, tags each keeper.

Reads output/raw-posts.json.
Saves output/keepers.json.
"""

import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
RAW = BASE.parent / "1_find-the-posts" / "output" / "raw-posts.json"
OUTPUT = BASE / "output" / "keepers.json"

# --- Rules (pulled from config in a real run) ---
MAX_AGE_HOURS = 24 * 8          # drop posts older than ~8 days
MAX_COMMENTS = 40               # drop posts already heavily answered
MIN_BODY_LEN = 40              # drop empty / one-line posts

# Subreddits where brand may NEVER be mentioned (value-only)
VALUE_ONLY_SUBS = {
    "ECEprofessionals", "oklahoma", "tulsa", "okc",
    "toddlers", "daddit", "Mommit",
}

# Simple audience tagging by keyword
AUDIENCE_KEYWORDS = {
    "parent": ["my son", "my daughter", "my kid", "my child", "toddler", "my teen"],
    "recovery": ["sober", "recovery", "relapse", "addiction", "clean time"],
    "reentry": ["prison", "incarcerated", "reentry", "released", "felony"],
}

# Target queries from the AEO report (UNTAPPED + competitor-gap). A post matching ANY row
# gets priority=true and inherits the row's funnel stage (TOFU/MOFU/BOFU).
TARGET_QUERIES_FILE = Path(
    r"C:\Users\1alph\.claude\skills\safeharbor-reddit-triage\references\target-queries.md"
)


def load_target_queries():
    """Parse the target-queries.md table -> [{query, funnel}]. Empty list if file missing."""
    if not TARGET_QUERIES_FILE.exists():
        return []
    rows = []
    for line in TARGET_QUERIES_FILE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or set(line.strip()) <= {"|", "-", " ", ":"}:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 3 and cells[0].lower() != "query":
            rows.append({"query": cells[0], "funnel": cells[2].upper()})
    return rows


def match_target_query(text: str, target_queries: list):
    """Match if every significant word of a target query appears as a WHOLE word.

    Two guards against false positives (2026-07-07 review):
    - whole-word match, not substring ("care" must not match "careful"/"daycare")
    - queries with fewer than 2 significant words are skipped ("family and" -> just
      "family" would flag nearly every parenting post as priority)
    """
    post_words = set(re.findall(r"[a-z]+", text.lower()))
    for tq in target_queries:
        words = [w for w in re.findall(r"[a-z]+", tq["query"].lower()) if len(w) >= 4]
        if len(words) >= 2 and all(w in post_words for w in words):
            return tq
    return None


def tag_audience(text: str) -> str:
    low = text.lower()
    for audience, words in AUDIENCE_KEYWORDS.items():
        if any(w in low for w in words):
            return audience
    return "general"


def is_keeper(post: dict) -> bool:
    body = post.get("body", "") or ""
    if len(body) < MIN_BODY_LEN:
        return False
    if post.get("num_comments", 0) > MAX_COMMENTS:
        return False
    age = post.get("age_hours")
    if age is not None and age > MAX_AGE_HOURS:
        return False
    return True


def main():
    if not RAW.exists():
        print(f"No raw posts found at {RAW}. Run Room 1 first.")
        return

    posts = json.loads(RAW.read_text())
    target_queries = load_target_queries()
    if not target_queries:
        print(f"No target queries found at {TARGET_QUERIES_FILE} — no priority flags this run.")
    keepers = []
    for p in posts:
        if not is_keeper(p):
            continue
        text = f"{p.get('title','')} {p.get('body','')}"
        p["audience"] = tag_audience(text)
        p["value_only"] = p.get("subreddit", "") in VALUE_ONLY_SUBS
        matched = match_target_query(text, target_queries)
        p["priority"] = matched is not None
        p["matched_query"] = matched["query"] if matched else None
        p["funnel"] = matched["funnel"] if matched else None
        keepers.append(p)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(keepers, indent=2))
    print(f"Kept {len(keepers)} of {len(posts)} posts -> {OUTPUT}")


if __name__ == "__main__":
    main()
