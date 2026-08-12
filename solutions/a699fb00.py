def transform(grid):
    out=[row[:] for row in grid]
    for r,row in enumerate(grid):
        for c in range(1,len(row)-1):
            if row[c-1:c+2]==[1,0,1]: out[r][c]=2
    return out
