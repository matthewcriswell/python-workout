def sum_numeric(*args):
    ''' attempt to sum numeric values '''
    mysum = 0
    for num in args:
        try:
            mysum += int(num)
        except:
            pass
    return mysum
