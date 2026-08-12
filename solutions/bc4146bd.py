def transform(grid):
    output = [row + row[::-1] + row + row[::-1] + row for row in grid]
    return output
