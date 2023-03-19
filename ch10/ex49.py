''' ex49 '''

from typing import Iterable
from time import perf_counter
from time import sleep

def gen_fun(seq):
    if not isinstance(seq, Iterable):
        raise ValueError(f'{seq} is not iterable')
    seq_iter = seq.__iter__()
    t_val = 0
    t_last = perf_counter()
    for _ in seq:
        if t_val:
            sleep(1)
            next_item = next(seq_iter)
            t_val = perf_counter()
            t_delta = t_val - t_last
            yield (t_delta, next_item)
            t_last = t_val
        else:
            next_item = next(seq_iter)
            yield(0, next_item)
            t_val = perf_counter()


my_seq = ['a', 'b', 'c', 'd', 'e']
for secs, next_item in gen_fun(my_seq):
    print(f'{secs}  {next_item}')

my_seq = {'a': 'matt', 'b': 'josh', 'c': 'bill', 'd': 'bort'}
for secs, next_item in gen_fun(my_seq):
    print(f'{secs}  {next_item}')

my_seq = 123
for secs, next_item in gen_fun(my_seq):
    print(f'{secs}  {next_item}')
