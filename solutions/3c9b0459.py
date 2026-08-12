def transform(grid):
    output = [row[::-1] for row in reversed(grid)]
    return output
