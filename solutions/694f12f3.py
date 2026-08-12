def transform(grid):
    h,w=len(grid),len(grid[0]); out=[row[:] for row in grid]; seen=set(); rects=[]
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=4 or (r,c) in seen: continue
            stack=[(r,c)]; seen.add((r,c)); cells=[]
            while stack:
                x,y=stack.pop(); cells.append((x,y))
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    q=(x+dx,y+dy)
                    if 0<=q[0]<h and 0<=q[1]<w and q not in seen and grid[q[0]][q[1]]==4:
                        seen.add(q); stack.append(q)
            rs=[x for x,_ in cells]; cs=[y for _,y in cells]; rects.append((len(cells),min(rs),max(rs),min(cs),max(cs)))
    rects.sort(reverse=True)
    for i,(_,r0,r1,c0,c1) in enumerate(rects):
        for r in range(r0+1,r1):
            for c in range(c0+1,c1): out[r][c]=2 if i==0 else 1
    return out
