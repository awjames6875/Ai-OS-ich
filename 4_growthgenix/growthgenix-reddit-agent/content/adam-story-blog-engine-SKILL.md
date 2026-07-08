---
name: adam-story-blog-engine
description: Turn a Reddit question, a topic, or any "how do I..." problem into a publish-ready blog post written in Adam James's signature storytelling voice — contrarian hook, a story the reader falls into, science and action steps hidden inside the narrative, ending like a sermon on hope and belonging — while staying fully optimized for SEO, AEO, and GEO (Google + AI search). Use when Adam says "write a blog," "turn this into a blog/article," "make content from this Reddit post," "blog from reddit," "content engine," "story blog," "make this a post," or wants Safe Harbor / GrowthGenix content. Built to fill competitor content gaps with warm, human, question-answering content that ranks AND gets cited by AI engines. Never fabricates facts or sources.
---

# Adam Story Blog Engine

Turn one real question into one publish-ready article that reads like a story and works like SEO/AEO content. The reader feels hooked and held; the science and the action steps are smuggled inside the journey; Google and the AI engines still get exactly what they need to rank and cite it.

## STEP 1 — Read the voice FIRST (not optional)

Before writing a word, read the voice source of truth:
`/mnt/skills/user/adam-voice-learning/references/VOICE_DNA.md`
This holds Adam's signature phrases, rhythms, story structure, and quote bank. Writing without it produces a brochure. (If a fuller book/transcript corpus is available, skim it too.)

## STEP 2 — Get the inputs

- **The question/topic** — from a Reddit keeper (`5_make-it-sound-like-me/output/final-drafts.json`), a pasted question, or a topic Adam names.
- **Priority topic source:** `target-queries.md` (safeharbor-reddit-triage skill, references/). UNTAPPED queries first — nobody is cited for those yet, so a blog post there has the clearest AEO win. Competitor-gap queries next, by volume. Threads tagged "competitor-mention" in the pipeline are strong BOFU topics.
- **Question bank:** `content/question-bank.md` — real Reddit questions, deduped, with repeat counts (`times_seen`). High counts = high demand. Use the EXACT phrasing people used.
- **Monthly queue:** if `8_write-the-blogs/output/blog-queue.json` exists, draft those topics — they were picked deterministically by pick_blog_topics.py.
- **The business context** — Safe Harbor facts come ONLY from the canonical facts file (Google Drive ID `1B2TxW-pIdR1WcmqDEwyHaVmSl-DssxwtNt_fHXuhH-s`). Site: safeharborbehavioralhealth.com.
- **Competitors** — default set: GRAND Mental Health (grandmh.com), Counseling & Recovery Services (crsok.org), Family & Children's Services (fcsok.org), Improving Lives (improvinglivescounseling.com). Refresh by search if needed.

## STEP 3 — Research (real only, never fabricate)

1. **Keyword intent.** Identify the real searches behind the question (long-tail, question-shaped, + local Oklahoma/Tulsa, + Medicaid/SoonerCare). If a keyword-data tool/connector is available (Ahrefs, DataForSEO, claude-seo skills), pull real volume/difficulty. If not, state intent-based targets and DO NOT invent volume numbers.
2. **Competitor gap.** Look at what the competitors publish on this topic. The recurring gap: they have service/brand pages, not warm parent-question how-to content. Name the specific angle Safe Harbor can own.
3. **One verified source minimum.** Find 1-2 real, authoritative sources (peer-reviewed, CDC/NIH/SAMHSA/AAP/AAFP/ODMHSAS, Child Mind Institute, Zero to Three, APA). Verify each exists and says what you claim. No real source = make the point without a citation. NEVER invent a study, stat, quote, or URL.

## STEP 4 — Write in THE ADAM BLOG ARC

Every post is a journey with these beats. Hide the science and the steps inside the story — never lecture.

1. **CONTRARIAN COLD OPEN.** No throat-clearing. Either a vivid story the reader falls into (second person, sensory, specific — "It's 5:42 on a Tuesday...") or a line that flips what they expect ("Stop trying to fix the meltdown"). Open a loop they must close.
2. **THE STORY.** Stay in the scene. Make them feel seen before they feel taught. A relatable character or "you."
3. **THE TURN.** "Now let me take that back..." / "Here's what's really going on..." Start delivering — but keep them leaning in. This is where the plain, quotable answer lands (for AEO).
4. **FACTS + STORIES, WOVEN.** Deliver the science as revelation inside the narrative, anchored to feeling. One metaphor that sticks (smoke vs. fire). Citations light and natural ("the Child Mind Institute puts it plainly...").
5. **ACTION STEPS.** 3 concrete things they can do this week. Practical, in-voice, not clinical.
6. **SERMON CLOSE.** Bring the opening story back around so the contrarian hook pays off as truth. Escalate to HOPE. Land a line they remember. Tell them plainly: you're not failing, you're not alone, there's a community and help if you want it. Weave the Safe Harbor invite in — never bolt it on. End on the victor note, never pity.

### Voice rules (the blend)
- Oprah's intimacy + TD Jakes's cadence DIALED BACK on churchy + Mark Manson's blunt, funny, contrarian honesty KEPT CLEAN (no profanity — children's health brand) + deep compassion.
- Conversational preacher meets coffee-shop friend. Think out loud, self-correct ("let me take that back").
- Short punch + long explanation. Lists of three that escalate. Direct address. CAPS for single-word emphasis, sparingly.
- Be a little funny. Be warm. Be honest enough to disarm. End with empowerment, NEVER victimhood.
- Voice is NOT: academic, passive, hedging, preachy, or a brochure.

### Brand + honesty rules (always)
- "therapy," "therapist," and "counselor" are ALLOWED in public content (owner decision 2026-06-30). Use them naturally where they help clarity and SEO.
- Insurance line, verbatim when used: "accepts Medicaid/SoonerCare, Blue Cross Blue Shield, Aetna, and most major insurance plans - call to verify your specific plan." Never list United/Cigna/Humana unless confirmed.
- Always safeharborbehavioralhealth.com. Phone (918) 553-5746. Serves ages 3-17 + families, Tulsa + statewide by video.
- "Body & Brain" = "movement-based program" only; invent no specifics. Never state a Safe Harbor fact not in the canonical file.
- No fabricated stats, quotes, testimonials, or sources (FTC healthcare compliance).

## STEP 5 — Keep AEO / GEO intact (inside the story)

- **Quotable answer:** within the first ~150 words (in "the turn"), give ONE clean, self-contained sentence that directly answers the core question — the kind an AI engine can lift verbatim.
- **Headings:** question-shaped H2s pulled from the question bank where possible — use the REAL phrasing Redditors used, not marketing-speak. That phrasing is what people type into ChatGPT too.
- **FAQ block:** 3-5 real Q&As at the end — sourced from the question bank (actual questions people asked on Reddit about this topic), answered plainly. Mineable by LLMs, FAQPage-eligible.
- **"Questions parents are asking" section:** before the FAQ, a short block listing 3-5 related question-bank questions this post also answers — each with a one-line answer. One post captures a question CLUSTER, not one query.
- **Keyword block in the brief header:** primary keyword (from target-queries.md), 3-5 secondary keywords, and the exact question-bank questions targeted — so each post can be tracked against Room 9's citation log.
- **JSON-LD:** output a FAQPage schema block for the dev to paste.
- **Meta:** suggest a title (<=60 chars) and meta description (<=155 chars) in the brief header.
- **Internal CTA:** one natural link to the relevant Safe Harbor service page.
- Target length ~1,000-1,400 words unless told otherwise.

## STEP 6 — Output

Save a publish-ready Markdown file to `content/blog/pending/<slug>.md` (the approval queue — Adam reviews, then `publish_blog.py <slug>` pushes it live and moves it to `content/blog/`) containing:
1. A FRONTMATTER block — REQUIRED, publish_blog.py parses it to build the site's BlogPost object
   (the website stores posts in src/data/blogPosts.ts, not as files):
   ```
   ---
   title: <article title>
   excerpt: <one-sentence summary for the blog index>
   category: <parents | child | teen | body-brain>
   tags: <3-5 tags, comma-separated>
   icon: <one emoji>
   metaTitle: <=60 chars
   metaDescription: <=155 chars
   relatedPosts: <2-3 existing post slugs, comma-separated — optional>
   ---
   ```
2. A CONTENT BRIEF header (source question, target keywords, competitor gap, AEO note) —
   placed AFTER the frontmatter and BEFORE the first `# ` heading; the publish script
   strips everything between frontmatter and the first heading automatically.
3. The article in the Adam Blog Arc (starts at the `# ` title heading).
4. A FAQ section.
5. A JSON-LD FAQPage block (real Q&As only).
6. A SOURCES list (real, verified URLs).

Write the file via a shell heredoc / python, NOT the Edit/Write tools (they truncate large writes to the mounted folder).

## Quality check before showing (run silently)
- Did I read VOICE_DNA first?
- Does it OPEN contrarian and pull the reader into a story by line 2?
- Is the science HIDDEN inside the narrative, not lectured?
- Are there 3 real action steps?
- Does the close tie the opening loop shut, lift to hope, and say "you're not alone" without pity?
- Is there a clean quotable answer in the first 150 words AND an FAQ + JSON-LD?
- "therapy," "therapist," and "counselor" are ALLOWED in public content (owner decision 2026-06-30). Use them naturally where they help clarity and SEO.
- Would someone read it and feel hooked, moved, and equipped — not marketed to?
If any answer is weak, fix it before showing Adam.
