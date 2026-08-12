def transform(grid):
    output = [[6 if c % 3 == 0 and value == 4 else value for c, value in enumerate(row)] for row in grid]
    return output
