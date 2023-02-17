'''
find words containing all vowels
'''

from time import perf_counter

VOWEL_HASH = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}


def get_sv(words_file):
    ''' find words with a, e, i, o, and u and return as a set '''
    with open(words_file, 'rt') as in_file:
        words = in_file.readlines()
    words = [word.strip() for word in words]
    words_vowel_mode = []
    for word in words:
        word_set = set(word.lower())
        vowel_mode = 0
        for char in word_set:
            if char in 'aeiou':
                vowel_mode += VOWEL_HASH[char]
        words_vowel_mode.append({'word': word, 'vowel_mode': vowel_mode})
    return set([
        word['word'] for word in words_vowel_mode if word['vowel_mode'] == 15
    ])


def get_sv2(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {
        word.strip()
        for word in open(filename)
        if vowels < set(word.lower())
    }


tic = perf_counter()
test_set = get_sv('words.txt')
toc = perf_counter()
print(f"Vowel hash took: {toc - tic:0.4f} seconds")

tic = perf_counter()
test_set2 = get_sv2('words.txt')
toc = perf_counter()
print(f"Boolean set logic took: {toc - tic:0.4f} seconds")
