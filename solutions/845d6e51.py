def _norm(cells):
    r0=min(r for r,c in cells);c0=min(c for r,c in cells)
    return frozenset((r-r0,c-c0) for r,c in cells)


def _variants(cells):
    result=set();cur=set(cells)
    for _ in range(4):
        result.add(_norm(cur));result.add(_norm({(r,-c) for r,c in cur}));cur={(c,-r) for r,c in cur}
    return result


def _components(grid,color,where=lambda r,c:True):
    h,w=len(grid),len(grid[0]);seen=set();result=[]
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=color or not where(r,c) or (r,c) in seen:continue
            st=[(r,c)];seen.add((r,c));q=[]
            while st:
                x,y=st.pop();q.append((x,y))
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    p=x+dx,y+dy
                    if 0<=p[0]<h and 0<=p[1]<w and p not in seen and where(*p) and grid[p[0]][p[1]]==color:seen.add(p);st.append(p)
            result.append(q)
    return result


def transform(grid):
    h,w=len(grid),len(grid[0]);row=max(range(h),key=lambda r:grid[r].count(5));col=max(range(w),key=lambda c:sum(grid[r][c]==5 for r in range(h)))
    refs=[]
    for color in set(v for rr in grid for v in rr)-{0,3,5}:
        for q in _components(grid,color,lambda r,c:r<row and c<col):refs.append((color,_variants(q)))
    targets=_components(grid,3);out=[rr[:] for rr in grid]
    for q in targets:
        shape=_norm(q)
        color=next(color for color,variants in refs if shape in variants)
        for r,c in q:out[r][c]=color
    return out
