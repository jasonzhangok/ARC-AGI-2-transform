def transform(grid):
    base=[row[::-1] for row in grid[::-1]]
    top=[row+row[::-1] for row in base]
    return top+top[::-1]
