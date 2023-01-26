def pig_latin(word):
    ''' converts an english word into pig latin '''
    punct = ''
    if not word[-1].isalnum():
        punct = word[-1]
        word = word[:-1]
    if word[0] in 'aeiou':
        return f"{word}way{punct}"
    elif word[0] in 'aeiou'.upper():
        pig_word = word + 'way' + punct
        return pig_word.lower().capitalize()
    elif word[0] in 'bcdfghjklmnpqrstvwxyz'.upper():
        pig_word = word[1:] + word[:1] + 'ay' + punct
        return pig_word.lower().capitalize()
    return word[1:] + word[:1] + 'ay' + punct
