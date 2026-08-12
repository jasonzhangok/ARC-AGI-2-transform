def transform(grid):
    cells=[(r,c) for r,row in enumerate(grid) for c,v in enumerate(row) if v]
    r0,r1=min(r for r,c in cells),max(r for r,c in cells);c0,c1=min(c for r,c in cells),max(c for r,c in cells)
    mask=[[1 if any(grid[r0+3*r+i][c0+3*c+j] for i in range(3) for j in range(3)) else 0 for c in range(3)] for r in range(3)]
    return [[5 if mask[r//3][c//3] and mask[r%3][c%3] else 0 for c in range(9)] for r in range(9)]
