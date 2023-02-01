def dictsmash(*args):
    output = {}
    key = ''
    val = ''
    for x, i in enumerate(args):
        if x % 2:
            val = i
        if not x % 2:
            key = i
        output.update({key:val})
    return output 
