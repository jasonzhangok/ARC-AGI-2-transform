def transform(grid):
    out=[row[:] for row in grid];rows=[r for r,row in enumerate(grid) if row.count(5)>=2]
    cols=[c for c in range(len(grid[0])) if sum(row[c]==5 for row in grid)>=2]
    r0,r1=min(rows),max(rows);c0,c1=min(cols),max(cols)
    colors=[]
    for r in range(r0+1,r1):
        for c in range(c0+1,c1):
            if grid[r][c] not in (0,5) and grid[r][c] not in colors:colors.append(grid[r][c])
    a,b=colors[:2]
    for r in range(r0+1,r1):
        for c in range(c0+1,c1):
            if grid[r][c]==a:out[r][c]=b
            elif grid[r][c]==b:out[r][c]=a
    output = out
    return output
