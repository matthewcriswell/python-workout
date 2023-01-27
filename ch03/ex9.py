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

def firstlast2(sequence):
    return sequence[:1] + sequence[-1:]


def firstlast3(sequence):
    print(f'----these are the sliced references----') 
    print(f'Values: {sequence[:1]} and {sequence[-1:]}')
    print(f'Types: {type(sequence[:1])} and {type(sequence[-1:])}')

    print(f'----these are the direct references----') 
    print(f'Values: {sequence[0]} and {sequence[-1:]}')
    print(f'Types: {type(sequence[0])} and {type(sequence[-1:])}')

    return sequence[:1] + sequence[-1:]
