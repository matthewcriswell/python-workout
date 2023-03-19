from os import listdir, stat
from os.path import join
import arrow
import datetime as dt
import time


def get_dir_files(directory):
    ''' get a list of files in a directory '''
    return [join(directory, file) for file in listdir(directory)]


def get_file_metadata(file):
    ''' get metadata for a given file '''
    file_info = stat(file)
    return {
        'name': file,
        'atime': dt.datetime.fromtimestamp(file_info.st_atime),
        'ctime': dt.datetime.fromtimestamp(file_info.st_ctime),
        'mtime': dt.datetime.fromtimestamp(file_info.st_mtime),
        'size_bytes': file_info.st_size
    }
    #return dict(('name',file),('mtime':(arrow.get(file_info.st_mtime), file_info.st_size):


def file_usage_timing(directory):
    ''' generator function which returns ctime, atime, and mtime of files in a directory '''
    files = get_dir_files(directory)
    for file in files:
        file_metadata = get_file_metadata(file)
        #yield (file_metadata['name'], file_metadata['atime'].humanize(), file_metadata['mtime'].humanize(), file_metadata['ctime'].humanize())
        yield (file_metadata['name'], file_metadata['atime'],
               file_metadata['mtime'], file_metadata['ctime'])
    return None


#def main():
#    ''' main function with primary program logic '''
#    directory = get_dir()
#    files = get_dir_files(directory)
#    files_metadata = [get_file_metadata(file) for file in files]
#    files_metadata.insert(0, get_file_metadata(directory))
#    print(f"{'File Name':>60s} {'Last Modified':>20s} {'Bytes':>8}")
#    for file in files_metadata:
#        print(
#            f"{file['name']:>60s} {file['mtime'].humanize():>20s} {file['size_bytes']:>8}"
#        )
#
#
#if __name__ == '__main__':
#    main()

for file in file_usage_timing('./test_dir'):
    time.sleep(1)
    print(
        f'Name: {file[0]}, atime: {file[1]}, mtime: {file[2]}, ctime: {file[3]}'
    )
