def transform(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    red = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    r0, r1 = min(r for r, _ in red), max(r for r, _ in red)
    c0, c1 = min(c for _, c in red), max(c for _, c in red)
    for r in range(r0, r1 + 1):
        if not any(grid[r][c] not in (0, 2) for c in range(c0)):
            for c in range(c0): out[r][c] = 2
        if not any(grid[r][c] not in (0, 2) for c in range(c1 + 1, w)):
            for c in range(c1 + 1, w): out[r][c] = 2
    for c in range(c0, c1 + 1):
        if not any(grid[r][c] not in (0, 2) for r in range(r0)):
            for r in range(r0): out[r][c] = 2
        if not any(grid[r][c] not in (0, 2) for r in range(r1 + 1, h)):
            for r in range(r1 + 1, h): out[r][c] = 2
    return out
