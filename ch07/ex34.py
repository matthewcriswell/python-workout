'''
find words containing all vowels
'''

# To profile:
# 1. decorate function of interest with @profile
# 2. kernprof -l ex34.py 
# 3. python -m line_profiler ex34.py.lprof 

from time import perf_counter

#VOWEL_HASH = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
VOWEL_HASH = {
    'a': 1,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 2,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 3,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 4,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 5,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
    '-': 0
}


#@profile
def get_sv(words_file):
    ''' find words with a, e, i, o, and u and return as a set '''
    with open(words_file, 'rt') as in_file:
        words = [word.strip() for word in in_file.readlines()]

    sv_words = []
    for word in words:
        #word_set = set(word.lower())
        vowel_mode = 0
        for char in set(word.lower()):
            #if char in 'aeiou':
            #    vowel_mode += VOWEL_HASH[char]
            vowel_mode += VOWEL_HASH[char]
        if vowel_mode == 15:
            sv_words.append(word)

    return set(sv_words)


#@profile
def get_sv2(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {
        word.strip()
        for word in open(filename) if vowels < set(word.lower())
    }


tic = perf_counter()
test_set = get_sv('words.txt')
toc = perf_counter()
print(f"Vowel hash took: {toc - tic:0.4f} seconds")

tic = perf_counter()
test_set2 = get_sv2('words.txt')
toc = perf_counter()
print(f"Boolean set logic took: {toc - tic:0.4f} seconds")
