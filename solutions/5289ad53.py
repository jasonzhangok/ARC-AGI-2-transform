from collections import deque


def transform(grid):
    h,w=len(grid),len(grid[0]);counts={3:0,2:0};seen=set()
    for color in (3,2):
        for sr in range(h):
            for sc in range(w):
                if grid[sr][sc]!=color or (sr,sc) in seen: continue
                counts[color]+=1;q=deque([(sr,sc)]);seen.add((sr,sc))
                while q:
                    r,c=q.popleft()
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc=r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]==color and (nr,nc) not in seen:
                            seen.add((nr,nc));q.append((nr,nc))
    values=[3]*counts[3]+[2]*counts[2]+[0]*(6-counts[3]-counts[2])
    return [values[:3],values[3:6]]
