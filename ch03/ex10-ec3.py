def dict_flattener(list_o_dicts):
    new_list = []
    modification = False
    for item in list_o_dicts:
        print(f"evaluating list_o_dicts: {item}")
        for i in item.keys():
            print(f"checking key {i} in {item} list_o_dicts")
            #if False:
            #    print(f"duplicate key")
            #else:
            for new_item in new_list:
                print(f"new_list is currently {new_list}")
                print(f"Iterating over new_list, evaluating: {new_item}")
                if i in new_item.keys():
                    print(f"Checking {new_item} key: {i}:")
                    if isinstance(new_item[i], list):
                        #print("{new_item[i]} already exists as a list; appending {item[i]}")
                        print(f"{new_item[i]} already exists as a list: {type(new_item[i])}; appending {item[i]}")
                        new_item[i].append(item[i])
                        print(f"new_list is currently {new_list}")
                        #break
                        modification = True
                    else:
                        print(f"The key {i} already exists as, pushing {new_item[i]} and {item[i]} as a new list object")
                        print(f"BEFORE new_item[i]: {new_item[i]} type:", type(new_item[i]))
                        new_item[i] = [new_item[i], item[i]]
                        print(f"AFTER new_item[i]: {new_item[i]} type:", type(new_item[i]))
                        print(f"new_list is currently {new_list}")
                        #break
                        modification = True
                    #print(item[i], "exists")
                #else:
            if not modification:
                print(f"new_list did not seem to have items with the key: {i}")
                print(f"appending item {i}, {item[i]} to new_list")
                new_list.append({i: item[i]})
                print(f"new_list is currently {new_list}")
            else:
                print("modication was made")
                    #break
    print(new_list)
    a_dict = {}
    for item in new_list:
        for i in item.keys():
            dict_key = i
            dict_value = item[i]
            a_dict[dict_key] = dict_value
    print(a_dict)
    #return dict(new_list)
    return a_dict
