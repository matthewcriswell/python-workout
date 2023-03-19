''' mychain which tries to replicain itertool's chain '''

from itertools import chain
from typing import Iterable

for one_item in chain('abc', [1, 2, 3], {'a': 1, 'b': 2}):
    print(one_item)


def mychain(*args):
    for seq in args:
        if isinstance(seq, Iterable):
            for item in seq:
                yield item
        else:
            yield seq
    return None


print('----')
for one_item in mychain('abc', [1, 2, 3], {'a': 1, 'b': 2}):
    print(one_item)
