def transform(grid):
    pattern = [row[:] for row in grid[len(grid) // 2:]]
    output = [row[:] for row in pattern[::-1]] + pattern
    return output
