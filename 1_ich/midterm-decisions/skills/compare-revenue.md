# Skill: Compare Revenue — Midterm vs Short-Term
# Room: /1_ich/midterm-decisions/
# Trigger: A midterm inquiry arrives for dates with existing short-term bookings

## INPUTS NEEDED BEFORE RUNNING
- Property address
- Midterm offer: monthly rate + number of months
- List of existing short-term bookings on those dates: each booking amount
- Any partial overlaps (some STR dates may not conflict)

## THE CALCULATION — RUN IN ORDER

### Step 1: Midterm Total Revenue
Midterm monthly rate × number of months = **A**

Example: $2,400/mo × 3 months = $7,200

### Step 2: Existing Short-Term Revenue
Add up ALL short-term booking amounts that fall inside the midterm dates.
Include only confirmed bookings, not pending/inquiries.
Short-term total = **B**

Example: $850 + $1,100 + $600 = $2,550

### Step 3: Refund Cost
Adam gives full refunds on all cancelled bookings.
Sum of all refunds owed = **C**
(C = B if all bookings are non-refundable to guest; C = B if Adam eats them)

Example: $2,550 (full refund on all)

### Step 4: Net Gain of Taking Midterm
A − B − C = **NET GAIN**

Example: $7,200 − $2,550 − $2,550 = $2,100

### Step 5: Percentage More Than Current
(NET GAIN / B) × 100 = **% more than current bookings**

Example: ($2,100 / $2,550) × 100 = 82% more

### Step 6: Apply Threshold
| NET GAIN % vs B | Recommendation |
|-----------------|---------------|
| 50%+ | STRONGLY RECOMMEND ACCEPT |
| 20–49% | RECOMMEND ACCEPT |
| Under 20% | FLAG — ADAM'S CALL |
| Negative | DO NOT RECOMMEND |

## OUTPUT
Pass all values to send-decision-telegram.md to format and send.
Do not make a recommendation without completing all 6 steps.
