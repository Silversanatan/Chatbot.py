def list2dict(list2d):
    result_dict = {}
    for row in list2d:
        if len(row)>0:
            key = row[0]
            values = row[1:]
            result_dict[key] = values
    return result_dict