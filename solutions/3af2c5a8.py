def transform(grid):
    top = [row + row[::-1] for row in grid]
    output = top + [row[:] for row in reversed(top)]
    return output
