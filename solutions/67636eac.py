def transform(grid):
    h,w=len(grid),len(grid[0]); seen=set(); objs=[]
    for r in range(h):
        for c in range(w):
            if grid[r][c]==0 or (r,c) in seen: continue
            color=grid[r][c]; stack=[(r,c)]; seen.add((r,c)); cells=[]
            while stack:
                x,y=stack.pop(); cells.append((x,y))
                for dx in (-1,0,1):
                  for dy in (-1,0,1):
                    if dx == dy == 0: continue
                    q=(x+dx,y+dy)
                    if 0<=q[0]<h and 0<=q[1]<w and q not in seen and grid[q[0]][q[1]]==color:
                        seen.add(q); stack.append(q)
            r0=min(x for x,_ in cells); r1=max(x for x,_ in cells); c0=min(y for _,y in cells); c1=max(y for _,y in cells)
            crop=[[grid[x][y] for y in range(c0,c1+1)] for x in range(r0,r1+1)]
            objs.append((r0,c0,crop))
    if max(c for _,c,_ in objs)-min(c for _,c,_ in objs) > max(r for r,_,_ in objs)-min(r for r,_,_ in objs):
        objs.sort(key=lambda x:x[1]); return [[v for _,_,g in objs for v in g[r]] for r in range(len(objs[0][2]))]
    objs.sort(key=lambda x:x[0]); return [row for _,_,g in objs for row in g]
