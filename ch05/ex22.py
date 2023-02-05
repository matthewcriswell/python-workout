'''
create a function, passwd_to_csv, that takes two filenames as arguments: the first is a passwd-style file to read from, and the second is the name of a file in which to write the output.
'''

import csv
from collections import namedtuple


def passwd_to_csv(passwd_file, csv_output):
    ''' converts a passwd formatted file to csv '''
    User = namedtuple("User", "username uid")
    users_list = []
    with open(passwd_file, 'rt') as file:
        for entry in file:
            entry = entry.split(':')
            try:
                username = entry[0]
            except:
                username = ''
            try:
                uid = entry[2]
            except:
                uid = -1
            if uid == -1 or not username:
                print(f"Unable to parse: {entry}")
            else:
                users_list.append(User(username, uid))
    with open(csv_output, 'w') as outfile:
        o = csv.writer(outfile, delimiter='\t')
        for entry in users_list:
            o.writerow([entry.username, entry.uid])
