'''
gematria_for, which takes a single word (string) as an argument and returns the gematria score for that word

gematria_equal_words, which takes a single word and returns a list of those dict words whose gematria scores match the current word’s score.
'''

from string import ascii_lowercase

gematria_hash = {k: v for v, k in enumerate(ascii_lowercase, start=1)}


def gematria_for(word):
    ''' takes a word and returns gematria score '''
    return sum([
        gematria_hash[char.lower()] for char in word
        if char.lower() in ascii_lowercase
    ])


with open('words.txt', 'rt') as in_f:
    words = [word.strip() for word in in_f.readlines()]
gem_dicts = [{
    'word': k,
    'score': v
} for k, v in [(word, gematria_for(word)) for word in words]]


def gematria_equal_words(word):
    ''' takes a word and returns a list of words with the same gematria score '''
    return [
        entry['word'] for entry in gem_dicts
        if entry['score'] == gematria_for(word)
    ]
