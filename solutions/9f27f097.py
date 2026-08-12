def transform(grid):
    h, w = (len(grid), len(grid[0]))
    bg = {}
    for cell_value in (v for row in grid for v in row):
        bg[cell_value] = bg.get(cell_value, 0) + 1
    bg = max(bg, key=bg.get)
    zero = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 0]
    zr0, zr1 = (min((r for r, _ in zero)), max((r for r, _ in zero)))
    zc0, zc1 = (min((c for _, c in zero)), max((c for _, c in zero)))
    colors = [v for row in grid for v in row if v not in (bg, 0)]
    ink = {}
    for cell_value in colors:
        ink[cell_value] = ink.get(cell_value, 0) + 1
    ink = max(ink, key=ink.get)
    cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != bg and grid[r][c] != 0]
    sr0, sr1 = (min((r for r, _ in cells)), max((r for r, _ in cells)))
    sc0, sc1 = (min((c for _, c in cells)), max((c for _, c in cells)))
    out = [row[:] for row in grid]
    for i in range(zr1 - zr0 + 1):
        for j in range(zc1 - zc0 + 1):
            out[zr0 + i][zc0 + j] = grid[sr0 + i][sc1 - j]
    output = out
    return output
