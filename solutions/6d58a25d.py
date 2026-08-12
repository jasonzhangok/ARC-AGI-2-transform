from collections import Counter

def transform(grid):
    h,w=len(grid),len(grid[0]);seen=set();comps=[]
    for r in range(h):
        for c in range(w):
            if grid[r][c]==0 or (r,c) in seen:continue
            color=grid[r][c];st=[(r,c)];seen.add((r,c));cells=[]
            while st:
                x,y=st.pop();cells.append((x,y))
                for a in (-1,0,1):
                    for b in (-1,0,1):
                        if a==0 and b==0:continue
                        q=(x+a,y+b)
                        if 0<=q[0]<h and 0<=q[1]<w and q not in seen and grid[q[0]][q[1]]==color:seen.add(q);st.append(q)
            comps.append((len(cells),color,cells))
    _,body,cells=max(comps);r0,r1=min(r for r,c in cells),max(r for r,c in cells);c0,c1=min(c for r,c in cells),max(c for r,c in cells);marker=next(v for v in set(v for row in grid for v in row)-{0,body});cols=sorted({c for r,row in enumerate(grid) for c,v in enumerate(row) if v==marker and r>r1 and c0<c<c1});out=[row[:] for row in grid]
    for c in cols:
        start=next((r for r in range(r0,r1+1) if grid[r][c]!=body and any(grid[r][x]==body for x in range(c0,c)) and any(grid[r][x]==body for x in range(c+1,c1+1))),r1)
        for r in range(start,h):out[r][c]=marker
    return out
