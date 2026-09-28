# Waypoints v3: founding group on overflow (no 2-3 seat cap), monthly entry, cap-and-overflow door,
# labeled warm-network source decaying over time, price steps. Conservative (c) vs good (g).
bands = {
 'A never breaks out': {3: (10, 20), 6: (20, 35), 9: (25, 50)},
 'B steady':           {3: (15, 30), 6: (40, 80), 9: (60, 150)},
 'C breaks out yr 1':  {3: (20, 40), 6: (60, 150), 9: (150, 400)},
 'D breakout':         {3: (25, 50), 6: (100, 250), 9: (400, 700)},
}
warm = {3: (2, 8), 6: (1, 5), 9: (1, 4)}           # warm network + replies + referrals (held conv/month), PL labeled
conv_rate = (0.12, 0.20)
close = {3: (0.15, 0.35), 6: (0.18, 0.35), 9: (0.20, 0.40)}
call_cap = (26, 35)                                 # ~6-8 held a week; overflow -> paid/async assessment
ass_rate, ass_close, fee = (0.03, 0.07), (0.25, 0.45), 200
cap = {3: (6, 8), 6: (7, 9), 9: (7, 10)}           # care capacity on new clients/month (founding group takes overflow)
price = {3: (1200, 1500), 6: (1400, 1800), 9: (1800, 2400)}
backend = {3: 0.0, 6: (0.03, 0.08), 9: (0.06, 0.15)}
fixed = {3: (400, 250), 6: (1200, 700), 9: (1800, 1200)}
var = (0.10, 0.07)
for b, lv in bands.items():
    print(f"Band {b}")
    for m in (3, 6, 9):
        out = []
        for i in (0, 1):
            leads = lv[m][i]
            c = leads * conv_rate[i] + warm[m][i]
            if c > call_cap[i]:
                over = leads - (call_cap[i] - warm[m][i]) / conv_rate[i]
                ass = max(over, 0) * ass_rate[i] / conv_rate[i] * conv_rate[i]  # overflow leads x assessment rate
                ass = max(over, 0) * ass_rate[i]
                enr = call_cap[i] * close[m][i] + ass * ass_close[i]
                fees = ass * (1 - ass_close[i]) * fee
                c = call_cap[i]
            else:
                ass, fees = 0, 0
                enr = c * close[m][i]
            enr = min(enr, cap[m][i])
            be = backend[m] if not isinstance(backend[m], tuple) else backend[m][i]
            cash = enr * price[m][i] * (1 + be) + fees
            profit = cash * (1 - var[i]) - fixed[m][i]
            out.append((leads, c, ass, enr, cash, profit))
        c_, g_ = out
        print(f"  m{m}: leads {c_[0]}-{g_[0]} | held conv {c_[1]:.0f}-{g_[1]:.0f} | overflow assess {c_[2]:.0f}-{g_[2]:.0f} | new clients {c_[3]:.1f}-{g_[3]:.1f} | cash ${c_[4]/1e3:.1f}-{g_[4]/1e3:.1f}k | profit ${c_[5]/1e3:.1f}-{g_[5]/1e3:.1f}k")
