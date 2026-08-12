def transform(grid):
    h,w=len(grid),len(grid[0]);out=[row[:] for row in grid]
    ones=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==1]
    twos=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==2]
    r,c=min(ones)
    r-=1;c-=1
    while r>=0 and c>=0:out[r][c]=1;r-=1;c-=1
    r,c=max(twos)
    r+=1;c+=1
    while r<h and c<w:out[r][c]=2;r+=1;c+=1
    return out
