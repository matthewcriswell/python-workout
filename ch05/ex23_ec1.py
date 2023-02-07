'''
convert etc/passwd to JSON formatted file

The JSON file will contain the equivalent of a list of Python tuples, with each tuple representing one line from the file.
'''

import csv
import json

PASSWD_FIELDS = [
    'username', 'password', 'uid', 'gid', 'userinfo', 'home_dir', 'shell'
]

passwd_file = 'example-etc-passwd'
json_out_file = 'etc-passwd.json'

with open(passwd_file, 'rt', encoding='UTF-8') as infile:
    in_csv = csv.reader(infile, delimiter=':')
    with open(json_out_file, 'wt', encoding='UTF-8') as outfile:
        for row in in_csv:
            if len(row) == len(PASSWD_FIELDS):
                json.dump(dict(tuple(zip(PASSWD_FIELDS, row))), outfile)
