def transform(grid):
    output = [[5 if value == 7 else value for value in row] for row in grid]
    return output
