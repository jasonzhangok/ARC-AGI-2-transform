def transform(grid):
    h,w=len(grid),len(grid[0]);color=next(v for row in grid for v in row if v);seen=set();out=[[0]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=color or (r,c) in seen:continue
            st=[(r,c)];seen.add((r,c));cells=[]
            while st:
                x,y=st.pop();cells.append((x,y))
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    p=x+dx,y+dy
                    if 0<=p[0]<h and 0<=p[1]<w and p not in seen and grid[p[0]][p[1]]==color:seen.add(p);st.append(p)
            best=(0,None)
            rs=range(min(x for x,y in cells),max(x for x,y in cells)+1);cs=range(min(y for x,y in cells),max(y for x,y in cells)+1)
            s=set(cells)
            for a in rs:
                for b in range(a,max(rs)+1):
                    for d in cs:
                        for e in range(d,max(cs)+1):
                            area=(b-a+1)*(e-d+1)
                            if area>best[0] and all((x,y) in s for x in range(a,b+1) for y in range(d,e+1)):best=(area,(a,b,d,e))
            if best[0]>=4:
                a,b,d,e=best[1]
                for x in range(a,b+1):
                    for y in range(d,e+1):out[x][y]=color
    return out
