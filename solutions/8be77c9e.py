def transform(grid):
    return [row[:] for row in grid] + [row[:] for row in reversed(grid)]
