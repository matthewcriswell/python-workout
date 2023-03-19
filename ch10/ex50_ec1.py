''' myzip which acts like zip '''

from typing import Iterable

for i in zip('abc', [10, 20, 30]):
    print(i)


def myzip(*args):
    index = 0
    longest_seq = 0
    output = []
    for seq in args:
        seq_len = len(seq)
        if seq_len > longest_seq:
            longest_seq = seq_len

    while index < longest_seq:
        for seq in args:
            try:
                output.append(seq[index])
            except:
                return None
        index += 1
        yield tuple(output)
        output = []


for i in myzip('abc', [10, 20, 30]):
    print(i)
