from random import randint

with open('test.txt', 'rt') as file:
    contents = file.readlines()

gibberish = []
i = 0

for x, sentence in enumerate(contents):
    if not sentence.isspace():
        sentence_list = sentence.split()
        #print(f"{sentence} is {len(sentence)} chars")
        try:
            rando = randint(0,len(sentence_list) - 1)
            gibberish.append(sentence_list[rando])
        except IndexError as e:
            print(f"sentence: {sentence}; {e}")
    if x>=12:
        break

print(' '.join(gibberish))
