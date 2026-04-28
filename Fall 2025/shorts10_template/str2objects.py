def str2objects(spec):
    parts = spec.split(None, 1)
    
    if len(parts) == 0:
        return []
    
    token = parts[0]
    current_obj = []
    
    if token == 'dict':
        current_obj = [{}]
    if token == 'list':
        current_obj = [[]]
    if token == 'str':
        current_obj = [""]
        
    rest = ""
    if len(parts) > 1:
        rest = parts[1]
        
    return current_obj + str2objects(rest)