def transform(grid):
    width = len(grid[0])
    output = [[5] * width if len(set(row)) == 1 else [0] * width for row in grid]
    return output
