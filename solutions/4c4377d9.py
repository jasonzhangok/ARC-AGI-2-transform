def transform(grid):
    output = [row[:] for row in grid[::-1]] + [row[:] for row in grid]
    return output
