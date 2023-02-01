def get_file_line(filename):
    with open(filename, 'rt') as file:
        for line in file.readlines(): 
            last_line = line 
    return last_line

print(get_file_line('test.txt'), end='')
