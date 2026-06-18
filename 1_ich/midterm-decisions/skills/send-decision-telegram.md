# Skill: Send Decision Telegram
# Room: /1_ich/midterm-decisions/
# Trigger: Revenue comparison is complete; send recommendation to Adam

## PREREQUISITE
Run compare-revenue.md first. This skill only formats and sends.
Never send without completed math from that skill.

## TELEGRAM MESSAGE FORMAT
Copy this exactly. Fill in the brackets.

---

MIDTERM DECISION — [Property Address]

Midterm inquiry: [X] months at $[monthly rate]/mo
Midterm total: $[A]

Existing short-term bookings:
[List each booking: dates + amount]
Short-term total: $[B]
Refund cost: $[C]

NET GAIN of taking midterm: $[A − B − C]
That is [X]% more than current bookings.

RECOMMENDATION: [ACCEPT / CONSIDER / ADAM'S CALL]

Accept midterm? Reply YES or NO

---

## RECOMMENDATION LABELS
| Threshold | Label to use |
|-----------|-------------|
| NET GAIN 50%+ vs B | ACCEPT |
| NET GAIN 20–49% vs B | CONSIDER |
| NET GAIN under 20% vs B | ADAM'S CALL |
| Negative NET GAIN | include note: "Math does not favor midterm" |

## WHAT TO DO AFTER SENDING
- Wait for Adam's reply
- YES → pass to /1_ich/leasing/ to begin lease process
- NO → no action; log the decision in /decisions/ich-decisions.jsonl
- No reply in 4 hours → send one follow-up nudge, then wait
