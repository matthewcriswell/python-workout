with open ('test.txt', 'rt') as file:
    contents = file.read()

wordlen = {}
for word in contents.strip().split():
    the_word = word.strip().replace('.','')
    the_key = len(the_word)
    if wordlen.get(the_key):
        wordlen[the_key].append(the_word)
    else:
        wordlen[the_key] = [the_word]


print("")
print("Word list sorted by word length:")
for item in sorted(wordlen.items()):
    print(*item)

print("")
print("Word list sorted by frequency of length:")
for item in sorted(wordlen.items(), key=len):
    print(*item)
