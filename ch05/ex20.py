from collections import Counter
#FILENAME = 'wcfile.txt'
FILENAME = 'test.txt'

with open(FILENAME, 'rt', encoding='UTF-8') as file:
    contents = file.read()

char_count = len(contents)
word_count = len(contents.split())
line_count = len(contents.splitlines())

wc_counter = Counter()
with open(FILENAME, 'rt', encoding='UTF-8') as file:
    for line in file:
        wc_counter['line'] += 1
        wc_counter['word'] += len(line.split())
        wc_counter['char'] += len(line)

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Chars: {char_count}")
print(f"Counter chars: {wc_counter['char']}")
print(f"Counter words: {wc_counter['word']}")
print(f"Counter lines: {wc_counter['line']}")
