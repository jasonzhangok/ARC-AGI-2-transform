def transform(grid):
    out=[row[:] for row in grid]
    for r,row in enumerate(grid):
        for c,v in enumerate(row):
            if v in (2,8):
                height={2:4,8:3}[v]
                for k in range(1,height+1):out[r-k][c]=v if k==height else 1
    return out
