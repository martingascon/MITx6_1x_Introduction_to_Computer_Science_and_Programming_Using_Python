def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    s = aStr
    sLen = 0
    if s == '':
        return 0
    else:
        return 1 + lenRecur(s[0:-1])