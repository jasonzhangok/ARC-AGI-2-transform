def transform(grid):
    h,w=len(grid),len(grid[0]); seen=set(); comps=[]
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=3 or (r,c) in seen: continue
            stack=[(r,c)]; seen.add((r,c)); cells=[]
            while stack:
                x,y=stack.pop(); cells.append((x,y))
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    q=(x+dx,y+dy)
                    if 0<=q[0]<h and 0<=q[1]<w and q not in seen and grid[q[0]][q[1]]==3:
                        seen.add(q); stack.append(q)
            comps.append(cells)
    out=[row[:] for row in grid]
    for target in comps:
        if len(target) > 1:
            for r,c in target: out[r][c]=8
    return out
