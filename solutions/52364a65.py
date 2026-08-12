from collections import Counter, deque


def transform(grid):
    h,w=len(grid),len(grid[0]);bg=Counter(v for row in grid for v in row).most_common(1)[0][0]
    out=[row[:] for row in grid];seen=set()
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc]==bg or (sr,sc) in seen: continue
            color=grid[sr][sc];q=deque([(sr,sc)]);seen.add((sr,sc));cells=[]
            while q:
                r,c=q.popleft();cells.append((r,c))
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr,nc=r+dr,c+dc
                    if 0<=nr<h and 0<=nc<w and grid[nr][nc]==color and (nr,nc) not in seen:
                        seen.add((nr,nc));q.append((nr,nc))
            left=min(c for _,c in cells)
            for r,c in cells:
                if c<left+2: out[r][c]=bg
    return out
