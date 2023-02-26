''' use menu.py '''

from menu import menu


def func_a():
    return "A"


def func_b():
    return "B"


def func_c():
    return "C"


def func_apple():
    return "apple"


return_value = menu(cheese=func_a, apple=func_apple)
print(f"Result is {return_value}")
