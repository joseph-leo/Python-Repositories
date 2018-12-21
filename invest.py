def invest(amount, rate, time):
    print('principal amount:', '$' + str(amount))
    print('annual rate of return:', str(rate))
    float(amount)
    float(rate)
    for i in range(1, time + 1):
        amount = amount + (amount * rate)       
        yearCount = i       
        print('year', str(yearCount) + ':', '$' +  str(amount))

invest(100, .05, 8)
invest(2000, .025, 5)

