from os import listdir

files = listdir()
ext_list = [file.split('.')[1] for file in files]
print("Unique apparent file extensions in current directory:", *list(set(ext_list)))
