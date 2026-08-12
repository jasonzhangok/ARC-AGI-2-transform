def _components(grid,color):
    h,w=len(grid),len(grid[0]);seen=set();ans=[]
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=color or (r,c) in seen:continue
            st=[(r,c)];seen.add((r,c));cells=[]
            while st:
                x,y=st.pop();cells.append((x,y))
                for a,b in ((1,0),(-1,0),(0,1),(0,-1)):
                    q=(x+a,y+b)
                    if 0<=q[0]<h and 0<=q[1]<w and q not in seen and grid[q[0]][q[1]]==color:seen.add(q);st.append(q)
            ans.append(cells)
    return ans
def _shape(cells):
    r0=min(r for r,c in cells);c0=min(c for r,c in cells);return frozenset((r-r0,c-c0) for r,c in cells)
def transform(grid):
    h,w=len(grid),len(grid[0]);frames=[]
    for cells in _components(grid,5):
        s=set(cells);r0,r1=min(r for r,c in s),max(r for r,c in s);c0,c1=min(c for r,c in s),max(c for r,c in s)
        per={(r,c) for r in range(r0,r1+1) for c in range(c0,c1+1) if r in (r0,r1) or c in (c0,c1)}
        if per<=s:frames.append((r0,r1,c0,c1))
    refs=[]
    for color in set(v for row in grid for v in row)-{0,1,5}:
        for cells in _components(grid,color):
            if any(all(r0<r<r1 and c0<c<c1 for r,c in cells) for r0,r1,c0,c1 in frames):refs.append((_shape(cells),color))
    out=[row[:] for row in grid]
    for cells in _components(grid,1):
        shape=_shape(cells)
        match=next((color for ref,color in refs if ref==shape),None)
        if match is not None:
            for r,c in cells:out[r][c]=match
    return out
