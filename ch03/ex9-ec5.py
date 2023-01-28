def plus_minus(sequence):
    myBool = True
    total = sequence[0]
    seq_slice = sequence[1:]
    for num in seq_slice:
       if myBool:
           total += num
           myBool = not myBool
       else: 
           total -= num
           myBool = not myBool
    return total
