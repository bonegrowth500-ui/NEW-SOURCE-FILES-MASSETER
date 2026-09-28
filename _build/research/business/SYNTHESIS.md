# SYNTHESIS — Business & Offers track (B1 + B2 + targeted gap fills)

Track: Business & Offers · Compiled 27 Sep 2026 · Status: research input, not playbook copy. The playbook never cites. Every idea below must be rewritten as native, first-principles content.

**Method note.** Inputs:
- **Dossiers.** B1 and B2, read in full. P1, P2, E1 and E2 were cross-checked where they bear on business design.
- **Gap fills.** The session's web-search budget was exhausted and WebFetch was egress-blocked for every host except GitHub, so gaps were filled three ways:
  1. **A new re-analysis of two open trial databases** hosted on GitHub: the Metapsy depression-psychotherapy database (~480 RCTs, ~600 comparisons) and the Metapsy self-guided-intervention database (118 comparisons). These are the deepest trial literature on *how* behaviour-change help is delivered.
  2. **Primary or near-primary texts surfaced through GitHub**: card-network rule summaries quoting Visa and Mastercard; age-of-majority clauses in major consumer terms and in the IRS Direct File code; UK Consumer Contracts Regulations and DMCC commencement notes dated Aug–Sep 2026; BDD screener validation figures.
  3. **Well-established findings recalled from the literature**, marked "recalled — verify".

Tags: STRONG / MODERATE / WEAK / ANECDOTAL / CONTESTED / DERIVED (my arithmetic) / ESTIMATE.

---

## 0. Contradictions between B1 and B2, resolved

| # | B1 | B2 | Resolution | Basis |
|---|---|---|---|---|
| 1 | Delivery hours are the binding constraint | Sales calls are the binding constraint | Both are the same scarce input: the operator's **synchronous one-to-one minutes**. Sales minutes bind first and care minutes bind at scale (see T1). | DERIVED |
| 2 | Default front door is a paid assessment, which is itself a call | Most enrollments must come without a call | The paid assessment roughly halves operator hours per enrollment (1.5–3 h vs 2.7–8.3 h) and pays for itself. It saturates at ~30 a month, so it goes async-first, and warm buyers get a call-optional path (T5). | DERIVED from both dossiers' inputs |
| 3 | Never anchor on surgery | Alternatives set a $1.5–10k "serious-solution band" | Use it as a **market map, never as an anchor** (T8) | Anchoring evidence + hard line 2 |
| 4 | Sell a $150–250 assessment | Analysis is commoditized, so never sell the diagnosis | Sell the **decision** (judgment, plan, refer-outs), not an analysis (T5) | B2 price scan + hard line 2 |
| 5 | ~5% of instalments uncollected | 15–20% plan defaults without dunning | **Plan structure decides**: short plans inside the program with retries ≈3–8%; long plans that outlive delivery ≈15–20% (T9) | CFPB BNPL, Recurly, payment depreciation; DERIVED |
| 6 | 1.5% Visa ratio; one dispute can end you | 1.5% is the "excessive" line | Network programs need **≥1,500** (Visa) or **≥100** (Mastercard) disputes a month, which a solo coach never reaches. The real risk is the **processor's tolerance at small counts** (T10). | Rule summaries on GitHub quoting Visa and Mastercard (MODERATE) |
| 7 | All paid offers 18+ | 18+, and 20+ for high-ticket | 18 isn't the legal floor everywhere: **19 in Alabama and Nebraska, 21 in Mississippi and Puerto Rico**. Add a "legal adult where you live" attestation. B2's 20+ high-ticket default clears most of it. | Primary consumer-terms clauses (STRONG) |
| 8 | Delay DIY until 30–50 graduates | Students 18–21 need a digital tier | A **minimal Down-Path now** (a humane decline destination) and the **full DIY system later** (T13) | Standard + completion evidence |
| 9 | Private 1:1 at $3.5–6k, 6–10 seats | Premium $3–6k | The price band is right; the delivery design is wrong. Standalone 1:1 earns about half the cohort's per-hour yield, so build it as a **layer** (T4). | DERIVED |
| 10 | Community churn 5–10%/mo | 4–8% typical, 8–15% open and cheap, 2–3% curated | Consistent. Price and programming drive it; adopt B2's split | WEAK |
| 11 | LTV ~$2.1k | LTV $1.8–3.9k | The gap is just the price assumption; use $1.8–3.9k | DERIVED |

---

## 1. Thesis candidates (16)

**T1. The scarce input is synchronous operator minutes, and which minutes bind moves with stage.**
- *Reasoning:* content, async review and group calls scale sub-linearly with clients; live one-to-one minutes don't. Early on, conversations bind: few clients, many decisions. At scale, care binds. So the master variable is revenue per synchronous minute, and the master move is turning live one-to-one work into one-to-many or async forms without losing the human contact that drives adherence (T2, T3).
- *Evidence:* the ICF base rate is ~11.6 coaching h/week across 12.4 clients (MODERATE); the rest is DERIVED.
- *Changes:* two core operating metrics, **Operator Hours per Enrollment** and **Care Minutes per Client-Week**. A monthly "which constraint binds?" call replaces generic growth goals.

**T2. Delivery format doesn't buy results; rhythm does. 1:1 is a service tier, not a results tier.**
- *Evidence (primary re-analysis):* in low-bias, high-income depression trials, pooled effects against control were individual g=0.46 [0.38–0.54, k=105], group 0.53 [0.41–0.65, k=57] and guided self-help 0.54 [0.47–0.61, k=90]. Treatment-arm dropout was ~19%, ~20% and ~25%.
  - Total sessions showed **no** association with effect (slope ≈0).
  - **Sessions per week** did: +0.17 to +0.42 g per extra weekly session, z=2.0–5.5.
  - Longer programs trended slightly weaker.
  - This matches the published delivery-format network meta-analysis and session meta-regression (recalled — verify).
- *Strength:* STRONG within its domain. Transfer to habit and adherence coaching is an analogy: MODERATE–WEAK.
- *Changes:*
  - Cohort plus weekly review is the flagship on outcome grounds, not just capacity grounds.
  - Private is sold on access, privacy and feedback speed, never on "better results", which would fail the Informed-Client Test.
  - Weekly short touches beat fortnightly long calls.
  - Run a 12-week intensive, then a lighter Hold phase.

**T3. The active ingredient is proactive contact, not available contact.**
- *Evidence (primary re-analysis of 118 self-guided comparisons, where no content guidance was allowed):*
  - *Content-free human encouragement* (someone checks on adherence) went with g=0.60–0.63, against 0.37–0.46 for pure self-help: +0.17 to +0.23, z=1.75–2.70. Dropout was ~12% against ~23–25%.
  - **Support on demand performed like no support.**
- *Strength:* MODERATE (between-trial comparison, small dropout k). It matches the supportive-accountability model (P2).
- *Changes:*
  - "DM me anytime" and "ask in the group" are not delivery units. Coach-initiated, scheduled check-ins are.
  - Even the Down-Path gets a scheduled human touch (a **Human-Touch Floor**).
  - Premium means *proactive attention*, not *access*.

**T4. Standalone Private 1:1 earns about half the cohort's per-delivery-hour yield, so build it as a layer.**
- *Reasoning:*
  - On B1's hour estimates, 1:1 at $3–6k over 12–16 weeks at 2.5–4 h/client/month yields ~$200–870/h (midpoint ~$430). The cohort at $1.9–2.4k and 0.6–1.2 h/client/month yields ~$575–1,450/h (midpoint ~$860).
  - Parity pricing for standalone 1:1 is ~$8–10k, above most 22–32-year-olds' cash ceiling.
  - A **Private layer on top of the cohort** adds ~1–1.5 h/month of 1:1 for +$2.5–4k, so the cohort carries curriculum, stage calls and peer effects. That keeps the familiar $4.5–6k total at cohort-level yield.
- *Evidence:* DERIVED from ESTIMATE hours. T2 implies no outcome penalty for the layer design.
- *Changes:* the ladder reads "Cohort" and "Cohort + Private", not "Cohort" and "1:1 Program". Private requires a call, so cap its seats by sales minutes as well as care minutes.

**T5. The paid assessment answers the Call Ceiling, provided it sells the decision rather than the diagnosis.**
- *Reasoning:*
  - A free sales call costs **2.7–8.3 operator hours per enrollment**: a 0.75 h slot ÷ (60–80% show × 15–35% close). It earns nothing from non-buyers.
  - A paid, credited assessment costs **1.5–3 h per enrollment** (0.75 h ÷ 25–50% conversion, ESTIMATE) and keeps $150–250 from each non-converter.
  - At 5 sales h/week, free calls yield ~2.6–8 enrollments a month; paid assessments yield ~7–14, plus ~$2.9–4.3k a month in fees.
  - It saturates near 30 a month, so at scale it goes async-first: a recorded review plus a written plan, with an optional 15-minute live slot.
  - "Analysis" is priced toward zero by software (~$3.99/week rating apps, ~$80 one-off, $150/yr memberships) and is exactly where the hard line on diagnosing sits. Judgment about *why this person stalled, what to change, whether coaching fits, and whom to see instead* is legally safer, harder to commoditize and nearer to the enrollment decision.
- *Evidence:* price screening (field RCT, STRONG, other domain); show-rate decay with lead time (MODERATE); conversion is an ESTIMATE with no public data. S1 profit swings ~$20k→$28k between 25% and 40% conversion.
- *Changes:* the assessment is the default front door, scoped as a stall/decision audit whose deliverable is a written plan and one recommendation. Measure its conversion in the first 60–90 days.

**T6. Screen before you charge. The sellable market may be only about half the raw lead flow.**
- *Reasoning:*
  - Minors dominate the hardcore audience (58–62% in two forum surveys, WEAK).
  - The age of majority is 19 or 21 in four US jurisdictions.
  - Clinical analogs put BDD at ~5–19% of appearance-change seekers.
  - A brief validated screen (sensitivity ~100%, specificity ~89–93% in clinical samples) would flag **~12–28% of adult applicants**, with positive predictive value only ~⅓–¾ (DERIVED). A flag therefore triggers a conversation and a referral route, not a label.
  - If minors are a fifth to three-fifths of opt-ins (the forum surveys set the top of that range; an older-skewing brand should sit lower, ESTIMATE), only **~30–70% of raw leads are sellable adults** before ability to pay.
  - Charging first and declining later creates refunds, disputes and harm.
- *Evidence:* STRONG (law; clinical prevalence), MODERATE (screener), DERIVED.
- *Changes:*
  - Order of operations: age and screen inside the free self-assessment, and a paid assessment only for eligible adults.
  - Gross up the demand requirement.
  - The declines become the Refusal Ledger, a costly and hence credible signal.

**T7. Price sits inside three ceilings (cash, capacity, credibility), and price rises are a capacity tool, not a profit lever.**
- *Reasoning:*
  - **Cash:** $2,500 is ~6% of a full-time 20–24-year-old man's gross annual pay (~$42k) and ~4% of a full-time 25–34-year-old's (~$59k). Plans are needed, and students fall below the flagship.
  - **Capacity:** revenue must clear ~$700 per delivery hour, which puts the cohort at roughly ≥$1.5–1.9k.
  - **Credibility:** for an unknown seller, a generous high-price guarantee isn't believed. Price signals quality weakly (r≈.29, weaker for services), and an unexplained premium reads as grift.
  - So the launch band is **~$1.5–2.2k**, rising to **$2.4–3k** as contextualized outcomes accumulate.
  - At 75–85% margins, +1% price adds only ~1.2–1.3% profit (DERIVED; versus ~11% at thin margins). Price matters because it throttles demand to seats and raises yield per synchronous minute.
  - Buyers who later see a lower price buy less (28-month field experiment, STRONG).
- *Changes:* a **Proof-Gated Price Ladder**. Raise only when utilization stays above 85% for 2+ cycles *and* outcome milestones are met, on announced dates that hold. Grandfather alumni and never discount below recent buyers.

**T8. Surgery and filler prices go on the market map, never into the anchor.**
- *Reasoning:*
  - Anchors move valuations most when they feel informative (contested for willingness to pay). A surgery anchor feels informative *because* it implies substitution, which the hard line forbids.
  - It also recruits the riskiest buyer: the structural-change seeker, who fits the BDD-risk profile.
  - Honest anchors: his own sunk spend (devices, apps, courses, months), coaching market rates ($234–297/h), and your delivery math.
- *Evidence:* MODERATE + Standard.
- *Changes:* "Cheaper than surgery" is banned copy. An alternatives table may appear only as "what each option is and isn't", with a refer-out.

**T9. For young buyers, when payments fall due matters as much as the price, so instalments must end before delivery does.**
- *Reasoning:*
  - Usage decays after each payment (payment depreciation, MODERATE–STRONG).
  - Paying after consumption feels like paying for nothing (prepaid-versus-post-paid mental accounting, recalled — verify).
  - Coaching plans have no underwriting. Underwritten BNPL still sees 4.1% of loans incur late fees and 1.83% charged off (STRONG). Involuntary card failure runs ~0.9%/cycle (MODERATE).
  - Plan-driven sales lift (~+20%) comes mostly from weak-credit buyers (STRONG).
- *Changes:* the **Plan-Within-Program Rule**:
  - ≤3–4 instalments, all due before about week 8–10 of a 12-week program;
  - a premium of ≤10–15%;
  - one affordability question;
  - automatic retries;
  - a no-plan Down-Path for anyone who can't pay.

  Expect ~3–8% leakage (DERIVED), not 15–20%.

**T10. For a solo coach, chargeback risk is a processor-relationship risk that arrives at small counts.**
- *Reasoning:*
  - Visa's 1.5% merchant tier needs ≥1,500 fraud reports plus disputes a month, and Mastercard's needs ≥100 chargebacks. A solo coach never gets there.
  - Acquirers, though, are graded on their whole portfolio (reported acquirer tiers ~0.3–0.7%), so they police small merchants on counts and patterns. At 30–60 transactions a month, one dispute is a 2–3% ratio.
  - Termination can mean a multi-year industry blacklist (MATCH, ~5 years; MODERATE).
  - Most coaching disputes are "didn't recognize the charge" or "didn't get what was promised".
- *Evidence:* MODERATE (secondary summaries quoting the network rules); mechanism DERIVED.
- *Changes:*
  - Use a **recognizable descriptor**: the brand name, not an obscure LLC name and not appearance-coded words. "Discreet billing" must not become an unrecognizable charge.
  - Record onboarding acknowledgement.
  - Make refunds claimable through a conversation.
  - Follow T9's plan rule.
  - Ask the processor about reserve policy before launch.

**T11. The fit window is partly the law, so build the guarantee on top of the statute.**
- *Reasoning:*
  - **UK:** consumers have 14 days to cancel online service contracts (Consumer Contracts Regulations reg 30). If they expressly ask to start early, they owe a proportionate amount (reg 36). They lose the right only if the service is fully performed after express request and acknowledgement.
  - **EU:** the waiver additionally needs durable-medium confirmation, and standard checkouts don't collect it.
  - **UK subscriptions:** the new regime (renewal reminders, easy exit, renewal cooling-off) is **not in force**. Aug 2026 notes say it was brought forward to January 2027; earlier guidance said spring 2027.
  - **US:** no general online cooling-off; state auto-renewal laws apply; the federal click-to-cancel rule was vacated in 2025 and rulemaking restarted in 2026.
- *Evidence:* STRONG (statutory text via compilations); timing MODERATE.
- *Changes:*
  - B1's 14–21-day fit window stands, framed as "at least your legal rights".
  - Deliver the assessment only after express request and acknowledgement.
  - Continuity gets reminders and one-click exit now.
  - "No refunds" copy is a misleading-omission risk for UK and EU buyers.

**T12. Continuity's real product is the outcome dataset; the monthly revenue is a by-product.**
- *Reasoning:*
  - At target scale, continuity is only ~8–10% of revenue (S1: $2.6k of $33.7k; high case: $5.4k of $52.8k).
  - The outcomes that matter here are slow. Habit automaticity has a median of ~2 months and spans days to most of a year.
  - So months 4–12 of re-measurement exist *only* in continuity. That is the source of long-timeline, typical-range proof, the moat that FTC typicality rules make scarce, and it is the natural referral moment.
- *Changes:*
  - Continuity is usage-backed: monthly reassessment prompts, quarterly standardized photo sets, one-click cancel.
  - Its KPIs are re-measurement completion and referral asks.
  - Sell it at graduation, priced $39–79.

**T13. One flagship, two buffers.**
- *Reasoning:* content-led demand is lumpy and capacity is fixed.
  - The **paid assessment** monetizes and screens the non-converters.
  - **Continuity** monetizes and measures the graduates.
  - The cohort, with rolling monthly starts and weekly stage calls, stays the only flagship.
  - A full DIY system waits for 30–50 graduates: unguided products produce little proof (MOOC completion 3.13%; app day-15 retention ~3.9%; STRONG).
  - A **minimal Down-Path exists from day one**, because the Standard needs a humane place to send "can't afford" and "not a fit".
- *Changes:* this resolves the B1/B2 DIY timing conflict.

**T14. Two unmeasured ratios decide the audience you need, by a factor of 3 or more.**
- *Reasoning:*
  - For S1's ~28 paid assessments a month, at 2–6% lead→assessment and ~5 subscribers per 1,000 long-form views, you need **~470–1,400 leads and ~90–280k long-form views a month**. Across the 1–10 subscribers-per-1,000 planning range, that becomes ~50k–1.4M views.
  - Assessment conversion moves profit by ~$8k a month.
- *Evidence:* DERIVED (WEAK/ANECDOTAL inputs, from E2/B1).
- *Changes:* months 1–3 are an instrumentation project: UTMs, a self-reported attribution field, and an assessment-vs-fit-call test. Paid ads come only after E2's Three Ad Gates.

**T15. The named brand should own the method, the protocol and the proof, and none of its names should be claims.**
- *Reasoning:*
  - Owner-named firms outperform because the owner's reputation is at stake (+~3 pp return on assets, AER 2017, STRONG), and they fall with the owner. The category's namesake was struck off in 2024 and lost his appeal in May 2026.
  - A product name is a claim: regulators judge the net impression, and platforms age-gate "restore structure" wording.
  - So a "Bone Remodeling Protocol" costs reach *and* adds legal exposure.
- *Changes:*
  - The face carries trust. The method, measurement protocol, cohort and continuity names sit under the brand, in process language.
  - "Mewing" is a search keyword, never the brand's identity.
  - This is a hard-to-reverse decision; make it before the first cohort.

**T16. The first 5–10 clients are R&D, and 1:1 is the right R&D format.**
- *Reasoning:*
  - The cohort's stall taxonomy, check-in instrument and proof protocol don't exist yet, and 1:1 generates that learning fastest.
  - Hybrid entrepreneurs (who keep other income) are ~33% less likely to exit (STRONG).
  - So early 1:1 at an honest, time-limited founding price is an investment in design and first contextualized outcomes, with a planned sunset.
- *Changes:* stage path is founding 1:1 (months 0–4), then a beta cohort (~months 3–5), then cohort + layer + continuity. B1's ~$16.5k profit at month 12 is a waypoint, not a failure.

---

## 2. Key decision inputs

### Business
- **Front door (options + default).**
  - Options:
    - (a) a paid decision assessment;
    - (b) a free 15-minute fit call;
    - (c) direct enrollment from a page;
    - (d) a paid community;
    - (e) a low-ticket product.
  - **Default: Assessment-First.** An age-gated, screened free self-assessment → a paid assessment ($150–250, credited within 14–30 days, slots within 0–3 days) → one recommendation. Warm viewers get (c) with an optional fit check. DMs only route. (d) is rejected as a front door, and (e) is used only as the Down-Path.
- **Offer ladder.**
  1. Down-Path: a $27–97 tool (ESTIMATE, inside B1's $27–300 low-ticket band) with a Human-Touch Floor.
  2. **Cohort (flagship):** 12 weeks, rolling monthly starts, stage calls, weekly async review.
  3. Cohort + Private layer: capped.
  4. Usage-backed continuity: alumni only.
  5. Later additions: a $97–297 DIY system and quarterly productized reviews, after 30–50 graduates.
- **Profit engine.** S1 (Assessment → Cohort → Continuity) is the default. S3's DIY-plus-ads is a later layer. S2's community core is rejected except as alumni continuity.
- **Pricing.**

  | Offer | Price |
  |---|---|
  | Assessment | $150–250 |
  | Cohort at launch | $1.5–2.2k |
  | Cohort after proof | $2.4–3k |
  | Private layer | +$2.5–4k (≈$4.5–6k total) |
  | Continuity | $39–79/mo |
  | Plans | ≤10–15% premium, inside the program |

- **Buyers.**
  - *Primary:* the employed Self-Taught Struggler, 20–32.
  - *Premium:* the Optimizer, 25–35.
  - *Students 18–21:* Down-Path or DIY only.
  - *Breathing-first adults:* an optional lower-stigma entry, with a firm referral protocol.
  - *Women and men over 30:* allowed, not targeted.
  - *Minors and parents:* excluded from paid offers.
- **Capacity.** ~40–65 concurrent clients at 6–10 minutes of review per client per week plus ~3 h of stage calls, which is ~13–22 enrollments a month. Seat caps are computed from measured review minutes.
- **A candidate module map for the ~14 Business modules:**
  1. Business math and the synchronous minute
  2. Market and buyer selection
  3. Category reframe and brand architecture
  4. Offer architecture
  5. The front door
  6. Flagship design and delivery rhythm
  7. The premium layer
  8. Pricing
  9. Payments, plans, guarantees and disputes
  10. Continuity and renewal
  11. The proof engine
  12. The referral engine
  13. The operating model (freelancers, time budget, systems)
  14. Metrics and the scaling path

### Persuasion: mechanisms that deserve whole modules
1. Trust without credentials: costly signals, refutational two-sidedness, the Refusal Ledger, evidence grading.
2. Belief change on "adults can't change": expectations rather than fantasies, re-attributing stalls to controllables.
3. Identity and commitment, tied to logged behaviour.
4. The glass-box sales conversation.
5. Price and payment psychology at the point of decision.
6. **Selling without a call**: pages, voice notes, one-to-many enrollment sessions. The Call Ceiling makes ≥50% call-optional enrollment necessary at scale.
7. **Adherence engineering**: proactive contact, frequency, if-then plans, two-track monitoring, lapse recovery (T2/T3 make this a business lever, not only a service one).
8. Expectations, measurement and proof ethics.
9. Retention, renewal and discreet referral.

### Ecosystem
- **Center of gravity:** YouTube long-form → email → a self-assessment on the owned site.
- **Channel roles:**
  - Short-form is a discovery feeder, judged by subscribers and opt-ins per 1,000 *engaged* views.
  - Instagram is a keyword-DM router for adults only.
  - X is a person-graph credibility network that captures to the newsletter.
  - Paid ads are an amplifier only, after the gates.
  - The website is the hub: prices, refusal/referral pages, the standardized-proof library.
- **What replaces the free community:** the email list, the paid assessment and continuity together form the owned relationship layer.
- **Demand requirement (S1, mid-case):** ~90–280k long-form views a month.

---

## 3. Ledger candidates

| Metric | Range | Moves up / down | Confidence |
|---|---|---|---|
| Average coach annual revenue | ~$49k global; ~$72k US | Experience, region, niche | MODERATE |
| Coaching fee per hour | $234 global; $297 N. America | Region, experience | MODERATE |
| Revenue needed for $25–50k profit | $30–75k/mo cash | Margin 65–85%; ads and a producer lower it | DERIVED |
| Revenue needed per delivery hour | $700–2,600 | Delivery hours 26–43/mo; cost share | DERIVED |
| 1:1-only revenue ceiling | $11–22k/mo | Engagement price; hours per client | DERIVED/ESTIMATE |
| Free-call sales ceiling (5 sales h/wk) | ~$10–25k/mo (≈2.6–8 enrollments) | Show and close rates; price | DERIVED (WEAK inputs) |
| Operator hours per enrollment | Free call 2.7–8.3; paid assessment 1.5–3 | Show rate, conversion, slot length | DERIVED/ESTIMATE |
| Care capacity | 40–65 concurrent clients | Review minutes (6–10/client/wk); check-in format | DERIVED |
| Per-hour yield | Cohort ~$575–1,450; standalone 1:1 ~$200–870 | Price; hours per client | DERIVED |
| Cohort price | Launch $1.5–2.2k; with proof $2.4–3k | Proof, utilization, buyer age | ESTIMATE (MODERATE anchors) |
| Paid assessment price | $150–250, credited 14–30 days | Commodity floor pushes down; judgment value pushes up | MODERATE |
| Assessment → program | 25–50% | Speed to slot, plan clarity, screening upstream | ESTIMATE (no public data) |
| Show rate by booking lead | ~81% next day → ~60% at 14 days | Reminders, lead time, payment | MODERATE |
| Close rate, held qualified calls | 15–35% | Warmth, qualification | WEAK |
| Delivery-format effects (analog) | Individual g≈0.46; group ≈0.53; guided ≈0.54 | — | STRONG in domain; transfer WEAK–MODERATE |
| Trial dropout by format (analog) | ~19% individual; ~20% group; ~25% guided | Human contact lowers it | STRONG in domain |
| Contact frequency (analog) | +0.17 to +0.42 g per extra weekly session; total sessions ≈0 | — | MODERATE (meta-regression) |
| Human encouragement vs pure self-help (analog) | +0.17–0.23 g; dropout ~12% vs ~23–25% | On-demand support ≈ none | MODERATE |
| Unguided real-world completion | MOOC 3.13%; apps ~3.9% at day 15 | Human touch, deadlines | STRONG |
| BDD prevalence (clinical analogs) | ~19% cosmetic-surgery seekers; ~11% orthognathic; 5–6% orthodontic; 1.7–2.4% general | Setting | STRONG (analogy to this audience) |
| Screen-positive share of adult applicants | ~12–28% (positive predictive value ~⅓–¾) | Prevalence, screener specificity | DERIVED |
| Sellable-adult share of raw leads | ~30–70% before ability to pay | Minor share (ESTIMATE), screen rate | DERIVED/ESTIMATE |
| Age of majority | 18 in most of the US; 19 AL/NE; 21 MS/PR | Jurisdiction | STRONG |
| Buyer income | Full-time men 20–24 ~$42k/yr; all full-time 25–34 ~$59k/yr; a $2.5k program = 4–6% of gross annual pay | Age, employment | STRONG |
| Payment plans | ~+20% sales, driven by weak-credit buyers; premium +10–15% | Underwriting, plan length | STRONG (effect) / WEAK (premium) |
| Uncollected plan revenue | ~3–8% short plans inside the program with retries; 15–20% long plans without recovery | Plan length versus delivery; dunning | DERIVED/WEAK |
| Refunds + chargebacks | 2–8% of coaching revenue | Guarantee design, onboarding, affordability screening | ESTIMATE |
| Card-network program floors | Visa merchant: 1.5% AND ≥1,500 disputes+fraud/mo; Mastercard: 1.5% AND ≥100 chargebacks | Rule changes | MODERATE |
| Dispute-rate target | <0.5% of transactions | Descriptor, terms, plan design | MODERATE |
| Community / continuity churn | 4–8%/mo typical; 8–15% open cheap; 2–3% curated premium | Price, programming | WEAK |
| Continuity take rate at graduation | 30–60% | Graduation-moment offer, usage design | WEAK/ESTIMATE |
| LTV per program client | $1.8–3.9k | Price, continuity take and churn | DERIVED |
| Continuity share of revenue at target | ~8–10% | Take rate, price | DERIVED |
| Required long-form views (S1 base) | ~90–280k/mo (≈470–1,400 leads) | Lead→assessment 2–6%; subscribers per 1,000 views | DERIVED (ANECDOTAL inputs) |
| Scenario profit | S1 base ~$27.8k at ~24.5 h/wk; high ~$45k; month-12 ~$16.5k; stress at 25% conversion ~$20k | Conversion, price, continuity | DERIVED |
| Price leverage at 75–85% margin | +1% price → ~+1.2–1.3% profit | Margin | DERIVED |
| Price–quality signal | r≈.29; weaker for services | Familiarity, service vs product | STRONG |
| Just-below price endings | g≈0.13 → ~0 after bias correction | — | STRONG |
| Freelance editing | Long-form $50–150 offshore / $300–1,500 domestic; shorts $20–100; bundle ~$2.5–3k/mo | Complexity, turnaround | MODERATE/WEAK |
| UK statutory cancellation window | 14 days (services); proportionate charge if started early at the buyer's request | Express request + acknowledgement | STRONG |

---

## 4. Framework seeds

1. **The Minute Ledger / Constraint Clock.** Revenue per synchronous minute, by activity. Each month, name the binding minute: sales early, care at scale.
2. **Enrollment Mix Equation.** Required call-optional enrollments = target enrollments − (sales hours ÷ hours per call-path enrollment). It tells you when to build async and one-to-many enrollment.
3. **Layered Private.** Premium sold as proactive attention added to the cohort and priced to per-hour parity. It is never a separate 1:1 track and never promises better results.
4. **Frequency-First Delivery.** A weekly rhythm of short touches. The check-in instrument is designed to be reviewed in 6–10 minutes. Program length stays short and intensive, followed by a Hold phase.
5. **Human-Touch Floor.** Every product, including DIY, carries at least one scheduled, coach-initiated contact, because on-demand access doesn't count.
6. **Screen-Before-Charge Door.** Age of majority → brief screen → paid decision assessment → one recommendation, with a scripted decline-and-refer.
7. **Sellable-Adult Yield.** The true top-of-funnel metric: adults who pass the screen and can pay, as a share of raw leads.
8. **Three-Ceiling Pricing + Proof-Gated Price Ladder.** Cash, capacity and credibility ceilings define the band. Rises unlock on utilization above 85% plus outcome milestones, on announced dates, with alumni grandfathered.
9. **Market Map, Not Anchor.** A whitelist of honest anchors (sunk spend, coaching rates, delivery math) and a blacklist (surgery or filler as substitutes).
10. **Plan-Within-Program Rule.** Instalments finish before delivery does; plus an affordability question and a no-plan Down-Path.
11. **Statute-Plus Guarantee.** Statutory cancellation rights first, then a fit window, then a Process Guarantee on controllables.
12. **Recognizable Discretion.** A billing descriptor that the buyer recognizes but that isn't appearance-coded, plus recorded onboarding acknowledgement.
13. **One Flagship, Two Buffers.** The assessment absorbs non-converters and continuity absorbs graduates around the cohort.
14. **R&D Clients.** A founding 1:1 cohort priced honestly, with an explicit sunset, to build the stall taxonomy and first proof.
15. **Pair Enrollment (Discreet Referral variant).** "Bring your training partner into the same cohort": a private referral that also works as an adherence intervention.

---

## 5. Standard Card flags

- **Assessment language (hard line 2).** Never "diagnosis", "analysis of your structure" or scores. Assess habits, history and standardized photos. Refer-out triggers: sleep, jaw pain, orthodontic history, BDD flags.
- **Anchoring (notch 8 vs hard line 2).** Anchoring is permitted; substitution anchors are not. The alternatives table is framed as scope and referral.
- **Payment plans (hard line 5).** 18+ *and* of legal age where the buyer lives. Ask one affordability question. After "I can't afford it", offer the Down-Path, then stop selling. No plans that outlive delivery.
- **Scarcity (notch 4 / hard line 3).** Seat caps are computed from published review minutes, and cohort dates and price rises actually happen. No invented "spots left".
- **Guarantees (notch 8 / hard line 2).** Guarantee process and controllables only. Claiming should be a conversation, not an obstacle course (Informed-Client Test). Never misstate statutory rights ("no refunds" to UK/EU consumers).
- **Private tier (Informed-Client Test).** Sell speed, privacy and attention, not superior outcomes; the format evidence says otherwise.
- **Continuity (Informed-Client Test).** No earning from non-use: reminders, usage nudges, one-click cancel, ahead of the UK's 2027 subscription rules.
- **Proof (hard line 1).** Ask everyone at fixed checkpoints, with consent, standardized photos and typical ranges. Disclose any incentive. Never gate reviews.
- **Names and credentials (hard lines 2 and 6).** No structural claims in product names. No "therapist", "specialist" or "myofunctional" titles.
- **Minors and BDD (hard line 5).** Screen before charging. Never enroll acute distress. Every decline carries a referral.
- **DMs (hard line 5).** Route people; never close with unverified ages.

---

## 6. Failure modes (what operators in this niche get wrong)

1. **Building 1:1 first and never leaving it.** Revenue caps at ~$11–22k.
2. **Using the free "strategy call" as the front door.** It hits the Call Ceiling and carries grift optics.
3. **Selling face analysis.** It lands on the commodity floor and on the hard line.
4. **Running low-ticket e-book ladders.** Nobody finishes, so there's no proof, against a $5–15 price floor.
5. **Using a paid community as the front door.** It brings churn, moderation load and minors, and drifts back to the free-community pattern.
6. **Pricing Private at ~2× the cohort while it eats 3–4× the hours.**
7. **Relying on monthly calls and "message me anytime" support** instead of weekly proactive touches.
8. **Selling long plans for short programs.** Defaults and disputes follow.
9. **Anchoring on surgery.** It implies substitution and attracts structural-change seekers.
10. **Taking money before age and screening checks.**
11. **Fake timers and discounts to fill cohorts.** This punishes past buyers and trains people to wait.
12. **Using an unrecognizable or embarrassing billing descriptor.**
13. **Writing "no refund" terms that ignore UK/EU statutory rights.**
14. **Building brand identity on "mewing"** or on a discredited founder's vocabulary.
15. **Buying ads before the organic ratios are measured.**
16. **Checking faces often instead of logging behaviour.** It feeds body-checking and produces noisy proof.

---

## 7. Remaining open questions

1. **Assessment → program conversion in this niche.** Run a 60–90-day test of the paid assessment against a free fit call.
2. **The achievable call-optional enrollment share at $1.5–3k.**
3. **This brand's real audience.** Age mix, minor share, income and geography.
4. **Real screen-positive rates** under a brief BDD screen in a non-clinical coaching intake, and which wording and cut-off to use.
5. **Actual plan leakage and dispute rates** at $1.5–3k, and processor reserve policy for coaching sold over months.
6. **Fitness and body-transformation coaching price bands, 2024–26.** Still unverified.
7. **Churn in paid continuity** for men aged 18–25.
8. **Does format equivalence transfer** from psychotherapy to habit and appearance coaching? Track adherence by tier.
9. **The minimum weekly review minutes that preserve adherence.** Test 5 vs 10 vs 15 minutes.
10. **Demand trend** for "mewing", "jawline" and "recessed chin" searches after the category's 2024–26 authority collapse.
11. **Is honest, anti-rating positioning a price driver** or only a trust driver?
12. **The UK subscription regime.** The exact commencement date, and whether monthly continuity triggers renewal cooling-off.

---

## 8. Gap-fill sources and method (for verification only; never cited in the playbook)

- **Trial re-analysis (T2, T3).** Metapsy `data-depression-psyctr` (DOI 10.5281/zenodo.7254845) and `data-depression-selfguided-psyctr` (DOI 10.5281/zenodo.12705748), fetched from raw.githubusercontent.com.
  - Post-test depression outcomes only; one effect per comparison (mean across instruments).
  - DerSimonian–Laird random effects.
  - "Low bias" = risk-of-bias score ≥3/4. "High-income" = US, UK, EU, Canada, Australia.
  - Frequency analysis: inverse-variance meta-regression on sessions, sessions per week and weeks.
  - Format comparisons are between trials, and therefore confounded.
- **Card networks (T10).** GitHub compilations quoting the 2025 Visa VAMP fact sheet and Mastercard ECP rules: `NithishaVenkatesh/upi-agent-conformance` (T02_vamp_governor.md), `luzan/payment-space` (ongoing-monitoring.md, network-requirements.md), `jaimeramiro-dev/better-safe-than-sued` (sources.ts), `ankitjha67/product-architect` (13-fraud-operations.md).
- **Age of majority (T6).** AT&T Terms of Service (`OpenTermsArchive/snapshots-tosback`); IRS Direct File (`openfile` dependentsBenefitSplit.xml).
- **UK/EU cancellation (T11).** UK Consumer Contracts Regulations 2013 regs 30 and 36 (legislation.gov.uk/uksi/2013/3134, via `Soham109/duesday`, `clemensjl/claude-skills` legal-uk); EU Consumer Rights Directive 2011/83/EU arts 9 and 16 and CJEU case C-641/19 (via `jaewookng/dermodel.v1`). DMCCA subscription timing: `ORCHORDS/docs` (18 Aug 2026), `Megablaze757/FOOTBALLFITNESSGURU` legal audit (17 Aug 2026, citing the GOV.UK response of April 2026), `mjmirza/app-store-compliance` (9 Aug 2026 announcement), `Marksbutcher/UK-Consumer-Rights` (17 Aug 2026).
- **BDD screener (T6).** A JMIR 2023 article (DOI 10.2196/46515) summarising BDDQ validation (sensitivity 100%; specificity 89–93%); Joseph et al. 2016, facial-plastic-surgery BDDQ screening.
- **Recalled — verify before the ledger:** Cuijpers et al. 2019, network meta-analysis of CBT delivery formats; Cuijpers et al. 2013, meta-regression on how much psychotherapy is needed; Prelec & Loewenstein 1998, "The Red and the Black" (prepayment and decoupling).
- **All other figures** come from B1, B2, P2, E1 and E2, with their original strength tags.
