'''
sum up numbers
'''


def sum_numbers(num_string):
    ''' take a string and filter out any non-numbers; sum the rest'''
    return sum([int(num) for num in num_string.split() if num.isdigit()])


user_input = input("enter a space separated string to sum:")
print(sum_numbers(user_input))
