'''
prefix notation calculator
'''
import operator

OPS = {
    '*': operator.mul,
    '%': operator.mod,
    '/': operator.truediv,
    '-': operator.sub,
    '+': operator.add,
    '**': operator.pow
}


def calc(calc_string):
    ''' takes a string containing a simple math expression with an operator and two numbers a returns the calculation '''
    calc_list = calc_string.split()
    operation = calc_list.pop(0)
    nums = [int(i) for i in calc_list]
    print(operation, ":", *calc_list)
    print("result: ", OPS[operation](*nums))
    return OPS[operation](*nums)


def test_addition():
    assert calc('+ 3 3') == 6
    assert calc('+ 5 -5') == 0
    assert calc('+ -10 -10') == -20


def test_subtraction():
    assert calc('- 10 7') == 3
    assert calc('- 1 10') == -9


def test_division():
    assert calc('/ 3 3') == 1
    assert calc('/ 10 3') == 3.3333333333333335


def test_multiplication():
    assert calc('* 3 3') == 9
    assert calc('* 10 10') == 100


def test_exponent():
    assert calc('** 10 3') == 1000
