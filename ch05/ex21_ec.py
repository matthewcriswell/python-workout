'''
Use the hashlib module in the Python standard library, and the md5 function within it, to calculate the MD5 hash for the contents of every file in a user-specified directory. Then print all of the filenames and their MD5 hashes.
'''

import os
from hashlib import file_digest

DEFAULT_DIR = '.'

def calc_md5(filename):
    ''' calculate the md5 digest of a file '''
    with open(filename, 'rb') as f:
        return file_digest(f,'md5').hexdigest()
    return -1
    
def find_all_md5(directory):
    ''' takes a directory name and returns a dict in which the keys are filenames and the values are the md5 digests of the files ''' 
    files_list = []
    for dirpath, _, name in list(os.walk(directory)):
        if isinstance(name, list):
            for fname in name:
                files_list.append(os.path.join(dirpath, fname))
    return dict([(file, calc_md5(file)) for file in files_list])

md5_sums = find_all_md5(DEFAULT_DIR)
print(md5_sums)
