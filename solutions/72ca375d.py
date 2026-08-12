def transform(grid):
    h,w=len(grid),len(grid[0]);seen=set();comps=[]
    for r in range(h):
        for c in range(w):
            if grid[r][c]==0 or (r,c) in seen:continue
            col=grid[r][c];st=[(r,c)];seen.add((r,c));cells=[]
            while st:
                x,y=st.pop();cells.append((x,y))
                for a,b in ((1,0),(-1,0),(0,1),(0,-1)):
                    q=(x+a,y+b)
                    if 0<=q[0]<h and 0<=q[1]<w and q not in seen and grid[q[0]][q[1]]==col:seen.add(q);st.append(q)
            r0,r1=min(x for x,y in cells),max(x for x,y in cells);c0,c1=min(y for x,y in cells),max(y for x,y in cells);crop=[[grid[x][y] for y in range(c0,c1+1)] for x in range(r0,r1+1)]
            if len(cells)>1 and crop==[row[::-1] for row in crop]:return crop
