def transform(grid):
    w = len(grid[0])
    out = []
    for row in grid:
        n = next((i for i, v in enumerate(row) if v == 0), w)
        seed = row[:n]
        middle = [seed[-1]] * (w - len(seed) - len(seed) + 1)
        out.append(seed + middle + seed[1:])
    return out
