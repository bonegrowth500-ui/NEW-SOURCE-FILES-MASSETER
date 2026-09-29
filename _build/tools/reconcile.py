#!/usr/bin/env python3
"""Step 4 global checks across all module files (read-only).

Checks:
  canon   - quoted sentences that closely resemble a Canon claim but differ from it
  stages  - the *Stages:* key line differs from the most common form
  cast    - composite labels and ages that disagree with the fixed cast
  qr      - Quick Reference parts missing (In one line, Takeaways, Leans on, Do this month)
  pointer - "(Module N)" pointers following a registered term whose owner is not N

Usage: python3 _build/tools/reconcile.py [check ...]   (default: all)
"""
import collections, difflib, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODS = sorted(glob.glob(os.path.join(ROOT, '[0-2][0-9]-*.md')))

CANON = [
    "There's no good evidence that habits change the shape of an adult's bone, and I don't sell that.",
    "Some things are debated, and I'll tell you where the evidence is thin.",
    "A lot does change and can be measured: your habits, your body composition, how you carry yourself, your grooming, how you're photographed.",
    "Most stalls we see are direction problems: months of real effort with no map and nothing measured.",
    "Measuring is how you'd know if yours is.",
    "Behavior gets measured every week; appearance gets captured rarely, the same way every time.",
    "A record doesn't read itself; review turns it into a decision.",
    "By week 6 your record shows what's moving, and by week 12 it can tell you a lever doesn't move for you.",
    "My face is not evidence for the method.",
    "The record is, published on the dates I committed to.",
    "Most of how people read you was never about your jaw.",
]

CAST = {'Dan': '24', 'Theo': '26', 'Adrian': '31', 'Sam': '22', 'Maya': '28', 'Jordan': '16'}


def norm(s):
    return re.sub(r'\s+', ' ', s.replace('’', "'").replace('“', '"').replace('”', '"')).strip()


def sentences(text):
    return re.split(r'(?<=[.!?;])\s+', text)


def check_canon():
    out = []
    for f in MODS:
        name = os.path.basename(f)[:2]
        for i, line in enumerate(open(f, encoding='utf-8'), 1):
            ln = norm(line)
            for sent in sentences(ln):
                s = sent.strip(' "*>-_')
                if len(s) < 25:
                    continue
                for c in CANON:
                    r = difflib.SequenceMatcher(None, s.lower(), c.lower()).ratio()
                    if 0.80 <= r < 0.999 and c.lower() not in ln.lower():
                        out.append(f"{name} L{i}: ~{r:.2f} to canon\n    text : {s[:160]}\n    canon: {c}")
    return out


def check_stages():
    lines = {}
    for f in MODS:
        for i, line in enumerate(open(f, encoding='utf-8'), 1):
            if line.startswith('*Stages:'):
                lines[os.path.basename(f)[:2]] = (i, line.strip())
    common = collections.Counter(v[1] for v in lines.values()).most_common(1)
    out = []
    if common:
        base = common[0][0]
        for m, (i, l) in sorted(lines.items()):
            if l != base:
                out.append(f"{m} L{i}: stages key differs\n    {l[:200]}")
        missing = [os.path.basename(f)[:2] for f in MODS if os.path.basename(f)[:2] not in lines]
        if missing:
            out.append(f"missing *Stages:* line: {', '.join(missing)}")
    return out


def check_cast():
    out = []
    pat = re.compile(r'\b(Dan|Theo|Adrian|Sam|Maya|Jordan)\s*\*\(([^)]*)\)\*,?\s*(\d{2})?')
    for f in MODS:
        name = os.path.basename(f)[:2]
        for i, line in enumerate(open(f, encoding='utf-8'), 1):
            for m in pat.finditer(line):
                who, label, age = m.group(1), m.group(2), m.group(3)
                if age and age != CAST[who]:
                    out.append(f"{name} L{i}: {who} age {age} (fixed {CAST[who]})")
                if who == 'Jordan' and 'minor' not in label.lower():
                    out.append(f"{name} L{i}: Jordan label lacks 'minor': ({label})")
    return out


def check_qr():
    out = []
    need = ['**In one line.**', '**Takeaways**', '**Leans on:**', '**Do this month:**']
    for f in MODS:
        t = open(f, encoding='utf-8').read()
        qr = t.split('## Quick Reference')[-1] if '## Quick Reference' in t else ''
        miss = [n for n in need if n not in qr]
        if not qr or miss:
            out.append(f"{os.path.basename(f)[:2]}: Quick Reference missing {miss or 'section'}")
    return out


def load_owners():
    owners = {}
    fw = open(os.path.join(ROOT, '_build', 'FRAMEWORKS.md'), encoding='utf-8').read()
    for row in fw.splitlines():
        if not row.startswith('|'):
            continue
        cells = [c.strip() for c in row.strip('|').split('|')]
        if len(cells) < 3:
            continue
        # tiered rows: | tier | **Name** | gloss | new/extended | owner | recaps |
        m = re.search(r'\*\*([^*]+)\*\*', cells[1]) if len(cells) >= 5 else None
        if m and re.fullmatch(r'\d{2}', cells[4] if len(cells) > 4 else ''):
            owners[m.group(1).strip().lower()] = int(cells[4])
            continue
        # register rows: | term · term | gloss · gloss | owner |
        if re.fullmatch(r'\d{2}', cells[-1]):
            for term in cells[0].split('·'):
                term = re.sub(r'[*_]', '', term).strip().lower()
                if 3 <= len(term) <= 60:
                    owners[term] = int(cells[-1])
    return owners


def check_pointer():
    owners = load_owners()
    out = []
    terms = sorted(owners, key=len, reverse=True)
    for f in MODS:
        name = os.path.basename(f)[:2]
        for i, line in enumerate(open(f, encoding='utf-8'), 1):
            if line.startswith('**Leans on:**'):
                continue
            for m in re.finditer(r'\(Module (\d{1,2})\)', line):
                n = int(m.group(1))
                before = line[max(0, m.start() - 90):m.start()].lower()
                for t in terms:
                    if t in before and before.rfind(t) > len(before) - len(t) - 45:
                        if owners[t] != n and owners[t] != int(name):
                            out.append(f"{name} L{i}: '{t}' owned by {owners[t]:02d}, pointer says {n}")
                        break
    return out


CHECKS = {'canon': check_canon, 'stages': check_stages, 'cast': check_cast, 'qr': check_qr, 'pointer': check_pointer}

if __name__ == '__main__':
    which = sys.argv[1:] or list(CHECKS)
    for w in which:
        res = CHECKS[w]()
        print(f"== {w}: {len(res)} finding(s)")
        for r in res:
            print('  ' + r)
