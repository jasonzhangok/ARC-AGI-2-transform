def transform(grid):
    return [row + row[::-1] + row + row[::-1] + row for row in grid]
