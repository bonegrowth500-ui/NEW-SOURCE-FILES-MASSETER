# LEDGER v2 model: reach-banded waypoints (m3/m6/m9 + maturity), hours line-by-line, capacity.
# Conservative (c) and good (g) cases; ranges reported c..g. DERIVED planning numbers.

# ---------- capacity ----------
care_months_per_enroll = (12 + 0.3 * 12) / 4.33  # 12-wk flagship + ~30% take Phase 2 (12 wk) -> months of active care
for conc in (25, 35, 45):
    print(f"concurrent {conc} -> max new enrollments/mo ~{conc / care_months_per_enroll:.1f}")

# ---------- hours model (design weeks) ----------
weeks = {
 'Early (m0-3; 0-6 clients)': [
  ('Long-form (1/wk; per-project editor)', 5.0),
  ('Short-form native (4-7/wk, batched)', 2.0),
  ('Weekly email', 1.0),
  ('Public replies + routing (comments, IG, X)', 1.5),
  ('Personal reply to every adult lead', 1.0),
  ('Held fit conversations (4 x ~0.9 h all-in)', 3.5),
  ('No-shows, reschedules, recaps, follow-up', 0.5),
  ('Founding 1:1 delivery (4 x ~35 min/client-wk)', 2.5),
  ('Screen-flag talks + Starter Path touches', 0.25),
  ('Build: door v0, offer page, capture standard, check-in form', 1.5),
  ('Admin + weekly Operator Review', 1.25)],
 'Month 6 (founding group; ~8-15 clients)': [
  ('Long-form (1/wk)', 5.0),
  ('Short-form (freelance clips + native)', 1.5),
  ('Weekly email', 1.0),
  ('Public replies + routing', 1.25),
  ('Lead replies', 0.75),
  ('Held fit conversations (4-5 x ~0.8 h)', 3.5),
  ('No-shows, recaps, follow-up', 0.5),
  ('Client review (12 x ~15 min)', 3.0),
  ('One combined group call', 1.0),
  ('Screen flags + Starter Path', 0.25),
  ('Build: verify page, sample plan, alumni room', 0.5),
  ('Admin, freelancer briefs, Operator Review', 1.5)],
 'Growing (m9-18; ~20-30 clients)': [
  ('Long-form (3-4/mo)', 4.25),
  ('Short-form approvals + a few native', 1.0),
  ('Weekly email', 1.0),
  ('Public replies (task-billed routing help)', 1.0),
  ('Lead handling (templated, high-intent personal)', 0.5),
  ('Conversations / assessments (5 x ~0.75 h)', 3.75),
  ('No-shows, recaps, follow-up', 0.5),
  ('Client review (25 x ~10 min)', 4.0),
  ('Group calls (split by stage)', 2.0),
  ('Renewal reviews, flags, Starter Path', 0.5),
  ('Admin, freelancers, Operator Review', 1.5)],
 'Scaling (~35-45 clients)': [
  ('Long-form (2-3/mo)', 3.0),
  ('Short-form approvals', 0.5),
  ('Weekly email', 1.0),
  ('Public replies', 0.75),
  ('Lead handling', 0.25),
  ('Async-first assessments (5 x ~0.55 h)', 2.75),
  ('No-shows, recaps, follow-up', 0.5),
  ('Client review (40 x ~8 min)', 5.25),
  ('Stage group calls', 2.5),
  ('Private seats (0-2) or alumni reviews', 1.0),
  ('Renewals, flags, Starter Path', 0.5),
  ('Admin, freelancers, Operator Review', 1.5)],
}
content_keys = ('Long-form', 'Short-form', 'Weekly email', 'Public replies')
for w, lines in weeks.items():
    tot = sum(h for _, h in lines)
    cont = sum(h for n, h in lines if n.startswith(content_keys))
    print(f"\n{w}: total {tot:.2f} h/wk; protected content {cont:.2f} h")

# ---------- per-delivery-hour yields ----------
# cohort: review 8-15 min/client-wk + group call amortized (1 h per 8-15 clients -> 4-7.5 min) ; 12 wks
for price, mins in ((1500, 22), (3000, 12)):
    h = mins * 12 / 60
    print(f"cohort ${price} at {mins} min/client-wk -> {h:.1f} h/client -> ${price / h:.0f}/delivery h")
for price, mins in ((1500, 75), (3000, 45)):
    h = mins * 12 / 60
    print(f"1:1 ${price} at {mins} min/client-wk -> {h:.1f} h/client -> ${price / h:.0f}/delivery h")
# one-to-one-only ceiling: 12-14 delivery h/wk
for price, mins, dh in ((1500, 75, 12), (3000, 45, 14)):
    conc = dh * 60 / mins
    enr = conc / (12 / 4.33)
    print(f"1:1-only: {conc:.0f} concurrent -> {enr:.1f} enroll/mo -> ${enr * price / 1e3:.1f}k/mo")
# free-call ceiling at 5 sales h/wk
for hper, close in ((1.0, 0.15), (0.75, 0.35)):
    conv = 5 * 4.33 / hper
    print(f"free-call ceiling: {conv:.0f} conv/mo x {close} = {conv * close:.1f} enroll/mo")

# ---------- reach-banded waypoints ----------
# eligible leads/mo at m3, m6, m9 (c, g)
bands = {
 'A never breaks out': {3: (10, 20), 6: (20, 35), 9: (25, 50)},
 'B steady':           {3: (15, 30), 6: (40, 80), 9: (60, 150)},
 'C breaks out yr 1':  {3: (20, 40), 6: (60, 150), 9: (150, 400)},
 'D breakout':         {3: (25, 50), 6: (100, 250), 9: (400, 700)},
}
extra = {3: (6, 12), 6: (3, 6), 9: (2, 5)}          # warm network / replies / referrals conversations
conv_rate = (0.12, 0.20)                            # eligible lead -> held fit conversation (personal reply)
close = {3: (0.15, 0.35), 6: (0.15, 0.35), 9: (0.20, 0.40)}
call_cap = (26, 35)                                 # ~6-8 held/wk; above this the door goes paid
ass_rate, ass_close, fee = (0.03, 0.07), (0.25, 0.45), 200
seat_cap = {3: (2, 3), 6: (6, 8), 9: (7, 10)}       # founding 1:1 seats/mo; founding group; care-capacity
price = {3: (1000, 1500), 6: (1200, 1500), 9: (1500, 2200)}
backend = {3: 0.0, 6: 0.03, 9: (0.06, 0.15)}        # Phase 2 + continuity as share of front-end cash
fixed = {3: (600, 300), 6: (1200, 700), 9: (1800, 1200)}  # editor+software(+optional ads) per month, c has more ads
var_cost = (0.10, 0.07)                             # processing + refunds/disputes + clip freelancer share
for b, lv in bands.items():
    print(f"\nBand {b}")
    for m in (3, 6, 9):
        res = []
        for i in (0, 1):
            leads = lv[m][i]
            conv_raw = leads * conv_rate[i] + extra[m][i]
            if conv_raw > call_cap[i]:
                conv = call_cap[i]
                ass = leads * ass_rate[i]
                enr = conv * close[m][i] + ass * ass_close[i]
                fees = ass * (1 - ass_close[i]) * fee
            else:
                conv, ass, fees = conv_raw, 0, 0
                enr = conv * close[m][i]
            enr = min(enr, seat_cap[m][i])
            be = backend[m] if not isinstance(backend[m], tuple) else backend[m][i]
            cash = enr * price[m][i] * (1 + be) + fees
            profit = cash * (1 - var_cost[i]) - fixed[m][i]
            res.append((leads, conv, ass, enr, cash, profit))
        c, g = res
        print(f"  m{m}: leads {c[0]}-{g[0]} | convs {c[1]:.0f}-{g[1]:.0f} | assess {c[2]:.0f}-{g[2]:.0f} | "
              f"new clients {c[3]:.1f}-{g[3]:.1f} | cash ${c[4] / 1e3:.1f}-{g[4] / 1e3:.1f}k | profit ${c[5] / 1e3:.1f}-{g[5] / 1e3:.1f}k")

# ---------- maturity per band (proof prices, capacity) ----------
ltv_open = (1500 + 0.2 * 800 + 0.2 * 39 * 6, 2200 + 0.4 * 1500 + 0.4 * 79 * 6)
ltv_proof = (2400 + 0.2 * 800 + 0.2 * 39 * 6, 3000 + 0.4 * 1500 + 0.4 * 79 * 6)
print(f"\nLTV opening {ltv_open[0]:.0f}-{ltv_open[1]:.0f}; proof {ltv_proof[0]:.0f}-{ltv_proof[1]:.0f}")
mature_leads = {'A': (30, 60), 'B': (80, 180), 'C': (200, 450), 'D': (450, 800)}
cap = (7, 12)
margin = (0.75, 0.85)
for b, (lo, hi) in mature_leads.items():
    out = []
    for i, leads in enumerate((lo, hi)):
        conv_raw = leads * conv_rate[i] + (3, 6)[i]   # referrals
        if conv_raw > call_cap[i]:
            enr = call_cap[i] * (0.25, 0.40)[i] + leads * ass_rate[i] * ass_close[i]
        else:
            enr = conv_raw * (0.25, 0.40)[i]
        enr = min(enr, cap[i])
        rev = enr * ltv_proof[i]
        out.append((enr, rev, rev * margin[i]))
    print(f"mature {b}: leads {lo}-{hi} -> enroll {out[0][0]:.1f}-{out[1][0]:.1f}/mo -> revenue ${out[0][1] / 1e3:.1f}-{out[1][1] / 1e3:.1f}k -> profit ${out[0][2] / 1e3:.1f}-{out[1][2] / 1e3:.1f}k")
# what $50k needs at capacity
for enr in (10, 12):
    for p in (3500, 4500):
        l = p + 0.3 * 1200 + 0.3 * 59 * 6
        print(f"$50k check: {enr} enroll x LTV ${l:.0f} = ${enr * l / 1e3:.1f}k rev -> profit ${enr * l * 0.84 / 1e3:.1f}k")
# take-home affordability
for gross, label in ((42000, '20-24'), (59000, '25-34')):
    net = gross * 0.80 / 12
    print(f"{label}: take-home ~${net:.0f}/mo; $1.5k={1500 / net:.2f} mo, $2.2k={2200 / net:.2f}, $3k={3000 / net:.2f}")
