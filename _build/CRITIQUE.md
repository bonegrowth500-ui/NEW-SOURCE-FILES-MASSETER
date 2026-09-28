# CRITIQUE RUBRIC — Step 3.3 (fresh-eyes adversarial review of one module)

You are the adversarial reviewer for one drafted module of *The End of Guessing*. You did not write it and owe it nothing. Your job is to find every place where it is shallow, padded, generic, off-voice, off-spec, off-ledger, or where its persuasion either crosses the line or under-sells. A soft review costs the reader: the module gets rebuilt from what you find.

Repo root: `/home/user/NEW-SOURCE-FILES-MASSETER`. Bible: `_build/`.

## Read
1. The module file (repo root) — read it fully, twice: once as the target reader (a solo operator, early stage, 20–25 h/week, smart and skeptical, wants mastery), once as an auditor.
2. Its brief in `_build/briefs/` (`## NN · Title`) — the contract.
3. `_build/VOICE.md` and `_build/voice/sample-v2.md` (the calibrated density and rhythm).
4. `_build/HOUSE_STANDARD.md` and `_build/STANDARD.md` (ceiling, floor, the nine licenses with under-use checks, six lines, stop rules, deliberate tightenings).
5. `_build/SPEC.md`, `_build/STYLE.md`.
6. `_build/MAP.md` (this module's Owns / Leans on, and the boundary table) and `_build/FRAMEWORKS.md` (names and owners).
7. `_build/LEDGER.md` (every number must match) and `_build/BUSINESS.md` (the default business).
8. Summaries of already-drafted modules in `_build/summaries/` (to catch contradictions and double-teaching).
9. Run `python3 _build/tools/audit.py <module file>` and use its output.

## Hunt for (in priority order)

**A. Depth and substance.**
- Sections that assert without a mechanism, skip the reason, or stop before the signs and moves. Where would the reader say "yes, but how?" or "why?"
- Flagship frameworks missing any of the five beats, or never run on a case.
- Filler: restatement, throat-clearing, triple-saying, summaries of what was just said, transitions that preview, padding to hit the budget.
- Generic advice: any paragraph that survives the niche swap test (swap "facial-development coaching" for "fitness coaching" and nothing breaks). Name each one.
- A worked example that illustrates instead of deciding: it must show signs → read → default move → what was left alone → outcome as a range, and teach something the sections didn't.
- Extras that are generic, too thin to use tomorrow, or scripts that don't end at a decision or a stop rule.
- Missing items from the brief (sections, owned frameworks, extras, the hard case, stage-note angles).

**B. The House Standard, both directions.**
- *Ceiling / lines:* anything a client at the low end of the range wouldn't endorse in hindsight; structural or appearance promises; claims beyond the Outcome Map; fake urgency or countdown logic; shame or worth-aimed force; selling past a stop rule (including automation); minors; affordability failures; prior spend near the price; the operator's face as proof; implied credentials; decoys, invented value, or fake discounts.
- *Floor / under-use:* for every license in the brief's "Licenses in play" line, answer its under-use question against the text. Flag scripts where a good-fit buyer is left un-asked, un-probed, or with the stake unnamed; prices apologized for or hidden; destinations described only as mechanics; categories left unchallenged; hard true things talked around.

**C. Voice (VOICE.md's twenty rules).** Recommendations without reasons; paragraphs over 130 words or walls of short ones; contrast-budget overuse ("not X, but Y"); frameworks named before shown; options left undecided; house nouns before their gloss; cross-reference density; certainty words outside House Standard/ledger thresholds; superlatives; "~" in prose; bold misuse; script format; cast violations; headings; fixed blocks doing jobs they shouldn't (Stage Notes restating the body; Standard Check bullets that could move to another module unchanged).

**D. Spec and ownership.** Teaching another module's owned concept beyond a two-sentence recap; contradicting another module's summary; exclusions (faceless, launches, mindset, podcasts/collabs, techniques, free community); AI or legal beyond minimal; any mention of sources or earlier material; source-relative phrasing; banned vocabulary (the diagnose family, clinical "treat", protocol, patient, therapy, healing, cure, restore/remodel/reshape).

**E. Numbers.** Every number against LEDGER (quote the line and the LEDGER row it should match); single-point outcome numbers; composite numbers not bracketed or not in LEDGER ranges; math that doesn't add up.

## Write `_build/critiques/NN.md` (≤1,500 words)

```
# Critique — NN · Title
Verdict: [ready after minor fixes | needs targeted rebuild | needs major rebuild] · Words: [n] (band 6,300–7,700)

## The three weakest sections (rebuild these first)
1. [Section] — what's wrong (specific), what the rebuilt section must do (specific enough to act on)
2. …
3. …

## Findings
| # | Severity (blocking/major/minor) | Where (heading + ≤15-word quote) | Problem | Fix |

## Under-use check (each license in play)
- *License:* used at default? stronger variant used where licensed? → verdict + where to add

## Ledger mismatches
- quote → LEDGER row → correct range

## Ownership and spec
- …

## What's strongest (keep it)
- two or three lines, so the rebuild doesn't sand them off
```

**Blocking** = crosses a House Standard line, breaks the spec or exclusions, mentions sources, invents a number presented as fact, or leaves a required template part missing. **Major** = shallow or generic section, missing brief item, under-use of a license, voice-rule violations that recur, ownership overlap. **Minor** = local wording, isolated voice slips.

Report back to the orchestrator in ≤100 words: verdict, finding counts by severity, the three weakest sections by name. Don't edit the module.
