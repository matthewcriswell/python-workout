'''  menu. The function takes any number of key-value pairs as arguments. Each value should be a callable '''

class InvalidKeyword(Exception):
    pass

def get_input(valid_keywords):
    ''' gets user input '''
    user_input = input(f"Select one of: {valid_keywords} ")
    if user_input not in valid_keywords:
        print(f'{user_input} is not a valid option')
        return InvalidKeyword()
    return user_input

def menu(**options):
    ''' return function '''
    valid_keywords = options.keys()
    user_input = get_input(valid_keywords)
    while isinstance(user_input, InvalidKeyword):
        print("Please try again.")
        user_input = get_input(valid_keywords)
    return options[user_input]()
