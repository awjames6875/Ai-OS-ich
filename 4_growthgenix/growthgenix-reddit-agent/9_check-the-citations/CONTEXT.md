# CONTEXT.md — Check The Citations

## Purpose
Monthly scoreboard: are AI engines (ChatGPT, Perplexity, Claude) citing Safe Harbor for the
top-20 target queries yet? Tracks progress against the 2.5% baseline (2 of 80, Red Rover
report, 2026-07-06).

## The Process (Step by Step) — once a month
1. Run `python code/check_citations.py`
   -> writes `output/citation-checklist-YYYY-MM.md` (top-20 queries x 3 engines)
2. ADAM, BY HAND: run each query through ChatGPT, Perplexity, and Claude.
   Mark `[x]` wherever Safe Harbor (safeharborbehavioralhealth.com) is named or cited.
   Save the file.
3. Run `python code/check_citations.py --log`
   -> parses the filled checklist, appends the month's numbers to `output/citation-log.json`

## Identity & Audience
- Who uses this room: Adam, once a month (~30 minutes)
- What "good" looks like here: the pct number in citation-log.json climbing month over month

## Tech Stack For This Room
- Python (`check_citations.py`)
- Queries come from the triage skill's `references/target-queries.md`
  (sorted UNTAPPED-first, then by volume — so top 20 rows = the right 20)

## Never Do This (Constraints)
- NEVER let AI guess or "check" whether an engine cited Safe Harbor — only Adam's
  hand-checked boxes count. This log must be real or it is worthless.
- Never edit citation-log.json by hand except to fix a genuine mistake
- Never delete the baseline entry (it has no "month" key so reruns never replace it)

## 60-30-10 Split For This Room
- 60% (Scripts): check_citations.py builds the checklist and parses results into the log
- 30% (Rules): target-queries.md holds the queries; this file holds the process
- 10% (AI): none — the whole point is human-verified ground truth

## Skills To Load (Layer 3)
- None — pure Python + human hands
