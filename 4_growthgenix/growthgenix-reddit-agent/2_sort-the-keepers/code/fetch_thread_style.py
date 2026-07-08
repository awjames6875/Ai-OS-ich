"""
fetch_thread_style.py — Room 2.5: Fetch Thread Format (KEEP threads only)
60% DETERMINISTIC. No AI. Second Apify pass fetches top comments for KEEPERS ONLY,
then computes a style profile per thread and writes it back into keepers.json.

WHY KEEPERS ONLY: comments are the expensive part of an Apify run. We never fetch
comments for all raw posts — only the handful that survived Room 2 sorting.
"""

import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
KEEPERS = BASE / "output" / "keepers.json"

APIFY_ACTOR = "fatihtahta/reddit-scraper-search-fast"  # verified 2026-07-07: urls accepts post links; scrapeComments + maxComments supported
MAX_COMMENTS = 5
DAILY_BATCH = 15  # only fetch comments for the day's drafting pool — human posts ~5-10/day

# Simple whole-word casual markers. One hit makes a comment "casual".
CASUAL_MARKERS = [
    "lol", "lmao", "omg", "tbh", "idk", "gonna", "wanna", "kinda",
    "dont", "cant", "im", "ive", "yall", "haha", "u", "ur",
]


def clean_reddit_url(url: str) -> str:
    """Same normalization as Room 1 — lets us match comments back to keepers."""
    m = re.match(r"(https?://(?:www\.)?reddit\.com/r/[^/]+/comments/[^/?]+)/?", url or "")
    return m.group(1) + "/" if m else (url or "").split("?")[0]


def build_apify_input(keepers):
    """The exact input the agent passes to the Apify actor for the comment pass."""
    batch = sorted(keepers, key=lambda k: (not k.get("priority"), -(k.get("score") or 0)))[:DAILY_BATCH]
    return {
        "urls": [k["permalink"] for k in batch if k.get("permalink")],
        "maxPosts": 1,
        "scrapeComments": True,
        "maxComments": MAX_COMMENTS,
        "includeNsfw": False,
    }


def is_bulleted(text: str) -> bool:
    lines = text.splitlines()
    return sum(1 for l in lines if re.match(r"\s*([-*•]|\d+[.)])\s+", l)) >= 2


def is_casual(text: str) -> bool:
    words = set(re.findall(r"[a-z']+", text.lower()))
    return any(m in words for m in CASUAL_MARKERS)


def build_profile(comment_texts):
    """Deterministic style profile from the top comments of one thread."""
    texts = [t.strip() for t in comment_texts if t and t.strip()][:MAX_COMMENTS]
    if not texts:
        return None
    word_counts = [len(t.split()) for t in texts]
    avg_words = round(sum(word_counts) / len(word_counts))
    length_band = "short" if avg_words < 50 else ("medium" if avg_words <= 150 else "long")
    bulleted = sum(1 for t in texts if is_bulleted(t))
    structure = "bullets" if bulleted >= len(texts) / 2 else ("mixed" if bulleted else "paragraphs")
    casual = sum(1 for t in texts if is_casual(t))
    return {
        "comments_sampled": len(texts),
        "avg_words": avg_words,
        "length_band": length_band,
        "structure": structure,
        "links_present": any("http" in t for t in texts),
        "tone": "casual" if casual >= len(texts) / 2 else "proper",
    }


def extract_comments_by_post(raw_apify_results):
    """Map cleaned post URL -> list of comment texts. Handles both shapes the actor
    can return: post items with a nested `comments` array, or flat comment items."""
    by_post = {}
    for item in raw_apify_results:
        nested = item.get("comments")
        if isinstance(nested, list):
            url = clean_reddit_url(item.get("url", item.get("permalink", "")))
            by_post.setdefault(url, []).extend(
                c.get("body", c.get("text", "")) if isinstance(c, dict) else str(c)
                for c in nested
            )
        elif item.get("postUrl") or item.get("parentPermalink"):
            url = clean_reddit_url(item.get("postUrl", item.get("parentPermalink", "")))
            by_post.setdefault(url, []).append(item.get("body", item.get("text", "")))
    return by_post


def main(raw_apify_results=None):
    """
    In a real run, the agent calls the Apify actor with build_apify_input() via the
    Apify connector, then hands the returned items here. No results = print the input.
    """
    if not KEEPERS.exists():
        print(f"No keepers found at {KEEPERS}. Run sort_posts.py first.")
        return
    keepers = json.loads(KEEPERS.read_text())

    if raw_apify_results is None:
        print("No Apify results passed in. Use this input with actor:", APIFY_ACTOR)
        print(json.dumps(build_apify_input(keepers), indent=2))
        return

    by_post = extract_comments_by_post(raw_apify_results)
    profiled = 0
    for k in keepers:
        profile = build_profile(by_post.get(clean_reddit_url(k.get("permalink", "")), []))
        k["format"] = profile  # None = no comments found; drafting falls back to normal
        profiled += 1 if profile else 0

    KEEPERS.write_text(json.dumps(keepers, indent=2))
    print(f"Style profiles for {profiled} of {len(keepers)} keepers -> {KEEPERS}")


if __name__ == "__main__":
    main()
