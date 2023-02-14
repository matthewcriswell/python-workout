'''
flatten some data
'''


def flatten_odd_ints(sequence):
    ''' flatten a 2 level list '''
    return [
        int(subitem) for item in sequence for subitem in item
        if not int(str(subitem)) % 2 and str(subitem).isdigit()
    ]
