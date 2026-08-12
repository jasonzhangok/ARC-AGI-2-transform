def transform(grid):
    output = [[value for value in row for _ in range(2)] for row in grid for _ in range(2)]
    return output
