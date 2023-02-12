'''
make a CSV list string out of a range
'''


def join_numbers(num_range):
    ''' take a range and return a comma seperated list '''
    nums_list = [str(i) for i in num_range]
    last_num = nums_list.pop()
    output_list = [i + ',' for i in nums_list]
    output_list.append(last_num)
    return ''.join(output_list)
