def transform(grid):
    height = len(grid)
    output = [
        [0] * (height - 1 - r) + row[:] + [0] * r
        for r, row in enumerate(grid)
    ]
    return output
