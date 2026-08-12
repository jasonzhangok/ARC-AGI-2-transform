def transform(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    centers = []
    for r in range(1, h - 1):
        for c in range(1, w - 1):
            if grid[r][c] == 0 and all(grid[r + dr][c + dc] == 2 for dr, dc in ((1,0),(-1,0),(0,1),(0,-1))):
                centers.append((r, c))
    for r in {r for r, _ in centers}:
        cols = sorted(c for rr, c in centers if rr == r)
        for c1, c2 in zip(cols, cols[1:]):
            for c in range(c1 + 2, c2 - 1):
                if out[r][c] == 0: out[r][c] = 1
    for c in {c for _, c in centers}:
        rows = sorted(r for r, cc in centers if cc == c)
        for r1, r2 in zip(rows, rows[1:]):
            for r in range(r1 + 2, r2 - 1):
                if out[r][c] == 0: out[r][c] = 1
    output = out
    return output
