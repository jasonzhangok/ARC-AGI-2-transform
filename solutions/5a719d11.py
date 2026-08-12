def transform(grid):
    h,w=len(grid),len(grid[0]);out=[row[:] for row in grid]
    groups=[];r=0
    while r<h:
        if all(v==0 for v in grid[r]):r+=1;continue
        a=r
        while r<h and any(grid[r]):r+=1
        groups.append((a,r))
    sep=next(c for c in range(w) if all(grid[r][c]==0 for a,b in groups for r in range(a,b)))
    for a,b in groups:
        left=[row[:sep] for row in grid[a:b]];right=[row[sep+1:] for row in grid[a:b]]
        lc,rc=left[0][0],right[0][0]
        lm={(r,c) for r,row in enumerate(left) for c,v in enumerate(row) if v!=lc}
        rm={(r,c) for r,row in enumerate(right) for c,v in enumerate(row) if v!=rc}
        for r in range(b-a):
            for c in range(sep):out[a+r][c]=rc if (r,c) in rm else lc
            for c in range(w-sep-1):out[a+r][sep+1+c]=lc if (r,c) in lm else rc
    return out
