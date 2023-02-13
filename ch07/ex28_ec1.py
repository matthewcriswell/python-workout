'''
make a CSV list string out of a range
'''


def join_numbers(num_range):
    ''' take a range and return a comma seperated list for values less than 10 '''
    return ','.join([str(i) for i in num_range if i <= 10 and i >= 0])
