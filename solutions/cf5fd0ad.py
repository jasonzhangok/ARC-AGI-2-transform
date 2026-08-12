def transform(grid):
    def rotate90(g):
        return [list(row) for row in zip(*g[::-1])]

    r90 = rotate90(grid)
    r180 = rotate90(r90)
    r270 = rotate90(r180)
    top = [a + a + b + b for a, b in zip(r180, r90)]
    bottom = [a + a + b + b for a, b in zip(r270, grid)]
    return top + top + bottom + bottom
