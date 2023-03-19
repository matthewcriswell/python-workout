''' MyRange that works a lot like range() '''


def MyRange(*args):
    if len(args) == 0:
        raise ValueError("Must provide a parameter")
    if len(args) > 3:
        raise ValueError("Provided more than 3 parameters")
    for item in args:
        if not isinstance(item, int):
            raise ValueError(f"{item} is not type int")
    if len(args) == 1:
        start = 0
        stop = args[0] - 1
        step = 1
    if len(args) == 2:
        start = args[0]
        stop = args[1] - 1
        step = 1
    if len(args) == 3:
        start = args[0]
        stop = args[1] - 1
        step = args[2]
    index = start

    while index <= stop:
        value = index
        index += step
        yield value
    return None


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
