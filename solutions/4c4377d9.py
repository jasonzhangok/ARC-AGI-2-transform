def transform(grid):
    return [row[:] for row in grid[::-1]] + [row[:] for row in grid]
