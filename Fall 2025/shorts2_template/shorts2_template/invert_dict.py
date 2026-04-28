def invert_dict(origdict):
    new_dict = {}
    for key, value in origdict.items():
        new_dict[value] = key
    return new_dict