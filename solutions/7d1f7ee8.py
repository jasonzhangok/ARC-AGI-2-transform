def transform(grid):
    out=[row[:] for row in grid];h=len(grid);w=len(grid[0]);rects=[]
    for color in set(v for row in grid for v in row)-{0}:
        cells=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==color]
        for r0,c0 in cells:
            for r1 in range(r0+2,h):
                for c1 in range(c0+2,w):
                    border={(r,c) for r in range(r0,r1+1) for c in range(c0,c1+1)
                            if r in (r0,r1) or c in (c0,c1)}
                    if border and all(grid[r][c]==color for r,c in border):rects.append((r0,r1,c0,c1,color))
    outer=[]
    for q in rects:
        if not any(p[0]<=q[0] and q[1]<=p[1] and p[2]<=q[2] and q[3]<=p[3] and p!=q for p in rects):outer.append(q)
    for r0,r1,c0,c1,color in outer:
        for r in range(r0,r1+1):
            for c in range(c0,c1+1):
                if out[r][c]!=0:out[r][c]=color
    return out
