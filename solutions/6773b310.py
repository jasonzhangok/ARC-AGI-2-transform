def transform(grid):
    output = [[1 if sum(grid[4*r+i][4*c+j]==6 for i in range(3) for j in range(3))==2 else 0 for c in range(3)] for r in range(3)]
    return output
