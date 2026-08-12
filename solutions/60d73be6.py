def transform(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    bg = max((v for row in grid for v in row), key=lambda v: sum(x == v for row in grid for x in row))
    sr = next(r for r, row in enumerate(grid) if len(set(row)) == 1 and row[0] != bg)
    sc = next(c for c in range(w) if len(set(grid[r][c] for r in range(h))) == 1 and grid[0][c] != bg)
    marks = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != bg]
    for r, c, color in marks:
        for rr in {r, 2 * sr - r}:
            for cc in {c, 2 * sc - c}:
                if 0 <= rr < h and 0 <= cc < w:
                    out[rr][cc] = color
    return out
