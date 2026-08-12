def transform(grid):
    h,w=len(grid),len(grid[0]);r,c,color=next((r,c,v) for r,row in enumerate(grid) for c,v in enumerate(row) if v);out=[[0]*w for _ in range(h)]
    up=True;x=c
    while x<w:
        for y in range(h):out[y][x]=color
        if x+1<w:out[0 if up else h-1][x+1]=5
        up=not up;x+=2
    output = out
    return output
