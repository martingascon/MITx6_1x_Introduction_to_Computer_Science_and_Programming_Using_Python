balance = 999999
annualInterestRate=0.18

balance2 = balance
low = balance/12
high = (balance * (1 + annualInterestRate/12.0)**12) / 12.0
mid = (low+high)/2
#print low,high,mid
monthlyPaymentRate = mid
eps = 0.01
while abs(balance2)>eps:
    mon = 0
    totalPaid = 0
    balance2=balance
    while mon <12:
        minPay = monthlyPaymentRate 
        unpaidBal = balance2 - minPay
        totalPaid += minPay
        balance2 = unpaidBal*(1  + annualInterestRate/12.0)
        mon += 1
    #print balance2,balance, balance2-balance
    if (balance2>0):
        low = mid
        mid = (mid + high)/2
    else:   
        high = mid 
        mid = (mid + low)/2
    monthlyPaymentRate = mid
    #print mid, balance2
    
print "Lowest Payment: %.2f" % (monthlyPaymentRate) 


