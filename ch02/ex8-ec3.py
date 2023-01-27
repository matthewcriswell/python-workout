with open('test.txt', 'rt') as file:
    text = file.read()

text_list = text.split()
longest_word = ''
longest = 0

for word in text_list:
    if len(word) > longest:
        longest = len(word)
        longest_word = word

print(f"The longest word is {longest_word} at {longest} chars.")
