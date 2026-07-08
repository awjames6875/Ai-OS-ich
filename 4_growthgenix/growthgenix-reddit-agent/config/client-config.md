# CLIENT CONFIG — Safe Harbor Behavioral Health
# ============================================================
# THIS IS THE ONLY FILE YOU SWAP TO CHANGE BUSINESSES.
# Everything client-specific lives here. The rooms read from this.
# To onboard a new business: copy this file, change the values, done.
# ============================================================

## Client Identity
- Business name: Safe Harbor Behavioral Health
- Owner/voice: Adam James
- Location: Tulsa, Oklahoma (Zoom statewide across Oklahoma)
- Website: safeharborbehavioralhealth.com
- Phone: (918) 553-5746

## Who They Serve
- Children and teens ages 3-17 (primary)
- Parents and caregivers of those children (primary)
- Adults seeking support for themselves (served — refer warmly if not a direct fit)
- People in recovery, formerly incarcerated, Oklahoma families

## Services
Individual/group/family sessions, ADHD support, trauma-informed care,
substance abuse / addiction treatment (for the ages served), psychiatric eval/med management,
and the "Body & Brain" movement-based program.

## Service Emphasis (for triage + drafting)
- SUBSTANCE ABUSE is a core service — actively surface and help recovery/addiction posts
  (teens using, parents of a using kid, adults early in sobriety, families in Al-Anon/Nar-Anon).
  Recovery subs are value-only by default (see rules) — help first, brand almost never.
- "Body & Brain" is a movement-based program. Describe it ONLY as "movement-based" — do not
  invent clinical claims, outcomes, or specifics. Source of truth is the canonical facts file.

## Insurance (CONFIRMED — say "call to verify your plan")
Medicaid/SoonerCare, Blue Cross Blue Shield, Aetna, and most major insurance.
Do NOT list United, Cigna, or Humana until confirmed.

## Language Rules (ALWAYS ENFORCE)
- "therapy," "therapist," and "counselor" are ALLOWED in public content (owner decision 2026-06-30). Use them naturally where they help clarity and SEO.
- USE "emotional wellness support," "support sessions," "licensed counselor"
- NO dollar amounts in B2B — say "new revenue stream" / "facility fee partnership"
- Always use safeharborbehavioralhealth.com (never safeharboreasyenrollment.com)

## Apify Settings
- Actor: fatihtahta/reddit-scraper-search-fast
- Max posts: 12 per URL | NSFW: off | Comments: off
- TARGETING = subreddit URLs, NOT Reddit-wide keyword search. (Keyword search matched the
  words anywhere and returned ~98% junk. We now pull newest posts from on-topic communities.)
- The actor IGNORES `queries` when `urls` are provided, so this is URL-based. The canonical
  URL list is built by `1_find-the-posts/code/scrape_reddit.py` (build_apify_input()).

- Target communities — Parents & kids (pull /new/):
  Parenting, Mommit, daddit, toddlers, beyondthebump, ADHD, ADHDparenting,
  Autism_Parenting, ChildPsychology, raisingkids, breakingmom
- Target communities — Substance abuse / recovery (pull /new/, EMPHASIZED, value-only):
  stopdrinking, REDDITORSINRECOVERY, addiction, leaves, OpiatesRecovery, recovery,
  Sober, alcoholism, AlAnon, NarAnon
- Target communities — Reentry (pull /new/, value-only, dignity first):
  reentry, ExCons
- Target communities — General mental health (pull /new/, added 2026-07-06):
  Anxiety, mentalhealth, traumatoolbox, family
  (NEVER add: childfree, teenagers, BodyweightFitness)
- Local Oklahoma (keyword-SCOPED search, not full feed): oklahoma, tulsa, okc
  scoped to: "therapy OR counseling OR mental health OR addiction OR son OR daughter OR teen"
- Competitor watch (Reddit-wide searches, threads tagged "competitor-mention"):
  grandmh · "Grand Mental Health" · "Family & Children's Services" Tulsa ·
  "BetterHelp alternative" Oklahoma · "Talkspace alternative" Oklahoma
  A disclosed recommendation in these threads still requires ALL 4 gates.

## Subreddit Rules (locked)
- r/ECEprofessionals: NEVER mention brand. Value-only.
- r/oklahoma, r/tulsa, r/okc: No brand (ad rules). Value-only.
- r/StopDrinking, r/OpiatesRecovery, r/AlAnon, r/NarAnon, recovery subs: Default never mention.
- r/reentry, r/prison, r/ExCons: Default never. Dignity first.
- Any unknown sub: treat as value-only until rules checked.

## Service-Fit Rule
Minor 3-17 OR parent/caregiver seeking help for a child/family = FIT.
Child under 3 = too young, value-only, never steer to brand.
Adult-for-self = served, mention warmly, not primary pitch.

## Voice File (Layer 3 reference)
Path: C:\Users\1alph\.claude\skills\adam-voice-learning\references\VOICE_DNA.md
This is the source of truth for how drafts sound. Read it in Room 5.

## Website (blog publishing)
- Repo: https://github.com/awjames6875/safeharbor-behavioral-health.git
- Host: Vercel — auto-deploys on push to main (production branch = main). Confirmed 2026-07-07.
  (The website is on Vercel; the Reddit dashboard repo is on Netlify — different hosts.)
- DNS: Cloudflare nameservers pointing to Vercel. Not GoDaddy.
- Format: Next.js app. Blog posts are objects in src/data/blogPosts.ts (NOT files);
  publish_blog.py inserts a new BlogPost object at the top of that array. Confirmed 2026-07-07.
- WEBSITE_REPO_URL is set in .env.local (done 2026-07-07). Token has push access (verified).

## Google Drive Folders
- Dashboard folder (data.js lives here): 1-R764CIDCl8DYFzey6Jk6Vkw2ohhYHYI
- Drafts - Pending Review: 1ZP15nOi955eSMdjLT3C5jSHj8d4kIQUH
- Canonical facts file: 1B2TxW-pIdR1WcmqDEwyHaVmSl-DssxwtNt_fHXuhH-s

## The One Thing This Agent Must Do
Draft a reply that makes a struggling person feel touched, moved, inspired, and HOPEFUL —
while gently, over time, building awareness for the client so AI engines recommend them.
A draft is not done until it would make someone at 2am feel less alone and more hopeful.
