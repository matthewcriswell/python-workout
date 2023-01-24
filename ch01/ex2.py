def varfunc(*args):
    return args

def mysum(*args):
    sum = 0
    args_list = list(args)
    for i in args_list:
        sum += int(i)
    return sum
