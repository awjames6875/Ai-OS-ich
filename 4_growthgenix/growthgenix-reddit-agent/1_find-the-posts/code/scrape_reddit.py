"""
scrape_reddit.py — Room 1: Find The Posts
60% DETERMINISTIC. No AI. Builds the Apify input, cleans URLs, saves raw posts as JSON.

WHY THIS CHANGED (2026-06-30):
The old version did a Reddit-WIDE keyword search ("toddler aggressive behavior", etc.).
Reddit search matches those words anywhere, so ~98% of results were junk (gaming, divorce,
matrimonial, sports). FIX: we now scrape TARGETED COMMUNITIES directly via the actor's `urls`
field — the newest posts from on-topic subreddits, plus scoped local searches for Oklahoma.
Triage (Room 2) then sorts keep/skip. On-topic communities in → real keeps out.

NOTE on the actor: if `urls` are provided, the actor uses them and IGNORES the `queries`
field. So this room is URL-based, not keyword-based.

Reads target subreddits + Apify settings from config/client-config.md (this script holds the
canonical defaults). Saves to output/raw-posts.json.
"""

import json
import re
from pathlib import Path
from urllib.parse import quote

APIFY_ACTOR = "fatihtahta/reddit-scraper-search-fast"  # 95.7% success — never use harshmaur
MAX_POSTS_PER_URL = 12
TIMEFRAME = "week"  # used by the scoped-search URLs below

# --- Targeted communities (newest posts pulled from each) ---------------------
# Parents & kids' behavioral health (primary audience)
PARENT_KID_SUBS = [
    "Parenting", "Mommit", "daddit", "toddlers", "beyondthebump",
    "ADHD", "ADHDparenting", "Autism_Parenting", "ChildPsychology",
    "raisingkids", "breakingmom",
]

# Substance abuse / addiction & recovery (EMPHASIZED — Safe Harbor treats substance use
# for the ages served, and serves families in recovery). Most are value-only per config.
SUBSTANCE_RECOVERY_SUBS = [
    "stopdrinking", "REDDITORSINRECOVERY", "addiction", "leaves",
    "OpiatesRecovery", "recovery", "Sober", "alcoholism",
    "AlAnon", "NarAnon",
]

# Reentry (dignity first — value-only by default)
REENTRY_SUBS = ["reentry", "ExCons"]

# General mental health (added 2026-07-06).
# NEVER add: childfree, teenagers, BodyweightFitness — off-mission or minors-heavy spaces.
MENTAL_HEALTH_SUBS = ["Anxiety", "mentalhealth", "traumatoolbox", "family"]

FEED_SUBS = PARENT_KID_SUBS + SUBSTANCE_RECOVERY_SUBS + REENTRY_SUBS + MENTAL_HEALTH_SUBS

# Local Oklahoma subs are broad/off-topic, so we DON'T pull the whole feed — we run a
# keyword-scoped search inside them to surface only behavioral-health-relevant posts.
LOCAL_SUBS = ["oklahoma", "tulsa", "okc"]
LOCAL_SEARCH_TERMS = "therapy OR counseling OR mental health OR addiction OR son OR daughter OR teen"

# --- Competitor watch (2026-07-06) --------------------------------------------
# Reddit-wide searches for competitor mentions. Local orgs are inherently Oklahoma;
# national platforms get "Oklahoma" appended to keep results local.
# Matching threads are tagged "competitor-mention" — high-value intel, BUT a disclosed
# Safe Harbor recommendation in these threads STILL requires all 4 gates. No shortcuts.
COMPETITOR_SEARCHES = [
    "grandmh",
    '"Grand Mental Health"',
    "\"Family & Children's Services\" Tulsa",
    '"BetterHelp alternative" Oklahoma',
    '"Talkspace alternative" Oklahoma',
]
COMPETITOR_TERMS = [
    "grandmh", "grand mental health", "family & children's services",
    "betterhelp alternative", "talkspace alternative",
]


def build_urls():
    """Return the list of Reddit URLs the actor should scrape (newest first)."""
    urls = [f"https://www.reddit.com/r/{sub}/new/" for sub in FEED_SUBS]
    q = LOCAL_SEARCH_TERMS.replace(" ", "%20")
    for sub in LOCAL_SUBS:
        urls.append(
            f"https://www.reddit.com/r/{sub}/search/?q={q}"
            f"&restrict_sr=1&sort=new&t={TIMEFRAME}"
        )
    for cq in COMPETITOR_SEARCHES:
        urls.append(f"https://www.reddit.com/search/?q={quote(cq)}&sort=new&t={TIMEFRAME}")
    return urls


def build_apify_input():
    """The exact input the agent passes to the Apify actor in Step 0."""
    return {
        "urls": build_urls(),
        "maxPosts": MAX_POSTS_PER_URL,
        "scrapeComments": False,
        "includeNsfw": False,
    }


def clean_reddit_url(url: str) -> str:
    """Strip Apify tracking params that trigger Reddit's bot block."""
    match = re.match(r"(https?://(?:www\.)?reddit\.com/r/[^/]+/comments/[^/?]+)/?", url)
    if match:
        return match.group(1) + "/"
    return url.split("?")[0]


def tag_competitor(post: dict) -> list:
    """Tag posts that mention a watched competitor (text match — works from any source URL)."""
    low = f"{post.get('title','')} {post.get('body', post.get('selftext',''))}".lower()
    return ["competitor-mention"] if any(t in low for t in COMPETITOR_TERMS) else []


def keep_fields(post: dict) -> dict:
    return {
        "title": post.get("title", ""),
        "body": post.get("body", post.get("selftext", "")),
        "subreddit": post.get("subreddit", ""),
        "permalink": clean_reddit_url(post.get("url", post.get("permalink", ""))),
        "score": post.get("score", 0),
        "num_comments": post.get("num_comments", 0),
        "query": post.get("query", ""),
        "age_hours": post.get("age_hours", None),
        "tags": tag_competitor(post),
    }


OUTPUT = Path(__file__).resolve().parents[1] / "output" / "raw-posts.json"


def main(raw_apify_results=None):
    """
    In a real run, the agent calls the Apify actor with build_apify_input() via the Apify
    connector, then hands the returned list here to clean and save. AI stays out of the
    mechanical work.
    """
    if raw_apify_results is None:
        print("No Apify results passed in. Use this input with actor:", APIFY_ACTOR)
        print(json.dumps(build_apify_input(), indent=2))
        return

    cleaned = [keep_fields(p) for p in raw_apify_results]

    seen = set()
    unique = []
    for p in cleaned:
        if p["permalink"] and p["permalink"] not in seen:
            seen.add(p["permalink"])
            unique.append(p)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(unique, indent=2))
    print(f"Saved {len(unique)} unique posts to {OUTPUT}")


if __name__ == "__main__":
    main()
