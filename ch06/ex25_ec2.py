'''
numbers and stuff
'''

def factorial(*args):
    ''' multiple args by each other '''
    output = 1
    for item in args:
        output = int(item) * output
    return output
