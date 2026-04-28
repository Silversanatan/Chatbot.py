def column2list_rec(grid, n):
    if grid == []:
        return []
    return [grid[0][n]] + column2list_rec(grid[1:], n)