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
            r0,r1=min(r for r,_ in cells),max(r for r,_ in cells); c0,c1=min(c for _,c in cells),max(c for _,c in cells)
            if len(cells) < (r1-r0+1)*(c1-c0+1): objs.append(((r0+r1)/2,(c0+c1)/2,color))
    vr=max(r for r,_,_ in objs)-min(r for r,_,_ in objs)
    vc=max(c for _,c,_ in objs)-min(c for _,c,_ in objs)
    if vc>=vr:
        objs.sort(key=lambda x:x[1]); out=[[0]*(4*len(objs)) for _ in range(4)]
        for k,(_,_,color) in enumerate(objs):
            for i in range(4):
                for j in range(4): out[i][4*k+j]=color if i in (0,3) or j in (0,3) else 0
    else:
        objs.sort(key=lambda x:x[0]); out=[[0]*4 for _ in range(4*len(objs))]
        for k,(_,_,color) in enumerate(objs):
            for i in range(4):
                for j in range(4): out[4*k+i][j]=color if i in (0,3) or j in (0,3) else 0
    return out
