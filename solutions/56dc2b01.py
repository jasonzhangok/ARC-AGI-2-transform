def transform(grid):
    h,w=len(grid),len(grid[0]);sep_row=next((r for r,row in enumerate(grid) if all(v==2 for v in row)),None)
    sep_col=next((c for c in range(w) if all(grid[r][c]==2 for r in range(h))),None)
    cells=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==3]
    r0,r1=min(r for r,_ in cells),max(r for r,_ in cells);c0,c1=min(c for _,c in cells),max(c for _,c in cells)
    out=[[0]*w for _ in range(h)]
    if sep_row is not None:
        for c in range(w):out[sep_row][c]=2
        dr=(sep_row-1-r1) if r1<sep_row else (sep_row+1-r0)
        for r,c in cells:out[r+dr][c]=3
        border=(r0+dr-1) if r1<sep_row else (r1+dr+1)
        if 0<=border<h:
            for c in range(w):out[border][c]=8
    else:
        for r in range(h):out[r][sep_col]=2
        dc=(sep_col-1-c1) if c1<sep_col else (sep_col+1-c0)
        for r,c in cells:out[r][c+dc]=3
        border=(c0+dc-1) if c1<sep_col else (c1+dc+1)
        if 0<=border<w:
            for r in range(h):out[r][border]=8
    output = out
    return output
