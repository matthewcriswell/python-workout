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
        for item in [entry.strip().split(':') for entry in contents]
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


def factor_nums(nums):
    ''' returns a dict of factors from a list of nums '''
    output_dict = {}
    for x in nums:
        output = []
        for i in range(1, x):
            if x % i == 0:
                numerator = x
                denominator = i
                quotient = int(numerator / denominator)
                if denominator not in output and quotient not in output:
                    output.append(denominator)
                    output.append(quotient)
        output_dict.update({x: sorted(set((output)))})
    return output_dict


#user_nums = input("Enter some integers separate by a space:").split()
user_nums = [
    int(item)
    for item in input("Enter some integers separate by a space:").split()
]
print(factor_nums(user_nums))

# From /etc/passwd, create a dict in which the keys are the usernames (as in the main exercise) and the values are themselves dicts with keys (and appropriate values) for user ID, home directory, and shell.#

#{username: {uid, home, shell}}
# 'username', 'password', 'uid', 'gid', 'userinfo', 'home_dir', 'shell'

user_info_dict = {}
for i in [entry['username'] for entry in passwd_list]:
    for item in [entry for entry in passwd_list if entry['username'] == i]:
        uid = item['uid']
        home_dir = item['home_dir']
        shell = item['shell']
        user_info_dict.update({
            i: {
                'uid': item['uid'],
                'home_dir': item['home_dir'],
                'shell': item['shell']
            }
        })
print(user_info_dict)
