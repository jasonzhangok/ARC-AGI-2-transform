def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    r2, c2 = next((r, c) for r in range(h) for c in range(w) if grid[r][c] == 2)
    r3, c3 = next((r, c) for r in range(h) for c in range(w) if grid[r][c] == 3)
    step = 1 if c3 > c2 else -1
    for c in range(c2 + step, c3 + step, step): out[r2][c] = 8
    step = 1 if r3 > r2 else -1
    for r in range(r2 + step, r3, step): out[r][c3] = 8
    out[r2][c2], out[r3][c3] = 2, 3
    return out
