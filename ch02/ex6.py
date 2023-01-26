def pig_latin(eng_word):
    ''' converts a lower case english word into pig latin '''
    if eng_word[0] in 'aeiou':
        return eng_word + 'way'
    return eng_word[1:] + eng_word[:1] + 'ay'

def pl_sentence(sentence):
    ''' converts a sentence to pig latin '''
    pig_sentence_list = []
    sentence_list = sentence.split()
    for word in sentence_list:
        pig_sentence_list.append(pig_latin(word))
    return ' '.join(pig_sentence_list)
