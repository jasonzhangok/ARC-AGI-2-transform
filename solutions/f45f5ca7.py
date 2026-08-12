def transform(grid):
    targets = {8: 1, 2: 2, 4: 3, 3: 4}
    h, w = len(grid), len(grid[0])
    out = [[0] * w for _ in range(h)]
    for r, row in enumerate(grid):
        if row[0] != 0:
            out[r][targets[row[0]]] = row[0]
    return out
