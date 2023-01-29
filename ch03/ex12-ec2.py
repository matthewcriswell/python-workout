from operator import itemgetter
from collections import Counter

def read_passwd(filename):
    ''' reads an /etc/passwd file and returns a dict of each line '''
    contents_list = []
    fields = ['user', 'password', 'uid', 'gid', 'userinfo', 'homedir', 'shell']
    #shell_count = Counter()
    with open(filename, 'rt') as file:
        lines = [line.rstrip().split(':') for line in file]
        for line in lines:
            contents_list.append(dict(zip(fields, line)))
            #count.add(tuple(zip(fields, line)))
    return contents_list #, count


passwd_list = read_passwd('example-etc-passwd')


for entry in sorted(passwd_list, key=itemgetter('shell', 'user'), reverse=True):
    print(f"{entry['user']}:{entry['shell']}")

#shell stats
shell_count = Counter([item['shell'] for item in passwd_list])
print(f"Shell stats: {shell_count}")
