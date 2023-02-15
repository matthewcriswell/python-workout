'''
Create a dict whose keys are filenames and whose values are the lengths of the files.
'''
import pathlib
from glob import glob

dir_string = input("Enter a directory:") + '/*'
files = glob(dir_string)
json_file = 'file_info.json'


def fileinfo(filename):
    ''' this takes a file and returns the size of said file '''
    try:
        return {
            "filename": filename,
            "bytes": pathlib.Path(filename).stat().st_size,
            "mtime": pathlib.Path(filename).stat().st_mtime
        }
    except:
        return -1


files_list = [fileinfo(file) for file in files]
files_dict = {file['filename']: file['bytes'] for file in files_list}
print(files_dict)
