# Rosta — product reference for blog articles

Rosta is the HR and payroll platform built by Blazonshots LTD. It runs at
https://blazonshotsltd.com (sign-up: https://blazonshotsltd.com/signup,
pricing: https://blazonshotsltd.com/pricing). On blazonshots.com its product
page is `site/rosta.html`.

**Rule for every Rosta article:** describe only what is in this file. Screen
and section names below are taken from the live app's own labels; use them
exactly. If an article needs a detail that is not here (a specific button
position, a mobile screen, an integration not listed), describe the step in
general terms or leave it out. Never invent features, prices, customer
names, testimonials or results. Prices change: when quoting them, say
"at the time of writing" and link to the pricing page. Last refreshed from the
app source and pricing page: 15 Nov 2026.

## Who it is for
- Business owners and HR teams in Nigeria running payroll, whether they use
  spreadsheets today or are switching from another payroll system.
- Payroll bureaus and HR firms that run payroll for several client companies
  under their own brand.
- Businesses across Africa: Rosta runs payroll in **48 African countries**,
  each in its own currency with its own income tax and statutory
  contributions. One account can hold several companies (e.g. one per country).
- **How the rules work (say this accurately):** Nigeria has a dedicated engine
  whose 2026 PAYE rules were signed off by a chartered accountant. Every other
  country uses Rosta's researched starting rules, published as **not reviewed
  by a local accountant** — the payroll screens say so — and each company can
  adjust bands, credits, allowances and every contribution under
  Payroll → Settings → Tax and contribution rules; every change is in the
  audit log. Always tell non-Nigerian readers to have a local accountant
  confirm settings before the first live pay run. Never call non-Nigerian
  rules "signed off", "certified" or "guaranteed compliant".
- Remittance deadlines outside Nigeria are set from each country's rules
  (income tax and contributions by the due day in the month after salaries
  are paid; changeable if the authority differs).

### Countries, contributions, payouts and rule confidence
(From Rosta's docs/countries.md. "Confidence": high = checked against 2026
sources; medium = known rules, small items may have moved; low = a template
to check with a local accountant. Do not quote Rosta's band amounts for any
country — verify current rates from that country's official tax authority.)

| Country | Currency | Tax | Method | Contributions | Payouts | Confidence |
|---|---|---|---|---|---|---|
| Nigeria | NGN | PAYE | Cumulative | Pension 8%/10%, NHF 2.5%, NSITF 1%, ITF 1% | Paystack, Flutterwave | Signed off |
| Ghana | GHS | PAYE | Monthly | SSNIT_EE, SSNIT_ER | Paystack, Flutterwave | high |
| Kenya | KES | PAYE | Monthly | NSSF_EE, NSSF_ER, SHIF, AHL_EE, AHL_ER, NITA | Paystack, Flutterwave | high |
| South Africa | ZAR | PAYE | Annualised | UIF_EE, UIF_ER, SDL | Paystack | high |
| Egypt | EGP | Salary tax | Annualised | SI_EE, SI_ER, MARTYRS | Bank file | medium |
| Morocco | MAD | IR | Annualised | CNSS_EE, AMO_EE, CNSS_ER, AF_ER, AMO_ER, TFP | Bank file | medium |
| Algeria | DZD | IRG | Annualised | CNAS_EE, CNAS_ER | Bank file | low |
| Tunisia | TND | IRPP | Annualised | CNSS_EE, CNSS_ER, TFP, FOPROLOS | Bank file | low |
| Côte d'Ivoire | XOF | ITS | Monthly | CNPS_EE, CNPS_ER, PF_ER, AT_ER, CMU_EE, CMU_ER, ITS_ER, FDFP | Bank file | low |
| Senegal | XOF | IR | Annualised | IPRES_EE, IPRES_ER, CSS_PF, CSS_AT, CFCE | Bank file | low |
| Cameroon | XAF | IRPP | Annualised | CNPS_EE, CNPS_ER, PF_ER, AT_ER, CFC_EE, CFC_ER, FNE, RAV, TDL | Bank file | low |
| Uganda | UGX | PAYE | Monthly | NSSF_EE, NSSF_ER | Flutterwave | high |
| Tanzania | TZS | PAYE | Monthly | NSSF_EE, NSSF_ER, SDL, WCF | Flutterwave | high |
| Rwanda | RWF | PAYE | Monthly | RSSB_EE, RSSB_ER, MAT_EE, MAT_ER, OH_ER, CBHI | Flutterwave | medium |
| Ethiopia | ETB | Employment income tax | Monthly | PEN_EE, PEN_ER | Bank file | medium |
| Zambia | ZMW | PAYE | Monthly | NAPSA_EE, NAPSA_ER, NHIMA_EE, NHIMA_ER, SDL | Bank file | medium |
| Zimbabwe | USD | PAYE | Monthly | NSSA_EE, NSSA_ER, ZIMDEF | Bank file | low |
| Malawi | MWK | PAYE | Monthly | PEN_EE, PEN_ER | Bank file | low |
| Mozambique | MZN | IRPS | Annualised | INSS_EE, INSS_ER | Bank file | low |
| Angola | AOA | IRT | Monthly | INSS_EE, INSS_ER | Bank file | low |
| Botswana | BWP | PAYE | Annualised | None | Bank file | medium |
| Namibia | NAD | PAYE | Annualised | SSC_EE, SSC_ER, VET | Bank file | medium |
| Lesotho | LSL | PAYE | Monthly | None | Bank file | low |
| Eswatini | SZL | PAYE | Annualised | ENPF_EE, ENPF_ER | Bank file | low |
| Mauritius | MUR | PAYE | Annualised | CSG_EE, CSG_ER, NSF_EE, NSF_ER, HRDC | Bank file | low |
| Seychelles | SCR | Income tax | Monthly | SPF_EE, SPF_ER | Bank file | low |
| Madagascar | MGA | IRSA | Monthly | CNAPS_EE, CNAPS_ER, OSTIE_EE, OSTIE_ER | Bank file | low |
| Benin | XOF | ITS | Monthly | CNSS_EE, CNSS_ER, AT_ER, VPS | Bank file | low |
| Burkina Faso | XOF | IUTS | Monthly | CNSS_EE, CNSS_ER, TPA | Bank file | low |
| Mali | XOF | ITS | Annualised | INPS_EE, AMO_EE, INPS_ER, AMO_ER, CF, TFP | Bank file | low |
| Niger | XOF | IUTS | Annualised | CNSS_EE, CNSS_ER, TA | Bank file | low |
| Togo | XOF | IRPP | Annualised | CNSS_EE, CNSS_ER | Bank file | low |
| Guinea | GNF | RTS | Monthly | CNSS_EE, CNSS_ER, VF, TA | Bank file | low |
| Guinea-Bissau | XOF | IPR | Monthly | INSS_EE, INSS_ER | Bank file | low |
| Sierra Leone | SLE | PAYE | Monthly | NASSIT_EE, NASSIT_ER | Bank file | low |
| Liberia | LRD | Income tax | Annualised | NASSCORP_EE, NASSCORP_ER | Bank file | low |
| Gambia | GMD | PAYE | Annualised | SSHFC_EE, SSHFC_ER | Bank file | low |
| Cabo Verde | CVE | IRPS | Annualised | INPS_EE, INPS_ER | Bank file | low |
| Mauritania | MRU | ITS | Monthly | CNSS_EE, CNSS_ER, CNAM_EE, CNAM_ER | Bank file | low |
| Gabon | XAF | IRPP | Annualised | CNSS_EE, CNSS_ER, CNAMGS_EE, CNAMGS_ER | Bank file | low |
| Congo | XAF | IRPP | Annualised | CNSS_EE, CNSS_ER, PF_ER, AT_ER, TUS | Bank file | low |
| DR Congo | CDF | IPR | Monthly | CNSS_EE, CNSS_ER, INPP, ONEM | Bank file | low |
| Chad | XAF | IRPP | Annualised | CNPS_EE, CNPS_ER | Bank file | low |
| Equatorial Guinea | XAF | IRPF | Annualised | INSESO_EE, INSESO_ER | Bank file | low |
| São Tomé and Príncipe | STN | IRS | Monthly | INSS_EE, INSS_ER | Bank file | low |
| Burundi | BIF | IPR | Monthly | INSS_EE, INSS_ER, AT_ER | Bank file | low |
| Comoros | KMF | IGR | Annualised | None | Bank file | low |
| Djibouti | DJF | ITS | Monthly | CNSS_EE, CNSS_ER | Bank file | low |

## Plans (Nigeria, naira, before 7.5% VAT, at time of writing)
- The pricing page has a selector for 48 African countries; quote only the
  Nigerian naira prices below and send other readers to the pricing page.
- 30-day free trial on every plan, no card needed. Billed per active
  employee per month (anyone in an approved pay run that month, or who signed
  in that month). Invoices on the 1st for the previous month.
- **Essentials** ₦1,700/employee/month (min ₦17,000): People, Payroll,
  Remittances, Leave, Attendance, Reports, plus the staff app.
- **Professional** ₦2,300 (min ₦23,000): adds Loans and benefits, Expenses and
  requests, Recruitment, Performance, Documents, own domain.
- **Enterprise** ₦2,900 (min ₦29,000): adds Assets, API access, webhooks,
  report builder.
- **Own platform** (flat monthly, own name/logo/domain, no "Powered by Rosta",
  all modules): up to 50 staff ₦200,000; up to 200 ₦650,000; up to 1,000
  ₦2,700,000; yearly billing gives 12 months for the price of 10.
- **Reseller** ₦1,600/employee (min ₦100,000) and **Reseller Plus** ₦2,000
  (min ₦150,000) for bureaus and HR firms, across all clients, fully branded.
- Add-on: a branded mobile app for own-platform and reseller plans.
- Nigeria's 2026 PAYE calculation was signed off by a chartered accountant.

## Getting started
- Create an account at /signup. The dashboard shows "Finish setting up" with
  four setup steps to get the workspace ready.
- Settings → Companies: each company gets its own staff, payroll and roles.
- Settings → Users: "Invite a user" — they get an email link to set a password.
- Settings → Branding: logo and colours shown on the sign-in page, app, emails
  and documents. Settings → Domains: staff sign in at your own address; the
  secure certificate is set up automatically (plans with own domain).
- Settings → Security: sign-in and payment protections, "Download all your
  data", and "Rosta support access" (Rosta staff can only see company data
  after starting a logged support session with a reason).
- Two-factor sign-in is available under Security for each user.
- Settings → Audit: an audit log of changes.

## People (employee records)
- People → Add employee (personal details, employment) or People → Import
  employees (import wizard from a spreadsheet); People → Export.
- People → Structure: departments, branches and grades.
- Employee record: personal details, next of kin and emergency contact,
  status, pay, documents.
- People → Change requests: staff ask to update their own details; approving
  applies the change; bank detail changes notify the employee.
- People → Onboarding: checklists for new starters and leavers, with tasks
  shared between HR, IT, finance, the line manager and the employee; a
  "Probation ending" list (people whose probation ends within 45 days or has
  ended).
- People → Exits: record a leaver (resignation, termination, other); their
  last day goes on their record so the final regular pay run pays salary up to
  the last working day; notice and exit interview.
- People → Cases: confidential HR cases; HR can issue a query that the
  employee can reply to in writing online.

## Payroll
- Payroll → Salary structures: how gross pay splits into basic, housing,
  transport and other allowances; the split decides NHF and pension.
- Payroll → Pay elements: the building blocks of a payslip; standard elements
  keep their pension/NHF treatment; add your own (meal allowance, uniform
  deduction, company car as benefit in kind).
- Payroll → Settings: pay day of the month (last day used in short months);
  PAYE method (cumulative or annualised); pro-rate part months by calendar
  days or working days; flag pay changes above a % (runs ask for a reason
  when net pay moves more than this); employer pension rate (at least 10%
  under the Pension Reform Act); "Who sees pay" (hide salaries from HR);
  approving pay runs (a second person must approve — whoever prepared or
  submitted cannot approve; self-approval can be allowed and is marked).
- Payroll → Opening balances: when switching mid-year, paste one line per
  person — employee number, taxable pay to date, PAYE to date, pension to
  date, NHF to date — from the previous payroll.
- Payroll → Tax reliefs: employees declare rent and other reliefs with proof;
  approved reliefs reduce PAYE from the next pay run; rent relief needs proof
  of payment.
- Payroll → Calculator: net pay from gross, or the gross needed for a target
  net, using the company's structures and settings — useful for job offers.
- **Pay runs** (Payroll → Pay runs). Each month: create the run, add one-off
  payments, calculate, submit for approval, then pay and send payslips.
  Stages shown: Draft → Calculated → Submitted → Approved → Paid → Closed.
  One-off payments can be added in bulk by pasting employee number, element
  code, amount and an optional note. "Add people" ticks who is paid in the run.
- Payroll → Payouts: pay staff straight from the company's own Paystack or
  Flutterwave balance, with checks that each salary account belongs to the
  right person (name check).
- Payslips: staff see every payslip under My payslips and can download them;
  payslips can be emailed.

## Remittances
- Remittances lists everything approved pay runs owe to tax, pension and other
  agencies, with due dates and the receipt for every payment; record a payment
  (bank transfer, Remita, agency portal, cheque, other); change a due date if
  the agency gave a different one.
- Deadlines Rosta uses (Nigeria): PAYE to the State Internal Revenue Service by
  the 10th of the month after salaries are paid; pension to the Pension Fund
  Administrator within 7 working days of paying salaries; NHF to the Federal
  Mortgage Bank of Nigeria within one month; NSITF by the 15th of the month
  after; ITF 1% of the year's payroll by 1 April of the following year.
- Reminders: notification and email before each due date, the day after it is
  missed, and a week later.
- For bureaus: Clients → calendar shows overdue remittances first, then pay
  days and remittance deadlines across all clients for the next 60 days.

## Leave
- Leave → Types, Balances (days left after approved and waiting leave; adjust
  a balance for time off in lieu, days bought back or corrections, recorded
  with your name), Calendar, Holidays (public holidays and company days off,
  skipped when leave is counted in working days), Settings (who approves
  leave, how leave affects pay). "Leave for someone" requests on someone's
  behalf or records leave already agreed.

## Attendance
- Attendance → Clock-ins (every clock-in/out with its source; staff can't edit
  their own; HR adds missed ones with a reason, logged; import from a device),
  Register (each person's month from clock-ins, schedules, leave and holidays),
  Schedules (working hours decide who is expected, who is late, what counts
  as overtime), Timesheets, Settings (how clocking in works, including from
  the mobile app, and overtime treatment).

## Approvals and self-service
- Approvals: one inbox for leave, attendance, loans, expense claims and other
  requests; you never see your own requests there.
- Staff self-service ("Me"): My details, My payslips, My leave, My attendance,
  My loans, My benefits, My expenses, My requests, My documents (tasks and
  policies to read and confirm), My performance (reviews, goals, improvement
  plan). Announcements and notifications.

## Loans and benefits (Professional and up)
- Salary advances (no interest, at most one month's pay, repaid over at least
  three months under the Labour Act) and staff loans; repayments are taken in
  pay runs automatically; if one-third of wages is already taken by other
  voluntary deductions, less is taken that month and the rest carries on.
  Loan rules set limits for self-service requests.
- Benefits: health insurance, group life and other plans — who is covered,
  cost, renewal dates.

## Expenses and requests (Professional and up)
- Expense claims with categories, limits, approval and payback rules;
  receipts required unless below an amount you set.
- Request forms: design forms for anything staff ask for (letters, equipment,
  ID cards, training); each request goes through Approvals.

## Recruitment (Professional and up)
- Jobs, applications, candidates and talent pool, interviews, offers, a
  careers page, approvals and privacy settings. Add candidates from referrals,
  agencies or CVs received elsewhere. An AI CV-screening add-on is planned
  ("coming soon") — say so only as coming soon, never as available.

## Performance (Professional and up)
- Review cycles (launching creates reviews and tells reviewers), company and
  department goals that staff link their goals to, competency library,
  one-to-ones with shared notes, improvement plans.

## Documents (Professional and up)
- Company policies staff read and acknowledge (you see who hasn't); letter
  templates with fields; issued letters numbered on your letterhead and
  unchangeable once issued; expiring documents list with reminders 30 days
  and 7 days before and on the day.

## Assets (Enterprise and own-platform)
- Add an asset, give it to someone, history and details.

## Reports and developers
- Reports (e.g. people by department); report builder on Enterprise and up.
- Settings → Developers: API keys for accounting/ERP/HR portals and signed
  webhooks (Enterprise, own platform, Reseller Plus).

## Bureaus and HR firms (reseller plans)
- Clients → New client company: its own employees, pay runs, policies and
  statutory registrations; run everything for them or invite their admin.
  Clients → staff and calendar across clients.

## Mobile
- Staff self-service (payslips, leave, attendance, requests) is included on
  all plans and works in the browser. Rosta's own mobile apps are not yet in
  the app stores at the time of writing — do not tell readers to download
  them from a store; say mobile apps are coming. Branded apps for white-label
  customers are published under the customer's own store account.
