''' Circle -- repeat a sequence '''


class CircleIterator:
    ''' helper for Circle class '''

    def __init__(self, sequence, my_wrap):
        self.sequence = sequence
        self.seq_len = len(sequence) - 1
        self.my_wrap = my_wrap
        self.full_repeats = self.seq_len // self.my_wrap
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.my_wrap > 0:
            if self.index < self.seq_len:
                value = self.sequence[self.index]
                self.index += 1
                self.my_wrap -= 1
            elif self.index == self.seq_len:
                value = self.sequence[self.index]
                self.full_repeats -= 1
                self.index = 0
                self.my_wrap -= 1
            return value
        raise StopIteration


class Circle(CircleIterator):
    ''' repeat a sequence '''

    def __iter__(self):
        return self


c = Circle('abc', 5)
print(list(c))

c = Circle('abcefg', 100)
print(list(c))
