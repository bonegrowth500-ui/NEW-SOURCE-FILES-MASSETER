# Stress test: the rival operator

**Lens.** I've built and scaled coaching businesses in fitness, skincare, looksmaxxing-adjacent self-improvement and dating. I read this architecture the way I'd read a competitor's plan: where it leaks money, where it's slow, what I can copy, and where its owner runs out of hours. I don't critique the locked spec (the exclusions, the persuasion standard, the track counts). I critique what's built inside it.

**Evidence.** Read in full: BUSINESS.md, MAP.md, FRAMEWORKS.md, briefs/part-1-2.md, part-3-4.md, part-5.md, part-6-7.md and LEDGER.md. Consulted: THESES.md, HOUSE_STANDARD.md, STANDARD.md, DECISIONS.md and critique/operator.md. I ran models/model3.py and models/mid.py. Unlabeled numbers come from the LEDGER or the model outputs. Anything marked *rival estimate* is my own assumption, and I say what it's anchored on.

**Count.** 20 findings: 2 critical, 16 major, 2 minor.

## Summary

| ID | Sev. | Main location | One line | Q |
|---|---|---|---|---|
| RIV-1 | critical | BUSINESS §2, §6–7 · LEDGER B, G · Modules 02, 08, 13 | The price path outruns the buyer. $25k in Band B and the $50k plan both need prices that the eligibility rule screens out | 1, 2 |
| RIV-2 | critical | BUSINESS §6 · LEDGER A4, B, C · Modules 04, 07, 12, 20 | On the LEDGER's own unit costs, the $25k and $50k weeks run ~23–29 h | 1 |
| RIV-3 | major | BUSINESS §4 · LEDGER C · Module 06 · model3.py | The Door Switch as written would cut Growing enrollments. The model behind the waypoints doesn't switch; it overflows | 1 |
| RIV-4 | major | BUSINESS §5, §11 · LEDGER A3, B · THESES B7 · Modules 05, 10 | The founding seat cap sets month 3, and the founding 1:1 is underpriced against the playbook's own rules | 1, 2 |
| RIV-5 | major | model3.py · LEDGER C, H · THESES §7 · Modules 04, 10 | In the weak case, month 3 rests on an unlabeled warm-network constant. The Month-3 Gate can't see a volume failure | 1 |
| RIV-6 | major | LEDGER B, D · Modules 07, 08, 11, 21 | The week-6 cash clause judges response before the playbook's own outcome window, and its markers are undefined | 1 |
| RIV-7 | minor | LEDGER A3, B, C, D · BUSINESS §6 · model3.py | Several denominator slips, all biasing the plan upward | 1 |
| RIV-8 | major | BUSINESS §5–6 · LEDGER B, H · THESES B17 · Modules 11, 19 | The premium lane is sequenced backwards | 2, 6 |
| RIV-9 | major | LEDGER A4, B · THESES B2 · Module 11 | Round Two spends full care minutes at about a third of the flagship's price | 1, 2 |
| RIV-10 | major | BUSINESS §5 · THESES P20 · LEDGER E · Module 11 | The back end starts late and small | 2 |
| RIV-11 | major | BUSINESS §8 · LEDGER B, C, H · Modules 08, 09 | Before Scaling, real dates have no force, and the Raise Gate is slow and statistically noisy | 1, 2 |
| RIV-12 | major | LEDGER A3, F · Modules 04, 13, 27, 28 | Band A's only plannable reach lever comes last and is switched off in Early | 2, 6 |
| RIV-13 | major | BUSINESS §3, §5 · Modules 03, 13, 15, 16 | The moat is copyable by design, and the clock on the one uncopyable asset starts at Scaling | 3 |
| RIV-14 | major | LEDGER A4, B, F · Modules 10, 12, 19, 24, 26 | The Early week's hours are allocated against its own binding constraint | 4 |
| RIV-15 | major | BUSINESS §4 · LEDGER C, D · Modules 06, 17 | The free 7-day log stands between the lead and the scarcest input | 4, 6 |
| RIV-16 | major | LEDGER A4, H · Modules 05, 07, 11, 12, 20 | After month 6, the leverage layer has no hours to be built | 2, 4 |
| RIV-17 | minor | FRAMEWORKS count · HOUSE_STANDARD checks | 174 named items and about a dozen checks per asset | 4 |
| RIV-18 | major | briefs default budget · Modules 06, 18–22, 28 | The money modules can't hold their scripts, and Modules 19 and 28 are overloaded | 5 |
| RIV-19 | major | MAP · Modules 01, 09, 25 (+04, 08, 11, 13) | Three modules risk padding, while the $50k path has no module | 5 |
| RIV-20 | major | MAP pointer · Modules 02, 03, 06–08, 12, 15, 21 | The month-1 job is spread across modules the early-stage pointer doesn't name | 6 |

---

## Findings

### RIV-1 · critical · The price path outruns the buyer it was built for

**Location.**
- BUSINESS.md §2: the core buyer is "able to pay from monthly income", and eligibility rests on the affordability question.
- BUSINESS.md §6 (the $25k and $50k configurations) and §7 (the Three Ceilings).
- LEDGER.md B (above band ~$3.5–4.5k) and G (the take-home table and the affordability question).
- models/mid.py (Band B maturity).
- Module 02 §4 and Module 08 §2 (briefs/part-1-2.md); MAP Module 13 ("the $50k levers").

**Issue.** The configurations that reach the target need prices the default buyer can't pay under the playbook's own eligibility rule.

- **Band B needs the above band for $25k.** Band B is the band the playbook tells the operator to plan on. In mid.py, Band B maturity gives ~$21k profit at proof prices and ~$30k above the band. LEDGER A3 agrees: $25k in Band B arrives "once price moves above the proof band or conversion matures".
- **$50k needs ~$4k prices.** The $50k configuration is ~11 enrollments a month at ~$4k.
- **Those prices cost the core buyer about a month of take-home or more.** On LEDGER G's figures, $3.5–4.5k is ~1.25–1.6 months of take-home for a 20–24-year-old and ~0.9–1.15 months for ages 25–34. Split into three installments, a $4k price is ~$1.33k a month: 48% and 34% of monthly take-home.
- **The affordability wording screens out savers.** The Eligibility Rule (Module 02) and the affordability question (LEDGER G) ask whether the price is "comfortable from your monthly income without new credit". That wording also excludes buyers paying from savings, which is the normal way to pay for a $2–4k purchase.
- **The cash ceiling has no threshold.** Module 08 defines it in months of take-home but never sets a limit, and LEDGER G's table stops at $3k.
- **Nobody owns the buyer-mix shift.** Above-band pricing needs older, employed buyers and Optimizers. BUSINESS §2 rejects Optimizer-first positioning as a "much smaller pool", and none of Module 02's stage notes mention a shift in mix.

**Why it costs.** The Raise Gate will walk the price into a wall. At the above band, affordability no's rise, the gate's "price named in <1 in 5 no's" signal stops firing, and the raise halts. That protects the buyer but strands the plan: $25k in Band B and the whole $50k plan stall with no module that explains why. Worse, an operator under pressure bends the affordability rule, which is hard-line-5 territory.

**Fix (inside the spec).**
1. Extend LEDGER G's months-of-take-home table to $3.5k and $4.5k. In Module 08, set a cash-ceiling threshold for each price band, stated as the share of the core buyer who clears it.
2. Reword the affordability question to "comfortable from your income or savings, without new credit or buy-now-pay-later". Hard line 5 still holds: no new credit, and "I can't afford it" still ends money talk.
3. Give one module ownership of the buyer mix by price band: which states and ages carry each band, and which packaging moves the mix (the Age-Up Dial, decision-stage topics, the Optimizer lane). Shift the mix by state and age, never by income targeting, which BUSINESS §2 rules out. Add a Scaling Trigger: raise into the above band only when a set share of held conversations clears the cash ceiling at the new price. The owner should be the new $50k module in RIV-19; otherwise split it between 02 (mix) and 13 (trigger).
4. Re-derive the $50k configuration with a conversion rate that falls as price rises.

### RIV-2 · critical · On the LEDGER's own unit costs, the 20-hour week at $25k and $50k doesn't close

**Location.**
- BUSINESS.md §6: "steady state, ~20 h/week"; care hours "~9–10" and "~10–11".
- LEDGER.md A4 (the design weeks, operator hours per enrollment, and the all-in time for a paid assessment), B (the service guarantee and Private hours), and C (which has no row for async or direct-checkout conversion).
- models/model3.py lines 69–75: cohort yield counts review plus the amortized call only.
- Module 07 §2 and §4–5, Module 12 §1, and Module 20.

**Issue.** The design weeks count weekly review and group calls. They leave out four kinds of work that the same files require:

- **(a) Milestone deliverables under the service guarantee.** The written week-6 read and the week-12 re-assessment carry "missed = credit or refund" (LEDGER B), and onboarding adds the Commit Ritual and the 72-hour touch (Module 21). No design week and no model line carries any of them. The re-assessment should cost about what LEDGER A4 gives a templated assessment (0.5–0.75 h), and the week-6 read about half that. On that anchor, the extra time over a normal review is ~0.75–1.2 h per enrollment (*rival estimate*). At 11 enrollments a month, that is ~1.9–3.1 h/week.
- **(b) Selling time.** LEDGER A4 prices an enrollment at ~1.5–3 operator hours on the async or paid door. Eleven a month need ~3.8–7.6 h/week. The Scaling week holds 3.25 h (2.75 for assessments plus 0.5 for follow-up), enough for about 5–9 enrollments.
- **(c) Private.** Two seats a quarter at ~14–17 h each (LEDGER B) come to ~2.2–2.6 h/week. The week gives them a single 1.0 h line, labelled "Private seats (0–2) or alumni reviews".
- **(d) The Hold.** About 65 members get "periodic review, re-captures" (BUSINESS §5), from that same 1.0 h line. At a 10-minute quarterly review each (*rival estimate*), that is ~0.8 h/week.

In total, the $50k week runs ~24–29 h, not 19.5. The $25k configuration (~32 concurrent) runs ~23–29 h against the Growing week, which has no Private or Hold line at all.

The selling line closes only if a large share of enrollments take almost no operator time. LEDGER C has no conversion row for that path (call-optional checkout, the Async Arc). Its only proxy is an all-industry landing-page median.

**Why it costs.** Seat caps are set "from measured care minutes" (LEDGER H). If the plan says 40 concurrent clients fit in 20 hours, the operator will sell 40 seats. Then one of two things happens:
- He misses turnarounds, which triggers the service guarantee's credits and refunds.
- He cuts the protected content minimum, which starts the feast-and-famine cycle the playbook exists to prevent (Module 12's opening frame).

Every Scaling decision hangs on the Capacity Ceiling (~25–45 concurrent; Module 04). Milestones add roughly 4–6 minutes per client-week. Holding hours fixed, that cuts capacity by about a quarter to two-fifths (*rival estimate*).

**Fix.**
1. Add three priced lines to every LEDGER A4 week: "milestones (onboarding, week-6 read, week-12 re-assessment)", "Private", and "Hold reviews". Re-derive the Capacity Ceiling and both configurations from them.
2. Add a PL row to LEDGER C for "warm offer-page visitor → enrollment (call-optional)", plus a row for "share of enrollments with no live call" by stage. Module 20 owns both, and the share becomes a Growing metric in Module 13.
3. In Module 07's instrument, template the week-6 read and fold the renewal conversation into the week-12 re-assessment. Module 07's own worked example (a calendar with minutes for a cohort of ten) will expose the gap anyway.
4. Before assuming more capacity, recover hours through RIV-8 (Private at hourly parity, or async) and RIV-9 (a lighter Round Two).

### RIV-3 · major · The Door Switch as written would cut Growing enrollments; the waypoint model overflows instead

**Location.**
- BUSINESS.md §4: "Door Switch (fit conversation → paid assessment)"; the Scaling row lists only the paid assessment.
- LEDGER.md C: eligible lead → held fit conversation 10–20%; eligible lead → paid assessment 2–7%.
- models/model3.py lines 110–116; models/mid.py lines 5–11.
- Module 06 §3 (briefs/part-1-2.md); THESES B5.

**Issue.** The narrative describes a switch, but the model runs cap-and-overflow.
- **What the model does.** model3.py and mid.py keep free or cheap fit conversations running at the call cap (26–35 a month) and add paid assessments for the remaining leads. That is what produces LEDGER A3's Band C–D waypoints ("20–35 conv (+0–28 paid assessments)").
- **What the brief teaches.** Module 06 presents "the Door Switch and its signals" as a move from one door to the other. The switch fires on call counts (more than 6–8 a week), a level reached at ~130–290 eligible leads a month, which is Bands B–C.
- **What that costs, taken literally.** It replaces a step 10–20% of leads take with one only 2–7% take:
  - At 150 eligible leads, ~24 conversations (~7.8 enrollments at 32.5%) become ~7.5 assessments (~2.6 enrollments plus ~$1k in fees).
  - In mid.py's Band C maturity case, overflow yields ~9.5 enrollments; replacement yields ~5.7.
- **The economic test got lost.** THESES B5 said the choice should be judged on "profit per operator hour per 100 eligible leads". The rule that reached BUSINESS and the LEDGER is a call count.

**Why it costs.** An operator who follows Module 06 literally could lose half to two-thirds of his monthly enrollments in the Growing stage, when conversion is the binding constraint.

**Fix.**
- **Restate the rule as cap and overflow in Module 06.** Fit conversations stay open up to the weekly cap, reserved by Readiness Tags (Module 26) for uncertain or high-intent buyers. Overflow and low-intent leads go to the paid Decision Assessment or the async path (Module 20).
- **Swap the trigger.** Replace the call count with THESES B5's economic test, measured over ≥30 events per door setting (Small Numbers Lie, Module 13).
- **Update BUSINESS §4.** The Scaling row should show both routes.

### RIV-4 · major · The founding seat cap sets month 3, and the founding 1:1 is underpriced against the playbook's own rules

**Location.**
- BUSINESS.md §5: founding 1:1 at ~$1.2–1.5k with 4–6 seats; the founding group switches on "at ≥4 founding clients (months 3–6)".
- BUSINESS.md §11: "Month 3 looks the same in every band because the Founding Sprint decides it."
- LEDGER.md A3; A4 (founding 1:1 at ~35 min/client-week, calls included); B (founding prices, and the coaching hourly rate as an internal sanity check).
- THESES B7; models/model3.py line 99 (the m3 seat cap is 2–3).
- Module 10 §4 and Module 05 §4.

**Issue.**
- **The cap, not reach, sets the good case.** In every band's good case, month-3 enrollments are set by model3.py's founding seat cap, not by reach or conversations. Uncapped, the good cases produce ~5.6 (Band A), 6.3 (B), 7.0 (C) and 7.7 (D) enrollments in month 3. The cap holds all four at 3. "The same in every band" is partly an artifact of this constant (and of the constant in RIV-5).
- **The overflow is scheduled too late.** The founding group is the obvious overflow. Its own trigger (≥4 founding clients) can fire by month 2 in the good case, but the schedule holds it until months 3–6.
- **The founding 1:1 is priced low.**
  - It runs ~35 min/client-week for 8–12 weeks (~4.7–7 h of delivery) at $1.2–1.5k. That is ~$170–320 per delivery hour, before counting sales time. It straddles the LEDGER's own coaching-market sanity rate (~$230–300).
  - It also sits below the opening-band group ($1.5–2.2k). So the public price history shows one-to-one cheaper than the group, which THESES B7 forbids.

**Why it costs.**
- **Month-3 cash.** In good cases, ~2.6–4.7 buyers a month are turned away or deferred. At the model's $1.5k, that's ~$3.9–7k of month-3 cash, when the whole month-3 cash waypoint is $1.3–4.5k.
- **A slower raise.** Fewer founding clients means fewer graduates toward the Raise Gate's proof milestone (≥10 graduates), which pushes the first raise back by a cycle.
- **A price history rivals can use.** The 1:1 price will be turned against the premium lane ("his 1:1 was $1.2k last spring").

**Fix.**
1. **Let the trigger govern.** Open the founding group, with a fixed start date, as soon as the founding 1:1 seats fill or three buyers are waiting. Sell it through the standing door, as HOUSE_STANDARD already says. Keep 1:1-depth review for the first three or four as the R&D Harvest.
2. **Restore THESES B7.** Price founding 1:1 at or above the top of the opening band (~$2.2k+) and state the access premium. Alternatively, sell every founding client into the founding group from day one and deliver 1:1-level review while fewer than four are enrolled.
3. **Update the model.** Change the seat cap in model3.py and the waypoints in LEDGER A3, so month 3 differs by band in the good case.

### RIV-5 · major · In the weak case, month 3 rests on an unlabeled constant, and the Month-3 Gate can't see the likeliest failure

**Location.**
- models/model3.py line 94: `extra = {3: (6, 12), ...}  # warm network / replies / referrals`.
- LEDGER.md A3 (month-3 conversations), C (the Month-3 gate) and H (Founding Sprint targets).
- Module 10 §2 and §6, and its action step "list 50 disclosed warm contacts".
- THESES §7 (verification debt: category demand); Module 04's line "Research for 3.1: None new".

**Issue.**
- **An unlabeled constant does most of the work.** model3.py adds 6–12 "warm network / replies / referrals" conversations a month at month 3. The constant has no LEDGER row, no status tag and no stated rationale. In Bands A–B it supplies 67–83% of month-3 conversations:
  - Band A: 6 of 7.2 (conservative), 12 of 16 (good).
  - Band B: 6 of 7.8 (conservative), 12 of 18 (good).
- **The warm network is this buyer's weakest source.** The playbook itself makes privacy part of the product: discreet sender names, pseudonymous cohorts, coach-only photos (HOUSE_STANDARD house rules). It does that because young men hide this pursuit from people who know them.
- **The gate can't see a volume failure.** The Month-3 Gate ("fewer than 3 clients from 25+ held conversations") tests conversion only. An operator with 12 held conversations by week 12, the more likely failure, triggers nothing.
- **The demand check is unscheduled.** THESES §7 lists "category demand after the category's authority collapse … check before committing reach assumptions" as verification debt. Module 04's research line says "None new", so no module pays that debt before the reach bands are taught.

**Why it costs.** If the warm-network yield is half the constant, month-3 conversations in Bands A–B fall by roughly a third to two-fifths. The operator then spends months 1–3 fixing an offer he believes is failing, when the real problem is volume.

**Fix.**
1. Promote the constant to a LEDGER H row (PL, a range, "replace after ~30 events"), split by source.
2. Give Module 10 a source-yield ladder with a week-3 check. If warm network plus replies produce fewer than 2 held conversations a week, shift ~2 h/week from long-form to short-form batches and permission-first public replies. Also open a small adult reach buy pointed at the Honest Answer and the founding page (RIV-12).
3. Add a volume leg to the Month-3 Gate. Fewer than ~15 held conversations by week 12 is a reach problem, fixed through sources, not through the offer.
4. Assign THESES §7's demand check to Module 04's Step 3.1 research.

### RIV-6 · major · The week-6 non-response clause pays on a read the playbook says is too early to mean anything

**Location.**
- LEDGER.md B: the non-response clause is "Pre-agreed week-6 markers; cash partial refund ~25–50% on exit", and what moves it is "Marker design". LEDGER.md D: median habit automaticity is ~2 months.
- BUSINESS.md §7 and §9.
- FRAMEWORKS The Honest Exit: "When the markers say the lever doesn't move".
- Module 07 §4, Module 08 §5, Module 11 §1 ("outcomes appear in months 4–9"), and Module 21 §4–5.

**Issue.**
- **The timing contradicts the playbook's own argument.** The clause refunds cash at week 6 when pre-agreed markers say "the lever doesn't move for this person" (Stall Verdict 3). But Module 11 argues that visible outcomes appear in months 4–9, and LEDGER D puts median habit automaticity at ~2 months.
- **The markers are undefined, and three modules share them.** No file defines them. Module 07 writes them into the Expectation Document, Module 08 sets the clause, and Module 21 applies it.
- **Either definition fails.**
  - If the markers are appearance-based, most clients "fail" at week 6 by design.
  - If they're behavior-based, anyone who did the work passes, and the clause never pays. It becomes a hygiene signal dressed as a costly one. The Burned Struggler (the verification-first route) will spot it, and it fails the Collectability Test.

**Why it costs.** One outcome is refund leakage after six weeks of care minutes (~25–50% of the price, pure margin), plus disputes against LEDGER B's target of ≤1 per rolling 90 days. The other is a guarantee that persuades no one. Either way it distorts the non-responder share the playbook commits to publish at ≥30 graduates.

**Fix.**
- **One owner.** Module 08 defines marker classes in the LEDGER.
- **Week 6 uses process markers.** These are markers the operator can verify: logging completion, capture quality met, the First-14 win achieved, the targeted blocks adopted. A failed process read triggers adjust, hold or refer, not cash. Keep a pro-rata exit at week 6 for clients who did the work and ask to stop.
- **The cash clause moves to week 12.** At the week-12 re-assessment, a matched capture and a full record can support Stall Verdict 3.

This keeps the Layered Guarantee both costly and collectable.

### RIV-7 · minor · Several planning numbers are biased upward by denominator slips

**Location.**
- LEDGER.md B: Round Two at "20–40% uptake among clients with measured momentum".
- LEDGER.md A3 note: view equivalents assume 50–70% of leads are eligible.
- LEDGER.md C (eligible share ~30–70%) and D (churn 4–8%).
- BUSINESS.md §6: Round Two at "~30% of graduates"; the Hold at ~45 and ~65 members.
- models/model3.py lines 5 and 129–130; Module 13 (Denominator Discipline).

**Issue.**
- **(a) Round Two's base.** Uptake is defined per client with measured momentum, but BUSINESS §6 and both models apply it to all enrollments, in care months and in LTV. If half to two-thirds of graduates show measured momentum (*rival estimate*), true uptake is ~10–27% of enrollments.
- **(b) The eligible share.** LEDGER A3's view equivalents assume 50–70% of leads are eligible, while LEDGER C's own range is 30–70%. At the low end, the views needed are understated by up to ~1.7×, and that happens in the early months, when the audience skews young.
- **(c) The Hold's ramp.** The Hold's ~45 members is a steady state. At ~6%/month churn the fill time constant is ~17 months. About 12 months after graduations reach ~9 a month, it holds about half that. The "year ~2" $25k configuration counts it as full.

**Why it costs.** Each slip is small ($1–2k a month, or a misread band). But they all point the same way, and the playbook sells Denominator Discipline (Module 13) as a core rule.

**Fix.**
- Restate Round Two per graduate in LEDGER B and in both models.
- Use 30–70% in A3's view equivalents.
- In BUSINESS §6, show the Hold's ramp (members at 6, 12 and 24 months after first graduation) instead of a steady state.

### RIV-8 · major · The premium lane is sequenced backwards

**Location.**
- BUSINESS.md §5: Private switches on "Month 9+ when measured care minutes leave seats spare", and the Priority Review "With Private". §6: the $50k configuration carries ~2 Private seats a quarter at capacity.
- LEDGER.md B (Private at ~$4–7k, with ~12–15 delivery hours plus ~2 h of sales per seat) and H (Private activation).
- THESES B17: Private is "priced to hourly parity".
- HOUSE_STANDARD "Present the price": "Show the real tiers, premium first … Every tier is real and bought by someone."
- FRAMEWORKS Premium First, Price Once (Module 19); the MAP early-stage pointer (which sends the operator to Module 19); Module 11 §5.

**Issue.** Private is missing when it's cheap to deliver and present when it's expensive.

- **(a) Early and Growing: absent while seats are spare.** Care minutes don't bind in these stages (LEDGER A2), so seats are spare by definition. Yet Private and the Priority Review don't switch on until month 9 or later. For nine months there is no real premium tier. Premium First, Price Once is the Module 19 technique the early-stage pointer sends the operator to in month 1, and it can't be used without a decoy, which the House Standard bans.
- **(b) Scaling: present while care binds, and far below parity.**
  - At $4–7k for ~14–17 operator hours, Private earns ~$235–500 an hour.
  - The cohort earns ~$1,125 (proof price) to ~$1,667 (above band) per delivery hour at 12 min/client-week (the model3.py method). Even with milestone minutes added it earns ~$800–1,200.
  - That is nowhere near the "hourly parity" THESES B17 requires.
  - In the $50k configuration, where care binds, two seats a quarter (~28–34 h) displace roughly 1.5–2.9 cohort enrollments a month (~$6–12k of revenue at $4k) to earn ~$4k.
- **(c) The same deliverable at two prices.** The Priority Review ($350–600: async review, written plan, recorded walkthrough) and the async-first Decision Assessment ($150–250: recorded review and written plan) are nearly the same product, maintained as two rungs.

**Why it costs.**
- **Early cash.** One Private seat at $4–7k exceeds an entire month-3 cash waypoint ($1.3–4.5k).
- **Early calls.** Every early call goes without a premium anchor.
- **Scaling.** Private leaks several thousand a month.

**Fix.**
1. **One product, two speeds, from month 0.** Make the Priority Review the premium tier of the Decision Assessment: the same written-plan template, with a faster turnaround and a recorded walkthrough. Sell it from month 0 to Optimizers. It doubles as R&D for the written plan the Door Switch will need later.
2. **Founding Private seats while hours are spare.** Allow one or two founding Private seats from month 0 while care minutes are spare. Price them in the Private band, with fixed deliverables. This gives Module 19 a real premium-first tier.
3. **A parity trigger at Scaling.** Activate a Private seat only when its price per operator hour clears the cohort's revenue per care-hour at the current price, and make that a Scaling Trigger in Module 13. In practice this means an async-heavy Private with fewer live minutes, or a higher price. Take Private out of the $50k configuration until it passes.

### RIV-9 · major · Round Two spends full care minutes at a third of the flagship's price

**Location.**
- LEDGER.md A4: "~30% Round Two ≈ 3.6 months of care per enrollment".
- LEDGER.md B: Round Two at ~$0.8–1.5k; above band at ~$3.5–4.5k.
- BUSINESS.md §6: at $50k, Round Two is ~$1.3k against a Program at ~$4k; the "Async-only Program" is listed as "a valid variant".
- THESES B2 ("extended low-intensity contact protects maintenance") and B15.
- models/model3.py line 5; Module 11 §2.

**Issue.** The capacity math counts Round Two as 12 more weeks of the same weekly review. In the $50k configuration that is ~9 of ~40 concurrent seats. Each earns ~$1.3k per 12 weeks against ~$4k for a new enrollment: about a third of the flagship's revenue per care-minute (43% at proof prices). The playbook's own delivery evidence (THESES B2) says maintenance needs extended low-intensity contact, not the same intensity. BUSINESS §6 already lists an async-only Program as a valid variant.

**Why it costs.** This bites only when care binds, at Scaling, which is exactly when the $50k is supposed to happen. Running Round Two at half the minutes frees ~4.6 concurrent seats. That is either ~1.3 more enrollments a month (~$5k/month at $4k) or ~2–3 hours a week back against RIV-2's overrun.

**Fix.**
- **Module 11 makes Round Two a maintenance format.** That means biweekly async review, an optional group call, and re-captures at weeks 6 and 12. Price it per care-minute at parity with the flagship, or keep the price and halve the minutes.
- **LEDGER A4's care-months formula** uses Round Two's actual minutes.
- **Keep full intensity for one case only.** It fits a client whose week-12 verdict is "misdirected, now corrected", and it's priced as a full Program.

### RIV-10 · major · The back end starts late and small

**Location.**
- BUSINESS.md §5: founding 1:1 runs "Months 0–4, then sunsets"; Round Two switches on at "First graduations (months ~6–9)"; the Hold at "First graduation".
- Module 11's stage notes ("Early: design Round Two during the founding phase; no community yet") and §3 (the opt-in default vs a disclosed Hold phase).
- THESES P20; LEDGER.md D (churn) and E (defaults, d≈0.6–0.7); BUSINESS.md §6 (the Hold at ~45 members).

**Issue.** There are three gaps.
- **(a) Founding graduates graduate into nothing.** The founding 1:1 clients graduate around months 2–4. But Round Two switches on at months 6–9, and Module 11's Early note says "no community yet". These are the clients with the richest data and the strongest working alliance, so they're the best renewal candidates.
- **(b) The first room is nearly empty.** The Hold opens "at first graduation" as an alumni room: a paid community of one to four people. A room that small is empty, and an empty paid room churns (*rival judgment*).
- **(c) The strongest default is parked as an option.** Continuity defaults to opt-in at the review. A disclosed Hold phase agreed at purchase, with a reminder before the first charge and one-click exit, is already allowed by the House Standard and THESES P20. LEDGER E rates defaults as the most robust lever in its table.

**Why it costs.**
- **Founding Round Two cash.** Founding Round Two alone is ~$0.6–3.6k in months 3–4 (4–6 graduates × 20–40% × $0.8–1.5k), roughly one month-3 cash waypoint.
- **Learning.** It also means learning about the renewal offer three to five months sooner.
- **Hold economics.** A dead early room depresses the Hold's take-up and raises its churn, and both configurations count the Hold at steady state.

**Fix.**
1. Offer founding graduates a Round Two seat inside the founding group. As veterans, they also seed the group with Transition stories (Module 16).
2. Until there are ~30+ alumni, run the Hold as a measurement subscription with no room: a quarterly re-capture, a written review, and the Canon Lane. Open the room at that point (Community Options, Module 11).
3. Once the Hold has a track record, test the disclosed Hold phase at purchase as the default for Program buyers, using the disclosure, reminder and exit terms already specified. Watch the dispute count (LEDGER B).

### RIV-11 · major · Before Scaling, real dates have no force, and price moves too slowly to supply them

**Location.**
- BUSINESS.md §8: starts every 6–8 weeks; seat caps from care minutes.
- LEDGER.md C (the Decision date RULE: "within ~2–4 weeks"), B (the Raise gate), H (Small numbers; seat caps), A2 (binding constraints) and D (one combined group call until ~12–15 clients).
- THESES B22; Module 09 §3–5; Module 08 §3.
- critique/operator.md OPE-21 proposed a standing group with monthly entry; it wasn't adopted.

**Issue.** Before Scaling, each of the three real decision points is weak:
- **Seat caps.** They come from care minutes, which don't bind until Scaling. So "5 of 8 seats taken" rarely forces a decision. A live under-filled count ("2 of 12") is also negative social proof and free intelligence for a rival.
- **Credit windows.** They only exist once a fee is charged, and the Early fit conversation is "free or ~$25–50".
- **Price steps.**
  - They wait on a Raise Gate that needs ≥10 graduates plus a conversion or utilization signal "held two cycles", then 30 days' notice. The first check sits in months 6–9 (Module 28 §4).
  - The conversion signals rest on about one cycle's worth of events, which is borderline against the playbook's own ~30-event rule.
  - The utilization leg (≥85–90% of seats for two starts) can't fire while caps are set from slack care minutes.

So the RULE that every assessed buyer meets a real decision point within ~2–4 weeks can't be met in Growing. A buyer assessed the week after a start faces a 6–8-week wait and nothing else.

**Why it costs.**
- **Deferral wins.** The enemy Module 09 names wins by default.
- **Lumpy cash.** Cash arrives unevenly across 6–8-week starts.
- **A late raise.** The proof band arrives around month 9–14, depending on whether two noisy cycles line up.
- **Forgone profit.** At Growing volume, each month at the opening band instead of the proof band forgoes ~$850 × 5–8 enrollments, which is ~$4–7k a month and almost all profit (LEDGER A, price leverage).

**Fix.**
1. **Monthly entry.** From the founding group onward, run a standing group with monthly entry. The group call stays combined until ~12–15 clients anyway (LEDGER D), so monthly starts add no call hours, and every buyer gets a real start within four weeks.
2. **An Early credit window.** Charge the small credited fee on Early fit conversations (~$25–50, credited for 14 days). That creates a credit window from month 0.
3. **A price-step calendar.** Replace the statistical Raise Gate with small announced steps (for example, every second start) that always happen while starts fill and close rates stay inside the LEDGER range. The proof milestone gates only the jump to the floor of the proof band.
4. **Fill history after the fact.** Publish it after each start closes, not as a live under-filled count.

All four stay inside the Launch Line (Module 09) and hard line 3.

### RIV-12 · major · The one reach lever the planned-for bands need is sequenced last and switched off in Early

**Location.**
- LEDGER.md A3: Band A "needs one reach lever (adult paid reach, a breakout piece, referrals)"; "Plan on A–B".
- LEDGER.md D (referrals: "plan acquisition without referrals") and F (an optional adult-only reach budget in months 3–6, ~$300–1,000; ~$25–30 per paid lead).
- Module 27's stage notes ("Early: … no ads"; "Growing: … the optional small reach budget") and §5.
- Module 28 §3 (the optional reach budget in months 3–6); Module 04 §6 (revenue per eligible lead, used only as a pricing metric); MAP Module 13 (Scaling Triggers).

**Issue.**
- **Paid is the only plannable lever for Band A.** The LEDGER names three reach levers for Band A: a breakout (not plannable), referrals (which the playbook forbids planning on), and paid adult reach.
- **It is gated and switched off early.** Paid sits in the last and least-developed module, behind Ad Gates that require organic proof and an offer that already converts without ads. Module 27's own stage notes say "Early: no ads", which contradicts LEDGER F and Module 28. Both of those put the small budget in months 3–6, and for Bands A–B that is still the Early stage.
- **No module prices a lead.** Module 04 owns revenue per eligible lead only "as the pricing metric", so nobody computes what a lead is worth buying.

**Why it costs.** The numbers make this a live decision by month 3–4.
- **What a lead is worth.** At opening prices, revenue per eligible lead is ~$26–210: LTV of $1.7–3.0k × lead-to-client 1.5–7% (LEDGER C, D).
- **What a lead costs.** Paid reach costs ~$36–100 per eligible lead: $25–30 per raw lead at a 30–70% eligible share (LEDGER F).
- **What the budget buys.** A $300–1,000 budget buys ~10–40 raw leads. Band A has only 10–20 eligible leads a month at month 3 and 25–50 at month 9.

**Fix.**
- **Module 04:** own "maximum affordable cost per eligible lead" alongside revenue per eligible lead.
- **Module 13:** make the paid adult reach test band-dependent in the trigger table.
  - Band A: the default at months 3–4, once the door and destinations pass the Destination Rule.
  - Bands C–D: optional.
- **Module 27:** match its Early note to LEDGER F.

Paid stays light, as the spec requires: a decision rule and a holdout, no platform tutorial.

### RIV-13 · major · The moat is copyable by design, and the one asset a rival can't copy starts its clock too late

**Location.**
- FRAMEWORKS The Moat Test (Module 13, "reused"). It shares ~600 words with the road to $50k (Module 13 §6).
- BUSINESS.md §3: Name | Brand, where "the brand owns the method, the capture standard, and the client library".
- BUSINESS.md §5: the Self-Serve System is "rebuilt from the stall taxonomy: capture standard, logs, decision framework, walkthroughs". The Free/Paid Line says "give away the why and the decision framework".
- THESES E11: the Verify Page includes "methodology".
- Modules 15 and 16 stage notes (pre-committed publication is a Scaling item) and Module 16 §6 (prebunking teaches the tells).
- LEDGER.md D: the non-responder share is published once there are ≥30 graduates.

**Issue.** As a rival, I'd copy the position in a month:
- **The stance and the standard are public.** The honest answer is a stance anyone can take. The capture standard is taught in public, through Module 16's Buying Test and the Verify Page's methodology.
- **The terms are public too.** The Layered Guarantee, the calendar and the prices are published by design (Sell in the Open).
- **The test stops being exclusive.** "The buying test only you pass" becomes a test we both pass once I adopt the standard it publishes.
- **The R&D is for sale.** The Self-Serve System ($97–297) is built from the stall taxonomy and sells its codified form. That's the operator's R&D at the price of a dinner. Meanwhile its "decision framework" is, by the Free/Paid Line, already free.

What I can't copy is a dated public record: outcome ranges with denominators published on a pre-committed schedule, claim rates, and fit-decline counts. It can't be back-dated. Nor can I copy the consented client library or the search equity in the brand's name. The architecture starts that clock at Scaling (Modules 15 and 16 stage notes; the non-responder share at ≥30 graduates) and gives the Moat Test ~300 words at the end of Module 13.

**Why it costs.** As copycats adopt the honest stance, the operator's differentiation decays into price competition. That happens in years 2–3, exactly when he needs above-band pricing.

**Fix.**
1. Move the Moat Test to Module 03 (Position) or to the $50k module proposed in RIV-19, and define the moat operationally: "a public record that can't be back-dated".
2. In months 1–3, publish the pre-commitment: what will be published, at what sample size, on what schedule, whatever it shows. From the founding group onward, keep a dated log of process metrics: check-in completion, turnaround kept, claim rate, and fit declines in aggregate. It costs nothing now and can't be copied later.
3. Keep the stall taxonomy's verdict logic out of the Self-Serve System. Sell the tools (logs, the capture standard, self-review prompts) and the optional single async review, not the decision rules.

### RIV-14 · major · The Early week is allocated against its own binding constraint

**Location.**
- LEDGER.md A4, Early column: long-form 5.0 h; short-form 2.0 h for 4–7 native pieces; weekly email 1.0; conversations 3.5 (~4 × 0.9 h).
- LEDGER.md A2 (the Early binding constraint), B (fit conversation 20–30 min) and F (the Early cadence RULE, which includes a weekly email).
- THESES E5: short-form is "the main reach source" in months 0–4.
- Module 24 §1, Module 26's stage notes ("Early: one result email plus a short welcome"), Module 10 §3, and Module 19 §1–6.
- FRAMEWORKS Close by Contract.

**Issue.** Module 01's rule is to decide for the constraint that binds this month. In months 0–3 that means reach, then conversations. The Early week spends against that rule in three places:

- **Long-form gets the biggest line.** The largest line in the week (5 h, a quarter of it) goes to one long-form video a week on a channel with no subscribers, the slowest-compounding source. The designated early reach engine gets 2 h for 4–7 native pieces, about 17–30 minutes each from script to posting.
- **The weekly email serves a tiny list.** The 1-hour email goes to perhaps a few dozen adults (Bands A–B bring 10–30 eligible leads a month). Module 26's own Early note drops the weekly broadcast, while LEDGER A4 and F keep it protected.
- **The call length can't hold the call.** The fit conversation is budgeted at 20–30 minutes. It has to carry the Dual-Purpose Conversation's research questions (Module 10) and Close by Contract's ten steps, with up to two probes per objection (Module 19). A realistic 40–60-minute call makes each conversation ~1.25–1.5 h all-in. Three to six a week is ~3.8–9 h against 3.5 budgeted.

**Why it costs.** The Founding Sprint is starved of reach in the months that decide it, and the conversation line quietly overruns. The overrun comes out of building, the first cut in the De-Scoping Order, which delays door v0.

**Fix.** For months 0–3 (Module 12's Design Week, sequenced in 28):
- **Long-form:** every other week after the Honest Answer, about 2.5 h/week. Return to one a week at month 3–4, or once the first founding clients are in.
- **Short-form:** 3–4 h/week.
- **Email:** keep the result email and welcome flow. Turn the weekly broadcast off until the list reaches a threshold (~300 eligible adults, *rival estimate*).
- **The freed ~1.5–2 h:** goes to replies and conversations.
- **The call:** budget the dual-purpose call at 45 minutes, or move the research and excavation prompts into the booking form (Module 06) so the call carries the recommendation and the close.

### RIV-15 · major · The free 7-day log stands between the lead and the scarcest input

**Location.**
- BUSINESS.md §4: the door diagram places "Optional: free 7-day log + one baseline capture" before the Early fit conversation.
- Module 17's stage notes ("Early: the free log as the door's first step"), §4, and action steps ("build your free log and its day-8 follow-up").
- FRAMEWORKS Let Him Succeed Before He Pays ("after the age fork").
- LEDGER.md C (lead-response speed: "contact within the hour ≫ later"; show rate ~80% next day → ~60% at 14 days), D (unguided completion is very low) and H (personal reply within hours).

**Issue.** In the Early stage, the door puts a week of unguided homework between a warm adult lead and the first conversation. Every speed-to-lead number in the LEDGER points the other way: contact within the hour, book close to now, reply within hours. LEDGER D's evidence on unguided completion says a large share of starters won't finish a solo log. The log is a filter: valuable when calls bind (Scaling), costly when conversations bind (Early). The Constraint Sequence (Module 01) says to choose the setting for the binding constraint, and here the setting is backwards.

**Why it costs.** Held conversations are the Early north star. A gate that loses even a third of warm leads (*rival estimate*) takes a third off conversations and clients in months 1–3.

**Fix.** Flip the placement by stage. Module 06 owns the placement and Module 17 owns the mechanism.
- **Early and Growing:** book first, log while waiting. The log becomes call prep and still produces the Back-Dated Baseline.
- **Scaling:** the log and the baseline capture become the pre-assessment step and the async arc's first commitment.

### RIV-16 · major · The leverage layer has no build hours

**Location.**
- LEDGER.md A4, the "Building …" line: 1.5 h in Early, 0.5 h at month 6, and none in Growing or Scaling.
- LEDGER.md H: the De-Scoping Order cuts building first.
- Module 20's stage notes ("Growing: build async from arcs proven live") and extras; Module 07 §2 (the templating path, from ~20 to ~8 minutes); Module 05 §5 (the Self-Serve System).
- Module 11 extras (the Private deliverables card, Hold terms, room rules); Module 26 (Growing: tags and sales sequences); Module 27 (Growing: claims library, brand long-form).

**Issue.** Everything that lets the $25k and $50k configurations fit into 20 hours has to be built in Growing:
- templated review;
- the async arc (result pages by state, a branched walkthrough, a five-email sequence, and checkout with the fit check);
- the Decision Assessment template;
- the Round Two and Hold terms;
- the Private deliverables;
- the Self-Serve System.

Growing's design week has no building line, and the De-Scoping Order cuts building first.

**Why it costs.** The operator stays call-bound and review-heavy at 10+ minutes a client-week. RIV-2's overrun becomes permanent, and the $50k levers never get built.

**Fix.**
- **Module 12:** keep a protected ~1–1.5 h/week build line through Growing, paid for by the call hours the async arc will save. Or run a build week each quarter, with content at its minimum and the build block raised.
- **A build queue,** ordered by hours saved per hour invested:
  1. templated review;
  2. the Decision Assessment template;
  3. the async arc;
  4. the Round Two and Hold terms;
  5. the Private deliverables;
  6. the Self-Serve System.
- **Module 28:** the Leverage phase (months 6–9) sequences the first two.

### RIV-17 · minor · Too many named tools and checks for one operator's week

**Location.**
- FRAMEWORKS.md Count: 33 ★, 139 ◆ and 2 ○, 174 entries in all.
- HOUSE_STANDARD.md "The five checks": "Run these on every asset, script, and offer".
- Per-asset rules owned by Modules 03, 16, 18, 23, 24 and 27.
- The briefs' default budget: a Standard Check of ~200 words in each of 28 modules.

**Issue.**
- **Checks per asset.** A solo operator shipping one long-form, 4–7 shorts and an email a week (LEDGER F) faces about a dozen named checks per asset:
  - the five House Standard checks and the Launch Line test;
  - the Neither-Grifter-nor-Doctor Test;
  - the Click Contract, One Ask per Asset, the Stake-to-Step Ratio and the Belief Sentence;
  - the Clip Context Check and the One-Defensible-Point Rule;
  - the Age-Up Dial and the Two-Job Scorecard;
  - the Destination Rule, the Proof Portability Gradient and the Context Stack.
- **Overlapping names.** 139 named tools turn a playbook into a vocabulary test, and several ◆ entries overlap: the Click Contract is nearly the Payoff Test, the One-Defensible-Point Rule nearly the Clip Context Check, and the Canon Lane sits inside the Canon.
- **Repeated Standard Checks.** 28 Standard Check blocks (~5,600 words) restate the Intro.

**Why it costs.** Each asset takes longer, and adoption suffers: tools that aren't used weekly don't get used at all.

**Fix.**
- **One pre-publish card.** Module 18 owns a card of at most ten yes/no lines, and the other modules feed it.
- **Demote the rest.** Turn ◆ entries that restate a rule, or are used less than monthly, into prose or glossary terms. Candidates: Belief Sentence, Click Contract, One-Defensible-Point Rule, Half-Life Budgeting, Production Floor, One-Way Broadcast, Landmark Pinning, Threshold Continuity, Canon Lane, Identity-Safe Shareables, Integrity Levels, and Presence over Pedigree. Aim for ~80–100 named items.
- **Shorter Standard Checks.** Cut each Standard Check block to the hard lines the module actually touches, and give the words back to scripts (RIV-18).

### RIV-18 · major · The money modules can't hold their scripts, and Modules 19 and 28 are overloaded

**Location.**
- briefs/part-1-2.md default budget: extras ~650 words, worked example ~700.
- DECISIONS D7 and the briefs/part-5.md header ("scripts and swipe copy as their main extras").
- Module 18 extras (five offer-piece scripts).
- Module 19: deep sections of 5,100 words, the largest; extras of a full call outline with verbatim lines, objection responses by link, recap and follow-up templates, and a call scorecard; a worked example of an annotated call plus two excerpts in ~700 words.
- Module 20 extras (result pages by state, a walkthrough outline, a five-email sequence, voice-note rules, DM lines) and Module 22 extras (renewal, referral and testimonial scripts; shareables).
- Module 28: "budget to be confirmed", with 5,900 deep words for the first 30 days week by week, nine months and four bands.
- Module 06 §6: the written plan, ~400 words.

**Issue.**
- **Scripts get under 10% of each module.** The pieces the operator will reuse every week get ~650 words per module: the call script, the objection responses, the offer-video script, the sales emails, the renewal script. A verbatim call outline alone runs longer than that, and five email scripts won't fit.
- **Module 19 is overloaded.** It carries:
  - the full close arc;
  - a seven-objection niche map, which also overlaps Module 14's objection → link map;
  - four state routes, stop rules, follow-up, and the skill loop.
- **Module 28 is over the band.** At ~5,900 deep words plus the default blocks (~2,450), it comes to ~8,350 words, over the 7,700 ceiling.
- **The most reused deliverable gets ~400 words.** That's the Decision Assessment's written plan in Module 06:
  - It is reused as the Priority Review, the week-12 re-assessment and the core of the Self-Serve System.
  - At $50k, ~21 async assessments a month depend on it.

**Why it costs.** The most-used swipe copy gets compressed into outlines. The operator then writes his own scripts under time pressure, and that's where claim and pressure errors happen.

**Fix (minimum, with no change in module count).**
- **Modules 18–22:** rebalance to deep sections of ~3,800–4,000 words, a worked example of ~1,000–1,200, and extras (scripts) of ~1,500–1,800.
- **Module 06:** raise the written plan to ~1,000 words with a full template, taking the words from §1 ("Why one owned door").
- **Module 28:** give the first 30 days its own ~1,500-word section, put the bands in one table with change rules, and move "After month 9" to the owner of the $50k path.

The structural option is in RIV-19.

### RIV-19 · major · Three modules risk padding, while the $50k path has no module

**Location.**
- MAP.md: the allocation and the Parts.
- Module 01: §5 "The Spine" (~900) and §6 "the standard as strategy" (~500) duplicate the Intro's "spine at a glance" and House Standard pages. Its guardrail reads "Don't teach door, pricing, or metrics detail".
- FRAMEWORKS: The Spine (01) and One Flagship, Two Buffers, One Floor (05) draw the same object twice.
- Module 09: all rules, under the guardrail "never teach launch mechanics, even as a contrast". The Launch Line is already stated in full in the House Standard.
- Module 25: its Early note says "Instagram as a router only if the editing budget allows; X optional". LEDGER H cuts X first, then native Instagram. LEDGER F puts X at ~21% of US adults, with ~0.03% median engagement.
- The $50k path is split across four modules: 04 ("what $25k and $50k require"), 08 (the above band), 11 (the Premium Lane) and 13 ("the $50k levers", ~600 words shared with the Moat Test).

**Issue.**
- **Module 01** can't teach anything in detail, and it repeats the Intro and Module 05.
- **Module 09** is thin unless it gets new substance.
- **Module 25** spends ~7,000 words on the two platforms the playbook tells the operator to cut first.
- **The $50k path has no home.** Meanwhile the hardest half of the profit target has four partial owners and ~600 dedicated words: the above-band price and buyer mix, the premium lane, Round Two at capacity, templated review, and the moat.

**Why it costs.** About 21,000 words are at risk of padding, and the decisions that settle $50k are scattered where no one reads them together.

**Fix.** Each change below keeps the 13 / 9 / 5 / 1 allocation.

| Track | Change | Count |
|---|---|---|
| Business | Fold 01's Spine and standard sections into the Intro, which already holds them. Merge the rest of 01 (End of Guessing, Five Scarcities, Constraint Sequence, Stage Map) with 04 into "The Whole Business and Its Equation". This is tight; the Reverse Funnel and the reach bands lead. Use the freed slot for a new last business module, "The Premium Lane and the Road to $50k", covering: Private and the Priority Review (from 11); above-band pricing and the buyer-mix shift (RIV-1, from 08 and 02); Round Two at capacity (RIV-9); templated review and async-assessment economics; the Moat Test (from 13). Module 11 then goes deeper on Round Two, the Hold, community and re-enrollment, and Module 13 on metrics and triggers. The founding premium tier (RIV-8) is taught in 10, with a pointer. | 13 |
| Business | Keep 09, but give it the substance it lacks: honest urgency when seats don't bind, meaning monthly entry, the credit window and the price-step calendar (RIV-11). | 13 |
| Persuasion | Merge 15 and 16 into "Trust and Evidence Without Credentials". Costly signals and proof formats are one system; both modules currently teach the pre-committed publication schedule. Split 19 into two modules. "The Sales Conversation" covers the contract, excavation, recommendation, price once, the close, follow-up and the skill loop. "Objections, Routes and Stops" covers the full niche objection map by link and by state (taking the objection → link map from 14), the Real-Objection Sort, the Pushback Signal, State Routing, and stop rules in practice. | 9 |
| Ecosystem | Re-scope 25 from "Instagram and X" to "Replies, DMs and Routes": getting public engagement to the door across platforms. It covers permission-first replies, the Keyword Route, DM templates by case, X replies captured to email, One-Way Broadcast and the Platform Count Rule. Instagram's content craft moves to 24. | 5 |

Update FRAMEWORKS owners to match.

### RIV-20 · major · The operator's month-1 job is spread across modules the pointer doesn't name

**Location.**
- MAP.md "Early-stage pointer (Intro, R1-40)": Modules 10, 6, 19, 24 and 28.
- Module 07's stage notes ("Early: founding 1:1 … building the instrument"); Module 08 §4–5 (plans, the guarantee); Module 21 §2 (the Commit Ritual, the First-14).
- Module 15's opening frame ("The first comment under your first video") and action steps; Module 03's action steps ("plan the Honest Answer as your first long-form"); Module 02's extras (the affordability question, verbatim).
- Module 12 §6 (the Risk Register) and LEDGER H (open the processor early).
- The lead → held conversation step, which is split across 06, 10, 12, 19, 20, 25 and 26.
- critique/operator.md OPE-18, which asked for a section-level pointer.

**Issue.** The first paying client arrives in weeks 2–6 (LEDGER H: 0–2 clients in month 1). He needs kit from seven modules the pointer leaves out:
- **Selling to him:** Module 08's guarantee and plan terms, and Module 02's affordability question.
- **Delivering to him:** Module 07's check-in form, capture standard v1 and Expectation Document, and Module 21's Commit Ritual and First-14.
- **His first skeptical comment:** Module 15's Qualifications Answer and face statement.
- **The first long-form:** Module 03's Honest Answer.
- **Day-one rules:** the processor and minors rules in Module 12.

None of 07, 08, 21, 15, 03, 02 or 12 is on the pointer. And the pointer names whole modules (~35,000 words), not sections.

Separately, the Early multiplier has no owner. Eligible lead → held conversation runs 10–20%, but only "with a personal reply within hours", and the pieces sit in seven places:
- reply speed in 10;
- booking disclosure in 06;
- reminders and no-shows in 12;
- follow-up in 19;
- DMs in 20 and 25;
- the result email in 26.

**Why it costs.** The operator either reads ~190,000 words before selling, or he sells and delivers with half the kit. The second shows up as refunds, disputes and a weak R&D Harvest.

**Fix.**
- **A section-level Early Fast Path.** One page in the Intro, roughly 15 lines of the form "module §section → action → week". The MAP already allows this as part of "how to use".
- **Give Module 06 "speed to lead".** It covers completion → personal reply → booked (within ~24–48 h, per the show-rate row) → reminded → held, with LEDGER C's response-speed and show-rate rows as its numbers.
- **Getting engagement to the door** goes to the re-scoped Module 25 (RIV-19).

---

## (a) My five highest-priority fixes

1. **Reconcile price with the buyer, and give the $50k path one owner (RIV-1, RIV-19).**
   - Extend the take-home table to $4.5k, and set a cash-ceiling threshold for each price band.
   - Reword the affordability question to include savings, with still no new credit.
   - Have the new "Premium Lane and the Road to $50k" module own the buyer-mix shift. It shifts the mix by state and age, never by income, and carries a trigger for when an above-band raise is allowed.
2. **Rebuild the hours model before any module teaches a seat cap (RIV-2, RIV-16).**
   - Add milestone, Private, Hold and build lines to LEDGER A4.
   - Add an async-enrollment row to LEDGER C.
   - Re-derive the Capacity Ceiling and both configurations. Today they assume ~20 h for weeks that cost ~23–29 h on the LEDGER's own unit costs.
3. **Spend care minutes where they earn (RIV-8, RIV-9).**
   - From month 0, sell the Priority Review as the Decision Assessment's premium tier, plus one or two founding Private seats while hours are spare. That gives Module 19 a real premium-first tier.
   - At Scaling, run Private only at hourly parity.
   - Make Round Two a lighter maintenance format priced per care-minute.
4. **Unthrottle months 0–4 (RIV-4, RIV-5, RIV-10, RIV-15).**
   - Open the founding group on overflow, and price founding 1:1 at or above the opening band.
   - Offer founding graduates a Round Two seat.
   - Book first and log while waiting.
   - Put the warm-network constant on the LEDGER, and give the Month-3 Gate a volume leg with a source-yield fallback.
5. **Give Early and Growing real dates and faster prices (RIV-11, RIV-3).**
   - Run monthly entry into a standing group, and charge a credited fit-conversation fee.
   - Replace the two-cycle statistical Raise Gate with a price-step calendar of small steps that always happen.
   - Restate the Door Switch as cap and overflow.

## (b) What's genuinely strong

- **The Constraint Sequence and its staged settings.** The door, the rungs, the north star and the cadence each change by stage. That's the right operating model; most rivals run the Scaling playbook in month 1.
- **Reach bands, including one where the channel never breaks out.** Paired with "month 3 is decided by conversations", this is honest planning that kills the "wait for virality" failure, even though month 3 needs the fixes above.
- **Judgment as the product.** Selling the decision, not the diagnosis, and a written plan worth its fee are commodity-resistant. The offer holds up against automated "face analysis" apps.
- **The capacity-to-price logic.** At the cap, profit grows through price and leverage, not hours. The thesis is right; only the numbers need re-deriving.
- **A real back end argued from the client's own record.** Round Two, the Hold and measured-peak asks capture money most rivals leave on the table.
- **A trust architecture built for a burned category.** The Outcome Map, the Verify Page, the Layered Guarantee, the Collectability Test and the buying test give a genuine first-mover edge. They also cut the platform, ad-policy and dispute risk that kills competitors in this niche.
- **The Protected Content Minimum and the De-Scoping Order.** Together they build a defense against feast and famine into the week.
- **Small Numbers Lie and fixed denominators.** They stop the classic early flail: three price changes on the evidence of four calls.

## (c) Verdict

Yes for $25k; not yet for $50k. The architecture is a sound operating system for a judgment business. The stage logic, the door, the flagship-plus-back-end shape and the trust architecture are what I'd copy if I were entering this niche.

As drafted, it reaches the $25k floor in year 2 in Bands B–C, with two conditions. Price has to reach the above band, which the default buyer can't pay under the playbook's own affordability rule. And the week has to absorb three to nine hours of work the LEDGER doesn't count.

The $50k configuration fails on three counts at once:
- the buyer's cash ceiling at ~$4k;
- a ~24–29-hour week on the LEDGER's own unit costs;
- Private and Round Two spending care minutes at a third or less of the flagship's yield, exactly when care binds.

None of the fixes needs a looser hard line or a broken spec. Re-derive the hours, give the $50k path one owner who plans the buyer-mix shift, move the premium lane to the months when hours are spare, lighten Round Two, and unthrottle the founding phase and the price steps.

With those changes, $25k becomes a realistic year-2 outcome in Band B (earlier in C). $50k becomes a credible year-2–3 outcome in Bands C–D, or in Band B with a working paid reach lever. Without them, the business plateaus near the LEDGER's own proof-price middle cases, from ~$10k in Band A to ~$21–27k in Bands B–D, and the operator works 25+ hours a week to hold it there.
