with open('test.txt','rt') as file:
    text = file.read()

text_list = text.split()
print(sorted(text_list)[-1])
