# Skill: Respond to Zillow Inquiry
# Room: /1_ich/inquiries/
# Trigger: New inquiry email received from Zillow

## BEFORE YOU WRITE ANYTHING
1. Check Guesty calendar for the requested dates
2. Check Wheelhouse for current nightly rate

## RESPONSE TEMPLATE

Subject: Re: [Property Address] — Available for Your Dates

---

Hi [First Name],

Thanks for reaching out! Great news — here's what we have available
for your dates ([Start Date] to [End Date]):

**[Property Address]**
[X] bed / [X] bath | Tulsa, OK
Rate: $[Wheelhouse rate]/night | Monthly rate available for 30+ day stays
Available: [Start Date] – [End Date]
✓ Fully furnished | ✓ All utilities included | ✓ Flexible lease terms

A few quick questions so I can get you the best fit:
- How many guests will be staying?
- What brings you to Tulsa?
- Are you open to a monthly rate? (We offer better pricing for 30+ days)

Happy to answer any questions.

Warm regards,
The ICH Team

---

## ZILLOW-SPECIFIC NOTES
- If they mention work/relocation → strong midterm candidate; flag for Adam
- Monthly rate estimate: Wheelhouse rate × 0.75 × 30 (rough midterm discount)

## RULES
- Never confirm availability without checking Guesty first
- Never quote a rate without checking Wheelhouse
- Sign as: The ICH Team

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
Wait for YES. Tag in GHL: ICH-Inquiry-Zillow
