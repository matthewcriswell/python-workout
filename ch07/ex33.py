'''
apply a function to each value of a dict
'''


def transform_values(func, d_t):
    ''' apply a func to values in a dict '''
    return {k: func(v) for k, v in d_t.items()}


d = {'a': 1, 'b': 2, 'c': 3}
print(f'd: {d}')

print('transform')
e = transform_values(lambda x: x * x, d)

print(f'd: {d}')
print(f'e: {e}')
