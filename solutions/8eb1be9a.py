def transform(grid):
    h, w = len(grid), len(grid[0])
    rows = [r for r in range(h) if any(grid[r][c] != 0 for c in range(w))]
    r0, r1 = min(rows), max(rows)
    motif = [row[:] for row in grid[r0:r1 + 1]]
    period = len(motif)
    return [motif[(r - r0) % period][:] for r in range(h)]
