'''
Given a string containing several (space-separated) words, create a dict in which the keys are the words, and the values are the number of vowels in each word.
'''

TEST_STRING = 'this is an easy test'


def vowel_count(word):
    ''' return the vowel count of a word '''
    output = 0
    for i in word:
        if i in 'aeiouAEIOU':
            output += 1
    return output


def vowel_count_string(string):
    ''' create a dictionary of words in a string and each words respective vowel count '''
    return {word: vowel_count(word) for word in string.split()}


print(vowel_count_string(TEST_STRING))
