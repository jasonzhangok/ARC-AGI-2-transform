def transform(grid):
    result = [[5] * len(grid[0]) for _ in grid]
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value != 0 and c > 0:
                result[r][c - 1] = value
    output = result
    return output
