# middle case: m9 and maturity (proof prices), plus months-to-$25k heuristic
m9_leads={'A':37,'B':100,'C':275,'D':550}
mat_leads={'A':45,'B':130,'C':325,'D':625}
conv=0.16; cap_call=30; ass=0.05; ass_close=0.35; fee=200
def enroll(leads,close,cap,extra):
    c=leads*conv+extra
    if c>cap_call:
        e=cap_call*close+leads*ass*ass_close; fees=leads*ass*(1-ass_close)*fee
    else:
        e=c*close; fees=0
    return min(e,cap),fees
ltv_open=1850+0.3*1150+0.3*59*6      # opening band mid + phase2/continuity mid
ltv_proof=2700+0.3*1150+0.3*59*6
ltv_above=4000+0.3*1300+0.3*59*6
print(f"LTV mid opening {ltv_open:.0f} proof {ltv_proof:.0f} above-band {ltv_above:.0f}")
for b in 'ABCD':
    e9,f9=enroll(m9_leads[b],0.30,8.5,3.5)
    cash9=e9*1850*1.1+f9; p9=cash9*0.9-1500
    em,fm=enroll(mat_leads[b],0.325,9.5,4.5)
    pm=(em*ltv_proof+fm)*0.8
    pa=(em*ltv_above+fm)*0.8
    print(f"{b}: m9 enroll {e9:.1f} cash ${cash9/1e3:.1f}k profit ${p9/1e3:.1f}k | mature enroll {em:.1f} profit proof ${pm/1e3:.1f}k, above-band ${pa/1e3:.1f}k")
