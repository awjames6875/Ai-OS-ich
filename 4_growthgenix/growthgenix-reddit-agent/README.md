# GrowthGenix Reddit Agent

A daily Reddit helper that finds posts worth replying to, drafts a genuinely helpful
reply in your voice with a real citation, and loads it into a simple dashboard you
review and post by hand.

Built for **Safe Harbor Behavioral Health** first. Swap `config/client-config.md`
to run it for any other business.

## The 60-30-10 Rule
- **60%** Python scripts do the mechanical work (scrape, sort, format) — no AI, no wasted tokens
- **30%** Markdown + config files hold the rules, voice, and facts
- **10%** AI does only what it's good at — research, drafting, and voice

## The 7 Rooms
1. `1_find-the-posts/` — Python scrapes Reddit via Apify
2. `2_sort-the-keepers/` — Python keeps the good posts, drops the rest
3. `3_find-the-proof/` — AI researches one real citation
4. `4_write-the-draft/` — AI writes the first draft
5. `5_make-it-sound-like-me/` — ⭐ AI runs it through your voice clone
6. `6_load-the-dashboard/` — Python writes data.js to Google Drive
7. `7_review-and-post/` — You review and post by hand

## How To Run It (daily)
From Cowork or Claude Code, say: **run Reddit**

The router (CLAUDE.md) walks each room in order. Mechanical rooms run their Python
scripts; AI rooms do the 10%. At the end, open your dashboard and post by hand.

## How To Reuse It For Another Business
1. Copy this whole folder
2. Edit `config/client-config.md` — new brand, search terms, voice file, Drive folder
3. Done. Everything else works as-is.

## Critical Rules
- Never auto-post — a human always hits submit (Reddit ToS)
- Never invent citations — real and verifiable only
- Space posts 10-15 min apart (Reddit rate limits)
