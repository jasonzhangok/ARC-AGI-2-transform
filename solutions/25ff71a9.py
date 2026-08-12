def transform(grid):
    output = [[0] * len(grid[0])] + [row[:] for row in grid[:-1]]
    return output
