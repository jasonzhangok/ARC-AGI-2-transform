def transform(grid):
    h,w=len(grid),len(grid[0]);out=[row[:] for row in grid]
    bars={c:grid[0][c] for c in range(w) if grid[0][c] and all(grid[r][c]==grid[0][c] for r in range(h))}
    fallen=set()
    def fall(c):
        if c in fallen or c not in bars:return
        color=bars[c];fallen.add(c)
        for r in range(h):out[r][c]=0
        for x in range(c,min(w,c+h)):out[h-1][x]=color
        if c+h in bars:fall(c+h)
    for c,color in sorted(bars.items()):
        if color==1:fall(c)
    return out
