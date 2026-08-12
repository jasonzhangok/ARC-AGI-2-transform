from collections import defaultdict,deque


def transform(grid):
    h,w=len(grid),len(grid[0]);seen=set();groups=defaultdict(list)
    for sr in range(h):
        for sc in range(w):
            if grid[sr][sc]!=1 or (sr,sc) in seen:continue
            q=deque([(sr,sc)]);seen.add((sr,sc));cells=[]
            while q:
                r,c=q.popleft();cells.append((r,c))
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr,nc=r+dr,c+dc
                    if 0<=nr<h and 0<=nc<w and grid[nr][nc]==1 and (nr,nc) not in seen:
                        seen.add((nr,nc));q.append((nr,nc))
            r0=min(r for r,_ in cells);c0=min(c for _,c in cells);mask={(r-r0,c-c0) for r,c in cells};groups[r0].append((c0,mask))
    columns=sorted(c for c,_ in max(groups.values(),key=len));out=[row[:] for row in grid]
    for r0,items in groups.items():
        if len(items)!=1:continue
        existing={c for c,_ in items};mask=items[0][1]
        for c0 in columns:
            if c0 in existing:continue
            for dr,dc in mask:out[r0+dr][c0+dc]=8
    return out
