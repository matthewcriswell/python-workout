def dictsmash(sequence):
    output_dict = {}
    for item in sequence:
        if isinstance(item, dict):
            output_dict.update(item)
        else:
            print("Non-dictionary item in sequence")

    return output_dict


d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
d5 = {'a':1, 'b':2, 'd':4}

