def floatfunc(base, before, after):
    str_base = str(base)
    point = str_base.index('.')
    before_str = str_base[point-before:point]
    after_str = str_base[point+1:point+after+1]
    post_str = before_str + '.' + after_str
    return float(post_str)
