# LEDGER v3 model (Step 2.5 revision): full-cost design weeks, capacity with milestones,
# configurations under the cash ceiling, Round Two per graduate, Hold ramp, Private at parity,
# founding group on overflow, labeled warm-network source. DERIVED planning numbers.

WK = 4.33  # weeks per month

# ---------- per-enrollment and per-client time components ----------
milestones_h = (0.75, 1.25)   # Commit Ritual/72h touch + written week-6 read + week-12 re-assessment, beyond weekly review
selling_h = {'early': (2.5, 6.0), 'growing': (1.5, 3.0), 'scaling': (0.8, 1.5)}  # per enrollment (scaling: ~60-70% no-call)

def care_min_per_client_week(review, clients, call_h, ms):
    return review + call_h * 60 / max(clients, 1) + ms * 60 / 12  # milestones spread over 12 weeks

print("Care minutes per client-week (review + amortized call + milestones):")
for label, review, clients, call_h, ms in [('early/founding', 18, 6, 1.0, 1.25), ('growing', 10, 25, 2.0, 1.0), ('scaling', 7, 40, 2.5, 0.8)]:
    m = care_min_per_client_week(review, clients, call_h, ms)
    print(f"  {label}: {m:.1f} min")

# capacity: concurrent clients that fit in the care hours available at each stage
for label, care_h, per in [('growing', 9.0, 19.0), ('scaling', 10.5, 14.0)]:
    conc = care_h * 60 / per
    months_care = 12 / WK * (1 + 0.18 * 0.5)   # Program + Round Two (maintenance, half minutes) at ~18% of graduates
    print(f"capacity {label}: {care_h} care h/wk at {per} min -> {conc:.0f} concurrent -> ~{conc / months_care:.1f} new enrollments/month")

# ---------- design weeks (h/week) ----------
weeks = {
 'Early (m0-3)': {
  'Long-form (every other week after the Honest Answer)': 2.5,
  'Short-form (4-7 native/week, batched): the early reach engine': 3.5,
  'Email (result email + welcome flow; no weekly broadcast yet)': 0.5,
  'Public replies, permission-first replies, routing': 2.0,
  'Personal reply to every adult lead (speed to lead)': 1.0,
  'Held conversations (4-5 x ~1.0 h all-in, 45-min call)': 4.5,
  'No-shows, recaps, follow-up': 0.5,
  'Founding group delivery (1:1-level review while < ~4 members) + milestones': 2.5,
  'Fit-check conversations, Starter Path hand-offs': 0.25,
  'Building (door v0, founding page, capture standard v1, check-in form)': 1.5,
  'Admin + Operator Review': 1.0,
 },
 'Growing (~$8-25k; ~15-30 clients)': {
  'Long-form (3/month)': 3.5,
  'Short-form (clips + a few native)': 1.25,
  'Weekly email': 1.0,
  'Public replies + routing': 1.0,
  'Lead handling (speed to lead, templated)': 0.5,
  'Conversations + assessments (cap-and-overflow)': 3.0,
  'No-shows, recaps, follow-up': 0.5,
  'Client review (~20-25 x ~10 min)': 3.75,
  'Group calls (combined, then split by stage)': 2.0,
  'Milestones (Commit Ritual, week-6 read, week-12 re-assessment)': 1.5,
  'Hold (measurement subscription) + Private (0-1 seat)': 0.75,
  'Renewal reviews, fit-check conversations, Starter Path': 0.5,
  'Building (protected build line: templates, async arc)': 1.25,
  'Admin, freelancer briefs, Operator Review': 1.5,
 },
 'Scaling at ~$25k (~8-9 enrollments/month)': {
  'Long-form (2-3/month)': 3.0,
  'Short-form approvals': 0.5,
  'Weekly email': 1.0,
  'Public replies': 0.75,
  'Lead handling': 0.25,
  'Selling (8-9 enrollments x ~1.3 h, ~50% no-call)': 2.6,
  'No-shows, recaps, follow-up': 0.5,
  'Client review (~24 x ~8 min)': 3.2,
  'Group calls': 2.0,
  'Milestones (templated)': 1.6,
  'Round Two (maintenance format)': 0.35,
  'Hold reviews (~25-35 members, quarterly)': 0.4,
  'Private (~1 seat)': 0.6,
  'Renewals, flags, Starter Path': 0.5,
  'Building': 1.0,
  'Admin, freelancers, Operator Review': 1.5,
 },
 'Scaling at ~$50k (~12 enrollments/month)': {
  'Long-form (2-3/month)': 3.0,
  'Short-form approvals': 0.5,
  'Weekly email': 1.0,
  'Public replies (routing help moderates)': 0.5,
  'Lead handling': 0.25,
  'Selling (12 enrollments x ~1.0 h, ~65-70% no-call; async assessments)': 2.8,
  'No-shows, recaps, follow-up': 0.4,
  'Client review (Program ~19 x 7 min + Async ~14 x 6 min)': 3.6,
  'Group calls (Program only)': 2.0,
  'Milestones (templated)': 2.1,
  'Round Two (maintenance format)': 0.4,
  'Hold reviews (~55-65 members, quarterly)': 0.8,
  'Private (~2 seats, async-first, at parity)': 1.1,
  'Renewals, flags, Starter Path': 0.5,
  'Building': 1.0,
  'Admin, freelancers, Operator Review': 1.5,
 },
}
for w, lines in weeks.items():
    tot = sum(lines.values())
    content = sum(h for n, h in lines.items() if n.startswith(('Long-form', 'Short-form', 'Email', 'Weekly email', 'Public replies')))
    print(f"\n{w}: total {tot:.2f} h/wk; content minimum {content:.2f} h")

# ---------- configurations ----------
def config(name, lines, margin):
    rev = sum(v for _, v in lines)
    print(f"\n{name}: revenue ${rev / 1e3:.1f}k -> profit ${rev * margin[0] / 1e3:.1f}-{rev * margin[1] / 1e3:.1f}k")
    for n, v in lines:
        print(f"   {n}: ${v / 1e3:.2f}k")

rt_share = (0.10, 0.26)  # Round Two per GRADUATE: 50-65% show measured momentum x 20-40% uptake
print(f"\nRound Two per graduate: {rt_share[0]:.0%}-{rt_share[1]:.0%} (mid ~18%)")
config('$25k configuration (year ~2; Band B-C)', [
    ('Program 8.5/mo x $3.1k (proof band, at the core buyer ceiling)', 8.5 * 3100),
    ('Round Two 8.5 x 18% x $1.0k (maintenance format)', 8.5 * 0.18 * 1000),
    ('Hold ~30 members x $59 (ramping, ~12 months after first graduation)', 30 * 59),
    ('Decision Assessment fees from non-buyers (overflow door)', 1000),
    ('Private ~1 seat a quarter x $5k (spare minutes)', 5000 / 3),
], (0.78, 0.84))
config('$50k configuration (year 2-3; Band C-D)', [
    ('Program 7/mo x $3.9k (above band; 25-34 majority)', 7 * 3900),
    ('Program Async 5/mo x $2.8k (under the 20-24 ceiling)', 5 * 2800),
    ('Round Two 12 x 18% x $1.2k (maintenance format)', 12 * 0.18 * 1200),
    ('Hold ~60 members x $69 (~24 months after first graduation)', 60 * 69),
    ('Private ~2 seats a quarter x $8k (async-first, at parity)', 2 * 8000 / 3),
    ('Self-Serve System ~15 x $197', 15 * 197),
    ('Decision Assessment fees from non-buyers (async)', 2200),
], (0.78, 0.84))

# ---------- Private parity ----------
cohort_rev_per_care_h = []
for price, per_week_min in ((3500, 14), (3900, 14), (3100, 19)):
    care_h = per_week_min * 12 / 60
    cohort_rev_per_care_h.append(price / care_h)
    print(f"cohort ${price} at {per_week_min} care-min/client-week -> ${price / care_h:.0f} per care hour")
for price, hours in ((4000, 16), (6000, 16), (7000, 9), (9000, 9)):
    print(f"Private ${price} over {hours} h -> ${price / hours:.0f}/h")

# ---------- Hold ramp ----------
grads_per_month, take, churn = 8, 0.3, 0.06
m = 0
for month in range(1, 25):
    m = m * (1 - churn) + grads_per_month * take
    if month in (6, 12, 24):
        print(f"Hold members {month} months after first graduation (at {grads_per_month} grads/mo): ~{m:.0f}")

# ---------- month-3 waypoints with the founding group on overflow ----------
bands = {'A': (10, 20), 'B': (15, 30), 'C': (20, 40), 'D': (25, 50)}
warm = (2, 8)   # disclosed warm network + early replies, held conversations/month in months 1-3 (PL, labeled)
conv, close = (0.12, 0.20), (0.15, 0.35)
print()
for b, (lo, hi) in bands.items():
    c_lo = lo * conv[0] + warm[0]; c_hi = hi * conv[1] + warm[1]
    e_lo = c_lo * close[0]; e_hi = c_hi * close[1]
    print(f"m3 Band {b}: held conv {c_lo:.0f}-{c_hi:.0f}/mo (warm {warm[0]}-{warm[1]}) -> new clients {e_lo:.1f}-{e_hi:.1f}/mo -> cash ${e_lo * 1200 / 1e3:.1f}-{e_hi * 1500 / 1e3:.1f}k")

# ---------- view equivalents with 30-70% eligible ----------
for b, (e_lo, e_hi) in {'A': (25, 50), 'B': (60, 150), 'C': (150, 400), 'D': (400, 700)}.items():
    v_lo = e_lo / 0.7 / 5 * 1000; v_hi = e_hi / 0.3 / 2 * 1000
    print(f"Band {b} m9 view equivalent: ~{v_lo / 1e3:.0f}k-{v_hi / 1e3:.0f}k engaged long-form views/month")

# ---------- paid lead economics ----------
for ltv, conv_rate in ((1700, 0.015), (3000, 0.07)):
    print(f"revenue per eligible lead: ${ltv * conv_rate:.0f}")
for cpl, elig in ((25, 0.7), (30, 0.3)):
    print(f"cost per eligible paid lead: ${cpl / elig:.0f}")
# take-home months
for gross, label in ((42000, '20-24'), (59000, '25-34')):
    net = gross * 0.8 / 12
    print(f"{label} take-home ${net:.0f}: " + ", ".join(f"${p / 1e3:.1f}k={p / net:.2f}mo" for p in (2400, 2800, 3100, 3500, 3900, 4500)))
