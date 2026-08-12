def transform(grid):
    middle = len(grid[0]) // 2
    output = [[value if c == middle else 0 for c, value in enumerate(row)] for row in grid]
    return output
