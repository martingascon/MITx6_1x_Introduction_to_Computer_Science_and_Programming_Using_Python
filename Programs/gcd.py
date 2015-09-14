def gcdIter(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    g = min(a,b);
    while (g >= 1):
        if max(a,b)%g== 0 and min(a,b)%g == 0:
            return g
        else:
            g-=1


def gcdRecur(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    r =a%b
    if r == 0:
        return b
    else: 
        return gcdRecur(b,r)
  
  
############### Test  
  
print gcdIter(70,91)
print gcdRecur(70,91)