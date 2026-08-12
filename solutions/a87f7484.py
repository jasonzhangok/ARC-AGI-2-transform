def transform(grid):
    counts={}
    for row in grid:
        for value in row:
            if value!=0:counts[value]=counts.get(value,0)+1
    color=None
    for value in counts:
        if color is None or counts[value]>counts[color]:color=value
    cells=[(r,c) for r,row in enumerate(grid) for c,v in enumerate(row) if v==color]
    r0,r1=min(r for r,_ in cells),max(r for r,_ in cells); c0,c1=min(c for _,c in cells),max(c for _,c in cells)
    output=[row[c0:c1+1] for row in grid[r0:r1+1]]
    return output
