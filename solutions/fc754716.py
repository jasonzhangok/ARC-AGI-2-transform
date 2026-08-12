def transform(grid):
    h, w = len(grid), len(grid[0])
    color = next(value for row in grid for value in row if value != 0)
    return [[color if r in (0, h - 1) or c in (0, w - 1) else 0
             for c in range(w)] for r in range(h)]
