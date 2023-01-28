def even_odd_sums(sequence):
    evens = 0
    odds = 0
    for num in sequence:
        if num/10 % 2:
            evens += num
        else:
            odds += num
    return [evens, odds]
