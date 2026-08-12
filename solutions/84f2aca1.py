def transform(grid):
    out=[row[:] for row in grid];h=len(grid);w=len(grid[0]);seen=set()
    for r in range(h):
        for c in range(w):
            if grid[r][c]==0 or (r,c) in seen:continue
            color=grid[r][c];st=[(r,c)];seen.add((r,c));q=[]
            while st:
                x,y=st.pop();q.append((x,y))
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    p=x+dx,y+dy
                    if 0<=p[0]<h and 0<=p[1]<w and p not in seen and grid[p[0]][p[1]]==color:seen.add(p);st.append(p)
            r0,r1=min(x for x,y in q),max(x for x,y in q);c0,c1=min(y for x,y in q),max(y for x,y in q)
            fill=5 if r1-r0==c1-c0 else 7
            for x in range(r0+1,r1):
                for y in range(c0+1,c1):
                    if out[x][y]==0:out[x][y]=fill
    return out
