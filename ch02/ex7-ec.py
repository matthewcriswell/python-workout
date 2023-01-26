def ubbi_dubbi(word):
    ubbi_dubbi = []
    for letter in word:
        if letter in 'aeiouAEIOU':
            ubbi_dubbi.append(f"ub{letter}")
        else:
            ubbi_dubbi.append(letter)
    if word[0].isupper():
        return ''.join(ubbi_dubbi).capitalize()
    return ''.join(ubbi_dubbi)
