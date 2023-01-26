
def transpose_strings(list_o_strings):
    ''' whacky swapparoo '''
    new_string_list = []
    inner = 3 #len(list_o_strings.split())
    outer = len(list_o_strings)
    for i in range(0,inner):
        for j in range(0,outer):
            print(f"j:{j}, i:{i}")
            new_string_list.append(list_o_strings[j].split()[i])
    return new_string_list
