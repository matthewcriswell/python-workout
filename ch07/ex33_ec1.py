'''
apply a function to each value of a dict
'''

def arbitrary_filter(k, v):
    ''' arbitrarily filter for certain items in a dict '''
    if k in 'a' or v == 2:
        return True

def transform_values(transform_func, filter_func, d_t):
    ''' apply a func to values in a dict '''
    return {k: transform_func(v) for k, v in d_t.items() if filter_func(k,v)}

d = {'a': 1, 'b': 2, 'c': 3}
print(f'd: {d}')

print('transform')
e = transform_values((lambda x: x*x), arbitrary_filter,  d)

print(f'd: {d}')
print(f'e: {e}')
