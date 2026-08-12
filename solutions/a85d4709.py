def transform(grid):
    colors=(2,4,3)
    output = [[colors[row.index(5)]]*len(row) for row in grid]
    return output
