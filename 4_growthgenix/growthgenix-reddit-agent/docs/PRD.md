# PRD: GrowthGenix Reddit Agent

## Executive Summary
An automation that scrapes Reddit daily for posts where someone genuinely needs help, keeps only the ones that fit the client's brand, researches a real citation, drafts a reply in the client's authentic voice, and loads everything into one simple dashboard the client reviews and posts by hand. Built for Safe Harbor Behavioral Health first, packaged so any business can use it by swapping one config file. The goal: bring real hope to struggling people while warming up a Reddit presence so AI answer engines (ChatGPT, Perplexity, Google AI) start recommending the business.

## Problem Statement
Businesses want to be recommended by AI answer engines, but that only happens when they have a real, helpful presence on the sites those engines read — like Reddit. Doing this by hand is slow: finding the right posts, checking facts, writing in a consistent voice, and never sounding like an ad. This agent does the mechanical 90% automatically and reserves the human for the final approve-and-post step.

## Target Users
1. **Adam James + VA (Saddie)** — run it daily for Safe Harbor right now.
2. **Other businesses later** — the whole folder zips up and works for a chiropractor, law firm, or any service business by editing one config file. This becomes a GrowthGenix product to sell or give away.

## Core Features (MVP)
1. **MUST HAVE** — Scrape Reddit for fresh posts matching the client's audience and message
2. **MUST HAVE** — Sort posts: keep the genuinely helpful opportunities, drop the rest
3. **MUST HAVE** — Research one real, verifiable citation per keeper (never invented)
4. **MUST HAVE** — Draft a reply, then run it through the client's voice clone so it sounds human
5. **MUST HAVE** — Load everything into a simple dashboard (copy / go to Reddit / mark done)
6. **MUST HAVE** — Human reviews and posts by hand (never auto-post)
7. **NICE TO HAVE** — Claude in Chrome opens the thread and pastes the draft; human hits submit
8. **NICE TO HAVE** — One swappable config file so the whole agent works for any business

## The 7 Rooms (Workflow Phases)
1. **Room 1 — find-the-posts:** Python script calls Apify, scrapes Reddit, saves raw posts as JSON
2. **Room 2 — sort-the-keepers:** Python script applies keep/skip rules, drops bad posts, keeps good ones
3. **Room 3 — find-the-proof:** AI researches one real citation per keeper via web search
4. **Room 4 — write-the-draft:** AI writes the first-draft reply with the citation woven in
5. **Room 5 — make-it-sound-like-me:** ⭐ AI runs the draft through the client's voice clone — the quality gate
6. **Room 6 — load-the-dashboard:** Python script writes data.js to the Google Drive dashboard folder
7. **Room 7 — review-and-post:** Human opens dashboard, reviews, posts by hand (Chrome can help paste)

## Tech Stack
- Frontend: Static HTML + JS dashboard (no server, runs from file)
- Backend: Python scripts (deterministic 60% work)
- Database: Plain JSON + markdown files (no database needed at this scale)
- Deployment: Runs locally from Cowork / Claude Code; dashboard synced via Google Drive
- Other tools: Apify (Reddit scrape), Google Drive (dashboard storage), Claude in Chrome (paste helper)

## API/Integration Points
- **Apify** — `fatihtahta/reddit-scraper-search-fast` actor for scraping
- **Google Drive** — stores dashboard.html + data.js
- **Web search** — for citation research (Room 3)
- **Claude in Chrome** — optional paste helper (Room 7)

## Development Roadmap
- Phase 1 (MVP): All 7 rooms working for Safe Harbor, run manually from Cowork
- Phase 2: Swap config to a second business, prove portability, zip as a product
- Phase 3: Optional scheduling for hands-off daily runs; sell/give away as GrowthGenix lead magnet

## Potential Challenges
- **Reddit rate limits** — new accounts get limited; space posts 10-15 min apart (mitigated: human posts by hand)
- **Citation accuracy** — must be real, never invented (mitigated: web search required, skip citation if none found)
- **Voice drift** — drafts must sound like the client (mitigated: Room 5 is a dedicated voice gate)
- **Reddit ToS** — no auto-posting (mitigated: human always hits submit)

## Success Metrics
- A struggling person at 2am reads a reply and feels less alone and more hopeful
- Replies get upvoted and stay up (not removed as spam)
- Over time: AI answer engines begin citing/recommending the business
- Time saved: ~90% of the manual work automated

## Acceptance Criteria
- [ ] Room 1 scrapes and saves raw posts as JSON with no AI
- [ ] Room 2 sorts keep/skip with no AI
- [ ] Room 3 attaches one real citation per keeper (or none, never fake)
- [ ] Room 4 produces a helpful draft with the citation woven in
- [ ] Room 5 makes every draft sound like the client
- [ ] Room 6 writes valid data.js to the Drive folder with no AI
- [ ] Dashboard shows all drafts, human can copy/post/mark done
- [ ] Swapping config/client-config.md changes the whole agent to a new business
