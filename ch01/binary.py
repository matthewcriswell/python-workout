def to_bin(x):
    binary_list = []
    while x > 0:
        if not x%2:
            x = x / 2
            binary_list.append(0)
        else:
            x = x - 1
            x = x / 2
            binary_list.append(1)
    binary_list.reverse()
    return binary_list

def to_trey(x):
    ternary_list = []
    while x > 0:
        if not x%3:
            x = int(x / 3)
            ternary_list.append(0)
        else:
            remainder = int(x%3)
            ternary_list.append(remainder)
            x = x - remainder
            x = int(x / 3)
    ternary_list.reverse()
    return ternary_list

def to_base(x, base):
    base_list = []
    while x > 0:
        if not x % base:
            x = int(x/base)
            base_list.append(0)
        else:
            remainder = int(x%base)
            if remainder == 10:
                base_list.append('A')
            elif remainder == 11:
                base_list.append('B')
            elif remainder == 12:
                base_list.append('C')
            elif remainder == 13:
                base_list.append('D')
            elif remainder == 14:
                base_list.append('E')
            elif remainder == 15:
                base_list.append('F')
            else:
                base_list.append(remainder)
            x = x - remainder
            x = int(x/base)
    base_list.reverse()
    return base_list

for i in range(0,101):
    result = to_bin(i)
    print(i, str(result))

