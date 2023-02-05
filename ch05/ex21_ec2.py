#!/usr/bin/env python
'''
Ask the user for a directory name. Show all of the files in the directory, as well as how long ago the directory was modified. You will probably want to use a combination of os.stat and the Arrow package on PyPI (http://mng.bz/nPPK) to do this easily.
'''

from os import listdir, stat
from os.path import join
import arrow


def get_dir():
    ''' get directory name from user '''
    return input("Enter a directory to inspect:")


def get_dir_files(directory):
    ''' get a list of files in a directory '''
    return [join(directory, file) for file in listdir(directory)]


def get_file_metadata(file):
    ''' get metadata for a given file '''
    file_info = stat(file)
    return {
        'name': file,
        'mtime': arrow.get(file_info.st_mtime),
        'size_bytes': file_info.st_size
    }
    #return dict(('name',file),('mtime':(arrow.get(file_info.st_mtime), file_info.st_size):


def main():
    ''' main function with primary program logic '''
    directory = get_dir()
    files = get_dir_files(directory)
    files_metadata = [get_file_metadata(file) for file in files]
    files_metadata.insert(0, get_file_metadata(directory))
    print(f"{'File Name':>60s} {'Last Modified':>20s} {'Bytes':>8}")
    for file in files_metadata:
        print(
            f"{file['name']:>60s} {file['mtime'].humanize():>20s} {file['size_bytes']:>8}"
        )


if __name__ == '__main__':
    main()
