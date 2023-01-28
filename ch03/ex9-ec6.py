def myzip(seq1, seq2):
    new_list = []
    for i in range(len(seq1)):
        new_list.append((seq1[i], seq2[i]))
    return new_list
