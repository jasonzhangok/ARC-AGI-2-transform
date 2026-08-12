def transform(grid):
    n = len({v for row in grid for v in row})
    rows = [row * n for row in grid]
    output = [row[:] for _ in range(n) for row in rows]
    return output
