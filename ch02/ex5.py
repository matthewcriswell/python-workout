def pig_latin(eng_word):
    ''' converts a lower case english word into pig latin '''
    if eng_word[0] in 'aeiou':
        return eng_word + 'way'
    return eng_word[1:] + eng_word[:1] + 'ay'
