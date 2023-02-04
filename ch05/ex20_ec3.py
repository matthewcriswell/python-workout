# Given a directory, read through each file and count the frequency of each letter. (Force letters to be lowercase, and ignore nonletter characters.) Use a dict to keep track of the letter frequencies. What are the five most common letters across all of these files?
import os
from collections import Counter

DIRECTORY = '.'


def getfiles(directory):
    ''' create list of files from base directory '''
    output = []
    for dirpath, _, name in [item for item in os.walk(directory)]:
        if isinstance(name, list):
            for fname in name:
                output.append(os.path.join(dirpath, fname))
    return output


files_list = getfiles(DIRECTORY)
letter_count = Counter()
for f_name in files_list:
    with open(f_name, 'rt') as file:
        #contents = file.read()
        for line in file:
            #print(line.lower().split())
            for word in line.lower().split():
                for character in word:
                    if character.isalpha():
                        letter_count.update(character)

for letter, count in letter_count.most_common(5):
    print(letter, count)
