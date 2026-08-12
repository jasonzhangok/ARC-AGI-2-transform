def transform(grid):
    color=next(v for row in grid for v in row if v);mapped={5:4,8:2,3:1}[color]
    output = [[0 if v else mapped for v in row] for row in grid]
    return output
