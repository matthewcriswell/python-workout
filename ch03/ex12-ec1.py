from collections import Counter
from operator import itemgetter

def greatest_vowel(sequence):
    ''' creates a list of dicts with a count of the frequently occuring vowel '''
    vowel_count_dict = {}
    vowel_count_list = []
    for word in sequence:
        c = Counter()
        for character in word:
            if character in 'aeiou':
                c[character] += 1
        vowel_count_dict = {
            'word': word, 
            'vowels': c.most_common()[0][1]
        }
        vowel_count_list.append(vowel_count_dict)
    return vowel_count_list

words = ['uuuuuuaaaaaiii', 'aaaaaaaaaaaa', 'uuuuuuuuuuuuuuuuuuuuuuuuuuuiiiiiiiiiaaaaaaeeee', 'union', 'unicorn', 'aaaba', 'eeyoree', 'this', 'is', 'an', 'elementary', 'test', 'example']

words_vowels = greatest_vowel(words)
for word in sorted(words_vowels, key=itemgetter('vowels'), reverse=True):
     print(f"{word['word']}: {word['vowels']}")
