def transform(grid):
    out=[row[:] for row in grid];h=len(grid);w=len(grid[0])
    pts=[(r,c) for r,row in enumerate(grid) for c,v in enumerate(row) if v==1]
    barrier=[(r,c) for r,row in enumerate(grid) for c,v in enumerate(row) if v==2]
    vertical=len({r for r,c in barrier})>len({c for r,c in barrier})
    ends=[p for p in pts if sum(abs(p[0]-q[0])==1 and abs(p[1]-q[1])==1 for q in pts)==1]
    for start in ends:
        neighbor=next(q for q in pts if abs(start[0]-q[0])==1 and abs(start[1]-q[1])==1)
        dr,dc=start[0]-neighbor[0],start[1]-neighbor[1]
        r,c=start
        while True:
            nr,nc=r+dr,c+dc
            if not(0<=nr<h and 0<=nc<w):break
            if grid[nr][nc]==2:
                if vertical:dc=-dc
                else:dr=-dr
                nr,nc=r+dr,c+dc
                if not(0<=nr<h and 0<=nc<w):break
            r,c=nr,nc;out[r][c]=1
    return out
