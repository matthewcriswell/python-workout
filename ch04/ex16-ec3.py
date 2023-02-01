def filter_func(d):
    d = dict({d})
    for item in d.keys():
        if item in 'aeiou':
            return True
        return False

def dict_partition(d,f):
    d1 = {}
    d2 = {}
    for item in d.items():
        if f(item):
            d1.update(dict({item}))
        else:
            d2.update(dict({item}))
    print("d1:", d1)
    print("d2:", d2)


d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3, 'e': 9, 'z':24}
d4 = {'a':1, 'b':2, 'c':4, 'i': 88, 'o': 22}
d5 = {'a':1, 'b':2, 'd':4}

dict_partition(d1, filter_func)
dict_partition(d2, filter_func)
dict_partition(d3, filter_func)
dict_partition(d4, filter_func)
dict_partition(d5, filter_func)
