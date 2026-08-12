def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    color = next(v for row in grid for v in row if v != 0)
    for d in range(-(h - 1), w):
        cells = [(r, r + d) for r in range(h) if 0 <= r + d < w and grid[r][r+d] == color]
        for i, (r, c) in enumerate(cells):
            if i % 2 == 1: out[r][c] = 4
    return out
