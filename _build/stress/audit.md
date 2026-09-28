# Spec audit: architecture of the 28-module playbook

**Scope.** This audit checks the architecture at commit `d383ac4` ("Step 2.1–2.4").

- **Read in full:** SPEC (the authority), STYLE, STANDARD, HOUSE_STANDARD, DECISIONS (including R1), BUSINESS, MAP, FRAMEWORKS, THESES, LEDGER, and the four briefs.
- **Checked only for stale names:** REGISTRY.
- **Spot-checked only for the overlap and buyer questions:** `mining/GAPS.md` and `mining/INVENTORY.md`.
- **Out of scope:** an untracked `_build/voice/sample-v1.md`, which appeared during the audit.

**Severity.**
- **Critical:** the architecture as written violates the locked SPEC.
- **Major:** likely to cause a violation during drafting, or a serious inconsistency between architecture files.
- **Minor:** polish.
- *Judgment call* marks a finding that rests on one reasonable reading of the spec when another reading is also possible.

**Compliance rule.**
- **Pass:** no finding above minor.
- **Partial:** at least one major and no critical.
- **Fail:** at least one critical.

---

## Summary

There are **25 findings: 1 critical, 15 major (one of them a judgment call), and 9 minor.**

- **Critical: AUD-1.** Module 28's section budget sums to about 8,350 words. The band ceiling is 7,700.
- **The skeleton holds.** There are 28 modules in track order, with the build plan last. Every brief has stage notes. No excluded strategy is recommended anywhere. The Technique Firewall is intact, and every module number in every cross-reference is correct.
- **The majors fall into four groups:**
  - Form budgets (AUD-2).
  - Wording and names that the architecture's own rules ban (AUD-3, AUD-4, AUD-16).
  - Places where a brief or BUSINESS contradicts the standard or the LEDGER (AUD-5, AUD-6, AUD-7).
  - The Notch Map not reaching the briefs, so the floor is under-audited (AUD-8).
- **The rest** are problems of single ownership, numbers, and the register (AUD-9 to AUD-15).

---

## Findings

### Critical

#### AUD-1 · Critical · Module 28 is budgeted above the audit band

**Location.** `briefs/part-6-7.md`, 28 · Sections (lines 185–191). The default block budget is in `briefs/part-1-2.md`, line 4.

**Evidence.** The brief says "Sections (budget to be confirmed after Step 4.1)". Its sections add up as follows:

| Section | Words |
|---|---|
| How to use | ~500 |
| Found | ~1,700 |
| Prove | ~1,300 |
| Leverage | ~1,300 |
| Waypoints | ~700 |
| After month 9 | ~400 |
| **Sections total** | **5,900** |

The default non-section blocks add about 2,450 more: opening ~200, worked example ~700, extras ~650, Stage Notes ~350, Standard Check ~200, and Quick Reference ~350. That makes **about 8,350 words**. SPEC §8 says: "Audit band: 6,300–7,700." Every other brief totals 7,050–7,550 (Appendix A).

**Issue.** The spec makes the closing build plan a success criterion, and it is planned about 650 words over the ceiling. The brief also asks it to recap "nearly everything in one or two sentences each", which adds words. The "to be confirmed" note gives no route back into the band.

**Fix.**
- Cap the deep sections at about 4,700. For example: How to use 400, Found 1,400, Prove 1,000, Leverage 1,000, Waypoints 600, After month 9 300.
- Run the worked example (the default operator in Band B, month by month) through sections 2–4 instead of as a separate ~700-word block, which would repeat them.
- Limit recaps to one cross-reference line each.

### Major

#### AUD-2 · Major · Script-heavy modules 18–20 get a checklist-sized extras budget

**Location.** `briefs/part-5.md`, line 3, and the Extras of 18 (line 27), 19 (line 61), and 20 (line 95). The default extras budget of ~650 is in `briefs/part-1-2.md`, line 4.

**Evidence.** Line 3 says "Persuasion, sales, and content modules carry scripts and swipe copy as their main extras (D7)". The three modules must carry the following.

| Module | Required scripts | Note |
|---|---|---|
| 18 | Five offer pieces | — |
| 19 | "the full call outline with verbatim load-bearing lines … objection responses by link; recap and follow-up templates … the call scorecard" | Already budgets 7,550 |
| 20 | Result-page templates "by state", "a five-email sales sequence", voice-note guidelines, and DM handoff lines | — |

Written out in full, each set runs about 1,300–1,800 words.

**Issue.** Either these three modules breach 7,700 words, or their scripts ship as outlines. Outlines would undercut D16 (load-bearing lines verbatim) and the spec's success criterion of "mastery-level skill" (SPEC §8).

**Fix.**
- Give 18–20 their own budgets: extras about 1,200–1,400, deep sections about 4,100–4,300. For example, 19 §4 could run about 700 words, with the objection responses living only in the extras.
- Each script appears once, in the extras, and the sections point to it.

#### AUD-3 · Major · Nurture Jobs is defined relative to earlier material, and the glossary would ship it

**Location.**
- `FRAMEWORKS.md`, line 207.
- `briefs/part-6-7.md`, 23 · Argument (line 9) and 23 · §1 (line 16).

**Evidence.**
- FRAMEWORKS: "The five jobs a community **used to do**".
- Brief 23: "A free community **once did** five jobs … Without one, each job needs an owning asset".
- STYLE's banned-phrasing rule: "No sentence may compare this playbook, its standard, or its advice to any earlier material". The only exception is a sentence that describes the buyer or the business itself.
- THESES E1 states the same idea natively: "Nurture is five jobs; each needs an owning asset."

**Issue.** The operator starts from a blank slate and has never run a community, so "used to" and "once did" can only refer to the source program's design. The Glossary is compiled from FRAMEWORKS definitions (FRAMEWORKS line 3; MAP line 272). STYLE's grep list ("anymore", "no longer", "previously", …) would not catch "used to" or "once".

**Fix.**
- Redefine the term natively. For example: "the five jobs every coaching business has to get done between first view and purchase (exposure, visible proof, identity rehearsal, a Q&A archive, a warm pool), each with an owning asset."
- If module 23 wants a contrast, compare with the industry ("most coaching businesses hand these jobs to a free group"), not with a past.
- Add "used to", "once", and "now that" to the STYLE grep list.

#### AUD-4 · Major · Banned clinical words are built into framework names and into module 14's core verb

**Location.**
- STYLE, line 36.
- FRAMEWORKS: line 24 (principle 5) and lines 126, 137, and 189.
- MAP: lines 122 and 137–138.
- Briefs: 01 (§3, worked example, extras), 12 §3, 14 (belief shift, §3, extras), and 21 (★).

**Evidence.**
- STYLE says: "Clinical or therapeutic vocabulary (diagnose, treat, therapy, healing, patient, protocol) is out." It has no exceptions.
- FRAMEWORKS principle 5 bans "diagnose, treat, protocol (except 'Plateau Protocol')". The register and briefs then use these words:

| Use | Where | Problem |
|---|---|---|
| ★ **The Plateau Protocol** | 21 | Flagship name that clients meet |
| "the no-show and reschedule protocol" | 12 §3; MAP 12 | "protocol" is banned |
| ◆ **The Leak-Gate Diagnostic** | 13 | Also breaks FRAMEWORKS' own principle 5 |
| "the monthly **Constraint Diagnosis**" | 01 extras | Banned word in a name |
| "Diagnose monthly" | 01 §3 | Banned word |
| "my job is to **diagnose** and repair links"; "Owns … link diagnosis" | MAP 14 | Module 14's core verb |
| "I diagnose and repair the broken link"; "§3 Link diagnosis"; "the link-diagnosis card" | Brief 14 | Module 14's core verb |
| Type labels "Protocol" and "Diagnostic" | Founding Sprint, DM Handoff, Honest Exit, Stall Verdicts | Banned words as labels |

- R1-25 already replaced "protocol" with "capture standard" for this reason.

**Issue.** Drafting to these briefs breaches STYLE on almost every page of the persuasion model (module 14). It also breaches it in a flagship name that clients see, because plateaus are pre-announced in the Expectation Document (21, Action steps).

**Fix.**
- **Default: rename.** Possible names:
  - The Plateau Plan, for the Plateau Protocol.
  - The no-show rule, for the no-show protocol.
  - The Leak-Gate Trace, for the Leak-Gate Diagnostic.
  - The monthly Constraint Questions, for the Constraint Diagnosis.
  - "Finding the broken link", for link diagnosis.
  - Sequence or Tool, for the type labels.
- **Alternative:** add a DECISIONS row that limits STYLE's ban to anything said to or about a client's face or body, and explicitly allows operator-facing phrases like "diagnose the constraint".
- Either way, remove FRAMEWORKS' silent exception.

#### AUD-5 · Major · The default door diagram puts a paid step before the Fit Check

**Location.**
- `BUSINESS.md` §4 diagram, lines 45–50.
- `briefs/part-1-2.md`: 06 · Argument (line 181) and 06 · Quick Reference ("the door diagram").

**Evidence.**
- The diagram branches to "EARLY: disclosed FIT CONVERSATION (free or **~$25–50** credited …)" and "SCALING: paid DECISION ASSESSMENT (**$150–250** …)". Only after that does it reach "FIT CHECK before any paid step".
- STANDARD notch 1 marks "any paid step before the fit check" as out.
- STANDARD §7 keeps "Fit check before any paid step" as a deliberate tightening (hard line 5 applied).
- THESES B9: "Paid step: a brief fit check at booking or checkout."

**Issue.** Module 06's Quick Reference reproduces this diagram. If the door is built as drawn, a buyer pays for a paid fit conversation or a Decision Assessment before tier 2 of the Fit Check runs.

**Fix.**
- Redraw the diagram so tier 2 runs at booking or checkout of any paid step. That means before a paid fit conversation, before the Decision Assessment, and embedded in checkout.
- Add one line to brief 06 §4: "tier 2 runs at booking of any paid human step."

#### AUD-6 · Major · The routing freelancer's duties contradict the LEDGER rule and keep growing (the spec part is a judgment call)

**Location.**
- `briefs/part-6-7.md`: 25 · Stage notes (line 97), 25 · Extras (line 95), and 26 · Stage notes (line 131).
- `briefs/part-5.md`: 21 · Stage notes (line 131).
- `BUSINESS.md` §6, line 104.

**Evidence.** The briefs give routing help these duties:
- 25: "Scaling: routing help **handles first-pass DMs**", using "DM reply templates by case (adult, **minor**, 'rate me', **distress**)".
- 26: "routing help on replies".
- 21: "routing help flags missed check-ins".
- BUSINESS: "routing help handles the inbox".

The rules they meet:
- LEDGER H: "routing and policy moderation only; no selling, claims, or client conversations; **no contact before age is confirmed**". THESES B21 says the same.
- THESES H7 keeps fit-check and health-adjacent answers out of any tool a freelancer can see.
- D34 keeps DMs with the operator.
- SPEC §3: "solo + freelancers (project-based help: editing, design). No team-building beyond that."

**Issue.**
- First-pass DMs happen before verification by definition, because the Keyword Route sends them before the age fork. The templates also cover minors and distress. On any reading of "contact", this crosses LEDGER H.
- "The inbox" and "replies" include client communication, which stays on the Keep-List.
- Taken together, these duties turn the role into a standing assistant for the inbox, DMs, and check-ins. That goes beyond the narrow task R1-6 accepted as "project freelancers". This part is the judgment call.

**Fix.**
- Make brief 12 §4 the single definition of the role, and align 21, 25, 26, and BUSINESS §6 to it:
  - Routing help may moderate public comments against the published policy and send one templated door link.
  - Anything revealing a minor, distress, a purchase question, or client content goes to the operator.
  - Routing help gets no view of check-in content or fit-check answers.
- Record in DECISIONS whether sending a templated door link counts as "contact".
- Confirm the "project-based" reading with the user.

#### AUD-7 · Major · The public offer piece "price with seat math" collides with Seat Math, which is internal

**Location.**
- MAP 18 · Owns (line 168).
- FRAMEWORKS, line 167.
- `briefs/part-5.md`: 18 §3 (line 18) and 18 · Extras (line 27).
- STANDARD notch 1 (the licensed stronger variant).

**Evidence.**
- The Offer Pieces include "**price with seat math**".
- Seat Math (module 07) is defined as "Seat caps set monthly from measured care minutes; **publish seats and deliverables, not minutes**" (FRAMEWORKS line 88; brief 07 §5).
- FRAMEWORKS line 298 retires "**Seat Math as a public disclosure (now internal)**".
- THESES P11: "Publishing raw review minutes is a test, not a default (it invites per-minute pricing)."

**Issue.** Whoever drafts module 18 must either publish care minutes, which contradicts 07, FRAMEWORKS, and P11, or quietly reinterpret a registered name.

**Fix.**
- Rename the piece "price with delivery math".
- Define it from P11 and notch 8's licensed variant: itemized delivery units, the seat cap as plain fact from the Fill History, and a fee breakdown that includes the operator's pay and profit. It never shows minutes.
- Update STANDARD notch 1, MAP 18, FRAMEWORKS line 167, and brief 18 together.

#### AUD-8 · Major · The Notch Map doesn't reach the briefs, so the floor is under-audited (drift toward restraint)

**Location.**
- The "Standard Check focus" lines in all four brief files.
- `briefs/part-3-4.md`: 17 (line 269) and 11 §4 (line 53).
- `briefs/part-1-2.md`: 08 (line 271).
- FRAMEWORKS, line 35.
- STYLE, line 45.

**Evidence.**
- **No under-use checks in any brief.**
  - STANDARD §1: "an ambiguity doesn't default to restraint … the stronger variant is used wherever its license holds".
  - STANDARD §2 gives each notch "an under-use check to run on every module".
  - None of the 28 briefs carries an under-use check.
- **Notch coverage is thin.**
  - Only 10 of 28 briefs mention a notch at all: 03, 05, 08, 09, 10, 11, 16, 17, 18, and 19.
  - **No brief references notch 9**, so its licensed variant ("say the hard true thing with force") has no home.
  - Brief 19's Standard Check names only "Notches 2, 3, and 8". The re-sale conversation in 21 names no notch at all.
- **Notch 7's strongest variant has vanished.**
  - Its licensed variant, "**opt-in leaderboards on logged process**", appears in no MAP, FRAMEWORKS, or brief line. A grep finds zero hits.
  - THESES B16's room rules include it, but brief 11 §4 keeps only the restrictions ("no face photos, pseudonymous handles, no comparison, camera-optional").
  - Brief 17 audits "Notch 7 **at its default**", and brief 08 audits "Notch 8 **at its default**".
- **Many Standard Check lines cover only the ceiling.**
  - In 15, 20, 21, 22, 23, 24, 25, and 26, where persuasion force applies, the focus lines name only ceiling or hard-line items. None names a floor or force element.
  - For example, 22: "No hidden renewals; the honest 'you don't need it'; testimonial consent; referrals never reward posting faces".
  - STYLE line 45 says the Standard Check covers "ceiling and floor, relevant licenses".
- **The terms don't match.**
  - The briefs say "notch N", which the playbook must never say (HOUSE_STANDARD line 3).
  - FRAMEWORKS and STYLE call the nine items "licenses". HOUSE_STANDARD calls them "Nine things we do on purpose".

**Issue.** The calibration exists in STANDARD, but the briefs audit the ceiling and not the floor. That is the drift R1-12 was written to stop. The only drift in the other direction (too loose) is AUD-5 and AUD-6.

**Fix.**
- Add a "Notches in play" line to every persuasion and ecosystem brief, and to 05, 08, 09, 10, and 11. Each line should give the notch, its default, its licensed variant, and its under-use question.
- Restore "opt-in leaderboards on logged process" in 17 §5 and 11 §4.
- Give notch 9's forceful variant a home in 19 §4–5 and 21 §4.
- Change 08 and 17 to "default and licensed variant".
- Tell drafters to write Standard Checks with the House Standard's item names ("Build identity on evidence", "Say the true thing") and never to write "notch".
- Pick one word for the nine items and use it in FRAMEWORKS, STYLE, and HOUSE_STANDARD.

#### AUD-9 · Major · The same option sets are taught in two or three modules

**Location.** Briefs 01 §5 (line 22), 05 §3 (line 156), 06 §3, 07 §6 (line 227), and 09 §3 (line 292). MAP Boundary table (lines 248–267).

**Evidence.**
- 01 §5: "the engine alternatives as options + default (table from BUSINESS §6)".
- 05 §3: "flagship: cohort vs 1:1 vs **long container** vs **async-only**; front buffer: fit conversation vs paid assessment vs application".
- 07 §6: "12 weeks (default) vs 8 weeks vs a **6-month container**; **cohort starts vs rolling entry**; the **async-only** variant".
- 09 §3 also teaches rolling starts.
- MAP line 3: "A concept is taught in full only by its owner".
- No module owns the profit-engine decision, which SPEC §3 leaves open ("Profit engine: open, leaning hybrid").
- The Boundary table has no row for 01↔05, 05↔06, 05↔07, or 07↔09.

**Issue.** Three modules argue for the same options, which invites three slightly different defaults.

**Fix.** Give each decision one owner, and add the missing rows to the Boundary table.

| Decision | Owner | Other modules |
|---|---|---|
| Profit engine | 01 | Point to 01 |
| Flagship format and container | 07 | 05 names the slot and points to 07 |
| Front-buffer options | 06 | 05 points to 06 |
| Cohort starts vs rolling entry | 09 | 07 points to 09 |

#### AUD-10 · Major · "Which asset may ask for what" has three owners

**Location.** MAP Owns lists for 06 (line 78), 18 (line 168), and 23 (line 205). Briefs 06 §5, 18 §1 and §5, and 23 §1.

**Evidence.**
- 06 owns "warm routes (what may link to checkout)".
- 18 owns "the Warmth Ladder (the direct-sell test)" and "what each rung licenses".
- 23 owns "Surface Types (jobs and allowed asks)".
- All three restate one rule (D20 / R1-23), and no boundary row separates them.

**Issue.** A question such as whether a warm Short may link to checkout would get three answers.

**Fix.**
- 18 owns the rule (the Warmth Ladder plus One Ask per Asset).
- 06 owns only the checkout mechanics: the age attestation and the embedded Fit Check.
- 23 maps each surface onto 18's rungs by pointer.
- Add a boundary row for this split.

#### AUD-11 · Major · Graduation and baseline day each have more than one owner

**Location.** MAP Owns lists for 07 (line 85) and 22 (line 196). FRAMEWORKS, lines 156 and 190. Briefs 17 §3, 21 §2, and 22 §2 and §6.

**Evidence.**
- MAP 07 owns "… privacy in delivery, **graduation**".
- MAP 22 owns "alumni status and **graduation**".
- In FRAMEWORKS, the Measurement Rituals (17) are "**Baseline day**, the re-captures, **graduation**".
- The Commit Ritual (21) is "**Baseline day**, his written reasons, the expectation document signed off".
- FRAMEWORKS line 303: "Every named item has exactly one owner".

**Issue.** Graduation has two MAP owners and also sits inside a third module's framework. Baseline day is defined inside two frameworks with different owners.

**Fix.**
- 07 owns both as deliverables: what happens and when.
- 17 owns what they mean for identity.
- 21's Commit Ritual and 22's asks point to them.
- Remove "graduation" from MAP 22's Owns list.

#### AUD-12 · Major · The affordability question has three owners and three wordings

**Location.** Briefs 02 · Extras (line 63), 08 §4 (line 259), and 19 §3. LEDGER G (line 211). BUSINESS §2 (line 17). THESES B12.

**Evidence.** Three briefs teach the question:
- 02 scripts "the affordability question (**verbatim**)".
- 08 §4 teaches it at the plan step.
- 19 §3 teaches it in conversation (MAP boundary 8↔19).

The three source files word it differently:

| Source | Wording |
|---|---|
| LEDGER G (RULE) | "Is this comfortable from your monthly income without new credit **or buy-now-pay-later**?" |
| BUSINESS §2 | "comfortable from monthly income without new credit?" |
| THESES B12 | "comfortable from your monthly income without new credit?" |

**Issue.** A safeguard that hard line 5 depends on, meant to be spoken word for word, would be printed three times from three sources. Two of the three versions drop "buy-now-pay-later", the very borrowing the question exists to catch.

**Fix.**
- LEDGER G's wording is the canonical one.
- 19 owns the spoken line. 02 states the policy and points to 19. 08 references it.
- Correct BUSINESS §2.

#### AUD-13 · Major · The engine-alternative numbers aren't in the LEDGER, and one contradicts it

**Location.** BUSINESS §6 Alternatives table (lines 111–118). Brief 01 §5 ("table from BUSINESS §6"). Brief 05 §1 ("the one-to-one-only ceiling").

**Evidence.**
- BUSINESS lists:
  - "Private-led (premium 1:1) | **~$17–22k profit**"
  - "Membership-led | Needs ~530–1,080 members"
  - "Digital-led | Needs ~160 sales/month"
  - "Long single container (6 months, ~$4.5–6k)"
- LEDGER A (line 22) says: "One-to-one-only ceiling … **~$5–20k/month revenue**".
- STYLE: "Every number matches LEDGER". BUSINESS line 3: "Numbers come from LEDGER v2".

**Issue.** Module 01 would print a one-to-one ceiling above the one module 05 prints from the LEDGER. The other engine figures have no LEDGER row at all.

**Fix.**
- Add the engine rows to LEDGER A as derived planning figures (PL, D), with their assumptions: premium one-to-one at about $6k per 12 weeks, versus one-to-one at program prices.
- Give the two ceilings distinct names in 01 and 05.

#### AUD-14 · Major (judgment call) · Operations are counted with a different taxonomy from the spec's

**Location.** SPEC §3 (line 34). MAP line 9. STYLE line 52. DECISIONS R1-39. MAP entries for 04, 08, 12, and 13.

**Evidence.**
- SPEC: "Operations (**pricing & unit economics**, systems & automation, freelancer management, time & energy design): in scope but **NOT in-depth**".
- The MAP counts operations as "two modules (12, 13)". That leaves out the two areas the spec lists first.
- Pricing (08) and unit economics each get a full module. Module 04 is the unit-economics one: the Demand Equation, the Reverse Funnel, and the Capacity Ceiling.
- Every module must reach 6,300 words, so every operations module is necessarily in depth.

**Issue.**
- Read literally, operations fill three or four full modules, against the architecture's own cap of two (STYLE).
- The other reading has merit. SPEC §2 names "pricing" as a Business & Offers topic, so 08 can be defended. That leaves 04 as the exposed module.

**Fix.**
- Record the classification in DECISIONS:
  - 08 is SPEC §2's "pricing".
  - 13 is "growing into a highly profitable solo operation".
  - Operations are 04 and 12.
- Hold 04 to planning depth. Its existing "no spreadsheet dumps" guardrail is the right lever.
- Alternatively, fold 04's math into 01 and 13 and give that module slot to a higher-focus area.
- **The user should confirm which reading holds.**

#### AUD-15 · Major · The glossary register lacks the product names and core terms every module uses

**Location.** The FRAMEWORKS register, which is the glossary source (FRAMEWORKS line 3; MAP line 272). BUSINESS line 3.

**Evidence.**
- **No register row at all** for:
  - **The Program, Private, and the Priority Review.** These are product names (BUSINESS line 3).
  - **The Fit Conversation.** MAP 06 says it "Owns … the Fit Conversation".
  - **Bounded agency.** MAP 14 lists it as owned.
  - The education lane.
  - The week-6 read and the week-12 re-assessment.
  - Evidence tier.
  - Door v0.
  - The dignity route and the verification-first route.
  - The refer-out triggers.
  - The Constraint Diagnosis.
- **Mentioned only inside other entries' definitions:** care minutes, stall taxonomy, age fork, fit window, non-response clause, and the Starter tool.
- The register holds only two ○ terms.

**Issue.** MAP line 272 promises that the Glossary will contain "every named framework and defined term". A glossary compiled from this register would miss the words readers meet most often.

**Fix.** Before Step 3, add ○ rows (owner plus a one-line definition) for these terms. That way each module's first-use definition and the Glossary share one wording.

#### AUD-16 · Major · "Floor" means five different things, including the standard's central test

**Location.** HOUSE_STANDARD (the floor of the Informed-Client Test). FRAMEWORKS, line 72 (★) and line 214 (◆). Brief 05 · Standard Check (line 169). Brief 12 · Stage notes (line 97). STYLE, line 52.

**Evidence.** The five meanings are:

| "Floor" as used | Meaning |
|---|---|
| The floor of the Informed-Client Test (HOUSE_STANDARD) | The House Standard's floor |
| ★ "One Flagship, Two Buffers, One **Floor**" | The Starter Path |
| ◆ "The Production **Floor**" | A production standard |
| "~5-hour content **floor**" | The protected content minimum |
| "Operations stay a **floor**" | Operations stay minimal |

- Brief 05's Standard Check says "**the floor offered once, never pushed**". It means the Starter Path, but it sits in the one block where "floor" means the House Standard's floor.
- FRAMEWORKS principle 4 requires a family word to "mean the same kind of thing every time". Its overlap check (lines 249–264) doesn't list "floor".

**Issue.** This is a collision readers will see, at the center of the standard. Brief 05's line reads as the opposite of the House Standard's floor, which says under-selling a good-fit buyer is a failure of care.

**Fix.**
- Reserve "floor" for the Informed-Client floor.
- Default changes:
  - In 05's Standard Check, write "the Starter Path, offered once".
  - Rename the Production Floor, for example to "the Production Bar".
  - Use the registered term "content minimum" instead of "content floor".
  - Write "operations stay minimal".
- Option: rename the ladder's "One Floor".

### Minor

#### AUD-17 · Minor · Retired or renamed names survive in MAP, BUSINESS, and the briefs

Stale names that should use the current register names:

| Stale name | Where | Current name or status |
|---|---|---|
| "the Reverse-Funnel Calculator" | MAP 04 | The Reverse Funnel |
| "(Signature System, light)" | MAP 05 | Folded into prose (FRAMEWORKS line 299) |
| "Packaging Is a Filter" | MAP 23 | Folded into prose |
| "the Three Gates" | MAP 27 | Ad Gates |
| "the Felt-Familiarity Premium" | MAP 08 | Registered only as a ○ term |
| "a public fill record" | BUSINESS §8 | The Fill History |
| "Why cash before audience" | Brief 10 §1 | Cash Before Audience is superseded |

Other inconsistencies:
- **"Spine" is still used for long-form** in MAP 23's shift ("One owned spine"), brief 23 §2 ("Why long-form is the spine"), and BUSINESS §1. FRAMEWORKS line 262 says "'spine' means the business only".
- **Module 25's title differs.** MAP says "25 · Instagram and X". The brief says "25 · Instagram and X: Routers and Arguments".
- **There is no "Transformation module"**, but BUSINESS §9 and MAP line 261 refer to one.

**Fix.** Search and replace, and pick one title for module 25.

#### AUD-18 · Minor · The glossary source is ambiguous, and the cast file is missing

- **Two files claim to feed the Glossary.**
  - STYLE line 23 says frameworks are "registered in `_build/REGISTRY.md`, which becomes the Glossary", and REGISTRY's header agrees.
  - FRAMEWORKS line 3 says it "supersedes REGISTRY.md", and that "The Glossary (Step 5.2) is compiled from here".
  - REGISTRY still carries retired names: Signature System, Cash Before Audience, and Reverse-Funnel Calculator.
- **The cast file doesn't exist.**
  - `briefs/part-1-2.md` line 5 ("The composite cast is defined in VOICE.md") and BUSINESS §12 ("defined in the Voice file") both point to it.
  - STYLE's Default cast lists the buyer states but gives the composites no names.

**Fix.**
- Point STYLE at FRAMEWORKS, and mark REGISTRY as history only.
- Point the briefs at STYLE's Default cast, or write the cast file with names.

#### AUD-19 · Minor · Secondary overlaps have no boundary row

- **The $50k levers** appear in three places: MAP 04 ("what $25k and $50k require"), MAP 13 ("the $50k levers"), and brief 28 §6.
- **13 §5's trigger table** restates triggers owned by 05, 06, 08, 11, 25, and 27.
- **Privacy** is owned twice: by MAP 07 ("privacy in delivery") and MAP 12 ("data and privacy operations"). It is taught again in 26 §6 and 27 §3.
- **Cash flow** is owned by MAP 08, but BUSINESS §10 gives it to the Operating Week.
- **The stage table** is owned by MAP 01 (the Stage Map), but BUSINESS §11 says "(owned by Growth Decisions …)".
- **The Training-Partner Seat** is registered as an Offer owned by 22 (FRAMEWORKS line 201). MAP line 262 gives 11 "The offers being asked for".
- **The founding price** sits in both 08 (the Price Path) and 10 (Founding Offers).
- **The education lane** is split. Brief 02 §4 covers "and what they get there", duplicating MAP 06's "(implementation)".

**Fix.**
- Make 13's trigger table and 28's lever list pointers only.
- Align BUSINESS's owner labels with the MAP.
- Move the Seat's offer design to 11.

#### AUD-20 · Minor (judgment call) · Naming families, and names on the edge of the Hostile-Screenshot Test

- **"Path"** names three different kinds of thing: a price sequence, an offer, and a content series. "The Starter Path" and "the Start Here Path" are especially easy to confuse.
- **"Ladder"** has four meanings: the Destination, Warmth, and Claim ladders, plus MAP 05's "the Ladder".
- **"Stack"** has three: the LTV, Context, and Proof stacks.
- **"Line"** means a test, a rule, the "lines we never cross", and "the AI line".
- **Module 28's phase "Leverage (months 6–9)"** clashes with BUSINESS §1, where leverage is the Scaling-stage lever ("then through lifetime value, then through leverage").
- **Three names read badly in a screenshot:**
  - "Every Plateau Is a Re-Sale": his plateau becomes a sales moment.
  - "The Buying Test Only You Pass": it reads as rigged.
  - "The Back-Dated Baseline": "back-dated" suggests falsified records.
- **There are 174 registered names**, about six per module, which puts SPEC §8's "memorable" at risk.

**Fix.**
- Rename the confusable Path pair and module 28's third phase.
- Re-run the Hostile-Screenshot Test on the three names above.
- Demote some ◆ entries to prose.

#### AUD-21 · Minor · Module 22's worked example under-asks against its own rule

**Evidence.**
- Brief 22's worked example runs "a cohort of ten … **four referral asks**". It also accounts for only 7 of the 10 clients: three renew, two join the Hold, one graduates clean, and one exits.
- The module owns "Ask Everyone, Privately", defined as "A direct, specific, private ask of every client at a peak" (FRAMEWORKS line 199).
- THESES P21 says "never skip the ask".

**Fix.**
- Ask every client at a measured peak. The exception is the client who exits, if no peak came.
- Account for all ten clients.

#### AUD-22 · Minor · Options and a default are missing where a real choice exists

- **Module 24 never picks a default set of short-form platforms** (TikTok, Reels, or Shorts).
  - D25 says "one or two platforms", and LEDGER F has the reach data.
  - Exposure to minors differs by platform.
- **Module 02 omits the core-buyer alternatives** that BUSINESS §2 records: Optimizer-first, breathing-first, and parent-funded teens.
- **05 §6's "new-creations catalog" is never listed out.**
  - This catalog is the spec's "plus new creations".
  - The actual new creations are owned in 06, 11, 20, and 22.

**Fix.**
- Add a default and options to 24 §1.
- Add the rejected buyer alternatives to 02 §1.
- Make 05 §6 an index with one line per new creation and a pointer to its owner.

#### AUD-23 · Minor · Buyer and ladder consistency

- **The core-buyer age range conflicts.**
  - BUSINESS §2 says "Core buyer … (range 19–28)".
  - THESES B17 says "Primary … (19–32; default protagonist mid-20s)".
  - BUSINESS merges the core buyer with the default protagonist.
- **The Optimizer (25–35) gets a targeted premium lane**, while BUSINESS §2 says men over 30 are "welcome, not targeted".
- **LEDGER B's Starter Path includes a "monthly group Q&A".**
  - It is a free, recurring live group for non-buyers, and fit-check signals route some people there.
  - It is the nearest thing in the architecture to a free community or a free live selling session, and no brief puts limits on it.
- **Brief 17 §6 refers to "the application as a commitment device".** The default door has an application step only for Private (BUSINESS §4).

**Fix.**
- Separate the core-buyer range from the protagonist range.
- State the Optimizer as "25–35, including over-30s by state".
- Put limits on the monthly group Q&A, or drop it and use templated checks by default.
- In 17, write "the self-assessment as a commitment device".

#### AUD-24 · Minor · Form and claim details

- **Module 28's Extras include no action steps.** STYLE's template (item 5) requires "action steps in every module".
- **Module 28's Argument overstates the outcome.** It says "Every band has a real business at the end of it". But LEDGER A3 shows Band A's month-9 profit at "~$0–13k", with the $25k floor reachable "Not on organic reach alone".
- **Opening frames use invented point results for composites.** Examples:
  - 24: "sends six adults to the door".
  - 26: "a 600-person list whose welcome sequence fills a cohort".
  - 12: "leads fall by half".
  - STYLE line 14 requires "bracketed placeholders or LEDGER ranges, never invented results".
- **The early-stage pointer (MAP line 28) omits 23 and 03.**
  - Long-form takes 5.0 of the roughly 20 hours in the Early week (LEDGER A4).
  - The Honest Answer is "your first long-form" (brief 03).
- **27 §3, "The Destination Rule and compliance (~900)", covers Risk Register flag 6 at length.** STYLE line 51 allows "one line elsewhere".

**Fix.** Fix each item where it occurs.

#### AUD-25 · Minor (judgment call) · Ecosystem weighting

- **X gets fewer words than the website and SEO.**
  - X gets about 1,950 words: 25 §4 plus its share of §1, §5, and §6.
  - The website and SEO get about 2,700 words: 27 §1–§3.
  - That inverts SPEC §5's "paid ads + website & SEO get less focus". One defense: the Verify Page is trust infrastructure.
- **The on-camera production extension is squeezed into a recap.**
  - INVENTORY and GAPS E4 flag it as the new material ("Add the face-era floor (light, framing, set)").
  - It sits inside 23 §6's ~500-word "recap".
  - Being on camera from day 1 is honored as policy but barely taught as craft.
- **The reused One-Defensible-Point Rule shares a heading** in 24 §5, even though the part-6-7 header says reused craft ideas get only a short native recap.

**Fix.**
- Trim 27 §1, or give the difference to 25 §4.
- Give the on-camera production standard about 300 words of its own in 23.

---

## Compliance table

| # | Checklist item | Result | Basis |
|---|---|---|---|
| 1 | Counts and order | **Pass** | See note 1. No findings. |
| 2 | Direction fidelity | **Pass** (minor notes) | See note 2. AUD-25. |
| 3 | Business parameters | **Partial** | See note 3. AUD-14, AUD-6 (solo scope), AUD-13, AUD-22, AUD-23. |
| 4 | Persuasion standard (Notch Map calibration) | **Partial** | See note 4. AUD-8, AUD-16, AUD-21, AUD-5, AUD-6. |
| 5 | Exclusions | **Pass** | See note 5. Latent risk in AUD-23. |
| 6 | Form | **Fail** | See note 6. AUD-1 (critical), AUD-2, AUD-24; AUD-3 puts the "never mentions a prior program" check at risk. |
| 7 | Build rules | **Partial** | See note 7. AUD-3, AUD-4, AUD-7, AUD-9 to AUD-12, AUD-15 to AUD-20. |
| 8 | Contradictions with THESES, LEDGER, or R1 | **Partial** | See note 8. AUD-4, AUD-5, AUD-6, AUD-7, AUD-8, AUD-13, AUD-21. |

**Notes on the basis for each result.**

1. **Counts and order.**
   - There are 28 modules: 13 business, 9 persuasion, 5 ecosystem, and the build plan.
   - Parts I–VII follow track order. Module 28 comes last and covers months 0–9.
   - The recap-and-point rule keeps each module self-contained while the book reads in order.
   - "About 14 business modules" is met by counting the business-led build plan as the 14th. That is how ~14 + ~9 + ~5, plus the plan, fits into 28.
2. **Direction fidelity.**
   - **Business:** the whole-business model (01), offers (05–07, 11), pricing (08), operations (12–13), and growth to profit (04, 13, 28).
   - **Persuasion:** trust, identity, and belief change, applied to content (18), sales (19–20), and transformation (21–22). Every brief pairs theory with application and excludes operator mindset.
   - **Ecosystem:** modules 23–27, with paid ads, the site, and SEO sharing one module.
3. **Business parameters.** These all pass:
   - Stage notes in all 28 briefs.
   - The $25–50k target, and a multi-year horizon.
   - No free community.
   - Every offer type is present:
     - One-to-one: founding 1:1 and Private.
     - Group: the Program.
     - Paid community: Community Options.
     - Digital: the Starter tool and the Self-Serve System.
     - New creations: the new rungs.
   - A cohort-led hybrid engine as the default.
   - A buyer who isn't a 180 from the sources. The sources use 17–32, 18–32, and 19–28; the architecture uses 19–28 and 19–32.
   - Face on camera, and a Name | Brand architecture.
   - Credential-agnostic scripts (15).
   - AI and legal kept minimal.
   - The Technique Firewall holds, and packaging stays light (05 §6).
4. **Persuasion standard.**
   - The calibration is mostly right:
     - 18 and 19 use both defaults and licensed variants.
     - 16 licenses teardowns, and 24 licenses clips.
     - No brief goes beyond the Notch Map.
   - The floor is under-audited: two licensed variants have no home, and many Standard Check lines cover only the ceiling.
   - Two items would breach deliberate tightenings if drafted as written: AUD-5 and AUD-6.
5. **Exclusions.**
   - No faceless, launch, mindset, podcast or collab, technique, or free-community recommendation appears anywhere.
   - The guardrails in 09, 10, 12, 15, 17, and 25 exclude them explicitly.
   - The only latent risk is LEDGER B's monthly Starter Path Q&A (AUD-23).
6. **Form.** These pass:
   - The hybrid template in every brief.
   - Named frameworks.
   - LEDGER ranges for numbers.
   - Research synthesized rather than cited.
   - One file per module, plus a README with a table of contents and a glossary.
   - No separate index or map.
7. **Build rules.**
   - Every module number in every cross-reference is correct. Every "Leans on", ↺, and pointer was checked.
   - The Technique Firewall is respected.
   - The problems are in single ownership, names, banned wording, and the register.
8. **Contradictions with THESES, LEDGER, or R1.**
   - Contradictions found: AUD-4 (R1-25), AUD-5 (B9 and STANDARD §7), AUD-6 (LEDGER H and B21), AUD-7 (P11), AUD-8 (B16 and R1-12), AUD-13 (LEDGER A), and AUD-21 (P21).
   - No architecture item follows a D-row that R1 superseded.

## Verdict

The architecture keeps to the locked spec in its structure. There are 28 modules in track order, with the nine-month build last. Every brief has stage notes, the hybrid template, and a Standard Check. No excluded strategy is recommended anywhere, and the Technique Firewall holds. The buyer and the ladder stay inside the spec's parameters, and every cross-reference points at the right module.

It is not ready to draft as written. One hard violation must be fixed first: module 28's budget of about 8,350 words. Fifteen majors would turn into violations or contradictions during drafting:

- **Banned wording (three):** the source-relative Nurture Jobs definition, clinical words in framework names, and the collision over "floor".
- **Clashes with the standard or the LEDGER (three):** the door diagram's paid step before the Fit Check, routing help handling first-pass DMs, and the public "seat math" piece.
- **The Notch Map (one):** it never reaches the briefs, so the floor goes unaudited and two licensed variants have no home.
- **Everything else (eight):** script budgets for 18–20, triple teaching of the same options, three owners for ask-licensing, double ownership of graduation, three wordings of the affordability question, engine numbers missing from the LEDGER, the operations count, and the incomplete glossary register.

Almost all of this is fixed by editing MAP, FRAMEWORKS, BUSINESS, and the briefs, not by restructuring. One question needs the user: how to count the spec's "operations" (AUD-14).

---

## Appendix A — Budget check

The default non-section blocks total 2,450 words (`part-1-2.md` line 4).

| Module | Deep sections | Total with defaults | | Module | Deep sections | Total with defaults |
|---|---|---|---|---|---|---|
| 01 | 4,700 | 7,150 | | 15 | 4,800 | 7,250 |
| 02 | 4,700 | 7,150 | | 16 | 5,000 | 7,450 |
| 03 | 4,700 | 7,150 | | 17 | 4,700 | 7,150 |
| 04 | 4,700 | 7,150 | | 18 | 4,800 | 7,250 (the scripts push it higher; AUD-2) |
| 05 | 4,700 | 7,150 | | 19 | 5,100 | 7,550 (the scripts push it higher; AUD-2) |
| 06 | 4,800 | 7,250 | | 20 | 4,800 | 7,250 (the scripts push it higher; AUD-2) |
| 07 | 5,000 | 7,450 | | 21 | 4,600 | 7,050 |
| 08 | 4,900 | 7,350 | | 22 | 4,600 | 7,050 |
| 09 | 4,600 | 7,050 | | 23 | 4,800 | 7,250 |
| 10 | 4,800 | 7,250 | | 24 | 4,700 | 7,150 |
| 11 | 4,700 | 7,150 | | 25 | 4,700 | 7,150 |
| 12 | 4,700 | 7,150 | | 26 | 4,700 | 7,150 |
| 13 | 4,800 | 7,250 | | 27 | 4,700 | 7,150 |
| 14 | 4,900 | 7,350 | | **28** | **5,900** | **~8,350 (over the ceiling; AUD-1)** |

The planned total is about 203k words, against the spec's figure of about 196k.

## Appendix B — Notch coverage in the briefs

| Notch | Named in the briefs' Standard Check focus | Does the licensed variant have a home? |
|---|---|---|
| 1 Direct selling | 10; 18 (default and stronger) | Yes: 18 §3 and §5, and 20 §5 (the DM Handoff) |
| 2 Closing | 19 | Yes: 19 |
| 3 Stakes | 19 (and 14's "floor on Now") | Yes: 19 §2 and 22 §3 |
| 4 Real dates | 09 (default and stronger) | Yes: 09, and 19 (the Decision Date) |
| 5 Outcome framing | 16 ("with its context") | Mostly: 14 §4, 16 §5, and 24 §5 |
| 6 Contrarian framing | 03 | Yes: 03 §4, and 16 §6 (teardowns) |
| 7 Identity | 11; 17 ("at its default") | Partly. Cohort sharing, founding-member and alumni status, and commitment devices are present; **opt-in leaderboards appear nowhere** |
| 8 Pricing | 05; 08 ("at its default"); 19 (stronger) | Yes: 08 §3 and 19 §3 |
| 9 Emotional directness | **none** | **No.** The forceful variant has no home |
