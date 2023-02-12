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
    first_num = nums.pop(0)
    next_num = nums.pop(0)
    result = OPS[operation](first_num, next_num)
    while nums:
        next_num = nums.pop(0)
        result = OPS[operation](result, next_num)
    print(operation, ":", *calc_list)
    return result


def test_addition():
    assert calc('+ 3 3') == 6
    assert calc('+ 5 -5') == 0
    assert calc('+ -10 -10') == -20
    assert calc('+ 10 10 10 10 10') == 50


def test_subtraction():
    assert calc('- 10 7') == 3
    assert calc('- 1 10') == -9
    assert calc('- 1 1 1') == -1
    assert calc('- 100 1000 1000') == -1900


def test_division():
    assert calc('/ 3 3') == 1
    assert calc('/ 10 3') == 3.3333333333333335


def test_multiplication():
    assert calc('* 3 3') == 9
    assert calc('* 10 10') == 100
    assert calc('* 5 5 5') == 125


def test_exponent():
    assert calc('** 10 3') == 1000
