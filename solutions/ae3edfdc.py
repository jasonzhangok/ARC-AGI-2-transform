from collections import Counter


def transform(grid):
    h,w=len(grid),len(grid[0]); out=[[0]*w for _ in range(h)]; counts=Counter(v for row in grid for v in row if v)
    centers=[(r,c,grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] and counts[grid[r][c]]==1]
    for r,c,color in centers: out[r][c]=color
    for r,c,v in [(r,c,grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] and counts[grid[r][c]]>1]:
        aligned=[(abs(r-cr)+abs(c-cc),cr,cc) for cr,cc,_ in centers if r==cr or c==cc]
        if not aligned: continue
        _,cr,cc=min(aligned)
        nr=cr+(1 if r>cr else -1 if r<cr else 0); nc=cc+(1 if c>cc else -1 if c<cc else 0)
        out[nr][nc]=v
    return out
