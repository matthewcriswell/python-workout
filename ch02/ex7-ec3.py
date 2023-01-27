def url_encode(string):
    ''' simpleton url encoding function '''
    encoded_string = []
    for char in string:
        if not char.isalnum():
            encoded_string.append('%' + ''.join(list(str(hex(ord(char))))[2:]))
        else:
            encoded_string.append(char)
    return ''.join(encoded_string)
