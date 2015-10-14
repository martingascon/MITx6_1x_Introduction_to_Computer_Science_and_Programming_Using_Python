 
def count7(n):
     if (n == 0):
        return 0
     else:
        if (n % 10 == 7):
            return 1 + count7(n // 10)
        else:
            return 0 + count7(n // 10)
            
            
print count7(717)
print count7(1237123)