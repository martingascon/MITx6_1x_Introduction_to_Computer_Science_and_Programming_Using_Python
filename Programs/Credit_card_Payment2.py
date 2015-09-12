balance = 3926
annualInterestRate=0.2
monthlyPaymentRate = 0
balance2 = balance

while balance2>0:
    mon = 0
    totalPaid = 0
    monthlyPaymentRate +=10
    balance2=balance
    while mon <12:
        minPay = monthlyPaymentRate 
        unpaidBal = balance2 - minPay
        totalPaid += minPay
        balance2 = unpaidBal*(1  + annualInterestRate/12.0)
        mon += 1
print "Lowest Payment: %.2f" % (monthlyPaymentRate) 