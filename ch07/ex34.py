'''
find words containing all vowels
'''

VOWEL_HASH = {
'a': 1,
'e': 2,
'i': 3,
'o': 4,
'u': 5
}

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
        words_vowel_mode.append({'word':word,'vowel_mode':vowel_mode})
    return set([word['word'] for word in words_vowel_mode if word['vowel_mode'] == 15])
