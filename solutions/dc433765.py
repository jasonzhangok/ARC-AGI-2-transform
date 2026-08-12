def transform(grid):
    output = [row[:] for row in grid]
    r3, c3 = next((r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 3)
    r4, c4 = next((r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 4)
    step_r = (r4 > r3) - (r4 < r3)
    step_c = (c4 > c3) - (c4 < c3)
    output[r3][c3] = 0
    output[r3 + step_r][c3 + step_c] = 3
    return output
