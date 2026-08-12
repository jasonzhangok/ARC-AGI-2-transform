def transform(grid):
    output = [[8 if value == 5 else 5 if value == 8 else value for value in row] for row in grid]
    return output
