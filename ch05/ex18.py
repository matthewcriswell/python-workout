def get_file_line(filename):
    ''' opens a text file and returns the last line '''
    with open(filename, 'rt', encoding="utf-8") as file:
        for line in file.readlines():
            last_line = line
    return last_line

print(get_file_line('test.txt'), end='')
