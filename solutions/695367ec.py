def transform(grid):
    n=len(grid); color=grid[0][0]
    output = [[color if r%(n+1)==n or c%(n+1)==n else 0 for c in range(15)] for r in range(15)]
    return output
