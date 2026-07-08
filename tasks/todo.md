# Upgrade: safeharbor-reddit-triage + growthgenix-reddit-agent

Date: 2026-07-06
Locked (DO NOT TOUCH): honesty lock, the 4 gates, the 9-to-1 ratio.
Blocker: `references/target-queries.md` does not exist yet — Adam still needs to paste
the Red Rover report. All code reads the file at runtime, so it degrades gracefully
(no matches / "file missing" message) until it lands.

## Todos

- [x] 1. TARGETING (sort_posts.py DONE; SKILL.md edits BLOCKED by permission-system
      outage for files outside the repo — retry: two pending edits, Step 1 target-query
      check + 4-gates competitor-mention line, exact text in conversation 2026-07-06)
- [x] 2. FUNNEL — DONE: sort_posts.py sets funnel from matched target query;
      write_dashboard.py to_card() passes it; template renders navy funnel badge.
- [x] 3. COMPETITOR WATCH — DONE: 5 competitor searches in scrape_reddit.py build_urls();
      tag_competitor() tags matching posts ["competitor-mention"]; 4-gates note in
      code comments + client-config.md + Room 1 CONTEXT.
- [x] 4. NEW SUBS — DONE: MENTAL_HEALTH_SUBS = Anxiety, mentalhealth, traumatoolbox,
      family. NEVER-add list in code comment + config.
- [x] 5. ROOM 9 — DONE: 9_check-the-citations/ (check_citations.py + CONTEXT.md +
      citation-log.json seeded with 2.5% baseline, 2 of 80, Red Rover, 2026-07-06).
- [x] 6. ROOM 10 — DONE: 10_write-original-posts/CONTEXT.md (always disclosed, never
      fake lived experience, sub rules per post, human posts by hand).
- [x] 7. Housekeeping — DONE: client-config.md, Room 1/2/6 CONTEXT.md, agent CLAUDE.md
      routing table + Monthly section (rooms 9, 10).
- [x] 8. QUESTION BANK — DONE: content/code/build_question_bank.py mines keepers.json
      for question titles, dedupes with times_seen, writes question-bank.json + .md.
- [x] 9. BLOG ENGINE DIFFS — DONE: adam-story-blog-engine-SKILL.md Step 2 (topic
      sources), Step 5 (real-phrasing H2s, question cluster, keyword block), Step 6
      (drafts -> content/blog/pending/ approval queue).
- [x] 10. ROOM 8 — DONE: 8_write-the-blogs/ (CONTEXT.md, pick_blog_topics.py,
      publish_blog.py). Website repo recorded:
      https://github.com/awjames6875/safeharbor-behavioral-health.git
      GUARD: BLOG_DIR + SITE_FORMAT = UNCONFIRMED in publish_blog.py — script refuses
      to publish until the repo is inspected and they're set. ADAM: add
      WEBSITE_REPO_URL=... line to .env.local (exact line in client-config.md).
- [x] 11. MISSION CONTROL TRACKER — DONE: 6_load-the-dashboard/code/write_tracker.py
      renders tracker.html (self-contained scoreboard); stats-history.jsonl snapshot
      per run (idempotent per date); publish_to_github.sh ships it at /tracker.html.
      Verified: clean_old_files() cannot delete tracker.html or stats-history.jsonl.

## Locked decisions (2026-07-06)
- Website: GitHub + Netlify
- Publish mode: APPROVE FIRST — human reads every blog before the script publishes
  (licensed healthcare brand; honesty lock + FTC compliance get a human check)
- Voice: VOICE_DNA.md is the source of truth for blogs (blog engine Step 1) and
  Reddit drafts (Room 5) — same voice everywhere
- Reddit auto-posting stays FORBIDDEN — approve-then-script-publish applies to the
  website only

## Review (2026-07-06 — core batch, items 1-7)

**Written and complete:**
- `2_sort-the-keepers/code/sort_posts.py` — loads target-queries.md (path constant),
  matches keepers word-wise, sets priority / matched_query / funnel. Missing file =
  printed notice, run continues.
- `1_find-the-posts/code/scrape_reddit.py` — 4 new mental-health subs, 5 competitor
  search URLs (urllib quote-encoded), tag_competitor() text-matcher, tags field saved.
- `6_load-the-dashboard/` — write_dashboard.py passes funnel; template shows navy
  TOFU/MOFU/BOFU badge next to the card tag.
- `9_check-the-citations/` — new room: script (checklist + --log), CONTEXT.md,
  citation-log.json seeded with the 2.5% baseline.
- `10_write-original-posts/` — new room: CONTEXT.md with locked disclosure rules.
- Config/docs: client-config.md, agent CLAUDE.md (routing + Monthly section),
  Room 1/2/6 CONTEXT.md.

**Honesty lock, 4 gates, 9-to-1 ratio: untouched.** All changes additive.

**Still open:**
1. SKILL.md (safeharbor-reddit-triage) — 2 edits blocked by a temporary permission-system
   outage (file is outside this repo). Exact text is in the 2026-07-06 conversation.
2. target-queries.md — waiting on Adam to paste the Red Rover report (3 paste attempts
   failed). Everything degrades gracefully until it exists.
3. Python scripts not smoke-tested (shell also blocked by the same outage) — run
   `python sort_posts.py` / `python check_citations.py` to verify.
4. Website repo (safeharbor-behavioral-health) not yet inspected — outage blocked
   gh/WebFetch. When it clears: list repo files, then set BLOG_DIR + SITE_FORMAT in
   8_write-the-blogs/code/publish_blog.py (guard currently refuses to publish).

## Code review findings (2026-07-07) — #1 and #2 FIXED, rest open

Fixed:
- [x] 1. publish_blog.py icon field unescaped -> could break live Vercel build (ts_str added)
- [x] 2. sort_posts.py priority over-matching (52/179 false flags -> 11/179 after
      whole-word match + skip 1-word queries)

Open (lower stakes, fix when touched):
- [ ] 3. publish_blog.py duplicate-slug guard checks raw slug vs escaped insert
- [ ] 4. publish_blog.py brief-strip cuts at first "# " (mis-slices H2-first bodies)
- [ ] 5. publish_blog.py crashes (ValueError) on draft missing closing --- fence
- [ ] 6. write_tracker.py 9-to-1 check warns on ~every run (compares keepers, not posts made)
- [ ] 7. scrape_reddit.py clean_reddit_url returns relative path for bare permalinks
- [ ] 8. pick_blog_topics.py can't dedup single-word topics (needs >=2 word overlap)
- [ ] 9. question-bank consumers hard-index 'subreddit'/'times_seen' (KeyError on legacy entries)
- [ ] 10. read_env keeps quotes on quoted .env.local values (would corrupt git auth URL)

## Review (2026-07-06 — blog batch, items 8-11)

**Written and complete:**
- content/code/build_question_bank.py — daily question archive with times_seen demand counts
- adam-story-blog-engine-SKILL.md — new topic sources (Step 2), GEO upgrades (Step 5:
  real Reddit phrasing, question clusters, keyword block), pending/ approval queue (Step 6)
- 8_write-the-blogs/ — CONTEXT.md + pick_blog_topics.py (UNTAPPED-first selection,
  covered-topic skip with printed skip log) + publish_blog.py (approve-first,
  UNCONFIRMED guard, copies proven publish_to_github.sh pattern in Python)
- 6_load-the-dashboard/code/write_tracker.py — Mission Control scoreboard (tracker.html)
- publish_to_github.sh — ships tracker.html alongside the dashboard
- client-config.md — Website section with repo URL + WEBSITE_REPO_URL line for Adam
- Agent CLAUDE.md — Room 8 routing, question-bank/tracker steps, Monthly section
