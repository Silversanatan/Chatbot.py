def diag2list_rec(grid):
    return diag2list_helper(grid, 0)

def diag2list_helper(grid, index):
    if grid == []:
        return []
    return [grid[0][index]] + diag2list_helper(grid[1:], index + 1)