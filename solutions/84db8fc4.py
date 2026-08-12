def transform(grid):
    out=[row[:] for row in grid];h=len(grid);w=len(grid[0]);seen=set()
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=0 or (r,c) in seen:continue
            st=[(r,c)];seen.add((r,c));q=[]
            while st:
                x,y=st.pop();q.append((x,y))
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    p=x+dx,y+dy
                    if 0<=p[0]<h and 0<=p[1]<w and p not in seen and grid[p[0]][p[1]]==0:seen.add(p);st.append(p)
            color=2 if any(x in (0,h-1) or y in (0,w-1) for x,y in q) else 5
            for x,y in q:out[x][y]=color
    output = out
    return output
