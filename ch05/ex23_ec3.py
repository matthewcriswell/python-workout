import json
import pathlib
from glob import glob
from os import stat
from operator import itemgetter

dir_string = input("Enter a directory:") + '/*'
files = glob(dir_string)
json_file = 'file_info.json'

def fileinfo(filename):
    ''' this takes a file and returns the size of said file '''
    try:
        return {"filename": filename, "bytes":pathlib.Path(filename).stat().st_size, "mtime":pathlib.Path(filename).stat().st_mtime}
    except:
        return -1


with open(json_file, 'w', encoding='UTF-8') as outfile:
    json.dump( 
        [
            fileinfo(single_file) for single_file in files
        ], outfile)

with open(json_file, 'r', encoding='UTF-8') as infile:
    contents = json.load(infile)

least_recent = sorted(contents, key=itemgetter('mtime'))[-1]
most_recent = sorted(contents, key=itemgetter('mtime'))[0]
smallest_file = sorted(contents, key=itemgetter('bytes'))[0]
largest_file = sorted(contents, key=itemgetter('bytes'))[-1]

print(f'most recently modified: {most_recent["filename"]}')
print(f'least recently modified: {least_recent["filename"]}')
print(f'smallest file: {smallest_file["filename"]}')
print(f'largest file: {largest_file["filename"]}')
