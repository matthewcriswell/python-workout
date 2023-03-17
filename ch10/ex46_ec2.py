''' MyEnumerate '''


class MyEnumerateIterator:
    ''' helper for MyEnumerate '''

    def __init__(self, data, start_val):
        self.data = data
        self.index = 0
        self.start_val = start_val

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return self.index + self.start_val - 1, value


class MyEnumerate:
    ''' enumerate an iterable '''

    def __init__(self, data, start_val=0):
        if not hasattr(data, '__iter__'):
            raise ValueError(f'{data} is not iterable')
        self.data = data
        self.start_val = start_val

    def __iter__(self):
        return MyEnumerateIterator(self.data, self.start_val)


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
