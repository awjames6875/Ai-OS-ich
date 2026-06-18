# Skill: Send Property Availability
# Room: /1_ich/inquiries/
# Trigger: Guest has asked "what do you have available?" or needs a property list

## WHEN TO USE THIS
Use when a guest is asking broadly what's available,
or when following up and wanting to share current openings.
Not for the first response to a sourced inquiry (use the source-specific skill instead).

## STEP 1 — CHECK GUESTY
For each active property, check if the requested date range is open:
- 1307 Indianapolis Ave (2BR) — check Guesty
- 3701 S Richmond Ave (3BR) — check Guesty
- 4518 S Quaker Ave (3BR) — check Guesty
- 1432 E 38th St (2BR) — check Guesty
- 4016 E 51st St (3BR) — check Guesty
- 6308 E 1st Pl, Broken Arrow (3BR) — check Guesty
- 1348 S Pittsburg Ave (2BR) — check Guesty
- 1506 S Florence Pl (4BR) — check Guesty

2631 E 10th St → long-term only, do NOT include in availability lists.

## STEP 2 — CHECK WHEELHOUSE FOR CURRENT RATES
Pull current nightly rate for each available property from Wheelhouse before quoting.

## STEP 3 — BUILD THE AVAILABILITY MESSAGE

---

Hi [First Name],

Here's what we have open for [dates]:

| Property | Beds | Rate/night | Available |
|----------|------|------------|-----------|
| [Address] | [X]BR | $[rate] | [dates] |
| [Address] | [X]BR | $[rate] | [dates] |

All properties are fully furnished with utilities and WiFi included.
Monthly rates available for 30+ day stays.

Let me know which one catches your eye and I can hold it while we
get the paperwork together.

Warm regards,
The ICH Team

---

## MIDTERM CONFLICT CHECK
Run this if the guest requests 30+ days AND Guesty shows STR bookings on those dates
for a property they're interested in.
DO NOT mark the property as unavailable yet. Do the math first.

1. Pull all existing STR bookings that overlap the requested dates
2. Run the compare-revenue.md math from /1_ich/midterm-decisions/skills/
   - A = midterm rate × months
   - B = sum of conflicting STR bookings
   - C = refund cost (Adam always gives full refunds)
   - NET GAIN = A − B − C
3. Include the result in the Telegram draft to Adam:

MIDTERM CONFLICT — [Property Address]
Guest wants: [X] months at ~$[estimated monthly rate]
Conflicts with: [list each STR booking + amount]
STR total: $[B] | Refund cost: $[C] | NET GAIN: $[A−B−C] ([X]% more)
RECOMMENDATION: [ACCEPT / CONSIDER / ADAM'S CALL]
Cancel short-terms and take the midterm? Reply YES or NO

4. Hold the guest with: "Let me confirm those dates and get right back to you."
   Do NOT say unavailable until Adam decides.

## RULES
- Only list properties confirmed open in Guesty — or flag conflicts using the check above
- Pull rates from Wheelhouse — never guess or use stale numbers
- For 30+ day inquiries: mention monthly rate option
- Sign as: The ICH Team

## AFTER DRAFTING
Send draft to Adam via Telegram before sending. Wait for YES.
