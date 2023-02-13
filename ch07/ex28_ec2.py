'''
sum hex values
'''

def sum_hex(hex_str):
    print(hex(sum([int(i, 16) for i in hex_str.split()])))
