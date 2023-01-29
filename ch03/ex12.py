from collections import Counter
from operator import itemgetter

def most_repeating_word(sequence):
    word_list = []
    word_dict = {}
    for word in sequence:
        c = Counter(word)
        word_dict = {
        'word': word,
        'repeats': c.most_common()[0][1]
        }
        word_list.append(word_dict)
    return word_list

words = ['this', 'is', 'an', 'elementary', 'test', 'example']
words_dict = most_repeating_word(words)
for item in sorted(words_dict, key=itemgetter('repeats'), reverse=True):
    print(f"{item['word']}: {item['repeats']}")

