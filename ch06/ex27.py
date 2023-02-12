'''
password generator factory function
'''

from random import choice

def create_password_generator(valid_chars):
    ''' takes a string of valid chars and makes a generator function '''

    def passwd_gen(num_chars):
        ''' takes a number and returns a randomly generated string of that length '''
        nonlocal valid_chars
        random_chars = []
        for i in range(num_chars):
            random_chars.append(choice(valid_chars))
        return ''.join(random_chars)

    return passwd_gen
