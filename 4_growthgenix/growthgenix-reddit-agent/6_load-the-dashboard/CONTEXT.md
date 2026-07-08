# CONTEXT.md — Load The Dashboard

## Purpose
Build a SELF-CONTAINED dashboard.html with today's drafts baked inside, overwriting the same
file every run so old data can never be shown again.

## The Process (Step by Step)
1. Read `output/final-drafts.json` from Room 5
2. Run the Python script `code/write_dashboard.py`
3. Script injects the data directly into `template/dashboard-template.html`
4. Script OVERWRITES `output/dashboard.html` (single canonical file — no separate data.js to go stale)
5. Open `output/dashboard.html` directly. It carries its own data; nothing else is needed.

## Why Self-Contained + Self-Cleaning (Stale-Data Fix)
The dashboard used to load a separate `data.js`. Old `data.js` files piled up — and could NOT
be deleted from Google Drive — so the dashboard sometimes loaded yesterday's posts. Now the data
lives INSIDE dashboard.html and the file is overwritten each run, so the previous day's data is
physically gone. The script also deletes any leftover files in `output/` (old data.js, dated
dashboards), so the folder always holds exactly ONE current `dashboard.html`. Nothing accumulates.

## Identity & Audience
- Who uses this room: the agent, automatically
- What "good" looks like here: data.js is valid, URLs are clean, the dashboard opens and shows every post

## Tech Stack For This Room
- Python (`write_dashboard.py`)
- Google Drive folder (ID in config)

## Patterns to Follow
- Match the data.js format the dashboard expects exactly
- Clean every Reddit URL (no Apify params)
- Mark priority posts and value-only vs brand-okay tags
- Funnel badge (2026-07-06): cards carry a "funnel" field (TOFU/MOFU/BOFU or null) from
  Room 2's target-query match; the template shows it as a navy badge next to the tag
- Mission Control (2026-07-06): `code/write_tracker.py` renders the scoreboard
  (tracker.html) — citation rate vs 2.5% baseline, activity trend (stats-history.jsonl),
  9-to-1 ratio check, funnel mix, competitor mentions, question bank, blogs, originals.
  publish_to_github.sh ships it alongside the dashboard at /tracker.html.
  clean_old_files() must never delete tracker.html or stats-history.jsonl.

## Never Do This (Constraints)
- Never use AI to write the dashboard — pure Python formatting
- Never leave messy URLs that trigger Reddit's bot block
- Never edit `output/dashboard.html` by hand — it is regenerated and overwritten each run
- Never edit `template/dashboard-template.html` for daily data — only the template's LOOK lives there
- Never reintroduce a separate loaded data.js as the source of truth (it caused stale-data bugs)

## 60-30-10 Split For This Room
- 60% (Scripts): write_dashboard.py does ALL formatting and saving
- 30% (Rules): config holds the Drive folder ID and dashboard format
- 10% (AI): none — pure Python

## Skills To Load (Layer 3)
- None — pure Python room
