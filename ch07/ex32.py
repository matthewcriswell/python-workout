'''
flip a dictionary
'''
d = {'a': 1, 'b': 2, 'c': 3}
new_d = {k: d for d, k in d.items()}
print(new_d)
