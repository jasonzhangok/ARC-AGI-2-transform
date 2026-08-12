def transform(grid):
    h, w = len(grid), len(grid[0])
    red = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    r0, r1 = min(r for r, _ in red), max(r for r, _ in red)
    c0, c1 = min(c for _, c in red), max(c for _, c in red)
    out = [[0] * w for _ in range(h)]
    for r, c in red: out[r][c] = 2
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 5: continue
            nr = min(max(r, r0 - 1), r1 + 1)
            nc = min(max(c, c0 - 1), c1 + 1)
            out[nr][nc] = 5
    return out
