# Skill: Respond to Furnished Finder Inquiry
# Room: /1_ich/inquiries/
# Trigger: New inquiry email received from Furnished Finder

## BEFORE YOU WRITE ANYTHING
1. Check Guesty calendar for the requested dates on ALL matching properties
2. Check Wheelhouse for current nightly rate on available properties
3. Pull guest info from the inquiry: name, dates, # of guests
4. Note if they mentioned employment — if so, flag as strong midterm candidate

## RESPONSE TEMPLATE

Subject: Re: [Property Address] — Available for Your Dates

---

Hi [First Name],

Thanks for reaching out through Furnished Finder! I'd love to help you find the right fit.

Based on your dates ([Start Date] to [End Date]), here's what we have available:

**[Property Address]**
[X] bed / [X] bath | Tulsa, OK
Rate: $[Wheelhouse rate]/night
Available: [Start Date] – [End Date]
✓ Fully furnished | ✓ Utilities included | ✓ Monthly rate available

[Add second property if applicable]

A few quick questions so I can get you the best fit:
- What brings you to Tulsa?
- How many guests will be staying?
- Are you open to a monthly rate? (We offer better pricing for 30+ days)

I'll check your availability in our system and get back to you right away.

Warm regards,
The ICH Team

---

## RULES FOR THIS TEMPLATE
- Never confirm availability without checking Guesty first
- Never quote a rate without checking Wheelhouse
- Always ask employer/purpose — this qualifies for midterm
- Lead with properties that are available; don't mention unavailable ones
- If stays 30+ days: note monthly rate option even if they didn't ask
- Sign as: The ICH Team (never Adam's name)

## MIDTERM CONFLICT CHECK
Run this if the guest requests 30+ days AND Guesty shows STR bookings on those dates.
DO NOT just say "not available." Do the math first.

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

4. Do NOT tell the guest the dates are unavailable until Adam decides.
   Hold them with: "Let me check on those dates and get back to you shortly."

## AFTER DRAFTING
Send draft to Adam via Telegram before sending.
Wait for YES. If NO — ask what to change.
Tag lead in GHL: ICH-Inquiry-FF
