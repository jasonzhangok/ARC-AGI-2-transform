def transform(grid):
    width = len(grid[0])
    return [[5] * width if len(set(row)) == 1 else [0] * width for row in grid]
