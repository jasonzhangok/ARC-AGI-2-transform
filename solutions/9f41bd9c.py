def transform(grid):
    h,w=len(grid),len(grid[0]); out=[row[:] for row in grid]
    cells=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==5]
    r0,r1=min(r for r,_ in cells),max(r for r,_ in cells); c0,c1=min(c for _,c in cells),max(c for _,c in cells)
    width=c1-c0+1
    for r,c in cells: out[r][c]=1
    from_right=c1==w-1
    last_base=0
    for i,r in enumerate(range(r0,r1+1)):
        base=max(0,i-2) if from_right else w-width-max(0,i-2)
        last_base=base
        for j in range(width):
            if grid[r][c0+j]==5: out[r][base+j]=5
    boundary=next(r for r in range(r1+1,h) if all(v==6 for v in grid[r]))
    if from_right:
        for c in range(last_base+1,w): out[boundary][c]=9
    else:
        for c in range(last_base+width-1): out[boundary][c]=9
    return out
