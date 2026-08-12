from collections import Counter


def transform(grid):
    h,w=len(grid),len(grid[0]);sep=next(row[0] for row in grid if len(set(row))==1 and row[0]!=0)
    sr=[r for r,row in enumerate(grid) if all(v==sep for v in row)]
    sc=[c for c in range(w) if all(grid[r][c]==sep for r in range(h))]
    def intervals(n,s):
        b=[-1]+s+[n];return [(b[i]+1,b[i+1]) for i in range(len(b)-1) if b[i]+1<b[i+1]]
    ris,cis=intervals(h,sr),intervals(w,sc)
    colors=Counter(v for row in grid for v in row if v not in (0,sep));template=max(colors,key=colors.get)
    tr=tc=None
    for i,(r0,r1) in enumerate(ris):
        for j,(c0,c1) in enumerate(cis):
            if any(grid[r][c]==template for r in range(r0,r1) for c in range(c0,c1)):tr,tc=i,j
    r0,r1=ris[tr];c0,c1=cis[tc]
    mask={(r-r0,c-c0) for r in range(r0,r1) for c in range(c0,c1) if grid[r][c]==template}
    out=[[0]*w for _ in range(h)]
    for r in sr:
        for c in range(w):out[r][c]=sep
    for c in sc:
        for r in range(h):out[r][c]=sep
    for i,(a,b) in enumerate(ris):
        band=[grid[r][c] for r in range(a,b) for c in range(w) if grid[r][c] not in (0,sep,template)]
        color=Counter(band).most_common(1)[0][0]
        for c0,c1 in cis:
            for dr,dc in mask:out[a+dr][c0+dc]=color
    return out
