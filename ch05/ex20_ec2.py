# Create a dict in which the keys are the names of files on your system and the values are the sizes of those files. To calculate the size, you can use os.stat

import os
import pathlib

#SEED_DIRECTORY = './'
SEED_DIRECTORY = '/Users'


def sizefile(filename):
    ''' this takes a file and returns the size of said file '''
    try:
        return pathlib.Path(filename).stat().st_size
    except:
        return -1


def getfiles(directory):
    ''' create list of files from base directory '''
    output = []
    for dirpath, _, name in [item for item in os.walk(directory)]:
        if isinstance(name, list):
            for fname in name:
                output.append(os.path.join(dirpath, fname))
    return output


files_list = getfiles(SEED_DIRECTORY)
sizes_list = [sizefile(file) for file in files_list]
files_size = dict(zip(files_list, sizes_list))
