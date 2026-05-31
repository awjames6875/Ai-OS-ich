# ICH Pricing Room — CONTEXT.md
# Layer 2 — Rules for /ich/pricing/

## PURPOSE
Decides nightly pricing for all 9 ICH properties.
Midterm always wins. Short-term fills gaps only.

## THE 4 PRICING MODES

### 1. MIDTERM HOLD
Activates when: an active midterm inquiry is pending for specific dates.
Action: Raise short-term minimum 35-40% on those dates to discourage
short-term bookings that would block the midterm.

### 2. GAP FILL
Activates when: no midterm pending AND under 30% booked over next 30 days.
Action: Drop to competitive market rate.

### 3. EMERGENCY
Activates when: under 7 days out and still empty.
Action: Drop to floor price.

### 4. HEALTHY
Activates when: 70%+ booked OR midterm confirmed.
Action: No action needed.

## DECISION THRESHOLD
If a midterm pays 50%+ more than existing short-term bookings
(after refund costs) = RECOMMEND accepting the midterm.

## APPROVAL RULE
Always send a Telegram alert before ANY rate change.
Never push a change without Adam saying yes.

## WHAT THIS ROOM CHECKS
1. Guesty — current bookings + calendar
2. Wheelhouse — current dynamic rate
3. property-list.md — base price + floor per property

## HOW TO RUN
1. Identify the property and date range
2. Check Guesty for existing bookings
3. Check for any pending midterm inquiry
4. Pick which of the 4 modes applies
5. Calculate the recommended rate
6. Send Telegram alert with recommendation
7. Wait for Adam's yes before any change
