def transform(grid):
    h,w=len(grid),len(grid[0]);out=[row[:] for row in grid];seen=set()
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc]==0 or (sr,sc) in seen:continue
            color=grid[sr][sc];st=[(sr,sc)];seen.add((sr,sc));cells=[]
            while st:
                r,c=st.pop();cells.append((r,c))
                for a,b in ((1,0),(-1,0),(0,1),(0,-1)):
                    q=(r+a,c+b)
                    if 0<=q[0]<h and 0<=q[1]<w and q not in seen and grid[q[0]][q[1]]==color:seen.add(q);st.append(q)
            r0,r1=min(r for r,c in cells),max(r for r,c in cells);c0,c1=min(c for r,c in cells),max(c for r,c in cells);missing=next((r,c) for r in range(r0,r1+1) for c in range(c0,c1+1) if (r,c) not in cells);dr=-1 if missing[0]==r0 else 1;dc=-1 if missing[1]==c0 else 1;r,c=missing[0]+dr,missing[1]+dc
            while 0<=r<h and 0<=c<w:out[r][c]=color;r+=dr;c+=dc
    return out
