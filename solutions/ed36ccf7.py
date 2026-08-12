def transform(grid):
    output = [list(row) for row in zip(*grid)][::-1]
    return output
