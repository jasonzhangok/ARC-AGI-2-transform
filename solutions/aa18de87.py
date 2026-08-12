def transform(grid):
    out=[row[:] for row in grid]
    for r,row in enumerate(grid):
        cells=[c for c,v in enumerate(row) if v!=0]
        if len(cells)>=2:
            for c in range(min(cells)+1,max(cells)):
                if out[r][c]==0: out[r][c]=2
    return out
