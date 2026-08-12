from collections import deque


def transform(grid):
    h,w=len(grid),len(grid[0]);out=[row[:] for row in grid];seen=set()
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc]!=1 or (sr,sc) in seen: continue
            q=deque([(sr,sc)]);seen.add((sr,sc));cells=[]
            while q:
                r,c=q.popleft();cells.append((r,c))
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr,nc=r+dr,c+dc
                    if 0<=nr<h and 0<=nc<w and grid[nr][nc]==1 and (nr,nc) not in seen:
                        seen.add((nr,nc));q.append((nr,nc))
            r0,r1=min(r for r,_ in cells),max(r for r,_ in cells);c0,c1=min(c for _,c in cells),max(c for _,c in cells)
            for r in range(r0+1,r1):
                for c in range(c0+1,c1):
                    if out[r][c]==0:out[r][c]=8
            for r in range(r0,r1+1):
                for c in (c0,c1):
                    if grid[r][c]==0:
                        for x in (range(0,c+1) if c==c0 else range(c,w)):out[r][x]=8
            for c in range(c0,c1+1):
                for r in (r0,r1):
                    if grid[r][c]==0:
                        for y in (range(0,r+1) if r==r0 else range(r,h)):out[y][c]=8
    return out
