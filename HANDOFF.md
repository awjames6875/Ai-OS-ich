# HANDOFF — Session Briefing (written July 7, 2026, late night)

Read this first next session. Pipeline root:
`4_growthgenix/growthgenix-reddit-agent/` (client #1 = Safe Harbor Behavioral Health)

## 1. WHAT GOT DONE (July 7)

- **Duplicate cleanup** — accidental nested copy at
  `4_growthgenix/growthgenix-reddit-agent/4_growthgenix/...` diffed, confirmed, deleted.
  No hardcoded paths pointed at it.
- **Format matching** — new Room 2.5 script `2_sort-the-keepers/code/fetch_thread_style.py`:
  second Apify pass (same actor, verified comment support) fetches top 5 comments for the
  top-15 keepers (priority first, then score — cost cap ~$0.11/run). Builds a style profile
  (avg words, length band, structure, links, tone) per thread, writes `format` into
  keepers.json. Dashboard cards show a style badge. SKILL.md Step 5.5 +
  `references/format-style-profile.md` document it. Rule: format changes the CONTAINER,
  never the content (honesty lock, 4 gates, 9:1, brand language untouched).
- **publish_blog.py safety gates** — (a) type-the-slug confirmation before clone/push,
  anything else aborts; (b) `--preview` flag runs every check + prints the exact post
  object, never commits/pushes; (c) claude-mem's CLAUDE.md excluded from pending list.
  All smoke-tested.
- **Skills re-zipped + uploaded** — both zips rebuilt with Python zipfile (forward-slash
  paths; PowerShell Compress-Archive backslashes had broken claude.ai upload). Both live
  on claude.ai as of 7/7/26: safeharbor-reddit-triage + adam-story-blog-engine.
- **Committed + pushed** — `4099438` on origin/master: all 10 rooms, format matching,
  publish gates, HANDOFF.md (81 files; .env.local stayed gitignored).
- **NOT done (see Open Items):** blog sandwich AEO upgrade.

## 2. CURRENT STATE — The 10 Rooms

| Room | Does |
|---|---|
| 1_find-the-posts | Python scrapes Reddit via Apify (fatihtahta actor), saves raw-posts.json |
| 2_sort-the-keepers | Python sorts keep/skip → keepers.json; then fetch_thread_style.py adds format profiles (top 15) |
| 3_find-the-proof | AI researches ONE real citation per keeper (never fabricated) |
| 4_write-the-draft | AI writes first draft matching thread's format profile |
| 5_make-it-sound-like-me | AI voice-clone pass (must not inflate short casual replies) |
| 6_load-the-dashboard | Python writes dashboard data.js + write_tracker.py scoreboard |
| 7_review-and-post | HUMAN reviews dashboard, posts by hand — never automated |
| 8_write-the-blogs | Monthly: blog engine drafts to pending/, publish_blog.py pushes ONE approved post (slug confirm / --preview) |
| 9_check-the-citations | Monthly: builds top-20 query checklist, Adam runs by hand, logs results |
| 10_write-original-posts | Monthly: 2–4 disclosed original posts, human posts by hand |

## 3. NEXT UP — Day 2 Plan (video lane)

1. Verify Node 22+ and FFmpeg installed
2. `npx skills add heygen-com/hyperframes --all`
3. Build Room **11_make-the-episode**
4. 15-second test render (prove the pipe works before anything bigger)
5. Build Room **12_cut-the-shorts** — two lanes:
   - Avatar lane = HeyGen
   - Auto lane = ElevenLabs + HiggsField + HyperFrames render

**HARD GATE: no paid API calls without Adam's explicit approval. Ask first, every time.**

## 4. OPEN ITEMS

- **Blog sandwich AEO upgrade** — offered, not built: FAQ blocks, answer-first sections,
  schema-friendly headings for the blog engine (70% machine-readability target).
  Adam says the word when he wants it.
- Live slug-confirmation prompt untested with a real draft — will be exercised on the
  next real publish (`--preview` first is the safe habit).
- Intermittent Claude Code classifier outage tonight blocked shell/browser tools;
  workaround: Adam runs commands via `!` prefix. May recur.
