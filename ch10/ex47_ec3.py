''' MyRange that works a lot like range() '''


class MyRange:
    ''' implements a range() like object '''

    def __init__(self, *args):
        if len(args) == 0:
            raise ValueError("Must provide a parameter")
        if len(args) > 3:
            raise ValueError("Provided more than 3 parameters")
        for item in args:
            if not isinstance(item, int):
                raise ValueError(f"{item} is not type int")
        if len(args) == 1:
            self.start = 0
            self.stop = args[0] - 1
            self.step = 1
        if len(args) == 2:
            self.start = args[0]
            self.stop = args[1] - 1
            self.step = 1
        if len(args) == 3:
            self.start = args[0]
            self.stop = args[1] - 1
            self.step = args[2]
        self.index = self.start

    def __iter__(self):
        return self

    def __next__(self):
        while self.index <= self.stop:
            value = self.index
            self.index += self.step
            return value
        raise StopIteration


b = MyRange(10)
c = MyRange(2, 20)
d = MyRange(2, 20, 2)

for i in b:
    print(i)

for i in c:
    print(i)

for i in d:
    print(i)

b = range(10)
c = range(2, 20)
d = range(2, 20, 2)

for i in b:
    print(i)

for i in c:
    print(i)

for i in d:
    print(i)
