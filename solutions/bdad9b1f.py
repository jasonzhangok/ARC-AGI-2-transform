def transform(grid):
    h, w = len(grid), len(grid[0])
    vertical_col = next(c for r in range(h) for c in range(w) if grid[r][c] == 8)
    horizontal_row = next(r for r in range(h) for c in range(w) if grid[r][c] == 2)
    output = [[0] * w for _ in range(h)]
    for r in range(h):
        output[r][vertical_col] = 8
    for c in range(w):
        output[horizontal_row][c] = 2
    output[horizontal_row][vertical_col] = 4
    return output
