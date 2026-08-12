def transform(grid):
    h,w=len(grid),len(grid[0]); out=[row[:] for row in grid]
    cells=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==2]
    r0=cells[0][0]; c0=min(c for _,c in cells); n=len(cells)
    for r in range(r0):
        length=n+(r0-r)
        for c in range(c0,min(w,c0+length)): out[r][c]=3
    for r in range(r0+1,h):
        length=n-(r-r0)
        for c in range(c0,min(w,c0+max(0,length))): out[r][c]=1
    output = out
    return output
