def transform(grid):
    h,w=len(grid),len(grid[0])
    runs=[]
    for c in range(w):
        rows=[r for r in range(h) if grid[r][c]==5]
        if rows: runs.append((len(rows),c,rows))
    longest=max(runs); shortest=min(runs)
    out=[[0]*w for _ in range(h)]
    for r in longest[2]: out[r][longest[1]]=1
    for r in shortest[2]: out[r][shortest[1]]=2
    return out
