from collections import deque


def transform(grid):
    h,w=len(grid),len(grid[0]); seen=set(); objs=[]
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc]==0 or (sr,sc) in seen: continue
            color=grid[sr][sc]; q=deque([(sr,sc)]); seen.add((sr,sc)); cells=[]
            while q:
                r,c=q.popleft(); cells.append((r,c))
                for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if 0<=nr<h and 0<=nc<w and grid[nr][nc]==color and (nr,nc) not in seen:
                        seen.add((nr,nc)); q.append((nr,nc))
            r0,c0=min(r for r,_ in cells),min(c for _,c in cells)
            shape={(r-r0,c-c0) for r,c in cells}
            missing=next((r,c) for r in range(2) for c in range(2) if (r,c) not in shape)
            objs.append((missing,color,shape))
    out=[[0]*4 for _ in range(4)]
    target={(1,1):(0,0),(1,0):(0,1),(0,1):(1,0),(0,0):(1,1)}
    for missing,color,shape in objs:
        band,side=target[missing]
        for r,c in shape: out[band*2+r][side*2+c]=color
    return out
