'''
Write a function, apply_to_each, that takes two arguments: a function that takes a single argument, and an iterable. Return a list whose values are the result of applying the function to each element in the iterable.
'''

def apply_to_each(my_func, my_sequence):
    ''' lame map() copy '''
    return [my_func(item) for item in my_sequence]
