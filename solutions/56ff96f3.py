def transform(grid):
    out=[row[:] for row in grid];groups={}
    for r,row in enumerate(grid):
        for c,v in enumerate(row):
            if v:groups.setdefault(v,[]).append((r,c))
    for color,cells in groups.items():
        r0,r1=min(r for r,_ in cells),max(r for r,_ in cells);c0,c1=min(c for _,c in cells),max(c for _,c in cells)
        for r in range(r0,r1+1):
            for c in range(c0,c1+1):out[r][c]=color
    output=out
    return output
