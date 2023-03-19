''' ex48: all lines, all files '''

from os import listdir, stat
from os.path import join

MOST_LINES = 0


def get_dir_files(directory):
    ''' get a list of files in a directory '''
    return [join(directory, file) for file in listdir(directory)]


def get_file_descs(files_list):
    ''' takes a list of file and returns a list of open files '''
    return {file:open(file) for file in files_list}


def get_lines(files, match_str = ''):
    output_str = ''
    index = 0
    file_no = 0
    while index < MOST_LINES:
        for file in files:
            file_no += 1
            try:
                cur_line = next(files[file])
                if match_str:
                    if match_str in cur_line:
                        output_str = output_str + cur_line
                        yield (file, file_no, index, output_str)
                        output_str = ''
                    else:
                        pass
                else:
                    output_str = output_str + cur_line
                    yield (file, file_no, index, output_str)
                    output_str = ''
            except:
                pass
        index += 1
        file_no = 0


directory = './test_dir'
files = get_dir_files(directory)
file_descs = get_file_descs(files)

for file in file_descs:
    most_lines = len(file_descs[file].readlines())
    if most_lines > MOST_LINES:
        MOST_LINES = most_lines
    file_descs[file].seek(0)

for line in get_lines(file_descs, 'ipsum'):
    print(line)
