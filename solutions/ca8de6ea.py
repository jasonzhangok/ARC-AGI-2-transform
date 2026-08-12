def transform(grid):
    m = len(grid) // 2
    output = [
        [grid[0][0], grid[m - 1][m - 1], grid[0][-1]],
        [grid[m + 1][m - 1], grid[m][m], grid[m - 1][m + 1]],
        [grid[-1][0], grid[m + 1][m + 1], grid[-1][-1]],
    ]
    return output
