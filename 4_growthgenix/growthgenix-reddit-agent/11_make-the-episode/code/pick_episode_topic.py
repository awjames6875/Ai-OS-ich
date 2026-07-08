"""
pick_episode_topic.py — Room 11: Make The Episode (topic selection).
60% DETERMINISTIC. No AI. Picks the next episode from published blogs.

Source = content/blog/*.md (published only, never pending/). Skips any blog already
in output/episodes-log.json. Suggests the lane: every 3rd episode is the real-Adam
lane (~30%), the rest are the HeyGen avatar lane (~70%). Adam can override.

    python pick_episode_topic.py

Writes output/episode-queue.json. Then say "write the episode" — AI drafts the
narration script from the blog (rules in skills/episode-format.md).
"""

import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PROJECT = BASE.parent
BLOG_DIR = PROJECT / "content" / "blog"
LOG_FILE = BASE / "output" / "episodes-log.json"
OUTPUT = BASE / "output" / "episode-queue.json"

REAL_LANE_EVERY = 3  # every 3rd episode = real-Adam lane (~30%)


def blog_title(path: Path) -> str:
    """First markdown H1, else the slug made readable."""
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def load_done_slugs() -> list:
    if not LOG_FILE.exists():
        return []
    return [e["slug"] for e in json.loads(LOG_FILE.read_text(encoding="utf-8"))]


def main():
    done = load_done_slugs()
    # claude-mem drops a CLAUDE.md stub in this folder — it is not a blog post
    published = sorted((p for p in BLOG_DIR.glob("*.md") if p.name != "CLAUDE.md"),
                       key=lambda p: p.stat().st_mtime)
    candidates = [p for p in published if p.stem not in done]

    if not candidates:
        print("No unused published blogs. Publish a blog in Room 8 first.")
        return

    pick = candidates[0]  # oldest unused first — work through the backlog in order
    lane = "real" if (len(done) + 1) % REAL_LANE_EVERY == 0 else "avatar"

    queue = {
        "slug": pick.stem,
        "title": blog_title(pick),
        "blog_path": str(pick.relative_to(PROJECT)),
        "lane": lane,
        "target_length": "2-3 minutes (280-420 spoken words)",
        "episode_number": len(done) + 1,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(queue, indent=2), encoding="utf-8")

    print(f"Episode #{queue['episode_number']}: {queue['title']}")
    print(f"  Source blog: {queue['blog_path']}")
    print(f"  Suggested lane: {lane.upper()}"
          + ("  (Adam records himself)" if lane == "real"
             else "  (HeyGen — PAID, Adam approves before any call)"))
    print(f"  Remaining unused blogs: {len(candidates) - 1}")
    print(f"Queue written: {OUTPUT}")
    print('Next: say "write the episode" — AI drafts the narration script.')


if __name__ == "__main__":
    main()
