def transform(grid):
    return [list(row) for row in zip(*grid)][::-1]
