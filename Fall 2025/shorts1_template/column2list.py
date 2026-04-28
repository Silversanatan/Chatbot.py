def column2list(grid, n):
    column = []
    for row in grid:
        column.append(row[n])
    return column