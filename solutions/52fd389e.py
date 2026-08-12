from collections import deque


def transform(grid):
    h,w=len(grid),len(grid[0]);out=[row[:] for row in grid];seen=set()
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc]!=4 or (sr,sc) in seen: continue
            q=deque([(sr,sc)]);seen.add((sr,sc));cells=[]
            while q:
                r,c=q.popleft();cells.append((r,c))
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr,nc=r+dr,c+dc
                    if 0<=nr<h and 0<=nc<w and grid[nr][nc]==4 and (nr,nc) not in seen:
                        seen.add((nr,nc));q.append((nr,nc))
            r0,r1=min(r for r,_ in cells),max(r for r,_ in cells);c0,c1=min(c for _,c in cells),max(c for _,c in cells)
            markers=[grid[r][c] for r in range(r0,r1+1) for c in range(c0,c1+1) if grid[r][c] not in (0,4)]
            color=markers[0];t=len(markers)
            for r in range(max(0,r0-t),min(h,r1+t+1)):
                for c in range(max(0,c0-t),min(w,c1+t+1)):
                    if not (r0<=r<=r1 and c0<=c<=c1): out[r][c]=color
    return out
