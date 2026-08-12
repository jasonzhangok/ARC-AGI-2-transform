def transform(grid):
    output = [row[:] for row in grid]
    r8, c8 = next((r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 8)
    r2, c2 = next((r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 2)
    for r in range(min(r8, r2), max(r8, r2) + 1):
        if output[r][c8] == 0:
            output[r][c8] = 4
    for c in range(min(c8, c2), max(c8, c2) + 1):
        if output[r2][c] == 0:
            output[r2][c] = 4
    return output
