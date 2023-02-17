'''
Create a list whose elements are strings--the names of people in your family. Now use a set comprehension (and, better yet, a nested set comprehension) to find which letters are used in your family members’ names.
'''

family_names = ['matt', 'josh', 'amy', 'mia', 'mike', 'aaron', 'lauren', 'fran', 'dave', 'dan', 'jenna', 'krista', 'irene']

name_char_set = {*(char for name in family_names for char in name)}
