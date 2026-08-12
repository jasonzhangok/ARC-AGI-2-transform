def transform(grid):
    base=[row[::-1] for row in grid[::-1]]
    top=[row+row[::-1] for row in base]
    output = top+top[::-1]
    return output
