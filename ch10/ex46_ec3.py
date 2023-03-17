''' MyEnumerate as a generator '''

def MyEnumerate(seq, start_val = 0):
    if not hasattr(seq,'__iter__'):
        raise ValueError(f'{seq} is not iterable')
    my_index = 0
    while my_index < len(seq):
        yield ((my_index + start_val),seq[my_index])
        my_index += 1


for index, letter in enumerate('abc'):
    print(f'{index}: {letter}')

for index, letter in MyEnumerate('abc'):
    print(f'{index}: {letter}')
for index, letter in MyEnumerate('abc', 10):
    print(f'{index}: {letter}')
for index, letter in MyEnumerate('abc'):
    print(f'{index}: {letter}')

#for index, item in MyEnumerate(123):
#    print(f'{index}: {item}')
