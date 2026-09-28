#!/usr/bin/env python3
"""Mechanical audit for one drafted module of The End of Guessing (Step 3.5).

Usage: python3 audit.py path/to/NN-module.md
Prints FAIL (must fix), FLAG (needs judgment), and PASS lines, then a list of
numbers to check against LEDGER. Exit code 1 if any FAIL.
"""
import re, sys, statistics, pathlib

CAST = {"Dan", "Theo", "Adrian", "Sam", "Maya", "Jordan", "Cole", "Reid"}
SPEAKERS = CAST | {"You"}
COMMON_NAMES = {"Mike", "Michael", "John", "Alex", "Chris", "Jake", "Ryan", "Tom", "Josh", "Matt",
                "Nick", "Ben", "Luke", "Kevin", "Jason", "Tyler", "Emma", "Sarah", "Jess", "Kate",
                "Mark", "Paul", "David", "James", "Daniel", "Marcus", "Ethan", "Noah", "Liam", "Leo",
                "Max", "Jack", "Harry", "Sophie", "Anna", "Lisa", "Tim", "Joe", "Nate", "Eli", "Owen",
                "Kai", "Zach", "Brandon", "Kyle", "Aaron", "Adam", "Carlos", "Omar", "Priya", "Raj"}

fails, flags, passes = [], [], []
def FAIL(m): fails.append(m)
def FLG(m): flags.append(m)
def OK(m): passes.append(m)

def wc(text):
    return sum(1 for t in text.split() if re.search(r"[A-Za-z0-9]", t))

path = pathlib.Path(sys.argv[1])
text = path.read_text()
lines = text.splitlines()
m = re.match(r"(\d\d)-", path.name)
modno = int(m.group(1)) if m else None
part_v = modno is not None and 18 <= modno <= 22
is28 = modno == 28

# ---------- structure ----------
blocks = []  # (heading, kind, body_lines)
cur_head, cur_kind, cur_body = "TITLE", "title", []
def kind_of(h):
    if re.match(r"^## [1-6]\. ", h): return "deep"
    if re.match(r"^## Worked Example", h): return "worked"
    if re.match(r"^## (Script|Scripts|Template|Templates|Checklist|Checklists)\b", h): return "extras"
    if h.strip() == "## Stage Notes": return "stage"
    if h.strip() == "## Standard Check": return "check"
    if h.strip() == "## Quick Reference": return "qr"
    return "other"
for ln in lines:
    if ln.startswith("## "):
        blocks.append((cur_head, cur_kind, cur_body))
        cur_head, cur_kind, cur_body = ln, kind_of(ln), []
    else:
        cur_body.append(ln)
blocks.append((cur_head, cur_kind, cur_body))

title_block = blocks[0][2]
nonempty = [l for l in title_block if l.strip()]
if nonempty and re.match(r"^# \d{1,2} · \S", nonempty[0]):
    OK("title line")
    tn = int(re.match(r"^# (\d{1,2})", nonempty[0]).group(1))
    if modno and tn != modno: FAIL(f"title number {tn} != file number {modno}")
else:
    FAIL("title line must be '# N · Title' (N unpadded)")
if len(nonempty) > 1 and re.match(r"^\*Part [IVX]+ — [^*]+\*$", nonempty[1]): OK("Part line")
else: FAIL("second line must be '*Part X — Part Title*'")
if any(re.match(r'^\*\*The shift:\*\* from \*"', l) for l in title_block): OK("shift line")
else: FAIL("missing '**The shift:** from *\"…\"* to *\"…\"*'")
opening_lines = [l for l in title_block if l.strip() and not l.startswith("# ") and not l.startswith("*Part") and not l.startswith("**The shift:**") and l.strip() != "---"]
opening_words = wc("\n".join(opening_lines))

kinds = [k for _, k, _ in blocks[1:]]
deep_heads = [h for h, k, _ in blocks if k == "deep"]
nums = [int(re.match(r"^## (\d)\.", h).group(1)) for h in deep_heads]
if nums == [1, 2, 3, 4, 5, 6]: OK("six numbered sections")
else: FAIL(f"deep sections must be ## 1.–## 6. in order; found {nums}")
if kinds.count("worked") == 1 or (is28 and kinds.count("worked") == 0): OK("worked example")
else: FAIL(f"worked example headings: {kinds.count('worked')} (need 1)")
ne = kinds.count("extras")
if 1 <= ne <= 3: OK(f"extras headings: {ne}")
else: FAIL(f"extras headings: {ne} (need 1–3, starting Script/Scripts/Template/Templates/Checklist)")
tail = kinds[-3:]
if tail == ["stage", "check", "qr"]: OK("fixed blocks in order at end")
else: FAIL(f"last three ## blocks must be Stage Notes, Standard Check, Quick Reference; got {tail}")
for h, k, _ in blocks:
    if k == "other": FAIL(f"unexpected ## heading: {h}")
    if "(Module" in h: FAIL(f"cross-reference in heading: {h}")

deep_text = "\n".join("\n".join(b) for _, k, b in blocks if k == "deep")
if "**When the signals disagree.**" in deep_text: OK("hard case run-in inside a deep section")
else: FAIL("missing '**When the signals disagree.**' run-in inside a deep section")

def block_text(kind): return "\n".join("\n".join(b) for _, k, b in blocks if k == kind)
qr = block_text("qr")
for need in ["**In one line.**", "**Takeaways**", "cheat sheet", "**Leans on:**", "**Do this month:**"]:
    if need.lower() in qr.lower(): OK(f"Quick Reference has {need}")
    else: FAIL(f"Quick Reference missing {need}")
st = block_text("stage")
if re.search(r"^\*Stages:", st, re.M): OK("stage key line")
else: FAIL("Stage Notes missing the italic '*Stages: …*' key line")
for s in ["**Early.**", "**Growing.**", "**Scaling.**"]:
    if s in st: OK(f"Stage Notes {s}")
    else: FAIL(f"Stage Notes missing {s}")

# ---------- word budgets ----------
total = wc(text)
if 6300 <= total <= 7700: OK(f"total words {total:,}")
else: FAIL(f"total words {total:,} outside 6,300–7,700")
bw = {k: wc(block_text(k)) for k in ["deep", "worked", "extras", "stage", "check", "qr"]}
per_deep = [(h, wc("\n".join(b))) for h, k, b in blocks if k == "deep"]
if part_v:
    tol = {"deep": (3500, 4400), "worked": (800, 1250), "extras": (1250, 1950)}
elif is28:
    tol = {"deep": (4300, 5200), "worked": (0, 10**6), "extras": (900, 1700)}
else:
    tol = {"deep": (4300, 5500), "worked": (500, 950), "extras": (350, 900)}
tol.update({"stage": (150, 260), "check": (90, 180), "qr": (180, 380)})
if not (120 <= opening_words <= 300): FLG(f"opening frame {opening_words} words (target ~200)")
for k, (lo, hi) in tol.items():
    if not (lo <= bw[k] <= hi): FLG(f"{k} block {bw[k]} words (target {lo}–{hi})")
budget_line = (f"opening {opening_words} · deep {bw['deep']} [" + ", ".join(f"{i+1}:{w}" for i, (_, w) in enumerate(per_deep))
               + f"] · worked {bw['worked']} · extras {bw['extras']} · stage {bw['stage']} · check {bw['check']} · qr {bw['qr']}")

# ---------- vocabulary ----------
def scan(pattern, label, severity, flags_re=re.I, quoted_ok=False):
    for i, ln in enumerate(lines, 1):
        for mm in re.finditer(pattern, ln, flags_re):
            ctx = ln[max(0, mm.start()-40): mm.end()+40].replace("\n", " ")
            quoted = bool(re.search(r'"[^"]*' + re.escape(mm.group(0)) + r'[^"]*"', ln)) or bool(re.search(r'“[^”]*' + re.escape(mm.group(0)), ln))
            msg = f"L{i} {label}: …{ctx}…"
            if severity == "FAIL" and not (quoted_ok and quoted): FAIL(msg)
            else: FLG(msg)
scan(r"\b(mis)?diagnos\w*", "banned (diagnose family)", "FAIL", quoted_ok=True)
scan(r"\bprotocols?\b", "banned (protocol)", "FAIL", quoted_ok=True)
scan(r"\b(sellable|down-path|defense meter|control lexicon)\b", "banned term", "FAIL")
scan(r"\bfix your face\b", "banned phrase", "FAIL", quoted_ok=True)
scan(r"\b(treat|treats|treated|treating|treatment|treatments)\b", "check 'treat' is not clinical", "FLAG")
scan(r"\b(therapy|therapeutic|therapist|healing|heal|cure|cured|cures|patients?)\b", "clinical vocabulary?", "FLAG")
scan(r"\b(restor\w*|remodel\w*|reshap\w*)\b", "structural verb?", "FLAG")
scan(r"\bbone growth\b", "'bone growth' only as a search term", "FLAG")
# sources and source-relative phrasing
scan(r"\b(blueprint|S-Tier|S\+|Master Guide|20-Module|source files?|prior program|the program you read)\b", "source mention", "FAIL")
scan(r"\b(as you learned|the old way|unlike before|than before|previously|used to do|once did|once handled|newly|looser)\b", "source-relative phrasing", "FAIL")
scan(r"\b(anymore|no longer|this time)\b", "source-relative? (ok if about the buyer/business)", "FLAG")
# hype and filler
scan(r"\b(secret|secrets|hack|hacks|game-changer|insane|crush|crushing|10x)\b", "hype", "FAIL")
scan(r"(the truth is|let that sink in|here's the thing|here’s the thing|at the end of the day|in this module,? you)", "filler", "FAIL")
scan(r"\b(the single most|worth more than any|can't buy any other way|most important|the only way)\b", "superlative", "FLAG")
# US spelling
scan(r"\b(behaviour\w*|colour\w*|organis\w*|analys(e|ed|ing)\b|programme\w*|centre\w*|favour\w*|licence\w*|judgement\w*|practis\w*|catalogue\w*|recognis\w*|prioritis\w*|optimis\w*|minimis\w*|maximis\w*|emphasis(e|ed|ing)\b|apologis\w*|realis\w*|utilis\w*)", "UK spelling", "FAIL")

# ---------- per-section rhythm ----------
def prose_paragraphs(body_lines):
    paras, buf, in_code = [], [], False
    for ln in body_lines + [""]:
        if ln.startswith("```"): in_code = not in_code; continue
        if in_code: continue
        s = ln.strip()
        if not s:
            if buf: paras.append(" ".join(buf)); buf = []
            continue
        if s.startswith(("#", "|", ">", "- ", "* ", "---")) or re.match(r"^\d+\. ", s) or (s.startswith("*") and not s.startswith("**")):
            if buf: paras.append(" ".join(buf)); buf = []
            continue
        buf.append(s)
    return paras

all_sent_lens, contrast_total, one_sentence_by_sec = [], 0, {}
for h, k, b in blocks:
    body = "\n".join(b)
    sec = h if k != "title" else "opening"
    if k in ("deep", "worked", "extras", "title", "stage", "check", "qr"):
        em = body.count("—") - sum(1 for l in b if l.startswith("*Part"))
        if em > 1: FLG(f"{sec}: {em} em dashes (≤1 per section)")
        for w in ("actually", "honestly"):
            c = len(re.findall(rf"\b{w}\b", body, re.I))
            if c > 1: FLG(f"{sec}: '{w}' ×{c} (≤1 per section)")
    paras = prose_paragraphs(b)
    ones = 0
    for p in paras:
        n = wc(p)
        if n > 130: FLG(f"{sec}: paragraph of {n} words (>130): {p[:70]}…")
        sents = [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"“(*\[])", p) if wc(s) > 0]
        if len(sents) == 1 and k == "deep" and not re.fullmatch(r"\*\*[^*]+\*\*\.?", p.strip()): ones += 1
        for s in sents:
            L = wc(s); all_sent_lens.append(L)
            if L > 45: FLG(f"{sec}: sentence of {L} words: {s[:70]}…")
    if k == "deep" and ones > 1: FLG(f"{sec}: {ones} one-sentence paragraphs (≤1 per section)")
    contrast_total += len(re.findall(r"\bnot [^.;:!?]{1,60}, but\b|\bisn['’]t [^.!?]{1,50}[.;] [Ii]t['’]s\b|\bnot [^.!?]{1,40}\. [Ii]t['’]s\b|\bit['’]s not [^.!?]{1,40}, it['’]s\b", body))
if all_sent_lens:
    med = statistics.median(all_sent_lens)
    (OK if 13 <= med <= 20 else FLG)(f"median sentence length {med} (target 14–18)")
limit = max(1, total // 700)
(OK if contrast_total <= limit else FLG)(f"contrast constructions {contrast_total} (budget ~{limit})")

# ---------- cross-references ----------
xrefs = re.findall(r"\(Module (\d+)\)", text)
if modno not in (1, 28):
    lim = total // 600
    (OK if len(xrefs) <= lim else FLG)(f"(Module N) pointers {len(xrefs)} (limit ~{lim})")
for x in xrefs:
    n = int(x)
    if n < 1 or n > 28: FAIL(f"pointer to non-existent Module {n}")
    if modno and n == modno: FLG(f"self-reference (Module {n})")
if re.search(r"\(Module 0\d\)", text): FAIL("pointer with leading zero, use (Module 5)")
for mm in re.finditer(r"\((\d\d)(?:, \d\d)*\)", text):
    FLG(f"brief-style pointer {mm.group(0)} — use (Module N)")
for mm in re.finditer(r"\b(see above|as we'll see|covered later|see below)\b", text, re.I):
    FAIL(f"forbidden pointer phrase: {mm.group(0)}")

# ---------- bold ----------
bold_other = {}
for i, ln in enumerate(lines, 1):
    if ln.lstrip().startswith("|"): continue
    for mm in re.finditer(r"\*\*([^*]+)\*\*", ln):
        t = mm.group(1).strip()
        if ln.lstrip().startswith(">") or re.match(r"^[A-Z][a-z]+:?$", t) and t.rstrip(":") in SPEAKERS: continue
        if t.endswith((".", ":", "?")) or t in ("Takeaways", "Framework cheat sheet") or t.startswith("Default"): continue
        bold_other.setdefault(t.lower(), []).append(i)
for t, ls in bold_other.items():
    if len(ls) > 1: FLG(f"bolded more than once (bold only at first use): '{t}' at lines {ls}")

# ---------- "~" in prose ----------
for i, ln in enumerate(lines, 1):
    s = ln.strip()
    if s.startswith("|") or s.startswith("```"): continue
    if s.startswith("*Stages:"): continue
    no_brackets = re.sub(r"\[[^\]]*\]", "", s)
    if "~" in no_brackets: FLG(f"L{i} '~' in prose (use about/roughly): {s[:80]}")

# ---------- cast ----------
for mm in re.finditer(r"\b([A-Z][a-z]+)\s*\*\(composite", text):
    if mm.group(1) not in CAST: FAIL(f"composite not in fixed cast: {mm.group(1)}")
for mm in re.finditer(r"^>\s*\*\*([A-Z][A-Za-z]+)\*\*", text, re.M):
    if mm.group(1) not in SPEAKERS: FAIL(f"speaker not in fixed cast: {mm.group(1)}")
for mm in re.finditer(r"\*\*([A-Z][A-Za-z]+):\*\*", text):
    if mm.group(1) not in SPEAKERS and mm.group(1) not in ("Default", "Why", "How", "Early", "Growing", "Scaling"): FLG(f"bold label '{mm.group(1)}:' — speaker outside cast?")
for nm in COMMON_NAMES:
    if re.search(rf"\b{nm}\b", text): FLG(f"name outside the fixed cast: {nm}")

# ---------- subsection headings ----------
for ln in lines:
    if ln.startswith("### "):
        ws = [w for w in re.findall(r"[A-Za-z][A-Za-z'’-]*", ln[4:])]
        caps = [w for w in ws[1:] if len(w) >= 4 and w[0].isupper()]
        if len(ws) >= 4 and len(caps) >= len([w for w in ws[1:] if len(w) >= 4]) and caps:
            FLG(f"### heading looks Title Case (use sentence case): {ln}")

# ---------- numbers to check ----------
numbers = []
for i, ln in enumerate(lines, 1):
    s = re.sub(r"\[[^\]]*\]", "", ln)
    for mm in re.finditer(r"(\$\s?\d[\d,.]*k?(?:[–-]\$?\d[\d,.]*k?)?(?:/month| a month)?|\d[\d,.]*(?:[–-]\d[\d,.]*)?\s?%|\b\d{2,}[–-]\d{2,}\b)", s):
        numbers.append((i, mm.group(0).strip(), ln.strip()[:90]))
    for mm in re.finditer(r"(?<![\d–-])\b(\d{1,3})%(?![–-])", s):
        if not s.lstrip().startswith("|"):
            FLG(f"L{i} single-point percentage in prose: {mm.group(0)} — ledger range or fixed threshold?")

# ---------- report ----------
print(f"AUDIT {path.name}")
print(f"words: {total:,} · {budget_line}")
for f in fails: print("FAIL", f)
for f in flags: print("FLAG", f)
print(f"PASS {len(passes)} checks")
print("NUMBERS (check each against LEDGER):")
seen = set()
for i, n, ctx in numbers:
    if (n, ctx) in seen: continue
    seen.add((n, ctx)); print(f"  L{i}: {n}  ←  {ctx}")
sys.exit(1 if fails else 0)
