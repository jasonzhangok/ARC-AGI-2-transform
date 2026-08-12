def transform(grid):
    height, width = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    for r in range(height):
        c = width - 1 - r
        if 0 <= c < width and result[r][c] == 0:
            result[r][c] = 2
    for c in range(width):
        if result[height - 1][c] == 0:
            result[height - 1][c] = 4
    return result
