# Stress test: the skeptical buyer (BUY2)

**What was tested.** This is the Step 2.4 architecture, read from the buyer's side of the table.
- Read in full: BUSINESS.md, MAP.md, FRAMEWORKS.md, HOUSE_STANDARD.md, and all four brief files.
- Checked for specific claims: THESES.md and LEDGER.md.
- Checked so that settled items aren't re-raised: DECISIONS.md and the first buyer pass (`critique/buyer.md`).
- Taken as given: SPEC.md.

**Citation style.** Each citation names the file, then the module and brief section, e.g. `part-1-2.md · 06 §4`.

**The buyers.**
- **(A)** is 24, an employed Struggler. He has done months of DIY with nothing measured, and he has been burned by a faked before/after and a device, so he is also in the Burned state. His take-home is about $2.8k a month (LEDGER G, men 20–24).
- **(B)** is 29, an Optimizer with a higher income; the 25–34 median take-home is about $3.9k a month. He wants speed, precision and privacy.
- **(C)** is 19 and on a tight budget. He is a legal adult in most states, and LEDGER G has no row under 20.
- **(D)** is a buyer with appearance anxiety. This is roughly 5–20% of appearance-change seekers (LEDGER G).

**Severity.**
- **Critical:** as designed, a buyer is harmed, a hard line is crossed in practice, or the deciding trust moment fails. Fix before drafting.
- **Major:** a buyer would likely say no, feel handled, or be under-served at a deciding moment. Fix in the brief before the module is drafted.
- **Minor:** naming or polish. Fix while drafting.

**A pattern to know before the list.** Six findings are *regressions*. Each is a protection the foundation already accepted, in THESES v2 or DECISIONS R1, that never reached the files drafters will follow. THESES is removed at ship and is never cited, so anything that lives only there won't get written. These findings are tagged *[regression]*.

## Summary

| ID | Severity | Buyers hit | Modules | The finding in one line |
|---|---|---|---|---|
| BUY2-1 | critical | D, C, A | 06, 09, 20, 26; House Standard | The stop rules bind the operator but not the email machine |
| BUY2-2 | critical | D, A | 05, 06, 08, 13, 17 | The seller resolves a fit-check signal with no cooling-off, and "Starter Path" can mean a self-run capture kit |
| BUY2-3 | major | C, A | 02, 06, 08, 19, 20 | The affordability question never reaches checkout or the paid assessment |
| BUY2-4 | major | A, C | 02, 08, 13; BUSINESS §6–7 | The cash ceiling is never set, and pricing above the band shuts out the default buyer |
| BUY2-5 | major | A, C | 06, 08, 14, 15, 16, 20 | The paid assessment risks being a pitch he pays for |
| BUY2-6 | major | C, A | 06, 09, 19 | The credit window turns his own fee into the deadline |
| BUY2-7 | major | B | 05, 06, 07, 11 | Scaling offers three overlapping paid reviews, and there's no Optimizer lane before month 9 |
| BUY2-8 | critical | A (all) | 07, 11, 18–22, 27 | The Program is designed to end before outcomes, and he learns the full path at week 10 |
| BUY2-9 | critical | A | House Standard; FRAMEWORKS; 06, 07, 19, 20, 27 | The Burned Struggler gets the closer's playbook |
| BUY2-10 | major | D | 02, 15, 18, 19, 20; House Standard | No module owns the appearance-anxious buyer |
| BUY2-11 | major | D, C | 15, 17; House Standard #7 | Identity turns the fit check and the price into status |
| BUY2-12 | major | all | 07, 12, 17, 19, 25, 27 | The objection map misses the objections that decide the sale, and no module owns privacy before purchase |
| BUY2-13 | major | A, D | 08, 10, 16, 21, 22; House Standard | Three consistency devices hem in the fit window |
| BUY2-14 | major | B, A | 07, 08, 12, 19; House Standard | Attention falls as the price rises, and the review automates without disclosure |
| BUY2-15 | critical | A | 07, 08, 21, 22 | At the plateau, every road leads back into the Program |
| BUY2-16 | minor | A | 08, 16, 21, 22 (FRAMEWORKS) | Three names fail the glass-box rule, and the ask rule permits asks at a flat read |
| BUY2-17 | major | A, B | 07, 08, 11, 12 | The Hold and Private are sold on deliverables the design week doesn't fund |
| BUY2-18 | major | C | 05, 08, 17, 19 | The Starter Path is the whole brand for the budget buyer, and it's one paragraph |

The findings follow the buyer's journey: the door and the offer (1–7), the promise and the call (8–12), delivery (13–14), the plateau (15–16), the back end (17), and the floor (18).

---

## Findings

### BUY2-1 · critical · The stop rules bind the operator but not the email machine

**Location.**
- HOUSE_STANDARD.md: the stop rules, and the house rule "Privacy is part of the product" (fit-check answers stay out of marketing tools).
- BUSINESS.md §4: the door diagram routes "unscored distress items → resources + opt-in human conversation".
- `part-1-2.md · 06 §2`: door tags (state, stage, route).
- `part-1-2.md · 09 §4, §6`: price steps are Decision Points; one announcement and one reminder go to engaged segments.
- `part-5.md · 20 §4`: the five-email sales sequence.
- FRAMEWORKS.md and `part-6-7.md · 26`: Readiness Tags; the Welcome Arc runs "from result to offer"; §6 keeps health-adjacent answers out of the marketing platform.
- LEDGER.md C: the Follow-Up Rule ends "then regular email only".

**Issue.** Every stop rule is written for a person in a conversation. The async machine never learns that one fired.
- **Distress.** The free door routes distress items to resources and an opt-in conversation, but he gives his email in the same flow. The privacy rule correctly keeps his answers out of the email tool, Readiness Tags carry only stage, state and route, and the Welcome Arc is defined as a sequence "from result to offer". No module says what the automation does with a distress answer. By default he gets the sales arc: the destination named vividly, a stake, and a real date.
- **"I can't afford it."** On the call, money talk stops. Afterwards the Follow-Up Rule returns him to "regular email". That includes one announcement and one reminder per start to engaged segments, and the ≥30-day price-step announcement that 09 lists as a Decision Point. The one person who said he can't afford it is the one who hears "the price rises on [date]".

**Why it matters to the buyer.** For (D), this is selling into distress on autopilot, which breaks hard line 5. It arrives days after he disclosed the distress, and it teaches him that disclosure gets harvested. For (C), a price-rise email after "I can't afford it" pushes toward the borrowing the affordability question exists to prevent. For (A), it's the moment the brand turns into the funnel he already knows.

**Fix (inside the spec).**
- **06** owns a route value that carries no content, e.g. *pause*. It's set by any endorsed distress item; by "can't afford" at a call, a checkout or the plan step; and by a fit-check pause. The tag never records why it was set, so the privacy rule holds.
- **26** owns what a pause does. For a stated period, e.g. 60–90 days, the lead gets no sales sequence and no start or price-step sends, only canon-lane and Starter Path content. After that period he gets a re-permission email, not an automatic resume.
- **20 and 09** each add one line: every automated sequence and every date send checks the route first.
- **House Standard:** add to the stop rules, "Stop rules bind automation too."
- **13:** add a guardrail counting promotional sends to paused leads, with a target of zero.

---

### BUY2-2 · critical · The seller resolves a fit-check signal with no cooling-off, and "Starter Path" can mean a self-run capture kit *[regression]*

**Location.**
- HOUSE_STANDARD.md, house rule "The fit check": three outcomes (enroll with adjusted expectations, the Starter Path, or a referral).
- `part-1-2.md · 06 §4`: "only acute signals end the sale".
- `part-1-2.md · 05 §5`.
- BUSINESS.md §4: the free 7-day log and the baseline capture sit before the Fit Check.
- BUSINESS.md §5: the Self-Serve System is "capture standard, logs, decision framework, walkthroughs".
- `part-3-4.md · 17 §4`.
- LEDGER.md C: "~5–20% show at least one signal; most continue after a conversation".
- LEDGER.md A4: "Fit-check talks, Starter Path, renewal reviews" get 0.25–0.5 h a week.
- THESES.md B12: "serial appearance purchasers get extra care (no plan, a cooling-off gap)". This is absent from `06 §4` and `08 §4`.

**Issue.** Three gaps stack.
1. **The seller decides.** The operator who earns from the enrollment runs the conversation that decides whether a signal is acute. That conversation is budgeted inside 15–30 minutes a week, shared with Starter Path touches and renewal reviews. Its common outcome ("most continue") is enrollment with adjusted expectations. Nothing prevents that outcome, and payment, in the same conversation.
2. **B12 was dropped.** THESES B12's extra care for serial appearance purchasers (no plan, a cooling-off gap) never reached 06 or 08. Yet the door asks what he has tried, and the Burned state is by definition someone who has bought before.
3. **The Starter Path is the wrong landing for a checking signal.** It is one of the three outcomes, but it was built for "can't afford / not now". Its free branch is logging, and its paid upgrade adds the capture standard. For a buyer flagged for compulsive checking, that is a tracking kit with no reviewer to hold the "appearance rarely" cadence the Program enforces. The free baseline capture is also offered to every adult before any fit check.

**Why it matters to the buyer.** (D) is the buyer most likely to show a signal. He is also the most likely to talk himself past it in a ten-minute conversation, and the most harmed by a self-run photo routine. (A), with a device in a drawer, is the serial purchaser THESES promised a cooling-off gap.

**Fix (inside the spec).**
- **06:** any signal means no same-day payment. The adjusted expectations go in writing into the Expectation Document. A stated cooling-off gap, e.g. ≥72 hours, runs before payment. No payment plan is offered, and the fit window starts on day one of delivery.
- **06 and 08:** carry B12 across, so a "what have you bought?" answer that shows repeated appearance purchases gets the same care.
- **Split the Starter Path outcome.** For checking or fixation signals it becomes a referral plus reading-only content. That means no capture tools, no tracking products, and sales paused under BUY2-1.
- **05:** the Self-Serve checkout embeds the Fit Check.
- **17:** the free baseline capture comes after the free-door distress items and is skipped when one is endorsed.
- **13:** track refund and exit rates among signal-flagged enrollees as their own guardrail.

---

### BUY2-3 · major · The affordability question never reaches checkout or the paid assessment

**Location.**
- MAP.md 02: owns the Eligibility Rule (age fork plus take-home affordability).
- FRAMEWORKS.md: the Eligibility Rule is listed as "Also in 6, 8, 19", not 20.
- `part-1-2.md · 06 §2`: the self-assessment has no affordability item.
- `part-1-2.md · 06 §5`: checkout embeds the age attestation and the Fit Check only.
- `part-1-2.md · 08 §4`: the question is asked at the plan step.
- MAP.md boundary 8↔19: the question is asked "in conversation".
- `part-5.md · 20 §5`: checkout design.
- LEDGER.md G: "asked of everyone before any plan".
- BUSINESS.md §4: warm routes go straight to checkout, and the assessment is async-first at Scaling.

**Issue.** Eligibility is two tests, and the async routes enforce only one of them.
- A warm buyer who pays in full at checkout, on a card or otherwise, is never asked whether the money comes from income.
- A buyer booking the $150–250 assessment is never asked either. So someone who can't afford the Program can buy an assessment whose only realistic recommendation is the Starter Path.

At Scaling, most enrollments are designed to happen without a call (20), so the gap grows with the business.

**Why it matters to the buyer.** (C) is exactly this buyer. $200 is real money to him, and the credit it buys is worthless if the Program is out of reach (see BUY2-4 and BUY2-6). For (A), a full-price purchase straight from a pitch segment is the impulse pattern he has regretted before.

**Fix (inside the spec).**
- **06:** ask the affordability question, with the Program's price range stated, before booking any paid human step and inside every checkout, whether full-pay or plan. A "no" routes to the Starter Path page and sets the pause route from BUY2-1.
- **20:** add it to the Eligibility Rule's "Also in" list and to 20 §5.
- **02:** state the placement once ("before any paid step, in every channel"), and word the question "from your own monthly income". BUY2-12 covers parent-funded adults.

---

### BUY2-4 · major · The cash ceiling is never set, and pricing above the band shuts out the default buyer

**Location.**
- BUSINESS.md §2: the default buyer is mid-20s (range 19–28) and "able to pay from monthly income".
- BUSINESS.md §6: the $50k configuration is "~11/month × ~$4k (above band)".
- BUSINESS.md §7: the cash ceiling is measured in months of take-home.
- MAP.md 08 (Three Ceilings) and 02 ("buyer economics").
- `part-1-2.md · 08 §2`: "Setting the first price" gives no numeric limit.
- LEDGER.md G: take-home is about $2.8k a month at 20–24 and about $3.9k at 25–34; months of take-home are computed only up to $3k.
- LEDGER.md B: at most three installments, all inside delivery.

**Issue.** The cash ceiling is a unit of measure, not a limit. LEDGER G stops at $3k, which is about 1.1 months of take-home at 20–24. Above the band, prices rise well past that:

| Price above the band | Months of take-home at 20–24 | Months of take-home at 25–34 | Each of three installments inside 12 weeks | Installment as a share of a 24-year-old's monthly take-home |
|---|---|---|---|---|
| $3.5–4.5k | ≈1.25–1.6 | ≈0.9–1.15 | ≈$1.17–1.5k | ≈42–54%, before any plan premium |

The $50k configuration needs about eleven of these sales a month. Nothing decides which of two things is true:
- The business has quietly re-targeted older, higher-income buyers, so the default protagonist and the examples should change.
- It still serves the mid-20s Struggler, so something must sit under his ceiling.

Asked honestly, most 20–24-year-olds will answer the affordability question "no". The architecture's default protagonist silently becomes ineligible for its own flagship.

**Why it matters to the buyer.** (A) watches the price climb from $1.5k to $4k as proof accrues, announced step by step in public. The better it gets, the less it's for him. (C) is priced out from the opening band. The brand's promise to stalled adults becomes a premium product without anyone having decided that.

**Fix (inside the spec).**
- **08:** set a numeric cash-ceiling rule for the declared core buyer. For example: the flagship price is at most about one month of his take-home, and any installment is at most a stated share of monthly take-home.
- **LEDGER G:** add rows for $3.5–4.5k.
- **Raise Gate:** when a raise would cross the ceiling, require one of two explicit decisions. Either re-declare the core buyer in 02 and move the default protagonist, or keep a container under the ceiling for the core buyer. The async-only Program, already listed in BUSINESS §6 as a valid variant, is the natural candidate. This isn't the lower-intensity edge-buyer block that R1-M rejected. It's a decision about who the flagship serves once its price leaves the default buyer's reach.
- **13:** add a guardrail for the share of eligible leads who answer the affordability question "no".

---

### BUY2-5 · major · The paid assessment risks being a pitch he pays for *[regression]*

**Location.**
- BUSINESS.md §2: the core buyer has "nothing measured".
- FRAMEWORKS.md, Stall Verdicts: unmeasured / misdirected / the lever doesn't move.
- `part-1-2.md · 06 §6`: the written plan is specified in one sentence ("the stall verdict, first steps, the recommendation") and budgeted at about 400 words.
- `part-1-2.md · 06 extras`: "booking-page disclosure copy", content unspecified.
- `part-1-2.md · 08 §5`: the Layered Guarantee covers the Program only.
- `part-3-4.md · 15 §2`: the costly signals are refusals, fit-decline counts and the claim rate; there is no assessment outcome mix.
- `part-5.md · 20 §5`: "the optional paid group decision session".
- LEDGER.md B: no refund term for the assessment.
- THESES.md P5: the assessment "must be willing to return verdict 3".
- `critique/buyer.md` BUY-4, and DECISIONS R1 ("accepted in substance").

**Issue.** The default buyer is defined as someone who has measured nothing. So the assessment's most common verdict is "unmeasured", and the remedy for that is the measurement program the assessor sells. Verdict 3 ("the lever doesn't move for you") needs data he doesn't have yet. At the assessment it can only come from the Outcome Map, when his goal sits in the never-claimed column. And what the plan gives someone who doesn't buy is specified in a single sentence.

The first buyer pass proposed eight safeguards for the assessment (BUY-4). The architecture clearly carries one: a written plan worth its fee. It gestures at a second: 06's booking-page disclosure copy, whose content is unspecified. Four have no owner:
- publishing the mix of recommendations;
- a refund if the plan wasn't useful;
- a public sample plan;
- stating the credit expiry once, and never in follow-ups.

The paid group decision session has the same shape: he pays to attend a session whose job is to help him decide to buy.

**Why it matters to the buyer.** (A) has paid for a free "analysis" that always recommended the product. A $150–250 review concluding "you haven't been measuring, and my program measures" is that pattern with a receipt. (C) pays $200 to learn he can't afford the Program.

**Fix (inside the spec).**
- **06** specifies what the plan gives a non-buyer, as deliverables: a measurement setup he can run alone; what to stop spending on; which levers the Outcome Map says matter for his goal, and which don't; the verdict with its reasoning; and a re-check date.
- **06** also states on the booking page that the plan ends with one recommendation, which may be a paid program, the Starter Path, or "don't buy".
- **15 and 16** add the aggregate recommendation mix (Program, Starter Path, don't buy, referral) as a costly signal, published after about 30 assessments.
- **08** extends the Collectability Test to the assessment: the fee is refunded if he says the plan wasn't useful.
- **06** owns a labeled-composite sample plan, shown before purchase.
- **20** names the group session for what it is: "cohort walkthrough and Q&A; the offer and price are inside". Attendees stay anonymous, with names hidden and cameras off by default.

---

### BUY2-6 · major · The credit window turns his own fee into the deadline, contradicting the decision that relied on it *[regression]*

**Location.**
- BUSINESS.md §4: "$150–250, credited 14–30 days".
- BUSINESS.md §8: the assessment credit window is the first decision point listed.
- LEDGER.md B and C: the decision date.
- `part-1-2.md · 09 §4` and FRAMEWORKS.md, Decision Points: "credit window, seat cap, price step".
- `part-5.md · 19`: the Decision Date is "tied to the next real decision point", and the Follow-Up Rule includes a check-in on that date.
- HOUSE_STANDARD.md hard line 5: "No recovery pitches built on money he has already lost".
- THESES.md B11.
- DECISIONS.md R1-M on BUY-16: "a later start with the assessment credit held covers timing".

**Issue.** The window's force comes from money he has already paid: enroll within 14–30 days, or lose $150–250. That is a sunk-cost deadline. The architecture makes it a primary Decision Point, and the Follow-Up Rule can put the one check-in on the day it expires. R1-M rejected a lower-intensity option for edge buyers partly because "a later start with the assessment credit held covers timing". But no architecture file holds the credit past 30 days.

**Why it matters to the buyer.** (C), and anyone told "not now", lose the credit precisely because they were honest about timing. (A) recognizes "your credit expires Friday" as the tripwire-and-expiry funnel. The deadline is real, and it still fails the Informed-Client ceiling for the low-end client who bought mainly so as not to lose $200.

**Fix (inside the spec).**
- **06 and 09:** hold the credit through the next two starts, or about 90 days. For anyone whose recommendation was "not now" or the Starter Path, hold it until he enrolls, capped at around 12 months.
- State the credit terms once, in writing, and never in follow-ups.
- **09:** remove credit windows from the Decision Points list. What remains is the start's real seat cap and the announced price step.

This also makes R1-M's premise true.

---

### BUY2-7 · major · Scaling offers three overlapping paid reviews, and there's no Optimizer lane before month 9

**Location.**
- BUSINESS.md §5: the Decision Assessment ($150–250) is credited to the Program; the Priority Review ($350–600) is credited to Private; the Self-Serve System has an "optional single async review".
- BUSINESS.md §11: Private and the Priority Review are Scaling rungs.
- LEDGER.md B: the single async review is "at the assessment price"; founding 1:1 runs months 0–4; Private starts month 9+.
- BUSINESS.md §8: starts come every 6–8 weeks, then monthly.
- `part-1-2.md · 05 §4`: the Rung Activation Schedule.
- `part-1-2.md · 06`: Sell the Decision, Not the Diagnosis (no face analysis).
- `part-3-4.md · 11 §5`: the Premium Lane; the Optimizer's needs are "speed, precision, privacy, status".

**Issue.** At Scaling, a buyer sees three paid written reviews of himself. They differ in price, turnaround, and which rung they credit, so he has to guess his tier before the "one recommendation" is made.

Before month 9 the Optimizer has no premium lane at all, and in Bands A–B it comes well after that, because BUSINESS §11 lists Private as a Scaling rung. Founding 1:1 ends around month 4. The Priority Review and the fast lane arrive only with Private. Meanwhile "speed" means waiting up to 6–8 weeks for the next cohort start.

"Precision" is listed as his need but never defined. The precision he'll picture, a detailed read of his face, is the one thing the brand never sells.

**Why it matters to the buyer.** (B) has the money and wants speed, precision and privacy. For nine months or more he gets a group start date and nothing that buys speed. Worse, he may buy Private expecting a facial analysis, and feel misled when he learns it was never on offer.

**Fix (inside the spec).**
- **05 and 06:** make the Decision Assessment the single paid entry. Give it a priority-turnaround option from the Door Switch onward, and apply its credit to whatever is recommended, Program or Private. Fold the Self-Serve single review into it.
- **07:** allow late entry into a running cohort through week 1–2, so no one waits a full cycle.
- **11:** define precision as deliverables: matched captures, logged metrics, and turnaround stated as a point. State "we never read or score your face" on the Private card and the Priority Review page.

---

### BUY2-8 · critical · The Program is designed to end before outcomes appear, and he learns the full path at week 10

**Location.**
- MAP.md 11, shift: "The first program ends before outcomes appear".
- `part-3-4.md · 11`: the argument, and §1 "outcomes appear in months 4–9".
- BUSINESS.md §1: "Round Two and the Hold carry clients through the months when outcomes appear".
- FRAMEWORKS.md: the Expectation Document is owned by 07, "Also in 8, 21". Its only scheduled sign-off is the post-purchase Commit Ritual (MAP boundary 17↔21).
- `part-5.md · 18, 19, 20`: no module owns the path before purchase.
- `part-5.md · 22`: renewal is argued from "many habits aren't automatic by week 12".
- LEDGER.md B: prices.

**Issue.** The architecture's own thesis is that visible outcomes, where they come at all, show in months 4–9. That is during Round Two and the Hold. Yet the flagship is sold as a 12-week program. Nothing requires him to see the Expectation Document (time commitment, what can and can't move, plateaus, markers) before paying. Nothing before payment states the likely path or what it costs. The first time he hears "many habits aren't automatic by week 12" is in the renewal pitch.

The full path costs well above the sticker. My arithmetic from LEDGER B, for the Program plus Round Two plus three months of the Hold:

| Price band | Program sticker price | Program + Round Two + three months of the Hold | Months of a 24-year-old's take-home |
|---|---|---|---|
| Proof | $2.4–3k | ≈$3.3–4.7k | ≈1.2–1.7 |
| Above band | $3.5–4.5k | ≈$4.4–6.2k | ≈1.6–2.2 |

**Why it matters to the buyer.** This is the grift pattern (A) knows best: the front-end offer is the first installment of a longer sale. The momentum gate and the honest "you don't need Round Two" help. But a renewal offered at week 10, for the very months when results appear, still reads as planned. It fails the Informed-Client ceiling in plain sight. A client at the low end of the range who learns at week 10 that the product was designed to stop before outcomes wouldn't say it served him.

**Fix (inside the spec).**
- **07** owns a one-page Path and Timeline card, sent before payment. The Expectation Document also goes out before payment and is signed after it. The card states three things:
  - What the 12 weeks reliably deliver: the verdict, the record, the habits, and the week-12 re-assessment. This is the End of Guessing promise.
  - When visible change tends to show, where it happens at all. Use category-level language until the operator has his own data, then his own range with its denominator.
  - The likely total cost of the Program, Round Two and the Hold, as a range. Show it next to the published share of clients told "you don't need Round Two".
- **18, 20, 19 and 27** recap the card and point to 07: in the offer pieces (18), on the result page (20), in the recommendation segment (19), and on the Verify Page (27).
- **22** then argues renewal from his data against a timeline he already accepted, not one he's hearing for the first time.

---

### BUY2-9 · critical · The Burned Struggler gets the closer's playbook *[regression]*

**Location.**
- THESES.md P4: "Burned buyers are the exception route: their 'I need to think' is due diligence to be supported".
- THESES.md P13: the verification-first path includes a "sample deliverable", with "no stakes questioning, a decision date *he* chooses".
- THESES.md B11: "prior spend is used diagnostically only".
- HOUSE_STANDARD.md:
  - the floor;
  - nine things #2: "name what 'I need to think' is hiding";
  - #3: "Reflect his months, money, and missed moments back to him, plainly";
  - #8;
  - hard line 5.
- FRAMEWORKS.md: State Routing reads "Burned → verification first", and the Verify Page definition has no sample deliverable.
- `part-5.md · 19`: the opening frame, §4 ("I need to think"), and §5.
- LEDGER.md A4: "sample plan" appears in the Early building line, but no module in MAP or FRAMEWORKS owns it.

**Issue.** The burned buyer's protections didn't survive into the files drafters will follow.
- **The exception is gone.** THESES is removed at ship. The House Standard, which every module's Standard Check quotes, now licenses the opposite:
  - the floor says that not challenging his story fails him;
  - #2 licenses naming "what 'I need to think' is hiding";
  - State Routing is cut down to "verification first", without "no stakes questioning" or "a decision date he chooses".
- **His lost money becomes the anchor.** #3 licenses reflecting his money back to him as a stake. For this buyer, that money is what he lost to grift. In a live call the order is stake, then recommendation, then price, so the lost money works as an anchor whatever the intent. That is the recovery pitch that #8, hard line 5 and B11 forbid.
- **The verification kit has a hole.** A sample written plan and a sample weekly review appear only in LEDGER A4's building line and in THESES. No module owns them, and the Verify Page's definition leaves them out.

**Why it matters to the buyer.** (A) was burned by closers. "What's 'I need to think' really hiding?" and "you've already put $600 into a device that did nothing" are the lines that came before his last bad purchase. His due diligence is exactly what the brand's positioning teaches him to do. Handling it as an objection tells him the brand is the grift with better manners.

**Fix (inside the spec).**
- **House Standard, the floor and #2:** name the burned route as an exception. With a buyer who has been burned before, "I need to think" is due diligence. Support it with the verification kit, make one firm recommendation, and let him choose the date.
- **House Standard #3:** "money" means money at stake from here on. Prior spend belongs in the diagnostic part of a conversation, and it never appears in the recommendation-and-price segment, for any buyer.
- **FRAMEWORKS State Routing:** carry P13's full wording. 19 §5 and its Burned excerpt then script it.
- **20:** the result page's Burned branch sends the verification kit, not the sales sequence.
- **06 and 07** own a labeled-composite sample plan and sample weekly review, and **27** adds both to the Verify Page.

---

### BUY2-10 · major · No module owns the appearance-anxious buyer *[regression]*

**Location.**
- `part-1-2.md · 02 §6`: names "the dignity route" once.
- FRAMEWORKS.md: no dignity route; State Routing has four routes.
- MAP.md 15: owns "dignity mechanics (shame proximity; never press the wound)".
- MAP.md 19: "Leans on: 2, 8, 9", not 15.
- `part-5.md · 19 §2`: the Destination Ladder live, the implication question, and the silence after it.
- `part-5.md · 18 §4`.
- HOUSE_STANDARD.md #3 ("missed moments … plainly") and #5 (the destination named "vividly", then "the obstacle and the plan").
- THESES.md P13: "Insecurity-led buyers get the dignity route".
- `critique/buyer.md` BUY-12: "pair desire-naming with a line that puts appearance in perspective", accepted in substance under R1-14.

**Issue.** THESES gives insecurity-led buyers a dignity route. The architecture names it once, in 02 §6, and never defines it.
- **The deepest sequence isn't linked to the dignity rules.** 19 teaches the sequence that goes deepest into the wound: laddering from "a sharper jaw" to "taken seriously", the implication question, reflecting missed moments, and holding the silence. Yet 19 doesn't lean on 15, where "never press the wound" lives, or on 02 §6.
- **The licensed stake is the wound.** For this buyer, "missed moments" (dodging photos, holding back in rooms) is the wound, and the House Standard licenses reflecting it plainly.
- **The perspective line never landed.** The accepted fix was to pair desire-naming with a line that puts appearance in perspective. Instead, #5 pairs the destination with "the obstacle and the plan". In a face brand, that completes the implied chain: the face is why he isn't taken seriously.

**Why it matters to the buyer.** (D) is 5–20% of appearance-change seekers, and most won't trip an unscored, self-reported check. He will be on calls and in the content audience. "Name the destination vividly, reflect the missed moments, hold the silence, name the price" can leave him more defective and fail the Dignity Check, without any single rule being broken.

**Fix (inside the spec).**
- **15** owns and defines the dignity route.
  - **Triggers:** insecurity-led language, a fit-check signal judged non-acute, or checking frequency.
  - **What changes:** stakes are limited to time, money at stake from here on, and guessing, with no reflection of missed social moments. Laddering stops at the destination. The recommendation is still made firmly.
- **19:** add 15 and 02 §6 to 19's Leans-on list.
- **19 and 20:** add the dignity route to State Routing (19) and to the result-page branches (20).
- **House Standard #5 and 18:** restore the perspective line, including in 18's use of Fantasy to Expectation. Any asset that names the destination carries one line that places it beyond the face: presentation, how he's photographed, knowing, and the parts no program touches.

---

### BUY2-11 · major · Identity turns the fit check and the price into status

**Location.**
- FRAMEWORKS.md, ★ Adults Who Measure: "adult, fit-checked, and logging is the status".
- HOUSE_STANDARD.md, nine things #7, and the house rule "The fit check … never a label".
- `part-3-4.md · 17 §2`: "status framing for young men (adults-only, fit-checked, premium signals seriousness)".
- `part-3-4.md · 17 §3` and FRAMEWORKS.md, Measurement Rituals: the re-captures as rituals.
- HOUSE_STANDARD.md, stop rules: the Starter Path is where "I can't afford it" lands.

**Issue.**
- **Fit-checked as status.** If being fit-checked is the status, failing the check is a label, and the house rules say the fit check must never be one. Starter Path users are never fit-checked at all, because the check runs only before a paid step. So the in-group excludes them by construction.
- **Premium as seriousness.** If premium signals seriousness, the Starter Path is the unserious tier, and it's where the stop rule sends everyone who can't afford the Program.

Identity mechanics are allowed, but these two markers aim them at exactly the buyers the hard lines protect. The re-captures as rituals also put face photos near the center of the identity, which is the wrong signal for a buyer prone to checking.

**Why it matters to the buyer.** (D) is the buyer most likely to be paused or referred by the fit check, and then to see content announcing that fit-checked adults are the in-group. (C) hears that seriousness has a price. Both leave more defective. (A) and (B) need neither marker, because logging already carries the status.

**Fix (inside the spec).**
- **17:** anchor the in-group on the practice: logs kept, captures on schedule, decisions made from the record. Name Starter Path users as members explicitly.
- "Fit-checked" stays a safety standard the brand holds itself to, never a trait of the member.
- Replace "premium signals seriousness" with "standards signal seriousness".
- Make the review and the decision the ritual, not the photo.
- **15:** add the declined buyer and the budget buyer to the Dignity Check's worked examples.

---

### BUY2-12 · major · The objection map misses the objections that decide the sale, and no module owns privacy before purchase

**Location.**
- `part-5.md · 19 §4`: the niche map has seven objections, and reads "I need to ask my parents" only as "minor → stop".
- THESES.md §1c: its objection map includes "no time", "I've failed before" and "is this legit?".
- `critique/buyer.md`, "Missing": scripted answers still open.
- `part-1-2.md · 07 §2, §4`: the Expectation Document, and the group-call recording.
- `part-1-2.md · 08 §4–5`: cancel-forward and the non-response clause.
- `part-3-4.md · 12 §5`: privacy operations.
- `part-3-4.md · 17 §4`: the free baseline capture, with storage unstated.
- FRAMEWORKS.md, 25 Keyword Route: "an Instagram keyword that sends a DM".
- FRAMEWORKS.md, 27 Verify Page: "… policies, prices, guarantee terms".

**Issue.** 19's map covers the category objections well. It misses the ones that decide the sale for these buyers:
1. "How much of your time do I actually get for $X?"
2. "Who sees my photos, and can anyone find out I'm doing this?"
3. "I work full-time. How many minutes a day?"
4. "I've tried everything and I always quit."
5. "How long until I see anything, and what will the whole thing cost?"
6. "Can I stop paying if it isn't working?"
7. An adult saying "I need to talk to my parents / partner".

On objection 2, no module owns the privacy promise before purchase. The Verify Page lists "policies" but has no privacy section, and 07 and 12 own privacy only in delivery and operations. There are two concrete leaks:
- The Keyword Route's definition doesn't say how the keyword is sent. If it's a public comment under a facial-development post, his followers see it.
- Nothing says whether the free baseline capture is uploaded or stays on his phone.

On objection 7, the only reading is "minor → stop". For an adult it's either a funding signal (the money isn't his, so affordability applies) or ordinary joint decision-making. Neither should get the Real-Objection Sort's two probes.

**Why it matters to the buyer.** These are the questions all four buyers ask before paying. Unmapped objections get improvised on the call, which is where pressure creeps in. (A) and (D) care most about friends finding out, and a public keyword comment is exactly the exposure they're avoiding. (B) will ask objections 1 and 2 in his first minute.

**Fix (inside the spec).**
- **19:** add all seven to the map. Tag each with its Belief Chain link, and point it to the module that owns the substance:
  - 07 for time and privacy;
  - 08 for cancel-forward;
  - the Path and Timeline card for objection 5 (BUY2-8);
  - 14 and 21 for prior failure;
  - 02 and 06 for affordability.
- **Adult parents or partner:**
  - Ask the affordability question: "from your own monthly income".
  - If the money isn't his, recommend the Starter Path.
  - If it's a joint decision, send the written recap he can share and let him set the date, with no probes.
- **27:** give the Verify Page a named privacy section. It covers who sees photos, where they're stored, deletion, which tools touch his check-ins, who can access call recordings, discreet billing and sender names, and pseudonymous cohorts.
- **25:** keywords are sent by DM, never posted as comments.
- **17:** the free baseline capture stays on his device until a paid step.

---

### BUY2-13 · major · Three consistency devices hem in the fit window

**Location.**
- HOUSE_STANDARD.md: "a fit window with a full refund after a short conversation". The rule against timing consistency devices to refund rights is absent.
- LEDGER.md B: the fit window is 14–21 days, "full refund through a short conversation".
- `part-1-2.md · 08 §5` and `part-3-4.md · 17 §5`: "never timed to refund rights".
- `part-5.md · 21`: the argument ("The Commit Ritual answers buyer's remorse with evidence") and §2 ("his written reasons … remorse inside the fit window").
- MAP.md 16 and `part-3-4.md · 16 §5`: "process … testimonials from week two".
- `part-3-4.md · 10 §5`: the R&D Harvest says the same.
- FRAMEWORKS.md, Measured-Peak Asks: "only at measurement moments".

**Issue.** The rule is right. It lives in 08, 17 and 21's Standard Check focus, but not in the House Standard. Three parts of the architecture sit inside the 14–21-day window:
1. **The Commit Ritual** collects his written reasons, and its stated job is to answer remorse.
2. **Testimonials** are asked for "from week two", which is days 8–14. That is inside the window and isn't a measurement moment, so 16 contradicts 22's Measured-Peak Asks.
3. **The refund** requires "a short conversation", and no module defines its purpose or limits. A burned buyer reads that as a save call.

**Why it matters to the buyer.** (A) knows the retention call, and (D) may dread any call at all. A client who wrote down his reasons on day one and praised the program on day ten is less likely to claim, on day twelve, a refund he's entitled to. That is exactly what "never timed to refund rights" forbids.

**Fix (inside the spec).**
- **House Standard:** add the rule that consistency devices are never timed to refund rights.
- **08** defines the fit-window conversation. It's optional, and a written request is enough. It's for feedback only, with a stated maximum length. The refund is processed whatever is said, and there's no re-pitch.
- **21:** his written reasons are never quoted in any refund or exit conversation. The Commit Ritual's job is clarity, not preventing remorse.
- **16 and 10:** no testimonial ask before the fit window closes. The first process-testimonial ask comes at the first measurement moment after it: the week-6 read, and only if that read is a peak. This makes 16 and 22 agree.

---

### BUY2-14 · major · Attention falls as the price rises, and the review automates without disclosure *[regression]*

**Location.**
- LEDGER.md A4, client review per client-week: founding 1:1 about 35 min; founding group about 15; Growing about 10; Scaling about 8, with templated review at 6–10.
- LEDGER.md B: price runs from about $1.2–1.5k for the founding group to about $3.5–4.5k above the band.
- `part-1-2.md · 07 §2`: "the templating path from ~20 minutes to ~8".
- `part-1-2.md · 08 §3`.
- `part-3-4.md · 12 §5`: the AI line, "templated summaries".
- HOUSE_STANDARD.md: "AI assists; it never appears".
- FRAMEWORKS.md, Seat Math: "publish seats and deliverables, not minutes". The Folded list records "Seat Math as a public disclosure (now internal)".
- THESES.md B10: "justify it by what was added, never by demand". This is absent from 08 and from the Raise Gate's definition.
- BUSINESS.md §6: routing help handles the inbox at Scaling.

**Issue.** From the founding group to above the band, the Program's price roughly triples while individual review minutes roughly halve. The review also becomes templated, with AI helping on the summaries. Choosing not to publish raw minutes is defensible, because it invites per-minute pricing. What's missing is:
- any disclosure of how the review is produced;
- any rule telling clients where AI and routing help touch their data;
- any straight answer to "how much of you do I get?".

From the buyer's side, "AI assists; it never appears" reads as "the AI is hidden". And the rule that a raise is justified by what was added, never by demand, didn't reach 08. The Raise Gate's triggers include conversion and utilization, which are demand signals.

**Why it matters to the buyer.** (B) pays the highest price for the thinnest human review, and he's the buyer most likely to ask what's automated. Suppose a client finds out his weekly personal review was a template with an AI-drafted summary and a freelancer on his inbox. He will feel the grift, even though every minute was approved. The ceiling test rules out anything that only works while he can't see it. The founding client, by contrast, is the best-served buyer in the whole architecture. That's fine, as long as later buyers know what changed.

**Fix (inside the spec).**
- **07's Expectation Document** states how reviews are made:
  - the operator reads every log and writes or approves every review, using a structured template;
  - which tools help summarize, and who routes messages;
  - what those tools and helpers never see: photos and health-adjacent answers;
  - the turnaround, stated as a point.
- **House rule:** reword it to "AI assists behind the scenes, never speaks as you, and clients are told where it helps".
- **12:** add client consent before any tool processes check-ins.
- **19:** answer "how much of your time?" straight, from the deliverables and the review format.
- **08:** restore "justify it by what was added", with two rules. A raise is never paired with a cut to a published deliverable or turnaround. Each price step names what was added, in terms the buyer can see.

---

### BUY2-15 · critical · At the plateau, every road leads back into the Program

**Location.**
- LEDGER.md B: the non-response clause is "Pre-agreed week-6 markers; cash partial refund ~25–50% on exit", and its "Moves it" column reads "Marker design".
- FRAMEWORKS.md: the Expectation Document lists "the week-6 markers" (07); the Layered Guarantee (08); the Plateau Protocol and the Honest Exit (21).
- `part-1-2.md · 07 §4` and `08 §5`.
- `part-5.md · 21 §4`: "pre-announcement; re-attribution to controllables with his data; … the re-sale conversation".
- `part-5.md · 22`, worked example: "one exits under the clause" in weeks 10–12.
- `part-3-4.md · 11` and THESES.md B15: outcomes in months 4–9.
- THESES.md P5: "never 'you weren't consistent' as a default alibi".
- HOUSE_STANDARD.md, five checks: the Collectability Test.

**Issue.** The burned buyer's real risk reversal is the non-response clause, and no module owns what its markers measure. 07 lists them, 08 guarantees them, and 21 applies them, but none says what a good marker is. The architecture's own timeline boxes the markers in:
- **If they measure visible change,** week 6 falls before the months when outcomes appear. A flat read is a "pre-announced plateau" by design. The protocol's default next steps are "re-attribution to controllables" (what you can adjust), then "the re-sale conversation".
- **If they measure adherence,** a client who adheres passes by definition.

Three more problems follow:
- After week 6 there is no non-response recourse at all, and the next measurement moment is where Round Two is sold.
- The refund's low end, 25%, is half of pro-rata at the program's midpoint.
- 22's worked example has a client exiting "under the clause" in weeks 10–12, which suggests even the clause's timing isn't settled.

**Why it matters to the buyer.** For (A), this is the loop that burned him: "it takes time", then "adjust your consistency", then "the real results come in phase two". The program's own timeline makes this guarantee nearly impossible to trigger, so it fails the Collectability Test, one of the House Standard's five checks. And it's the one guarantee he would actually try to collect on.

**Fix (inside the spec).**
- **08** owns marker design, written into the Expectation Document before payment. Markers must be:
  - measurable signals the Program itself says should move by week 6 (intermediate, behavior-linked, and in the changeable column);
  - never adherence, which is the precondition, not the marker;
  - never appearance change the Program says arrives later;
  - each set with a threshold.
- **21:** the week-6 read asks the verdict question first ("given your adherence, is the lever moving?") before any re-plan. A pre-announced plateau can't be used to pass a failed marker.
- Set the refund floor at pro-rata of the undelivered weeks, about 50% at week 6.
- State whether a second check exists at week 12, and fix 22's worked example to match.
- **08** runs the Collectability Test on the marker set, with a worked pass-and-fail example, and publishes the claim rate once data exists.

---

### BUY2-16 · minor · Three names fail the glass-box rule, and the ask rule permits asks at a flat read

**Location.**
- FRAMEWORKS.md naming principle 1, and THESES.md H10 (the Hostile-Screenshot Test).
- FRAMEWORKS.md:
  - ◆ Every Plateau Is a Re-Sale (21);
  - ★ The Buying Test Only You Pass (16). MAP.md 16's own shift says "a buying test only honest operators pass".
  - ○ Felt-familiarity premium (08);
  - ★ Measured-Peak Asks: "only at measurement moments".
- `part-5.md · 22 §4`: upgrade asks for Private.

**Issue.** Three names say the quiet part out loud:
- **"Every Plateau Is a Re-Sale"** tells a client his stall is a sales moment.
- **"The Buying Test Only You Pass"** says the yardstick was built so only this operator passes. MAP 16's own shift has the accurate version: only honest operators pass.
- **"Felt-familiarity premium"** says his parasocial trust carries a price tag.

Separately, Measured-Peak Asks is defined by "measurement moments", and week 6 is one. So a Private upgrade ask at a flat week-6 read is technically allowed.

**Why it matters to the buyer.** The Glossary is a deliverable, and names leak through freelancers and screen-shares. (A) would take any one of these as proof that the honesty is a technique. The ask definition matters more: an upgrade pitch at the moment he's stuck is the "buy the premium tier to break your plateau" move.

**Fix (inside the spec).**
- Rename the first two "Every Plateau Renews the Decision" and "The Honest-Evidence Test".
- Drop the third name, and fold the idea into the prose on the credibility ceiling.
- Redefine Measured-Peak Asks as asks made "at a measurement moment that shows progress on his own record — never at a plateau, a flat read, or an exit read".

---

### BUY2-17 · major · The Hold and Private are sold on deliverables the design week doesn't fund

**Location.**
- BUSINESS.md §5: the Hold offers "periodic review, re-captures, belonging". Private offers a weekly 30–45 minute call, a stated turnaround, and a business-hours line.
- BUSINESS.md §6: the $25k configuration has about 45 Hold members and about 1 Private seat a quarter; the $50k configuration has about 65 members and about 2 seats. Both are at Scaling revenue.
- `part-3-4.md · 11 extras`: a Round Two offer card and a Private deliverables card, but for the Hold only "Hold terms (disclosure, reminder, exit)".
- LEDGER.md A4: "Private seats / alumni reviews" has no line before Scaling, and 1.0 h a week at Scaling.
- LEDGER.md B: Private is "~12–15 delivery h … per seat", which is about 1–1.25 h a week.
- LEDGER.md H: the De-Scoping Order protects "review turnaround".

**Issue.** The Hold has terms but no deliverables, only review at an unstated "periodic" frequency. In the Scaling design week, Private seats and alumni reviews share 1.0 h a week. Two Private seats alone need about 2–2.5 h a week, which leaves the roughly 65 Hold members' reviews unbudgeted. Even ten minutes each per quarter comes to about 50 minutes a week. The Growing design week has no line for either.

**Why it matters to the buyer.** A monthly charge of $39–79 for a room, plus reviews that get squeezed out, is the continuity product (A) has already cancelled once. (B)'s business-hours line and weekly call are the first things a 20-hour week sheds when it runs hot. The De-Scoping Order protects review turnaround, but not Private's call cadence or its message line.

**Fix (inside the spec).**
- **11:** add a Hold deliverables card. It states the review frequency as a point (e.g., one written review per quarter alongside the re-capture), what the room does week to week, and the operator's touch per member.
- **07's Seat Math:** cap Private seats and Hold size from budgeted minutes, the same way it caps cohort seats.
- **12:** add Private and alumni-review lines to the Growing and Scaling design weeks, sized to the BUSINESS §6 configurations.
- **08:** extend the service guarantee to Hold and Private deliverables, with the same credit-or-refund remedy.

---

### BUY2-18 · major · The Starter Path is the whole brand for the budget buyer, and it's one paragraph

**Location.**
- `part-1-2.md · 05 §5`: about 700 words, shared with the Self-Serve System.
- BUSINESS.md §5: "free branch (public curriculum + logs); a low-cost Starter tool named once".
- LEDGER.md B: human touches are batched, as a monthly group Q&A or a templated check.
- HOUSE_STANDARD.md, stop rule: "name the Starter Path once, then stop".
- `part-3-4.md · 17 §4`: the Back-Dated Baseline.
- `part-1-2.md · 08 §3`: "the raise always happens".

**Issue.** Every "can't afford", "not now" and non-fit buyer lands on the Starter Path. The architecture defines it only as a free branch (public content plus logs) and a paid tool "named once". Nothing specifies:
- a sequence he can follow;
- a self-check;
- when to come back;
- what happens to his logs when he does. The Back-Dated Baseline exists, but it isn't connected to the Starter Path.

Meanwhile, the price keeps stepping up while he saves.

**Why it matters to the buyer.** For (C), this is the purest case of under-selling. The one firm recommendation he gets is "the Starter Path", and if that means "watch my videos", the brand has under-served him. The Informed-Client floor applies to him too, just at a different rung. A path with a re-entry point also turns the saver into a future client instead of a lost lead.

**Fix (inside the spec).**
- **05:** specify the free branch as a sequenced path he runs himself: what to do in weeks 1–4 and 5–8, which logs to keep, a self-check at weeks 4 and 8 against the Outcome Map, and a re-entry trigger. Make clear that "named once" applies to the paid tool, not to the free path.
- **19:** the stop-rule line hands over the path as a concrete next step in the written recap: the first action, the log, and the re-check date.
- **17:** if he enrolls, his Starter Path logs become his back-dated baseline.
- **08:** tell him plainly how and when prices step up. If he paid for an assessment, his credit is held (BUY2-6).

---

## (a) The five highest-priority fixes

1. **Make the stop rules bind automation (BUY2-1).** 06 owns a content-free *pause* route tag. 26, 20 and 09 honor it: no sales sequence, and no start or price-step sends. The House Standard adds "Stop rules bind automation too." This is the one place where the architecture, as written, crosses hard line 5 without anyone deciding to.
2. **Show the whole path before he pays (BUY2-8).** 07 owns a Path and Timeline card: what 12 weeks deliver, when visible change tends to show, and the likely total cost of Program, Round Two and Hold. The Expectation Document goes out before payment, and 18, 19, 20 and 27 recap it.
3. **Give the non-response clause real markers (BUY2-15).** 08 owns marker design: never adherence, and never appearance change the Program says comes later. The week-6 read asks the verdict question before any re-plan, and the refund floor is pro-rata.
4. **Restore the burned route in the House Standard (BUY2-9).**
   - His "I need to think" is due diligence, and he chooses the date.
   - In a stake, "money" means money at stake from here on, never money already spent.
   - State Routing carries P13's full wording.
   - 06 and 07 own a sample plan and a sample weekly review for the Verify Page.
5. **Add a fit-check signal protocol (BUY2-2).** No same-day payment, written adjusted expectations, a cooling-off gap, no plan, and no capture tools for checking or fixation signals. B12's care for serial purchasers is carried into 06 and 08.

Next in line:
- Define the dignity route and link 19 to 15 (BUY2-10).
- Put the affordability question before every paid step, including checkout (BUY2-3).
- Set a numeric cash ceiling (BUY2-4).
- Disclose how reviews are made (BUY2-14).

## (b) What the architecture gets especially right from the buyer's side

- **It answers the bone question straight.** The Outcome Map and the Honest Answer (03) are what (A) came looking for. The null-result stance keeps the offer honest if visible change turns out small.
- **It guarantees what it controls, and never appearance (08).** There is a full-refund fit window, a service guarantee on the operator's own inputs, cancel-forward plans, and a published claim rate. The right to stop paying is rare in this category, and (A) will notice it.
- **Its prices are public and clean (House Standard #8).** Every tier is real. There are no decoys and no invented "total value", and it never anchors on surgery, sunk spend or hourly rates.
- **Its dates are real (09).** Seat caps come from capacity, with a public fill history that includes under-filled starts. There are no countdowns and no window bonuses.
- **Privacy is part of the product (house rules).** Photos are coach-only, cohorts can be pseudonymous and camera-optional, billing and sender names are discreet, and anything can be deleted.
- **It limits appearance checking by design (07).** Behavior is measured often and appearance rarely, which protects (D).
- **Its verdicts can say stop (14, 21).** "The lever doesn't move for you" is an allowed verdict, backed by the Honest Exit.
- **Round Two has to be earned (11, 22).** It's gated on measured momentum, with an honest "you don't need it".
- **Minors get education and no data (06).**
- **The operator's own face is never offered as proof (15).**
- **Commitment is built on his own record (17).** "Let him succeed before he pays" and the Back-Dated Baseline turn his DIY months into data rather than shame. Commitments stay private by default.
- **He always gets it in writing (19).** A written recap follows every call, and a burned buyer values that more than any script.

## (c) Verdict

From the buyer's chair, this is the most defensible architecture I've seen for this category. It answers the bone question, prices in public, guarantees what it controls, protects photos and minors, and allows a verdict that says stop. Its failures are at the seams, where one module's protection ends and the next module's machinery begins:
- The stop rules never reach the email system.
- The burned-buyer and dignity routes were lost between THESES and the House Standard.
- The flagship is designed to end before outcomes, and the buyer finds that out at renewal.
- The one guarantee a burned buyer would try to collect has no marker design, and the program's own timeline absorbs any flat week-6 read.
- The price climbs out of the default buyer's reach while the review he gets thins and automates, and nobody tells him.

None of this needs a new principle. Each fix is a disclosure, a routing rule, or a protection that already exists in THESES or DECISIONS and needs an owning module. Make the five fixes above, and a 24-year-old who has been burned will find the rare offer that survives his audit. Leave them, and he'll find the seams within weeks of paying. Then he'll say so where the next buyer searches the brand's name.
