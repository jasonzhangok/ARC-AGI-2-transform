def transform(grid):
    middle = len(grid[0]) // 2
    return [[value if c == middle else 0 for c, value in enumerate(row)] for row in grid]
