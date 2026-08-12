def transform(grid):
    out=[row[:] for row in grid];pts8=[(r,c) for r,row in enumerate(grid) for c,v in enumerate(row) if v==8];pts4=[(r,c) for r,row in enumerate(grid) for c,v in enumerate(row) if v==4]
    r0,r1=min(r for r,c in pts8),max(r for r,c in pts8);c0,c1=min(c for r,c in pts8),max(c for r,c in pts8);width=c1-c0+1
    top=min(r for r,c in pts4);tip=next(c for r,c in pts4 if r==top);center=(min(c for r,c in pts4)+max(c for r,c in pts4))/2;right=tip>center
    nc0=c1+1 if right else c0-width
    for r,c in pts8:
        nc=nc0+(c1-c)
        if 0<=nc<len(grid[0]):out[r][nc]=8
    return out
