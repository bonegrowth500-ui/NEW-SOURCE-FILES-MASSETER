# Step 3 tracker (orchestrator's working file)

Process per module: drafter agent (3.1 + 3.2) → fresh critic agent writes `critiques/NN.md` (3.3) → SendMessage to the same drafter to rebuild + write `summaries/NN.md` (3.4) → orchestrator runs `tools/audit.py`, reviews flags, registers terms/ledger proposals, commits and pushes (3.5).

Rounds = Parts (SPEC §9: one blueprint phase per round; no approval gates). Round N+1 starts when every module in round N has passed 3.5.

| Module | File | Drafter agent | Critic agent | Status |
|---|---|---|---|---|
| 01 | 01-the-whole-business.md | a66743a4358c63e43 | a4dc9005b9562c418 | ✅ 3.5 passed (7,463 w) |
| 02 | 02-the-buyer.md | a6e6b16066686151e | aa9f016d84771f742 | ✅ 3.5 passed (7,394 w) |
| 03 | 03-the-honest-position.md | ad8557f03357ac575 | a7e11a17c8e86f9d7 | ✅ 3.5 passed (7,651 w) |

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
