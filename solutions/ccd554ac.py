def transform(grid):
    n = len(grid)
    output = [row * n for _ in range(n) for row in grid]
    return output
