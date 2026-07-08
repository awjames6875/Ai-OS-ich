# CONTEXT.md — Write The Blogs

## Purpose
Turn the questions we already answer on Reddit into 2-4 monthly blog posts on
safeharborbehavioralhealth.com. By draft time, 80% of a post already exists: Room 2 found
the question, Room 3 verified a real citation, Room 5 wrote the answer in Adam's voice.
The blog is that same answer expanded on our own domain — where AI engines cite hardest.

## The Process (Step by Step) — once a month
1. Run `python code/pick_blog_topics.py`
   -> picks top 2-4 topics (UNTAPPED target queries first, then question bank by demand),
      skips anything already in content/blog/, writes output/blog-queue.json
2. Say **"write the blogs"** — the adam-story-blog-engine skill (in /content) drafts each
   queued topic: VOICE_DNA.md FIRST, real Reddit phrasing as H2s, keyword block,
   question-cluster section, FAQ + JSON-LD, only REAL verified citations
   -> drafts land in content/blog/pending/
3. ADAM: read each draft (~5 min each). Your approval = running the publish command.
4. Run `python code/publish_blog.py <slug>` per approved post
   -> commits to the website repo -> Netlify auto-deploys
   -> post moves pending/ -> content/blog/ (published)

## Identity & Audience
- Who uses this room: Adam + the agent, monthly (~30 minutes total)
- What "good" looks like here: posts that read like Adam talking, answer a real question
  in the first 150 words, and start showing up in Room 9's citation checks

## Website Repo
- https://github.com/awjames6875/safeharbor-behavioral-health.git (Vercel auto-deploys, Next.js)
- Confirmed 2026-07-07: posts live in src/data/blogPosts.ts as objects (not files).
  publish_blog.py parses the draft's frontmatter and inserts a BlogPost object at the top
  of that array, then pushes to main -> Vercel deploys at /blog/<slug>. Token has push access.

## Never Do This (Constraints — LOCKED)
- NEVER publish without Adam running the publish command himself (approve-first, always)
- NEVER fabricate a stat, quote, source, or testimonial (honesty lock, FTC healthcare)
- NEVER auto-post anything to Reddit from this room — website only
- Never state a Safe Harbor fact not in the canonical facts file

## 60-30-10 Split For This Room
- 60% (Scripts): pick_blog_topics.py selects topics; publish_blog.py ships approved posts
- 30% (Rules): adam-story-blog-engine-SKILL.md + client-config.md + target-queries.md
- 10% (AI): drafting the posts in Adam's voice — judgment work only

## Skills To Load (Layer 3)
- adam-story-blog-engine (in /content) — the drafting skill
- adam-voice-learning (VOICE_DNA.md) — mandatory before drafting
