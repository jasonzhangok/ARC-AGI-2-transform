def transform(grid):
    return [[1 if all(row == row[::-1] for row in grid) else 7]]
