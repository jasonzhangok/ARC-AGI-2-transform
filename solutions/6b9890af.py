def transform(grid):
    h,w=len(grid),len(grid[0]); twos=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==2]
    r0,r1=min(r for r,c in twos),max(r for r,c in twos);c0,c1=min(c for r,c in twos),max(c for r,c in twos)
    size=r1-r0+1; small=[(r,c,grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] not in (0,2)]
    sr0=min(r for r,c,v in small);sc0=min(c for r,c,v in small);sr1=max(r for r,c,v in small);sc1=max(c for r,c,v in small)
    pat=[[grid[r][c] for c in range(sc0,sc1+1)] for r in range(sr0,sr1+1)]; scale=(size-2)//len(pat)
    out=[[2]*size for _ in range(size)]
    for r in range(1,size-1):
        for c in range(1,size-1): out[r][c]=pat[(r-1)//scale][(c-1)//scale]
    return out
