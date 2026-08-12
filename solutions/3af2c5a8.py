def transform(grid):
    top = [row + row[::-1] for row in grid]
    return top + [row[:] for row in reversed(top)]
