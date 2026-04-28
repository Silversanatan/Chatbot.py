def shuffle_dict(somedict):
    sorted_k= sorted(list(somedict.keys()))
    sorted_v= sorted(list(somedict.values()))
    shuffled_dict = {}
    for i in range(len(sorted_k)):
        shuffled_dict[sorted_k[i]] = sorted_v[i]
        
    return shuffled_dict