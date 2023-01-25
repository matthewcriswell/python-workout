def pig_latin(eng_word):
    ''' converts a lower case english word into pig latin '''
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    if eng_word[0] in vowels_list:
        return eng_word + 'way'
    return eng_word[1:] + eng_word[:1] + 'ay'
