def transform(grid):
    h,w=len(grid),len(grid[0]);out=[row[:] for row in grid]
    split_rows=[r for r,row in enumerate(grid) if all(v==5 for v in row)]
    split_cols=[c for c in range(w) if all(grid[r][c]==5 for r in range(h))]
    def intervals(n,s):
        b=[-1]+s+[n];return [(b[i]+1,b[i+1]) for i in range(len(b)-1) if b[i]+1<b[i+1]]
    for r0,r1 in intervals(h,split_rows):
        for c0,c1 in intervals(w,split_cols):
            marker=next(grid[r][c] for r in range(r0,r1) for c in range(c0,c1) if grid[r][c]!=0)
            for r in range(r0,r1):
                for c in range(c0,c1):out[r][c]=marker+5
    return out
