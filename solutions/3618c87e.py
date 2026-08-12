def transform(grid):
    result = [row[:] for row in grid]
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == 1:
                result[r][c] = 0
                result[-1][c] = 1
    output = result
    return output
