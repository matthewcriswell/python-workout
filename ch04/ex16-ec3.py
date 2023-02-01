def filter_func(d):
    print(f"passed {d} of type {type(d)} to filter_func")
    #d = dict(d)
    d = dict({d})
    print(f"Item {d} of type {type(d)} being iterated")
    for item in d.keys():
        if item in 'aeiou':
            print("Filter func returning the value of True")
            return True
        print("Filter func returning the value of False")
        return False

def dict_partition(d,f):
    d1 = {}
    d2 = {}
    for item in d.items():
        print(f"passing {item} of type {type(item)}")
        if f(item):
            print(f"updating {d1} with {item} which is currently type {type(item)}")
            d1.update(dict({item}))
        else:
            print(f"updating {d2} with {item} which is currently type {type(item)}")
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
