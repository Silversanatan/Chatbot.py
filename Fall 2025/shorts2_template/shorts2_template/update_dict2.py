def update_dict2(dict2, key1, key2, value):
    new_dict2 = {}
    for k, v in dict2.items():
        inner_dict = {}
        for inner_k, inner_v in v.items():
            inner_dict[inner_k] = inner_v
        new_dict2[k] = inner_dict    
    if key1 in new_dict2:
        new_dict2[key1][key2] = value
    else:
        new_dict2[key1] = {key2: value}
    return new_dict2