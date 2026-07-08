# CONTEXT.md — Find The Posts

## Purpose
Scrape Reddit for fresh posts that match the client's audience and message.

## The Process (Step by Step)
1. Read the search terms and Apify settings from `config/client-config.md`
2. Run the Python script `code/scrape_reddit.py`
3. Script calls the Apify actor, pulls fresh posts
4. Script saves raw posts to `output/raw-posts.json`

## Identity & Audience
- Who uses this room: the agent, automatically
- What "good" looks like here: fresh posts from the last week, saved cleanly as JSON, no duplicates

## Tech Stack For This Room
- Python (`scrape_reddit.py`)
- Apify actor: `fatihtahta/reddit-scraper-search-fast` (95.7% success)

## Patterns to Follow
- TARGET SUBREDDITS, not Reddit-wide keyword search. Pull newest posts from on-topic
  communities via the actor's `urls` field (built by scrape_reddit.py). Keyword search
  matched words anywhere and returned ~98% junk — do not go back to it.
- Substance abuse / recovery subs are first-class targets (client treats substance use).
- Local Oklahoma subs use a keyword-SCOPED search, not the full feed (they're too broad).
- General mental health subs added 2026-07-06: Anxiety, mentalhealth, traumatoolbox, family.
  NEVER add: childfree, teenagers, BodyweightFitness.
- Competitor watch (2026-07-06): Reddit-wide searches for grandmh, "Grand Mental Health",
  "Family & Children's Services" Tulsa, "BetterHelp alternative" Oklahoma, "Talkspace
  alternative" Oklahoma. Matching posts get tags: ["competitor-mention"]. A disclosed
  recommendation in these threads STILL requires all 4 gates.
- Clean Reddit URLs — strip `?solution=`, `&js_challenge=`, `&token=` params
- Save only needed fields: title, body, subreddit, permalink, score, num_comments, query, age_hours, tags

## Never Do This (Constraints)
- Never use the AI to scrape — this is 100% Python
- Never use actor `harshmaur/reddit-scraper` (only 55.8% success)
- Never scrape comments or NSFW content

## 60-30-10 Split For This Room
- 60% (Scripts): scrape_reddit.py does ALL the work — call Apify, clean URLs, save JSON
- 30% (Rules): config/client-config.md holds the search terms and Apify settings
- 10% (AI): none — this room needs zero AI

## Skills To Load (Layer 3)
- None — pure Python room
