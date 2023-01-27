def firstlast(item):
    ''' takes a sequence and returns the first and last element of said sequence '''
    if type(item) == list:
        bort = []
        bort.append(item[0])
        bort.append(item[-1])
        return bort

    if type(item) == tuple:
        return (item[0],item[-1])

    return item[0] + item[-1]
