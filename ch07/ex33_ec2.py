'''
Use a dict comprehension to create a dict in which the keys are usernames and the values are (integer) user IDs, based on a Unix-style /etc/passwd file.
'''

with open('example-etc-passwd', 'rt') as in_f:
    lines = [
        line.strip().split(':') for line in in_f.readlines()
        if len(line.strip().split(':')) == 7
    ]

passwd_dict = {line[0]: int(line[3]) for line in lines}

for username, uid in passwd_dict.items():
    print(f'username: {username}, uid: {uid}')
