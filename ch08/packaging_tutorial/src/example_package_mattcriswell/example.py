'''  menu. The function takes any number of key-value pairs as arguments. Each value should be a callable '''

import mock
import pytest
import builtins

class InvalidKeyword(Exception):
    pass

def get_input(valid_keywords):
    ''' gets user input '''
    user_input = input(f"Select one of: {valid_keywords} ")
    if user_input not in valid_keywords:
        print(f'{user_input} is not a valid option')
        return InvalidKeyword()
    return user_input

def menu(**options):
    ''' return function '''
    valid_keywords = options.keys()
    user_input = get_input(valid_keywords)
    while isinstance(user_input, InvalidKeyword):
        print("Please try again.")
        user_input = get_input(valid_keywords)
    return options[user_input]()

def func_test():
    ''' dummy function for testing '''
    return "cheeseburgers"

def test_get_input():
    ''' test by injecting user input with mock '''
    # https://stackoverflow.com/a/55033710
    with mock.patch.object(builtins, 'input', lambda _: 'burger'):
        print(menu(burger=func_test))
        assert menu(burger=func_test) == 'cheeseburgers'

if __name__ == '__main__':
    print("Standalone mode: running tests")
    test_get_input()
