# DRAFTING KIT — Step 3 (passes 3.1–3.4 for one module)

You are drafting one module of *The End of Guessing*, an advanced playbook for a solo operator building a facial-development coaching business to $25–50k/month profit. The architecture is locked: your job is to write the module the brief describes, to the voice already calibrated, with nothing invented that the bible doesn't support. Everything lives under `_build/` (the bible) and the module file goes to the repo root.

Repo root: `/home/user/NEW-SOURCE-FILES-MASSETER`. Bible: `/home/user/NEW-SOURCE-FILES-MASSETER/_build`.

---

## 3.1 Load (read fully, in this order)

1. `SPEC.md`: the locked spec. Exclusions and form rules are absolute.
2. `VOICE.md`: the twenty rules, the cast, the formats, the vocabulary. This is how the module reads.
3. `voice/sample-v2.md`: the calibrated reference. Match its density, rhythm, paragraph length, table and script formats. (Where it differs from VOICE.md, VOICE.md wins.)
4. `STYLE.md`: scope and hard rules (Technique Firewall, Outcome Map, numbers).
5. `HOUSE_STANDARD.md` (playbook-facing) and `STANDARD.md` (internal Notch Map with under-use checks). The playbook never mentions notches or calibration.
6. Your module's brief in `briefs/` (find `## NN · Title`). The brief is the contract: argument, shift, opening frame, six sections with weights, frameworks owned/recapped, worked example, extras, stage-note angles, licenses in play, Standard Check focus, Quick Reference, dependencies, research, guardrails.
7. `MAP.md`: your module's job, shift, **Owns** list, **Leans on**, and the boundary-rules table. Never teach what another module owns beyond a recap of at most two sentences plus "(Module N)".
8. `FRAMEWORKS.md`: every name, tier, definition, and owner. Use names exactly (capitalization per `voice/style-sheet.md`). If you need a concept that has no name, describe it in prose; don't coin a new named framework unless the brief implies one, and log any new term (see 3.4).
9. `LEDGER.md` and `BUSINESS.md`: every number and the default business. **Every number in the module must come from LEDGER** (ranges with what moves them), or be a bracketed placeholder inside a composite.
10. Research: the brief's "Research for 3.1" line. Use `research/<track>/SYNTHESIS.md` first (business, persuasion, or ecosystem), then the dossiers (B1/B2, P1/P2, E1/E2) and `THESES.md` IDs cited in the brief's Dependencies. Where the brief says "verify", you may run a targeted web search to confirm the direction and evidence tier of a claim. Never cite studies, authors, or sources in the text; synthesize in the playbook's own words. Never introduce a new number from research: propose it instead (3.4).
11. Running summaries in `summaries/` for modules already drafted (read all that exist; they're short). For neighbors not yet drafted, rely on their briefs and MAP entries.

## 3.2 Draft

Write the full module to the repo root at the file name in MAP (e.g., `/home/user/NEW-SOURCE-FILES-MASSETER/05-the-door.md`).

**Skeleton (VOICE §3.1), exactly:**
```
# N · Title
*Part X — Part Title*

**The shift:** from *"before"* to *"after"*

[Opening frame ~200 words]

## 1. Section Title
### Claim-shaped subsection (sentence case)
…
## 6. Section Title

## Worked Example: [Composite], [Situation]

## Script: … / ## Scripts: … / ## Template: … / ## Templates: … / ## Checklist: …   (1–3 extras headings, per the brief)

## Stage Notes
## Standard Check
## Quick Reference
```
- `N` is unpadded in the title ("# 5 · The Door"). Part titles are in MAP ("Part II — The Offer System").
- **Budget** (VOICE rule 20): default opening ~200 · six deep sections ~4,900 total (use the brief's weights) · worked example ~700 · extras ~600 · Stage Notes ~200 · Standard Check ~130 · Quick Reference ~300 ≈ 7,030. **Part V (18–22):** deep ~3,800–4,000 · worked example ~1,000 · extras ~1,500–1,700. The whole file must land in **6,300–7,700 words**; aim for 6,900–7,300.
- **The hard case** ("When the signals disagree", listed under Extras in the brief) goes as a bold run-in paragraph **inside the most relevant deep section**, exactly as in the sample: `**When the signals disagree.** …`. The extras block holds scripts, templates, and checklists.
- **Flagship frameworks (★)** get the five beats (VOICE rule 5), with a run on one composite case (150–250 words) unless the worked example is built on it. Tools (◆) get a short treatment; terms (○) get a gloss at first use.
- **Options + default** in the VOICE §3.2 format wherever the brief names a real choice.
- **Scripts** (VOICE rules 15–16): blockquote, bold speaker labels, fixed cast with *(composite, state)* at first appearance, ≤150 words per block, then the debrief as plain prose, the scripted pushback variant, the line you never say, and the return to the recommendation and the ask, or the stop rule that ends it. Every sales unit ends at the decision.
- **Composites:** only Dan, Theo, Adrian, Sam, Maya, Jordan (buyers) and Cole, Reid (operators), with the sketches in VOICE §2. Their numbers are bracketed placeholders or LEDGER ranges. A composite's events are self-contained in this module; don't claim continuity with other modules' events.
- **Cross-references:** "(Module N)" after the gloss, at most one per ~600 words (Modules 1 and 28 excepted), never in headings. For Intro-owned items (the House Standard, the Informed-Client Test, Stop Rules, the Dignity Check, the Hostile-Screenshot Test, the Payoff Test, the Spine), use "(Intro)" when a pointer is needed.
- **Numbers:** LEDGER ranges in units he can act on, with what moves them. "About/roughly" in prose; "~" only in tables and bracketed placeholders. Digits for ranges, money, percentages, and numbers ≥10. No single-point outcome numbers.
- **The Technique Firewall:** method content appears only as bracketed placeholders ("[first adjustment]", "[weekly habit block]") or at category level. The Outcome Map governs every outcome sentence.
- **Standard Check** (100–160 words): 2–4 bullets, each naming a tactic from this module, the House Standard item it touches (by name: *Sell directly*, *Close*, *Name the stakes*, *Use real dates*, *Name the destination boldly*, *Fight ideas, not people*, *Build identity on evidence*, *Present the price*, *Say the true thing*; or "the line on …"), and what keeps it inside the line. Nothing that could move to another module unchanged.
- **Licenses in play** (brief): every license listed must be *used* in the module at its default where it applies and at the stronger variant where licensed. Under-selling is a defect just like overreach. The floor matters: a screened, good-fit buyer in your examples or scripts is never left un-asked, un-probed, or with the stake unnamed (burned buyers excepted, as defined).
- **Stage Notes** (150–250 words): the italic stage key line from the sample, then Early / Growing / Scaling, each with this module's binding constraint, the default move, and the one trap. No restatement of the body.
- **Quick Reference** (200–350 words): **In one line.** · **Takeaways** (3–5) · the module's one or two decision tables · **Framework cheat sheet** (owned frameworks only, "Use it to…", verbs first) · **Leans on:** · **Do this month:** (three actions).

**Never:** mention the source files, a prior program, course, or blueprint; compare anything to earlier material; use banned vocabulary (VOICE §4: the diagnose family, treat/treatment in the clinical sense, therapy, healing, patient, protocol, cure, "fix your face", restore/remodel/reshape, bone growth as a promise); teach techniques; recommend a free community, launches, faceless content, podcasts/collabs, or operator mindset work; use hype (secret, hack, game-changer…); invent credentials; use the operator's face as proof; sell to minors; let a stop rule be crossed, including by automation.

## 3.3 (not yours) Adversarial critique
A separate reviewer writes `_build/critiques/NN.md`. You'll receive it for 3.4.

## 3.4 Rebuild (when you receive the critique)

1. Fix every **blocking** and **major** finding; fix minors unless they conflict with the brief (say why in your report).
2. **Rewrite the weakest sections** the critique names, from the argument up, to the level of the module's strongest section. Don't patch sentences where the section needs rethinking.
3. Reconcile every number against `LEDGER.md`. Anything you need that isn't there becomes a *Proposed LEDGER addition* in your summary (with status and reasoning), and the text uses a bracketed placeholder or a verbal range until it's approved.
4. Log every term you introduced that isn't in `FRAMEWORKS.md` (see the summary template). Prefer prose to new names.
5. Run the audit: `python3 /home/user/NEW-SOURCE-FILES-MASSETER/_build/tools/audit.py /home/user/NEW-SOURCE-FILES-MASSETER/NN-file.md` and resolve every FAIL, and every FLAG that is a real problem (FLAGs need judgment: "treat it as" in the ordinary sense is fine; a clinical "treatment" is not).
6. Write the running summary to `_build/summaries/NN.md` (template below, ≤350 words).

## Running summary template (`_build/summaries/NN.md`)

```
# NN · Title — running summary
- Words: [count] · Status: rebuilt after critique
- Shift: …
- Sections: 1. [claim, one line] · 2. … · 6. …
- Taught here (name — the gloss as written): …
- Recaps made (name → Module N): …
- Numbers used (LEDGER section/row): …
- Composites used and what happens to each: …
- Scripts/templates/checklists included: …
- New terms not in FRAMEWORKS (term — gloss — why needed): … or "none"
- Proposed LEDGER additions (number — status — reasoning): … or "none"
- Deliberately left to other modules: …
- Open issues for integration (Step 4): …
```

## Your report back (≤150 words)
File path and word count; audit result (FAILs remaining should be zero); the three biggest changes made in the rebuild (or, after 3.2, the parts of the brief you found hardest); any proposed LEDGER additions or new terms; any conflict you found between bible files. Don't paste module text into the report.

---

## Standing rulings from rounds 1–3 (read with DECISIONS.md R3; they override older wording anywhere)

- **Composites:** Cole makes the right reads; Reid makes common *strategic* misreads (chasing views, skipping a check, free-call calendars). No composite ever crosses a House Standard line, even as the contrast.
- **Money and stop rules:**
  - Ask the affordability question verbatim before every paid step.
  - Show tiers premium-first *before* the question, then ask about his pick.
  - A "no" ends money talk: the Starter Path plus the pause route, with no downsell and no Program Async offer.
  - Nothing he receives after "I can't afford it" carries a price, offer, or date.
  - The paid Starter tool exists only after about 20 graduates. Fit-paused buyers get the reading-only path. Re-entry is buyer-controlled, never a money condition.
- **Automation:** the pause route blocks sales sequences, date sends, checkout, and abandoned-cart emails for 60–90 days, then asks for re-permission. A minor found after the fork is deleted and refunded.
- **Dates:**
  - Credit is never a deadline and never appears beside a decision date; it's stated once as a term in the written plan.
  - Late entry runs through week 2. Every send carries the start date and the last day to join.
  - Deferral effects are contested (LEDGER E): never lean on urgency psychology.
- **Delivery:**
  - Markers: 2–3 per client, never read from photos, never binary did-it items.
  - "Haven't moved" means no marker reached its threshold.
  - Measured momentum means adherence at or above threshold, plus at least one marker still improving across its last two readings.
  - Testimonial asks come never before the fit window closes, never in the week-6 exit conversation, and first at the first measured peak after the exit decision.
- **Guarantee:** refunds are paid within 7 days. Your own review errors earn free corrective weeks (capped at 6).
- **Tiers and targets:**
  - Program Async is Scaling-only.
  - $50k is the good case (LEDGER A3's middle case tops out around $28–35k in Bands B–D).
  - The $50k week is about 20.5 h without Private.
  - The Hold and Round Two sit below parity at Scaling, so they sell while minutes are spare.
- **Terms:** "eligible lead → enrollment" is the single conversion term. The stage thresholds are in LEDGER A2 (revised).
- **Tags and privacy (round 4):**
  - No stored tag records fit, goal-sensitivity, or insecurity answers. The stored tags are stage, Buyer State, route, and the content-free pause tag.
  - Result-page branches (burned, dignity, Optimizer, Ambivalent) are computed at render time from his answers, and nothing is stored from them.
  - Every automated sequence follows the Dignity Route's limits by default: stakes limited to time, money from here on, and guessing, with no missed-social-moment reflection. So no dignity tag is ever needed.
  - The checking signal is "many times a day" at both tiers; regular checking short of that is a Dignity Route trigger, not a signal.
- **Status and refund rights (round 4):** status (founding, alumni, membership, boards) is never contingent on not using a refund right. Exits are never mentioned in the room or on boards.
- **Dignity Route in practice (round 4):** a buyer on the route never hears his missed social moments reflected back, even ones he stated as his goal. Keep the destination at "knowing instead of guessing".
- **Protective stops leave no record (round 4, refined in round 5):** a protective stop (money he said he can't spare, distress, a fit-check signal, a minor) leaves only "stopped: stop rule"; no words or reasons feed content planning, the objection log, or the Conversation-to-Content Loop. A clear no ends the ask for that conversation, but its link may be logged.
- **Verdict integrity (round 4):** "misdirected" needs a named lever, a documented correction, and early movement on it at the next reading; otherwise "the lever doesn't move for this person" stands. Never relabel it to sell more time.
- **Minors (round 4):** education-lane copy never implies a minor can buy later or after a visit: no "first", no "come back when", no route to the door. Adulthood re-entry is never marketed to minors.
- **Testimonial asks and refunds (round 4):** never in a conversation where a refund right is decided (the week-6 exit, the week-12 non-response verdict), and never asked of a client who claimed a refund. Client stories (Transitions, Cases) need consent given after the fit window, so none exist in month 1; the operator's Origin and anonymized stall patterns can run from month 1.
- **Claims about "his" stall (round 4):** never tell a general audience their stall "isn't genetic" or "is fixable". Say most stalls you see come from direction, and that measuring is how he'd know which verdict is his.
- **Measured peak (round 5):** adherence at or above his threshold and at least one marker at its threshold, so no refund decision is open. Every renewal, referral, testimonial, or upgrade ask waits for one.
- **Training-Partner Seat (round 5):** pair enrollment of two adults into one start, each through his own door. At graduation it's a referral variant: the graduate introduces the person he trains with. No pair discount.
- **Warmth Ladder rungs (round 5):** Stranger → Returning → Assessed → Deciding. Surfaces map onto these by pointer (Module 18).
- **Evergreen content and dates (round 5):** evergreen videos and pages never speak specific dates; they point to "the next start and its last day to join" on a page that updates. Only dated sends carry dates.
- **Before/after pairs (round 6):** matched pairs live in long-form and the site library only; never in short-form, Instagram posts or carousels, or ads (THESES E8; Module 27's gradient). Organic short-form may carry contextualized outcome stories with range and denominator on screen.
- **TikTok trigger (round 6):** add TikTok only after a labeled trial matches Reels on eligible adults per editing hour over ~30 door completions (LEDGER F).
- **The pause route in email (round 6):** a pause holds every marketing send (sequences, date sends, checkout links, unfinished-checkout notes, the Canon Lane, the weekly letter) for 60–90 days; only mail he asked for goes. Then one re-permission ask with no price, offer, or date; a yes is his own re-entry, silence or a no ends marketing mail.
- **The Canon Lane (round 6):** opens by the first graduation (the Hold lists it as free to every subscriber), about one email a month, never to paused leads; Scaling adds cohort tuning.
- **Mail during a pause (round 6):** Starter Path check-ins go only after he takes the path (a click or reply to the handover) and carry no offer, price, or date. The re-permission ask names start announcements and reminders plainly; a "not for me" click never counts as engagement.
- **Unfinished-checkout note (round 6):** one note, only after a yes to the affordability question and a stop at payment; leaving at or before that question sends nothing.
- **Result email (round 6):** the result and one next step; a quiet footer line may link the Verify Page (how we work, prices, terms).
- **Composite continuity (Step 4):** a composite's sketch is fixed (age, state, background, situation); each module's events are its own illustration, not a continuing timeline, unless a module explicitly continues another's story (as 20 → 21 → 22 follow one April start). Adjacent modules that read as one story must agree. The Intro states this convention.
- **Pause gloss (Step 4):** "a content-free tag that holds every marketing send and blocks checkout for 60–90 days, then asks permission once".
