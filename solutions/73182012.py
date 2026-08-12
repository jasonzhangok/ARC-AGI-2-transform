def transform(grid):
    pts=[(r,c) for r,row in enumerate(grid) for c,v in enumerate(row) if v];r0,r1=min(r for r,c in pts),max(r for r,c in pts);c0,c1=min(c for r,c in pts),max(c for r,c in pts);hh=(r1-r0+1)//2;ww=(c1-c0+1)//2
    return [grid[r][c0:c0+ww] for r in range(r0,r0+hh)]
