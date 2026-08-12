def transform(grid):
    pts=[(r,c) for r,row in enumerate(grid) for c,v in enumerate(row) if v==8];out=[row[:] for row in grid]
    r0,r1=min(r for r,c in pts),max(r for r,c in pts);c0,c1=min(c for r,c in pts),max(c for r,c in pts)
    for r in range(r0,r1+1):
        for c in range(c0,c1+1):
            if out[r][c]==0:out[r][c]=2
    output = out
    return output
