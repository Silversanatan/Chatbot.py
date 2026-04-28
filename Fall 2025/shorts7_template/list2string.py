def list2string(arglist):
    if arglist == []:
        return ''
    return arglist[0] + list2string(arglist[1:])