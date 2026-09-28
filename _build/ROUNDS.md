# Step 3 tracker (orchestrator's working file)

Process per module: drafter agent (3.1 + 3.2) → fresh critic agent writes `critiques/NN.md` (3.3) → SendMessage to the same drafter to rebuild + write `summaries/NN.md` (3.4) → orchestrator runs `tools/audit.py`, reviews flags, registers terms/ledger proposals, commits and pushes (3.5).

Rounds = Parts (SPEC §9: one blueprint phase per round; no approval gates). Round N+1 starts when every module in round N has passed 3.5.

| Module | File | Drafter agent | Critic agent | Status |
|---|---|---|---|---|
| 01 | 01-the-whole-business.md | a66743a4358c63e43 | a4dc9005b9562c418 | critique done (2 blocking, 10 major) → rebuilding |
| 02 | 02-the-buyer.md | a6e6b16066686151e | aa9f016d84771f742 | draft done (7,559 w) → critique |
| 03 | 03-the-honest-position.md | ad8557f03357ac575 | a7e11a17c8e86f9d7 | critique done (0 blocking, 11 major) → rebuilding |

## Decisions made during Step 3
(terms registered, LEDGER additions, rule clarifications)
- R1: LEDGER A5 "Eligible leads needed" recomputed from LEDGER's own eligible lead → client range (1.5–7%): $25k ≈ 120–285 at 3–7% (≈570 at 1.5%); $50k ≈ 185–435 at 3–7% (≈870 at 1.5%). Tell 01's drafter at rebuild (draft used the stale 100–275).
- R1: LEDGER H Dated Record: process metrics from month 1; outcome metrics once ≥30 graduates (resolves FRAMEWORKS vs LEDGER wording).
- R1: "the null-result stance" registered as ○, owner 03 (16 recaps).
- R1: BUSINESS §6 membership wording aligned with LEDGER B (never the engine; optional add-on from Growing).
- R1: style-sheet Name | Brand row repaired.
- R1 note: sample-v2's Cole placeholders were adjusted by 01's drafter to fit Band B; the sample stays a voice reference, not a number source.
- R1: BUSINESS §2 'the line on minors' → 'the line on vulnerability (no selling to minors)' (minors sit under the vulnerability line).
