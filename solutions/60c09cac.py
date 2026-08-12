def transform(grid):
    output = [[v for v in row for _ in range(2)] for row in grid for _ in range(2)]
    return output
