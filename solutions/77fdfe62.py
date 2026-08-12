def transform(grid):
    h,w=len(grid),len(grid[0]);corners=(grid[0][0],grid[0][-1],grid[-1][0],grid[-1][-1]);oh,ow=h-4,w-4;out=[]
    for r in range(oh):
        row=[]
        for c in range(ow):
            if grid[r+2][c+2]!=8:row.append(0)
            else:row.append(corners[(2 if r>=oh/2 else 0)+(1 if c>=ow/2 else 0)])
        out.append(row)
    output = out
    return output
