def grid_is_square(arglist):
    numrow = len(arglist)
    if numrow == 0:
        return True
    for row in arglist:
        if len(row) != numrow:
            return False
    return True