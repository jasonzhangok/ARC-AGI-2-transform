def transform(grid):
    h,w=len(grid),len(grid[0]); out=[row[:] for row in grid]
    marks={(r,c) for r in range(h) for c in range(w) if grid[r][c]==4}
    for r0,c0 in marks:
        for r1,c1 in marks:
            if r1>r0 and c1>c0 and {(r0,c1),(r1,c0)}<=marks:
                for r in range(r0+1,r1):
                    for c in range(c0+1,c1): out[r][c]=2
    output = out
    return output
