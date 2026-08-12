def transform(grid):
    output = [[1 if all(row == row[::-1] for row in grid) else 7]]
    return output
