def transform(grid):
    h,w=len(grid),len(grid[0]); best=None
    fives=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==5]
    for r1,c1 in fives:
        for r2,c2 in fives:
            if r2<=r1 or abs(r2-r1)!=abs(c2-c1): continue
            dc=1 if c2>c1 else -1
            cells=[(r1+k,c1+dc*k) for k in range(1,r2-r1)]
            if cells and all(grid[r][c]==0 for r,c in cells):
                key=(len(cells),-r1,c1)
                if best is None or key>best[0]: best=(key,cells)
    out=[row[:] for row in grid]
    for r,c in (best[1] if best else []): out[r][c]=8
    output = out
    return output
