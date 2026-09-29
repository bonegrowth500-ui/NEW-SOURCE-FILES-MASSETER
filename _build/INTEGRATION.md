# INTEGRATION KIT — Step 4

The step, as planned:
- **4.1 Cover-to-cover read:** read the whole thing in order as the target reader, fixing seams, repetition, contradictions, and drifting terminology.
- **4.2 Depth upgrade:** find each module's weakest part and rebuild it to the level of its strongest.
- **4.3 Reconciliation:** make sure numbers, frameworks, and cross-references between modules all agree.
- **4.4 The 9-month build plan:** written last, putting everything into a month-by-month build, then run through the same five passes.

Sequence: 4.1 runs by Part (one reader-fixer per Part, in parallel). The orchestrator arbitrates cross-Part issues and sends each fix to the Part that owns the file. 4.2 goes to the same agents. 4.3 goes to fresh reconcilers by Part, plus scripted global checks. 4.4 is Module 28's five passes.

Parts: I (01–03) · II (04–08) · III (09–13) · IV (14–17) · V (18–22) · VI (23–27).

## Load (every Step 4 agent, in this order)
1. `_build/SPEC.md`, `_build/VOICE.md`, `_build/voice/sample-v2.md`, `_build/STYLE.md`.
2. `_build/HOUSE_STANDARD.md` and `_build/STANDARD.md`.
3. `_build/DRAFTING.md`, all of it. Its **Standing rulings** section overrides older wording everywhere, including in modules drafted before a ruling existed. That makes it the main seam checklist.
4. `_build/DECISIONS.md` section R3 (R3-1 to R3-44).
5. `_build/MAP.md`, its owners and **Boundary rules**; `_build/FRAMEWORKS.md`; `_build/voice/style-sheet.md`.
6. `_build/LEDGER.md` and `_build/BUSINESS.md`.
7. All running summaries, `_build/summaries/01.md` to `27.md`.
8. This file.

## 4.1 — What to fix
Read your Part's modules fully, in order, as the target reader: a solo operator, early stage, 20–25 h a week, smart and skeptical, wanting mastery. Before your Part, read the last module of the previous Part; after it, read the first module of the next Part. Both are read-only and are there to check the handoffs.

1. **Seams.** A standing ruling or DECISIONS R3 entry that an earlier-drafted module hasn't caught up with. Two modules describing one mechanism differently. A recap that no longer matches its owner.
2. **Repetition.**
   - Teaching another module's owned item beyond a two-sentence recap (MAP owners and Boundary rules).
   - The same story, example, script line, or composite beat told again.
   - The same point made twice inside one module.
   Cut to a recap plus a pointer. The owner keeps the full treatment.
3. **Contradictions.** Facts, rules, sequences, timelines, prices, windows, and cast facts. When a number disagrees with LEDGER, LEDGER wins; fix it now if you see it (4.3 does the full sweep).
4. **Drifting terminology.**
   - Every registered term uses its FRAMEWORKS name and gloss, glossed at first use in each module (VOICE).
   - Use one term per concept (VOICE's one-term table).
   - No synonyms for owned terms, and no house noun before its gloss.
5. **Cast continuity.**
   - Fixed ages and states: Dan 24, Struggler; Theo 26, Burned Struggler; Adrian 31, Optimizer; Sam 22, Ambivalent; Maya 28; Jordan 16, a minor, education lane only; Cole, the operator who makes right reads; Reid, strategic misreads only, never crossing a House Standard line.
   - Each composite carries its label at first appearance in each module.
   - Events stay plausible across modules. The same person shouldn't get contradictory verdicts or timelines unless a module says why.
6. **Flow.**
   - The opening lands the shift.
   - Nothing depends on a later module without a pointer.
   - **Leans on:** lists what the module actually uses.
   - Section openings don't preview, and transitions don't restate.
7. **The integration notes for your modules** (below).

Rules:
- **Edit only your Part's module files** (and their summaries, if a change alters what a summary says).
- Log cross-Part problems; don't fix them.
- Keep every module inside 6,300–7,700 words. Removing repetition should lower counts, and nothing grows without reason.
- Keep the audit clean: `python3 _build/tools/audit.py <file>` shows 0 FAIL after your edits.
- Don't rebuild sections for depth (that's 4.2). Do note where depth is weakest.
- Don't commit.

## Canon (Module 14), for verbatim checks
1. "There's no good evidence that habits change the shape of an adult's bone, and I don't sell that. Some things are debated, and I'll tell you where the evidence is thin. A lot does change and can be measured: your habits, your body composition, how you carry yourself, your grooming, how you're photographed."
2. "Most stalls we see are direction problems: months of real effort with no map and nothing measured. Measuring is how you'd know if yours is."
3. "Behavior gets measured every week; appearance gets captured rarely, the same way every time."
4. "A record doesn't read itself; review turns it into a decision."
5. "By week 6 your record shows what's moving, and by week 12 it can tell you a lever doesn't move for you."
6. "My face is not evidence for the method. The record is, published on the dates I committed to."
7. "Most of how people read you was never about your jaw."

Any quotation presented as a Canon claim must match these words exactly, including claim 2's round-5 wording. A spoken Honest Answer may be longer (Module 3 owns it), but where it carries claim 1, the claim's words stay intact.

## Integration notes by module (carried from Step 3)
**Part I**
- 01: Recap Dan's door answer, the say-back, and Theo's route (owned by 02) rather than re-running them. Cole's [40] warm messages: 01 says month 2, 09 says weeks 1–2. Align to 09, which owns the Founding Sprint, or say plainly why 01's timeline differs.
- 02: "Nearest start after it" (§5) vs 08, which offers the next start first. Align to 08.
- 03:
  - Harmonize the door gloss with 05's definition (the self-assessment is the door's first step).
  - Recap rather than re-run 02's Dan and Theo material.
  - 03 recommends the Program to Theo while 05's sample plan tells Theo "don't buy". Check plausibility: either make the difference explicit or ask Part II to use another composite.
  - At 7,691 words, 03 is a trim candidate.

**Part II**
- 04: §5's "baseline taken while he waited" vs 05 (capture instructions moved to the recap and plan) and FRAMEWORKS' Week-Zero Baseline, which covers no-call buyers through the first seven logged days. Harmonize.
- 05:
  - Door definition, shared with 03.
  - Theo's sample plan (see 03).
  - The intake includes the age-band item (LEDGER G, aggregate only).
  - The no-pixel reason widens to the hub-wide rule: no ad pixel on any hub page (27).
  - The one-stock-send cap (LEDGER F) and the round-6 result email: the result, one next step, and a quiet Verify Page footer link.
- 06:
  - The week-12 table cell for a below-adherence client whose marker moved: not covered by the clause; give an honest read; Round Two only on measured momentum.
  - The week-1 review's "one thing he did well" is phrased as a record fact, never a label (17's no-labels-in-the-fit-window rule).
  - The plateau item allows "hold" (21).
  - The "misdirected" standard (R3-29).
- 07: Adopt the trigger rule from 21 (L151): a trigger ends delivery only when he chooses to stop and see someone, or when continuing would keep the trigger alive; otherwise review can run alongside a clinician's care. Check the service guarantee and stops-outside-the-windows wording against LEDGER B.
- 08: Harmonize the seat-cap reason in start announcements (L285 says "each week") across 08, 18, 20, and 26. Adopt the one-stock-send cap, the round-6 result email, and the mid-window default (a lead inside a running start's window is named that start while [a week] remains; LEDGER F).

**Part III**
- 09: Cole's warm messages in weeks 1–2 (see 01). L44 adds the checkout-confirmation source question for the no-call route: "Where did you find me?", a source label, never a readiness tag.
- 10: Adopt the board freeze from 21: labels and boards pause in the fit and exit windows. The Canon Lane is "free to every subscriber (outside a pause)".
- 11: Cole starts templating at month 11 (01). Routing help never works DMs, check-ins, or client replies.
- 12: Complaints are read per delivered email over a rolling month (26). The paid read window is about 30 eligible leads bought (27).
- 13:
  - L90, L245, and L303 read age as an observed mix moved by the state lever and the Optimizer page (THESES E2). The Age-Up Dial only lowers the minors' share and never aims at an adult age band (23).
  - Check that the $50k week reads about 20.5 hours.

**Part IV**
- 14: The Now check uses the Implication Question (19).
- 15: The spoken money line matches 19's ("…and thanks for saying it straight"). Adopt the trigger rule (see 07). The face statement lives in the comment policy every pin links to (already fixed; check the rest of 15 agrees).
- 16:
  - The opening's "two posts sit in his feed" shows a matched pair in a feed; check it against the pairs rule (long-form and site library only). It's another coach's post, so illustration may stand if it's framed that way.
  - The null-result stance recap uses 03's gloss.
- 17: The flat week-6 script overlaps 21 §5 (21 owns the week-6 conversation), so cut it to a recap. Adopt the board freeze (see 10).

**Part V**
- 18: L221: piece 2's price sits on the end card (23's editable-price rule). Harmonize the seat-cap reason (see 08). Card recaps use the [9]-month horizon.
- 19:
  - The written recap omits the credit.
  - Call-heard answers go to the same tags.
  - The pause tag blocks checkout.
  - A late-found minor is deleted and refunded.
  - The Starter tool is never named after "I can't afford it".
  - Canon claims are quoted verbatim.
- 20: The result page gains 25's door-code line ("Prefer Instagram? Send me this code"), confirmed by email reply. Adopt the one-stock-send cap and the round-6 result email. Harmonize the seat-cap reason. The Card uses [9] months.
- 21: Check the week-6 overlap with 17 from this side (21 keeps the full conversation).
- 22: Asks wait for a measured peak. Alumni status is a record fact.

**Part VI**
- 23–27 passed last and against the newest rulings, so check them against each other:
  - X lifespan: "within a day or two" (23, 25).
  - Each platform's own fixed, dated count (24, 25).
  - The door code (25, 20).
  - The result email's Verify Page footer (26, 27).
  - The Card's [9] months (27).
  - The Stranger rung carries no price (23, 24, 27).
  - Pairs appear only in long-form and the site library (23, 24, 27).
  - "Matchup" is the test term in 24.

**Everywhere**
- Canon claims are verbatim.
- Warmth Ladder rung names.
- The round-6 pause scope: every marketing send.
- Before/after pairs appear only in long-form and the site library.
- Evergreen content never speaks dates.
- The credit never appears beside a date or in a send.
- Asks wait for a measured peak.
- Protective stops leave only "stopped: stop rule".
- Minors get the education lane only, with no implied later sale.
- Tags are stage, Buyer State, route, and pause only.
- "(Intro)" pointers: list every one you find in your log, since the Intro (5.1) must hold what they point to.

## Log (`_build/integration/4.1-partN.md`, N = I…VI)
```
# 4.1 — Part N
## Fixes made
| Module | Where (heading + ≤12-word quote) | Change | Why |
## Cross-Part issues for the orchestrator
| Module (other Part) | Where | Problem | Suggested fix |
## "(Intro)" pointers found
## 4.2 nominations (per module)
- NN · weakest part: [section/block] — why, as the target reader (specific) · strongest part: [section/block] — what makes it strong
## Word counts before → after
```

## 4.2 — Depth upgrade (issued after 4.1)
For each module, rebuild the weakest part (a deep section, the worked example, an extras block, or a fixed block) to the level of the strongest part in the same module.
- Stronger means more mechanism and more niche grounding.
- Reasons come before rules.
- Frameworks get run on cases.
- Decisions come with signs → read → default move → what's left alone.
- Numbers follow LEDGER.
- The House Standard holds at both ceiling and floor.

Replace rather than add, and stay inside the band. Update the running summary. Audit clean.

## 4.3 — Reconciliation (issued after 4.2)
Goal: numbers, frameworks, and cross-references between modules all agree. Run by one fresh reconciler per Part, with edits only in that Part's module files and summaries, plus the orchestrator's global checks.

Load: this file's load list (DECISIONS R3 only), plus `_build/integration/later-notes.md` ("For 4.3") and Cole's canonical price path at the end of `_build/integration/4.1-partII.md`.

For each module in your Part:
1. **Numbers.** Run `python3 _build/tools/audit.py <file>`. Check every listed number, plus every bracketed composite figure, against LEDGER:
   - the row, the range, and the status (EV, PL, or RULE);
   - rows added in rounds 3–6 and Step 4.
   Arithmetic must add up. Composite figures stay bracketed and inside LEDGER ranges. Cole's prices and months follow the canonical path. No single-point outcome numbers.
2. **Frameworks and terms.** Every registered term must match FRAMEWORKS and the style sheet in name, gloss, owner, and tier:
   - Capitals for ★ and ◆ names, as registered. "Stop Rules" when naming the set, "a stop rule" for one, and "stopped: stop rule" stays as record text.
   - A gloss at first use in each module.
   - No synonyms.
   - Only the owner teaches an item; everyone else recaps in two sentences or fewer and points to it.
   - Run `python3 _build/tools/reconcile.py caps` and judge each hit, since some lowercase uses are generic and correct.
3. **Cross-references.**
   - Every "(Module N)" pointer names the module that owns or teaches the item.
   - Every module a body pointer names appears in **Leans on:**.
   - Every recap agrees with its owner's current text; grep the owner.
   - Every "(Intro)" pointer names something the Intro will hold.
   - Run `python3 _build/tools/reconcile.py pointer leans` as a starting list; `pointer` gives false positives.
4. **Summaries.** Update `_build/summaries/NN.md` to match, and clear open issues that are now resolved.

Rules:
- Every module stays inside 6,300–7,700 words. 18 (7,695) and 19 (7,692) must stay net-neutral.
- 0 FAIL on the audit.
- Log cross-Part problems; don't fix them.
- Don't commit.

Log (`_build/integration/4.3-partN.md`):
```
# 4.3 — Part N
## Numbers fixed | Module | Where | Was → Now | LEDGER row |
## Terms and frameworks fixed | Module | Where | Was → Now | Register |
## Cross-references fixed | Module | Where | Was → Now | Why |
## Cross-Part issues for the orchestrator
## Word counts before → after
```
