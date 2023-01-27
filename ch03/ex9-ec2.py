def find_largest(sequence):
    ''' find and return the 'largest' item in a sequence '''
    if not sequence:
        return None
    thing = sequence[0]
    for item in sequence:
        if item > thing:
            thing = item

    return thing
