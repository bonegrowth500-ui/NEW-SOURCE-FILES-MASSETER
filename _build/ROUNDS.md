# Step 3 tracker (orchestrator's working file)

Process per module: drafter agent (3.1 + 3.2) → fresh critic agent writes `critiques/NN.md` (3.3) → SendMessage to the same drafter to rebuild + write `summaries/NN.md` (3.4) → orchestrator runs `tools/audit.py`, reviews flags, registers terms/ledger proposals, commits and pushes (3.5).

Rounds = Parts (SPEC §9: one blueprint phase per round; no approval gates). Round N+1 starts when every module in round N has passed 3.5.

| Module | File | Drafter agent | Critic agent | Status |
|---|---|---|---|---|
| 01 | 01-the-whole-business.md | a66743a4358c63e43 | a4dc9005b9562c418 | ✅ 3.5 passed (7,463 w) |
| 02 | 02-the-buyer.md | a6e6b16066686151e | aa9f016d84771f742 | ✅ 3.5 passed (7,394 w) |
| 03 | 03-the-honest-position.md | ad8557f03357ac575 | a7e11a17c8e86f9d7 | ✅ 3.5 passed (7,651 w) |
| 04 | 04-offer-architecture.md | ae789f43cf5fcbf02 | a8c8d6b0183699bf1 | ✅ 3.5 passed (7,561 w) |
| 05 | 05-the-door.md | ac25cee9328b86fba | aae990a7bb75afe21 | ✅ 3.5 passed (7,425 w) |
| 06 | 06-the-program.md | a7ee757e20232197b | a50cca6d05e5b9053 | ✅ 3.5 passed (7,362 w) |
| 07 | 07-price-plans-and-promises.md | a221eb1ab3ec932ae | a380515d49553e60b | ✅ 3.5 passed (7,371 w) |
| 08 | 08-real-dates.md | abac773561fc0f762 | a27f5c6b241ee3e4c | ✅ 3.5 passed (7,443 w) |
| 09 | 09-the-founding-phase.md | a4d1beee624d836ef | a22bba410642a677c | ✅ 3.5 passed (7,593 w) |
| 10 | 10-lifetime-value.md | a5ebf882ac6f073ee | af28fb6227a00d9d0 | ✅ 3.5 passed (7,606 w) |
| 11 | 11-the-operating-week.md | ad69db360e41d53c3 | abbb51cf9aabb080d | ✅ 3.5 passed (7,664 w) |
| 12 | 12-growth-decisions.md | a5c76ed0875a1df40 | a951a3169f17d9330 | ✅ 3.5 passed (7,614 w) |
| 13 | 13-the-premium-lane-and-the-road-to-50k.md | af1c784364515bae9 | ab0d36721ab429764 | ✅ 3.5 passed (7,611 w) |
| 14 | 14-the-belief-chain.md | a89abc2dfc2ee7182 | a8010ad9e8a0be949 | ✅ 3.5 passed (7,589 w) |
| 15 | 15-trust-without-credentials.md | a8333252e33aa0f27 | ab6ffdd5f62788935 | ✅ 3.5 passed (7,519 w) |
| 16 | 16-evidence-that-persuades.md | a69517812edf19da3 | a721610947ef123b4 | ✅ 3.5 passed (7,557 w) |
| 17 | 17-identity-and-commitment.md | a731ca3f0c80dc3c6 | a2fd5d01abb28e5b3 | ✅ 3.5 passed (7,601 w) |

## Decisions made during Step 3
(terms registered, LEDGER additions, rule clarifications)
- R1: LEDGER A5 "Eligible leads needed" recomputed from LEDGER's own eligible lead → client range (1.5–7%): $25k ≈ 120–285 at 3–7% (≈570 at 1.5%); $50k ≈ 185–435 at 3–7% (≈870 at 1.5%). Tell 01's drafter at rebuild (draft used the stale 100–275).
- R1: LEDGER H Dated Record: process metrics from month 1; outcome metrics once ≥30 graduates (resolves FRAMEWORKS vs LEDGER wording).
- R1: "the null-result stance" registered as ○, owner 03 (16 recaps).
- R1: BUSINESS §6 membership wording aligned with LEDGER B (never the engine; optional add-on from Growing).
- R1: style-sheet Name | Brand row repaired.
- R1 note: sample-v2's Cole placeholders were adjusted by 01's drafter to fit Band B; the sample stays a voice reference, not a number source.
- R1: BUSINESS §2 'the line on minors' → 'the line on vulnerability (no selling to minors)' (minors sit under the vulnerability line).
- R1: prevalence ruling for 02: LEDGER G (clinical analog, reason the Fit Check exists) vs LEDGER C row 'fit-check signal share' (what the operator sees: ~5–20how a signal; most continue; acute rare). Never convert G into a claim about applicants' condition.
- R1 (from 01's rebuild): LEDGER A2 stage volume signals redrawn so the $25k configuration reads as Scaling: Growing ~50–150 leads / ~15–25 concurrent; Scaling ~150+ leads / ~25+ concurrent or a waiting list. sample-v2 Stage Map updated.
- R1: proof milestone vs Dated Record: outcome ranges first join the log at the proof milestone (≥10 graduates) labeled as a small sample; standing published log from ≥30.
- R1: "eligible lead → enrollment" is the single conversion term (VOICE §4 one-term table; LEDGER standardized).
- R1: LEDGER additions approved from 01: held conversations at the configuration (~8–17/month at $25k; ~9–18 at $50k); engaged long-form view equivalent (~35–475k/month at $25k; ~55–725k at $50k); conversation-bind signs row (Call Cap trigger).

## Integration notes for Step 4 (seams to fix in 4.1/4.3)
- 03 glosses "your door" as "the self-assessment every lead starts with"; harmonize door glosses with 05's definition (self-assessment is the door's first step).
- 16 §6 recaps the null-result stance with 03's gloss; 19 reuses 03's spoken Honest Answer verbatim.
- R1: "men over 30" → "men past the core band (over ~32)" in BUSINESS §2 and brief 02 (core band runs to 32; Optimizer 25–35 by state).
- R1: audit.py no longer counts the Quick Reference "Leans on:" line toward (Module N) density.
- 02 integration note: 01 and 03 should recap Dan's door answer, the say-back, and Theo's route rather than re-run them.
- R2 (from 08): deferral evidence downgraded to contested (choice-conflict replications failed; a key deadline study retracted in 2026). New LEDGER E row; THESES P10 and persuasion SYNTHESIS T14 annotated. Real dates rest on honesty and planning, never on a deferral effect. Fresh-start evidence is for starting a goal, not purchase timing.
- R2: FRAMEWORKS Launch Line definition now has all five conditions (matches STANDARD §6 and HOUSE_STANDARD).
- R2 (from 06): LEDGER D additions approved: markers per client 2–3 (RULE); client check-in time ~10 min/week (RULE D).
- R2: marker DESIGN is owned by 06 (MAP/FRAMEWORKS win over DECISIONS R2 wording); 07 owns the clauses and runs the Collectability Test on the markers.
- R2: Round Two re-captures follow Round Two's own weeks 6 and 12; everyone else goes quarterly after week 12.
- R2 (from 05): 'the signal pause' registered as ○ (owner 05). sample-v2 show-rate bind sign aligned to LEDGER C ('toward about 60%'). Fit Check at every paid step (R2 beats THESES E13).
- R2 (from 07): payment plans are the operator's own installments only; no third-party lenders or BNPL (the affordability question rules out new credit). Local consumer-credit classification is a Risk Register flag (11). LEDGER B row updated. Price Step announcements ride inside the start announcement (08's send rules).
- R2 (from 04): the paid Starter tool is named only to not-now and not-a-fit buyers; never after 'I can't afford it', never when the money isn't his; a fit-check pause gets a reading-only version. Applies to 19, 20, 26 scripts and sequences.
- R2 (from 06 critique): non-response clause defined: 'haven't moved' = no marker reached its threshold (one crossing = lever moves, no refund); below-adherence clients not covered (honest verdict; week-6 exit right was the route). Markers never read from photos; binary did-it items count as adherence. Path and Timeline Card: total cost over the first [6–9] months with a separate full-intensity Round Two line; the 'you don't need Round Two' share published at >=30 graduates. 07's clause wording must match.
- R2 (from 05 critique): checkout enforces before payment (attestation, affordability question, Fit Check tier 2 before the pay button; pause tag blocks checkout; signal blocks same-day payment; BNPL/third-party financing off). Free-call booking form shows the public price range and asks the affordability question ('no' → free Starter Path + pause route, no call). Minor discovered after the fork: immediate exit to the education lane, delete data, refund anything paid. Default sample plans never recommend Program Async (Scaling-only, 13).
- R2 (from 07 critique): first testimonial ask moved off the week-6 exit conversation to the first measured peak after the exit decision (from ~week 7) — LEDGER D row and briefs 09/16 updated; 22 must follow. New LEDGER B row: refunds paid within 7 days of request/verdict. Installment cap (≤3 × ≤⅓ take-home) binds: ~$2.8k plan cap at 20–24; above that, upfront from income/savings or a later start. Failed payment: reminder + retry, grace, delivery pauses, no fees/collections. Price Steps stay inside ledger bands; beyond the proof band is 13's.
- R2 (from 08): LEDGER C 'Late entry: through end of week 2; that last day to join is the decision point'; LEDGER F send timing: announce on previous start's day, remind the week before, both dates on every send.
- R2 (from 04 critique): Starter tool ($27–97) is a paid self-serve product → arrives with the ~20-graduate trigger; before that the Starter Path is free and tool-free. Re-entry trigger is buyer-controlled, never a money condition. LEDGER B + BUSINESS updated.

## Integration notes (continued)
- 19, 20, 25, 26 must write call-heard answers to the same tags, block checkout on the pause tag, never send abandoned-cart email to paused buyers, and delete + refund late-found minors (05's rules).
- Theo gets a 'don't buy' sample plan in 05 but a Program recommendation in 03: events are self-contained, but check plausibility in 4.1 (consider another composite for 05's sample).
- 18–20 and 27 recaps of the Path and Timeline Card use its [9]-month total-cost horizon.
- 02 §5 says 'nearest start after it'; 08 offers the next start first. Harmonize in 4.3.
- 19's written recap must omit the credit (08 ruling: the credit appears once, as a stated term, in the written plan).
- R2 (from 06): service guarantee covers operator review errors (corrective weeks free, never a paid block); full-intensity Round Two priced as a Program only when the misdirection came from outside the plan, disclosed on the Card. LEDGER B updated; 07 and 10 must follow.
- R2 (from 04 final): fixed Module 2 L182 money-based re-entry ('when it's comfortable…') → buyer-controlled re-entry ('the door opens again whenever he writes back'). Told 07: fit-paused buyers get the reading-only Starter Path.
- R2 (07 final): failed-payment grace period 7 days; non-response share fixed per start inside 25–50% = largest the reserve covers if the whole start claimed, stated in the Expectation Document (LEDGER B).
- R3 round (from 11): LEDGER A4/A5 + BUSINESS $50k week corrected to ~20.25 h (~21–21.5 with 1–2 Private seats at parity); lines never summed to 21. New LEDGER H rows: live windows 2–3/week; no-show rule (one templated rebooking, second miss releases the slot, no chasing). Module 06 Expectation Document fixed: automated reminders for scheduling; no one but the operator reads or answers client messages. 13 told to say 'about 20–21 hours'.
- R3 round (from 13): A4 $50k review line corrected to 4.0 h (22×7 + 14×6 min) → $50k week ~20.5 h (~21–22 with 1–2 Private seats at parity); model4.py aligned (20.55 h). New LEDGER rows: Private hours per 12-week seat (~14–15 with weekly calls; ~7–8 async-first); age band at intake (18–24/25–34/35+, aggregate only). Brief 09 stage note: Program Async is Scaling-only (pilots, not founding phases).
- Integration: 06's week-12 table cell for a below-adherence client whose marker moved (not covered by the clause; honest read; Round Two only on measured momentum). 05 intake adds the age-band item (G row).
- R3 round (11 critique): Cole = right reads, Reid = misreads (composite roles enforced); Cole starts templating at month 11 (Module 1). Routing help hides face-rating requests silently; distress/minor/purchase/client content → operator at once. Risk Register stays six flags; testimonials/endorsements fold into the claims-and-advertising flag.
- R3 round (from 12): Module 03 (passed) put all outcome ranges at 30 graduates; sent 03's drafter a surgical fix to align with R3-4 (first ranges at the proof milestone as a labeled small sample; standing log at 30).
- R3 round (from 10 critique): LEDGER D rules added: measured momentum (adherence ≥ threshold + ≥1 marker still improving across its last two readings); Round Two repeats (once by default; second only on its own measured momentum and his ask); corrective weeks for review errors (weeks lost, capped at 6, free, logged in the claim rate). Round Two below parity at Scaling (~$990/care h) → sold while minutes are spare, Seat Math caps it. $50k Hold 0.6 h = ~0.4 h templated quarterly reviews + ~0.2 h room moderation.
- R3 round (13 critique): $50k told with LEDGER A3's middle case (tops ~$14k/$28k/$34k/$35k by band) → $50k is the good case (C–D, or B with a paid lever; years 2–3). Age packaging addressed as an income proxy (legit only with the affordability gate + Program Async under the younger ceiling; never income signals). No downsell after a 'no': tiers shown premium-first before the question; question asked about his pick. Parity benchmark defined by stage/price (~$800 Growing proof band → ~$1,250–1,400 Scaling ceiling); Hold and Round Two below parity at Scaling.
- R3 round (09 critique): source label = booking source; Month-3 Gate reads volume and conversion, not bands (band unknowable at m3; paid test is the default fix when volume fails); conversion-leg fix order (replay calls → position/Card/price → one change at a time); founding price never extended; composites never cross a House Standard line, even as contrast (Reid's misreads are strategic).
- R3 round (12 critique): Small Numbers Lie operationalized: event = one unit of a rate's denominator; window = time to ~30 of them; rates under ~10% are read through their stages (lead→held 10–20%, held→enrollment 15–45%, no-call route) or after ~30 enrollments. Leak Trace ranks by profit lost this month per route (free call / assessment / no-call); back-end joints by lost LTV per graduate.
- R3 round (10/11 final): 'measured momentum' registered ○ (owner 10). LEDGER B derived row: back-end revenue per care hour (Round Two ≈$990 at $25k; Hold ≈$680 at $25k, ≈$1,190 at $50k; Hold parity only near $72–80/month templated). LEDGER H speed-to-lead automation trigger aligned with the design-week line (template the first reply you approve after two weeks over the line). Module 06: review disclosure prose (no message routing) and the Card's full-intensity line (outside-the-plan misdirection priced; your review miss = free corrective weeks). audit.py skips Leans on/Do this month lines in rhythm checks.
- R3 round (13 final): parity ruling corrected: Round Two ≈$990/care h at $25k (below) but ≈$1,600 at $50k (above, from volume + templating); the Hold just below at both until ~$72–80. model4.py $50k configuration aligned with A5 (8 Program, 45 Hold members, no Private: $56.3k → $43.9–47.3k). New derived LEDGER rows: Private parity prices (async-first ≈$10k; weekly-call ≈$18–20k); two tiers vs one (≈$3k more profit at $50k volume).
- R3 round (09 final): FRAMEWORKS Founding Sprint definition updated: five booking-source labels (warm network, replies, Permission-First Replies, native short-form, long-form and search); the founding page and speed to lead serve all sources. Round Two's first cohort = founding graduates (Early).
- Integration: 01 sends Cole's [40] warm messages in month 2; 09 has them in weeks 1–2. Harmonize in 4.3.
- R3 round (12 final): Price Step gate: close rate read over the 30 held conversations since the last step landed; until 30 exist, filling starts carry the step alone; one readable window below range holds the next announcement, two send the work to the call. Call Cap fires on volume (most weeks > 6–8 held, selling eating content); show rate/no-fit at lower volume = fix screening (05), not a cap. LEDGER B and C updated; Modules 01 (checklist item 4), 05 (§3 and Stage Notes), 07 (§3 and worksheet) aligned.
- R4 round (from 17): FRAMEWORKS Week-Zero Baseline covers no-call buyers (first seven logged days). Integration: 04 §5 says a baseline 'taken while he waited' counts, but 05 moved capture instructions to the recap/plan; harmonize in 4.3.
- R4 round (from 14): LEDGER E row added: mental contrasting (moderate, likely inflated, one research group; EV M/C). FRAMEWORKS Belief Chain: a stop rule can mark a link you never work on.
- R4 round (from 15): no stored tag records fit/insecurity answers; result-page branches computed at render time; all automated sequences follow Dignity Route limits by default (no dignity tag). Checking signal = 'many times a day' at both tiers; regular checking short of it = Dignity Route trigger. Added to DRAFTING standing rulings.
- R4 round (from 16): Integrity Levels defined (Matched → In context → Placed) in FRAMEWORKS. Proof Portability Gradient now includes contextualized organic short-form clips with range + denominator on screen (per STANDARD notch 5 and R1-29); 24 and 27 must follow.
- R4 round (17 critique): status is never contingent on not using a refund right (founding status = joined + kept the practice; alumni status = a record fact of graduation, never framed as a cost of exiting; exits never mentioned in the room). Dignity Route: no missed-social-moment reflection, even of his stated goal. The free log is a head start, never a gate.
- R4 round (14 critique): stop-rule endings leave no record beyond 'stopped: stop rule' and never feed content planning or the Conversation-to-Content Loop. 'Misdirected' verdict requires a named lever + documented correction + early movement at the next reading; otherwise 'doesn't move' stands (no relabeling to sell time).
- R4 round (15 critique): education-lane copy never implies minors can buy later or after a visit (no 'first', no 'come back', no door route); costly signals measured from the grifter's side with buyer-checkable verification.
- R4 round (17 final): Module 06 boards open only after the fit window; Module 05 'Sometimes' answers get the render-time dignity branch (unstored). 22 must adopt alumni status as a record fact (Round 5 prompt).
- R4 round (16 critique): testimonial asks never in any refund-deciding conversation (week-6 exit, week-12 verdict) and never of a client who claimed a refund (LEDGER D). No client stories in month 1. No universal 'your stall isn't genetic' claims.
- Integration (5.1): MAP's Early Fast Path schedules Transition stories earlier than R3-11 allows; fix when writing the Intro.
- R4 round (14 final): bounded-agency gloss fixed in FRAMEWORKS and Module 03 ('measurement shows what's moving', never a ceiling read off his face). LEDGER E rows: positive fantasy vs expectation (M, one group); sustained exposure to corrections (M/W, one six-month field experiment). LEDGER H: Canon rotation rule (claim #1 on every entry surface; each claim every ~4–6 weeks in the same words; a resurfacing myth's claim first for ~2 weeks). 19, 20, 26 quote canon claims verbatim; 26 adopts the rotation; 05, 06, 21 adopt the 'misdirected' standard.
- R4 round (15 final): Module 05 table clarified: distress 'yes, most days' or checking 'many times a day' (no checking 'most days' signal).
- R4 round (16 final): LEDGER D rules: testimonial asks per client (≤2; a no is final; scoped consent; never ghostwritten); teardown cadence (quarterly + on recurring door-answer claim patterns). FRAMEWORKS Integrity Levels wording aligned (compare / show / claim).
