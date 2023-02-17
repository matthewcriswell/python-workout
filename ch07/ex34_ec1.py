'''
Handles some /etc/passwd stuff
'''

FILENAME = 'example-etc-passwd'
PASSWD_FIELDS = [
    'username', 'password', 'uid', 'gid', 'userinfo', 'home_dir', 'shell'
]


def passwd_to_dicts(filename):
    ''' reads an /etc/passwd file and stuffs contents into a list of dicts '''
    filename = FILENAME
    with open(filename, 'rt', encoding='UTF-8') as file:
        contents = file.readlines()
    passwd_entries = [
        dict(zip(PASSWD_FIELDS, item))
        for item in [entry.strip().split(':') for entry in contents if len(entry.strip().split(':')) == 7]
    ]
    return passwd_entries


passwd_list = passwd_to_dicts(FILENAME)

user_shell_dict = {}
for i in set([entry['shell'] for entry in passwd_list]):
    user_shell_dict.update({
        i: [entry['username'] for entry in passwd_list if entry['shell'] == i]
    })

for i in user_shell_dict.keys():
    print(f"{i:<20} Users: {user_shell_dict.get(i)}")
