def transform(grid):
    h, w = len(grid), len(grid[0])
    cells = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != 0]
    r0, r1 = min(r for r, _, _ in cells), max(r for r, _, _ in cells)
    c0, c1 = min(c for _, c, _ in cells), max(c for _, c, _ in cells)
    output = [row[:] for row in grid]
    for r, c, color in cells:
        rows = range(r1 + 1, min(h, r1 + 3)) if r == r0 else range(max(0, r0 - 2), r0)
        cols = range(c1 + 1, min(w, c1 + 3)) if c == c0 else range(max(0, c0 - 2), c0)
        for x in rows:
            for y in cols:
                output[x][y] = color
    return output
