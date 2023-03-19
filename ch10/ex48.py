''' ex48: all lines, all files '''

from os import listdir, stat
from os.path import join

MOST_LINES = 0


def get_dir_files(directory):
    ''' get a list of files in a directory '''
    return [join(directory, file) for file in listdir(directory)]


def get_file_descs(files_list):
    ''' takes a list of file and returns a list of open files '''
    return [open(file) for file in files_list]


def get_lines(files):
    output = ''
    index = 0
    while index < MOST_LINES:
        for file in files:
            output = output + next(file)
        index += 1
    yield output


directory = './test_dir'
files = get_dir_files(directory)
file_descs = get_file_descs(files)

for file in file_descs:
    most_lines = len(file.readlines())
    if most_lines > MOST_LINES:
        MOST_LINES = most_lines
    file.seek(0)

for line in get_lines(file_descs):
    print(line)
