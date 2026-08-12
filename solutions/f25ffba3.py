def transform(grid):
    pattern = [row[:] for row in grid[len(grid) // 2:]]
    return [row[:] for row in pattern[::-1]] + pattern
