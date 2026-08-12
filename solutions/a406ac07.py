def transform(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    bottom = grid[-1]
    for r in range(h - 1):
        color = grid[r][-1]
        for c, v in enumerate(bottom):
            if v == color: out[r][c] = color
    return out
