def transform(grid):
    height = len(grid)
    return [
        [0] * (height - 1 - r) + row[:] + [0] * r
        for r, row in enumerate(grid)
    ]
