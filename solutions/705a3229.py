def transform(grid):
    h,w=len(grid),len(grid[0]);out=[row[:] for row in grid]
    for r,c in [(r,c) for r in range(h) for c in range(w) if grid[r][c]!=0]:
        color=grid[r][c];vr=range(0,r+1) if r<h/2 else range(r,h);hc=range(0,c+1) if c<w/2 else range(c,w)
        for x in vr:out[x][c]=color
        for y in hc:out[r][y]=color
    output = out
    return output
