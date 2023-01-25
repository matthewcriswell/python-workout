def hex_output(hex_num):
    hex_num_list = list(hex_num)
    hex_num_list.reverse()
    iteration = 0
    total = 0
    for i in hex_num_list:
        if i ==  'A':
            num = 10
        elif i == 'B':
            num = 11
        elif i == 'C':
            num = 12
        elif i == 'D': 
            num = 13
        elif i == 'E':
            num = 14
        elif i == 'F':
            num = 15
        else:
            num = int(i)
        total += num * (16 ** iteration)
        iteration += 1
    return total 
        
