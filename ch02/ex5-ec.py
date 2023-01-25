def pig_latin(eng_word):
    ''' converts an english word into pig latin '''
    if eng_word[0] in 'aeiou':
        return f"{eng_word}way"
    elif eng_word[0] in 'aeiou'.upper():
        pig_word = eng_word + 'way'
        return pig_word.lower().capitalize()
    elif eng_word[0] in 'bcdfghjklmnpqrstvwxyz'.upper():
        pig_word = eng_word[1:] + eng_word[:1] + 'ay'
        return pig_word.lower().capitalize()
    return eng_word[1:] + eng_word[:1] + 'ay'
