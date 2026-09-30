#!/usr/bin/env python3
"""Step 5.3 mechanical final audit across the deliverables (read-only).

Sections:
  files      - deliverable set and names (MAP), stray root files
  links      - every relative markdown link in README.md, glossary.md and modules resolves
  sources    - zero mentions of source files, prior programs, or source-relative phrasing
  exclusions - hits for excluded topics, listed with context for judgment
  card       - House Standard phrase flags (fake urgency, structural claims, shame, credentials)
  quotes     - canonical wordings (affordability question, protective stop record)
  words      - module word counts against the 6,300-7,700 band (via audit.py)
"""
import glob, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODS = sorted(glob.glob(os.path.join(ROOT, '[0-2][0-9]-*.md')))
DOCS = MODS + [p for p in (os.path.join(ROOT, 'README.md'), os.path.join(ROOT, 'glossary.md')) if os.path.exists(p)]

EXPECTED = [
    '01-the-whole-business.md', '02-the-buyer.md', '03-the-honest-position.md', '04-offer-architecture.md',
    '05-the-door.md', '06-the-program.md', '07-price-plans-and-promises.md', '08-real-dates.md',
    '09-the-founding-phase.md', '10-lifetime-value.md', '11-the-operating-week.md', '12-growth-decisions.md',
    '13-the-premium-lane-and-the-road-to-50k.md', '14-the-belief-chain.md', '15-trust-without-credentials.md',
    '16-evidence-that-persuades.md', '17-identity-and-commitment.md', '18-content-that-sells.md',
    '19-the-sales-conversation.md', '20-selling-without-the-call.md', '21-onboarding-adherence-and-the-plateau.md',
    '22-renewal-and-referral.md', '23-long-form-where-trust-compounds.md', '24-short-form-reach-and-the-hook-lab.md',
    '25-instagram-and-x.md', '26-email-the-private-room.md', '27-the-hub-search-and-paid.md',
    '28-the-first-nine-months.md', 'README.md', 'glossary.md',
]

AFFORD = "Is this comfortable from your own income or savings, without new credit or buy-now-pay-later?"


def lines_of(p):
    return open(p, encoding='utf-8').read().splitlines()


def name(p):
    return os.path.basename(p)


def check_files():
    out = []
    root_md = sorted(n for n in os.listdir(ROOT) if n.endswith('.md'))
    for e in EXPECTED:
        if e not in root_md:
            out.append(f"missing deliverable: {e}")
    for n in root_md:
        if n not in EXPECTED:
            out.append(f"unexpected root file: {n}")
    for n in os.listdir(ROOT):
        if n.startswith('.') or n == '_build' or n.endswith('.md'):
            continue
        out.append(f"non-markdown item at root: {n}")
    return out


def check_links():
    out = []
    for p in DOCS:
        for i, l in enumerate(lines_of(p), 1):
            for m in re.finditer(r'\]\(([^)#\s]+)(#[^)]*)?\)', l):
                target = m.group(1)
                if re.match(r'https?://', target):
                    out.append(f"{name(p)} L{i}: external link {target}")
                    continue
                if target.startswith('_build') or '/_build' in target:
                    out.append(f"{name(p)} L{i}: link into _build: {target}")
                if not os.path.exists(os.path.join(ROOT, target)):
                    out.append(f"{name(p)} L{i}: broken link {target}")
    return out


SOURCE_PAT = re.compile(r"S\+|\bBlueprint\b|Master Guide|source file|the program you read|\bsequel\b|prior (?:program|course|material)|earlier (?:program|course|material)|previous (?:program|course|playbook)|as (?:covered|taught) (?:before|previously|elsewhere)", re.I)


def check_sources():
    out = []
    for p in DOCS:
        for i, l in enumerate(lines_of(p), 1):
            for m in SOURCE_PAT.finditer(l):
                out.append(f"{name(p)} L{i}: '{m.group(0)}' … {l[max(0, m.start()-50):m.end()+50]}")
    return out


EXCL = [
    (r'\bfaceless\b', 'faceless strategy'),
    (r'\blaunch(?:es|ed|ing)?\b(?! Line)', 'launch campaigns'),
    (r'\bpodcasts?\b', 'podcasts'),
    (r'\bcollabs?\b|\bcollaborations?\b', 'collabs'),
    (r'\bmindset\b|\bself-help\b', 'mindset'),
    (r'\bprotocols?\b', 'protocols (banned word)'),
    (r'\bfree community\b|\bfree group\b|\bfree Discord\b|\bfree Skool\b', 'free community'),
    (r'\bexercises?\b|\bmewing\b|\bchewing\b|\btongue posture\b', 'technique content'),
]


def check_exclusions():
    out = []
    for p in DOCS:
        for i, l in enumerate(lines_of(p), 1):
            for pat, label in EXCL:
                for m in re.finditer(pat, l, re.I):
                    out.append(f"[{label}] {name(p)} L{i}: … {l[max(0, m.start()-60):m.end()+60]}")
    return out


CARD = [
    (r'\blast chance\b|\btoday only\b|\bexpires? (?:tonight|today|soon)\b|\bonly \d+ (?:spots?|seats?) left\b|\bhurry\b|\bdon\'t miss\b|\bcountdown\b', 'fake urgency'),
    (r'\b(?:grow|widen|change|move|build) (?:your|his|the) (?:jaw|jawline|bone|maxilla|mandible)\b', 'structural claim'),
    (r'\bguaranteed results?\b|\bresults? guaranteed\b', 'outcome guarantee'),
    (r'\bugly\b|\bsubhuman\b|\bmog\b|\bLooksmax\w*\b|\bnormie\b', 'shame / rating culture'),
    (r'\bDr\.|\bdoctor-approved\b|\bclinically proven\b|\bcertified\b', 'credential claim'),
]


def check_card():
    out = []
    for p in DOCS:
        for i, l in enumerate(lines_of(p), 1):
            for pat, label in CARD:
                for m in re.finditer(pat, l, re.I):
                    out.append(f"[{label}] {name(p)} L{i}: … {l[max(0, m.start()-70):m.end()+70]}")
    return out


def check_quotes():
    out = []
    for p in DOCS:
        t = open(p, encoding='utf-8').read()
        for m in re.finditer(r'[Ii]s this comfortable from your own income[^"\n]*', t):
            q = m.group(0).rstrip('*_" ')
            if not AFFORD.startswith(q[:len(AFFORD)]) or (len(q) >= len(AFFORD) and q[:len(AFFORD)] != AFFORD):
                line = t[:m.start()].count('\n') + 1
                out.append(f"{name(p)} L{line}: affordability question differs: {q[:140]}")
        for m in re.finditer(r'"stopped:[^"]*"', t):
            if m.group(0) != '"stopped: stop rule"':
                line = t[:m.start()].count('\n') + 1
                out.append(f"{name(p)} L{line}: record text differs: {m.group(0)}")
    return out


def check_words():
    out = []
    audit = os.path.join(ROOT, '_build', 'tools', 'audit.py')
    for p in MODS:
        r = subprocess.run([sys.executable, audit, p], capture_output=True, text=True).stdout
        m = re.search(r'words: ([\d,]+)', r)
        w = int(m.group(1).replace(',', '')) if m else 0
        fails = len(re.findall(r'^FAIL', r, re.M))
        if not (6300 <= w <= 7700) or fails:
            out.append(f"{name(p)}: {w} words, {fails} FAIL")
    return out


CHECKS = {'files': check_files, 'links': check_links, 'sources': check_sources, 'exclusions': check_exclusions,
          'card': check_card, 'quotes': check_quotes, 'words': check_words}

if __name__ == '__main__':
    for w in (sys.argv[1:] or list(CHECKS)):
        res = CHECKS[w]()
        print(f"== {w}: {len(res)} finding(s)")
        for r in res:
            print('  ' + r)
