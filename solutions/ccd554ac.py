def transform(grid):
    n = len(grid)
    return [row * n for _ in range(n) for row in grid]
