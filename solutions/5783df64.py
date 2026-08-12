def transform(grid):
    h,w=len(grid),len(grid[0]);bh,bw=h//3,w//3;out=[]
    for br in range(3):
        row=[]
        for bc in range(3):
            row.append(next(grid[r][c] for r in range(br*bh,(br+1)*bh) for c in range(bc*bw,(bc+1)*bw) if grid[r][c]!=0))
        out.append(row)
    return out
