# ICH Midterm Decisions Room
# Layer 2 Context — Load ONLY for midterm decisions

## PURPOSE
When a midterm inquiry comes in for dates
that have existing short-term bookings,
this room does the math and recommends
whether to accept the midterm or keep
the short-term bookings.

## THE CORE DECISION
Midterm inquiry arrives for Property X
for dates that have short-term bookings.
Should Adam cancel the short-terms and
accept the midterm?

## THE MATH
Step 1: Calculate midterm total revenue
  Midterm rate × number of months = A

Step 2: Calculate existing short-term revenue
  Sum of all short-term booking revenue
  for those dates = B

Step 3: Calculate refund cost
  Sum of all refunds Adam would owe
  for cancelled bookings = C

Step 4: Net gain of taking midterm
  A - B - C = NET GAIN

Step 5: Apply the threshold
  If NET GAIN is 50%+ more than B
  = STRONGLY recommend accepting midterm
  If NET GAIN is 20-49% more than B
  = RECOMMEND accepting midterm
  If NET GAIN is under 20% more than B
  = Flag for Adam's judgment

## REFUND POLICY
Adam always gives full refunds when
he cancels existing bookings.
Always include full refund cost in math.

## TELEGRAM FORMAT
Send Adam exactly this:

MIDTERM DECISION — [Property Address]

Midterm inquiry: [X] months at $[Y]/mo
Midterm total: $[A]

Existing short-term bookings:
[List each booking with amount]
Short-term total: $[B]
Refund cost: $[C]

NET GAIN of taking midterm: $[A-B-C]
That is [X]% more than current bookings.

RECOMMENDATION: [ACCEPT / CONSIDER / ADAM'S CALL]

Accept midterm? Reply YES or NO

## SKILLS IN THIS ROOM
/ich/midterm-decisions/skills/compare-revenue.md
/ich/midterm-decisions/skills/send-decision-telegram.md
