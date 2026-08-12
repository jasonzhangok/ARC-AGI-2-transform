def transform(grid):
    h,w=len(grid),len(grid[0])
    blocks=[(r,c) for r in range(h-1) for c in range(w-1)
            if all(grid[r+i][c+j]==8 for i in range(2) for j in range(2))]
    pieces=[]
    for r in sorted({r for r,_ in blocks}):
        cols=sorted(c for rr,c in blocks if rr==r)
        for left,right in zip(cols[::2],cols[1::2]):
            pieces.extend([grid[r+i][left+2:right] for i in range(2)])
    output = pieces
    return output
