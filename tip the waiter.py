def total_calc(billamount,tipperc):
    total=billamount*(1+0.01*tipperc)
    total=round(total,2)
    print(f"please pay {total}")
total_calc(200,20)