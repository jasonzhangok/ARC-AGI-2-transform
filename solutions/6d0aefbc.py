def transform(grid):
    output = [row+row[::-1] for row in grid]
    return output
