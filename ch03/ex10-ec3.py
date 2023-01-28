def dict_flattener(list_o_dicts):
    ''' takes a list of dicts and flattens them into a single dictionary '''
    new_list = []
    modification = False
    for item in list_o_dicts:
        for i in item.keys():
            for new_item in new_list:
                if i in new_item.keys():
                    if isinstance(new_item[i], list):
                        new_item[i].append(item[i])
                        modification = True
                    else:
                        new_item[i] = [new_item[i], item[i]]
                        modification = True
            if not modification:
                new_list.append({i: item[i]})
            else:
                pass
    a_dict = {}
    for item in new_list:
        for i in item.keys():
            dict_key = i
            dict_value = item[i]
            a_dict[dict_key] = dict_value

    return a_dict
