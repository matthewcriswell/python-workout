'''
password generator factory function
'''

from random import choice
from collections import Counter


def create_password_generator(valid_chars):
    ''' takes a string of valid chars and makes a generator function '''

    def passwd_gen(num_chars):
        ''' takes a number and returns a randomly generated string of that length '''
        random_chars = []
        for i in range(num_chars):
            random_chars.append(choice(valid_chars))
        return ''.join(random_chars)

    return passwd_gen


def create_password_checker(min_uppercase, min_lowercase, min_punctuation,
                            min_digits):
    ''' creates a test function based on parameters passed in '''

    def check_passwd(passwd):
        char_count = Counter()
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        punctuation = '!@#$%^&*()-_,.?/'
        digits = '1234567890'
        for i in passwd:
            if i in lowercase:
                char_count['lowercase'] += 1
            elif i in uppercase:
                char_count['uppercase'] += 1
            elif i in punctuation:
                char_count['punctuation'] += 1
            elif i in digits:
                char_count['digits'] += 1
            else:
                print('unknown chars')
        if char_count['lowercase'] >= min_lowercase and char_count[
                'uppercase'] >= min_uppercase and char_count[
                    'punctuation'] >= min_punctuation and char_count[
                        'digits'] >= min_digits:
            return True
        else:
            return False

    return check_passwd
