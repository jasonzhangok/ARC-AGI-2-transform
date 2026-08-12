def transform(grid):
    n = sum(v != 0 for row in grid for v in row)
    order = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)]
    out = [[0] * 3 for _ in range(3)]
    for r, c in order[:n]:
        out[r][c] = 2
    return out
