def mysum_bigger_than(*args):
    ''' sums values greater than the first arg passed in '''
    if not args:
        return args
    thres = args[0]
    mysum = ''
    for item in args:
        if item > thres:
            if not mysum:
                mysum = item
            else:
                mysum += item
    return mysum
