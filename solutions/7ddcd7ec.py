def transform(grid):
    out=[row[:] for row in grid];color=next(v for row in grid for v in row if v)
    cells={(r,c) for r,row in enumerate(grid) for c,v in enumerate(row) if v==color}
    h,w=len(grid),len(grid[0])
    core=next({(r,c),(r+1,c),(r,c+1),(r+1,c+1)} for r in range(h-1) for c in range(w-1)
              if all(grid[x][y]==color for x,y in ((r,c),(r+1,c),(r,c+1),(r+1,c+1))))
    cr=sum(r for r,c in core)/4;cc=sum(c for r,c in core)/4
    directions={(1 if r>cr else -1,1 if c>cc else -1) for r,c in cells-core}
    for dr,dc in directions:
        r,c=max(cells,key=lambda p:dr*p[0]+dc*p[1])
        x,y=r+dr,c+dc
        while 0<=x<h and 0<=y<w:
            out[x][y]=color;x+=dr;y+=dc
    return out
