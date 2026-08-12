from collections import Counter

def transform(grid):
    out=[row[:] for row in grid]; h=len(grid); w=len(grid[0])
    seen=set()
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=8 or (r,c) in seen: continue
            stack=[(r,c)]; seen.add((r,c)); cells=[]
            while stack:
                x,y=stack.pop(); cells.append((x,y))
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    q=(x+dx,y+dy)
                    if 0<=q[0]<h and 0<=q[1]<w and q not in seen and grid[q[0]][q[1]]==8:
                        seen.add(q); stack.append(q)
            rs=[x for x,_ in cells]; cs=[y for _,y in cells]; r0,r1=min(rs),max(rs); c0,c1=min(cs),max(cs)
            band=min(r1-r0+1,c1-c0+1)//4
            for x,y in cells:
                if r0+band<=x<=r1-band and c0+band<=y<=c1-band: color=4
                elif x < r0+(r1-r0+1)/2: color=6 if y < c0+(c1-c0+1)/2 else 1
                else: color=2 if y < c0+(c1-c0+1)/2 else 3
                out[x][y]=color
    return out
