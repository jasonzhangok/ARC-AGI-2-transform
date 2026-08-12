def transform(grid):
    h, w = len(grid), len(grid[0])
    block = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    r0, r1 = min(r for r, _ in block), max(r for r, _ in block)
    c0, c1 = min(c for _, c in block), max(c for _, c in block)
    markers = [(r, c, grid[r][c]) for r in range(h) for c in range(w)
               if grid[r][c] not in (0, 5)]
    colors = {}
    for r, c, value in markers:
        colors[(0 if r < r0 else 1, 0 if c < c0 else 1)] = value
    out = [[0] * w for _ in range(h)]
    rm, cm = (r0 + r1 + 1) // 2, (c0 + c1 + 1) // 2
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            out[r][c] = colors[(0 if r < rm else 1, 0 if c < cm else 1)]
    return out
