def transform(grid):
    h,w=len(grid),len(grid[0]); out=[[0]*w for _ in range(h)]
    r,c=next((r,c) for r in range(h) for c in range(w) if grid[r][c]==2)
    for dr,dc,color in ((-1,-1,3),(-1,1,6),(1,-1,8),(1,1,7)):
        nr,nc=r+dr,c+dc
        if 0<=nr<h and 0<=nc<w: out[nr][nc]=color
    output = out
    return output
