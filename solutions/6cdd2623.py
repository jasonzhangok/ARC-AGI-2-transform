def transform(grid):
    h,w=len(grid),len(grid[0]); out=[[0]*w for _ in range(h)]
    choices=[]
    for color in set(v for row in grid for v in row)-{0}:
        hr=[r for r in range(h) if grid[r][0]==grid[r][w-1]==color]
        cs=[c for c in range(w) if grid[0][c]==grid[h-1][c]==color]
        choices.append((len(hr)+len(cs),color,hr,cs))
    _,color,hrs,cs=max(choices)
    for r in hrs:out[r]=[color]*w
    for c in cs:
        for r in range(h):out[r][c]=color
    output = out
    return output
