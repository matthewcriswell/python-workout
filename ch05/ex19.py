'''
Handles some /etc/passwd stuff
'''

FILENAME = 'example-etc-passwd'
PASSWD_FIELDS = [
    'username', 'password', 'uid', 'gid', 'userinfo', 'home_dir', 'shell'
]


def passwd_to_dict(filename):
    ''' reads an /etc/passwd file and stuffs contents into a list of dicts '''
    filename = FILENAME
    with open(filename, 'rt', encoding='UTF-8') as file:
        contents = file.readlines()
    passwd_entries = [
        dict(zip(PASSWD_FIELDS, item))
        for item in [entry.strip().split(':') for entry in contents]
    ]
    user_uid = {}
    _ = [
        user_uid.update({entry['username']: entry['uid']})
        for entry in passwd_entries
    ]
    return user_uid


#passwd_entries = passwd_to_dict(FILENAME)
#print(passwd_entries)
print(passwd_to_dict(FILENAME))
