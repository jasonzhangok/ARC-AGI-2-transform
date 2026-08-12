def transform(grid):
    h, w = len(grid), len(grid[0])
    cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0]
    color = grid[cells[0][0]][cells[0][1]]
    r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
    c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
    dr = -r0 if color == 6 else (h - 1 - r1 if color == 4 else 0)
    dc = w - 1 - c1 if color == 8 else 0
    out = [[0] * w for _ in range(h)]
    for r, c in cells:
        out[r + dr][c + dc] = color
    return out
