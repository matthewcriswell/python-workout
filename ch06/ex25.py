'''
handle different parameters
'''


def inner_flatten(my_tup):
    ''' flatten a tuple into a string '''
    my_str = ''
    for i in my_tup:
        my_str = my_str + ' ' + i
    return my_str.strip()


def dict_flatten(my_dict):
    ''' flatten a dict into a preformatted string '''
    my_str = ''
    for i in my_dict.keys():
        my_str = my_str + str(i) + '=' + '"' + str(my_dict[i]) + '"' + ' '
    return my_str.strip()


def myxml(*args, **kwargs):
    ''' return an XML string '''
    outer_val = args[0]
    if len(args) > 1:
        inner_val = inner_flatten(args[1:])
    else:
        inner_val = None
    if kwargs:
        attrs = dict_flatten(kwargs)
        if inner_val:
            return f'<{outer_val} {attrs}>{inner_val}<{outer_val}>'
        return f'<{outer_val} {attrs}><{outer_val}>'
    if inner_val:
        return f'<{outer_val}>{inner_val}<{outer_val}>'
    return f'<{outer_val}><{outer_val}>'
