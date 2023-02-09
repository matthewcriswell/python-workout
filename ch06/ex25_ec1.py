'''
don't copy that floppy 
'''

def copyfile(myfile='myfile.txt', *args):
    ''' copies a file to other files '''
    file_dict = {}
    for file in args:
        file_dict[file] = open(file, 'wt', encoding='UTF-8')
    with open(myfile, 'rt', encoding='UTF-8') as infile:
        for line in infile:
            for i in args:
                file_dict[i].write(line)
    for file in args:
        file_dict[file].close()
