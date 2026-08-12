def transform(grid):
    vals=[row[0] for row in grid]
    vals[0],vals[1]=vals[1],vals[0]
    vals[-2],vals[-1]=vals[-1],vals[-2]
    output = [[v] for v in vals]
    return output
