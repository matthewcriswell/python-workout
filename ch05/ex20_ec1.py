from collections import Counter
from time import sleep
file = ''
words_list = []

user_input = input("Enter a filename and words to count in the file (space seperated):").split()

file = user_input[0]
words_set = set(user_input[1:])
generic_counter = Counter()
specific_words = Counter()
with open(file, 'rt', encoding='UTF-8') as file:
    for line in file:
        specific_words.update([word for word in line.split() if word in words_set])
        generic_counter.update([word for word in line.split()])
    
for word, count in [item for item in generic_counter.most_common()]:
    print(word,count)

print('\n\n\n')
for word, count in [item for item in specific_words.most_common()]:
    print(word,count)

