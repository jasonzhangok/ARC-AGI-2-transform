def transform(grid):
    output = [row[:] for row in grid] + [row[:] for row in reversed(grid)]
    return output
