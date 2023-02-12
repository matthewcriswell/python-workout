'''
make a CSV list string out of a range
'''


def join_numbers(num_range):
    ''' take a range and return a comma seperated list '''
    return ','.join([str(i) for i in num_range])
