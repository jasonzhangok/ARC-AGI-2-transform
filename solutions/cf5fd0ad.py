def transform(grid):
    r90 = [list(row) for row in zip(*grid[::-1])]
    r180 = [list(row) for row in zip(*r90[::-1])]
    r270 = [list(row) for row in zip(*r180[::-1])]
    top = [a + a + b + b for a, b in zip(r180, r90)]
    bottom = [a + a + b + b for a, b in zip(r270, grid)]
    output = top + top + bottom + bottom
    return output
