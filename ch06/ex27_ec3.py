'''
perform 2 functions as a closure
'''

def doboth(func_1, func_2):
    ''' return a function that invokes 2 functions passed in '''
    def bothinate(i):
        return func_2(func_1(i))
    return bothinate
