'''
reads some files and finds the longest word in each one
'''

import os
from collections import Counter


def find_longest_word(filename):
    ''' find and return the longest word in a file '''
    word_count = Counter()
    with open(filename, 'rt') as file:
        [word_count.update(line.strip().split()) for line in file]
    return word_count.most_common(1)


def find_all_logest_words(directory):
    ''' takes a directory name and returns a dict in which the keys are filenames and the values are the longest words from each file '''
    files_list = []
    for dirpath, _, name in [item for item in os.walk(directory)]:
        if isinstance(name, list):
            for fname in name:
                files_list.append(os.path.join(dirpath, fname))
    output_dict = {
        item[0]: item[1][0][1]
        for item in [(file, find_longest_word(file)) for file in files_list]
    }
    return output_dict
