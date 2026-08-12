def transform(grid):
    h,w=len(grid),len(grid[0])
    row=max((grid[r].count(5),-r,r) for r in range(h))[2]
    col=max((sum(grid[r][c]==5 for r in range(h)),-c,c) for c in range(w))[2]
    components_by_color={}
    for color in set(v for rr in grid for v in rr)-{0,5}:
        for restricted in (True,False):
            seen=set();result=[]
            for r in range(h):
                for c in range(w):
                    allowed=not restricted or r<row and c<col
                    if grid[r][c]!=color or not allowed or (r,c) in seen:continue
                    st=[(r,c)];seen.add((r,c));q=[]
                    while st:
                        x,y=st.pop();q.append((x,y))
                        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            p=x+dx,y+dy
                            neighbor_allowed=not restricted or p[0]<row and p[1]<col
                            if 0<=p[0]<h and 0<=p[1]<w and p not in seen and neighbor_allowed and grid[p[0]][p[1]]==color:seen.add(p);st.append(p)
                    result.append(q)
            components_by_color[color,restricted]=result
    refs=[]
    for color in set(v for rr in grid for v in rr)-{0,3,5}:
        for q in components_by_color.get((color,True),[]):
            variants=set();cur=set(q)
            for _ in range(4):
                for variant in (cur,{(r,-c) for r,c in cur}):
                    r0=min(r for r,c in variant);c0=min(c for r,c in variant)
                    variants.add(frozenset((r-r0,c-c0) for r,c in variant))
                cur={(c,-r) for r,c in cur}
            refs.append((color,variants))
    targets=components_by_color.get((3,False),[]);out=[rr[:] for rr in grid]
    for q in targets:
        r0=min(r for r,c in q);c0=min(c for r,c in q);shape=frozenset((r-r0,c-c0) for r,c in q)
        color=next(color for color,variants in refs if shape in variants)
        for r,c in q:out[r][c]=color
    output=out
    return output
