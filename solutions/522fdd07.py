from collections import Counter, deque


def transform(grid):
    h, w = len(grid), len(grid[0]); bg = Counter(v for row in grid for v in row).most_common(1)[0][0]
    out = [[bg]*w for _ in range(h)]; seen=set()
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc]==bg or (sr,sc) in seen: continue
            color=grid[sr][sc]; q=deque([(sr,sc)]);seen.add((sr,sc));cells=[]
            while q:
                r,c=q.popleft();cells.append((r,c))
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr,nc=r+dr,c+dc
                    if 0<=nr<h and 0<=nc<w and grid[nr][nc]==color and (nr,nc) not in seen:
                        seen.add((nr,nc));q.append((nr,nc))
            r0,r1=min(r for r,_ in cells),max(r for r,_ in cells);c0,c1=min(c for _,c in cells),max(c for _,c in cells)
            if r0==r1 and c0==c1:
                for r in range(max(0,r0-4),min(h,r0+5)):
                    for c in range(max(0,c0-4),min(w,c0+5)): out[r][c]=color
            else:
                for r in range(r0+1,r1):
                    for c in range(c0+1,c1): out[r][c]=color
    return out
