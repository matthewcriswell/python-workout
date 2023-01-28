def mysum(*args):
    if not args:
        return args
    sum = args[0] 
    for item in args[1:]:
       sum += item
    return sum
