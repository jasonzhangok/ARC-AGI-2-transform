def transform(grid):
    out=[row[:] for row in grid];r=next(i for i,row in enumerate(grid) if any(row));positions=[c for c,v in enumerate(grid[r]) if v];colors=[grid[r][c] for c in positions];pos=positions[-1];gap=len(colors)-1;i=len(colors)
    while True:
        gap+=1;pos+=gap
        if pos>=len(grid[r]):break
        out[r][pos]=colors[i%len(colors)];i+=1
    return out
