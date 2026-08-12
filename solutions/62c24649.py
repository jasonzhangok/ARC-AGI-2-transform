def transform(grid):
    top = [row + row[::-1] for row in grid]
    output = top + top[::-1]
    return output
