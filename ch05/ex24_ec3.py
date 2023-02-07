import csv
from operator import itemgetter

PASSWD_FILE = 'example-etc-passwd'
PASSWD_FIELDS = [
    'username', 'password', 'uid', 'gid', 'userinfo', 'home_dir', 'shell'
]

with open(PASSWD_FILE, 'rt', encoding='UTF-8') as infile:
    passwd_list = []
    csv_in = csv.reader(infile, delimiter=':')
    for line in csv_in: 
        if len(line) == len(PASSWD_FIELDS):
            passwd_list.append(dict(list(zip(PASSWD_FIELDS,[entry for entry in line]))))


shell_set = set([item['shell'] for item in passwd_list])
for i in shell_set:
    print(i, *[item['username'] for item in passwd_list if item['shell'] == i])
