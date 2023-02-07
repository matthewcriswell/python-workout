'''
Given an existing text file, create two new text files. The new files will each contain the same number of lines as the input file. In one output file, you’ll write all of the vowels (a, e, i, o, and u) from the input file. In the other, you’ll write all of the consonants.
'''

input_file = 'new_test.txt'
vowel_output = 'vowels.txt'
consonant_output = 'consonats.txt'

with open(input_file, 'rt', encoding='UTF-8') as infile, open(vowel_output, 'wt', encoding='UTF-8') as vowelout, open(consonant_output, 'wt', encoding='UTF-8') as consonatout:
    for line in infile:
        vowels = [char for char in line.strip() if char in 'aeiouAEIOU']
        consonants = [char for char in line.strip() if char in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz']
        vowelout.write(''.join(vowels) + '\n')
        consonatout.write(''.join(consonants) + '\n')
