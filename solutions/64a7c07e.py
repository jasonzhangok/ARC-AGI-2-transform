def transform(grid):
    h,w=len(grid),len(grid[0]); out=[[0]*w for _ in range(h)]; seen=set()
    for r in range(h):
        for c in range(w):
            if grid[r][c]==0 or (r,c) in seen: continue
            stack=[(r,c)]; seen.add((r,c)); cells=[]
            while stack:
                x,y=stack.pop(); cells.append((x,y,grid[x][y]))
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    q=(x+dx,y+dy)
                    if 0<=q[0]<h and 0<=q[1]<w and q not in seen and grid[q[0]][q[1]]!=0:
                        seen.add(q); stack.append(q)
            width=max(y for _,y,_ in cells)-min(y for _,y,_ in cells)+1
            for x,y,v in cells: out[x][y+width]=v
    return out
