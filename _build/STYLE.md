# STYLE v3 — scope and hard rules for every module (aligned with R2)

**Precedence:** SPEC → HOUSE_STANDARD (claims) → **STYLE (scope and hard rules)** → VOICE (how it reads) → `voice/sample-v2.md`. The canonical sources are:
- names and owners: FRAMEWORKS v2;
- numbers: LEDGER v3;
- the default business: BUSINESS v2;
- module jobs and boundaries: MAP v2;
- per-module plans: `briefs/` v2.

## Voice
The voice is locked in `VOICE.md` (twenty rules, formats, vocabulary, pre-commit checks). In short:
- Second person, operator to operator ("you").
- Calm authority with conviction; direct, never hypey.
- Optimistic because the plan is sound, not because outcomes are promised.
- Every recommendation carries its reason.
- Theory plus application: name the psychological or economic mechanism, then show how it works in this niche.

## Default cast
Fixed in `VOICE.md` §2, and never contradicted or extended:
- **Buyers:** Dan (24, the Struggler and default protagonist), Theo (Burned), Adrian (Optimizer), Sam (Ambivalent), Maya (welcome, not targeted), Jordan (minor, education lane only).
- **Operators:** Cole (the default path) and Reid (the contrast).

Other rules:
- The core buyer is 19–32. Eligibility is the age fork plus the canonical affordability question, never student status or income targeting.
- Composites are labeled as composites. Numbers inside examples are bracketed placeholders or LEDGER ranges, never invented results.

## Niche grounding and the Technique Firewall
- Every module is about a facial-development coaching business: the buyers, the category's grift history, the adult "is it too late?" question, stalls, skepticism, photos, measurement, presentation.
- **Technique Firewall:** the method is never taught.
  - In examples and scripts, method content appears only as bracketed placeholders ("[first adjustment]", "[weekly habit block]") or at category level ("a consistency problem, not a technique problem").
  - Topics appear as titles and angles, never as instructions.
  - Packaging the method (naming, structure, deliverables, capture standard) is in scope.
- **The Outcome Map governs every outcome sentence.**
  - For adults, these are changeable and measurable: habits, body composition, posture and breathing *habits*, grooming, presentation, and how they're photographed.
  - Visible jaw or profile change from habits is debated, and is presented at its evidence tier.
  - Habit-driven skeletal change is never claimed.
  - "Bone growth" and "mewing" are category search terms the brand explains; they are never its promise or its identity.
- **Referral triggers** are named where relevant and never elaborated into health advice: sleep or snoring signs, jaw pain, bite concerns, distress or fixation, minors.
- The operator is on camera from day one. The operator's face is a trust carrier, never evidence.

## Named frameworks
- Every framework and defined term is registered in `FRAMEWORKS.md`, with one owner and its tier: ★ flagship, ◆ tool, or ○ term. The Glossary is compiled from it. REGISTRY.md is history only.
- **Glass-box naming:** every name must pass the Hostile-Screenshot Test. A buyer who saw it would find it accurate and unoffensive.
- Frameworks are presented as **options plus a default pick** wherever a real choice exists, in the VOICE §3.2 format.

## Numbers and evidence
- **Ranges with context, always:** "typically X–Y; higher when…, lower when…".
  - No false precision.
  - No single-point statistics except fixed process facts and the ledger's fixed thresholds.
  - Every number matches `LEDGER.md`.
- **Planning ranges are presented as planning ranges,** to be replaced by the operator's own ratio after about 30 events. None is ever framed as a result the brand has achieved.
- **Research is synthesized in the playbook's own words:** no citations, no study names, no author names. Weak or contested effects are described as small or conditional. No pop neuroscience.
- **Outcome language follows "observed, not caused":** no causal verbs for appearance change.

## Banned phrasing
The full lists are in `VOICE.md` §4, and are grepped before every commit:
- **Source-relative comparisons.** No sentence compares this playbook, its standard, or its advice to any earlier material. This includes "used to do", "once did", "anymore", "than before", "unlike before", "previously", and "the old way". Concepts are defined natively. A hit is allowed only when it describes the buyer or the business itself.
- **No mention of the source files,** or of any "prior program", course, or blueprint.
- **Clinical and therapeutic vocabulary** is out, including in the playbook's own analysis. That covers the whole diagnose family and treat, therapy, healing, patient, and protocol. A word is mentioned in quotation marks only where the Plain-Language Rule is taught or a House Standard line names what's out.
- **Reserved words:** "floor" means only the Informed-Client floor; "the Spine" means only the Intro's one-page view.

## Module template (hybrid)
The skeleton is in `VOICE.md` §3.1:
1. Title, Part line, the shift line, and an opening frame of about 200 words.
2. Six deep numbered `##` sections, each running mechanism → reasoning → application in the niche.
3. Named frameworks with variants and a default pick, introduced in five beats.
4. One worked example: a composite case walked end to end.
5. Extras chosen per module type:
   - scripts and swipe copy for persuasion, sales, and content modules;
   - checklists and templates for business and ecosystem modules;
   - one "When the signals disagree" hard case in every module.
6. **Stage Notes:** Early, Growing, and Scaling (LEDGER A2), covering what changes and which constraint binds for this module's topic.
7. **Standard Check:** 2–4 module-specific bullets naming House Standard items by name, covering the ceiling and floor, the licenses in play, the lines, and stop rules.
8. **Quick Reference:**
   - one line;
   - takeaways;
   - decision tables;
   - a cheat sheet of owned frameworks;
   - "Leans on:";
   - "Do this month:" (three actions, replacing a separate action-steps block).

## Hard rules
- **Cross-references use "(Module N)",** sparingly, per VOICE rule 11. Each module stays self-contained, and recaps of other modules are at most two sentences.
- **The exclusions never appear as recommendations:** faceless strategy, launch campaigns, operator mindset or self-help, podcasts and collabs, techniques and methods, a free community.
- **AI tools stay minimal** (the AI rule: "AI assists behind the scenes, never speaks as you, and clients are told where it helps").
- **Legal and risk stay minimal.** The Risk Register (Module 11) holds the biggest flags, with one line elsewhere where relevant.
- **Operations stay minimal.**
  - Operations proper are the Operating Week (11) plus 01's math, held at planning depth.
  - Pricing (07) and growth (12, 13) are their own spec areas.
  - At most six metrics per stage, plus guardrails.
- **Length:** per VOICE rule 20. The default is about 7,030 words, with an audit band of 6,300–7,700. Part V and Module 28 carry their own splits inside the same band.
