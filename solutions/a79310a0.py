def transform(grid):
    h,w=len(grid),len(grid[0]); out=[[0]*w for _ in range(h)]
    for r in range(h-1):
        for c in range(w):
            if grid[r][c]==8: out[r+1][c]=2
    output = out
    return output
