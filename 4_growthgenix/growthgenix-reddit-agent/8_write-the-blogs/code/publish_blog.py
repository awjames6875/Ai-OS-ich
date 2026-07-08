"""
publish_blog.py — Room 8: Write The Blogs (approve-then-publish).
60% DETERMINISTIC. No AI. Pushes ONE approved blog post to the website repo;
Vercel auto-deploys (production branch = main).

The website (github.com/awjames6875/safeharbor-behavioral-health, inspected 2026-07-07)
is a Next.js app. Blog posts are NOT files — they are objects in the array inside
src/data/blogPosts.ts. This script parses the approved draft's frontmatter, builds a
BlogPost object, and inserts it at the TOP of that array (the site lists newest first).

Usage:
    python publish_blog.py            -> list posts waiting in content/blog/pending/
    python publish_blog.py <slug>     -> publish that ONE post (your approval = running this)
    python publish_blog.py <slug> --preview -> run every check + print the exact post
                                               object, but NEVER commit or push

Draft format expected in content/blog/pending/<slug>.md (the blog engine writes this):
    ---
    title: Is My Child's Behavior Normal?
    excerpt: One-sentence summary shown on the blog index.
    category: parents            (parents | child | teen | body-brain)
    tags: tag one, tag two, tag three
    icon: emoji
    metaTitle: <=60 chars
    metaDescription: <=155 chars
    relatedPosts: slug-one, slug-two   (optional)
    ---
    # Article title
    ...markdown body...
Anything between the frontmatter and the first "# " heading (the content brief) is stripped.

Reads GITHUB_TOKEN and WEBSITE_REPO_URL from the project .env.local (gitignored).
NEVER publishes anything you didn't name. NEVER touches Reddit.
"""

import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PROJECT = BASE.parent
PENDING = PROJECT / "content" / "blog" / "pending"
PUBLISHED = PROJECT / "content" / "blog"
ENV_FILE = PROJECT / ".env.local"

BLOG_DATA_FILE = "src/data/blogPosts.ts"          # confirmed 2026-07-07
INSERT_ANCHOR = "export const blogPosts: BlogPost[] = ["
DEFAULT_AUTHOR = "Safe Harbor Behavioral Health Team"
REQUIRED_KEYS = ("title", "excerpt", "category", "tags", "metaTitle", "metaDescription")


def read_env() -> dict:
    if not ENV_FILE.exists():
        sys.exit(f"No .env.local at {ENV_FILE}")
    env = {}
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    for key in ("GITHUB_TOKEN", "WEBSITE_REPO_URL"):
        if key not in env:
            sys.exit(f"{key} missing from .env.local")
    return env


def parse_draft(path: Path):
    """Split frontmatter and body; strip any content-brief text before the first heading."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        sys.exit(f"{path.name} has no frontmatter block. Re-run the blog engine (Step 6).")
    _, fm, body = text.split("---", 2)
    meta = {}
    for line in fm.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    missing = [k for k in REQUIRED_KEYS if not meta.get(k)]
    if missing:
        sys.exit(f"{path.name} frontmatter is missing: {', '.join(missing)}")
    heading = body.find("# ")
    if heading > 0:
        body = body[heading:]  # drop the content brief
    return meta, body.strip()


def ts_str(value: str) -> str:
    """Escape for a single-quoted TS string."""
    return value.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")


def ts_template(value: str) -> str:
    """Escape for a backtick TS template literal."""
    return value.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")


def ts_list(csv: str) -> str:
    items = [i.strip() for i in csv.split(",") if i.strip()]
    return "[" + ", ".join(f"'{ts_str(i)}'" for i in items) + "]"


def build_post_object(slug: str, meta: dict, body: str) -> str:
    read_time = max(1, round(len(body.split()) / 200))
    published_date = f"{date.today().strftime('%B')} {date.today().day}, {date.today().year}"
    return f"""  {{
    slug: '{ts_str(slug)}',
    title: '{ts_str(meta["title"])}',
    excerpt: '{ts_str(meta["excerpt"])}',
    content: `
{ts_template(body)}
    `,
    author: '{ts_str(meta.get("author", DEFAULT_AUTHOR))}',
    date: '{published_date}',
    readTime: '{read_time} min read',
    category: '{ts_str(meta["category"])}',
    tags: {ts_list(meta["tags"])},
    icon: '{ts_str(meta.get("icon", "💙"))}',
    metaTitle: '{ts_str(meta["metaTitle"])}',
    metaDescription: '{ts_str(meta["metaDescription"])}',
    relatedPosts: {ts_list(meta.get("relatedPosts", ""))}
  }},"""


def confirm_publish(slug: str, meta: dict, body: str):
    """Show what's about to go live and require the slug typed back. Anything else aborts."""
    words = body.split()
    capsule = " ".join(words[:50]) + ("..." if len(words) > 50 else "")
    print("\nAbout to publish to the LIVE site:")
    print(f"  Title: {meta['title']}")
    print(f"  Slug:  {slug}")
    print(f"  First 50 words:\n  {capsule}\n")
    typed = input(f"Type the slug ({slug}) to confirm, anything else aborts: ").strip()
    if typed != slug:
        sys.exit("Aborted. Nothing pushed.")


def list_pending():
    posts = sorted(p for p in PENDING.glob("*.md") if p.name != "CLAUDE.md") if PENDING.exists() else []
    if not posts:
        print("Nothing waiting in content/blog/pending/. Run the blog engine first.")
        return
    print("Waiting for your approval:")
    for p in posts:
        print(f"  python publish_blog.py {p.stem}")


def publish(slug: str, preview: bool = False):
    src = PENDING / f"{slug}.md"
    if not src.exists():
        sys.exit(f"No pending post named {slug}. Run with no args to list pending posts.")
    meta, body = parse_draft(src)
    post_object = build_post_object(slug, meta, body)

    if not preview:
        confirm_publish(slug, meta, body)  # gate BEFORE the clone — abort costs nothing

    env = read_env()
    auth_url = env["WEBSITE_REPO_URL"].replace(
        "https://", f"https://x-access-token:{env['GITHUB_TOKEN']}@"
    )

    work = Path(tempfile.mkdtemp())
    try:
        subprocess.run(["git", "clone", "--depth", "1", auth_url, str(work / "repo")],
                       check=True, capture_output=True)
        repo = work / "repo"
        data_file = repo / BLOG_DATA_FILE
        if not data_file.exists():
            sys.exit(f"{BLOG_DATA_FILE} not found in the website repo — layout changed?")
        ts = data_file.read_text(encoding="utf-8")
        if f"slug: '{slug}'" in ts:
            sys.exit(f"A post with slug '{slug}' is already live. Pick a new slug.")
        if INSERT_ANCHOR not in ts:
            sys.exit(f"Anchor not found in {BLOG_DATA_FILE} — layout changed? Nothing pushed.")
        ts = ts.replace(INSERT_ANCHOR,
                        INSERT_ANCHOR + "\n" + post_object, 1)
        data_file.write_text(ts, encoding="utf-8")

        if preview:
            print("PREVIEW — exact object that would be inserted at the top of blogPosts.ts:")
            print(post_object)
            print("\nAll checks passed (repo cloned, slug unique, anchor found).")
            print("Nothing committed. Nothing pushed. Draft stays in pending/.")
            return

        git = ["git", "-C", str(repo),
               "-c", "user.email=reddit-agent@growthgenix.local",
               "-c", "user.name=GrowthGenix Reddit Agent"]
        subprocess.run(git + ["add", "-A"], check=True, capture_output=True)
        commit = subprocess.run(git + ["commit", "-m", f"Blog: {slug} ({date.today()})"],
                                capture_output=True)
        if commit.returncode != 0:
            print("No change to publish (post already live?).")
            return
        subprocess.run(git + ["push", "origin", "HEAD:main"], check=True, capture_output=True)
    finally:
        shutil.rmtree(work, ignore_errors=True)

    PUBLISHED.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(PUBLISHED / src.name))  # pending -> published locally
    print(f"Published {slug} -> blogPosts.ts on GitHub. Vercel will deploy it shortly.")
    print(f"Live at: safeharborbehavioralhealth.com/blog/{slug}")
    print(f"Moved to content/blog/{src.name} (marked as published).")


if __name__ == "__main__":
    preview = "--preview" in sys.argv[1:]
    args = [a for a in sys.argv[1:] if a != "--preview"]
    if args:
        publish(args[0], preview=preview)
    else:
        list_pending()
