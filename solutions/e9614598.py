def transform(grid):
    out = [row[:] for row in grid]
    points = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 1]
    (r1, c1), (r2, c2) = points
    r, c = (r1 + r2) // 2, (c1 + c2) // 2
    for dr, dc in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
        out[r + dr][c + dc] = 3
    for y, x in points:
        out[y][x] = 1
    return out
