def transform(grid):
    colors=(2,4,3)
    return [[colors[row.index(5)]]*len(row) for row in grid]
