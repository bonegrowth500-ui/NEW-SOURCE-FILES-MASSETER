# Step 3 tracker (orchestrator's working file)

Process per module: drafter agent (3.1 + 3.2) → fresh critic agent writes `critiques/NN.md` (3.3) → SendMessage to the same drafter to rebuild + write `summaries/NN.md` (3.4) → orchestrator runs `tools/audit.py`, reviews flags, registers terms/ledger proposals, commits and pushes (3.5).

Rounds = Parts (SPEC §9: one blueprint phase per round; no approval gates). Round N+1 starts when every module in round N has passed 3.5.

| Module | File | Drafter agent | Critic agent | Status |
|---|---|---|---|---|
| 01 | 01-the-whole-business.md | a66743a4358c63e43 | a4dc9005b9562c418 | ✅ 3.5 passed (7,463 w) |
| 02 | 02-the-buyer.md | a6e6b16066686151e | aa9f016d84771f742 | ✅ 3.5 passed (7,394 w) |
| 03 | 03-the-honest-position.md | ad8557f03357ac575 | a7e11a17c8e86f9d7 | ✅ 3.5 passed (7,651 w) |
| 04 | 04-offer-architecture.md | ae789f43cf5fcbf02 | a8c8d6b0183699bf1 | draft done (7,374 w) → critique |
| 05 | 05-the-door.md | ac25cee9328b86fba | aae990a7bb75afe21 | critique done (2 blocking, 9 major) → rebuilding |
| 06 | 06-the-program.md | a7ee757e20232197b | a50cca6d05e5b9053 | critique done (0 blocking, 16 major) → rebuilding |
| 07 | 07-price-plans-and-promises.md | a221eb1ab3ec932ae | a380515d49553e60b | critique done (1 blocking, 16 major) → rebuilding |
| 08 | 08-real-dates.md | abac773561fc0f762 | a27f5c6b241ee3e4c | critique done (0 blocking, 15 major) → rebuilding |

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
