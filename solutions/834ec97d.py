def transform(grid):
    h,w=len(grid),len(grid[0]);r,c,color=next((r,c,v) for r,row in enumerate(grid) for c,v in enumerate(row) if v)
    out=[[0]*w for _ in range(h)]
    for x in range(r+1):
        for y in range(c%2,w,2):out[x][y]=4
    if r+1<h:out[r+1][c]=color
    output = out
    return output
