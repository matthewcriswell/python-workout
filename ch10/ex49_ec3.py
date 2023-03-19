''' generator function that returns if something is true '''


def isvowel(char):
    if char in 'aeiouAEIOU':
        return True
    else:
        return False


def my_gen_func(seq, test_func):
    ''' tests items in a sequence '''
    for item in seq:
        if test_func(item):
            yield item
    return None


a = ['a', 'b', 'c', 'd', 'e', 'f']
for i in my_gen_func(a, isvowel):
    print(i)

b = 'hello there'
for i in my_gen_func(b, isvowel):
    print(i)
