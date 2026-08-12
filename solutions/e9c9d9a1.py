def transform(grid):
    h, w = len(grid), len(grid[0])
    rows = [r for r, row in enumerate(grid) if all(v == 3 for v in row)]
    cols = [c for c in range(w) if all(grid[r][c] == 3 for r in range(h))]
    out = [row[:] for row in grid]
    for r in range(h):
        ri = sum(line < r for line in rows)
        for c in range(w):
            if grid[r][c] != 0:
                continue
            ci = sum(line < c for line in cols)
            if ri == 0 and ci == 0:
                out[r][c] = 2
            elif ri == 0 and ci == len(cols):
                out[r][c] = 4
            elif ri == len(rows) and ci == 0:
                out[r][c] = 1
            elif ri == len(rows) and ci == len(cols):
                out[r][c] = 8
            elif 0 < ri < len(rows) and 0 < ci < len(cols):
                out[r][c] = 7
    return out
