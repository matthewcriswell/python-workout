'''
return a function that gets a specific item out of a sequence
'''


def getitem(item):
    ''' return a function that gets a specific item from a sequence '''

    def itemgetter(sequence):
        return sequence[item]

    return itemgetter
