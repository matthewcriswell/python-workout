'''
flatten some data
'''


def flatten(sequence):
    ''' flatten a 2 level list '''
    return [subitem for item in sequence for subitem in item]
