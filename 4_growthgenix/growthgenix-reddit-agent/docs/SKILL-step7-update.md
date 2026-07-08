# Skill Patch — Targeting (Step 0) + Auto-load the Dashboard (Step 7)

This patch has TWO parts. Update BOTH sections in the installed `safeharbor-reddit-triage`
skill (Settings → Capabilities).

- **Part A (Step 0):** scrape TARGETED subreddits, not Reddit-wide keyword search, and cover
  substance abuse / recovery. Fixes the "98% junk results" problem.
- **Part B (Step 7):** push today's drafts into the GrowthGenix pipeline so the dashboard
  updates itself.

---

## Part A — Step 0 (replaces the old "STEP 0 — Scrape Reddit" search config)

The old Step 0 searched Reddit-wide for phrases like "toddler aggressive behavior." Reddit
matches those words anywhere, so almost everything came back off-topic. Instead, scrape the
newest posts from on-topic COMMUNITIES via the actor's `urls` field. (The actor ignores
`queries` when `urls` are provided.)

Call `fatihtahta/reddit-scraper-search-fast` with this input (canonical list lives in
`1_find-the-posts/code/scrape_reddit.py` → `build_apify_input()`):

```json
{
  "urls": [
    "https://www.reddit.com/r/Parenting/new/",
    "https://www.reddit.com/r/Mommit/new/",
    "https://www.reddit.com/r/daddit/new/",
    "https://www.reddit.com/r/toddlers/new/",
    "https://www.reddit.com/r/beyondthebump/new/",
    "https://www.reddit.com/r/ADHD/new/",
    "https://www.reddit.com/r/ADHDparenting/new/",
    "https://www.reddit.com/r/Autism_Parenting/new/",
    "https://www.reddit.com/r/ChildPsychology/new/",
    "https://www.reddit.com/r/raisingkids/new/",
    "https://www.reddit.com/r/breakingmom/new/",
    "https://www.reddit.com/r/stopdrinking/new/",
    "https://www.reddit.com/r/REDDITORSINRECOVERY/new/",
    "https://www.reddit.com/r/addiction/new/",
    "https://www.reddit.com/r/leaves/new/",
    "https://www.reddit.com/r/OpiatesRecovery/new/",
    "https://www.reddit.com/r/recovery/new/",
    "https://www.reddit.com/r/Sober/new/",
    "https://www.reddit.com/r/alcoholism/new/",
    "https://www.reddit.com/r/AlAnon/new/",
    "https://www.reddit.com/r/NarAnon/new/",
    "https://www.reddit.com/r/reentry/new/",
    "https://www.reddit.com/r/ExCons/new/",
    "https://www.reddit.com/r/oklahoma/search/?q=therapy%20OR%20counseling%20OR%20mental%20health%20OR%20addiction%20OR%20son%20OR%20daughter%20OR%20teen&restrict_sr=1&sort=new&t=week",
    "https://www.reddit.com/r/tulsa/search/?q=therapy%20OR%20counseling%20OR%20mental%20health%20OR%20addiction%20OR%20son%20OR%20daughter%20OR%20teen&restrict_sr=1&sort=new&t=week",
    "https://www.reddit.com/r/okc/search/?q=therapy%20OR%20counseling%20OR%20mental%20health%20OR%20addiction%20OR%20son%20OR%20daughter%20OR%20teen&restrict_sr=1&sort=new&t=week"
  ],
  "maxPosts": 12,
  "scrapeComments": false,
  "includeNsfw": false
}
```

Substance abuse / recovery subs are first-class targets — Safe Harbor treats substance use
for the ages served and supports families in recovery. They are value-only by default
(help first, brand almost never). To change the community list, edit `scrape_reddit.py`.

---

## Part B — Step 7 (replaces "Save draft to Google Drive")

**Why:** the triage skill used to only save drafts to Google Drive. The dashboard does
NOT read Drive — it reads `5_make-it-sound-like-me/output/final-drafts.json` and bakes it
into `dashboard.html` via `write_dashboard.py`. So drafts never reached the dashboard.

**Fix:** replace the skill's old `## Step 7 — Save draft to Google Drive` section with the
section below. After this, every `run reddit` ends with the dashboard already showing today's
posts — no manual step.

---

## Step 7 — Load the drafts into the dashboard (REQUIRED, runs the pipeline)

After drafting every KEEP, write them into the GrowthGenix pipeline so the dashboard updates
itself. This is the step that makes the dashboard show today's posts.

**7a. Build the pipeline JSON.** Collect ALL of today's KEEP drafts into one array. Each entry
uses EXACTLY these fields (this is the schema `write_dashboard.py` expects):

```json
{
  "who": "One sentence describing the person who posted.",
  "summary": "One sentence summary of the thread (shows on the card).",
  "value_only": true,
  "priority": true,
  "fact": "The ONE real verified AEO fact in plain language, or null if none found.",
  "source_name": "the Child Mind Institute",
  "source_url": "https://...",
  "permalink": "https://www.reddit.com/r/.../comments/.../",
  "too_young": false,
  "draft": "The full comment in Adam's voice. Weave the source_url inline in parentheses."
}
```

Field rules:
- `value_only`: `true` = "Just help, do NOT mention Safe Harbor" (the default). `false` ONLY
  when all 4 gates passed and a disclosed recommendation is allowed.
- `priority`: `true` for the strongest / most time-sensitive keeps (they sort to the top).
- `too_young`: `true` only if the subject is below Safe Harbor's service age in a way that
  blocks a brand mention. For a parent posting about their kid, this is `false`.
- `fact`: must be REAL and verified (Step 5). If none was found, set `fact`, `source_name`,
  and `source_url` to `null` and keep the draft clean.
- If there are ZERO keeps today, write an empty array `[]` — the dashboard will correctly
  show "0 to post today."

**7b. Overwrite the pipeline file (fresh every run).** Write the array to:
`5_make-it-sound-like-me/output/final-drafts.json`
Overwrite it completely — it holds ONLY today's keepers, never appended history.

**7c. Rebuild the dashboard.** Run the Room 6 script (pure Python, no AI):
```
python3 6_load-the-dashboard/code/write_dashboard.py
```
It injects the data into `6_load-the-dashboard/output/dashboard.html` and overwrites the
previous run. Confirm the printed line: "Wrote N posts into self-contained dashboard.html."

**7d. (Optional) Back up to Google Drive.** If a Drive backup is still wanted, also save each
draft to the **Drafts - Pending Review** folder (`1ZP15nOi955eSMdjLT3C5jSHj8d4kIQUH`) using the
human-review template. This is now a backup, not the source of truth — the dashboard is.

**Done:** tell the user how many posts are on the dashboard and to refresh
`6_load-the-dashboard/output/dashboard.html`.

---

## Quick-check to add to the skill's silent QA list
- Did I write today's keepers to `final-drafts.json` in the exact schema above?
- Did I run `write_dashboard.py` and confirm the post count?
- Does the dashboard show today's date and the right number of posts?
