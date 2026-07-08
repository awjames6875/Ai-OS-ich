# CONTEXT.md — Sort The Keepers

## Purpose
Keep the posts genuinely worth replying to, drop the ones that aren't.

## The Process (Step by Step)
1. Read `output/raw-posts.json` from Room 1
2. Run the Python script `code/sort_posts.py`
3. Script applies the keep/skip rules from config
4. Script saves keepers to `output/keepers.json`
5. Run `code/fetch_thread_style.py` — second Apify pass (top 15 keepers ONLY, priority
   first then highest score, top 5 comments each), computes a style profile (avg length,
   structure, links, tone) and writes it into each keeper as the `format` field. The 15
   with profiles are the day's drafting pool; keepers.json stays full for the question bank.

## Identity & Audience
- Who uses this room: the agent, automatically
- What "good" looks like here: only real help opportunities survive; spam, ads, and off-brand posts are dropped

## Tech Stack For This Room
- Python (`sort_posts.py`)

## Patterns to Follow
- Keep posts where someone is genuinely struggling and the client can help
- Tag each keeper: audience type + whether the brand can be mentioned or it's value-only
- Target-query priority (2026-07-06): each keeper is matched against the triage skill's
  `references/target-queries.md`. A match (UNTAPPED or competitor-gap query) sets
  priority=true, matched_query, and funnel (TOFU/MOFU/BOFU). No file = no flags, run continues.
- Drop posts that are too old, off-topic, or already heavily answered

## Never Do This (Constraints)
- Never use AI to do the sorting — rules live in config, Python applies them
- Never keep a post that breaks a subreddit's self-promo rules
- Never mention the brand where config says value-only

## 60-30-10 Split For This Room
- 60% (Scripts): sort_posts.py applies the rules and writes keepers.json
- 30% (Rules): config/client-config.md holds keep/skip rules and subreddit rules
- 10% (AI): none — deterministic yes/no decisions

## Skills To Load (Layer 3)
- The client's triage skill (for Safe Harbor: safeharbor-reddit-triage) as the rule source
