def transform(grid):
    color = next(v for row in grid for v in row if v != 0)
    inverse = [[0 if v == color else color for v in row] for row in grid]
    top = [row + row[:] for row in inverse]
    output = top + [row[:] for row in top]
    return output
