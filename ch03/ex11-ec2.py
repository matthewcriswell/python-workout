from operator import itemgetter

def count_vowels(word):
    ''' returns the number of vowels in a word '''
    count = 0
    for letter in word:
        if letter in 'aeiouAEIOU':
            count += 1
    return count

def sort_vowels(word_list):
    ''' sorts a list of words by vowel count '''
    vowel_count_list = []
    vowel_count = {}
    for item in word_list:
        vowel_count = {
            'word': item,
            'vowels': count_vowels(item)
        }
        vowel_count_list.append(vowel_count)

    sorted_vowel_count_list = sorted(
        vowel_count_list, key=itemgetter('vowels', 'word'), reverse=True)
    return sorted_vowel_count_list

words = [
    'this',
    'is',
    'a',
    'list',
    'of',
    'words',
    'which',
    'can',
    'be',
    'used',
    'to',
    'test',
    'things',
    'alphabet',
    'bangorang',
    'oooooh',
    'aaaaaaah',
    'cheesecakefactory'
]

for word in sort_vowels(words):
    print(f"{word['word']}: {word['vowels']}")
