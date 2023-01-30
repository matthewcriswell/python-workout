user_creds = {
'matt': 'jabroni123',
'bojack': 'blow123',
'tom': 'secretSecret',
'root': 'SuperAdmin123'
}
auth_loop = True
valid_users = set(user_creds.keys())
while auth_loop:
    user = input("Enter username: ").strip()
    if user in valid_users:
        while True:
            password = input("Enter password: ").strip()
            if password == user_creds[user]:
                print("Successful auth.")
                auth_loop = False
                break
            else:
                print("Unsuccessful auth.")
                break
        auth_loop = False
        break
    else:
        print("Invalid user.")
        auth_loop = False
