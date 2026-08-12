def transform(grid):
    h,w=len(grid),len(grid[0]); out=[row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if grid[r][c]==2 and not any(0<=x<h and 0<=y<w and grid[x][y]==2 for x,y in ((r-1,c),(r+1,c),(r,c-1),(r,c+1))): out[r][c]=1
    output = out
    return output
