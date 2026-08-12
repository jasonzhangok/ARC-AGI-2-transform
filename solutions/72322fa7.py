from collections import Counter

def transform(grid):
    h,w=len(grid),len(grid[0]);out=[row[:] for row in grid]
    templates=[]
    for r in range(h):
        for c in range(w):
            anchor=grid[r][c]
            if anchor==0:continue
            near=[(dr,dc,grid[r+dr][c+dc]) for dr in (-1,0,1) for dc in (-1,0,1) if (dr or dc) and 0<=r+dr<h and 0<=c+dc<w and grid[r+dr][c+dc] not in (0,anchor)]
            counts=Counter(v for _,_,v in near)
            if counts and counts.most_common(1)[0][1]>=2:
                support=counts.most_common(1)[0][0];offsets=tuple((dr,dc,support) for dr,dc,v in near if v==support)
                templates.append((anchor,offsets))
    unique=[]
    for t in templates:
        if t not in unique:unique.append(t)
    for anchor,offsets in unique:
        original=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==anchor]
        for r,c in original:
            for dr,dc,v in offsets:
                if 0<=r+dr<h and 0<=c+dc<w:out[r+dr][c+dc]=v
        for r in range(h):
            for c in range(w):
                if grid[r][c]==0 and all(0<=r+dr<h and 0<=c+dc<w and grid[r+dr][c+dc]==v for dr,dc,v in offsets):out[r][c]=anchor
    return out
