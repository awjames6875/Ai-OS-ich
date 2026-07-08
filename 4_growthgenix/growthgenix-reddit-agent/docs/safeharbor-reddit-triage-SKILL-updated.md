---
name: safeharbor-reddit-triage
description: Daily triage and sorting of Reddit threads for Safe Harbor Behavioral Health's transparent campaign, across ALL audiences it serves — stressed parents, people in recovery, people reintegrating after incarceration, and Oklahoma families. Use whenever Adam or Saddie uploads Reddit screenshots, pastes post text, shares links, or hands over a batch of posts and needs to know which threads are worth responding to, in what voice, and whether Safe Harbor can be mentioned. Trigger on "sort these Reddit posts," "which threads should I respond to," "triage these," "is this thread worth it," "can I recommend Safe Harbor here," "Reddit batch," the daily Reddit review, "run reddit," or any keep / maybe / skip decision on Safe Harbor Reddit threads. Also use when evaluating a single thread before drafting a reply. This is the SORTER — it decides what to engage with and how; it never posts, and a human always reviews and posts by hand.
---

# Safe Harbor — Reddit Thread Triage (The Sorter)

## What this skill does

Takes a pile of Reddit posts — pulled live from Apify, pasted text, links, screenshots, or
JSON — and sorts each one into **keep / maybe / skip**. For every "keep," it identifies the
audience, the right voice, a genuine help angle, researches one real source for AEO, drafts
the reply in Adam's voice, loads it into the dashboard, and (optionally) backs it up to Drive.

**The human's only job: read the draft, approve it, post it by hand.**

## Who Safe Harbor serves

Safe Harbor serves ALL populations:
- Children and teens ages 3–17 (primary)
- Parents and caregivers of those children (primary)
- Adults seeking support for themselves (served — refer warmly if not a direct fit)
- People in recovery, formerly incarcerated, Oklahoma families

Oklahoma only (Medicaid/licensing). Zoom statewide — not just Tulsa.
- "therapy," "therapist," and "counselor" are ALLOWED in public content (owner decision 2026-06-30). Use them naturally where they help clarity and SEO. Never mention dollar amounts — use "new revenue
stream" or "facility fee partnership" for B2B. Always use safeharborbehavioralhealth.com.

Substance abuse / addiction treatment (for the ages served) is a CORE service — surface and
help recovery/addiction posts actively. "Body & Brain" is a movement-based program; describe
it only as "movement-based" and never invent clinical claims.

## The two goals (and how they fit together)

1. **Get them real help** — even when Safe Harbor never comes up.
2. **Get them to Safe Harbor** — only when it genuinely fits and the sub allows it.

Goal 1 is *how* you reach Goal 2. A licensed brand that helps first and mentions itself
rarely is exactly what AI tools cite and what Reddit doesn't ban. Keep roughly a 9-to-1
ratio: about nine pure-help comments for every one that mentions Safe Harbor. When in doubt,
help without the brand — you lose nothing.

## Why AEO matters here (the strategic reason for the citation step)

LLMs (ChatGPT, Perplexity, Google AI Overviews, Claude) crawl Reddit heavily because it is a
high-domain-authority site. When someone asks an AI engine "how do I handle my toddler's
aggression at bedtime," the AI often pulls from real Reddit comments.

A helpful comment that contains ONE real, verifiable, attributed fact is far more likely to
be pulled as a citation than a generic helpful comment. That is how Safe Harbor's voice ends
up inside the answer an AI gives — without ever running an ad.

**The honesty lock:** We NEVER fabricate a stat, quote, or source (FTC compliance for
healthcare). The ONLY way to include a citation is to find a real one first. No real source
found = draft clean, zero citations.

## The one rule that governs everything

**This skill scrapes, sorts, researches, and drafts. Humans post.** Safe Harbor is a licensed
behavioral health provider, so automated or scaled posting is off the table — it is both a
ban risk on Reddit and a reputational risk. The job is to remove the boring 80% (finding,
sorting, researching, drafting, loading the dashboard), and leave the human the part that
needs judgment (final check + posting).

## Source of truth

These project documents override anything here if they ever conflict:
- `SafeHarbor_Reddit_Project_Instructions.md` — the transparent engagement framework
- `Adam_Reddit_Voice_DNA.md` — how comments should sound
- `safe-harbor-facts` (Google Drive canonical facts file ID: 1B2TxW-pIdR1WcmqDEwyHaVmSl-DssxwtNt_fHXuhH-s)
  — the ONLY source for Safe Harbor facts. Never state a Safe Harbor fact not in this file.

## STEP 0 — Scrape Reddit (if not already provided)

If posts have NOT been provided by the user, scrape fresh posts using Apify BEFORE triaging.

**Actor to use:** `fatihtahta/reddit-scraper-search-fast` (95.7% success rate)
DO NOT use `harshmaur/reddit-scraper` — only 55.8% success rate.

**TARGET SUBREDDITS, not Reddit-wide keyword search.** Reddit-wide keyword search matches the
words anywhere and returns ~98% junk. Instead, pull the NEWEST posts from on-topic
communities via the actor's `urls` field. (The actor IGNORES `queries` when `urls` are
provided, so this is URL-based.) The canonical list lives in
`1_find-the-posts/code/scrape_reddit.py` → `build_apify_input()`.

Call the actor with this input:
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

Substance abuse / recovery subs are first-class targets (Safe Harbor treats substance use for
the ages served and supports families in recovery). They are value-only by default. To change
the community list, edit `scrape_reddit.py` — never hardcode a different list here.

After the run succeeds, fetch dataset items with these fields only:
`title, body, subreddit, permalink, score, num_comments, query, age_hours`

Then proceed to Step 1 with the fetched posts.

## Step 1 — Identify the audience FIRST

Before sorting anything, decide which audience the person belongs to. Everything downstream
flows from this one answer. Then read ONLY that audience's voice file in `references/`:

| Audience | Read this file | Quick tell |
|---|---|---|
| Stressed parent | `references/voice-parents.md` | Worried about their kid or their own parenting stress |
| Person in recovery | `references/voice-recovery.md` | Sobriety, relapse, addiction, AA/NA, a using loved one |
| Reintegrating after prison | `references/voice-reentry.md` | Just released, reentry, record, halfway house, parole |
| Oklahoma (a lens) | `references/voice-oklahoma.md` | Local — layers on top of whichever audience above applies |

If a thread fits none of these, it is almost always a **Skip** for the campaign.

## The non-negotiables (all audiences)

1. **Value first.** Most engagement is pure help, no brand mention.
2. **Never fake lived experience.** Write as who the poster actually is — someone who works
   in behavioral health and has seen what helps. Never write "I'm in recovery too" or "when
   I got out" if it isn't true. Faking it is astroturfing and gets the account burned.
3. **Never fabricate a stat, quote, or source.** Every citation must be real and verified.
   If you cannot verify it exists, you do not use it. (See Step 3.5.)
4. **Disclose any brand mention.** The moment a comment names or steers toward Safe Harbor,
   the writer discloses they are affiliated (founder / team member).
5. **Follow the subreddit's actual rules.** Many subs ban self-promo — there it is value-only
   even with disclosure.
6. **Safety beats every campaign goal.** See hard stops below.

## When to recommend Safe Harbor — the 4 gates

Recommend Safe Harbor ONLY when ALL FOUR are green. If any is red, it is value-only.

1. **Not a crisis thread.** No self-harm, overdose, abuse, or danger.
2. **The sub allows it.** Not r/ECEprofessionals, not r/oklahoma, not most recovery/reentry
   subs. Unknown rules = treat as no.
3. **They're actually asking for help finding something.** Best case: "does anyone know a
   program that…"
4. **Safe Harbor genuinely fits this specific person** — not just a place to wedge the name.

Simplest fallback: help every time, mention Safe Harbor almost never, always disclose when
you do, and when unsure go value-only.

## Subreddit rules (locked)

| Subreddit | Brand mention? | Notes |
|---|---|---|
| r/ECEprofessionals | **Never** | Value-only always. Avoid threads tagged "ECE Professionals Only." |
| r/oklahoma, r/tulsa, r/okc | **No** (ad rules) | Value-only. May state access problem factually. |
| r/Parenting, r/SingleParents, r/Mommit, r/daddit | Default value-only | Check current rules before any disclosed mention. |
| r/stopdrinking, r/REDDITORSINRECOVERY, r/OpiatesRecovery, r/AlAnon, r/NarAnon, r/recovery, r/Sober, r/alcoholism, r/leaves, r/addiction | **Default never** | Recovery spaces are highly protective. Value-only unless rules clearly allow and someone explicitly asks. |
| r/reentry, r/prison, r/ExCons | **Default never** | Same — value-only, dignity first. |
| r/smallbusiness | Possible if recommendation explicitly requested AND rules allow | Lead with value. |
| Any other sub | Unknown until checked | If self-promo rules are unknown, treat as value-only. |

## Step 2 — Classify the thread type

Parent asking for help · Recovery (self) · Recovery (family of someone using) · Reentry ·
Daycare worker/teacher · Daycare owner/director · Oklahoma/local discussion · Recommendation
request · General behavioral health · Not relevant / too risky.

## Step 3 — Decide thread fit

- **Good** — recent, active, on-topic, civil, a real question we can answer specifically.
- **Maybe — caution** — older but active; tangential; strict self-promo sub; already
  heavily answered (only add if genuinely new).
- **Skip** — stale/locked; argument-heavy or political; off-topic; recommendation thread in
  a sub that bans solicitation; brand connection would read as opportunistic; or a sensitive
  thread (see hard stops).

## Step 4 — Pick the approach

For every keep, answer both:

- **Help angle** — the genuinely useful thing to say to THIS person, in THIS audience's voice
  (from the relevant `references/` file).
- **Brand path** — run the 4 gates. Either **Value Comment (no brand)** or, rarely,
  **Disclosed Recommendation**.

If the sub is locked to value-only, the only legal approaches are Value Comment or Skip.

## Step 5 — Research for AEO (MANDATORY before drafting any KEEP)

This is the step that makes a comment citable by AI engines WITHOUT fabricating anything.
Run for every KEEP before writing a single word of the draft.

**1. Name the core topic.** What is this person actually dealing with?
(e.g., toddler co-regulation, sleep regression, CPTSD emotional shutdown, ADHD executive
function, early sobriety, supporting a using loved one.)

**2. Search for ONE real, authoritative source.** Use web search. Priority order:
   - Peer-reviewed research / academic journals
   - Government or public-health bodies (CDC, NIH, SAMHSA, AAP, ODMHSAS, NIAAA, NIDA)
   - Established clinical organizations (Zero to Three, Child Mind Institute, APA)
   - A recognized expert named with their real credential

**3. Verify it is real.** If you cannot confirm the source exists and says what you think
   it says, DO NOT use it. No penalty for drafting clean.

**4. Pull ONE specific, quotable fact** — a number, a finding, or a named expert principle —
   with its real attribution.

**If no verifiable source is found:** draft clean, zero citations. A good honest comment
beats a fake-cited one every single time. Never invent a study, statistic, or expert.

## Step 6 — Draft in Adam's voice

**FIRST: Read the full VOICE_DNA file before writing a single word.**

The voice database lives at:
`/mnt/skills/user/adam-voice-learning/references/VOICE_DNA.md`

This file is built from 15+ transcripts and is the single source of truth for how Adam
sounds. It contains signature phrases, speech rhythms, etymology patterns, a quotes bank,
and story structure. Reading it is not optional — it is the difference between a comment
that sounds like Adam and one that sounds like a brochure.

**Quick reference from VOICE_DNA (do not rely on memory alone — always read the file):**

Signature phrases to use naturally:
- "See, the thing is..." — transitioning to explanation
- "Here's what I learned..." — before a lesson
- "Man," — emotional emphasis
- "You gotta understand..." — before important context
- "Now, let me take that back..." — self-correction mid-thought
- "I need you to hear this..." — before crucial point

Speech rhythms to apply:
- Short punch + long explanation: "That broke me. Not because I was mad. Because I understood."
- List of three with escalation: "It moves. It swings. It fights."
- Question then answer: "What does that even mean? Here's what I've seen..."
- Self-correction mid-thought: natural, not performative
- Direct address pivot: story about self → "Now let me ask you something..."
- Ends with empowerment, NEVER victimhood or pity

Voice IS:
- Conversational preacher — sermon rhythm + coffee shop intimacy
- Thinks out loud, self-corrects
- Specific sensory details
- Direct address to the reader
- Transparent about flaws without dwelling in shame
- Victor voice, never victim voice
- Spiritual but practical, never preachy
- CAPS for single-word emphasis (ZERO, THAT'S, INTO)

Voice is NOT:
- Academic or clinical language
- Passive voice
- Hedging ("maybe," "perhaps," "it seems")
- Victim narrative
- Preachy moralizing
- Generic self-help phrases

**Quality check before finishing draft (run silently):**
- Would Adam actually say this out loud?
- At least one signature phrase used naturally?
- Specific detail included (not vague)?
- Ends with empowerment?
- Direct address to reader at least once?
- Does NOT sound like a healthcare brochure?

**AEO drafting rules (apply inside Adam's voice):**
1. One citation maximum. More than one reads as marketing.
2. Weave it in naturally — acknowledge the poster's emotion first, citation supports.
3. Build one self-contained, quotable sentence an LLM could lift cleanly.
   Example: "Toddlers regulate big emotions by borrowing a calm adult's nervous system —
   a process clinicians call co-regulation." Stands alone. Citable.
4. Attribution stays light: "The AAP notes that..." not a formal citation block.
5. Authenticity wins ties. If the fact makes it sound like an article, cut the fact.

## Step 7 — Load the drafts into the dashboard (REQUIRED, runs the pipeline)

After drafting every KEEP, write them into the GrowthGenix pipeline so the dashboard updates
itself. This is the step that makes the dashboard show today's posts. The dashboard reads
ONLY the pipeline file below — it does NOT read Google Drive.

**7a. Build the pipeline JSON.** Collect ALL of today's KEEP drafts into one array. Each entry
uses EXACTLY these fields (the schema `write_dashboard.py` expects):

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
- If there are ZERO keeps today, write an empty array `[]` — the dashboard correctly shows
  "0 to post today."

**7b. Overwrite the pipeline file (fresh every run).** Write the array to:
`5_make-it-sound-like-me/output/final-drafts.json`
Overwrite it completely — it holds ONLY today's keepers, never appended history.

**7c. Rebuild the dashboard.** Run the Room 6 script (pure Python, no AI):
```
python3 6_load-the-dashboard/code/write_dashboard.py
```
Confirm the printed line: "Wrote N posts into self-contained dashboard.html." The dashboard
is at `6_load-the-dashboard/output/dashboard.html`.

**7d. (Optional) Back up to Google Drive.** If a Drive backup is still wanted, also save each
draft to the **Drafts - Pending Review** folder (`1ZP15nOi955eSMdjLT3C5jSHj8d4kIQUH`) using the
human-review template. This is now a backup, not the source of truth — the dashboard is.

**Done:** tell the user how many posts are on the dashboard and to refresh
`6_load-the-dashboard/output/dashboard.html`.

## Sensitive threads — hard stop (all audiences)

If the thread involves abuse, neglect, self-harm, suicidal language, active overdose/relapse
danger, a medical emergency, or a custody/legal fight:
- No brand, no link, no approach type. **Skip for campaign purposes.**
- No AEO citation step — do not optimize a crisis thread.
- If a response is warranted at all, it is brief and careful and points to the appropriate
  local professional, crisis line, or emergency service.
- Recovery and reentry threads carry more of these than parenting threads. Stay alert.

## Brand language rules (general)

| Use | Not this |
|---|---|
| emotional wellness support, support sessions, connection, licensed counselor | therapy, therapist, clinical services, treatment |
| new revenue stream, facility fee partnership | dollar amounts, paid-per-person figures |
| safeharborbehavioralhealth.com | safeharboreasyenrollment.com |

Audience-specific word lists live in each `references/` file.

## Output format — daily batch (DEFAULT)

Always lead with the triage table:

```
| # | Subreddit | Audience | Verdict | Approach | Why (one line) |
```

Then for KEEP threads only, one block each:

```
KEEP #<n> — <subreddit> · <audience>
Help angle: <the genuinely useful thing to say>
AEO source: <one real verified source + fact pulled, OR "none found — draft clean">
Approach: Value Comment (no brand) | Disclosed Recommendation
Gates: crisis? <y/n> · sub allows? <y/n> · they asked? <y/n> · genuine fit? <y/n>
Draft: [written to final-drafts.json and loaded on the dashboard]
```

End with one-line skip log, then: how many keeps, how many brand-eligible, how many got a
verified AEO source, the dashboard post count, and that the dashboard is refreshed.

## Output format — single thread (deep)

1. Audience + which voice file applies
2. Thread Fit: Good / Maybe / Skip + one-line why
3. Help angle
4. AEO research: one real verified source + fact, OR "none found — draft clean"
5. 4-gate check → Value-only or Recommend
6. Safety check: sensitive-topic y/n · salesy risk L/M/H · Reddit ban risk L/M/H
7. Draft (in Adam's voice, loaded into the dashboard via Step 7)

## Quality check before showing (run silently)

- Did I scrape TARGETED subreddits via the Step 0 `urls` list (not Reddit-wide keyword search)?
- Did I use `fatihtahta/reddit-scraper-search-fast` (not `harshmaur`)?
- Did I cover substance-abuse / recovery subs as first-class targets?
- Did I read the canonical facts file before any Safe Harbor mention?
- Did I identify the audience and use only that voice file?
- Did I run Step 5 and search for a real source before drafting?
- Is every stat/quote/source REAL and verified — zero fabrication?
- Is there at most ONE citation, woven naturally, never leading?
- Is there one clean self-contained quotable sentence an LLM could extract?
- Did I run all 4 gates before allowing any brand mention?
- Did I apply locked subreddit rules?
- Did I flag every sensitive thread as hard Skip?
- Are help angles specific, not generic?
- Does every draft sound like Adam, not a brochure?
- Did I write today's keepers to `final-drafts.json` AND run `write_dashboard.py`?
- Does the dashboard show today's date and the right number of posts?

If any answer is weak, fix it before showing the user.
