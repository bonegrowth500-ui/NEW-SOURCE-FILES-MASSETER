# LEDGER v3 — Canonical numbers & ranges

Every number in any module must match this ledger. Update the ledger first, with reasoning. In the playbook, numbers appear as **ranges with context** (what moves them up or down), never as single points, and never cited.

v3 applies DECISIONS R2:
- full-cost design weeks (milestones, selling, Private, Hold, and building all priced);
- the cash ceiling;
- two tiers at scale;
- Round Two per graduate;
- the Hold ramp;
- Private only at parity;
- the Call Cap;
- the founding group on overflow;
- a labeled warm-network source.

Models: `models/model4.py` (weeks, configurations, parity) and `models/model5.py` (waypoints).

**Status key.** **EV** = evidence-based (tag S/M/W/C). **PL** = planning assumption, derived or estimated; the operator's own data replaces it after ~30 events. **RULE** = a policy or design number we set.

**Denominators.**
- YouTube ratios: per 1,000 *engaged* views.
- Email: per *delivered*.
- Sales: per *eligible-lead cohort*.
- Round Two: per *graduate*.
- Profit: per *operator hour*.

**Margin basis (one definition everywhere).** Profit = cash collected − processing − refunds/disputes − freelancers − software − paid reach. The planning margin is 75–85% without paid reach and 65–80% with it. In the first months fixed costs dominate, so profit is computed from costs, not from a margin.

**Public-number rule.** No PL figure is ever published as the brand's result. Performance, outcome, and client numbers appear in public only from the operator's own records. External research appears only attributed at its evidence tier.

---

## A. Targets & economics

| Metric | Range | Moves it up / down | Status |
|---|---|---|---|
| Profit target | $25–50k/month | — | RULE (spec) |
| Cash collected needed | ~$29–38k for $25k; ~$59–77k for $50k | Margin; paid reach lowers it | PL (D) |
| Operator hours | 20–25/week (≈87–108/month). **Designed to ~20 early.** Target configurations run ~20–22 and use part of the slack | — | RULE |
| Revenue per operator hour at target | ~$270–890 | Margin; share of non-revenue hours | PL (D) |
| Care minutes per client-week, all-in (review + amortized group call + milestones) | Early/founding ~30–35; Growing ~18–20; Scaling ~13–15 | Templating; group size; milestone templates | PL (D) |
| Cohort revenue per care hour | ~$800 (proof band, Growing) to ~$1,250–1,400 (at the ceiling, Scaling) | Price; care minutes | PL (D) |
| Standalone 1:1 per delivery hour | ~$100–330 (45–75 min/client-week) | Price; templating | PL (D) |
| One-to-one-only ceiling (12–14 delivery h/week) | ~$5–20k/month revenue | Price; minutes per client | PL (D) |
| Engine alternatives (planning comparison) | **Premium 1:1-led** (~$6k per 12 weeks, ~10–12 concurrent): ~$17–22k profit. **Membership-led**: needs ~530–1,080 members at $29–59 with 8–15% monthly churn. **Digital-led**: needs ~160 sales/month at ~$197 for $25k | Price; churn; reach | PL (D) |
| Free-call selling ceiling at ~5 selling h/week | ~3–10 enrollments/month | Close rate; hours per call | PL (D) |
| Price leverage | +1% price → ~+1.2–1.3% profit at 75–85% margin if volume holds. When seats bind, a raise that loses a smaller share of buyers than its % flows almost entirely to profit | Margin; share of buyers lost | PL (D) |
| Capacity Ceiling (care hours ~9–10.5/week) | Growing ~25–30 concurrent (~8–10 new enrollments/month). Scaling ~40–45 concurrent (~12–15/month) | Templated review; milestone templates; group-call load | PL (D) |
| Revenue per eligible lead | ~$25–210 (LTV $1.7–3.0k × eligible lead → enrollment 1.5–7%) | Conversion; price; back end | PL (D) |
| Maximum affordable cost per eligible lead | At most about a third of revenue per eligible lead, so roughly $10–70 | Margin target; conversion | RULE (D) |

### A2. Stages (trailing 3-month average + a volume signal)

| Stage | Revenue | Volume signal | Binding constraint | North star |
|---|---|---|---|---|
| **Early** | < ~$8k/month | < ~50 eligible leads/month; < ~15 concurrent clients | Reach, then conversations | Held qualified conversations/week + cash collected |
| **Growing** | ~$8–30k/month | ~50–150 eligible leads/month; ~15–25 concurrent | Conversion + selling minutes | Enrollments/month + eligible lead → enrollment |
| **Scaling** | ~$30k+/month | ~150+ eligible leads/month; ~25+ concurrent, or a waiting list | Care minutes | Profit per operator hour |

Mixed signals (e.g., Growing on revenue, Early on volume): the binding constraint decides which moves apply. The sequence can slide back after a lever is pulled (a raise can hand the constraint back to conversations).

### A3. Reach bands & waypoints (PL, derived; conservative → good assumptions)

Bands are defined by **eligible adult leads per month** at month 9. Engaged long-form view equivalents assume a 30–70% eligible share and 2–5 raw leads per 1,000 engaged views. Short-form and Instagram add reach these figures don't capture.

| Band | Eligible leads/month (m3 → m6 → m9) | View equivalent at m9 |
|---|---|---|
| **A: the channel never breaks out** | 10–20 → 20–35 → 25–50 | ~7–85k/month |
| **B: steady** | 15–30 → 40–80 → 60–150 | ~17–250k/month |
| **C: breaks out in year 1** | 20–40 → 60–150 → 150–400 | ~43–670k/month |
| **D: breakout** | 25–50 → 100–250 → 400–700 | ~115k–1.2M/month |

**Waypoints, per month.** Held conversations include the labeled warm-network source (H). New clients are founding-group clients at m3, founding/opening-band clients at m6, and opening-band clients at m9. Cash includes early back-end revenue at m6 and m9. Hours run about 20/week in every band.

| Band | Month 3 | Month 6 | Month 9 | Middle case (profit: m9 → maturity at proof → two tiers at the ceiling) | When $25k is likely |
|---|---|---|---|---|---|
| **A** | 3–12 held · 0.5–4 new · cash $0.6–6k | 3–12 held · 0.5–4 new · cash $1–8k · profit ~$0–7k | 4–14 held · 1–6 new · cash $1.5–15k · profit ~$0–13k | ~$4k → ~$10k → ~$14k | Not on organic reach alone. It needs a reach lever (the Band A paid test at months 3–4, a breakout piece, referrals) plus ceiling pricing; year 2–3 |
| **B** | 4–14 held · 0.5–5 new · $0.7–7k | 6–21 held · 1–7 new · $1.5–14k · ~$0–13k | 8–34 held · 1.5–10 new · $3–28k · ~$1–25k | ~$9k → ~$21k → ~$28k | Year 2 (months ~12–24) |
| **C** | 4–16 held · 0.7–5.5 new · $0.8–8k | 8–35 held · 1.5–9 new · $2–17.5k · ~$1–16k | 19–35 held (+0–17 overflow assessments) · 4–10 new · $7–30k · ~$5–26k | ~$16k → ~$26k → ~$34k | Months ~12–18 (good case by ~9) |
| **D** | 5–18 held · 0.8–6 new · $0.9–9k | 13–35 held (+0–7) · 2–9 new · $3.5–18k · ~$2–16k | calls capped ~26–35 (+6–38) · 6.5–10 new · $13.5–32k · ~$10–28k | ~$17k → ~$27k → ~$35k | Months ~9–15. Capacity binds early, so price and templating are the levers |

**Readings.**
- Month 3 is decided by the Founding Sprint's sources and conversations; reach separates the bands from month 6.
- **Plan on A–B; treat C–D as upside.**
- Conservative assumptions plateau near ~$6–14k in every band until conversion, price, or capacity moves, and those are exactly the levers the playbook moves.
- $50k is the top of the range: years 2–3 in Bands C–D (or Band B with a working paid reach lever), through two tiers at the ceiling, the back end, and leverage, never through hours.

### A4. Hours — design weeks (PL; model4.py)

| Line (h/week) | Early (m0–3) | Growing (~$8–25k; 15–30 clients) | Scaling at ~$25k (~8–9 enrollments/month) | Scaling at ~$50k (~13 enrollments/month) |
|---|---|---|---|---|
| Long-form | 2.5 (every other week after the Honest Answer) | 3.5 (3/month) | 3.0 (2–3/month) | 3.0 |
| Short-form | 3.5 (4–7 native/week: the reach engine) | 1.25 | 0.5 | 0.5 |
| Email | 0.5 (result email + welcome flow; no weekly broadcast until a few hundred eligible adults) | 1.0 | 1.0 | 1.0 |
| Public replies, permission-first replies, routing | 2.0 | 1.0 | 0.75 | 0.5 (routing help moderates) |
| Speed to lead (personal reply to every adult lead) | 1.0 | 0.5 | 0.25 | 0.25 |
| Conversations / assessments | 4.5 (4–5 × ~1.0 h; 45-min dual-purpose call) | 3.0 (Call Cap + overflow) | 2.6 (~1.3 h/enrollment; ~50% no-call) | 2.8 (~1.0 h/enrollment; ~65–70% no-call) |
| No-shows, recaps, follow-up | 0.5 | 0.5 | 0.5 | 0.4 |
| Client review | 2.5 (founding group incl. milestones) | 3.75 (~20–25 × ~10 min) | 3.2 (~24 × ~8 min) | 3.6 (Program ~22 × 7 + Async ~14 × 6 min) |
| Group calls | — (inside founding delivery) | 2.0 | 2.0 | 2.0 (Program tier only) |
| Milestones (Commit Ritual, week-6 read, week-12 re-assessment) | (inside founding delivery) | 1.5 | 1.6 | 2.1 |
| Round Two (maintenance format) | — | (inside review) | 0.35 | 0.4 |
| Hold (measurement subscription → room) | — | 0.25 | 0.4 | 0.6 |
| Private | 0–0.5 (a founding Private seat, spare minutes) | 0.5 (0–1 seat) | 0.6 (~1 seat) | — (only at parity) |
| Fit-check conversations, Starter Path hand-offs, renewal reviews | 0.25 | 0.5 | 0.5 | 0.5 |
| Building (protected build line) | 1.5 | 1.25 | 1.0 | 1.0 |
| Admin, freelancer briefs, Operator Review | 1.0 | 1.5 | 1.5 | 1.5 |
| **Total** | **~19.75–20.25** | **~22.0** | **~19.75** | **~21.0** |
| Protected content minimum | ~8.5 | ~6.75 | ~5.25 | ~5.0 |

| Unit | Range | Moves it | Status |
|---|---|---|---|
| Review minutes per client-week | 12–20 for the first ~20 clients; 6–10 once templated | Check-in instrument; templates the operator approves | PL (D) |
| Milestones per enrollment (beyond weekly review) | ~0.75–1.25 h (onboarding + written week-6 read + week-12 re-assessment) | Templates | PL (D) |
| Selling hours per enrollment | Early 2.5–6 · Growing 1.5–3 · Scaling ~0.8–1.5 (most enrollments without a call) | Door setting; async arc; close rate | PL (D) |
| Fit conversation, all-in | ~1.0 h early (45-min dual-purpose call + prep + recap); 0.75 h later | Booking-form prompts | PL (D) |
| Decision Assessment, all-in | 1–1.5 h early; 0.5–0.75 h templated / async-first | Templates | PL (D) |
| Long-form, operator hours per piece (with editor) | ~4–6 | Scripting; batch filming | PL (D) |

### A5. Target configurations (steady state; PL, model4.py)

| | **$25k/month profit** (year ~2; Bands B–C) | **$50k/month profit** (year 2–3; Bands C–D) |
|---|---|---|
| Flagship | Program ~8–9/month × ~$3.1k (top of the proof band, at the 20–24 ceiling) ≈ $26k | Program ~8/month × ~$3.9k (25–34 majority) ≈ $31k + **Program Async** ~5/month × ~$2.8k (under the 20–24 ceiling) ≈ $14k |
| Round Two (per graduate ~18%; maintenance format) | ≈ $1.5k | ≈ $2.8k |
| The Hold (ramping) | ~20 members × $59 ≈ $1.2k | ~45 members × $69 ≈ $3.1k |
| Private | ~1 seat a quarter × ~$5k while minutes are spare ≈ $1.7k | Only if it passes the Parity Rule (not counted) |
| Self-Serve System | — | ~15 × ~$197 ≈ $3k |
| Decision Assessment fees (non-buyers) | ≈ $1k | ≈ $2.2k |
| **Revenue → profit** | **≈ $31.5k → ≈ $24.5–26.5k** | **≈ $56k → ≈ $44–47k; small Price Steps over time carry it to ~$50k** |
| Week | ~19.75 h | ~21 h |
| Eligible leads needed (≈ enrollments ÷ eligible lead → enrollment) | ~120–285/month at 3–7% (a proven door by Scaling); ~570 at 1.5% | ~185–435/month at 3–7% (~13 enrollments); ~870 at 1.5%. Band C–D reach, or Band B with a working paid reach lever |
| Held conversations at the configuration | ~8–17/month (about half of enrollments close without a call; held → enrollment 25–45%) | ~9–18/month (~65–70% of enrollments without a call) |
| Engaged long-form view equivalent | ~35–475k/month (120–285 eligible leads; 30–70% eligible share; 2–5 raw leads per 1,000 engaged views). Short-form and Instagram add reach not captured here | ~55–725k/month on the same assumptions |

## B. Offers & pricing (PL; anchors M)

| Metric | Range | Moves it up / down | Status |
|---|---|---|---|
| Early door: disclosed fit conversation | **Default free.** A small credited fee (~$25–50) only if no-shows eat selling hours. 20–30 min standard; ~45 min for the dual-purpose founding call. Purpose, price, and "one recommendation, which may be a program, the Starter Path, or don't buy" stated on the booking page | — | RULE |
| Decision Assessment (overflow of the Call Cap; async-first at volume) | $150–250. Credit held ~90 days (two starts); after a "not now" or Starter Path recommendation, until he enrolls (capped ~12 months). Terms stated once in writing. The written plan is worth its fee without buying, with a plan-usefulness refund | Judgment value; speed; commodity "analysis" apps | PL (M anchors) |
| Decision Assessment, priority tier | ~$350–600 (faster turnaround + recorded walkthrough), credited to the Program or Private; available from month 0; the Optimizer's entry | Demand for speed | PL (E) |
| Founding group (from the first client; monthly entry; 1:1-level review while under ~4 members) | ~$1.2–1.5k for 12 weeks; next price stated | Warmth; process proof | PL |
| Founding Private seats (1–2, while minutes are spare) | ~$4–6k for 12 weeks, fixed deliverables | Optimizer demand | PL (E) |
| Program, opening band | $1.5–2.2k, reached through Price Steps | Starts filling; close rate in range | PL |
| Program, proof band | $2.4–3.2k (the top sits at the 20–24 cash ceiling) | Proof milestone | PL |
| Program at the ceiling for 25–34 (Scaling) | ~$3.5–3.9k, alongside **Program Async** at ~$2.4–2.8k (async review only, no live call) as the real tier under the 20–24 ceiling | Buyer mix; proof | PL (E) |
| **Cash ceiling** | The core container's price stays within ~1–1.25 months of the core buyer's take-home, payable from income or savings without new credit or BNPL: ≈$2.8–3.5k at 20–24; ≈$3.9–4.9k at 25–34. Installments ≤ ~⅓ of monthly take-home | — | RULE |
| **Price Steps** | Small scheduled steps (e.g., ~5–10% every second start) that always happen while starts fill and close rates stay inside the ledger range. Each step names what was added, and none cuts a published deliverable or turnaround. The proof milestone gates the jump into the proof band. Announced ≥30 days ahead. Alumni grandfathered; never below recent buyers | — | RULE |
| Proof milestone | ≥10 graduates with consented process testimonials, plus the first outcome ranges with denominators | — | RULE |
| Round Two (maintenance format: biweekly async review, optional group call, re-captures at weeks 6 and 12) | ~$0.8–1.2k; uptake ~10–26% of graduates (20–40% of the 50–65% with measured momentum). Full intensity only for "misdirected, now corrected", priced as a Program | Adherence data; peak design | PL (E) |
| The Hold | $39–79/month; 20–40% take at graduation. A measurement subscription (quarterly re-capture + written review + Canon Lane) until ~30 alumni, then the alumni room opens. Members ≈ 12 / 21 / 31 at 6 / 12 / 24 months after first graduation (~8 graduates/month, 30% take, 6% churn) | Programming; review cadence | PL (W/E) |
| Hold deliverables | One written review per quarter with the re-capture; weekly room prompts (once open); stated operator touch per member | — | RULE |
| Open paid membership (option; Growing/Scaling; verified adults) | ~$29–59/month, only with budgeted moderation minutes | Moderation cost | PL (E) |
| Private at Scaling (**Parity Rule**) | Sold only when price per operator hour ≥ cohort revenue per care hour (≈$1,250–1,400 at Scaling). In practice an async-first seat at ~$10k+, or no Private | Care minutes | RULE (D) |
| Starter Path | A free sequenced path (weeks 1–4 and 5–8, logs, self-checks, a re-entry trigger); a low-cost tool of $27–97 named once; human touches templated (no free live group) | — | PL |
| Self-Serve System (the Starter tool's upgrade, after ~20 graduates) | ~$97–297 one-time: tools (logs, capture standard, self-review prompts, walkthroughs), not the stall taxonomy's decision rules. Its optional review is a Decision Assessment | Stall taxonomy; proof library | PL (E) |
| Payment plans | ≤3 installments, all due inside delivery. Premium 0–5% (processing + expected leakage) stated as a total. Your own installments only: no third-party lenders or buy-now-pay-later, since the affordability question rules out new credit (where local law treats installment plans as consumer credit, that's a Risk Register flag for professional advice). Each installment at or below about a third of monthly take-home. Cancel-forward after the fit window. No plan after a fit-check signal | Plan length vs delivery | RULE (M evidence) |
| Payment-plan sales lift | ~+20%, concentrated among buyers least able to absorb risk | Underwriting | EV (M) |
| Uncollected plan revenue (short plans inside delivery, with retries) | ~3–8% | Dunning; cancel-forward exits | PL (D/W) |
| Fit window | 14–21 days, full refund. The conversation is optional (a written request is enough), feedback-only, with no re-pitch | — | RULE |
| Service guarantee | Every review inside the stated turnaround (e.g., 48–72 h), the written week-6 read, the week-12 re-assessment, and the Hold and Private deliverables. Missed = credit or refund | — | RULE |
| Week-6 exit right | A client who did the work and asks to stop gets a pro-rata refund of undelivered weeks (~50%) | — | RULE |
| Week-12 non-response clause | When pre-agreed changeable-column markers (thresholds set at baseline; never adherence alone; never appearance change; never read from photos) haven't moved despite adherence ≥ the agreed threshold: cash partial refund ~25–50%, an honest verdict, and no Round Two offer. "Haven't moved" means no marker reached its threshold: one marker crossing it means the lever moves for him, so there's no refund. A client below the adherence threshold isn't covered; his week-12 read gives an honest verdict, and the week-6 exit right was his earlier route out | Marker design | RULE |
| Refunds + disputes | ~2–8% of revenue | Guarantee design; onboarding; affordability question | PL (E) |
| Dispute target | ≤1 per rolling 90 days early, each one investigated. Processors monitor ratios around ~1% of transactions, and at solo volume one dispute can breach a ratio, so track the count | Descriptor; terms; plan design | RULE (M) |
| Coaching market hourly rate | ~$230–300 | Internal sanity check only; never a buyer-facing anchor | EV (M) |
| Price–quality inference | Weak–moderate (r≈.3) | Familiarity with the category | EV (S) |
| Just-below price endings | Contested; small at best | — | EV (C) |

## C. Funnel & sales

| Metric | Range | Moves it up / down | Status |
|---|---|---|---|
| Engaged long-form views → raw email leads | 1–10 per 1,000 (plan 2–5 early) | Up: video-matched door, spoken mid-roll plus pinned ask, decision-stage topics. Down: generic freebie, teen-heavy traffic | PL (W/E) |
| Short-form views → leads | Far below long-form per view (plan ~0.1–1 per 1,000); its job is reach and hook learning | Profile routing; adult framing | PL (E) |
| Eligible-adult share of raw leads | ~30–70% | Minor share (packaging); door wording | PL (D/E) |
| Self-assessment start → lead | ~40% (≈65% completion) | Question count; value of the result | EV (W–M) |
| Landing-page conversion | All-traffic median ~6–7% across industries; email-sourced traffic converts several-fold higher | Warmth; plain language; mobile | EV (M) |
| Eligible lead → held fit conversation | 10–20% with a personal reply within hours and booking within 24–48 h | Reply speed; booking friction; book-first (log while waiting) | PL (E) |
| Held conversation → enrollment, before proof | 15–35% | Warmth; qualification; offer fit | PL (W) |
| Held conversation → enrollment, with proof | 25–45% | Proof; state routing | PL (W/E) |
| Eligible lead → Decision Assessment (≈60 days; overflow route) | 2–7% | Source; stage tag | PL (E) |
| Decision Assessment → program | 25–45% | Speed to slot; plan clarity; fit check | PL (E) |
| Warm offer-page visitor → enrollment (call-optional) | ~1–3% | Warmth; the Async Arc; proof | PL (E) |
| Share of enrollments with no live call | Early ~0–20%; Growing ~20–50%; Scaling ~50–70% | The Async Arc; tiering | PL (E) |
| Show rate by booking lead time | ~80% next day → ~60% at 14 days | Reminders; lead time; payment | EV (M) |
| Conversation-bind signs (Call Cap trigger) | Most weeks above ~6–8 held conversations; show rate sliding toward ~60%; more than half of held conversations ending no-fit; selling hours eating the content minimum | Door screening; book-first; Readiness Tags | RULE (THESES B5) |
| Lead-response speed | Contact within the hour ≫ later | — | EV (M, transfer) |
| **Call Cap** | Free fit conversations open up to ~6–8 held a week, reserved (by Readiness Tags) for uncertain or high-intent buyers; overflow → paid or async Decision Assessment. Judged on profit per operator hour per 100 eligible leads over ≥30 events | — | RULE |
| Month-3 Gate | **Volume leg:** fewer than ~15 held conversations by week 12 → a reach problem; fix sources (shift hours to short-form and replies; the Band A paid test). **Conversion leg:** fewer than 3 clients from 25+ held conversations → fix the offer or position before building further | — | RULE |
| Week-3 source check | If warm network plus replies produce fewer than 2 held conversations a week, shift ~2 h/week from long-form to short-form batches and permission-first replies | — | RULE |
| Fit-check signal share (paid-step applicants) | ~5–20% show at least one signal; most continue after a conversation; acute signals are rare | Prevalence; wording | PL (D) |
| Fit-check signal pause | No same-day payment; adjusted expectations in writing; ≥72 h cooling-off; no payment plan; fit window from day one of delivery. Checking or fixation → referral plus reading-only content | — | RULE |
| Pause route | Set by an endorsed distress item, "can't afford" (call, checkout, or plan step), or a fit-check pause. No sales sequence or date sends for 60–90 days, then re-permission. It records no reason | — | RULE |
| Category's hardcore audience under 18 | Majority in self-selected samples | Packaging; adult positioning lowers it | EV (W) |
| Decision points | Every assessed buyer meets one real decision point within ~2–4 weeks: the next monthly start (with its real seat cap) or an announced price step. Credit windows are **not** deadlines | Calendar design | RULE |
| Follow-up | Written recap within 24 h · one check-in on the agreed decision date · one close-the-loop message · then regular email only (subject to the pause route) | — | RULE |
| Early weekly numbers | Eligible leads · held conversations · enrollments + cash · pieces published · check-in completion | — | RULE |

## D. Delivery, adherence & retention

| Metric | Range | Moves it up / down | Status |
|---|---|---|---|
| Format effects in behavior-change trials | Individual ≈ group ≈ guided at equal intensity | — | EV (S in domain; transfer M–W) |
| Contact frequency | More contacts per week helps; the total number of sessions has little effect | — | EV (M) |
| Proactive encouragement vs self-help | Better outcomes and roughly half the dropout; on-demand-only support adds little | — | EV (M) |
| Progress monitoring → goal attainment | Moderate (d≈0.4); larger when recorded, reported, and reviewed | — | EV (S) |
| If-then plans | Smaller than headline figures after bias correction (≈0.15–0.35) | Format; rehearsal | EV (S that it shrinks; size C) |
| Habit automaticity | Median ~2 months; range from days to most of a year | Behavior complexity. **Never used to time outcomes** | EV (M) |
| Unguided completion | Very low (MOOCs ~3% overall; apps ~4% retained at day 15). Paying/verified MOOC learners ~46% (selection + commitment) | Human touch; deadlines; payment | EV (S/M) |
| Working alliance ↔ outcome | r≈.3 | — | EV (S) |
| Markers per client | 2–3 pre-agreed changeable-column markers, thresholds set at baseline (never adherence alone, never appearance change) | Goal; what his record can measure | RULE |
| Client check-in time | ~10 minutes a week to complete the weekly check-in | Instrument length; templates | RULE (D) |
| One combined group call | Until ~12–15 concurrent clients, then split by stage | — | RULE |
| Late entry into a running cohort | Through week 1–2 | — | RULE |
| Appearance capture cadence | Baseline, ~week 6, week 12, then quarterly. Behavior logged and reviewed weekly. The free pre-purchase baseline stays on his device | — | RULE |
| Continuity/community churn | 4–8%/month typical; 8–15% open and cheap; 2–3% curated premium | Price; programming | EV (W) |
| Lifetime value per client (before referrals) | ~$1.7–3.0k at opening prices; ~$2.6–3.8k at proof prices | Price; Round Two and Hold take; churn | PL (D) |
| Referred customers | More loyal and more valuable than other acquisitions | Plan acquisition without referrals | EV (M) |
| First testimonial ask | Never before the fit window closes, and never in the conversation where the week-6 exit right is available. The first process-testimonial ask comes at the first measured peak after the week-6 exit decision is settled (from about week 7), if his record shows progress | — | RULE |
| Refund timing | Paid within 7 days of the request (fit window, exit right) or of the week-12 verdict (non-response clause); the plan-usefulness refund within 7 days of the request | — | RULE |
| Non-responder share; recommendation mix; share told "you don't need Round Two" | Measured from the founding clients; published once there are ≥30 graduates (≥30 assessments for the mix) | — | RULE |

## E. Persuasion effect sizes (explanation only; never a promise, always a range)

| Mechanism | Size | Note | Status |
|---|---|---|---|
| Self-efficacy change → behavior | Largest tested belief lever (d≈0.4–0.5) | vs attitude ≈0.35–0.4, norms ≈0.35 | EV (S) |
| Stakes / fear appeals | Small–moderate overall (d≈0.2–0.3); depend on efficacy; threat alone does little | Contested for threat | EV (S/C) |
| Gain vs loss framing | Negligible overall difference | Frame for accuracy, not loss | EV (S) |
| Defaults | Robust, moderate–large (d≈0.6–0.7 in meta-analysis; smaller for consequential choices) | Why hidden defaults are banned | EV (S/M) |
| Nudges in general | Small after bias correction | Heterogeneous | EV (C) |
| Fresh-start landmarks | Goal pursuit rises after temporal landmarks; the evidence is for starting a goal, not for purchase timing | Monthly starts near real landmarks | EV (M) |
| Deferral effects (choice conflict; imposed deadlines) | "A second good option makes people wait" failed large replications; the headline evidence that imposed deadlines improve follow-through is weakened (a key study retracted in 2026). Treat both as contested | Real dates are justified by honesty and planning, never by a deferral effect | EV (C) |
| Inoculation / prebunking | Moderate protection against later persuasion attempts | Build the capture standard before publishing anti-grift content | EV (S/M) |
| Two-sided refutational messages | Small advantage over one-sided | Only when the counterargument is answered | EV (M) |
| Narrative persuasion | Small–moderate | Composites labeled | EV (M) |
| Underestimating compliance with direct asks | People expect roughly half the yeses they get | Ask everyone, privately | EV (M) |
| Peak-end memory | Final moments and peaks weigh heavily in retrospective judgment | Make the last fortnight the peak | EV (M) |
| "Free to refuse" phrasing | Small or none in low-bias studies | Insurance, not a lever | EV (C) |
| Correction backfire | Essentially none; effects small and fading | Repetition needed | EV (S) |
| Scarcity | Small, heterogeneous | Supply-based works best for experiences | EV (C) |
| Cost transparency | Meaningful lift in field tests | Comprehensible cost story; one domain | EV (M) |
| Range vs point claims | Conditional: ranges win when buyers compare formats | Tight ranges; process facts as points | EV (W–M) |
| Loss aversion | λ≈1.3–2.0 | Smaller at low stakes | EV (C size) |

## F. Ecosystem (teach principles over dated specifics)

| Metric | Range | Moves it up / down | Status |
|---|---|---|---|
| US adult reach | YouTube ~84% (≈95% of 18–29s); Instagram ~50%; TikTok ~37%; X ~21% | Age | EV (S) |
| YouTube impressions CTR | Most videos 2–10% | Surface; audience warmth | EV (M) |
| Organic engagement per post (median) | TikTok ~1.7%; Instagram ~0.4%; X ~0.03% | Averages run higher than medians | EV (M) |
| Content cadence | Early: the Honest Answer, then long-form every other week + 4–7 native short-form/week + result email and welcome flow. Growing: 3/month long-form + weekly email. Scaling: 2–3/month. Batch filming every two weeks | Editing budget | RULE |
| Default short-form platforms | Shorts first (it feeds the long-form channel), Reels second (it feeds the Instagram router). TikTok only if eligible-adult yield by source proves out | Minor exposure; yield | RULE (D) |
| Email clicks per delivered | 2–5% (deep niches higher) | One link; stage match | EV (M) |
| Unsubscribes per send | 0.1–0.4% | Frequency; relevance | EV (M) |
| Spam complaints | Target < 0.1%; never ≥ 0.3% | Pressure; dormant segments | RULE (S) |
| Welcome flow vs broadcast (per recipient) | Several-fold more clicks and orders | E-commerce transfer | EV (M/W) |
| Lead-age cohorts for revenue | 0–60 · 61–180 · 181–365 days; re-permission, don't delete | — | RULE |
| Promotion sends per start date | One announcement + one reminder, engaged segments only, never to paused leads | Launch Line | RULE |
| Paid lead cost (Meta, broad benchmark) | ~$25–30 per raw lead → ~$36–100 per eligible lead | Objective; health-adjacent classification removes optimization | EV (M) / D |
| Band A paid adult reach test | Default at months 3–4 once destinations pass the Destination Rule: ~$300–1,000/month pushing proven pieces to adults, judged against a holdout and the maximum affordable cost per eligible lead | Band; yield | RULE (D) |
| Minimum meaningful conversion-optimized test | ~$1–3k/month per ad set | Event volume | PL (D) |
| Search clicks when an AI summary appears | Non-branded informational queries: roughly halved. Branded/navigational: smaller effect, sometimes positive | Query type | EV (M) / EV (W) |

## G. Buyers & law

| Metric | Range | Note | Status |
|---|---|---|---|
| Core buyer | 19–32; default protagonist 24 (Dan) | Optimizer 25–35, including over-30s by state | RULE |
| Buyer income (US full-time) | Men 20–24 ≈ $42k/year gross (take-home ≈ $2.8k/month); ages 25–34 ≈ $59k/year (take-home ≈ $3.9k/month) | — | EV (S); take-home D |
| Price in months of take-home pay (20–24 / 25–34) | $2.4k ≈ 0.86 / 0.61 · $2.8k ≈ 1.0 / 0.71 · $3.1k ≈ 1.1 / 0.79 · $3.5k ≈ 1.25 / 0.89 · $3.9k ≈ 1.4 / 1.0 · $4.5k ≈ 1.6 / 1.14 | The cash ceiling is measured here | PL (D) |
| **Affordability question** (canonical; before every paid step, in every channel) | **"Is this comfortable from your own income or savings, without new credit or buy-now-pay-later?"** | "No" → Starter Path + pause route. Money that isn't his → Starter Path | RULE |
| Age of majority | 18 in most US states; 19 in two; 21 in one state and one territory | The door asks "legal adult where you live" | EV (S) |
| Appearance-concern prevalence | General population ~2%; far higher among appearance-change seekers (roughly 5–20% by setting) | Fit check before any paid step | EV (S, analog) |
| Statutory cancellation (UK/EU consumers) | ~14 days for online services, with rules on early start | Legal is minimal: one flag | EV (S) |

## H. Operating rules with numbers

| Rule | Setting | Status |
|---|---|---|
| Small numbers | A ledger range yields to the operator's own ratio only after ~30 events. Change course only when a ratio sits outside the range for two consecutive 30-event windows, or on strong qualitative signal | RULE |
| Warm network and early replies (labeled source) | ~2–8 held conversations/month in months 1–3 (disclosed), decaying to ~1–4 by month 9 (including referrals). Replace after ~30 events | PL (E) |
| Speed to lead | Personal reply to every adult door completion within hours; booked within 24–48 h; reminded; held. Automate when replies exceed ~1 h/day | RULE |
| Founding Sprint targets | 3–6 held conversations/week. Honest expectation: 0–2 clients in month 1, 2–6 by month 3 depending on sources | PL |
| Seat caps | Set monthly from measured care minutes (Seat Math), including the Hold and Private, so client work cannot eat the protected content minimum | RULE |
| Content minimum | Never below ~5 h/week at any stage; the A4 allocations are protected | RULE |
| De-scoping order (weeks past 25 h) | Cut in order: (1) building beyond the protected line and experiments → (2) extra platforms (X first, then native Instagram; keep routing) → (3) short-form above its weekly minimum → (4) long-form above the minimum cadence → (5) new conversations (pause booking; tighten the Call Cap). Never cut review turnaround, milestones, Hold/Private deliverables, the content minimum, or the Operator Review. Two weeks at step 5 means capacity binds: raise price, cap seats, template review | RULE |
| Routing help (from Growing; task-billed per batch) | Moderates public comments against the published policy and sends one templated door link. Anything revealing a minor, distress, a purchase question, or client content goes to the operator. No view of check-in content or fit-check answers | RULE |
| Build queue (ordered by hours saved per hour invested) | Templated review → the Decision Assessment template → the Async Arc → Round Two and Hold terms → Private deliverables → the Self-Serve System | RULE |
| Cash flow | Open the payment processor early with small charges; hold ~2–3 months of costs in reserve; keep other income until trailing 3-month profit covers personal costs | RULE |
| Starts | Monthly entry into a standing group from the founding group onward, pinned near real landmarks; expect New-Year intent | RULE (EV M landmarks; W seasonality in this niche) |
| Private | Founding seats while minutes are spare; at Scaling only under the Parity Rule | RULE |
| Paid self-serve products | Only after ~20 graduates have produced proof and a stall taxonomy | RULE |
| The Dated Record | From month 1: publish the pre-commitment (what, at what sample size, on what schedule) and keep a dated log of process metrics (check-in completion, turnaround kept, claim rate, fit declines in aggregate). Outcome ranges with denominators first join the log at the proof milestone (≥10 graduates), labeled as a small sample; from ≥30 graduates they become the standing published log, with the non-responder share | RULE |
| Guardrails (always) | Refund + dispute count (rolling) · complaint rate · fit-check signal and decline counts (aggregate) · refunds/exits among signal-flagged enrollees · promotional sends to paused leads (target zero) · affordability "no" share · non-responder share · review turnaround kept | RULE |
