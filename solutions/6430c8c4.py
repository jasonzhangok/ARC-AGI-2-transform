def transform(grid):
    split = next(r for r,row in enumerate(grid) if len(set(row))==1 and row[0]==4)
    a=grid[:split]; b=grid[split+1:]
    output = [[3 if a[r][c]==0 and b[r][c]==0 else 0 for c in range(len(grid[0]))] for r in range(split)]
    return output
