def transform(grid):
    h, w = len(grid), len(grid[0])
    counts = {color: sum(row.count(color) for row in grid) for color in range(1, 5)}
    out = [[0] * w for _ in range(h)]
    for c, color in enumerate(range(1, 5)):
        for r in range(h - counts[color], h):
            out[r][c] = color
    return out
