''' use menu.py '''

from menu import menu


def func_a():
    ''' dummy func '''
    return "A"


def func_b():
    ''' dummy func '''
    return "B"


def func_c():
    ''' dummy func '''
    return "C"


def func_apple():
    ''' dummy func '''
    return "apple"


return_value = menu(cheese=func_a, apple=func_apple)
print(f"Result is {return_value}")
