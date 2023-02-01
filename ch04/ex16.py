def dictdiff(d1, d2):

    print(f"d1: {d1}")
    print(f"d2: {d2}")

    diff_list = list(set(d1.items()) ^ set(d2.items()))
    if diff_list:
        print("There is a difference.")
        #print(*diff_list)
        #return diff_list

        temp_dict = {}
        if set([item[0] for item in diff_list]):
            for key in set([item[0] for item in diff_list]):
                temp_dict.update({key:[d1.get(key), d2.get(key)]})
                #print(f"{temp_dict}")
                #print(f"{key}:[{d1.get(key)}, {d2.get(key)}]")
        #set([item[1] for item in diff_list])
        print(f"{temp_dict}")
    print("")

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
d5 = {'a':1, 'b':2, 'd':4}

dictdiff(d1, d1)
dictdiff(d1, d2)
dictdiff(d3, d4)
dictdiff(d1, d5)

