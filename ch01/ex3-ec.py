def floatfunc(base, before, after):
    str_base = str(base)
    point = str_base.index('.')
    before_str = str_base[point-before:point]
    after_str = str_base[point+1:point+after+1]
    post_str = before_str + '.' + after_str
    return float(post_str)

def strfloat(base, base2):
    str_base = str(base)
    str_base2 = str(base2)

    from decimal import Decimal
    dec_base = Decimal(str_base)
    dec_base2 = Decimal(str_base2)
    dec_sum = dec_base + dec_base2

    print(dec_sum)
    return dec_sum
    
