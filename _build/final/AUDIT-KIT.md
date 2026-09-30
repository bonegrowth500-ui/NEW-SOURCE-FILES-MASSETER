# 5.3 Final audit kit

The plan says: "Final audits: exclusions, zero mentions of the sources, word budgets, the persuasion card, stage notes, template completeness, and file naming."

One auditor per Part (I–VI), plus one for Module 28, `README.md` and `glossary.md`. Each fixes in place and logs its changes. Fixes stay small and word-neutral. Anything that would need a rewrite is logged for the orchestrator instead of fixed.

## Load
- `_build/SPEC.md` (§1, §7 exclusions, §8 form).
- `_build/HOUSE_STANDARD.md` and `_build/STANDARD.md`: the persuasion card, with its ceiling, floor, nine licenses, six lines, and Stop Rules.
- `_build/CRITIQUE.md`: section B, the House Standard in both directions.
- `_build/VOICE.md` (rules) and `_build/STYLE.md`.
- `_build/DRAFTING.md`: the skeleton and budgets, plus the Standing rulings.
- `_build/DECISIONS.md`: R3 and R4.
- `_build/LEDGER.md`: only as needed to check a number you touch.
- Your Part's 4.1 log in `_build/integration/4.1-partN.md`. Its "4.2 Depth upgrade" section names the sections rebuilt in 4.2, which no critic has reviewed yet.

## Run first
- `python3 _build/tools/audit.py <module>` for each module: 0 FAIL, and words inside 6,300–7,700.
- `python3 _build/tools/final_audit.py sources exclusions card quotes links`, then judge each hit. Exclusion mentions that rule a thing out are fine, and so are grift patterns named in order to fight them. Techniques taught, a launch run, or a structural promise made are not fine.

## Read and check, per module
1. **The persuasion card, both directions.** Read the whole module fast. Read slowly: the sections rebuilt in 4.2, every script, template, and email, and the worked example.
   - **Ceiling:** the six lines never crossed (fabricated proof, structural claims, fake scarcity or urgency, shame, vulnerability including minors and money, credentials). Stop Rules bind scripts and automation. The affordability question is verbatim before every paid step. No downsell after a no. The credit never sits beside a date. The pause route holds every marketing send. A protective stop leaves only "stopped: stop rule" (a minor's leaves nothing). Asks wait for a measured peak.
   - **Floor:** each license in play is used at strength where the module licenses it: *Sell directly*, *Close*, *Name the stakes*, *Use real dates*, *Name the destination boldly*, *Fight ideas, not people*, *Build identity on evidence*, *Present the price*, *Say the true thing*. A screened, good-fit buyer is never left un-asked.
2. **Exclusions.** Faceless strategy, launch campaigns, operator mindset or self-help, podcasts and collabs, facial-development techniques or protocols, and a free community are all out. The method stays out.
3. **Zero mentions of sources** or prior programs, and no source-relative phrasing.
4. **Word budget:** inside the band, with section weights near DRAFTING's (Part V and 28 have their own).
5. **Stage Notes:**
   - the `*Stages:*` key line;
   - Early, Growing, and Scaling each present, specific to this module, and stating its traps rather than restating the body.
6. **Template completeness** (DRAFTING skeleton), in order:
   - the title and Part line, then the shift line;
   - the opening, then six numbered sections, one holding a "**When the signals disagree.**" run-in;
   - the worked example (28 is exempt), then 1–3 extras headings;
   - Stage Notes, the Standard Check, and the Quick Reference, which carries In one line, Takeaways, the cheat sheet, Leans on, and Do this month.
   - Standard Check bullets are specific to this module.
7. **File naming and links.** Names follow MAP, and every relative link resolves.

## Log: `_build/final/5.3-<scope>.md`
```
# 5.3 — <scope>
## Fixed | Module | Where | Was → Now | Card line or rule |
## Logged for the orchestrator (not fixed) | Module | Where | Problem | Suggested fix |
## Checks passed per module (one line each)
```
Report in ≤120 words.
