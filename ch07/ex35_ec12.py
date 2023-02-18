'''
read a sample config and stuff it in a dict
'''

def load_config(filename):
    ''' read config file and put in a dict '''
    with open(filename,'rt') as in_f:
        return {k:int(v) for k,v in (line.strip().split('=') for line in in_f.readlines()) if v.isdigit()}
