# Claude Code Work Order — Ai-OS-ich Architecture Fix
# Prepared by: Jake Methodology Advisor
# Date: 2026-05-31
# Repo: github.com/awjames6875/Ai-OS-ich

---

## WHO YOU ARE WORKING FOR

Adam James — builder, not a traditional developer.
This is his AI Operating System for 4 businesses:
- ICH (corporate housing — 9 properties in Tulsa)
- Safe Harbor Behavioral Health
- GrowthGenix (AI agency)
- Adam Personal Brand (@adamspeakslife)

The architecture follows Jake Van Clief's ICM (Interpretable Context Methodology).
Three layers: CLAUDE.md (the map) → CONTEXT.md per room (the rules) → references/ (the factory).

---

## WHAT YOU ARE FIXING

An ICM audit found 5 problems. Fix them in this exact order.
Do not skip steps. Do not combine steps.
Confirm each step is done before moving to the next.

---

## STEP 1 — Trim CLAUDE.md from 203 lines to under 50

The CLAUDE.md is a routing file only. It currently contains build rules and model rules
that belong in reference files, not the map.

### 1a. Create references/build-rules.md

Create this file at /references/build-rules.md with this content:

```
# Build Rules — Reference
# Loaded by: CLAUDE.md (global)
# Last updated: 2026-05-31

## 60-30-10 BUILD RULE
Before writing any code in any room, split the work into 3 layers:

| Layer    | %   | What goes here                                                      |
|----------|-----|---------------------------------------------------------------------|
| Scripts  | 60% | Predictable steps — fetch data, check availability, route events   |
| Database | 30% | Structured data — property list, decisions log, inquiry history    |
| AI       | 10% | Judgment only — draft replies, pricing calls, content, voice       |

Rule: If a task has a deterministic answer (same input = same output every time),
it is a script. Not a Claude prompt.

Before building any skill or CONTEXT.md, ask:
1. Which steps here are just math or data fetching? → Script
2. What data needs to be stored and queried? → Database
3. What requires real judgment or Adam's voice? → Claude

## ONE JOB RULE
Each room does ONE thing only.
/ich/pricing/ handles pricing. Nothing else.
If a CONTEXT.md is trying to do two things — split it.

## DON'T REINVENT RULE
Before building any new room or skill, check:
1. Does this already exist in adam-ai-os/?
2. Does this already exist on GitHub?
3. Can an existing room handle this with a small edit?
If yes to any — use what exists. Don't build new.

## PLAN FIRST RULE
Before writing any CONTEXT.md — write 3 sentences describing:
- What this room does
- What it takes in
- What it produces
If you can't do that clearly, the room isn't ready to be built yet.

## THE WIRING RULE
Any time a new tool, room, skill, or folder is added — update root
CLAUDE.md routing table in the same session. Never defer.

## THE COMPLETION CHECKLIST
When any build task finishes, ask:
1. Is this wired into CLAUDE.md routing?
2. Does the right CONTEXT.md reference it?
3. Is it committed to GitHub?
If any answer is NO — fix it before moving on.
```

### 1b. Create references/model-rules.md

Create this file at /references/model-rules.md with this content:

```
# Model Rules — Reference
# Loaded by: CLAUDE.md (global)
# Last updated: 2026-05-31

## MODEL ROUTING

Haiku — default for all tasks:
- Morning pricing check
- Maintenance routing
- Inquiry intake
- Calendar checks
- Telegram alerts

Sonnet — switch automatically when:
- Writing midterm decision analysis
- Drafting guest responses
- Content and video scripts
- Anything requiring judgment calls

## CONTEXT LIMIT RULE
If conversation exceeds 80% context window:
→ Summarize to /decisions/[business]-decisions.jsonl
→ Start fresh session with summary as context
This prevents running out of context mid-task.
```

### 1c. Rewrite CLAUDE.md — replace the entire file

Replace the full contents of CLAUDE.md with this:

```
# Adam James — AI Operating System
# Root Routing Table (Layer 1)
# Last updated: 2026-05-31

## IDENTITY
Name: Adam James — Tulsa, Oklahoma
GitHub: awjames6875 | Brand: @adamspeakslife
This is a multi-business AI OS. One map. Four businesses.

## CONTEXT LOADING RULES
Load ONLY this file first.
Identify the task. Load ONE room CONTEXT.md.
Never load multiple business contexts at once.

## ROUTING TABLE

| Task                         | Go to                                    | Read        |
|------------------------------|------------------------------------------|-------------|
| ICH pricing                  | /1_ich/pricing/                          | CONTEXT.md  |
| ICH inquiry response         | /1_ich/inquiries/                        | CONTEXT.md  |
| ICH midterm decision         | /1_ich/midterm-decisions/               | CONTEXT.md  |
| ICH lease or signing         | /1_ich/leasing/                          | CONTEXT.md  |
| ICH maintenance ticket       | /1_ich/maintenance/                      | CONTEXT.md  |
| ICH social content           | /1_ich/content/                          | CONTEXT.md  |
| ICH owner report             | /1_ich/owner-reports/                    | CONTEXT.md  |
| Safe Harbor partner outreach | /2_safe-harbor/partner-outreach/        | CONTEXT.md  |
| Safe Harbor parent comms     | /2_safe-harbor/parent-comms/            | CONTEXT.md  |
| Safe Harbor credentialing    | /2_safe-harbor/credentialing/           | CONTEXT.md  |
| Safe Harbor content          | /2_safe-harbor/content/                  | CONTEXT.md  |
| GrowthGenix (all tasks)      | /3_growthgenix/                          | CONTEXT.md  |
| Personal content + scripts   | /4_adam-personal/content/               | CONTEXT.md  |
| Personal reputation          | /4_adam-personal/reputation/            | CONTEXT.md  |
| Memoir                       | /4_adam-personal/memoir/                | CONTEXT.md  |
| Marketing + GoViralBro       | /5_marketing/                            | CONTEXT.md  |
| Build rules (any room)       | /references/build-rules.md              | read whole  |
| Model routing (any room)     | /references/model-rules.md              | read whole  |

## GLOBAL NON-NEGOTIABLES

### ICH
- MIDTERM ALWAYS FIRST. Short-term fills gaps only.
- Never auto-send anything without Telegram approval.
- Never confirm a booking without checking Guesty.
- Never quote a rate without checking Wheelhouse.

### Safe Harbor
- NEVER SAY: therapy, therapist, mental health treatment
- ALWAYS SAY: emotional wellness, support sessions, licensed counselor
- B2B content: never mention dollar amounts — say new revenue stream
- Always include logo and website on all designs

### Adam (ADHD rules)
- One task at a time. Numbered steps always.
- Copy-paste ready outputs always.
- Honest when something is harder than expected.
- Action over research always.

## CONTENT MOMENT RULE
When Adam builds, breaks, fixes, or ships something real:
Stop. Say CONTENT MOMENT. Run /4_adam-personal/content/skills/show-your-work.md

## DECISIONS LOG
All important decisions → /decisions/[business]-decisions.jsonl
Read last 50 lines at session start for context continuity.

## SHARED REFERENCES
/references/property-list.md — all 9 ICH properties
/references/build-rules.md — 60-30-10 rule, completion checklist
/references/model-rules.md — Haiku vs Sonnet routing, context limit rule
```

Verify: new CLAUDE.md is under 60 lines. Tell me when done.

---

## STEP 2 — Rename room folders with numbered prefixes

Rename these folders exactly as shown. Do not change anything inside them — only the folder name.

```
ich/            → 1_ich/
safe-harbor/    → 2_safe-harbor/
adam-personal/  → 3_adam-personal/
growthgenix/    → 4_growthgenix/
marketing/      → 5_marketing/
goviralbro/     → 5_marketing/goviralbro/
```

Note on goviralbro: move it INSIDE 5_marketing/ as a sub-folder.
It is a marketing sub-room, not a top-level business.

After renaming, verify the routing table in CLAUDE.md matches the new paths.
The routing table written in Step 1c already uses the new names.

---

## STEP 3 — Kill phantom routes / create placeholder files

These routes exist in the routing table but the files don't exist.
Create placeholder files for each one so routes don't lead to dead ends.

### 3a. Create missing reference files in /references/

Create each file with just this content (replace [filename] with actual name):

```
# [filename] — Reference
# STATUS: Not built yet
# BUILD: Add real content here when ready
# Last updated: 2026-05-31
```

Files to create:
- /references/wheelhouse-api.md
- /references/guesty-api.md
- /references/avail-process.md
- /references/openclaw-internals.md

### 3b. Create missing GrowthGenix sub-rooms

The routing table points to these — they don't exist yet.
Create each folder with a placeholder CONTEXT.md:

Folder: /4_growthgenix/client-intake/
File: /4_growthgenix/client-intake/CONTEXT.md

```
# GrowthGenix — Client Intake Room
# STATUS: Not built yet
# BUILD: Next sprint
# Last updated: 2026-05-31

Placeholder. Keep this file so the route stays live.
Write real rules here when client intake workflow is ready.
```

Folder: /4_growthgenix/proposals/
File: /4_growthgenix/proposals/CONTEXT.md

```
# GrowthGenix — Proposals Room
# STATUS: Not built yet
# BUILD: Next sprint
# Last updated: 2026-05-31

Placeholder. Keep this file so the route stays live.
Write real rules here when proposal workflow is ready.
```

Folder: /4_growthgenix/content/
File: /4_growthgenix/content/CONTEXT.md

```
# GrowthGenix — Content Room
# STATUS: Not built yet
# BUILD: Next sprint
# Last updated: 2026-05-31

Placeholder. Keep this file so the route stays live.
Write real rules here when content workflow is ready.
```

### 3c. Create goviralbro CONTEXT.md (now inside 5_marketing/)

File: /5_marketing/goviralbro/CONTEXT.md

```
# GoViralBro — Content Research Room
# STATUS: Not built yet
# BUILD: Week 7 (same as marketing)
# Last updated: 2026-05-31

Placeholder. Keep this file so the route stays live.
This room handles content research and viral hooks.
Write real rules here when GoViralBro workflow is ready.
```

### 3d. Create missing skills folders with placeholder files

Folder: /1_ich/inquiries/skills/
Create these 3 placeholder files:

/1_ich/inquiries/skills/respond-to-furnished-finder.md
```
# Skill: Respond to Furnished Finder Inquiry
# STATUS: Not built yet
# Last updated: 2026-05-31
Write skill instructions here.
```

/1_ich/inquiries/skills/respond-to-zillow.md
```
# Skill: Respond to Zillow Inquiry
# STATUS: Not built yet
# Last updated: 2026-05-31
Write skill instructions here.
```

/1_ich/inquiries/skills/send-property-availability.md
```
# Skill: Send Property Availability
# STATUS: Not built yet
# Last updated: 2026-05-31
Write skill instructions here.
```

Folder: /2_safe-harbor/partner-outreach/skills/
Create these 2 placeholder files:

/2_safe-harbor/partner-outreach/skills/respond-to-partner-inquiry.md
```
# Skill: Respond to Partner Inquiry
# STATUS: Not built yet
# Last updated: 2026-05-31
Write skill instructions here.
```

/2_safe-harbor/partner-outreach/skills/draft-partner-follow-up.md
```
# Skill: Draft Partner Follow-Up
# STATUS: Not built yet
# Last updated: 2026-05-31
Write skill instructions here.
```

---

## STEP 4 — Add output/ folders to all active rooms

Active rooms need an output/ folder — this is where finished work lands.
Create an empty .gitkeep file inside each output/ so Git tracks the folder.

Rooms to add output/ to:

```
/1_ich/pricing/output/.gitkeep
/1_ich/inquiries/output/.gitkeep
/1_ich/leasing/output/.gitkeep
/1_ich/maintenance/output/.gitkeep
/1_ich/midterm-decisions/output/.gitkeep
/1_ich/content/output/.gitkeep
/1_ich/owner-reports/output/.gitkeep
/2_safe-harbor/partner-outreach/output/.gitkeep
/2_safe-harbor/parent-comms/output/.gitkeep
/2_safe-harbor/credentialing/output/.gitkeep
/2_safe-harbor/content/output/.gitkeep
/3_adam-personal/memoir/output/.gitkeep
/3_adam-personal/reputation/output/.gitkeep
```

Do NOT add output/ to placeholder rooms (growthgenix sub-rooms, marketing, goviralbro).
They are not active yet.

---

## STEP 5 — Add "Last updated" to all active CONTEXT.md files

Open each active CONTEXT.md and add this as line 1:

```
Last updated: 2026-05-31
```

Files to update:

```
/1_ich/pricing/CONTEXT.md
/1_ich/inquiries/CONTEXT.md
/1_ich/leasing/CONTEXT.md
/1_ich/maintenance/CONTEXT.md
/1_ich/midterm-decisions/CONTEXT.md
/1_ich/content/CONTEXT.md
/1_ich/owner-reports/CONTEXT.md
/2_safe-harbor/partner-outreach/CONTEXT.md
/2_safe-harbor/parent-comms/CONTEXT.md
/2_safe-harbor/credentialing/CONTEXT.md
/2_safe-harbor/content/CONTEXT.md
/3_adam-personal/memoir/CONTEXT.md
/3_adam-personal/reputation/CONTEXT.md
```

---

## COMPLETION CHECKLIST

When all 5 steps are done, verify every item below before committing to GitHub:

- [ ] CLAUDE.md is under 60 lines
- [ ] CLAUDE.md routing table uses new numbered folder names (1_ich, 2_safe-harbor, etc.)
- [ ] references/build-rules.md exists
- [ ] references/model-rules.md exists
- [ ] All 4 missing reference placeholders exist in /references/
- [ ] goviralbro/ is now inside 5_marketing/ as a sub-folder
- [ ] All 3 GrowthGenix sub-room folders exist with placeholder CONTEXT.md
- [ ] goviralbro CONTEXT.md exists inside 5_marketing/goviralbro/
- [ ] All 5 skill placeholder files exist in the correct skills/ folders
- [ ] All 13 active rooms have an output/ folder with .gitkeep
- [ ] All 13 active CONTEXT.md files have "Last updated: 2026-05-31" as line 1
- [ ] Git commit with message: "fix: ICM architecture audit — step 1-5 complete"

---

## WHAT NOT TO TOUCH

Do not change:
- The content inside any active CONTEXT.md (pricing modes, inquiry rules, partner-outreach rules, etc.)
- The content inside references/property-list.md
- The .env.example file
- The decisions/ folder structure

The room content is correct. Only the structure needed fixing.

---

## AFTER THIS IS DONE

Return to the Jake Methodology Advisor project in Claude.ai
and say: "Ai-OS-ich fixes are done" for a follow-up audit.
