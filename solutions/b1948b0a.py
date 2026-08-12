def transform(grid):
    output = [[2 if v==6 else v for v in row] for row in grid]
    return output
