def longest_word(f):
    ''' takes a file descriptor type of thing and findest the longest text word '''
    f.seek(0)
    longest_word = ''

    for line in f:
        for word in line.split():
            if len(word) > len(longest_word):
                longest_word = word
    return longest_word
