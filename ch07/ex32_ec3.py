'''
stuff a config file in a dict
'''
FILENAME = 'os-release'

with open(FILENAME, 'rt') as infile:
    lines = [line.strip().split('=') for line in infile.readlines()]

config_dict = {line[0]:line[1] for line in lines}
