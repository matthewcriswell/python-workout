'''
asking the user to enter a space-separated list of integers, indicating which fields should be written to the output CSV file. Also ask the user which character should be used as a delimiter in the output file. Then read from /etc/passwd, writing the user’s chosen fields, separated by the user’s chosen delimiter
'''

import csv
from collections import namedtuple

PASSWD_FIELDS = [
    'username', 'password', 'uid', 'gid', 'userinfo', 'home_dir', 'shell'
]


def passwd_to_csv(passwd_list, user_delimiter, field_list):
    ''' take a passwd_list and writes it to a file with '''
    csv_output = 'test_output.csv'
    with open(csv_output, 'w') as outfile:
        o = csv.writer(outfile, delimiter=user_delimiter)
        o.writerow([PASSWD_FIELDS[i] for i in field_list])
        [
            o.writerow([entry[i] for i in field_list])
            for entry in passwd_entries_list
        ]


def passwd_list(filename):
    ''' reads a passwd file and puts entries in a list of namedtuples '''
    Entry = namedtuple("Entry", PASSWD_FIELDS)
    passwd_entries = []
    with open(filename, 'rt', encoding='UTF-8') as file:
        for line in file:
            split_line = [item for item in line.strip().split(':')]
            if len(split_line) > 1:
                passwd_entries.append(Entry(*split_line))
            else:
                print(f"skipping: {split_line}")
    return passwd_entries


def prompt_user():
    ''' get desired fields and delimiter '''
    valid_delims = set(['\t', '.', ':', ' ', ',', ';'])
    desired_fields = input(
        'Enter the numer(s) of the /etc/passwd field(s):').split(' ')
    desired_fields = [int(item) for item in desired_fields]
    user_delimiter = input('Input the delimiter character:')
    if user_delimiter not in valid_delims:
        print("Invalid delimiter, defaulting to ','.")
        user_delimiter = ','
    return (user_delimiter, desired_fields)


user_options = prompt_user()
passwd_entries_list = passwd_list('example-etc-passwd')
passwd_to_csv(passwd_entries_list, user_options[0], user_options[1])
