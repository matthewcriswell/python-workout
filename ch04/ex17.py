def how_many_different_numbers(sequence):
    output = len(set([num for num in sequence]))
    return output

numbers = [1, 2, 3, 1, 2, 3, 4, 1]
