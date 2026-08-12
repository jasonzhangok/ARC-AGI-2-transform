def transform(grid):
    out=[[0]*len(grid[0]) for _ in grid]
    vals=[(r,c,grid[r][c]) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c]!=0]
    rows=sorted(set(r for r,_,_ in vals))
    for r,c,v in vals:
        out[0 if r==rows[0] else len(grid)-1][0 if c==min(x[1] for x in vals if x[0]==r) else len(grid[0])-1]=v
    output = out
    return output
