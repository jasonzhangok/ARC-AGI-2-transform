def transform(grid):
    ccw = [list(row) for row in zip(*grid)][::-1]
    half = [row[::-1] for row in grid[::-1]]
    cw = [list(row) for row in zip(*grid[::-1])]
    n = len(grid)
    return [grid[r] + ccw[r] for r in range(n)] + [half[r] + cw[r] for r in range(n)]
