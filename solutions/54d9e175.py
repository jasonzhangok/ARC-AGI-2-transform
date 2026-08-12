def transform(grid):
    h,w=len(grid),len(grid[0]);out=[row[:] for row in grid]
    split_rows=[r for r,row in enumerate(grid) if all(v==5 for v in row)]
    split_cols=[c for c in range(w) if all(grid[r][c]==5 for r in range(h))]
    row_bounds=[-1]+split_rows+[h]
    row_intervals=[(row_bounds[i]+1,row_bounds[i+1]) for i in range(len(row_bounds)-1) if row_bounds[i]+1<row_bounds[i+1]]
    col_bounds=[-1]+split_cols+[w]
    col_intervals=[(col_bounds[i]+1,col_bounds[i+1]) for i in range(len(col_bounds)-1) if col_bounds[i]+1<col_bounds[i+1]]
    for r0,r1 in row_intervals:
        for c0,c1 in col_intervals:
            marker=next(grid[r][c] for r in range(r0,r1) for c in range(c0,c1) if grid[r][c]!=0)
            for r in range(r0,r1):
                for c in range(c0,c1):out[r][c]=marker+5
    output=out
    return output
