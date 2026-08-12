def transform(grid):
    n=len({v for row in grid for v in row if v!=0})
    output = [[v for v in row for _ in range(n)] for row in grid for _ in range(n)]
    return output
