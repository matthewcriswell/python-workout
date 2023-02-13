'''
Show the lines of a text file that contain at least one vowel and contain more than 20 characters.
'''

TEXT_FILE='text2.txt'
def has_vowels(a_string):
    for char in a_string:
         if char in 'AEIOUaeiou':
             return True
    return False

with open(TEXT_FILE, "rt", encoding="UTF-8") as in_file:
    for line in in_file:
        print(*[word for word in line.split() if len(line) >= 20 and has_vowels(line)])
