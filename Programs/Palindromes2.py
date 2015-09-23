def isPal(x):
    assert type(x) == list
    temp = list(x) # otherwise pointer makes them the same.
    temp.reverse
    if temp == x:
        return True
    else:
        return False

def silly(n):
    for i in range(n):
        result = []
        elem = raw_input('Enter element: ')
        result.append(elem)
    print result
    if isPal(result):
        print('Yes')
    else:
        print('No')