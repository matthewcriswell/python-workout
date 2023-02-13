'''
reverses the order of words per line in a file
'''


def rev_lines(infile):
    ''' opens a file and reverses the order of words per line as a list '''
    with open(infile, 'rt', encoding='UTF-8') as in_f:
        output = [line.strip().split() for line in in_f]
        for item in output:
            item.reverse()
        return output
