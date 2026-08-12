def transform(grid):
    h, w = len(grid), len(grid[0])
    background = 7
    r, c, color = next((r, c, grid[r][c]) for r in range(h) for c in range(w)
                       if grid[r][c] != background)
    out = [[background] * w for _ in range(h)]
    left = c == 0
    if r == 0:
        cols = (1, 2) if left else (w - 3, w - 2)
        for y in (1, 2):
            for x in cols:
                out[y][x] = color
    else:
        x = 2 if left else w - 3
        out[h - 4][x] = color
        out[h - 3][x] = color
        out[h - 2][x + (1 if left else -1)] = color
    return out
