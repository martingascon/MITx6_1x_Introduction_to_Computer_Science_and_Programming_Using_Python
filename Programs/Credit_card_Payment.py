balance = 5000
monthlyPaymentRate = 0.02
annualInterestRate=0.18

mon = 0
totalPaid = 0
while mon <12:
    minPay = monthlyPaymentRate * balance
    unpaidBal = balance - minPay
    totalPaid += minPay
    balance = unpaidBal*(1  + annualInterestRate/12.0)
    mon += 1
    print "Month: %2d" % (mon)
    print "Minimum monthly payment: %.2f" % (minPay)
    print "Remaining balance: %.2f" % (balance)
print "Total paid: %.2f" % totalPaid
print "Remaining balance: %.2f" % (balance) 