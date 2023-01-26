def ubbi_dubbi(word):
    ubbi_dubbi = []
    for letter in word:
        if letter in 'aeiou':
            ubbi_dubbi.append(f"ub{letter}")
        else:
            ubbi_dubbi.append(letter)
    return ''.join(ubbi_dubbi)
