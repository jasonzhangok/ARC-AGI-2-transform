def transform(grid):
    h,w=len(grid),len(grid[0]);sep=next(r for r,row in enumerate(grid) if all(v==2 for v in row));out=[row[:] for row in grid]
    top=[c for c,v in enumerate(grid[0]) if v not in (0,2)];bot=[c for c,v in enumerate(grid[-1]) if v not in (0,2)]
    longer_top=len(top)>len(bot);cols=set(top)&set(bot);rows=range(1,sep) if longer_top else range(sep+1,h-1)
    for r in rows:
        for c in cols:out[r][c]=4
    return out
