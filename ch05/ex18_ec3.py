'''
read a file and count up its vowels
'''

from collections import Counter

FILENAME = 'test.txt'

with open(FILENAME, 'rt', encoding='UTF-8') as file:
    contents = file.readlines()

vowel_count = Counter()

for item in [line.strip() for line in contents]:
    for char in item:
        if char in 'aeiouAEIOU':
            vowel_count[char] += 1

for letter, count in list(vowel_count.most_common()):
    print(f"{letter}: {count}")
