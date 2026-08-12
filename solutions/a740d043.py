def transform(grid):
    cells=[(r,c) for r,row in enumerate(grid) for c,v in enumerate(row) if v!=1]
    r0,r1=min(r for r,_ in cells),max(r for r,_ in cells); c0,c1=min(c for _,c in cells),max(c for _,c in cells)
    output = [[0 if grid[r][c]==1 else grid[r][c] for c in range(c0,c1+1)] for r in range(r0,r1+1)]
    return output
