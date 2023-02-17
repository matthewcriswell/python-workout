'''
Given a text file, what are the lengths of the different words? Return a set of different word lengths in the file.
'''

import itertools
from itertools import chain

def word_lens(filename):
    ''' return a set of the length of words in a given file '''
    with open(filename,'rt') as in_f:
        lines = list(chain(*[line.strip().split() for line in in_f.readlines()]))
    return set([len(word) for word in lines])
