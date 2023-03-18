''' Circle as a generator '''


def Circle(seq, repititions=0):
    ''' Circle class implemented as a generator function '''

    if not hasattr(seq, '__iter__'):
        raise ValueError(f'{seq} is not iterable')

    seq_len = len(seq) - 1
    reps = repititions
    index = 0

    while reps > 0:
        if index < seq_len:
            value = seq[index]
            index += 1
            reps -= 1
        elif index == seq_len:
            value = seq[index]
            index = 0
            reps -= 1
        yield value


c = Circle('abc', 5)
print(list(c))

c = Circle('abcefg', 100)
print(list(c))
