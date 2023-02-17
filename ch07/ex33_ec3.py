'''
Write a function that takes a directory name (i.e., a string) as an argument. The function should return a dict in which the keys are the names of files in that directory, and the values are the file sizes. You can use os.listdir or glob .glob to get the files, but because only regular files have sizes, you’ll want to filter the results using methods from os.path. To determine the file size, you can use os.stat or (if you prefer) just check the length of the string resulting from reading the file.
'''

import pathlib
from glob import glob


def dict_dir(dirname):
    ''' takes a directory name and returns a dict of filenames and size '''
    files = glob(dirname + '/*')
    return {file: pathlib.Path(file).stat().st_size for file in files}
