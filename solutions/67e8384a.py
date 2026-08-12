def transform(grid):
    top=[row+row[::-1] for row in grid]
    return top+top[::-1]
