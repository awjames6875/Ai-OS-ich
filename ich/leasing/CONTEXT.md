ICH Leasing Room — CONTEXT.md
Layer 2 — Rules for /ich/leasing/
Built from: Saddie's Avail SOP + Avail platform docs
Last updated: May 30, 2026
PURPOSE
Turn a qualified midterm lead into a signed lease
and confirmed reservation using Avail.
This room activates AFTER the inquiries room
has qualified the guest and Adam has said YES.
WHEN THIS ROOM ACTIVATES
Guest is qualified (name, employer, dates, guests collected)
Midterm decision has been made (see /ich/midterm-decisions/)
Adam has approved moving forward
Dates are NOT blocked in Guesty
WHAT YOU NEED BEFORE STARTING
Pull these from property-list.md:
Property address
Monthly rent rate
Security deposit amount
Pet fee (if applicable): $350 long-term
Cleaning fee
Utility policy for that property
THE 10-STEP LEASING PROCESS
Step 1 — Log into Avail
Go to avail.co and log in with ICH credentials
from the .env file.
Step 2 — Navigate to Properties
Click Properties or Listings tab.
Find the correct property.
Step 3 — Confirm Guest Information
Have ready before proceeding:
Full legal name
Phone number
Email address
Lease start and end dates
Number of occupants
Pets (yes/no)
Step 4 — Send Rental Application
Go to Applications section in Avail.
Two options:
Copy and paste the application link → send via text or email
Request Application → enter name, email, phone → Avail sends it
Tell the guest to complete it fully before proceeding.
Step 5 — Review Completed Application
Check application status = "Complete"
Review submitted documents for completeness.
Flag anything missing before moving to lease setup.
Step 6 — Set Up Lease
Click "Set Up Lease" and enter:
Monthly rent amount (from property-list.md)
Lease term (use exact start and end dates)
Security deposit
Pet fee if applicable
Any additional fees
USE AVAIL'S STATE-SPECIFIC TEMPLATE:
Select Oklahoma template.
Avail Local Assist automatically adds all required
Oklahoma state clauses, disclosures, and attachments.
Do NOT skip this — it protects Adam legally.
Customize as needed:
Pet policy
Smoking policy
Any property-specific rules
⚠️ DOUBLE CHECK EVERYTHING BEFORE FINALIZING.
Changes cannot be made after the lease is finalized.
Step 7 — Send for Signing
Click "Send for Signing."
Tenant signs digitally with name and email.
Once ALL tenants have signed →
Adam countersigns using Avail e-signature in account.
Finalized lease saves automatically in Avail account.
Step 8 — Set Up Payments
Choose Avail for payment processing.
Set up:
Security deposit + pet fee → due at reservation
Monthly rent → set correct due dates
Enable automated payment reminders
Step 9 — Telegram Alert to Adam
Send Adam this exact format:
LEASE READY — [Property Address]
Tenant: [Full Name]
Dates: [Start] to [End]
Monthly rent: $[amount]
Deposit collected: $[amount]
Lease signed: YES / PENDING
Confirm reservation? Reply YES or NO
Step 10 — Confirm Reservation
After Adam says YES:
Block dates in Guesty
Send confirmation to tenant with check-in details
Log in /decisions/ich-decisions.jsonl
LEASE AMENDMENTS
If an existing lease needs changes:
Go to Lease Documents section in Avail account.
Use Avail's lawyer-written lease amendment tool.
Do NOT edit the original lease directly.
STORING EXTERNAL LEASES
If a lease was signed outside Avail:
Upload to the Leases section of the unit in Avail.
Keeps all records in one place.
APPROVAL RULE
Never send a lease without Adam saying YES via Telegram.
Never confirm a reservation without a signed lease.
Never set up payments before lease is fully signed.
REFERENCE FILES
Always read:
/references/property-list.md → rates, deposits, owner info
/ich/inquiries/CONTEXT.md → guest info already collected
/ich/midterm-decisions/CONTEXT.md → decision already made
WHAT THIS ROOM DOES NOT DO
Does not handle pricing → /ich/pricing/
Does not handle maintenance → /ich/maintenance/
Does not handle guest inquiries → /ich/inquiries/
Does not make midterm vs short-term decisions → /ich/midterm-decisions/