def hex_output(hex_num):
    ''' takes a string and converts it from hex to decimal '''

    hex_dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    hex_num_list = list(hex_num.upper())
    hex_num_list.reverse()

    iteration = 0
    total = 0
    for i in hex_num_list:
        num = hex_dict[i]
        total += num * (16 ** iteration)
        iteration += 1
    return total

if __name__ == "__main__":
    print(hex_output('99'))
